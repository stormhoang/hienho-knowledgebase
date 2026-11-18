#!/usr/bin/env python3
"""INTAKE AGENT - Drop file -> Xu ly -> Push sang hubs-momo (/dashboard).

Luong van hanh:
  1. SCAN     : quet thu muc intake, bo qua da xu ly (idempotency bang sha256)
  2. DETECT   : nhan dien format theo signature registry
  3. PARSE    : goi parser tuong ung -> ghi SSOT local
  4. VALIDATE : kiem tra sanity bound truoc khi push
  5. ROUTE    : map file -> dich (dashboard)
  6. PUSH     : goi build-dashboard-data.py cua hubs-momo
  7. LOG      : ghi push_log.jsonl (nguon, hash, result, thoi gian)

Su dung:
  python3 scripts/intake.py --scan                 # dry-run: xu ly moi file, khong push
  python3 scripts/intake.py --scan --push          # xu ly + push
  python3 scripts/intake.py --file <path> [--push] # xu ly 1 file cu the
  python3 scripts/intake.py --verify               # health check

Drop zone: ~/Downloads/intake/
Quarantine: 13_INTAKE/quarantine/
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"
INTAKE_DIR = os.path.expanduser("~/Downloads/intake")
QUARANTINE_DIR = os.path.join(BASE_DIR, "13_INTAKE/quarantine")
DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS/data")
HASHES_PATH = os.path.join(DATA_DIR, "processed_hashes.json")
LOG_PATH = os.path.join(DATA_DIR, "push_log.jsonl")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intake_parsers import registry, parse_tracking, parse_crawl, parse_backlink  # noqa: E402

# Sanity bounds cho tracking (PV MTD)
TRACKING_PV_MIN = 50_000
TRACKING_PV_MAX = 20_000_000


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_hashes():
    if os.path.exists(HASHES_PATH):
        with open(HASHES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_hashes(hashes):
    os.makedirs(os.path.dirname(HASHES_PATH), exist_ok=True)
    with open(HASHES_PATH, "w", encoding="utf-8") as f:
        json.dump(hashes, f, ensure_ascii=False, indent=2)


def log_event(entry):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    entry["ts"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def notify_mac(title, message):
    try:
        subprocess.run(
            ["osascript", "-e", f'display notification "{message}" with title "{title}"'],
            capture_output=True, timeout=5,
        )
    except Exception:
        pass


def route_for(fmt):
    """Map format -> push targets."""
    if fmt in (registry.TRACKING, registry.CRAWL, registry.BACKLINK):
        return ["dashboard"]
    # Lưu ý: Luồng /board và /bang-tin bên Hub đã xóa hoàn toàn, task list chỉ lưu SSOT local
    return []


def validate_tracking(summary):
    pv = summary.get("actual_mtd_pv", 0)
    if not (TRACKING_PV_MIN <= pv <= TRACKING_PV_MAX):
        return False, f"PV MTD {pv} vuot ngoai sanity bound [{TRACKING_PV_MIN}, {TRACKING_PV_MAX}]"
    days = summary.get("days_elapsed", 0)
    if not (1 <= days <= 31):
        return False, f"days_elapsed {days} khong hop le"
    return True, "ok"


def run_parser(fmt, file_path):
    if fmt == registry.TRACKING:
        return parse_tracking.parse(file_path)
    if fmt == registry.CRAWL:
        return parse_crawl.parse(file_path)
    if fmt == registry.BACKLINK:
        return parse_backlink.parse(file_path)
    raise RuntimeError(f"Khong co parser cho format {fmt}")


def push_to_hubs(targets):
    """Go endpoint co san cua hubs-momo. Tra ve (ok, message)."""
    if not os.path.exists(HUBS_REPO):
        return False, f"Khong tim thay hubs-momo tai {HUBS_REPO}"
    msgs = []
    ok = True
    # Da ngung luong day task sang /bang-tin theo chi dao; chi day so lieu /dashboard
    if "dashboard" in targets:
        build_script = os.path.join(HUBS_REPO, "scripts/build-dashboard-data.py")
        if os.path.exists(build_script):
            res = subprocess.run(
                [sys.executable, build_script, "--base", BASE_DIR],
                capture_output=True, text=True,
            )
            if res.returncode == 0:
                msgs.append("build-dashboard OK")
            else:
                ok = False
                msgs.append(f"build-dashboard FAIL: {res.stderr.strip()[:200]}")
    if "bang-tin" in targets:
        msgs.append("bang-tin push SKIPPED (luong day task da ngung)")
    return ok, "; ".join(msgs) if msgs else "khong co gi de push"


def process_file(file_path, do_push=False):
    """Xu ly 1 file: detect -> parse -> (validate) -> push -> log."""
    digest = sha256_of(file_path)
    hashes = load_hashes()
    name = os.path.basename(file_path)

    if digest in hashes.get("processed", {}):
        print(f"[SKIP] Da xu ly truoc do: {name} (hash {digest[:12]})")
        return {"file": name, "status": "skipped_duplicate"}

    fmt = registry.detect(file_path)
    print(f"[DETECT] {name} -> {fmt}")
    if fmt == registry.UNKNOWN:
        os.makedirs(QUARANTINE_DIR, exist_ok=True)
        dest = os.path.join(QUARANTINE_DIR, name)
        shutil.copy2(file_path, dest)
        print(f"[QUARANTINE] Khong nhan dien duoc format, da copy sang {dest}")
        log_event({"file": name, "hash": digest, "format": "unknown", "status": "quarantine", "push": False})
        return {"file": name, "status": "quarantine"}

    try:
        result = run_parser(fmt, file_path)
    except Exception as e:
        print(f"[PARSE FAIL] {e}")
        log_event({"file": name, "hash": digest, "format": fmt, "status": "parse_fail", "error": str(e)})
        notify_mac("Intake Agent", f"Parse fail: {name}")
        return {"file": name, "status": "parse_fail", "error": str(e)}

    # Validate tracking truoc khi push
    if fmt == registry.TRACKING:
        summary_path = os.path.join(DATA_DIR, "monthly_10_2026_consolidated.json")
        if os.path.exists(summary_path):
            with open(summary_path, "r", encoding="utf-8") as f:
                summary = json.load(f)
            ok_v, msg_v = validate_tracking(summary)
            if not ok_v:
                print(f"[VALIDATE FAIL] {msg_v} - khong push.")
                log_event({"file": name, "hash": digest, "format": fmt, "status": "validate_fail", "error": msg_v})
                notify_mac("Intake Agent", f"Validate fail: {name}")
                return {"file": name, "status": "validate_fail", "error": msg_v}

    targets = route_for(fmt)
    push_ok, push_msg = True, "dry-run (khong push)"
    if do_push:
        push_ok, push_msg = push_to_hubs(targets)
        print(f"[PUSH] {push_msg}")
        if not push_ok:
            notify_mac("Intake Agent", f"Push fail: {name}")

    hashes.setdefault("processed", {})[digest] = {
        "file": name, "format": fmt, "at": datetime.now().isoformat(), "pushed": bool(do_push and push_ok),
    }
    save_hashes(hashes)

    status = "pushed" if (do_push and push_ok) else ("parsed" if not do_push else "push_fail")
    log_event({"file": name, "hash": digest, "format": fmt, "status": status, "push": targets, "push_msg": push_msg, "parse": result})
    if do_push and push_ok:
        notify_mac("Intake Agent", f"Push thanh cong: {name}")
    print(f"[DONE] {name} -> {status}")
    return {"file": name, "status": status, "format": fmt, "push": push_msg}


def scan_intake(do_push=False):
    os.makedirs(INTAKE_DIR, exist_ok=True)
    files = sorted(
        os.path.join(INTAKE_DIR, f)
        for f in os.listdir(INTAKE_DIR)
        if os.path.isfile(os.path.join(INTAKE_DIR, f)) and not f.startswith(".")
    )
    if not files:
        print(f"Khong co file nao trong {INTAKE_DIR}. Drop file vao do roi chay lai.")
        return []
    print(f"Phat hien {len(files)} file trong intake zone.")
    results = []
    for fp in files:
        results.append(process_file(fp, do_push=do_push))
    return results


def verify_health():
    print("=== HEALTH CHECK ===")
    checks = []

    hubs_ok = os.path.exists(HUBS_REPO)
    checks.append(("hubs-momo repo", hubs_ok, HUBS_REPO))

    webdata = os.path.join(HUBS_REPO, "lib/dashboard/web-data.json")
    exists = os.path.exists(webdata)
    fresh = False
    if exists:
        age_h = (datetime.now().timestamp() - os.path.getmtime(webdata)) / 3600
        fresh = age_h < 24 * 7
        checks.append(("web-data.json (dashboard)", exists, f"age {age_h:.1f}h, fresh={fresh}"))
    else:
        checks.append(("web-data.json (dashboard)", exists, webdata))

    intake_exists = os.path.isdir(INTAKE_DIR)
    checks.append(("intake drop zone", intake_exists, INTAKE_DIR))

    ssot = os.path.join(BASE_DIR, "07_REPORTS/web_performance_tracking.xlsx")
    checks.append(("SSOT tracking xlsx", os.path.exists(ssot), ssot))

    hashes = load_hashes()
    n_processed = len(hashes.get("processed", {}))
    checks.append(("processed ledger", True, f"{n_processed} file da xu ly"))

    all_ok = True
    for label, ok, detail in checks:
        mark = "OK" if ok else "FAIL"
        if not ok:
            all_ok = False
        print(f"  [{mark}] {label}: {detail}")
    print(f"Ket qua: {'ALL OK' if all_ok else 'CO LOI'}")
    return all_ok


def main():
    ap = argparse.ArgumentParser(description="Intake Agent: drop file -> push hubs-momo")
    ap.add_argument("--scan", action="store_true", help="Quet intake folder xu ly tat ca file moi")
    ap.add_argument("--file", help="Xu ly 1 file cu the")
    ap.add_argument("--push", action="store_true", help="Thuc te push sang hubs-momo (mac dinh chi dry-run)")
    ap.add_argument("--verify", action="store_true", help="Health check pipeline")
    ap.add_argument("--sync-inventory", action="store_true", help="Gom cum toan bo Inventory va push sang hubs-momo")
    args = ap.parse_args()

    if args.sync_inventory:
        inv_script = os.path.join(BASE_DIR, "scripts", "sync_inventory_to_hubs.py")
        subprocess.run([sys.executable, inv_script], check=True)
        return

    if args.verify:
        verify_health()
        return
    if args.file:
        process_file(args.file, do_push=args.push)
        return

    if args.scan or not (args.verify or args.file):
        scan_intake(do_push=args.push)
        return


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUARD HUB WRITERS - dam bao moi script ghi repo react-web-momo deu co hub_sync_lock
va moi duong push deu qua flag (--push-hubs / --push / hub_push helper).

Bai hoc nguon: dot audit 2026-11-20 phat hien 5 script ghi Hub repo khong lock
(race last-writer-wins) va ingest scripts tung auto-push khong can flag.

Rule:
  FAIL : file trong KNOWN_HUB_WRITERS thieu "hub_sync_lock", hoac file bat ky
         chua git push/push_to_hubs_api ma khong co co --push-hubs/--push.
  WARN : file moi tham chieu react-web-momo/HUBS_REPO, khong nam trong
         KNOWN_HUB_WRITERS/EXEMPT, va co dau hieu ghi (json.dump/open write)
         -> co the la hub writer moi chua lock.

Cach dung:
    ./.venv/bin/python scripts/guard_hub_writers.py            # quet toan bo scripts/
    ./.venv/bin/python scripts/guard_hub_writers.py --staged   # chi file staged (pre-commit)
"""

import re
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = BASE_DIR / "scripts"

HUB_REF_RE = re.compile(r"react-web-momo|HUBS_REPO|hubs-momo")
LOCK_RE = re.compile(r"hub_sync_lock")
PUSH_RE = re.compile(r"git.{0,40}push|push_to_hubs_api|commit_and_push_hub")
PUSH_GATE_RE = re.compile(r"push_hubs|args\.push|do_push|--push")
WRITE_RE = re.compile(r"json\.dump|open\([^)]*[\"'][wa]|shutil\.copy")

# Writer da verify: bat buoc co hub_sync_lock
KNOWN_HUB_WRITERS = {
    "scripts/ingest_ga4_daily.py",
    "scripts/ingest_gsc_mtd.py",
    "scripts/sync_inventory_to_hubs.py",
    "scripts/sync_agent_tasks.py",
    "scripts/sync_seo_news.py",
    "scripts/sync_roadmap_to_supabase.py",
    "scripts/sync_data_to_hubs_dashboard.py",
    "scripts/sync_all_data.py",
    "scripts/sync_tracking_report.py",
    "scripts/intake.py",
}

# File tham chieu Hub repo nhung KHONG can lock (read-only / lib / push bi tat)
EXEMPT = {
    "scripts/lib/hub_sync_lock.py",
    "scripts/lib/hub_push.py",
    "scripts/lib/hubs_dashboard.py",
    "scripts/lib/url_project_resolver.py",
    "scripts/lib/theme_matcher.py",
    "scripts/push_to_hubs_api.py",
    "scripts/normalize_hub_project_names.py",   # --write da tat, chi dry-run
    "scripts/theme_seasonality.py",             # read-only data/seo-clusters
    "scripts/sync_data_mart.py",                # read hub-map, ghi KB sqlite
    "scripts/detect_knowledge_conflicts.py",    # scan text, khong ghi hub
    "scripts/intake.py",                        # da co lock (push_to_hubs)
    "scripts/build_hub_style_slide_demo.py",
    "scripts/build_official_templated_pptx.py",
    "scripts/build_templated_pptx.py",
    "scripts/clean_page_mtd_exports.py",
    "scripts/enrich_geo_entity_data.py",
    "scripts/generate_content_plan.py",
    "scripts/generate_geo_entity_registry.py",
    "scripts/validate_seo_pipeline.py",
    "scripts/route.py",
    "scripts/harness_doctor.py",
    "scripts/guard_hub_writers.py",
}


def rel(path: Path) -> str:
    return str(path.relative_to(BASE_DIR))


def scan_file(path: Path):
    """Tra ve (co_hub_ref, co_lock, co_push, co_push_gate, co_write)."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return (False,) * 5
    return (
        bool(HUB_REF_RE.search(text)),
        bool(LOCK_RE.search(text)),
        bool(PUSH_RE.search(text)),
        bool(PUSH_GATE_RE.search(text)),
        bool(WRITE_RE.search(text)),
    )


def staged_py_files():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True, cwd=str(BASE_DIR),
    )
    files = []
    for line in out.stdout.splitlines():
        p = BASE_DIR / line.strip()
        if (line.strip().startswith("scripts/") and p.suffix == ".py" and p.exists()
                and "archive" not in p.parts):
            files.append(p)
    return files


def all_py_files():
    # bo qua scripts/archive/ - dead code co chu dich, khong enforce
    return [p for p in sorted(SCRIPTS_DIR.rglob("*.py")) if "archive" not in p.parts]


def main():
    staged = "--staged" in sys.argv
    targets = staged_py_files() if staged else all_py_files()
    mode = "staged" if staged else "all"

    fails, warns = [], []

    # 1. KNOWN_HUB_WRITERS luon phai co lock (ke ca khi khong staged - bat drift)
    for rel_path in sorted(KNOWN_HUB_WRITERS):
        p = BASE_DIR / rel_path
        if not p.exists():
            fails.append(f"{rel_path}: KNOWN_HUB_WRITER bi xoa/doi ten - cap nhat guard")
            continue
        has_lock = LOCK_RE.search(p.read_text(encoding="utf-8", errors="ignore"))
        if not has_lock:
            fails.append(f"{rel_path}: hub writer thieu hub_sync_lock")

    # 2. Quet file targets: push khong gate -> FAIL; hub ref + write + ngoai whitelist -> WARN
    for p in targets:
        r = rel(p)
        if r in EXEMPT or r in KNOWN_HUB_WRITERS:
            # van check push gate cho known writers
            pass
        has_ref, has_lock, has_push, has_gate, has_write = scan_file(p)
        if not has_ref:
            continue
        if has_push and not has_gate and r not in EXEMPT:
            fails.append(f"{r}: chua push/push_to_hubs_api nhung khong co co --push-hubs/--push")
        if (has_write and not has_lock and r not in KNOWN_HUB_WRITERS
                and r not in EXEMPT and not r.startswith("scripts/lib/")):
            warns.append(f"{r}: tham chieu Hub repo + co ghi file, khong thay hub_sync_lock - review thu cong")

    for w in warns:
        print(f"  [WARN] {w}")
    if fails:
        for f in fails:
            print(f"  [FAIL] {f}")
        print(f"\nGUARD HUB WRITERS: {len(fails)} FAIL, {len(warns)} WARN ({mode} mode, {len(targets)} files scanned)")
        sys.exit(1)
    print(f"GUARD HUB WRITERS: PASS - {len(warns)} WARN ({mode} mode, {len(targets)} files scanned)")


if __name__ == "__main__":
    main()

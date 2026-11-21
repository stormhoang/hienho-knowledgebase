#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KNOWLEDGE REVIEW - consumer cua KNOWLEDGE_LOG.md (dong vong lap Phase 2).

Doc log append-only -> aggregate TARGET/ACTION -> phat hien pattern lap
(cung file bi FIX/REFACTOR nhieu lan = bug class can guard/skill)
-> join knowledge_freshness.json + knowledge_conflicts.json -> bao cao "diem nong".

Cach dung:
    ./.venv/bin/python scripts/knowledge_review.py            # in markdown ra stdout
    ./.venv/bin/python scripts/knowledge_review.py --write    # ghi 00_HARNESS_CORE/knowledge_review.md
    ./.venv/bin/python scripts/knowledge_review.py --days 14   # chi entry trong N ngay gan nhat
"""

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
LOG_PATH = BASE_DIR / "00_HARNESS_CORE" / "KNOWLEDGE_LOG.md"
FRESHNESS_PATH = BASE_DIR / "00_HARNESS_CORE" / "knowledge_freshness.json"
CONFLICTS_PATH = BASE_DIR / "00_HARNESS_CORE" / "knowledge_conflicts.json"
OUT_PATH = BASE_DIR / "00_HARNESS_CORE" / "knowledge_review.md"

ENTRY_RE = re.compile(r"^\[(\d{4}-\d{2}-\d{2})(?:\s+\d{2}:\d{2})?\]\s*\[([A-Z_ -]+)\]\s*\[([^\]]+)\]\s*(.*)$")
PATH_RE = re.compile(r"(?:scripts|00_HARNESS_CORE|03_SKILLS|04_MOSPARK_PLATFORM|05_HUBS|06_USE_CASE_MOMO|07_REPORTS|14_ROADMAP|\.agents|graphify-out|react-web-momo)/[^\s\],;`+]+")

# Tu khoa can theo doi xuyen suot log (bug class / chu de nong)
WATCH_KEYWORDS = [
    "hub_sync_lock", "push", "stale", "broken", "lock", "ingest", "sync",
    "guard", "registry", "routing", "snapshot", "ai_traffic", "non-paid",
    "truncat", "16kb", "dead", "archive",
]

CHANGE_ACTIONS = {"FIX", "REFACTOR", "BUG", "PATCH", "REPAIR"}


def parse_log(days=None):
    entries = []
    cutoff = None
    if days:
        cutoff = datetime.now().date() - timedelta(days=days)
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        m = ENTRY_RE.match(line.strip())
        if not m:
            continue
        date_s, action, target, summary = m.groups()
        d = datetime.strptime(date_s, "%Y-%m-%d").date()
        if cutoff and d < cutoff:
            continue
        entries.append({
            "date": d, "action": action.strip(), "target": target.strip(),
            "summary": summary.strip(), "raw": line.strip(),
        })
    return entries


def extract_paths(target_str):
    return PATH_RE.findall(target_str)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def build_report(entries):
    out = []
    out.append("# KNOWLEDGE REVIEW (generated)")
    out.append("")
    if not entries:
        out.append("Khong co entry nao trong KNOWLEDGE_LOG.md.")
        return "\n".join(out)

    dates = sorted(e["date"] for e in entries)
    out.append(f"- Entries: **{len(entries)}** | Ky: {dates[0]} -> {dates[-1]}")
    out.append(f"- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    out.append("")

    # 1. Action distribution
    actions = Counter(e["action"] for e in entries)
    out.append("## Hanh dong")
    out.append("")
    out.append("| Action | So luong |")
    out.append("|---|---|")
    for a, n in actions.most_common():
        out.append(f"| {a} | {n} |")
    out.append("")

    # 2. Top targets (file paths xuat hien trong TARGET)
    path_counts = Counter()
    for e in entries:
        for p in extract_paths(e["target"]):
            path_counts[p.rstrip("/.")] += 1
    out.append("## Top targets bi dung nhieu nhat")
    out.append("")
    if path_counts:
        out.append("| Target | So lan |")
        out.append("|---|---|")
        for p, n in path_counts.most_common(10):
            out.append(f"| `{p}` | {n} |")
    else:
        out.append("_Khong extract duoc file path nao (target la mo ta tu do)._")
    out.append("")

    # 3. Recurring fix detection: cung path + action thay doi >= 3
    fix_counts = Counter()
    for e in entries:
        if e["action"] in CHANGE_ACTIONS:
            for p in extract_paths(e["target"]):
                fix_counts[p.rstrip("/.")] += 1
    recurring = [(p, n) for p, n in fix_counts.most_common() if n >= 3]
    out.append("## Pattern lap - ung vien bug class can guard/skill")
    out.append("")
    if recurring:
        out.append("| Target | So lan sua | De xuat |")
        out.append("|---|---|---|")
        for p, n in recurring:
            out.append(f"| `{p}` | {n} | So lai co guard/pre-commit check chua; neu chua -> viet guard nho |")
    else:
        out.append("_Chua co target nao bi sua >= 3 lan trong ky nay._")
    out.append("")

    # 4. Hot keywords trong summaries
    kw_counts = Counter()
    for e in entries:
        low = e["summary"].lower()
        for kw in WATCH_KEYWORDS:
            if kw in low:
                kw_counts[kw] += 1
    out.append("## Chu de nong (keyword trong summary)")
    out.append("")
    if kw_counts:
        out.append(", ".join(f"`{k}` x{n}" for k, n in kw_counts.most_common(12)))
    else:
        out.append("_Khong co._")
    out.append("")

    # 5. Debt join: freshness + conflicts
    out.append("## No ky thuat (join voi generated artifacts)")
    out.append("")
    fresh = load_json(FRESHNESS_PATH)
    if fresh:
        s = fresh.get("summary", {})
        status_counts = Counter(x.get("status", "?") for x in fresh.get("sources", []))
        stale_sources = [x.get("path") for x in fresh.get("sources", [])
                         if x.get("status") == "stale"]
        out.append(f"- freshness: {dict(status_counts)} "
                   f"(generated {fresh.get('generated_at', '?')})")
        for p in stale_sources[:5]:
            out.append(f"  - STALE: `{p}`")
    else:
        out.append("- freshness: khong doc duoc knowledge_freshness.json")

    conf = load_json(CONFLICTS_PATH)
    if conf:
        conflicts = conf.get("conflicts", [])
        by_kind = Counter(c.get("kind") for c in conflicts)
        broken = by_kind.get("broken_reference", 0)
        age_d = None
        try:
            gen = datetime.fromisoformat(str(conf.get("generated_at", "")).replace("Z", "+00:00"))
            age_d = (datetime.now(gen.tzinfo) - gen).days
        except Exception:
            pass
        age_txt = f", age {age_d}d" if age_d is not None else ""
        out.append(f"- conflicts: {conf.get('conflict_count', len(conflicts))} findings "
                   f"({dict(by_kind)}){age_txt} - broken_reference={broken}")
    else:
        out.append("- conflicts: khong doc duoc knowledge_conflicts.json")
    out.append("")

    # 6. Recent entries (10 moi nhat)
    out.append("## Entry gan nhat")
    out.append("")
    for e in entries[-10:]:
        out.append(f"- `{e['date']}` [{e['action']}] [{e['target']}] {e['summary'][:140]}")
    out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Review KNOWLEDGE_LOG -> diem nong knowledge layer")
    ap.add_argument("--write", action="store_true", help="Ghi ra 00_HARNESS_CORE/knowledge_review.md")
    ap.add_argument("--days", type=int, default=None, help="Chi entry trong N ngay gan nhat")
    args = ap.parse_args()

    if not LOG_PATH.exists():
        sys.exit(f"Khong tim thay {LOG_PATH}")
    entries = parse_log(days=args.days)
    report = build_report(entries)

    if args.write:
        OUT_PATH.write_text(report, encoding="utf-8")
        print(f"Da ghi {OUT_PATH}")
    else:
        print(report)


if __name__ == "__main__":
    main()

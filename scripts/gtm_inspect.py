# -*- coding: utf-8 -*-
"""
GTM INSPECT CLI
Tra cứu nhanh GTM container (live version, tags, triggers, variables, folders)
bằng shared client scripts/lib/gtm_client.py.

Thay thế các script ad-hoc scratch/check_gtm_*.py, review_gtm_*.py.

Usage:
  ./.venv/bin/python scripts/gtm_inspect.py                      # tổng quan
  ./.venv/bin/python scripts/gtm_inspect.py --list tags --filter utility
  ./.venv/bin/python scripts/gtm_inspect.py --list triggers --filter click_to_app
  ./.venv/bin/python scripts/gtm_inspect.py --list versions --limit 10
  ./.venv/bin/python scripts/gtm_inspect.py --container inapp --list tags
"""

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.gtm_client import get_client


def _brief_tag(t: dict) -> dict:
    return {
        "tagId": t.get("tagId"),
        "name": t.get("name"),
        "type": t.get("type"),
        "paused": t.get("paused", False),
        "firingTriggerId": t.get("firingTriggerId"),
        "folderId": t.get("folderId"),
    }


def _brief_trigger(t: dict) -> dict:
    return {
        "triggerId": t.get("triggerId"),
        "name": t.get("name"),
        "type": t.get("type"),
        "customEventFilter": [
            {"type": f.get("type"), "parameter": [
                {"key": p.get("key"), "value": p.get("value")} for p in f.get("parameter", [])
            ]} for f in t.get("customEventFilter", [])
        ] or None,
    }


def _brief_var(v: dict) -> dict:
    return {
        "variableId": v.get("variableId"),
        "name": v.get("name"),
        "type": v.get("type"),
        "folderId": v.get("folderId"),
    }


def main():
    ap = argparse.ArgumentParser(description="GTM container inspector")
    ap.add_argument("--container", default="web", choices=["web", "inapp"],
                    help="web=GTM-P9JDDJZ (10104547), inapp=57119568")
    ap.add_argument("--list", dest="kind", default="overview",
                    choices=["overview", "tags", "triggers", "variables", "folders", "versions"])
    ap.add_argument("--filter", help="Lọc theo chuỗi con trong name")
    ap.add_argument("--live", action="store_true", default=True,
                    help="Đọc từ live version (mặc định); workspace dùng --no-live")
    ap.add_argument("--no-live", dest="live", action="store_false")
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--json", action="store_true", help="Output raw JSON")
    args = ap.parse_args()

    c = get_client(args.container)

    if args.kind == "overview":
        lv = c.latest_version()
        print(f"Container: {c.container}")
        print(f"Live version: {lv.get('containerVersionId')} | {lv.get('name')}")
        print(f"Tags={lv.get('numTags')} Triggers={lv.get('numTriggers')} "
              f"Variables={lv.get('numVariables')} Notes={lv.get('numNotes')}")
        print(f"Workspaces: {len(c.list_workspaces())} | Folders: {len(c.list_folders())}")
        return

    if args.kind == "versions":
        for v in c.list_versions(page_size=args.limit):
            print(f"v{v.get('containerVersionId')} | {v.get('name')} | "
                  f"tags={v.get('numTags')} triggers={v.get('numTriggers')}")
        return

    if args.kind == "folders":
        for f in c.list_folders():
            print(f"{f.get('folderId')} | {f.get('name')}")
        return

    if args.kind == "tags":
        items = [_brief_tag(t) for t in c.list_tags(live=args.live)]
    elif args.kind == "triggers":
        items = [_brief_trigger(t) for t in c.list_triggers(live=args.live)]
    else:
        items = [_brief_var(v) for v in c.list_variables(live=args.live)]

    if args.filter:
        f = args.filter.lower()
        items = [i for i in items
                 if f in json.dumps(i, ensure_ascii=False).lower()]

    if args.json:
        print(json.dumps(items[:args.limit], ensure_ascii=False, indent=2))
        return

    for i in items[:args.limit]:
        print(json.dumps(i, ensure_ascii=False))
    print(f"# {len(items)} items", file=sys.stderr)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXECUTABLE FAST ROUTER
Parse 00_HARNESS_CORE/FAST_ROUTING_INDEX.md -> tra cuu SSOT target theo intent.

Cach dung:
    ./.venv/bin/python scripts/route.py "audit url mat impressions"
    ./.venv/bin/python scripts/route.py "top pages gsc" --top 3
    ./.venv/bin/python scripts/route.py --list          # liet ke toan bo routes

Nguyen tac: bang markdown la SSOT duy nhat - script KHONG duplicate du lieu,
chi parse va match. Sua bang trong FAST_ROUTING_INDEX.md la router tu cap nhat.
"""

import argparse
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INDEX_PATH = BASE_DIR / "00_HARNESS_CORE" / "FAST_ROUTING_INDEX.md"

TOKEN_RE = re.compile(r"[0-9a-zA-ZÀ-ỹ]+")
LINK_RE = re.compile(r"\[([^\]]*)\]\((file:///[^)\s]+|[^)\s]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")


def parse_routes():
    """Parse 2 bang routing -> list dict {intent, targets, policy, section}."""
    routes = []
    if not INDEX_PATH.exists():
        return routes
    section = ""
    for line in INDEX_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            section = line.lstrip("#").strip()
            continue
        line = line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        intent_raw, target_raw, policy_raw = cells[0], cells[1], cells[2]
        # bo header/separator
        if set(intent_raw) <= set(":- ") or "Nghiệp vụ" in intent_raw or "Target" in intent_raw and "---" in line:
            continue
        if intent_raw.replace("*", "").replace("-", "").strip() in ("", ":"):
            continue

        intent = re.sub(r"\*\*", "", intent_raw).strip()
        policy = re.sub(r"\*\*", "", policy_raw).strip()

        # targets: uu tien link file:///, fallback code span dang path, skill name
        targets = []
        for text, url in LINK_RE.findall(target_raw):
            targets.append(url.replace("file://", ""))
        if not targets:
            for code in CODE_RE.findall(target_raw):
                if "/" in code or code.endswith((".py", ".md", ".json", ".yaml")):
                    targets.append(code)
        skills = re.findall(r"Skill `([a-z0-9-]+)`", target_raw, re.I)
        for s in skills:
            targets.append(f"skill:{s}")
        if not targets:
            # target dang text tu do (vd 'File code lien quan') -> lay nguyen van rut gon
            targets = [re.sub(r"\*\*", "", target_raw).strip()[:120]]

        routes.append({
            "intent": intent,
            "targets": targets,
            "policy": policy,
            "section": section,
            "raw": intent_raw + " " + target_raw + " " + policy_raw,
        })
    return routes


def tokenize(text):
    return [t.lower() for t in TOKEN_RE.findall(text) if len(t) >= 2]


def score_route(route, query_tokens, query_lower):
    raw_lower = route["raw"].lower()
    score = 0
    # bonus neu nguyen cau query xuat hien trong intent
    if query_lower and query_lower in route["intent"].lower():
        score += 10
    hits = sum(1 for t in set(query_tokens) if t in raw_lower)
    score += hits
    # penalty nhe neu route thuoc bang data ssot nhung query co tinh tu dinh tuyen file
    return score


def main():
    ap = argparse.ArgumentParser(description="Fast routing tra cuu SSOT target theo intent")
    ap.add_argument("query", nargs="?", help="Cau hoi/intent can dinh tuyen")
    ap.add_argument("--top", type=int, default=5, help="So ket qua toi da (mac dinh 5)")
    ap.add_argument("--list", action="store_true", help="Liet ke toan bo routes")
    args = ap.parse_args()

    routes = parse_routes()
    if not routes:
        sys.exit(f"Khong parse duoc route nao tu {INDEX_PATH}")

    if args.list:
        for i, r in enumerate(routes, 1):
            print(f"{i:>2}. {r['intent']}")
            for t in r["targets"]:
                print(f"     -> {t}")
        print(f"\nTong: {len(routes)} routes")
        return

    if not args.query:
        ap.error("can query hoac --list")

    q = args.query.strip().lower()
    qtokens = tokenize(args.query)
    scored = [(score_route(r, qtokens, q), r) for r in routes]
    scored = [(s, r) for s, r in scored if s > 0]
    scored.sort(key=lambda x: -x[0])

    if not scored:
        print(f"Khong match route nao cho: {args.query!r}")
        print("Go y: --list de xem toan bo routes, hoac dien tu khoa khac.")
        return

    print(f"ROUTES cho: {args.query!r}  ({len(scored)} match, top {min(args.top, len(scored))})")
    print("=" * 78)
    for score, r in scored[: args.top]:
        print(f"\n[{score}] {r['intent']}")
        for t in r["targets"]:
            print(f"      target: {t}")
        print(f"      policy: {r['policy'][:160]}")


if __name__ == "__main__":
    main()

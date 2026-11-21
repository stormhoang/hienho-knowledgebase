#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HARNESS DOCTOR - health check cho chinh harness cua repo.

Kiem tra cac lop enforce co con dung khong sau moi dot refactor:
  1. AGENTS.md < 16KB (nguong inject cua Devin harness - file bi truncate se mat rules)
  2. FAST_ROUTING_INDEX.md: moi link file:/// va path `...` trong bang deu ton tai
  3. Skills: moi thu muc .agents/skills/* co SKILL.md
  4. knowledge_registry.yaml hop le (chay validate_knowledge_registry.py)
  5. knowledge_conflicts.json baseline: broken_reference = 0 va file generated con moi
  6. pre-commit hook + .venv ton tai

Cach dung:
    ./.venv/bin/python scripts/harness_doctor.py          # check nhanh
    ./.venv/bin/python scripts/harness_doctor.py --deep   # + chay pytest

Exit code: 1 neu co FAIL (de dung trong CI/manual gate).
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
AGENTS_MAX_BYTES = 16 * 1024  # 16384 - nguong inject thuc te cua harness
STALE_DAYS = 7

LINK_RE = re.compile(r"\((file:///[^)\s]+)\)")
CODE_PATH_RE = re.compile(r"`((?:scripts|07_REPORTS|00_HARNESS_CORE|03_SKILLS|04_MOSPARK_PLATFORM|05_HUBS|06_USE_CASE_MOMO|14_ROADMAP|graphify-out)/[^`\s|)]+)`")


FAILS = []


def check(name, ok, detail=""):
    mark = "OK" if ok else "FAIL"
    line = f"  [{mark}] {name}" + (f": {detail}" if detail else "")
    print(line)
    if not ok:
        FAILS.append(name)
    return ok


def warn(name, detail=""):
    print(f"  [WARN] {name}" + (f": {detail}" if detail else ""))


def check_routing_targets():
    """Moi file:/// link va path trong backtick cua FAST_ROUTING_INDEX phai ton tai."""
    index = BASE_DIR / "00_HARNESS_CORE" / "FAST_ROUTING_INDEX.md"
    if not index.exists():
        return check("FAST_ROUTING_INDEX.md", False, "missing")
    text = index.read_text(encoding="utf-8")
    broken = []
    for m in LINK_RE.finditer(text):
        p = Path(m.group(1).replace("file://", ""))
        if "<" in str(p) or "*" in str(p):
            continue  # placeholder/pattern
        if not p.exists():
            broken.append(str(p))
    for m in CODE_PATH_RE.finditer(text):
        p = BASE_DIR / m.group(1).rstrip("/.")
        raw = m.group(1)
        if any(ch in raw for ch in "<*()"):
            continue
        # path thu muc (vd 05_HUBS/inventory/) -> check dir
        if not p.exists():
            broken.append(raw)
    if broken:
        return check("routing targets", False, f"{len(broken)} broken: {broken[:5]}")
    return check("routing targets", True, "moi link/path trong FAST_ROUTING_INDEX ton tai")


def check_skills():
    skills_dir = BASE_DIR / ".agents" / "skills"
    if not skills_dir.is_dir():
        return check("skills registry", False, ".agents/skills missing")
    missing = [d.name for d in skills_dir.iterdir()
               if d.is_dir() and not (d / "SKILL.md").exists()]
    n = sum(1 for d in skills_dir.iterdir() if d.is_dir())
    if missing:
        return check("skills registry", False, f"{len(missing)}/{n} thieu SKILL.md: {missing[:5]}")
    return check("skills registry", True, f"{n} skills deu co SKILL.md")


def check_registry():
    script = BASE_DIR / "scripts" / "validate_knowledge_registry.py"
    if not script.exists():
        return check("knowledge_registry", False, "validator missing")
    res = subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                         cwd=str(BASE_DIR))
    out = (res.stdout + res.stderr).strip().splitlines()
    tail = out[-1] if out else ""
    return check("knowledge_registry", res.returncode == 0, tail[:120])


def check_conflicts_baseline():
    f = BASE_DIR / "00_HARNESS_CORE" / "knowledge_conflicts.json"
    if not f.exists():
        return check("knowledge_conflicts baseline", False, "chua generate - chay detect_knowledge_conflicts.py")
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        return check("knowledge_conflicts baseline", False, f"json loi: {e}")
    findings = d.get("findings", d if isinstance(d, list) else [])
    broken = [x for x in findings
              if isinstance(x, dict) and x.get("type") == "broken_reference"]
    age_d = (datetime.now().timestamp() - f.stat().st_mtime) / 86400
    if broken:
        return check("knowledge_conflicts baseline", False,
                     f"{len(broken)} broken_reference (baseline=0)")
    if age_d > STALE_DAYS:
        warn("knowledge_conflicts.json", f"generated {age_d:.0f} ngay truoc - chay lai detect_knowledge_conflicts.py")
        return True
    return check("knowledge_conflicts baseline", True, f"0 broken, generated {age_d:.1f} ngay truoc")


def main():
    deep = "--deep" in sys.argv
    print("=== HARNESS DOCTOR ===")
    print(f"Repo: {BASE_DIR}")

    agents = BASE_DIR / "AGENTS.md"
    if agents.exists():
        size = agents.stat().st_size
        check("AGENTS.md size", size < AGENTS_MAX_BYTES,
              f"{size} bytes / nguong {AGENTS_MAX_BYTES} ({'trong vung inject' if size < AGENTS_MAX_BYTES else 'BI TRUNCATE!'})")
    else:
        check("AGENTS.md size", False, "missing")

    check("CLAUDE.md shim", (BASE_DIR / "CLAUDE.md").exists())
    check("FAST_ROUTING_INDEX.md", (BASE_DIR / "00_HARNESS_CORE" / "FAST_ROUTING_INDEX.md").exists())
    check("pre-commit hook", (BASE_DIR / "scripts" / "git-hooks" / "pre-commit").exists())
    check(".venv", (BASE_DIR / ".venv" / "bin" / "python").exists())

    check_routing_targets()
    check_skills()
    check_registry()
    check_conflicts_baseline()

    if deep:
        print("\n  [deep] pytest scripts/tests ...")
        res = subprocess.run([sys.executable, "-m", "pytest", "scripts/tests/", "-x", "-q"],
                             capture_output=True, text=True, cwd=str(BASE_DIR))
        tail = res.stdout.strip().splitlines()
        check("pytest", res.returncode == 0, tail[-1] if tail else "")

    print("=" * 60)
    if FAILS:
        print(f"CO LOI: {len(FAILS)} check FAIL -> {', '.join(FAILS)}")
        sys.exit(1)
    print("ALL OK - harness nguyen ven.")


if __name__ == "__main__":
    main()

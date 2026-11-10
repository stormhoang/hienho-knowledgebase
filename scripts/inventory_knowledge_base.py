#!/usr/bin/env python3
"""Build a read-only inventory of the repository knowledge base."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "00_HARNESS_CORE" / "knowledge_registry.yaml"
DEFAULT_JSON = ROOT / "00_HARNESS_CORE" / "knowledge_inventory.json"
DEFAULT_MD = ROOT / "00_HARNESS_CORE" / "knowledge_inventory.md"
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", "graphify-out", ".claude", ".kilo"}
EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".csv", ".sql", ".py", ".js", ".ts", ".tsx", ".mts"}


def load_registry() -> set[str]:
    try:
        import yaml
        payload = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8")) or {}
        return {entry.get("path") for entry in payload.get("entries", []) if entry.get("path")}
    except Exception:
        return set()


def domain_for(path: Path) -> str:
    parts = path.parts
    if parts[0] == "00_HARNESS_CORE":
        return "agent_governance"
    return parts[0] if parts else "root"


def collect() -> dict:
    registered = load_registry()
    files = []
    unregistered = []
    by_domain = Counter()
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        rel_text = relative.as_posix()
        stat = path.stat()
        record = {
            "path": rel_text,
            "domain": domain_for(relative),
            "type": path.suffix.lower().lstrip("."),
            "bytes": stat.st_size,
            "modified_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            "registered": rel_text in registered,
        }
        files.append(record)
        by_domain[record["domain"]] += 1
        if path.suffix.lower() in {".md", ".yaml", ".yml", ".json"} and rel_text not in registered:
            unregistered.append(rel_text)
    files.sort(key=lambda item: item["path"])
    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "observe",
        "repository": str(ROOT),
        "summary": {
            "total_files": len(files),
            "registered_files": sum(1 for item in files if item["registered"]),
            "unregistered_knowledge_files": len(unregistered),
            "domains": dict(sorted(by_domain.items())),
        },
        "unregistered_knowledge_files": unregistered,
        "files": files,
    }


def render_markdown(payload: dict) -> str:
    summary = payload["summary"]
    lines = [
        "# Knowledge Base Inventory",
        "",
        f"Generated: {payload['generated_at']}",
        "Mode: observe",
        "",
        "## Summary",
        "",
        f"- Total scanned files: {summary['total_files']}",
        f"- Registered files: {summary['registered_files']}",
        f"- Unregistered knowledge files: {summary['unregistered_knowledge_files']}",
        "",
        "## Files by domain",
        "",
        "| Domain | Files |",
        "| --- | ---: |",
    ]
    for domain, count in summary["domains"].items():
        lines.append(f"| {domain} | {count} |")
    lines += ["", "## Interpretation", "", "Unregistered files are candidates for later Registry review. They are not errors and are not modified by this inventory.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory repository knowledge files")
    parser.add_argument("--json-out", default=str(DEFAULT_JSON))
    parser.add_argument("--md-out", default=str(DEFAULT_MD))
    args = parser.parse_args()
    payload = collect()
    Path(args.json_out).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    Path(args.md_out).write_text(render_markdown(payload), encoding="utf-8")
    print(json.dumps(payload["summary"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

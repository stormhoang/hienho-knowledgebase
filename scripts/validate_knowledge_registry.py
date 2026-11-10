#!/usr/bin/env python3
"""Validate the additive Knowledge Registry without changing the knowledge base."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "00_HARNESS_CORE" / "knowledge_registry.yaml"
ALLOWED_STATUS = {"active", "legacy", "deprecated", "draft", "historical", "retired"}
ALLOWED_AUTHORITY = {"primary", "secondary", "reference", "generated"}
REQUIRED = {"id", "path", "domain", "type", "authority", "status", "used_for"}


def validate(registry: dict, today: date | None = None) -> list[str]:
    errors: list[str] = []
    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        return ["entries phải là mảng không rỗng"]

    seen_ids: set[str] = set()
    seen_paths: dict[str, str] = {}
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"Entry {index} không phải object")
            continue
        missing = REQUIRED - entry.keys()
        if missing:
            errors.append(f"Entry {index} thiếu: {', '.join(sorted(missing))}")
            continue
        entry_id = entry["id"]
        path_text = entry["path"]
        if entry_id in seen_ids:
            errors.append(f"Trùng id: {entry_id}")
        seen_ids.add(entry_id)
        if path_text in seen_paths:
            errors.append(f"Trùng path: {path_text} ({seen_paths[path_text]}, {entry_id})")
        seen_paths[path_text] = entry_id
        path = (ROOT / path_text).resolve()
        if not path.is_relative_to(ROOT):
            errors.append(f"Path vượt repository boundary: {path_text}")
        elif not path.is_file():
            errors.append(f"Không tìm thấy source: {path_text}")
        if entry["authority"] not in ALLOWED_AUTHORITY:
            errors.append(f"{entry_id}: authority không hợp lệ")
        if entry["status"] not in ALLOWED_STATUS:
            errors.append(f"{entry_id}: status không hợp lệ")
        if not isinstance(entry["used_for"], list) or not entry["used_for"]:
            errors.append(f"{entry_id}: used_for phải là mảng không rỗng")
        for relation in ("supersedes", "cross_check_with"):
            for target in entry.get(relation, []):
                if target not in {item.get("id") for item in entries if isinstance(item, dict)}:
                    errors.append(f"{entry_id}: {relation} trỏ tới id không tồn tại: {target}")
        freshness = entry.get("freshness_days")
        if freshness is not None and (not isinstance(freshness, int) or freshness <= 0):
            errors.append(f"{entry_id}: freshness_days phải là số nguyên dương")
        gen_script = entry.get("generator_script")
        if gen_script is not None:
            if not isinstance(gen_script, str) or not gen_script.strip():
                errors.append(f"{entry_id}: generator_script phải là chuỗi không rỗng")
            elif gen_script != "manual_authoring":
                script_path = (ROOT / gen_script).resolve()
                if not script_path.is_file():
                    errors.append(f"{entry_id}: generator_script không tìm thấy tệp: {gen_script}")
        sor = entry.get("system_of_record")
        if sor is not None and (not isinstance(sor, str) or not sor.strip()):
            errors.append(f"{entry_id}: system_of_record phải là chuỗi không rỗng")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate additive Knowledge Registry")
    parser.add_argument("--registry", default=str(REGISTRY))
    args = parser.parse_args()
    try:
        import yaml
        payload = yaml.safe_load(Path(args.registry).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Không đọc được Registry: {exc}")
        return 1
    errors = validate(payload)
    if errors:
        print("Knowledge Registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Knowledge Registry valid: {len(payload['entries'])} entries, mode={payload.get('mode', 'unknown')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

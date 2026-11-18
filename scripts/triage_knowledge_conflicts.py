#!/usr/bin/env python3
"""Classify Knowledge Base conflicts without changing source documents."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "00_HARNESS_CORE" / "knowledge_conflicts.json"
DEFAULT_JSON = ROOT / "00_HARNESS_CORE" / "knowledge_conflict_triage.json"
DEFAULT_YAML = ROOT / "00_HARNESS_CORE" / "knowledge_conflict_triage.yaml"


def classify(conflict: dict) -> dict:
    reference = conflict.get("reference", "")
    if conflict.get("kind") == "skill_asset_reference":
        category = "skill_asset_review"
        action = "verify_skill_package_base"
        confidence = "low"
    elif conflict.get("kind") == "code_path_reference":
        category = "code_path_review"
        action = "verify_input_or_generated_output"
        confidence = "low"
    elif conflict.get("kind") == "external_reference":
        category = "external_reference"
        action = "review_repository_boundary"
        confidence = "high"
    elif reference.startswith("Base/"):
        target = reference.removeprefix("Base/")
        category = "path_alias" if (ROOT / target).exists() else "missing_source"
        action = "review_alias_target" if category == "path_alias" else "identify_source_owner"
        confidence = "high" if category == "path_alias" else "medium"
    elif reference.startswith("08_PRD/") and (ROOT / reference.replace("08_PRD/", "09_PRD/", 1)).exists():
        category = "path_alias"
        action = "review_alias_target"
        confidence = "high"
    elif reference.startswith("../") or reference.startswith("Idea/"):
        category = "external_reference"
        action = "review_repository_boundary"
        confidence = "high"
    elif "/data/" in reference or reference.endswith(".json") or reference.endswith(".csv"):
        category = "missing_source"
        action = "identify_generator_or_mark_legacy"
        confidence = "medium"
    else:
        category = "broken_internal_reference"
        action = "manual_source_review"
        confidence = "low"
    return {
        "reference": reference,
        "sources": conflict.get("sources", []),
        "original_kind": conflict.get("kind"),
        "line": conflict.get("line"),
        "raw_reference": conflict.get("raw_reference", reference),
        "reason": conflict.get("reason"),
        "category": category,
        "proposed_action": action,
        "confidence": confidence,
        "status": "pending_review",
        "do_not_edit_source": True,
    }


def yaml_scalar(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    return json.dumps(value, ensure_ascii=False)


def render_yaml(payload: dict) -> str:
    lines = [
        f"version: {yaml_scalar(payload['version'])}",
        f"generated_at: {yaml_scalar(payload['generated_at'])}",
        f"mode: {yaml_scalar(payload['mode'])}",
        f"resolved: {yaml_scalar(payload['resolved'])}",
        "items:",
    ]
    for item in payload["items"]:
        lines.append(f"  - reference: {yaml_scalar(item['reference'])}")
        lines.append(f"    category: {yaml_scalar(item['category'])}")
        lines.append(f"    proposed_action: {yaml_scalar(item['proposed_action'])}")
        lines.append(f"    confidence: {yaml_scalar(item['confidence'])}")
        lines.append(f"    status: {yaml_scalar(item['status'])}")
        lines.append(f"    line: {yaml_scalar(item.get('line'))}")
        lines.append(f"    raw_reference: {yaml_scalar(item.get('raw_reference'))}")
        lines.append(f"    reason: {yaml_scalar(item.get('reason'))}")
        lines.append(f"    do_not_edit_source: {yaml_scalar(item['do_not_edit_source'])}")
        lines.append("    sources:")
        for source in item["sources"]:
            lines.append(f"      - {yaml_scalar(source)}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Triage Knowledge Base conflicts")
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--json-output", default=str(DEFAULT_JSON))
    parser.add_argument("--yaml-output", default=str(DEFAULT_YAML))
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    items = [classify(conflict) for conflict in source.get("conflicts", [])]
    payload = {
        "version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "observe",
        "resolved": False,
        "items": items,
    }
    Path(args.json_output).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    Path(args.yaml_output).write_text(render_yaml(payload), encoding="utf-8")
    counts = {}
    for item in items:
        counts[item["category"]] = counts.get(item["category"], 0) + 1
    print(json.dumps({"total": len(items), "categories": counts}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

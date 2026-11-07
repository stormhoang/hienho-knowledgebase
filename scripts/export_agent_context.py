#!/usr/bin/env python3
"""Xuất manifest ngữ cảnh chỉ đọc cho Agent (Claude, Antigravity) tích hợp độ mới và nguồn gốc tri thức (Provenance).

SSOT Script: scripts/export_agent_context.py
Domain: 00_HARNESS_CORE / Knowledge Governance
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

REGISTRY_PATH = ROOT / "00_HARNESS_CORE" / "knowledge_registry.yaml"
FRESHNESS_JSON_PATH = ROOT / "00_HARNESS_CORE" / "knowledge_freshness.json"
PROVENANCE_JSON_PATH = ROOT / "00_HARNESS_CORE" / "knowledge_provenance.json"


def get_freshness_data(registry_path: Path, reference_date: date | None = None, force_refresh: bool = False) -> dict[str, Any]:
    """Lấy dữ liệu độ mới từ cache JSON hoặc quét trực tiếp."""
    if not force_refresh and FRESHNESS_JSON_PATH.is_file() and reference_date is None:
        try:
            return json.loads(FRESHNESS_JSON_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass

    from scripts.check_knowledge_freshness import scan_registry_freshness
    return scan_registry_freshness(registry_path, reference_date)


def get_provenance_data(registry_path: Path, force_refresh: bool = False) -> dict[str, Any]:
    """Lấy dữ liệu nguồn gốc và mã checksum từ cache JSON hoặc sinh trực tiếp."""
    if not force_refresh and PROVENANCE_JSON_PATH.is_file():
        try:
            return json.loads(PROVENANCE_JSON_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass

    from scripts.generate_knowledge_provenance import generate_provenance
    return generate_provenance(registry_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export read-only Agent context manifest with freshness and provenance governance")
    parser.add_argument("--domain", help="Filter by domain")
    parser.add_argument("--as-of-date", help="Reference date YYYY-MM-DD for freshness check")
    parser.add_argument("--refresh-freshness", action="store_true", help="Force refresh of freshness evaluation")
    parser.add_argument("--refresh-provenance", action="store_true", help="Force refresh of provenance checksums")
    args = parser.parse_args()

    import yaml

    if not REGISTRY_PATH.is_file():
        print(f"Lỗi: Không tìm thấy registry tại {REGISTRY_PATH}", file=sys.stderr)
        return 1

    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    entries = registry.get("entries", [])

    ref_date: date | None = None
    if args.as_of_date:
        try:
            from scripts.check_knowledge_freshness import parse_date_str
            ref_date = parse_date_str(args.as_of_date)
        except Exception:
            pass

    freshness_payload = get_freshness_data(REGISTRY_PATH, ref_date, args.refresh_freshness)
    freshness_by_id: dict[str, dict[str, Any]] = {
        item["id"]: item for item in freshness_payload.get("sources", [])
    }

    provenance_payload = get_provenance_data(REGISTRY_PATH, args.refresh_provenance)
    provenance_by_id: dict[str, dict[str, Any]] = {
        item["id"]: item for item in provenance_payload.get("sources", [])
    }

    if args.domain:
        entries = [entry for entry in entries if entry.get("domain") == args.domain]

    sources_output: list[dict[str, Any]] = []
    domain_warnings: list[str] = []

    for entry in entries:
        eid = entry["id"]
        f_meta = freshness_by_id.get(eid, {})
        p_meta = provenance_by_id.get(eid, {})
        
        source_item: dict[str, Any] = {
            "id": eid,
            "path": entry["path"],
            "domain": entry["domain"],
            "type": entry["type"],
            "authority": entry["authority"],
            "status": entry["status"],
            "owner": entry.get("owner", "Web Platform"),
            "used_for": entry["used_for"],
        }

        # Bổ sung provenance metadata
        source_item["provenance"] = {
            "system_of_record": entry.get("system_of_record", p_meta.get("system_of_record", "Unknown")),
            "generator_script": entry.get("generator_script", p_meta.get("generator_script", "manual_authoring")),
            "sha256": p_meta.get("sha256"),
            "content_length_bytes": p_meta.get("content_length_bytes"),
            "verified_at": p_meta.get("verified_at"),
        }

        # Bổ sung freshness metadata
        if f_meta:
            source_item["freshness"] = {
                "status": f_meta.get("status", "unknown"),
                "data_as_of": f_meta.get("data_as_of"),
                "data_period": f_meta.get("data_period"),
                "age_days": f_meta.get("age_days"),
                "freshness_threshold_days": f_meta.get("freshness_threshold_days"),
                "file_modified_at": f_meta.get("file_modified_at"),
                "mtime_drift_days": f_meta.get("mtime_drift_days", 0),
            }
            if f_meta.get("warning"):
                source_item["freshness"]["warning"] = f_meta["warning"]
                domain_warnings.append(f_meta["warning"])
            if f_meta.get("drift_notice"):
                source_item["freshness"]["drift_notice"] = f_meta["drift_notice"]

        sources_output.append(source_item)

    payload = {
        "registry_version": str(registry.get("version", "unknown")),
        "mode": registry.get("mode", "observe"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reference_date": freshness_payload.get("reference_date", date.today().isoformat()),
        "repository": str(ROOT),
        "read_only": True,
        "domain_filter": args.domain or "all",
        "provenance_summary": {
            "total_sources": len(sources_output),
            "verified_count": sum(1 for s in sources_output if s.get("provenance", {}).get("sha256")),
            "checksum_algorithm": "sha256",
        },
        "freshness_summary": {
            "total_sources": len(sources_output),
            "fresh": sum(1 for s in sources_output if s.get("freshness", {}).get("status") == "fresh"),
            "stale": sum(1 for s in sources_output if s.get("freshness", {}).get("status") == "stale"),
            "lag_reconciled": sum(1 for s in sources_output if s.get("freshness", {}).get("status") == "lag_reconciled"),
            "normative": sum(1 for s in sources_output if s.get("freshness", {}).get("status") == "normative"),
            "historical": sum(1 for s in sources_output if s.get("freshness", {}).get("status") == "historical"),
        },
        "freshness_warnings": domain_warnings,
        "sources": sources_output,
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

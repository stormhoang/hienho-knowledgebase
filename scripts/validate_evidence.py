#!/usr/bin/env python3
"""Validate grounded answer evidence records before an Agent states conclusions."""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TYPES = {"fact", "inference", "recommendation"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
REQUIRED_FIELDS = {"id", "claim", "source", "period", "evidence_type", "confidence"}


def validate(payload: dict, max_age_days: int | None = None, today: date | None = None) -> list[str]:
    errors = []
    today = today or date.today()
    if not payload.get("as_of"):
        errors.append("Thiếu as_of")
    claims = payload.get("claims")
    if not isinstance(claims, list) or not claims:
        return ["claims phải là mảng không rỗng"]

    if payload.get("as_of"):
        try:
            age = (today - date.fromisoformat(payload["as_of"])).days
            if age < 0:
                errors.append("as_of nằm trong tương lai")
            if max_age_days is not None and age > max_age_days:
                errors.append(f"Evidence stale: {age} ngày, ngưỡng {max_age_days} ngày")
        except ValueError:
            errors.append("as_of không đúng định dạng YYYY-MM-DD")

    seen = defaultdict(list)
    by_id = {c.get("id"): c for c in claims if isinstance(c, dict)}
    for index, claim in enumerate(claims, start=1):
        missing = REQUIRED_FIELDS - claim.keys()
        if missing:
            errors.append(f"Claim {index} thiếu: {', '.join(sorted(missing))}")
            continue
        source = claim["source"]
        if not (str(source).startswith("http://") or str(source).startswith("https://")):
            source_path = (ROOT / source).resolve()
            if not source_path.is_relative_to(ROOT) or not source_path.is_file():
                errors.append(f"Claim {claim['id']}: không tìm thấy source {source}")
            elif claim["evidence_type"] == "fact" and source_path.suffix == ".json":
                field = claim.get("source_field")
                if not field:
                    errors.append(f"Claim {claim['id']}: JSON fact thiếu source_field")
                else:
                    try:
                        actual = json.loads(source_path.read_text(encoding="utf-8"))
                        for part in field.split("."):
                            actual = actual[int(part)] if isinstance(actual, list) else actual[part]
                        if type(actual) is not type(claim.get("value")) or actual != claim.get("value"):
                            errors.append(f"Claim {claim['id']}: value {claim.get('value')!r} khác source_field {actual!r}")
                        snapshot_days = json.loads(source_path.read_text(encoding="utf-8")).get("days_elapsed")
                        match = re.search(r"monthly_(\d{2})_(\d{4})_mtd_(\d+)d\.json$", source_path.name)
                        if match and snapshot_days is not None:
                            month, year, filename_days = map(int, match.groups())
                            expected = f"{year:04d}-{month:02d}-01/{year:04d}-{month:02d}-{snapshot_days:02d}"
                            if int(filename_days) != snapshot_days or claim["period"] != expected:
                                errors.append(f"Claim {claim['id']}: period hoặc tên snapshot không khớp {expected}")
                    except (ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
                        errors.append(f"Claim {claim['id']}: không đọc được source_field {field}: {exc}")
        if claim["evidence_type"] not in ALLOWED_TYPES:
            errors.append(f"Claim {claim['id']}: evidence_type không hợp lệ")
        if claim["confidence"] not in ALLOWED_CONFIDENCE:
            errors.append(f"Claim {claim['id']}: confidence không hợp lệ")
        if claim["evidence_type"] == "fact" and "value" not in claim:
            errors.append(f"Claim {claim['id']}: fact phải có value")
        metric_key = (claim.get("metric"), claim["period"], claim.get("unit"))
        if claim.get("metric") is not None:
            seen[metric_key].append(claim)

        calculation = claim.get("calculation")
        if calculation:
            if calculation.get("operator") != "subtract" or len(calculation.get("inputs", [])) != 2:
                errors.append(f"Claim {claim['id']}: calculation không được hỗ trợ")
            else:
                try:
                    left, right = (by_id[key]["value"] for key in calculation["inputs"])
                    if left - right != claim.get("value"):
                        errors.append(f"Claim {claim['id']}: phép trừ không khớp")
                except (KeyError, TypeError):
                    errors.append(f"Claim {claim['id']}: thiếu claim đầu vào")

    for key, same_metric_claims in seen.items():
        values = {json.dumps(c.get("value"), sort_keys=True) for c in same_metric_claims if "value" in c}
        if len(values) > 1:
            ids = ", ".join(c["id"] for c in same_metric_claims)
            errors.append(f"Conflict metric {key}: claims {ids} có value khác nhau")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agent evidence JSON")
    parser.add_argument("file", nargs="?", default="-", help="Đường dẫn evidence JSON hoặc - để đọc stdin")
    parser.add_argument("--max-age-days", type=int, help="Ngưỡng stale tùy capability")
    args = parser.parse_args()
    try:
        payload = json.load(sys.stdin) if args.file == "-" else json.loads(Path(args.file).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Không đọc được evidence file: {exc}")
        return 1
    errors = validate(payload, args.max_age_days)
    if errors:
        print("Evidence validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Evidence valid: {len(payload['claims'])} claims, as_of={payload['as_of']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

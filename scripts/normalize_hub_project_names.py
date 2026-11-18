#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHUẨN HÓA TÊN PROJECT TRONG WEB HUBS
Nguồn BigQuery/Excel có lúc trả tên project khác nhau chỉ ở hoa/thường
("Phạt Nguội" / "Phạt nguội", "Vay Nhanh" / "Vay nhanh"...), khiến dashboard
tách thành 2 dòng: một dòng giữ lịch sử, một dòng giữ số tháng hiện tại.

Script này gộp các biến thể về tên chính thức khai báo trong hub-map.json,
cộng dồn số liệu theo từng tháng/kênh rồi ghi lại web-data.json.

Cách dùng:
    ./.venv/bin/python scripts/normalize_hub_project_names.py            # dry-run
    ./.venv/bin/python scripts/normalize_hub_project_names.py --write    # ghi file
"""

import argparse
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
if not HUBS_REPO.exists():
    HUBS_REPO = Path("/Users/hienhv/Klaus/Web-Idea/react-web-momo")

WEB_DATA = HUBS_REPO / "lib" / "dashboard" / "web-data.json"
HUB_MAP = HUBS_REPO / "lib" / "dashboard" / "hub-map.json"


def load_canon(hub_map_path: Path) -> dict:
    hub_map = json.loads(hub_map_path.read_text(encoding="utf-8"))
    return {p.strip().lower(): p.strip() for h in hub_map["hubs"] for p in h["projects"]}


def merge_matrix(rows, n_months, n_channels):
    out = [[0] * n_channels for _ in range(n_months)]
    for row in rows:
        for m in range(min(n_months, len(row))):
            for c in range(min(n_channels, len(row[m]))):
                out[m][c] += row[m][c] or 0
    return out


def main():
    parser = argparse.ArgumentParser(description="Gộp biến thể hoa/thường của tên project trong web-data.json")
    parser.add_argument("--write", action="store_true", help="Ghi đè web-data.json (mặc định chỉ dry-run)")
    args = parser.parse_args()

    canon = load_canon(HUB_MAP)
    data = json.loads(WEB_DATA.read_text(encoding="utf-8"))
    months = data["months"]
    projects = data.get("projects", [])

    grouped = {}
    renamed = []
    for p in projects:
        raw = (p.get("name") or "").strip()
        if not raw:
            continue
        name = canon.get(raw.lower(), raw)
        if name != raw:
            renamed.append(f"{raw} -> {name}")
        slot = grouped.setdefault(name, {"name": name, "hub": p.get("hub", "others"), "rows": []})
        slot["rows"].append(p)

    merged = []
    for name, slot in grouped.items():
        rows = slot["rows"]
        merged.append({
            **{k: v for k, v in rows[0].items() if k not in ("full", "mtd")},
            "name": name,
            "full": merge_matrix([r.get("full", []) for r in rows], len(months), 5),
            "mtd": merge_matrix([r.get("mtd", []) for r in rows], len(months), 5),
        })

    collided = {n: s["rows"] for n, s in grouped.items() if len(s["rows"]) > 1}

    print(f"Projects trước: {len(projects)} | sau khi gộp: {len(merged)}")
    if renamed:
        print("Đã chuẩn hóa tên:")
        for r in sorted(set(renamed)):
            print(f"  {r}")
    if collided:
        print("Đã gộp dòng trùng:")
        for name, rows in collided.items():
            print(f"  {name}: {len(rows)} dòng -> 1")
    if not renamed and not collided:
        print("Không có biến thể tên project nào cần xử lý.")

    if args.write:
        # build-dashboard-data.py đã gộp tên project không phân biệt hoa/thường và là writer duy nhất.
        print("--write đã tắt: chạy scripts/build-dashboard-data.py trong repo Hubs để dựng lại web-data.json.")
    else:
        print("Dry-run: chưa ghi file. Thêm --write để áp dụng.")


if __name__ == "__main__":
    main()

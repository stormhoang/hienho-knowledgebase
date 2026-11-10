#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC DATA TO HUBS DASHBOARD
Đồng bộ toàn bộ bảng ánh xạ, chỉ số GA4 và GSC của Nhóm Tài Chính (Financial Hub)
và Nhóm Tiện Ích Giao Thông (Vehicle Hub) sang Web Hubs Dashboard (/dashboard).

Cập nhật các tệp đích:
1. react-web-momo/lib/dashboard/summary.json
2. react-web-momo/lib/dashboard/web-data.json (enrich.gsc, hubTargets, projects)
3. react-web-momo/data/analytics/ga4-w2a-attribution.json (top_landing_pages)
4. react-web-momo/lib/dashboard/hub-map.json
5. Đẩy sang GitHub Hubs (main) qua REST API
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
if not HUBS_REPO.exists():
    HUBS_REPO = Path("/Users/hienhv/Klaus/Web-Idea/react-web-momo")

sys.path.insert(0, str(BASE_DIR))
import scripts.lib.url_project_resolver as upr

def main():
    parser = argparse.ArgumentParser(description="Đồng bộ dữ liệu sang Hubs /dashboard.")
    parser.add_argument("--push-hubs", action="store_true", default=False, help="Cho phép đẩy lên GitHub Hubs qua REST API")
    args = parser.parse_args()

    print("=" * 70)
    print("BẮT ĐẦU ĐỒNG BỘ DỮ LIỆU SANG HUBS /DASHBOARD")
    print("=" * 70)

    # 1. Nạp url_project_mapping.json SSOT
    mapping_path = BASE_DIR / "07_REPORTS" / "data" / "url_project_mapping.json"
    with open(mapping_path, "r", encoding="utf-8") as f:
        mapping_data = json.load(f)

    url_lookup = {}
    for item in mapping_data.get("mapping", []):
        u = item["url"].replace("https://www.momo.vn", "").replace("https://momo.vn", "").rstrip("/") or "/"
        url_lookup[u] = item

    rules = upr.load_rules()

    def primary_project(path):
        """Project chính của path: ưu tiên mapping SSOT, thiếu thì tra DIM. Không lấy projects[0] (thứ tự chữ cái)."""
        item = url_lookup.get(path)
        if item and item.get("projects"):
            return item.get("primary") or upr.resolve_primary("https://www.momo.vn" + path, rules) or item["projects"][0]
        return upr.resolve_primary("https://www.momo.vn" + path, rules)

    # 2. Nạp GA4 multichannel cache MTD 24d
    ga4_path = BASE_DIR / "07_REPORTS" / "data" / "ga4_multichannel_cache_2026-10-01_2026-10-24.json"
    with open(ga4_path, "r", encoding="utf-8") as f:
        ga4_data = json.load(f)

    def channel_to_idx(ch):
        c = ch.lower()
        if "organic" in c: return 0
        if "paid" in c or "ads" in c: return 1
        if "direct" in c: return 2
        if "referral" in c: return 3
        return 4

    project_channels = defaultdict(lambda: [0, 0, 0, 0, 0])
    page_metrics = defaultdict(lambda: {"pv": 0, "sessions": 0, "channels": [0, 0, 0, 0, 0]})

    for row in ga4_data.get("landing_page_channels", []):
        lp = row["dimensionValues"][0]["value"]
        ch = row["dimensionValues"][1]["value"]
        pv = int(row["metricValues"][0]["value"])
        ses = int(row["metricValues"][1]["value"])
        clean = lp.split("?")[0].rstrip("/") or "/"

        proj = primary_project(clean)
        if not proj:
            continue

        c_idx = channel_to_idx(ch)
        project_channels[proj][c_idx] += pv
        page_metrics[clean]["pv"] += pv
        page_metrics[clean]["sessions"] += ses
        page_metrics[clean]["channels"][c_idx] += pv

    # 3. Nạp GSC 30d cache
    gsc_path = BASE_DIR / "07_REPORTS" / "data" / "cache" / "gsc_30d_cache.json"
    with open(gsc_path, "r", encoding="utf-8") as f:
        gsc_list = json.load(f)

    page_gsc = defaultdict(lambda: {"clicks": 0, "impressions": 0, "pos_w": 0.0})
    for row in gsc_list:
        u = row["keys"][0]
        p = u.replace("https://www.momo.vn", "").replace("https://momo.vn", "").rstrip("/") or "/"
        page_gsc[p]["clicks"] += row.get("clicks", 0)
        page_gsc[p]["impressions"] += row.get("impressions", 0)
        page_gsc[p]["pos_w"] += row.get("position", 0.0) * row.get("impressions", 0)

    # 4. Cập nhật hub-map.json
    print("[1/5] Cập nhật danh mục dự án trong hub-map.json...")
    hub_map_path = HUBS_REPO / "lib" / "dashboard" / "hub-map.json"
    with open(hub_map_path, "r", encoding="utf-8") as f:
        hub_map = json.load(f)

    for h in hub_map["hubs"]:
        if h["id"] == "vehicle":
            existing = set(h["projects"])
            for add_p in ["Giá xăng", "Cây xăng", "Trạm sạc"]:
                if add_p not in existing:
                    h["projects"].append(add_p)
        elif h["id"] == "financial":
            existing = set(h["projects"])
            for add_p in ["Quỹ"]:
                if add_p not in existing:
                    h["projects"].append(add_p)

    with open(hub_map_path, "w", encoding="utf-8") as f:
        json.dump(hub_map, f, ensure_ascii=False, indent=2)
    print("  ✓ Đã cập nhật hub-map.json")

    # 5-6. summary.json và web-data.json (enrich, hubTargets, projects) không ghi ở đây nữa:
    # build-dashboard-data.py là writer duy nhất, dữ liệu lấy từ Excel SSOT và targets trong KB.
    print("[2-3/5] Bỏ qua summary.json / web-data.json: dùng build-dashboard-data.py")

    # 7. Cập nhật ga4-w2a-attribution.json
    print("[4/5] Cập nhật ga4-w2a-attribution.json với Top Landing Pages...")
    w2a_path = HUBS_REPO / "data" / "analytics" / "ga4-w2a-attribution.json"
    with open(w2a_path, "r", encoding="utf-8") as f:
        w2a_data = json.load(f)

    # Xây dựng danh sách top landing pages theo project
    proj_to_lps = defaultdict(list)
    for path, metrics in page_metrics.items():
        proj = primary_project(path)
        if not proj:
            continue

        proj_to_lps[proj].append({
            "path": path,
            "clicks": metrics["pv"], # Proxy clicks/views
            "pv": metrics["pv"],
            "sessions": metrics["sessions"],
            "organic_pv": metrics["channels"][0]
        })

    for p_attr in w2a_data.get("projects_attribution", []):
        pname = p_attr["project_name"]
        if pname in proj_to_lps:
            top_lps = sorted(proj_to_lps[pname], key=lambda x: x["pv"], reverse=True)[:10]
            # Giữ format chuẩn
            p_attr["top_landing_pages"] = [
                {"path": lp["path"], "clicks": lp["clicks"]}
                for lp in top_lps
            ]

    with open(w2a_path, "w", encoding="utf-8") as f:
        json.dump(w2a_data, f, ensure_ascii=False, indent=2)
    with open(BASE_DIR / "07_REPORTS" / "data" / "analytics" / "ga4_w2a_attribution.json", "w", encoding="utf-8") as f:
        json.dump(w2a_data, f, ensure_ascii=False, indent=2)
    print("  ✓ Đã cập nhật ga4-w2a-attribution.json")

    # 8. Đẩy lên GitHub Hubs qua REST API (Mặc định không đẩy trừ khi có --push-hubs)
    if args.push_hubs:
        print("[5/5] Tự động commit và đẩy dữ liệu lên GitHub Hubs qua REST API (--push-hubs)...")
        push_script = BASE_DIR / "scripts" / "push_to_hubs_api.py"
        if push_script.exists():
            res = subprocess.run([
                sys.executable, str(push_script),
                "--commit-local",
                "--message", "feat: sync financial and vehicle hub breakdown and GSC metrics to dashboard"
            ], capture_output=True, text=True)
            print(res.stdout)
            if res.stderr:
                print(res.stderr)
    else:
        print("[5/5] Mặc định an toàn (No-Push): Bỏ qua đẩy GitHub Hubs.")

    print("=" * 70)
    print("ĐỒNG BỘ THÀNH CÔNG DỮ LIỆU SANG /DASHBOARD TRÊN HUBS!")
    print("=" * 70)

if __name__ == "__main__":
    main()

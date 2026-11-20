#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLEAN PAGE MTD EXPORTS (SSOT: SPEC-page-mtd.md)
Tạo page_mtd.json (schema_version 2) từ các file export CSV THỰC TẾ của GA4 và GSC.
TUYỆT ĐỐI KHÔNG GỌI API GA4/GSC. KHÔNG ĐỌC LẠI PAGE_MTD.JSON CŨ LÀM ĐẦU VÀO.

Tuân thủ nghiêm ngặt 10 bước clean trong SPEC-page-mtd.md:
1. Path: bỏ domain, query string, #, trailing slash. Gom trùng path.
2. Hostname: chỉ giữ www.momo.vn.
3. Dòng tổng và (other): bỏ dòng tổng, đưa (other) vào coverage.
4. Kênh: gộp Session default channel group về 5 kênh (organic, paid, direct, referral, others).
5. GSC: tính position gia quyền theo impression; ghi clicks_prev, impressions_prev, position_prev.
   - Trang không có impression kỳ trước: impressions_prev = 0, position_prev = None.
   - Trang không có trong GSC: BỎ HẲN các trường GSC, không ghi 0.
6. Độ phủ GSC: ghi coverage.gsc_pages và coverage.gsc_clicks.
7. project: chuẩn hóa theo url_project_resolver SSOT.
8. Giữ dòng: giữ mọi URL hợp lệ để dashboard rollup tổng, kênh và dự án.
9. Năm trước: pv_ly, pv_prev_ly (0 nếu chưa có năm trước; bỏ trường nếu không có export năm trước).
10. Tự kiểm tra checks: sum_pv vs ga4_pv từ export #4. Lệch quá 1% thì KHÔNG ghi đè, báo lỗi 4 số.
    Kiểm tra có ít nhất một trang có impressions_prev.
"""

import os
import sys
import csv
import json
import argparse
from datetime import datetime
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR / "scripts" / "lib"))
import url_project_resolver as upr

DATA_DIR = BASE_DIR / "07_REPORTS" / "data"
ANALYTICS_DIR = DATA_DIR / "analytics"
GSC_DIR = DATA_DIR / "gsc_exports"

OUT_FILE = ANALYTICS_DIR / "page_mtd.json"
HUB_OUT_FILE = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/analytics/page_mtd.json")

# File mặc định chuẩn trên đĩa
DEFAULT_F1 = ANALYTICS_DIR / "ga4_explore_page_channel_2026-11-01_19.csv"
DEFAULT_F2 = ANALYTICS_DIR / "ga4_explore_page_ly_2025-11-01_19.csv"
DEFAULT_F3 = GSC_DIR / "gsc_pages_compare_2026-11-01_16.csv"
DEFAULT_F4 = ANALYTICS_DIR / "ga4_report_views_mtd_19d.csv"

CHANNEL_ORDER = ["organic", "paid", "direct", "referral", "others"]

def map_channel(ch_raw: str) -> str:
    ch = (ch_raw or "").strip()
    if ch in ["Organic Search", "organic"]:
        return "organic"
    elif ch.startswith("Paid") or ch in ["Display", "Cross-network", "paid"]:
        return "paid"
    elif ch in ["Direct", "direct"]:
        return "direct"
    elif ch in ["Referral", "referral", "App Referral"]:
        return "referral"
    else:
        return "others"

def normalize_path(raw_url: str) -> str:
    p = (raw_url or "").replace("https://www.momo.vn", "").replace("https://momo.vn", "").replace("http://www.momo.vn", "").replace("http://momo.vn", "")
    p = p.split("?")[0].split("#")[0].strip()
    if not p.startswith("/"):
        p = "/" + p
    if len(p) > 1 and p.endswith("/"):
        p = p.rstrip("/")
    return p

def clean_and_build(ga4_export_1, ga4_export_2, gsc_export_3, ga4_totals_4, export_date=None):
    print("=" * 70)
    print("BẮT ĐẦU CLEAN EXPORTS VÀ XUẤT PAGE_MTD.JSON V2 (NO-API, RAW CSV ONLY)")
    print("=" * 70)

    f1_path = Path(ga4_export_1 or DEFAULT_F1)
    f2_path = Path(ga4_export_2 or DEFAULT_F2)
    f3_path = Path(gsc_export_3 or DEFAULT_F3)
    f4_path = Path(ga4_totals_4 or DEFAULT_F4)

    # Kiểm tra sự tồn tại của các file export
    for label, fp in [("File #1 (GA4 Explore Channel)", f1_path),
                      ("File #2 (GA4 Explore LY)", f2_path),
                      ("File #3 (GSC Compare)", f3_path),
                      ("File #4 (GA4 Report Views)", f4_path)]:
        if not fp.exists():
            print(f"❌ Không tìm thấy {label}: {fp}")
            sys.exit(1)
        print(f"📄 Nạp {label}: {fp.name} ({fp.stat().st_size:,} bytes)")

    # 1. BƯỚC 10 (Chuẩn bị): Đọc File #4 lấy ga4_pv và ga4_pv_prev cho checks (KHÔNG GÕ CỨNG)
    ga4_pv = 0
    ga4_pv_prev = 0
    with open(f4_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 2 or row[0].startswith("#"):
                continue
            txt = ",".join(row).lower()
            if "prev" in txt or "previous" in txt or "oct" in txt:
                try:
                    ga4_pv_prev = int(row[-1])
                except ValueError:
                    pass
            elif "mtd" in txt or "period" in txt or "nov" in txt:
                try:
                    ga4_pv = int(row[-1])
                except ValueError:
                    pass

    if ga4_pv <= 0 or ga4_pv_prev <= 0:
        print(f"❌ Không thể đọc ga4_pv và ga4_pv_prev từ File #4: ga4_pv={ga4_pv}, ga4_pv_prev={ga4_pv_prev}")
        sys.exit(1)
    print(f"🎯 Target kiểm tra từ File #4: ga4_pv={ga4_pv:,} | ga4_pv_prev={ga4_pv_prev:,}")

    # 2. Đọc File #1: GA4 Explore (Page path + Channel)
    print("-> Đang xử lý File #1 (Page path + Channels)...")
    pages_raw = defaultdict(lambda: {
        "pv": 0, "pv_prev": 0,
        "channels": defaultdict(lambda: [0, 0])
    })
    ga4_other_pv = 0
    ga4_other_pv_prev = 0

    with open(f1_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].startswith("#") or len(row) < 3:
                continue
            # Bỏ dòng header
            if row[0].strip() in ["Page path", "Page path and screen class", "path"]:
                continue
            
            raw_path = row[0].strip()
            ch_raw = row[1].strip()
            
            try:
                v_curr = int(row[2].replace(",", ""))
                v_prev = int(row[3].replace(",", "")) if len(row) > 3 else 0
            except ValueError:
                continue

            path = normalize_path(raw_path)
            # Bước 3: (other)
            if path == "/(other)" or "(other)" in raw_path:
                ga4_other_pv += v_curr
                ga4_other_pv_prev += v_prev
                continue

            ch = map_channel(ch_raw)
            pages_raw[path]["pv"] += v_curr
            pages_raw[path]["pv_prev"] += v_prev
            pages_raw[path]["channels"][ch][0] += v_curr
            pages_raw[path]["channels"][ch][1] += v_prev

    print(f"   Đã đọc {len(pages_raw):,} unique paths từ File #1 | other_pv: {ga4_other_pv:,}, other_pv_prev: {ga4_other_pv_prev:,}")

    # 3. Đọc File #2: GA4 Explore LY (Năm trước)
    print("-> Đang xử lý File #2 (Cùng kỳ năm trước)...")
    pages_ly = defaultdict(lambda: [0, 0])
    with open(f2_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].startswith("#") or len(row) < 2:
                continue
            if row[0].strip() in ["Page path", "path"]:
                continue
            path = normalize_path(row[0].strip())
            try:
                ly_curr = int(row[1].replace(",", ""))
                ly_prev = int(row[2].replace(",", "")) if len(row) > 2 else 0
                pages_ly[path] = [ly_curr, ly_prev]
            except ValueError:
                continue
    print(f"   Đã đọc {len(pages_ly):,} paths có số năm trước từ File #2")

    # 4. Đọc File #3: GSC Compare (Top pages, Clicks, Clicks_prev, Impressions, Impressions_prev, Position, Position_prev)
    print("-> Đang xử lý File #3 (GSC Comparison)...")
    gsc_data = {}
    gsc_has_prev_count = 0

    with open(f3_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Chuẩn hóa tên cột
        field_map = {}
        for col in reader.fieldnames:
            c_low = col.lower().strip()
            if "top pages" in c_low or "page" in c_low: field_map["url"] = col
            elif "clicks (previous)" in c_low or "clicks_prev" in c_low: field_map["clicks_prev"] = col
            elif "clicks" in c_low: field_map["clicks"] = col
            elif "impressions (previous)" in c_low or "impressions_prev" in c_low: field_map["imp_prev"] = col
            elif "impressions" in c_low: field_map["imp"] = col
            elif "position (previous)" in c_low or "position_prev" in c_low: field_map["pos_prev"] = col
            elif "position" in c_low: field_map["pos"] = col

        for r in reader:
            raw_url = r.get(field_map.get("url", "Top pages"), "")
            if not raw_url:
                continue
            
            path = normalize_path(raw_url)
            try:
                c = int(r.get(field_map.get("clicks", "Clicks"), 0) or 0)
                imp = int(r.get(field_map.get("imp", "Impressions"), 0) or 0)
                pos = float(r.get(field_map.get("pos", "Position"), 0) or 0.0)
            except ValueError:
                continue

            c_prev_raw = r.get(field_map.get("clicks_prev", "Clicks (previous)"))
            imp_prev_raw = r.get(field_map.get("imp_prev", "Impressions (previous)"))
            pos_prev_raw = r.get(field_map.get("pos_prev", "Position (previous)"))

            c_prev = int(c_prev_raw or 0) if c_prev_raw not in [None, ""] else 0
            imp_prev = int(imp_prev_raw or 0) if imp_prev_raw not in [None, ""] else 0
            pos_prev = float(pos_prev_raw) if pos_prev_raw not in [None, ""] else None

            if imp_prev > 0:
                gsc_has_prev_count += 1

            if path not in gsc_data:
                gsc_data[path] = {
                    "clicks": 0, "clicks_prev": 0,
                    "impressions": 0, "impressions_prev": 0,
                    "pos_weighted": 0.0, "pos_prev_weighted": 0.0
                }

            gsc_data[path]["clicks"] += c
            gsc_data[path]["clicks_prev"] += c_prev
            gsc_data[path]["impressions"] += imp
            gsc_data[path]["impressions_prev"] += imp_prev
            gsc_data[path]["pos_weighted"] += pos * imp
            if pos_prev is not None and imp_prev > 0:
                gsc_data[path]["pos_prev_weighted"] += pos_prev * imp_prev

    print(f"   Đã đọc {len(gsc_data):,} GSC paths từ File #3 (Số trang có impressions_prev: {gsc_has_prev_count:,})")

    # Kiểm tra điều kiện bắt buộc: có ít nhất 1 trang có impressions_prev
    if gsc_has_prev_count == 0:
        print("❌ LỖI: Không tìm thấy bất kỳ trang nào có impressions_prev trong File #3!")
        sys.exit(1)

    # 5. Phân giải Project và Xây dựng cấu trúc Pages
    print("-> Đang phân giải Project và làm sạch từng URL theo 10 bước...")
    rules = upr.load_rules()
    inferred = upr.load_inferred_rules(rules)

    cleaned_pages = []
    gsc_pages_count = 0
    gsc_clicks_sum = 0
    sum_pv = 0
    sum_pv_prev = 0

    for path, d in pages_raw.items():
        pv = d["pv"]
        pv_prev = d["pv_prev"]
        sum_pv += pv
        sum_pv_prev += pv_prev

        # Chuẩn hóa Channels
        clean_channels = {}
        for ch in CHANNEL_ORDER:
            pair = d["channels"].get(ch, [0, 0])
            if pair[0] > 0 or pair[1] > 0:
                clean_channels[ch] = [pair[0], pair[1]]

        # Phân giải Project SSOT
        full_url = "https://www.momo.vn" + path
        res = upr.resolve(full_url, rules, inferred)
        proj = res.get("primary") or "Others"

        row = {
            "path": path,
            "project": proj,
            "pv": pv,
            "pv_prev": pv_prev,
            "channels": clean_channels
        }

        # GSC Data
        if path in gsc_data:
            g = gsc_data[path]
            row["clicks"] = g["clicks"]
            row["impressions"] = g["impressions"]
            row["position"] = round(g["pos_weighted"] / g["impressions"], 1) if g["impressions"] > 0 else 0.0

            # Ghi kỳ trước: clicks_prev, impressions_prev, position_prev
            row["clicks_prev"] = g["clicks_prev"]
            row["impressions_prev"] = g["impressions_prev"]
            if g["impressions_prev"] > 0:
                row["position_prev"] = round(g["pos_prev_weighted"] / g["impressions_prev"], 1)
            else:
                row["position_prev"] = None

            gsc_pages_count += 1
            gsc_clicks_sum += g["clicks"]
        # Lưu ý: Trang không có trong GSC thì BỎ HẲN các trường GSC (không ghi 0)

        # LY Data (Năm trước)
        if path in pages_ly:
            ly_vals = pages_ly[path]
            row["pv_ly"] = ly_vals[0]
            row["pv_prev_ly"] = ly_vals[1]

        cleaned_pages.append(row)

    # Sắp xếp trang theo PV giảm dần
    cleaned_pages.sort(key=lambda x: x["pv"], reverse=True)

    # 6. Kiểm tra an toàn checks (ngưỡng 1%)
    total_pv_calculated = sum_pv + ga4_other_pv
    total_pv_prev_calculated = sum_pv_prev + ga4_other_pv_prev

    diff_pv = abs(total_pv_calculated - ga4_pv) / ga4_pv * 100
    diff_pv_prev = abs(total_pv_prev_calculated - ga4_pv_prev) / ga4_pv_prev * 100

    print("=" * 50)
    print("KẾT QUẢ KIỂM TRA BỐN SỐ (CHECKS):")
    print(f"  - ga4_pv (Export #4):      {ga4_pv:,}")
    print(f"  - sum_pv (Tổng trang):     {total_pv_calculated:,} (Khác biệt: {diff_pv:.2f}%)")
    print(f"  - ga4_pv_prev (Export #4): {ga4_pv_prev:,}")
    print(f"  - sum_pv_prev (Tổng trang):{total_pv_prev_calculated:,} (Khác biệt: {diff_pv_prev:.2f}%)")
    print("=" * 50)

    if diff_pv > 1.0 or diff_pv_prev > 1.0:
        print(f"❌ LỖI VƯỢT NGƯỠNG AN TOÀN 1%: Không ghi đè file cũ!")
        print(f"   Bốn số: ga4_pv={ga4_pv}, sum_pv={total_pv_calculated}, ga4_pv_prev={ga4_pv_prev}, sum_pv_prev={total_pv_prev_calculated}")
        sys.exit(1)

    # 7. Xây dựng cấu trúc JSON cuối cùng
    exported_at_str = export_date or datetime.now().strftime("%Y-%m-%d")
    source_files = [f1_path.name, f2_path.name, f3_path.name, f4_path.name]

    out_data = {
        "schema_version": 2,
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "period": {"start": "2026-11-01", "end": "2026-11-19"},
        "prev_period": {"start": "2026-10-01", "end": "2026-10-19"},
        "gsc_period": {"start": "2026-11-01", "end": "2026-11-16"},
        "gsc_prev_period": {"start": "2026-10-01", "end": "2026-10-16"},
        "ly_period": {"start": "2025-11-01", "end": "2025-11-19"},
        "ly_prev_period": {"start": "2025-10-01", "end": "2025-10-19"},
        "source": {
            "method": "manual_export",
            "exported_at": exported_at_str,
            "files": source_files
        },
        "coverage": {
            "ga4_other_pv": ga4_other_pv,
            "ga4_other_pv_prev": ga4_other_pv_prev,
            "gsc_pages": gsc_pages_count,
            "gsc_clicks": gsc_clicks_sum
        },
        "checks": {
            "ga4_pv": ga4_pv,
            "ga4_pv_prev": ga4_pv_prev,
            "sum_pv": total_pv_calculated,
            "sum_pv_prev": total_pv_prev_calculated
        },
        "pages": cleaned_pages
    }

    # Ghi vào KB
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi thành công vào KB: {OUT_FILE}")

    # Đồng bộ sang Hub Dashboard
    if HUB_OUT_FILE.parent.exists():
        with open(HUB_OUT_FILE, "w", encoding="utf-8") as f:
            json.dump(out_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã đồng bộ sang Hub Dashboard: {HUB_OUT_FILE}")

    print("=" * 70)
    print(f"HOÀN TẤT THỰC THI: {len(cleaned_pages):,} trang được làm sạch.")
    print(f"  - Số trang có GSC so sánh: {gsc_pages_count:,}")
    print(f"  - Số trang có impressions_prev: {gsc_has_prev_count:,}")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean manual exports to page_mtd.json v2")
    parser.add_argument("--f1", help="File export 1 (GA4 Explore Free form: pagePath + channel)")
    parser.add_argument("--f2", help="File export 2 (GA4 Explore Free form LY: 1 year ago)")
    parser.add_argument("--f3", help="File export 3 (GSC Performance tab Pages comparison)")
    parser.add_argument("--f4", help="File export 4 (GA4 Reports total views)")
    parser.add_argument("--date", help="Ngày export (YYYY-MM-DD)")
    args = parser.parse_args()

    clean_and_build(args.f1, args.f2, args.f3, args.f4, args.date)

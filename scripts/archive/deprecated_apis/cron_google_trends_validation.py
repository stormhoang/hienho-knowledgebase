#!/usr/bin/env python3
"""
Cron Script: Google Trends Validation for Top Keywords
Mục đích:
1. Sample top keywords từ Inventory (toàn bộ hoặc theo Sector / Theme chỉ định).
2. Query Pytrends để get interest over time, interest by region, related queries.
3. Validate xem keywords có trend thực sự không.
4. Xuất / Cập nhật (Upsert) báo cáo sang 07_REPORTS/data/google_trends_validation.json.
"""

import os
import sys
import json
import csv
import glob
import time
import random
import argparse
from datetime import datetime

def clean_val(val):
    if not val:
        return ""
    val = val.strip()
    if val.startswith('="') and val.endswith('"'):
        return val[2:-1]
    return val

def parse_args():
    parser = argparse.ArgumentParser(description="Google Trends Validation for Inventory Keywords")
    parser.add_argument("--sector", default=None, help="Lọc theo Sector (vd: Financial, Lottery, vehicle-hub...)")
    parser.add_argument("--themes", default=None, help="Danh sách Theme (tên file CSV ko cần đuôi, cách nhau bởi dấu phẩy, vd: gia-vang,ty-gia,vay-tin-chap)")
    parser.add_argument("--kws-per-theme", type=int, default=2, help="Số từ khóa top volume lấy cho mỗi Theme (mặc định: 2)")
    parser.add_argument("--top-n", type=int, default=None, help="Số lượng keywords tối đa cần phân tích (mặc định: 200)")
    parser.add_argument("--delay", type=float, default=3.0, help="Thời gian chờ (giây) giữa các batch (mặc định: 3.0s)")
    parser.add_argument("--no-upsert", action="store_true", help="Ghi đè hoàn toàn file json thay vì cập nhật (upsert)")
    return parser.parse_args()

def main():
    args = parse_args()
    print("=== BẮT ĐẦU GOOGLE TRENDS VALIDATION ===")
    if args.sector:
        print(f"[INFO] Lọc theo Sector: {args.sector}")
    if args.themes:
        print(f"[INFO] Lọc theo Themes: {args.themes}")

    inventory_dir = os.path.join(os.path.dirname(__file__), "..", "05_HUBS", "inventory")
    target_themes = [t.strip().lower() for t in args.themes.split(",")] if args.themes else None

    # Thu thập keywords theo cấu trúc
    candidates = [] # list of dict: {keyword, volume, sector, theme}

    if not os.path.exists(inventory_dir):
        print(f"[ERROR] Không tìm thấy thư mục: {inventory_dir}")
        sys.exit(1)

    sectors = [args.sector] if args.sector else os.listdir(inventory_dir)

    for sec in sectors:
        sec_dir = os.path.join(inventory_dir, sec)
        if not os.path.isdir(sec_dir):
            continue

        csv_files = glob.glob(os.path.join(sec_dir, "*.csv"))
        for csv_file in csv_files:
            file_basename = os.path.splitext(os.path.basename(csv_file))[0].lower()
            if target_themes and file_basename not in target_themes:
                continue

            theme_kws = {}
            try:
                with open(csv_file, "r", encoding="utf-8-sig", errors="replace") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        kw_raw = clean_val(row.get("Keyword", ""))
                        if not kw_raw:
                            continue
                        vol_str = clean_val(row.get("Volume", "0"))
                        try:
                            vol = int(vol_str) if vol_str else 0
                        except ValueError:
                            vol = 0

                        kw = kw_raw.lower().strip()
                        if kw and vol > 0:
                            # Tránh từ khóa lặp lại hoặc lỗi chính tả thô thiển giống hệt
                            if kw not in theme_kws or vol > theme_kws[kw]:
                                theme_kws[kw] = vol
            except Exception as e:
                print(f"[WARNING] Không thể đọc {csv_file}: {e}")

            # Sắp xếp từ khóa của theme này theo volume
            sorted_theme_kws = sorted(theme_kws.items(), key=lambda x: x[1], reverse=True)

            if target_themes or args.kws_per_theme:
                limit = args.kws_per_theme if args.kws_per_theme else 2
                chosen = sorted_theme_kws[:limit]
            else:
                chosen = sorted_theme_kws

            for kw, vol in chosen:
                candidates.append({
                    "keyword": kw,
                    "volume": vol,
                    "sector": sec,
                    "theme": file_basename
                })

    # Khử trùng lặp từ khóa giữa các file nếu có
    unique_candidates = {}
    for c in candidates:
        kw = c["keyword"]
        if kw not in unique_candidates or c["volume"] > unique_candidates[kw]["volume"]:
            unique_candidates[kw] = c

    sorted_keywords = sorted(unique_candidates.values(), key=lambda x: x["volume"], reverse=True)

    top_n = args.top_n if args.top_n else (len(sorted_keywords) if target_themes else 200)
    sorted_keywords = sorted_keywords[:top_n]

    print(f"[INFO] Tổng số từ khóa chọn phân tích: {len(sorted_keywords)}")
    for item in sorted_keywords:
        print(f"  - [{item['sector']} / {item['theme']}] {item['keyword']} (Vol: {item['volume']:,})")

    if not sorted_keywords:
        print("[WARNING] Không tìm thấy từ khóa nào phù hợp tiêu chí.")
        return

    # Install/Import Pytrends
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("[ERROR] Thiếu thư viện pytrends. Hãy chạy: pip3 install pytrends")
        sys.exit(1)

    # Khởi tạo Pytrends với timeout an toàn (retries=0 để tương thích urllib3 2.0+)
    pytrends = TrendReq(hl='vi-VN', tz=420, timeout=(15, 30), retries=0)

    batch_size = 5
    new_results = []
    total_batches = (len(sorted_keywords) + batch_size - 1) // batch_size

    for i in range(0, len(sorted_keywords), batch_size):
        batch = sorted_keywords[i:i + batch_size]
        batch_keywords = [item["keyword"] for item in batch]
        batch_idx = i // batch_size + 1

        print(f"\n[INFO] Đang xử lý Batch {batch_idx}/{total_batches}: {', '.join(batch_keywords)}...")

        try:
            # Query interest over time (12 tháng qua tại VN)
            pytrends.build_payload(batch_keywords, cat=0, timeframe='today 12-m', geo='VN', gprop='')

            interest_over_time_df = pytrends.interest_over_time()
            time.sleep(1) # delay nhỏ giữa các sub-calls
            interest_by_region_df = pytrends.interest_by_region(resolution='CITY', inc_low_vol=True, inc_geo_code=False)
            time.sleep(1)
            related_queries = pytrends.related_queries()

            for item in batch:
                kw = item["keyword"]
                vol = item["volume"]
                kw_data = {
                    "keyword": kw,
                    "inventory_volume": vol,
                    "sector": item["sector"],
                    "theme": item["theme"],
                    "trend_data": {}
                }

                # 1. Interest over time
                if interest_over_time_df is not None and kw in interest_over_time_df.columns:
                    kw_series = interest_over_time_df[kw]
                    kw_data["trend_data"]["avg_interest"] = float(kw_series.mean())
                    kw_data["trend_data"]["max_interest"] = float(kw_series.max())
                    kw_data["trend_data"]["min_interest"] = float(kw_series.min())
                    kw_data["trend_data"]["has_trend"] = bool(kw_series.max() > 0)
                else:
                    kw_data["trend_data"]["avg_interest"] = 0.0
                    kw_data["trend_data"]["max_interest"] = 0.0
                    kw_data["trend_data"]["min_interest"] = 0.0
                    kw_data["trend_data"]["has_trend"] = False

                # 2. Interest by region (top 5 tỉnh/thành)
                if interest_by_region_df is not None and kw in interest_by_region_df.columns:
                    region_series = interest_by_region_df[kw].sort_values(ascending=False)
                    top_regions = []
                    for region, val in region_series.head(5).items():
                        if val > 0:
                            top_regions.append({"region": region, "interest": int(val)})
                    kw_data["trend_data"]["top_regions"] = top_regions
                else:
                    kw_data["trend_data"]["top_regions"] = []

                # 3. Related queries (top 5 rising)
                if related_queries is not None and kw in related_queries and 'rising' in related_queries[kw] and related_queries[kw]['rising'] is not None:
                    rising_queries = related_queries[kw]['rising'].head(5)
                    related = []
                    for _, row in rising_queries.iterrows():
                        val = row.get('value')
                        related.append({
                            "query": str(row['query']),
                            "value": int(val) if str(val).isdigit() else (9999 if val == 'Breakout' else 0)
                        })
                    kw_data["trend_data"]["related_queries"] = related
                else:
                    kw_data["trend_data"]["related_queries"] = []

                new_results.append(kw_data)

        except Exception as e:
            print(f"[WARNING] Batch {batch_idx} gặp lỗi: {e}")
            for item in batch:
                new_results.append({
                    "keyword": item["keyword"],
                    "inventory_volume": item["volume"],
                    "sector": item["sector"],
                    "theme": item["theme"],
                    "trend_data": {
                        "avg_interest": 0.0,
                        "max_interest": 0.0,
                        "min_interest": 0.0,
                        "has_trend": False,
                        "top_regions": [],
                        "related_queries": []
                    },
                    "error": str(e)
                })

        # Giãn cách an toàn tránh bị rate limit
        sleep_duration = args.delay + random.uniform(0.5, 1.5)
        print(f"[INFO] Giãn cách an toàn {sleep_duration:.2f}s trước batch tiếp theo...")
        time.sleep(sleep_duration)

    # 4. Ghi nhận / Upsert vào SSOT JSON
    output_dir = os.path.join(os.path.dirname(__file__), "..", "07_REPORTS", "data")
    os.makedirs(output_dir, exist_ok=True)
    report_file = os.path.join(output_dir, "google_trends_validation.json")

    final_results_map = {}

    # Đọc dữ liệu cũ nếu ở chế độ upsert
    if not args.no_upsert and os.path.exists(report_file):
        try:
            with open(report_file, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                for r in old_data.get("results", []):
                    final_results_map[r["keyword"]] = r
            print(f"[INFO] Đã nạp {len(final_results_map)} bản ghi cũ từ {report_file} để thực hiện Upsert.")
        except Exception as e:
            print(f"[WARNING] Không thể đọc bản ghi cũ: {e}")

    # Cập nhật kết quả mới
    for r in new_results:
        final_results_map[r["keyword"]] = r

    merged_results = list(final_results_map.values())
    has_trend_count = sum(1 for r in merged_results if r.get("trend_data", {}).get("has_trend"))
    no_trend_count = len(merged_results) - has_trend_count

    report_data = {
        "generated_at": datetime.now().isoformat(),
        "sample_size": len(merged_results),
        "total_keywords_analyzed": len(merged_results),
        "has_trend_count": has_trend_count,
        "no_trend_count": no_trend_count,
        "trend_percentage": round(has_trend_count / len(merged_results) * 100, 2) if merged_results else 0.0,
        "results": merged_results
    }

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)

    print(f"\n=== HOÀN TẤT GOOGLE TRENDS VALIDATION ===")
    print(f"- Số từ khóa mới xử lý: {len(new_results)}")
    print(f"- Tổng số từ khóa tích lũy trong SSOT: {len(merged_results)}")
    print(f"- Từ khóa có xu hướng quan tâm: {has_trend_count} ({report_data['trend_percentage']}%)")
    print(f"- File SSOT: {report_file}")

if __name__ == "__main__":
    main()

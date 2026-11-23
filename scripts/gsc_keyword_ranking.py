#!/usr/bin/env python3
"""
Cron Script: Google Search Console (GSC) Keyword Position Tracker
Mục đích:
1. Kết nối với Google Search Console API bằng Service Account credentials.
2. Quét position thực tế của toàn bộ keywords từ Inventory (GSC Search Analytics).
3. Làm tròn position theo quy tắc: round(x.5) = x+1 (standard rounding).
4. Re-score opportunity dựa trên actual position.
5. Xuất dữ liệu sang 07_REPORTS/data/gsc_keyword_ranking.json.
"""

import os
import sys
import json
import time
from datetime import datetime, timedelta
from collections import defaultdict

def main():
    print("=== BẮT ĐẦU QUY TRÌNH GSC KEYWORD POSITION TRACKING ===")

    # 1. Kiểm tra file credentials
    key_file = os.path.join(os.path.dirname(__file__), "..", "07_REPORTS", "data", "gsc-credentials.json")
    if not os.path.exists(key_file):
        key_file = os.path.join(os.path.dirname(__file__), "..", "07_REPORTS", "data", "credentials", "gsc-credentials.json")

    if not os.path.exists(key_file):
        print(f"[ERROR] Không tìm thấy file credentials tại {key_file}")
        sys.exit(1)

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
    except ImportError:
        print("[ERROR] Thiếu thư viện google-api-python-client hoặc google-auth. Hãy chạy: pip3 install google-api-python-client google-auth")
        sys.exit(1)

    # 2. Đọc cấu hình từ credentials
    with open(key_file, "r", encoding="utf-8") as f:
        cred_data = json.load(f)
    client_email = cred_data.get("client_email", "")
    print(f"[INFO] Sử dụng Service Account: {client_email}")

    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    credentials = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
    service = build("searchconsole", "v1", credentials=credentials)

    # 3. Xác định Site URL & Khung thời gian 30 ngày (để position accuracy cao hơn)
    site_url = os.environ.get("GSC_SITE_URL")
    if not site_url:
        try:
            sites_res = service.sites().list().execute()
            site_entries = sites_res.get("siteEntry", [])
            if site_entries:
                site_url = site_entries[0].get("siteUrl")
                print(f"[INFO] Tự động nhận diện Site URL từ GSC: {site_url}")
            else:
                site_url = "https://www.momo.vn/"
        except Exception:
            site_url = "https://www.momo.vn/"

    days_back = int(os.environ.get("GSC_DAYS", "30"))
    end_date = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days_back + 3)).strftime("%Y-%m-%d")

    print(f"[INFO] Truy vấn Site: {site_url}")
    print(f"[INFO] Khung thời gian quét (30 ngày): {start_date} -> {end_date}")

    # 4. Load seed keywords từ Inventory
    inventory_dir = os.path.join(os.path.dirname(__file__), "..", "05_HUBS", "inventory")
    seed_keywords = set()

    if os.path.exists(inventory_dir):
        import glob
        import csv

        for sector in os.listdir(inventory_dir):
            sector_dir = os.path.join(inventory_dir, sector)
            if not os.path.isdir(sector_dir):
                continue

            csv_files = glob.glob(os.path.join(sector_dir, "*.csv"))
            for csv_file in csv_files:
                try:
                    with open(csv_file, "r", encoding="utf-8-sig", errors="replace") as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            kw_raw = row.get("Keyword", "")
                            if kw_raw:
                                kw = kw_raw.lower().strip()
                                if kw:
                                    seed_keywords.add(kw)
                except Exception as e:
                    print(f"[WARNING] Không thể đọc {csv_file}: {e}")

    print(f"[INFO] Đã load {len(seed_keywords):,} seed keywords từ Inventory")

    # 5. Phân trang lấy dữ liệu từ GSC (Query-only để tối ưu performance)
    all_rows = []
    start_row = 0
    batch_size = 25000
    max_rows = int(os.environ.get("GSC_MAX_ROWS", "100000"))

    print(f"[INFO] Bắt đầu quét GSC Query-only (Tối đa {max_rows:,} dòng, {batch_size:,} dòng/lần gọi)...")

    while start_row < max_rows:
        request_body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query"],
            "rowLimit": batch_size,
            "startRow": start_row,
        }

        try:
            response = service.searchanalytics().query(siteUrl=site_url, body=request_body).execute()
        except HttpError as err:
            if err.resp.status == 403:
                print(f"[PERMISSION REQUIRED] Tài khoản {client_email} chưa được cấp quyền trong Google Search Console cho Property '{site_url}'.")
                sys.exit(2)
            else:
                print(f"[API ERROR] Lỗi truy vấn GSC API tại dòng {start_row}: {err}")
                break
        except Exception as e:
            print(f"[UNEXPECTED ERROR] {e}")
            break

        batch_rows = response.get("rows", [])
        if not batch_rows:
            break

        all_rows.extend(batch_rows)
        print(f"[INFO] Batch [{start_row:,} - {start_row + len(batch_rows):,}]: Đã tải thành công {len(batch_rows):,} bản ghi (Tổng lũy kế: {len(all_rows):,})")

        if len(batch_rows) < batch_size:
            break

        start_row += batch_size
        time.sleep(0.5)

    print(f"[INFO] Hoàn tất trích xuất GSC. Tổng cộng: {len(all_rows):,} bản ghi (Query-only).")

    # 6. Map GSC data với seed keywords và làm tròn position
    gsc_data = {}
    for r in all_rows:
        query = r["keys"][0].lower()
        clicks = r.get("clicks", 0)
        impressions = r.get("impressions", 0)
        position = r.get("position", 0.0)

        # Làm tròn position theo quy tắc: round(x.5) = x+1
        rounded_position = round(position)

        gsc_data[query] = {
            "query": query,
            "clicks": clicks,
            "impressions": impressions,
            "position": position,
            "rounded_position": rounded_position
        }

    # 7. Merge với seed keywords
    keyword_ranking = []
    matched_count = 0
    unmatched_count = 0

    for kw in seed_keywords:
        if kw in gsc_data:
            matched_count += 1
            data = gsc_data[kw]
            keyword_ranking.append(data)
        else:
            unmatched_count += 1
            keyword_ranking.append({
                "query": kw,
                "clicks": 0,
                "impressions": 0,
                "position": 0,
                "rounded_position": 0
            })

    print(f"[INFO] Mapping kết quả: {matched_count:,} keywords matched / {unmatched_count:,} keywords not found in GSC")

    # 8. Re-score opportunity dựa trên position
    def calculate_position_bonus(rounded_position):
        if rounded_position == 0:
            return 0.3  # Không có rank
        elif rounded_position <= 3:
            return 1.5  # Top 3 bonus
        elif rounded_position <= 10:
            return 1.0  # Neutral
        elif rounded_position <= 20:
            return 0.7  # Penalty
        else:
            return 0.5  # Heavy penalty

    for kw_data in keyword_ranking:
        pos = kw_data["rounded_position"]
        kw_data["position_bonus"] = calculate_position_bonus(pos)

    # 9. Xuất file kết quả vào thư mục cache
    output_dir = os.path.join(os.path.dirname(__file__), "..", "07_REPORTS", "data", "cache")
    os.makedirs(output_dir, exist_ok=True)

    ranking_file = os.path.join(output_dir, "gsc_keyword_ranking.json")
    report_data = {
        "generated_at": datetime.now().isoformat(),
        "site_url": site_url,
        "period": f"{start_date} -> {end_date} (30 ngày)",
        "total_analyzed_rows": len(all_rows),
        "total_seed_keywords": len(seed_keywords),
        "matched_keywords": matched_count,
        "unmatched_keywords": unmatched_count,
        "keywords": keyword_ranking
    }

    with open(ranking_file, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)

    print(f"\n=== KẾT QUẢ GSC KEYWORD POSITION TRACKING HOÀN TẤT ===")
    print(f"- Tổng số dòng dữ liệu GSC: {len(all_rows):,}")
    print(f"- Tổng số seed keywords từ Inventory: {len(seed_keywords):,}")
    print(f"- Keywords matched trong GSC: {matched_count:,}")
    print(f"- Keywords không có trong GSC: {unmatched_count:,}")
    print(f"- Đã lưu Keyword Ranking vào: {ranking_file}")

if __name__ == "__main__":
    main()

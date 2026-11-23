#!/usr/bin/env python3
"""
Cron Script: Google Search Console (GSC) Query & Cannibalization Analyzer (3 Months / 90 Days)
Mục đích:
1. Kết nối với Google Search Console API bằng Service Account credentials.
2. Quét dữ liệu Search Analytics trong 90 ngày (3 tháng gần nhất) với cơ chế phân trang (Pagination).
3. Quét và trích xuất TOÀN BỘ URLs thực tế của momo.vn đang nhận traffic/impression từ Google SERP.
4. Tự động phát hiện các Query bị ăn thịt từ khóa (Cannibalization) trên momo.vn.
5. Xuất ma trận kiểm soát sang 07_REPORTS/data/gsc_cannibalization_matrix.json và gsc_live_active_urls.json.
"""

import os
import sys
import json
import time
from datetime import datetime, timedelta

def main():
    print("=== BẮT ĐẦU QUY TRÌNH GSC 3-MONTH SCAN & CANNIBALIZATION ANALYZER ===")

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

    # 3. Xác định Site URL & Khung thời gian 3 tháng (90 ngày)
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

    days_back = int(os.environ.get("GSC_DAYS", "90"))
    end_date = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days_back + 3)).strftime("%Y-%m-%d")

    print(f"[INFO] Truy vấn Site: {site_url}")
    print(f"[INFO] Khung thời gian quét (3 tháng): {start_date} -> {end_date}")

    # 4. Phân trang lấy dữ liệu (Pagination Loop)
    all_rows = []
    start_row = 0
    batch_size = 25000
    max_rows = int(os.environ.get("GSC_MAX_ROWS", "500000"))
    top_queries_per_url = int(os.environ.get("GSC_TOP_QUERIES_PER_URL", "20"))

    print(f"[INFO] Bắt đầu quét đa phân trang (Tối đa {max_rows:,} dòng, {batch_size:,} dòng/lần gọi)...")

    while start_row < max_rows:
        request_body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query", "page"],
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
            # Đã hết dữ liệu từ phía Google
            break

        start_row += batch_size
        time.sleep(0.5)  # Tránh vượt rate limit của Google

    print(f"[INFO] Hoàn tất trích xuất GSC. Tổng cộng: {len(all_rows):,} bản ghi (Query x URL).")

    # 5. Thống kê & Lưu trữ toàn bộ URLs thực tế đang nhận Traffic trên SERP
    url_stats = {}
    query_map = {}

    for r in all_rows:
        q = r["keys"][0]
        url = r["keys"][1]
        clicks = r.get("clicks", 0)
        impressions = r.get("impressions", 0)
        position = r.get("position", 0.0)

        # Thống kê URL
        if url not in url_stats:
            url_stats[url] = {
                "url": url,
                "total_clicks": 0,
                "total_impressions": 0,
                "top_queries": []
            }
        url_stats[url]["total_clicks"] += clicks
        url_stats[url]["total_impressions"] += impressions
        url_stats[url]["top_queries"].append({"query": q, "clicks": clicks, "impressions": impressions, "position": round(position, 1)})

        # Gom nhóm Query
        if q not in query_map:
            query_map[q] = []
        query_map[q].append({
            "url": url,
            "clicks": clicks,
            "impressions": impressions,
            "position": round(position, 1)
        })

    # 6. Phân tích Cannibalization
    cannibalized_queries = []
    for q, pages in query_map.items():
        if len(pages) > 1:
            total_imp = sum(p["impressions"] for p in pages)
            total_clicks = sum(p["clicks"] for p in pages)
            if total_imp >= 50:  # Ngưỡng tối thiểu 50 impressions trong 3 tháng
                sorted_pages = sorted(pages, key=lambda x: (x["clicks"], x["impressions"]), reverse=True)
                top_page_share = (sorted_pages[0]["clicks"] / total_clicks) if total_clicks > 0 else 0.5
                
                if top_page_share < 0.70:
                    risk = "CRITICAL"
                    action = "CANONICAL_OR_301_CONSOLIDATE"
                else:
                    risk = "MODERATE"
                    action = "INTERNAL_LINK_REALIGNMENT"

                cannibalized_queries.append({
                    "query": q,
                    "total_impressions": total_imp,
                    "total_clicks": total_clicks,
                    "risk_level": risk,
                    "recommended_action": action,
                    "competing_pages": sorted_pages
                })

    cannibalized_queries.sort(key=lambda x: x["total_impressions"], reverse=True)

    # 7. Xuất file kết quả
    output_dir = os.path.join(os.path.dirname(__file__), "..", "07_REPORTS", "data", "cache")
    os.makedirs(output_dir, exist_ok=True)

    # A. File Ma trận Cannibalization
    matrix_file = os.path.join(output_dir, "gsc_cannibalization_matrix.json")
    report_data = {
        "generated_at": datetime.now().isoformat(),
        "site_url": site_url,
        "period": f"{start_date} -> {end_date} (90 ngày)",
        "total_analyzed_rows": len(all_rows),
        "total_unique_urls": len(url_stats),
        "total_cannibalized_queries": len(cannibalized_queries),
        "critical_count": sum(1 for c in cannibalized_queries if c["risk_level"] == "CRITICAL"),
        "moderate_count": sum(1 for c in cannibalized_queries if c["risk_level"] == "MODERATE"),
        "top_cannibalized": cannibalized_queries
    }
    with open(matrix_file, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)

    # B. File Danh mục Toàn bộ URLs đang sống và có traffic từ Google
    active_urls_file = os.path.join(output_dir, "gsc_live_active_urls.json")
    for stats in url_stats.values():
        stats["top_queries"].sort(key=lambda x: (x["clicks"], x["impressions"]), reverse=True)
        stats["total_queries"] = len(stats["top_queries"])
        stats["top_queries"] = stats["top_queries"][:top_queries_per_url]
    sorted_urls = sorted(url_stats.values(), key=lambda x: x["total_clicks"], reverse=True)
    with open(active_urls_file, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "period": f"{start_date} -> {end_date}",
            "total_active_urls": len(sorted_urls),
            "urls": sorted_urls
        }, f, ensure_ascii=False, indent=2)

    # D. Map đầy đủ Query -> các URL MoMo đang rank (SSOT cho "keyword đã có bài chưa")
    # Format gọn: query -> [[url, clicks, impressions, position], ...] sắp theo clicks giảm dần
    query_page_file = os.path.join(output_dir, "gsc_query_page_map.json")
    with open(query_page_file, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "period": f"{start_date} -> {end_date}",
            "total_rows": len(all_rows),
            "truncated": len(all_rows) >= max_rows,
            "total_queries": len(query_map),
            "fields": ["url", "clicks", "impressions", "position"],
            "queries": {
                q: [[p["url"], p["clicks"], p["impressions"], p["position"]]
                    for p in sorted(pages, key=lambda x: (x["clicks"], x["impressions"]), reverse=True)]
                for q, pages in query_map.items()
            },
        }, f, ensure_ascii=False, separators=(",", ":"))

    # C. Cập nhật và làm giàu kho momo_live_urls.json
    sitemap_file = os.path.join(output_dir, "momo_live_urls.json")
    existing_sitemap_urls = set()
    if os.path.exists(sitemap_file):
        try:
            with open(sitemap_file, "r", encoding="utf-8") as f:
                existing_sitemap_urls = set(json.load(f).get("urls", []))
        except Exception:
            pass
    existing_sitemap_urls = {u.split("#")[0] for u in existing_sitemap_urls}

    merged_live_urls = sorted(existing_sitemap_urls.union(u.split("#")[0] for u in url_stats))
    with open(sitemap_file, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_urls": len(merged_live_urls),
            "source": "Merged Sitemap + GSC 90-Day Active URLs",
            "urls": merged_live_urls
        }, f, ensure_ascii=False, indent=2)

    print(f"\n=== KẾT QUẢ QUÉT 3 THÁNG GSC HOÀN TẤT ===")
    print(f"- Tổng số dòng dữ liệu (Query x URL): {len(all_rows):,}")
    print(f"- Tổng số URL thực tế của momo.vn phát hiện trên SERP: {len(url_stats):,} URLs")
    print(f"- Tổng số Query bị Cannibalization: {len(cannibalized_queries):,} (Critical: {report_data['critical_count']:,}, Moderate: {report_data['moderate_count']:,})")
    print(f"- Đã lưu Ma trận Cannibalization vào: {matrix_file}")
    print(f"- Đã lưu Danh sách Active URLs vào: {active_urls_file}")
    print(f"- Đã lưu Query -> Page map ({len(query_map):,} queries) vào: {query_page_file}")
    if len(all_rows) >= max_rows:
        print(f"[WARN] Chạm trần GSC_MAX_ROWS={max_rows:,}, dữ liệu long-tail có thể bị thiếu. Tăng GSC_MAX_ROWS để quét đủ.")
    print(f"- Đã cập nhật SSOT Live URLs ({len(merged_live_urls):,} URLs) vào: {sitemap_file}")

if __name__ == "__main__":
    main()

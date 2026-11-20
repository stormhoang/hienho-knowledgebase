#!/usr/bin/env python3
"""
FETCH GA4 SEARCH ANALYTICS FOR /TIM-KIEM
Trích xuất dữ liệu từ khóa tìm kiếm và traffic cho trang /tim-kiem
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
PROPERTY_ID = "270743103"
STREAM_ID = "G-02G70QKZ26"

def get_access_token():
    creds_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
    token_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-token.json"

    if not creds_file.exists() or not token_file.exists():
        raise FileNotFoundError(f"Thiếu file credentials hoặc token tại: {creds_file}")

    with open(creds_file, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    oauth_creds = creds_data.get("installed") or creds_data.get("web")
    if not oauth_creds:
        raise ValueError("File ga4-credentials.json không chứa installed/web client credentials")

    with open(token_file, "r", encoding="utf-8") as f:
        token_data = json.load(f)
    refresh_token = token_data.get("refresh_token")
    if not refresh_token:
        raise ValueError("File ga4-token.json không chứa refresh_token hợp lệ")

    # Refresh token
    body = urllib.parse.urlencode({
        "client_id": oauth_creds["client_id"],
        "client_secret": oauth_creds["client_secret"],
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["access_token"]
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"Lỗi refresh token từ Google OAuth: {err_msg}")

def run_ga4_report(access_token, request_body):
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"
    req = urllib.request.Request(
        url,
        data=json.dumps(request_body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"Lỗi GA4 runReport: {err_msg}")

def main():
    start_time = time.time()
    print("=" * 70)
    print("FETCH GA4 SEARCH ANALYTICS FOR /TIM-KIEM")
    print(f"Property ID: {PROPERTY_ID} | Stream ID: {STREAM_ID}")
    print("=" * 70)

    # 1. Khởi tạo xác thực
    print("[1/4] Khởi tạo xác thực Google OAuth 2.0...")
    access_token = get_access_token()
    print("✓ Lấy access token thành công.")

    # Khung thời gian: 1/10/2026 đến hôm nay (22/10/2026)
    start_date_str = "2026-10-01"
    end_date_str = "2026-10-22"

    date_ranges = [{"startDate": start_date_str, "endDate": end_date_str}]
    print(f"Khung thời gian phân tích: {start_date_str} -> {end_date_str}")

    # 2. Lấy Traffic tổng cho /tim-kiem
    print("[2/4] Kéo traffic cho /tim-kiem...")
    res_traffic = run_ga4_report(access_token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "date"},
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "dimensionFilter": {
            "filter": {
                "fieldName": "landingPage",
                "stringFilter": {"matchType": "EXACT", "value": "/tim-kiem"}
            }
        },
        "metrics": [
            {"name": "sessions"},
            {"name": "engagedSessions"},
            {"name": "activeUsers"}
        ],
        "orderBys": [{"dimension": {"dimensionName": "date"}, "desc": True}],
        "limit": 10000
    })

    traffic_data = []
    total_sessions = 0
    total_engaged = 0
    total_users = 0

    for r in res_traffic.get("rows", []):
        date = r["dimensionValues"][0]["value"]
        channel = r["dimensionValues"][1]["value"]
        source = r["dimensionValues"][2]["value"]
        sessions = int(r["metricValues"][0]["value"])
        engaged = int(r["metricValues"][1]["value"])
        users = int(r["metricValues"][2]["value"])

        total_sessions += sessions
        total_engaged += engaged
        total_users += users

        traffic_data.append({
            "date": date,
            "channel_group": channel,
            "source": source,
            "sessions": sessions,
            "engaged_sessions": engaged,
            "active_users": users
        })

    print(f"✓ Traffic /tim-kiem: {len(traffic_data)} bản ghi")
    print(f"  - Total Sessions: {total_sessions:,}")
    print(f"  - Total Engaged Sessions: {total_engaged:,}")
    print(f"  - Total Active Users: {total_users:,}")

    # 3. Thử lấy Search Queries - Check event 'search' hoặc custom parameter
    print("[3/4] Thử lấy Search Queries từ GA4 Events...")

    # Cách 1: Thử event 'search' với parameter 'search_term'
    try:
        res_search_events = run_ga4_report(access_token, {
            "dateRanges": date_ranges,
            "dimensions": [
                {"name": "eventName"},
                {"name": "eventParameter:search_term"}
            ],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "eventName",
                    "stringFilter": {"matchType": "EXACT", "value": "search"}
                }
            },
            "metrics": [{"name": "eventCount"}],
            "limit": 10000
        })

        search_queries = []
        for r in res_search_events.get("rows", []):
            event_name = r["dimensionValues"][0]["value"]
            search_term = r["dimensionValues"][1]["value"] if len(r["dimensionValues"]) > 1 else "(empty)"
            count = int(r["metricValues"][0]["value"])

            if search_term and search_term != "(empty)" and search_term != "(not set)":
                search_queries.append({
                    "search_term": search_term,
                    "event_count": count
                })

        print(f"✓ Search Queries từ event 'search': {len(search_queries)} bản ghi")
    except Exception as e:
        print(f"⚠ Không thể lấy search queries từ event 'search': {e}")
        search_queries = []

    # Cách 2: Thử dimension 'searchTerm' (nếu Site Search được bật)
    try:
        res_search_term = run_ga4_report(access_token, {
            "dateRanges": date_ranges,
            "dimensions": [{"name": "searchTerm"}],
            "metrics": [{"name": "sessions"}],
            "limit": 10000
        })

        search_term_data = []
        for r in res_search_term.get("rows", []):
            term = r["dimensionValues"][0]["value"]
            sessions = int(r["metricValues"][0]["value"])
            if term and term != "(not set)":
                search_term_data.append({
                    "search_term": term,
                    "sessions": sessions
                })

        print(f"✓ Search Queries từ dimension 'searchTerm': {len(search_term_data)} bản ghi")
    except Exception as e:
        print(f"⚠ Không thể lấy search queries từ dimension 'searchTerm': {e}")
        search_term_data = []

    # 4. Thử lấy event page_view với parameter 'page_location' hoặc 'page_title' để check search queries trong URL
    print("[4/4] Thử phân tích URL parameters từ page views...")
    try:
        res_page_params = run_ga4_report(access_token, {
            "dateRanges": date_ranges,
            "dimensions": [
                {"name": "pagePath"},
                {"name": "eventParameter:page_location"}
            ],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "pagePath",
                    "stringFilter": {"matchType": "BEGINS_WITH", "value": "/tim-kiem"}
                }
            },
            "metrics": [{"name": "screenPageViews"}],
            "limit": 10000
        })

        page_data = []
        for r in res_page_params.get("rows", []):
            path = r["dimensionValues"][0]["value"]
            location = r["dimensionValues"][1]["value"] if len(r["dimensionValues"]) > 1 else ""
            views = int(r["metricValues"][0]["value"])

            page_data.append({
                "page_path": path,
                "page_location": location,
                "page_views": views
            })

        print(f"✓ Page Views với URL params: {len(page_data)} bản ghi")
    except Exception as e:
        print(f"⚠ Không thể lấy page params: {e}")
        page_data = []

    # Xuất kết quả
    output_dir = BASE_DIR / "07_REPORTS" / "data" / "search_analytics"
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "property": STREAM_ID,
        "period": {
            "start": start_date_str,
            "end": end_date_str
        },
        "summary": {
            "total_sessions": total_sessions,
            "total_engaged_sessions": total_engaged,
            "total_active_users": total_users,
            "traffic_records": len(traffic_data)
        },
        "traffic_by_date_channel": traffic_data,
        "search_queries_from_event": search_queries,
        "search_queries_from_dimension": search_term_data,
        "page_views_with_params": page_data,
        "_note": f"Dữ liệu xuất từ GA4 Property {PROPERTY_ID} vào {datetime.now().isoformat()}"
    }

    output_file = output_dir / "tim-kiem-analytics-2026-10-01-to-2026-10-22.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Đã lưu kết quả: {output_file}")

    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"HOÀN THÀNH TRONG {elapsed:.1f} GIÂY")
    print(f"- Total Sessions /tim-kiem: {total_sessions:,}")
    print(f"- Total Active Users: {total_users:,}")
    print(f"- Search Queries (event): {len(search_queries)}")
    print(f"- Search Queries (dimension): {len(search_term_data)}")
    print("=" * 70)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
SYNC GA4 REAL DATA TO WEB HUBS (react-web-momo)
Đồng bộ dữ liệu hiệu suất Google Analytics 4 (Property 270743103) vào Web Hubs:
- Schema đích: data/ga4/landing-pages.json
- Khớp với giao diện: components/content-plan/Ga4Dashboard.tsx
- Bao gồm:
  1. Toàn bộ 132+ theme landing pages từ seo-clusters-summary.json
  2. Toàn bộ session trích dẫn từ các công cụ AI (ChatGPT, Perplexity, Gemini, Copilot)
  3. Top landing pages có lượng truy cập lớn nhất toàn Website
  4. Bóc tách chính xác click chuyển đổi Web-to-App:
     - Track 1: onelink.momo.vn (User hiện hữu mở App)
     - Track 2: momoapp.onelink.me (User mới cài App)
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
PROPERTY_ID = "270743103"
STREAM_ID = "G-02G70QKZ26"

def get_access_token():
    raise RuntimeError("[CHÍNH SÁCH HẠ TẦNG MOMO] Toàn bộ lệnh gọi GA4 API đã bị vô hiệu hóa vĩnh viễn. Chỉ vận hành GTM.")

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

def load_theme_paths():
    """Tải danh sách URL của toàn bộ theme từ seo-clusters-summary.json"""
    summary_file = HUBS_REPO / "data" / "seo-clusters-summary.json"
    if not summary_file.exists():
        summary_file = BASE_DIR / "07_REPORTS" / "data" / "inventory_clusters_summary.json"
        
    if not summary_file.exists():
        print(f"Cảnh báo: Không tìm thấy seo-clusters-summary.json tại {summary_file}")
        return []

    with open(summary_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    paths = set()
    for u in data.get("usecases", []):
        url = u.get("cannibalization_shield", {}).get("top_live_url")
        if url:
            p = urlparse(url).path.strip()
            if p:
                paths.add(p)
    return sorted(list(paths))

def main():
    start_time = time.time()
    print("=" * 70)
    print("ĐỒNG BỘ DỮ LIỆU GA4 THỰC TẾ SANG WEB HUBS (REACT-WEB-MOMO)")
    print(f"Property ID: {PROPERTY_ID} | Stream ID: {STREAM_ID}")
    print("=" * 70)

    # 1. Khởi tạo xác thực
    print("[1/5] Khởi tạo xác thực Google OAuth 2.0...")
    access_token = get_access_token()
    print("✓ Lấy access token thành công.")

    # Khung thời gian phân tích (hỗ trợ --mtd hoặc --start-date / --end-date)
    import argparse
    parser = argparse.ArgumentParser(description="Sync GA4 real data to Web Hubs")
    parser.add_argument("--start-date", default=None, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default=None, help="End date (YYYY-MM-DD)")
    parser.add_argument("--mtd", type=int, default=None, help="Số ngày lũy kế MTD (vd: 21)")
    cli_args = parser.parse_args()

    if cli_args.mtd:
        start_date_str = "2026-10-01"
        end_date_str = f"2026-10-{cli_args.mtd:02d}"
    elif cli_args.start_date and cli_args.end_date:
        start_date_str = cli_args.start_date
        end_date_str = cli_args.end_date
    else:
        yesterday = datetime.now() - timedelta(days=1)
        days_30_ago = datetime.now() - timedelta(days=30)
        start_date_str = days_30_ago.strftime("%Y-%m-%d")
        end_date_str = yesterday.strftime("%Y-%m-%d")

    date_ranges = [{"startDate": start_date_str, "endDate": end_date_str}]
    print(f"Khung thời gian phân tích: {start_date_str} -> {end_date_str}")

    # 2. Lấy danh sách Theme URLs
    theme_paths = load_theme_paths()
    print(f"[2/5] Đã tải {len(theme_paths)} Theme Landing Pages từ SSOT Clusters.")

    # 3. Kéo Traffic: Themes + AI Sources + Top Pages
    print("[3/5] Kéo dữ liệu Traffic từ Google Analytics 4...")
    rows_map = {}  # key: (landing_page, channel_group, source) -> dict

    def add_traffic_rows(res):
        for r in res.get("rows", []):
            lp = r["dimensionValues"][0]["value"].strip()
            cg = r["dimensionValues"][1]["value"].strip()
            src = r["dimensionValues"][2]["value"].strip()
            pv = int(r["metricValues"][2]["value"])
            key = (lp, cg, src)
            if key not in rows_map:
                rows_map[key] = {
                    "landing_page": lp,
                    "channel_group": cg,
                    "source": src,
                    "pageviews": pv,
                    "onelink_clicks_track1": 0,
                    "onelink_clicks_track2": 0
                }
            else:
                rows_map[key]["pageviews"] = max(rows_map[key]["pageviews"], pv)

    # 3.1. Kéo Traffic cho Theme Landing Pages
    if theme_paths:
        res_themes = run_ga4_report(access_token, {
            "dateRanges": date_ranges,
            "dimensions": [
                {"name": "landingPage"},
                {"name": "sessionDefaultChannelGroup"},
                {"name": "sessionSource"}
            ],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "landingPage",
                    "inListFilter": {"values": theme_paths}
                }
            },
            "metrics": [{"name": "sessions"}, {"name": "engagedSessions"}, {"name": "screenPageViews"}],
            "limit": 10000
        })
        add_traffic_rows(res_themes)
        print(f"✓ Theme Landing Pages traffic: {len(res_themes.get('rows', []))} bản ghi.")

    # 3.2. Kéo Traffic từ các nguồn AI Search (ChatGPT, Perplexity, Gemini, Copilot)
    ai_sources = [
        "chatgpt.com",
        "perplexity.ai",
        "gemini.google.com",
        "copilot.microsoft.com",
        "android-app://com.openai.chatgpt"
    ]
    res_ai = run_ga4_report(access_token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "landingPage"},
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "dimensionFilter": {
            "filter": {
                "fieldName": "sessionSource",
                "inListFilter": {"values": ai_sources}
            }
        },
        "metrics": [{"name": "sessions"}, {"name": "engagedSessions"}, {"name": "screenPageViews"}],
        "limit": 10000
    })
    add_traffic_rows(res_ai)
    print(f"✓ AI Search referrals traffic: {len(res_ai.get('rows', []))} bản ghi.")

    # 3.3. Kéo Top 300 Landing Pages toàn Website để bao phủ mọi hub chính
    res_top = run_ga4_report(access_token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "landingPage"},
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "metrics": [{"name": "sessions"}, {"name": "engagedSessions"}, {"name": "screenPageViews"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
        "limit": 300
    })
    add_traffic_rows(res_top)
    print(f"✓ Top General Landing Pages: {len(res_top.get('rows', []))} bản ghi.")
    print(f"  Tổng số tổ hợp (Landing Page x Channel x Source) đã tích lũy: {len(rows_map)}")

    # 4. Kéo Clicks Web-to-App (Track 1 & Track 2)
    print("[4/5] Kéo sự kiện chuyển đổi OneLink Web-to-App...")

    # 4.1. Track 1: onelink.momo.vn (User hiện hữu mở App)
    res_t1 = run_ga4_report(access_token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "landingPage"},
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink.momo.vn"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink.momo.vn"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 10000
    })
    total_t1_clicks = 0
    for r in res_t1.get("rows", []):
        lp = r["dimensionValues"][0]["value"].strip()
        cg = r["dimensionValues"][1]["value"].strip()
        src = r["dimensionValues"][2]["value"].strip()
        cnt = int(r["metricValues"][0]["value"])
        total_t1_clicks += cnt
        key = (lp, cg, src)
        if key in rows_map:
            rows_map[key]["onelink_clicks_track1"] += cnt
        else:
            rows_map[key] = {
                "landing_page": lp,
                "channel_group": cg,
                "source": src,
                "pageviews": 0,
                "sessions": 0,
                "engaged_sessions": 0,
                "onelink_clicks_track1": cnt,
                "onelink_clicks_track2": 0
            }
    print(f"✓ Track 1 (onelink.momo.vn): {total_t1_clicks:,} lượt click từ {len(res_t1.get('rows', []))} luồng.")

    # 4.2. Track 2: momoapp.onelink.me (User mới cài App)
    res_t2 = run_ga4_report(access_token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "landingPage"},
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "momoapp.onelink.me"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "momoapp.onelink.me"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 10000
    })
    total_t2_clicks = 0
    for r in res_t2.get("rows", []):
        lp = r["dimensionValues"][0]["value"].strip()
        cg = r["dimensionValues"][1]["value"].strip()
        src = r["dimensionValues"][2]["value"].strip()
        cnt = int(r["metricValues"][0]["value"])
        total_t2_clicks += cnt
        key = (lp, cg, src)
        if key in rows_map:
            rows_map[key]["onelink_clicks_track2"] += cnt
        else:
            rows_map[key] = {
                "landing_page": lp,
                "channel_group": cg,
                "source": src,
                "pageviews": 0,
                "onelink_clicks_track1": 0,
                "onelink_clicks_track2": cnt
            }
    print(f"✓ Track 2 (momoapp.onelink.me): {total_t2_clicks:,} lượt click từ {len(res_t2.get('rows', []))} luồng.")

    # 5. Đóng gói payload chuẩn Contract
    print("[5/5] Xuất bản dữ liệu sang Web Hubs...")
    final_rows = list(rows_map.values())
    # Sắp xếp theo pageviews giảm dần
    final_rows.sort(key=lambda x: (x["pageviews"], x["onelink_clicks_track1"] + x["onelink_clicks_track2"]), reverse=True)

    dataset_payload = {
        "sample": False,
        "property": STREAM_ID,
        "period": {
            "start": start_date_str,
            "end": end_date_str
        },
        "_note": f"Dữ liệu thực tế xuất từ Google Analytics 4 Property {PROPERTY_ID} vào {datetime.now().isoformat()}",
        "rows": final_rows
    }

    # Xuất ra file tại react-web-momo
    hubs_ga4_dir = HUBS_REPO / "data" / "ga4"
    hubs_ga4_dir.mkdir(parents=True, exist_ok=True)
    hubs_target = hubs_ga4_dir / "landing-pages.json"
    with open(hubs_target, "w", encoding="utf-8") as f:
        json.dump(dataset_payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu file đích Web Hubs: {hubs_target} ({len(final_rows):,} hàng)")

    # Lưu bản copy SSOT tại Hienho_MoMo-Base
    kb_ga4_dir = BASE_DIR / "07_REPORTS" / "data" / "ga4"
    kb_ga4_dir.mkdir(parents=True, exist_ok=True)
    kb_target = kb_ga4_dir / "landing-pages.json"
    with open(kb_target, "w", encoding="utf-8") as f:
        json.dump(dataset_payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu bản sao SSOT KB: {kb_target}")

    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"HOÀN THÀNH ĐỒNG BỘ GA4 TRONG {elapsed:.1f} GIÂY")
    print(f"- Tổng số dòng dữ liệu: {len(final_rows):,}")
    print(f"- Tổng Track 1 Clicks : {total_t1_clicks:,}")
    print(f"- Tổng Track 2 Clicks : {total_t2_clicks:,}")
    print("=" * 70)

if __name__ == "__main__":
    print("[CHÍNH SÁCH HẠ TẦNG MOMO] sync_ga4_to_hubs.py đã bị vô hiệu hóa hoàn toàn. Hệ thống chỉ vận hành GTM.")
    sys.exit(0)

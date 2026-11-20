#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BUILD PAGE RETENTION & REPEAT VISITORS MATRIX (GA4 API)
Đo lường khách quan và đúng bản chất: Các URL người dùng đã vào và quay trở lại.
Bóc tách rõ ràng giữa:
- Tần suất xem trang: PV / User (Lượt xem trên mỗi người)
- Tần suất mở lại phiên mới: Sessions / User (Người dùng mở lại trang ở các ngày/phiên khác nhau)
"""

import os
import sys
import json
import time
from pathlib import Path
from collections import defaultdict
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")

# Import các hàm dùng chung từ scripts
sys.path.insert(0, str(BASE_DIR))
from scripts.sync_ga4_to_hubs import get_access_token, PROPERTY_ID, run_ga4_report
from scripts.build_full_funnel_matrix import build_theme_matcher, normalize_path

def main():
    start_time = time.time()
    print("=" * 70)
    print("XÂY DỰNG BẢNG ĐO LƯỜNG URL QUAY TRỞ LẠI (PAGE LEVEL REPEAT VISITS)")
    print(f"Property ID: {PROPERTY_ID}")
    print("=" * 70)

    # Khung thời gian: Hỗ trợ --mtd hoặc --start-date / --end-date (mặc định MTD 23)
    import argparse
    parser = argparse.ArgumentParser(description="Build Page Retention Matrix")
    parser.add_argument("--start-date", default="2026-10-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default="2026-10-23", help="End date (YYYY-MM-DD)")
    parser.add_argument("--mtd", type=int, default=None, help="Số ngày lũy kế MTD (vd: 23)")
    cli_args = parser.parse_args()

    if cli_args.mtd:
        start_date = "2026-10-01"
        end_date = f"2026-10-{cli_args.mtd:02d}"
    else:
        start_date = cli_args.start_date
        end_date = cli_args.end_date
    date_ranges = [{"startDate": start_date, "endDate": end_date}]

    print("[1/5] Khởi tạo xác thực Google Analytics 4...")
    token = get_access_token()
    print("✓ Xác thực thành công.")

    # 1. Kéo dữ liệu PagePath (PV, Users, PV/User, Engagement Duration)
    print(f"[2/5] Kéo dữ liệu PagePath ({start_date} -> {end_date})...")
    res_page = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "pagePath"}],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "totalUsers"},
            {"name": "screenPageViewsPerUser"},
            {"name": "userEngagementDuration"}
        ],
        "dimensionFilter": {
            "filter": {
                "fieldName": "pagePath",
                "stringFilter": {"matchType": "FULL_REGEXP", "value": "^/.*"}
            }
        },
        "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}],
        "limit": 5000
    })
    page_rows = res_page.get("rows", [])
    print(f"✓ Đã kéo {len(page_rows):,} URLs từ GA4 PagePath.")

    # 2. Kéo dữ liệu LandingPage (Sessions, TotalUsers, SessionsPerUser)
    print(f"[3/5] Kéo dữ liệu LandingPage Sessions & Re-entry frequency...")
    res_landing = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "metrics": [
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "sessionsPerUser"}
        ],
        "dimensionFilter": {
            "filter": {
                "fieldName": "landingPage",
                "stringFilter": {"matchType": "FULL_REGEXP", "value": "^/.*"}
            }
        },
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
        "limit": 5000
    })
    landing_map = {}
    for r in res_landing.get("rows", []):
        lp = normalize_path(r["dimensionValues"][0]["value"])
        s = int(r["metricValues"][0]["value"])
        u = int(r["metricValues"][1]["value"])
        spu = float(r["metricValues"][2]["value"])
        landing_map[lp] = {
            "landing_sessions": s,
            "landing_users": u,
            "landing_spu": spu
        }
    print(f"✓ Đã nạp {len(landing_map):,} Landing Pages mapping.")

    # 3. Kéo dữ liệu OneLink W2A Clicks theo URL
    print(f"[4/5] Kéo dữ liệu OneLink W2A Clicks theo URL...")
    res_w2a = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "pagePath"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 5000
    })
    w2a_map = defaultdict(int)
    for r in res_w2a.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cnt = int(r["metricValues"][0]["value"])
        w2a_map[p] += cnt
    print(f"✓ Đã tổng hợp OneLink W2A Clicks cho {len(w2a_map):,} URLs.")

    # 4. Phân tích & Gắn Metadata Dự án / Theme
    print("[5/5] Xử lý số liệu thuần túy (loại bỏ toàn bộ nhãn chủ quan)...")
    matcher = build_theme_matcher()

    items = []
    multi_session_count = 0
    in_session_repeat_count = 0

    for r in page_rows:
        raw_p = r["dimensionValues"][0]["value"].strip()
        p = normalize_path(raw_p)
        pv = int(r["metricValues"][0]["value"])
        u = int(r["metricValues"][1]["value"])

        if u < 50:  # Lọc các URL có dưới 50 user để tránh mẫu nhỏ gây nhiễu
            continue

        pv_per_u = float(r["metricValues"][2]["value"])
        dur = float(r["metricValues"][3]["value"])
        avg_dur = round(dur / u, 1) if u > 0 else 0.0

        lp_info = landing_map.get(p, {"landing_sessions": 0, "landing_users": 0, "landing_spu": 1.0})
        spu = lp_info["landing_spu"]
        ls = lp_info["landing_sessions"]
        lu = lp_info["landing_users"]

        w2a = w2a_map.get(p, 0)
        w2a_cr = round(w2a / pv, 4) if pv > 0 else 0.0

        tid, tname, sec, mvol, proj, ptype = matcher(p)

        is_multi_session = (spu >= 1.5)
        if is_multi_session:
            multi_session_count += 1
        elif pv_per_u >= 1.5:
            in_session_repeat_count += 1

        items.append({
            "path": p,
            "project_name": proj,
            "page_type": ptype,
            "theme_name": tname,
            "sector": sec,
            "total_users": u,
            "pageviews": pv,
            "pv_per_user": round(pv_per_u, 2),
            "landing_sessions": ls,
            "landing_users": lu,
            "sessions_per_user": round(spu, 2),
            "is_multi_session": is_multi_session,
            "avg_duration_sec": avg_dur,
            "w2a_clicks": w2a,
            "w2a_cr": w2a_cr
        })

    # Sắp xếp mặc định theo Pageviews giảm dần (các trang quan trọng nhất lên đầu)
    items.sort(key=lambda x: -x["pageviews"])

    total_analyzed = len(items)
    tot_pv = sum(x["pageviews"] for x in items)
    tot_users = sum(x["total_users"] for x in items)
    overall_pvu = round(tot_pv / tot_users, 2) if tot_users > 0 else 0.0

    payload = {
        "title": "Bảng Đo Lường URL Quay Trở Lại (MoMo Web Platform)",
        "generated_at": datetime.now().isoformat(),
        "period": {"start": start_date, "end": end_date},
        "summary": {
            "total_urls_analyzed": total_analyzed,
            "total_pageviews": tot_pv,
            "total_users": tot_users,
            "overall_pv_per_user": overall_pvu,
            "multi_session_urls_count": multi_session_count,
            "in_session_repeat_urls_count": in_session_repeat_count,
            "guide": {
                "sessions_per_user": "Tần suất mở phiên mới: Nếu >= 1.5, người dùng thực sự quay lại mở trang ở các ngày/phiên khác nhau.",
                "pv_per_user": "Số lượt xem/người: Nếu cao nhưng sessions_per_user = 1.0, người dùng chỉ xem lặp nội bộ trong 1 phiên duy nhất."
            }
        },
        "urls": items
    }

    # Xuất bản file:
    # 1. SSOT Knowledge Base
    kb_out = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "page_retention_matrix.json"
    kb_out.parent.mkdir(parents=True, exist_ok=True)
    with open(kb_out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã xuất bản SSOT Knowledge Base: {kb_out}")

    # 2. Web Hubs (react-web-momo)
    hubs_out = HUBS_REPO / "data" / "analytics" / "page-retention-matrix.json"
    hubs_out.parent.mkdir(parents=True, exist_ok=True)
    with open(hubs_out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
    print(f"✓ Đã xuất bản Web Hubs: {hubs_out} ({len(items):,} URLs)")

    # 3. Cập nhật vào full-funnel-matrix.json để đồng bộ toàn bộ view
    hubs_matrix = HUBS_REPO / "data" / "analytics" / "full-funnel-matrix.json"
    if hubs_matrix.exists():
        with open(hubs_matrix, "r", encoding="utf-8") as f:
            mat = json.load(f)
        mat["page_retention_summary"] = payload["summary"]
        mat["repeat_visitors"] = items
        with open(hubs_matrix, "w", encoding="utf-8") as f:
            json.dump(mat, f, ensure_ascii=False, separators=(",", ":"))
        print(f"✓ Đã tích hợp repeat_visitors vào {hubs_matrix}")

    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"HOÀN THÀNH XÂY DỰNG BẢNG ĐO LƯỜNG TRONG {elapsed:.1f} GIÂY")
    print(f"- Tổng số URLs phân tích (Users >= 50) : {total_analyzed:,}")
    print(f"- URLs có người mở lại phiên mới (>=1.5): {multi_session_count:,}")
    print(f"- URLs xem lặp trong phiên (PV/U >= 1.5)  : {in_session_repeat_count:,}")
    print("=" * 70)

if __name__ == "__main__":
    main()

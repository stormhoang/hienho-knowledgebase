#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HYBRID REPORT SYNC & CROSS-RECONCILIATION ENGINE
Tự động đối soát và hợp nhất 2 đầu dữ liệu Web Platform:
- Nguồn 1: File Excel Quản trị (BigQuery Connected Sheets trong Downloads/ hoặc 07_REPORTS/)
- Nguồn 2: Luồng GA4 Data API trực tiếp (Property 270743103)

Cơ chế vận hành tự động (Auto-Reconcile & Intelligent Fusion):
1. Đọc số ngày lũy kế và ma trận Pivot từ file Excel.
2. Truy vấn GA4 API cho cùng kỳ (để đối soát độ khớp) và ngày mới nhất (để bù đắp độ trễ).
3. Lập bảng đối soát chéo (Cross-Reconciliation Table) chỉ rõ độ lệch hoặc phần tăng thêm (Net Add).
4. Làm giàu (Enrich) số liệu Excel bằng các tầng API sâu: W2A OneLink Clicks, URL Retention Matrix.
5. Ghi đồng bộ vào toàn bộ hệ thống: Hubs /dashboard (web-data.json, summary.json), Excel SSOT, Markdown SSOT.
6. Tự động commit và đẩy lên GitHub Hubs qua REST API trong vòng 8-12 giây.
"""

import os
import sys
import glob
import json
import time
import argparse
import subprocess
import openpyxl
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
DOWNLOADS_DIR = Path("/Users/hienhv/Downloads")

sys.path.insert(0, str(BASE_DIR))
from scripts.sync_ga4_to_hubs import get_access_token, PROPERTY_ID, run_ga4_report
from scripts.build_full_funnel_matrix import build_theme_matcher
from scripts.sync_ga4_master import patch_excel_dynamic

TARGET_OCT = 3665607

def find_excel_file():
    patterns = [
        DOWNLOADS_DIR / "*[Ww]eb*[Pp]erformance*[Tt]racking*.xlsx",
        DOWNLOADS_DIR / "*[Tt]racking*.xlsx",
    ]
    matched = []
    for p in patterns:
        matched.extend(glob.glob(str(p)))
    if matched:
        matched.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return matched[0]
    ssot = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    if ssot.exists():
        return str(ssot)
    return None

def parse_excel_mtd(file_path):
    wb = openpyxl.load_workbook(file_path, data_only=True)
    
    # Check days elapsed
    days_elapsed = 22
    for sname in ["Overall Performance", "Vehicle"]:
        if sname in wb.sheetnames:
            c_val = wb[sname].cell(1, 1).value or wb[sname].cell(1, 2).value
            if c_val and "update to:" in str(c_val).lower():
                try:
                    days_elapsed = int(str(c_val).lower().replace("update to:", "").strip())
                    break
                except:
                    pass

    ws_pivot = wb["MTD Pivot"]
    col_idx = 9 # Col 9 is Oct 2026 MTD
    excel_total = 0
    for r in range(ws_pivot.max_row, 1, -1):
        c1 = ws_pivot.cell(r, 1).value
        if c1 and "grand total" in str(c1).lower():
            v = ws_pivot.cell(r, col_idx).value
            if v:
                excel_total = int(v)
            break

    channels = defaultdict(int)
    hubs = defaultdict(int)
    for r in range(3, ws_pivot.max_row):
        proj = ws_pivot.cell(r, 1).value
        if not proj or "grand total" in str(proj).lower():
            continue
        g_hub = ws_pivot.cell(r, 2).value or "Others"
        g_ch = ws_pivot.cell(r, 3).value or "Others"
        pv = ws_pivot.cell(r, col_idx).value or 0
        if pv:
            try:
                pv = int(pv)
                channels[str(g_ch).strip()] += pv
                hubs[str(g_hub).strip()] += pv
            except:
                pass

    return {
        "file": file_path,
        "days_elapsed": days_elapsed,
        "total_pv": excel_total,
        "channels": dict(channels),
        "hubs": dict(hubs)
    }

def fetch_ga4_mtd(days):
    now = datetime.now()
    start_date = f"{now.year}-{now.month:02d}-01"
    end_date = f"{now.year}-{now.month:02d}-{days:02d}"
    token = get_access_token()
    date_ranges = [{"startDate": start_date, "endDate": end_date}]

    # 1. Total
    res_prop = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "engagedSessions"},
            {"name": "userEngagementDuration"}
        ]
    })
    r0 = res_prop["rows"][0]
    total_pv = int(r0["metricValues"][0]["value"])
    total_sessions = int(r0["metricValues"][1]["value"])
    total_users = int(r0["metricValues"][2]["value"])
    total_engaged = int(r0["metricValues"][3]["value"])

    # 2. Channels & W2A
    res_ch = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "totalUsers"}],
        "limit": 10000
    })
    res_w2a = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [
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
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 10000
    })
    w2a_map = {(r["dimensionValues"][0]["value"], r["dimensionValues"][1]["value"]): int(r["metricValues"][0]["value"]) for r in res_w2a.get("rows", [])}

    channels_data = {}
    for r in res_ch.get("rows", []):
        ch = r["dimensionValues"][0]["value"]
        src = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        us = int(r["metricValues"][2]["value"])
        cl = w2a_map.get((ch, src), 0)
        channels_data[(ch, src)] = {"pv": pv, "sessions": sess, "users": us, "w2a": cl}

    return {
        "days_elapsed": days,
        "start_date": start_date,
        "end_date": end_date,
        "total_pv": total_pv,
        "total_sessions": total_sessions,
        "total_users": total_users,
        "total_engaged": total_engaged,
        "channels": channels_data,
        "total_w2a": sum(w2a_map.values())
    }

def run_hybrid_sync(force_mtd=None, no_push=False):
    start_time = time.time()
    print("=" * 80)
    print("KHỞI CHẠY HỆ THỐNG ĐỐI SOÁT & HỢP NHẤT DỮ LIỆU KÉP (HYBRID DATA SYNC)")
    print("=" * 80)

    # 1. Đọc Nguồn 1: Excel
    excel_path = find_excel_file()
    excel_data = parse_excel_mtd(excel_path) if excel_path else None
    excel_days = excel_data["days_elapsed"] if excel_data else 22
    excel_pv = excel_data["total_pv"] if excel_data else 0
    print(f"[1/5] Đã nạp Nguồn Excel ({excel_path}): MTD {excel_days} ngày | {excel_pv:,} PV")

    # 2. Đọc Nguồn 2: GA4 API
    now = datetime.now()
    yesterday_day = (now - timedelta(days=1)).day
    target_api_days = force_mtd or yesterday_day

    print(f"[2/5] Truy vấn GA4 Data API cho kỳ MTD {target_api_days} ngày...")
    api_latest = fetch_ga4_mtd(target_api_days)
    
    # Kéo thêm kỳ đối soát nếu ngày Excel khác ngày API mới nhất
    api_reconcile = api_latest if target_api_days == excel_days else fetch_ga4_mtd(excel_days)

    # 3. Đối soát chéo (Reconciliation)
    print("[3/5] Tiến hành đối soát chéo giữa BigQuery Excel và GA4 API...")
    delta_same_period = api_reconcile["total_pv"] - excel_pv
    pct_same_period = (delta_same_period / excel_pv * 100) if excel_pv > 0 else 0
    
    incremental_net_add = api_latest["total_pv"] - excel_pv if target_api_days > excel_days else 0

    reconciliation = {
        "excel_days": excel_days,
        "api_days": target_api_days,
        "excel_pv": excel_pv,
        "api_same_period_pv": api_reconcile["total_pv"],
        "delta_pv": delta_same_period,
        "delta_pct": round(pct_same_period, 4),
        "status": "KHỚP TUYỆT ĐỐI (100% MATCH)" if delta_same_period == 0 else f"LỆCH {delta_same_period:+d} PV ({pct_same_period:+.2f}%)",
        "latest_live_pv": api_latest["total_pv"],
        "incremental_net_add": incremental_net_add
    }

    # 4. Hợp nhất thông minh & Ghi SSOT / Web Hubs
    print(f"[4/5] Hợp nhất dữ liệu (Live MTD {target_api_days}d: {api_latest['total_pv']:,} PV) vào /dashboard...")
    
    # Chuẩn bị số kênh MTD mới nhất
    ch_map = api_latest["channels"]
    org_pv = 0
    dir_pv = 0
    paid_pv = 0
    ref_pv = 0
    oth_pv = 0
    for (ch, src), v in ch_map.items():
        cn = ch.lower()
        sn = src.lower()
        pv = v["pv"]
        if sn == "in_app" or sn.startswith("in_app"):
            ref_pv += pv
        elif "organic search" in cn:
            org_pv += pv
        elif "direct" in cn:
            dir_pv += pv
        elif "referral" in cn:
            ref_pv += pv
        elif any(x in cn for x in ["paid", "cpc", "display"]):
            paid_pv += pv
        else:
            oth_pv += pv
    non_paid_pv = org_pv + dir_pv + ref_pv + oth_pv

    daily_pace = round(api_latest["total_pv"] / target_api_days, 2)
    forecast_31d = round(daily_pace * 31, 2)
    forecast_pct = round((forecast_31d / TARGET_OCT) * 100, 2)
    progress_pct = round((api_latest["total_pv"] / TARGET_OCT) * 100, 2)
    daily_needed = round((TARGET_OCT - api_latest["total_pv"]) / max(1, 31 - target_api_days), 2)

    # 4.1 web-data.json: chỉ build-dashboard-data.py được ghi, gọi ở cuối script.
    # 4.2 Cập nhật summary.json
    summary_data = {
        "lastFull": {
            "month": "2026-09",
            "pv": 3952859,
            "prevPv": 3465363,
            "target": 3509044
        },
        "running": {
            "month": "2026-10",
            "daysElapsed": target_api_days,
            "daysInMonth": 31,
            "report": f"monthly_10_2026_mtd_{target_api_days}d.json",
            "pv": api_latest["total_pv"],
            "target": TARGET_OCT,
            "dailyPace": round(daily_pace),
            "dailyNeeded": round(daily_needed),
            "forecast": round(forecast_31d),
            "forecastPct": forecast_pct
        },
        "hubs": [
            {"id": "cinema", "name": "Cinema Hub", "pv": 889399},
            {"id": "financial", "name": "Financial Hub", "pv": 163850},
            {"id": "new_user", "name": "New User Hub", "pv": 92150},
            {"id": "vehicle", "name": "Vehicle Hub", "pv": 29740},
            {"id": "insurance", "name": "Insurance Hub", "pv": 27937},
            {"id": "student", "name": "Student Hub", "pv": 1892}
        ],
        "lastFullHubs": [
            {"id": "cinema", "name": "Cinema Hub", "pv": 1220075},
            {"id": "payment", "name": "Payment Hub", "pv": 520612},
            {"id": "home", "name": "Home MoMo", "pv": 467476},
            {"id": "new_user", "name": "New User Hub", "pv": 462878},
            {"id": "financial", "name": "Financial Hub", "pv": 249823},
            {"id": "travel", "name": "Travel Hub", "pv": 114475}
        ],
        "channels": {
            "organic": org_pv,
            "direct": dir_pv,
            "referral": ref_pv,
            "paid": paid_pv,
            "others": oth_pv
        }
    }
    # lib/dashboard/summary.json do build-dashboard-data.py ghi.
    with open(BASE_DIR / "07_REPORTS" / "data" / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_data, f, ensure_ascii=False, indent=2)

    # 4.3 Cập nhật Snapshot JSON
    snapshot_path = BASE_DIR / "07_REPORTS" / "data" / f"monthly_10_2026_mtd_{target_api_days}d.json"
    snapshot_payload = {
        "reconciliation": reconciliation,
        "file_source": f"Hybrid Fusion (Excel: {Path(excel_path).name if excel_path else 'N/A'} + GA4 Data API)",
        "read_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "days_elapsed": target_api_days,
        "days_in_month": 31,
        "target_oct_pv": TARGET_OCT,
        "actual_mtd_pv": api_latest["total_pv"],
        "progress_pct": progress_pct,
        "daily_pace": daily_pace,
        "forecast_31d": forecast_31d,
        "forecast_pct": forecast_pct,
        "users": api_latest["total_users"],
        "sessions": api_latest["total_sessions"],
        "total_w2a_clicks": api_latest["total_w2a"],
        "w2a_cvr_pct": round(api_latest["total_w2a"] / api_latest["total_pv"] * 100, 2),
        "channels": {
            "organic": {"pv": org_pv, "pct": round(org_pv / api_latest["total_pv"] * 100, 2)},
            "direct": {"pv": dir_pv, "pct": round(dir_pv / api_latest["total_pv"] * 100, 2)},
            "paid": {"pv": paid_pv, "pct": round(paid_pv / api_latest["total_pv"] * 100, 2)},
            "referral": {"pv": ref_pv, "pct": round(ref_pv / api_latest["total_pv"] * 100, 2)},
            "others": {"pv": oth_pv, "pct": round(oth_pv / api_latest["total_pv"] * 100, 2)},
            "non_paid_total": {"pv": non_paid_pv, "pct": round(non_paid_pv / api_latest["total_pv"] * 100, 2)}
        }
    }
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(snapshot_payload, f, ensure_ascii=False, indent=2)
    with open(BASE_DIR / "07_REPORTS" / "data" / "monthly_10_2026_consolidated.json", "w", encoding="utf-8") as f:
        json.dump(snapshot_payload, f, ensure_ascii=False, indent=2)

    # 4.4 Patch Excel Tracking SSOT (BigQuery Connected Sheets)
    bq_excel = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    if bq_excel.exists():
        patch_excel_dynamic(
            str(bq_excel), days_elapsed, total_pv,
            organic_pv, paid_pv, direct_pv, referral_pv, others_pv, non_paid_pv,
            hubs_pv, {}
        )

    # 4.5 Xuất bản lại file Excel Executive Presentation chuẩn 5 tabs
    build_script = BASE_DIR / "scripts" / "build_web_platform_performance.py"
    if build_script.exists():
        subprocess.run([sys.executable, str(build_script)], check=False)

    # 4.6 Tự động đồng bộ lên Google Drive công ty
    gdrive_script = BASE_DIR / "scripts" / "upload_to_gdrive.py"
    if gdrive_script.exists():
        try:
            print("[Auto-Drive] Đang tự động cập nhật Google Drive công ty...")
            subprocess.run([sys.executable, str(gdrive_script)], check=False)
        except Exception as e:
            print(f"[Auto-Drive] Lưu ý đồng bộ Drive: {e}")

    # 4.7 Tự động đồng bộ biến động 7 ngày SERP (Gainers & Losers) vào /report và /dashboard
    try:
        print("[Auto-7D-SERP] Đang đồng bộ biến động 7 ngày SERP (Gainers & Losers) vào /report & /dashboard...")
        sync_7d_script = BASE_DIR / "scripts" / "sync_7d_performance_report.py"
        if sync_7d_script.exists():
            subprocess.run([sys.executable, str(sync_7d_script), "--no-push"], check=False)
    except Exception as e:
        print(f"[Auto-7D-SERP] Lưu ý đồng bộ 7D SERP: {e}")

    # 5. Push GitHub qua REST API
    if not no_push:
        print("[5/5] Tự động đẩy dữ liệu hợp nhất lên GitHub Hubs...")
        push_script = BASE_DIR / "scripts" / "push_to_hubs_api.py"
        subprocess.run([
            sys.executable, str(push_script),
            "-m", f"data(hybrid-sync): reconcile Excel MTD {excel_days}d vs GA4 MTD {target_api_days}d ({api_latest['total_pv']:,} PV)"
        ], check=True)
    else:
        print("[5/5] Chế độ no-push: Bỏ qua đẩy GitHub.")

    elapsed = time.time() - start_time
    print("=" * 80)
    print(f"HOÀN THÀNH ĐỐI SOÁT & HỢP NHẤT TRONG {elapsed:.1f} GIÂY")
    print(f"- Nguồn 1 (Excel BigQuery) : MTD {excel_days}d = {excel_pv:,} PV")
    print(f"- Nguồn 2 (GA4 API Live)   : MTD {target_api_days}d = {api_latest['total_pv']:,} PV")
    print(f"- Trạng thái đối soát      : {reconciliation['status']}")
    if incremental_net_add > 0:
        print(f"- Phần bù ngày mới (Net add): +{incremental_net_add:,} PV (Cập nhật từ ngày {excel_days + 1} đến {target_api_days})")
    print(f"- Dự phóng 31 ngày         : {forecast_31d:,.0f} PV ({forecast_pct}% Target {TARGET_OCT:,})")
    print("=" * 80)

    return snapshot_payload

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mtd", type=int, default=None)
    parser.add_argument("--no-push", action="store_true")
    args = parser.parse_args()
    run_hybrid_sync(force_mtd=args.mtd, no_push=args.no_push)

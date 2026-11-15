#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT PAGE MTD BY URL
Xuất số liệu MTD theo từng URL ra 07_REPORTS/data/analytics/page_mtd.json
theo đúng đặc tả tại react-web-momo/data/analytics/SPEC-page-mtd.md.

Số liệu bao gồm:
- GA4 MTD tháng đang chạy (period)
- GA4 MTD cùng kỳ tháng trước (prev_period)
- GSC MTD mới nhất (gsc_period)
- Project chuẩn hóa từ url_project_resolver SSOT
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime
from collections import defaultdict
from google.oauth2 import service_account
from googleapiclient.discovery import build

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
import url_project_resolver as upr

OUT_FILE = os.path.join(BASE_DIR, "07_REPORTS", "data", "analytics", "page_mtd.json")
HUB_OUT_FILE = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/analytics/page_mtd.json"

# Kỳ số tự tính theo ngày chạy, để chạy lịch hằng ngày không phải sửa tay.
# - GA4: từ ngày 1 tới hôm qua (ngày 1 đầu tháng thì ra trọn tháng trước).
# - Cùng kỳ tháng trước: cùng số ngày, tháng ngắn hơn thì lấy hết tháng.
# - GSC: trễ dữ liệu ~3 ngày nên chốt tới hôm nay - 3.
# Ghi đè ngày chốt GA4: --end YYYY-MM-DD.
def _periods(end_arg=None):
    import calendar
    from datetime import date, timedelta
    end = date.fromisoformat(end_arg) if end_arg else date.today() - timedelta(days=1)
    start = end.replace(day=1)
    prev_last = start - timedelta(days=1)
    prev_start = prev_last.replace(day=1)
    prev_end = prev_start.replace(day=min(end.day, calendar.monthrange(prev_start.year, prev_start.month)[1]))
    gsc_end = end - timedelta(days=2)
    gsc_start = start if gsc_end >= start else gsc_end.replace(day=1)
    return [d.isoformat() for d in (start, end, prev_start, prev_end, gsc_start, gsc_end)]

def _end_arg():
    import argparse
    ap = argparse.ArgumentParser(description="Xuất page_mtd.json")
    ap.add_argument("--end", help="Ngày chốt GA4 (YYYY-MM-DD), mặc định hôm qua")
    return ap.parse_args().end

CURR_START, CURR_END, PREV_START, PREV_END, GSC_START, GSC_END = _periods(_end_arg() if __name__ == "__main__" else None)

def get_ga4_token():
    token_file = os.path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "ga4-token.json")
    creds_file = os.path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "ga4-credentials.json")
    with open(token_file, "r") as f:
        token_data = json.load(f)
    with open(creds_file, "r") as f:
        creds_data = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": creds_data["installed"]["client_id"],
        "client_secret": creds_data["installed"]["client_secret"],
        "refresh_token": token_data["refresh_token"],
        "grant_type": "refresh_token"
    }).encode()

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())["access_token"]

def fetch_ga4_pages(access_token, start_date, end_date):
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    pages = defaultdict(int)
    offset = 0
    limit = 10000
    print(f"-> Truy vấn GA4 ({start_date} tới {end_date})...")
    while True:
        payload = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "dimensions": [{"name": "pagePath"}],
            "metrics": [{"name": "screenPageViews"}],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "hostName",
                    "stringFilter": {"value": "www.momo.vn", "matchType": "EXACT"}
                }
            },
            "limit": limit,
            "offset": offset
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        })
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode())
            rows = res.get("rows", [])
            for r in rows:
                p = r["dimensionValues"][0]["value"]
                pv = int(r["metricValues"][0]["value"])
                pages[p] += pv
            if len(rows) < limit:
                break
            offset += limit
    print(f"   Đã lấy {len(pages)} unique pagePaths từ GA4.")
    return pages

def fetch_gsc_pages():
    print(f"-> Truy vấn GSC ({GSC_START} tới {GSC_END})...")
    key_file = os.path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "gsc-credentials.json")
    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    creds = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
    service = build("searchconsole", "v1", credentials=creds)

    pages = {}
    start_row = 0
    batch_size = 25000

    while True:
        body = {
            "startDate": GSC_START,
            "endDate": GSC_END,
            "dimensions": ["page"],
            "rowLimit": batch_size,
            "startRow": start_row
        }
        res = service.searchanalytics().query(siteUrl="https://www.momo.vn/", body=body).execute()
        rows = res.get("rows", [])
        for r in rows:
            page = r["keys"][0]
            clicks = int(r.get("clicks", 0))
            impressions = int(r.get("impressions", 0))
            position = float(r.get("position", 0))
            pages[page] = {"clicks": clicks, "impressions": impressions, "position": position}
        if len(rows) < batch_size:
            break
        start_row += batch_size
    print(f"   Đã lấy {len(pages)} unique URLs từ GSC.")
    return pages

def normalize_path(raw_url: str) -> str:
    # Bỏ domain
    p = raw_url.replace("https://www.momo.vn", "").replace("https://momo.vn", "").replace("http://www.momo.vn", "").replace("http://momo.vn", "")
    # Bỏ query string
    p = p.split("?")[0].split("#")[0].strip()
    if not p.startswith("/"):
        p = "/" + p
    # Bỏ trailing slash (trừ root '/')
    if len(p) > 1 and p.endswith("/"):
        p = p.rstrip("/")
    return p

def main():
    print("=" * 70)
    print("BẮT ĐẦU XUẤT SỐ MTD THEO URL (page_mtd.json)")
    print("=" * 70)

    # 1. Nạp GA4
    token = get_ga4_token()
    ga4_curr = fetch_ga4_pages(token, CURR_START, CURR_END)
    ga4_prev = fetch_ga4_pages(token, PREV_START, PREV_END)

    # 2. Nạp GSC
    gsc_data = fetch_gsc_pages()

    # 3. Nạp bộ luật DIM SSOT
    print("-> Nạp bộ quy tắc phân loại DIM SSOT...")
    rules = upr.load_rules()

    # 4. Gom nhóm theo clean path
    path_stats = defaultdict(lambda: {
        "pv": 0,
        "pv_prev": 0,
        "clicks": 0,
        "impressions": 0,
        "weighted_pos_sum": 0.0,
    })

    for raw_p, pv in ga4_curr.items():
        cp = normalize_path(raw_p)
        path_stats[cp]["pv"] += pv

    for raw_p, pv_p in ga4_prev.items():
        cp = normalize_path(raw_p)
        path_stats[cp]["pv_prev"] += pv_p

    for raw_u, g in gsc_data.items():
        cp = normalize_path(raw_u)
        path_stats[cp]["clicks"] += g["clicks"]
        path_stats[cp]["impressions"] += g["impressions"]
        path_stats[cp]["weighted_pos_sum"] += g["position"] * g["impressions"]

    print(f"-> Tổng hợp thành {len(path_stats)} normalized paths. Đang phân loại dự án...")

    # 5. Phân giải Project và lọc ngưỡng theo spec
    # Giữ mọi URL có pv + pv_prev >= 10 hoặc impressions >= 10
    pages_list = []
    vehicle_count = 0
    vehicle_pv = 0

    for cp, st in path_stats.items():
        pv = st["pv"]
        pv_prev = st["pv_prev"]
        clicks = st["clicks"]
        impressions = st["impressions"]

        if (pv + pv_prev < 10) and (impressions < 10):
            continue

        position = round(st["weighted_pos_sum"] / impressions, 1) if impressions > 0 else None

        full_url = "https://www.momo.vn" + cp
        res = upr.resolve(full_url, rules)
        proj = res.get("primary") or "Others"

        pages_list.append({
            "path": cp,
            "project": proj,
            "pv": pv,
            "pv_prev": pv_prev,
            "clicks": clicks,
            "impressions": impressions,
            "position": position
        })

        if proj in ["Phạt Nguội", "Nộp Phạt CSGT", "Tiện Ích Giao Thông", "Phí Không Dừng", "Bảo Hiểm Ô Tô", "Bảo Hiểm Xe Máy", "Cây xăng", "Giá xăng", "Trạm sạc", "Garage", "Hãng Xe"]:
            vehicle_count += 1
            vehicle_pv += pv

    # Sắp xếp theo pv giảm dần
    pages_list.sort(key=lambda x: x["pv"], reverse=True)

    print(f"-> Đã lọc được {len(pages_list)} URL thỏa điều kiện (pv+prev>=10 hoặc imp>=10).")
    print(f"   Trong đó Vehicle Hub: {vehicle_count} URL | Tổng PV: {vehicle_pv:,d} PVs.")

    # 6. Đóng gói JSON theo đúng spec
    out_data = {
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "period": {"start": CURR_START, "end": CURR_END},
        "prev_period": {"start": PREV_START, "end": PREV_END},
        "gsc_period": {"start": GSC_START, "end": GSC_END},
        "pages": pages_list
    }

    # 7. Ghi file
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi thành công vào KB: {OUT_FILE}")

    if os.path.exists(os.path.dirname(HUB_OUT_FILE)):
        with open(HUB_OUT_FILE, "w", encoding="utf-8") as f:
            json.dump(out_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã sao chép sang Hub repo: {HUB_OUT_FILE}")

    print("=" * 70)
    print("HOÀN TẤT XUẤT BẢN FILE PAGE_MTD.JSON!")
    print("=" * 70)

if __name__ == "__main__":
    main()

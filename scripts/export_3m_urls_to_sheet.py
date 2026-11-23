#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT 3-MONTH URL TRAFFIC DATA TO GOOGLE SHEETS
Nguồn dữ liệu: GA4 Data API (Property 270743103)
Đích: Google Sheets ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU
Tab name: URLs_Traffic_3M

Kỳ đối soát:
- Tổng thể: 01/08/2026 đến Hiện tại (3 tháng + MTD Tháng 11)
- Tháng 8/2026: 01/08/2026 - 31/08/2026
- Tháng 9/2026: 01/09/2026 - 30/09/2026
- Tháng 10/2026: 01/10/2026 - 31/10/2026
- Tháng 11/2026: 01/11/2026 - today
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.lib.url_project_resolver import (
    load_rules, load_inferred_rules, resolve, DEFAULT_CSV
)

# ---------------------------------------------------------------------------
# CẤU HÌNH XÁC THỰC VÀ ĐÍCH ĐẾN
# ---------------------------------------------------------------------------
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
SHEETS_TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
GA4_TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-token.json"

TARGET_SHEET_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"
TARGET_TAB_NAME = "URLs_Traffic_3M"
PROPERTY_ID = "270743103"


def get_oauth_token(token_path: Path) -> str:
    """Lấy Access Token từ refresh token tương ứng."""
    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        cdata = json.load(f)
    cinfo = cdata.get("installed") or cdata.get("web")

    with open(token_path, "r", encoding="utf-8") as f:
        tdata = json.load(f)

    body = urllib.parse.urlencode({
        "client_id": cinfo["client_id"],
        "client_secret": cinfo["client_secret"],
        "refresh_token": tdata["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))["access_token"]


def get_sheets_token() -> str:
    return get_oauth_token(SHEETS_TOKEN_FILE)


def get_ga4_token() -> str:
    return get_oauth_token(GA4_TOKEN_FILE)


# ---------------------------------------------------------------------------
# KÉO DỮ LIỆU TỪ GA4 DATA API
# ---------------------------------------------------------------------------
def run_ga4_query(token: str, payload: dict) -> dict:
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_all_ga4_traffic():
    """Kéo song song toàn bộ dữ liệu GA4 cho 3 tháng + MTD."""
    ga4_token = get_ga4_token()
    print("▶ Bắt đầu kéo dữ liệu từ GA4 Data API (Property 270743103)...")

    # 1. Kéo tổng thể 3 tháng (Pageviews, Sessions, Users)
    print("  1/6 Đang tải Tổng thể 3 tháng (01/08/2026 - today)...")
    body_overall = {
        "dateRanges": [{"startDate": "2026-08-01", "endDate": "today"}],
        "dimensions": [{"name": "pagePath"}],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"}
        ],
        "limit": 100000
    }
    res_overall = run_ga4_query(ga4_token, body_overall)
    overall_rows = res_overall.get("rows", [])
    print(f"    ✓ Đã tải {len(overall_rows):,} URLs tổng thể.")

    # 2. Kéo sự kiện W2A (Click to App / Outbound Onelink)
    print("  2/6 Đang tải sự kiện Chuyển đổi Web-to-App (W2A)...")
    body_w2a = {
        "dateRanges": [{"startDate": "2026-08-01", "endDate": "today"}],
        "dimensions": [{"name": "pagePath"}],
        "dimensionFilter": {
            "filter": {
                "fieldName": "eventName",
                "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    res_w2a = run_ga4_query(ga4_token, body_w2a)
    w2a_rows = res_w2a.get("rows", [])
    w2a_dict = {}
    for r in w2a_rows:
        path = r["dimensionValues"][0]["value"]
        clicks = int(r["metricValues"][0]["value"])
        w2a_dict[path] = w2a_dict.get(path, 0) + clicks
    print(f"    ✓ Đã tải {len(w2a_dict):,} URLs có phát sinh W2A clicks.")

    # 3. Kéo song song Pageviews từng tháng (T8, T9, T10, T11 MTD)
    monthly_ranges = [
        ("T8", "2026-08-01", "2026-08-31"),
        ("T9", "2026-09-01", "2026-09-30"),
        ("T10", "2026-10-01", "2026-10-31"),
        ("T11", "2026-11-01", "today"),
    ]

    monthly_pvs = {"T8": {}, "T9": {}, "T10": {}, "T11": {}}

    def fetch_month(item):
        label, s_date, e_date = item
        body = {
            "dateRanges": [{"startDate": s_date, "endDate": e_date}],
            "dimensions": [{"name": "pagePath"}],
            "metrics": [{"name": "screenPageViews"}],
            "limit": 100000
        }
        res = run_ga4_query(ga4_token, body)
        out = {}
        for r in res.get("rows", []):
            path = r["dimensionValues"][0]["value"]
            pv = int(r["metricValues"][0]["value"])
            out[path] = pv
        return label, out

    print("  3-6/6 Đang tải song song Pageviews Tháng 8, Tháng 9, Tháng 10, Tháng 11 MTD...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        for label, out in executor.map(fetch_month, monthly_ranges):
            monthly_pvs[label] = out
            print(f"    ✓ {label}: {len(out):,} URLs.")

    return overall_rows, w2a_dict, monthly_pvs


# ---------------------------------------------------------------------------
# MAPPING TAXONOMY: URL -> DỰ ÁN & HUB
# ---------------------------------------------------------------------------
def build_taxonomy_mappings():
    """Nạp hub-map.json và thiết lập bộ định tuyến URL sang Hub và Project."""
    hub_map_path = BASE_DIR.parent / "Web-Idea" / "react-web-momo" / "lib" / "dashboard" / "hub-map.json"
    if not hub_map_path.exists():
        hub_map_path = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/hub-map.json")

    proj_to_hub = {}
    if hub_map_path.exists():
        with open(hub_map_path, "r", encoding="utf-8") as f:
            hm = json.load(f)
            for h in hm.get("hubs", []):
                hname = h.get("name") or h.get("id")
                for p in h.get("projects", []):
                    p_clean = p.strip()
                    proj_to_hub[p_clean] = hname
                    proj_to_hub[p_clean.lower()] = hname

    rules = load_rules(DEFAULT_CSV)
    inferred = load_inferred_rules(rules)

    def resolve_hub(primary: str, path: str) -> str:
        if primary and primary in proj_to_hub:
            return proj_to_hub[primary]
        if primary and primary.lower() in proj_to_hub:
            return proj_to_hub[primary.lower()]

        p = path.lower()
        if p.startswith("/cinema"):
            return "Cinema Hub"
        if any(p.startswith(x) for x in ["/ve-xe", "/du-lich-di-lai", "/ve-may-bay", "/ve-tau-hoa"]):
            return "Travel Hub"
        if any(p.startswith(x) for x in ["/bao-hiem", "/bhyt", "/bhxh"]):
            return "Insurance Hub"
        if any(p.startswith(x) for x in [
            "/cong-dong-tai-chinh", "/vay-", "/tiet-kiem", "/chung-khoan",
            "/vi-tra-sau", "/tra-gop", "/the-tin-dung", "/gia-vang", "/ty-gia"
        ]):
            return "Financial Hub"
        if any(p.startswith(x) for x in ["/tin-tuc", "/blog"]):
            return "Home MoMo"
        if any(p.startswith(x) for x in ["/hoi-dap", "/huong-dan"]):
            return "Support Hub"
        if any(p.startswith(x) for x in ["/nap-the", "/the-cao", "/nap-dien-thoai", "/data"]):
            return "Telco Hub"
        if any(p.startswith(x) for x in ["/thanh-toan-hoa-don", "/bill"]):
            return "Billpay Hub"
        if any(p.startswith(x) for x in ["/download", "/tai-app"]):
            return "Download"
        return "Others"

    return rules, inferred, resolve_hub


def process_url_records(overall_rows, w2a_dict, monthly_pvs):
    """Xử lý, làm sạch và gắn nhãn cho toàn bộ URL."""
    rules, inferred, resolve_hub = build_taxonomy_mappings()
    print("▶ Đang mapping taxonomy Hub và Project cho toàn bộ URLs...")

    records = []
    for r in overall_rows:
        path = r["dimensionValues"][0]["value"]
        total_pv = int(r["metricValues"][0]["value"])
        sessions = int(r["metricValues"][1]["value"])
        total_users = int(r["metricValues"][2]["value"])

        # Mapping taxonomy
        match_info = resolve(path, rules, inferred)
        project = match_info.get("primary") or "Chưa phân loại"
        hub = resolve_hub(project, path)

        # Monthly breakdown
        pv_t8 = monthly_pvs["T8"].get(path, 0)
        pv_t9 = monthly_pvs["T9"].get(path, 0)
        pv_t10 = monthly_pvs["T10"].get(path, 0)
        pv_t11 = monthly_pvs["T11"].get(path, 0)

        # W2A
        w2a_clicks = w2a_dict.get(path, 0)
        w2a_cvr = round(w2a_clicks / sessions, 4) if sessions > 0 else 0.0

        full_url = f"https://www.momo.vn{path}"

        records.append({
            "path": path,
            "url": full_url,
            "hub": hub,
            "project": project,
            "total_pv": total_pv,
            "pv_t8": pv_t8,
            "pv_t9": pv_t9,
            "pv_t10": pv_t10,
            "pv_t11": pv_t11,
            "sessions": sessions,
            "total_users": total_users,
            "w2a_clicks": w2a_clicks,
            "w2a_cvr": w2a_cvr
        })

    # Sắp xếp giảm dần theo Tổng Pageviews
    records.sort(key=lambda x: x["total_pv"], reverse=True)
    print(f"✓ Đã chuẩn bị {len(records):,} dòng dữ liệu hoàn chỉnh.")
    return records


# ---------------------------------------------------------------------------
# GOOGLE SHEETS API: TẠO TAB & ĐỒNG BỘ DỮ LIỆU
# ---------------------------------------------------------------------------
def api_request(token: str, url: str, method: str = "GET", payload: dict = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"[API ERROR {e.code}] {err_msg}")
        raise


def setup_sheet_tab(token: str, total_rows_needed: int) -> int:
    """Kiểm tra sheet tab, tạo mới hoặc resize nếu cần, trả về sheetId."""
    print(f"▶ Kiểm tra tab '{TARGET_TAB_NAME}' trên Google Sheets...")
    meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}?fields=sheets.properties"
    meta = api_request(token, meta_url)

    target_sheet_id = None
    existing_rows = 0

    for s in meta.get("sheets", []):
        p = s["properties"]
        if p["title"] == TARGET_TAB_NAME:
            target_sheet_id = p["sheetId"]
            existing_rows = p.get("gridProperties", {}).get("rowCount", 1000)
            break

    batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    required_rows = total_rows_needed + 500

    if target_sheet_id is None:
        print(f"  Tạo mới tab '{TARGET_TAB_NAME}' ({required_rows:,} hàng, 15 cột)...")
        add_req = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": TARGET_TAB_NAME,
                            "gridProperties": {
                                "rowCount": required_rows,
                                "columnCount": 15,
                                "frozenRowCount": 1
                            },
                            "tabColor": {
                                "red": 0.85,
                                "green": 0.15,
                                "blue": 0.5
                            }
                        }
                    }
                }
            ]
        }
        res = api_request(token, batch_url, method="POST", payload=add_req)
        target_sheet_id = res["replies"][0]["addSheet"]["properties"]["sheetId"]
        print(f"  ✓ Đã tạo tab mới thành công (Sheet ID: {target_sheet_id})")
    else:
        print(f"  ✓ Tìm thấy tab '{TARGET_TAB_NAME}' sẵn có (Sheet ID: {target_sheet_id}).")
        # Resize nếu số hàng hiện tại chưa đủ
        if existing_rows < required_rows:
            print(f"  Mở rộng số hàng từ {existing_rows:,} lên {required_rows:,}...")
            resize_req = {
                "requests": [
                    {
                        "updateSheetProperties": {
                            "properties": {
                                "sheetId": target_sheet_id,
                                "gridProperties": {
                                    "rowCount": required_rows,
                                    "columnCount": 15,
                                    "frozenRowCount": 1
                                }
                            },
                            "fields": "gridProperties(rowCount,columnCount,frozenRowCount)"
                        }
                    }
                ]
            }
            api_request(token, batch_url, method="POST", payload=resize_req)

    # Định dạng Header và Cột
    format_requests = [
        # Format Header Row (A1:N1)
        {
            "repeatCell": {
                "range": {
                    "sheetId": target_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 14
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 0.12, "green": 0.16, "blue": 0.22},  # Dark navy #1F2937
                        "textFormat": {
                            "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                            "bold": True,
                            "fontSize": 10
                        },
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
            }
        },
        # Định dạng số cho các cột chỉ số (Cols F-M: #,##0)
        {
            "repeatCell": {
                "range": {
                    "sheetId": target_sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": required_rows,
                    "startColumnIndex": 5,
                    "endColumnIndex": 13
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "#,##0"
                        },
                        "horizontalAlignment": "RIGHT"
                    }
                },
                "fields": "userEnteredFormat(numberFormat,horizontalAlignment)"
            }
        },
        # Định dạng CVR % cho Cột N (Index 13: 0.00%)
        {
            "repeatCell": {
                "range": {
                    "sheetId": target_sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": required_rows,
                    "startColumnIndex": 13,
                    "endColumnIndex": 14
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "PERCENT",
                            "pattern": "0.00%"
                        },
                        "horizontalAlignment": "RIGHT"
                    }
                },
                "fields": "userEnteredFormat(numberFormat,horizontalAlignment)"
            }
        },
        # Chiều rộng các cột
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1}, "properties": {"pixelSize": 60}, "fields": "pixelSize"}},    # STT
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 2}, "properties": {"pixelSize": 340}, "fields": "pixelSize"}},   # URL
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 2, "endIndex": 3}, "properties": {"pixelSize": 280}, "fields": "pixelSize"}},   # Path
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 3, "endIndex": 4}, "properties": {"pixelSize": 140}, "fields": "pixelSize"}},   # Hub
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 4, "endIndex": 5}, "properties": {"pixelSize": 170}, "fields": "pixelSize"}},   # Project
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 5, "endIndex": 6}, "properties": {"pixelSize": 125}, "fields": "pixelSize"}},   # Tổng PV
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 6, "endIndex": 7}, "properties": {"pixelSize": 110}, "fields": "pixelSize"}},   # PV T8
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 7, "endIndex": 8}, "properties": {"pixelSize": 110}, "fields": "pixelSize"}},   # PV T9
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 8, "endIndex": 9}, "properties": {"pixelSize": 110}, "fields": "pixelSize"}},   # PV T10
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 9, "endIndex": 10}, "properties": {"pixelSize": 115}, "fields": "pixelSize"}},  # PV T11 MTD
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 10, "endIndex": 11}, "properties": {"pixelSize": 120}, "fields": "pixelSize"}}, # Sessions
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 11, "endIndex": 12}, "properties": {"pixelSize": 120}, "fields": "pixelSize"}}, # Users
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 12, "endIndex": 13}, "properties": {"pixelSize": 120}, "fields": "pixelSize"}}, # W2A Clicks
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "COLUMNS", "startIndex": 13, "endIndex": 14}, "properties": {"pixelSize": 110}, "fields": "pixelSize"}}, # W2A CVR
        # Đặt chiều cao hàng Header (Row 1: 36px)
        {"updateDimensionProperties": {"range": {"sheetId": target_sheet_id, "dimension": "ROWS", "startIndex": 0, "endIndex": 1}, "properties": {"pixelSize": 36}, "fields": "pixelSize"}}
    ]

    print("  Áp dụng thiết lập định dạng bảng và chiều rộng cột...")
    api_request(token, batch_url, method="POST", payload={"requests": format_requests})
    print("  ✓ Đã định dạng Header, cột số và đóng băng dòng 1 thành công.")

    return target_sheet_id


def upload_data_batches(token: str, records: list, batch_size: int = 10000):
    """Tải toàn bộ dữ liệu lên Google Sheets theo từng batch 10,000 hàng."""
    header = [
        "STT",
        "URL Đầy Đủ",
        "Đường Dẫn (Page Path)",
        "Hub Phụ Trách",
        "Dự Án (Project)",
        "Tổng Pageviews (3M+MTD)",
        "PV Tháng 8/2026",
        "PV Tháng 9/2026",
        "PV Tháng 10/2026",
        "PV Tháng 11/2026 (MTD)",
        "Tổng Sessions",
        "Tổng Người Dùng (Users)",
        "Lượt Click Vào App (W2A)",
        "Tỷ Lệ Chuyển Đổi (W2A CVR)"
    ]

    # Chuẩn bị toàn bộ dòng dữ liệu
    all_rows = [header]
    for idx, r in enumerate(records, start=1):
        all_rows.append([
            idx,
            r["url"],
            r["path"],
            r["hub"],
            r["project"],
            r["total_pv"],
            r["pv_t8"],
            r["pv_t9"],
            r["pv_t10"],
            r["pv_t11"],
            r["sessions"],
            r["total_users"],
            r["w2a_clicks"],
            r["w2a_cvr"]
        ])

    total_rows = len(all_rows)
    print(f"▶ Bắt đầu đẩy {total_rows:,} hàng dữ liệu lên Google Sheets...")

    # Upload theo từng batch
    for start_idx in range(0, total_rows, batch_size):
        end_idx = min(start_idx + batch_size, total_rows)
        chunk = all_rows[start_idx:end_idx]

        row_start_sheet = start_idx + 1
        row_end_sheet = end_idx
        range_str = f"{TARGET_TAB_NAME}!A{row_start_sheet}:N{row_end_sheet}"

        url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(range_str)}?valueInputOption=USER_ENTERED"
        payload = {
            "range": range_str,
            "majorDimension": "ROWS",
            "values": chunk
        }

        t0 = time.time()
        api_request(token, url, method="PUT", payload=payload)
        dt = time.time() - t0
        print(f"  ✓ Đã ghi hàng {row_start_sheet:,} đến {row_end_sheet:,} ({len(chunk):,} hàng) trong {dt:.2f}s")


# ---------------------------------------------------------------------------
# MAIN WORKFLOW
# ---------------------------------------------------------------------------
def main():
    t_start = time.time()
    print("=" * 70)
    print("XUẤT TOÀN BỘ URL CÓ TRAFFIC 3 THÁNG VÀO GOOGLE SHEETS")
    print(f"Mục tiêu: {TARGET_SHEET_ID} | Tab: {TARGET_TAB_NAME}")
    print("=" * 70)

    # 1. Kéo dữ liệu GA4
    overall_rows, w2a_dict, monthly_pvs = fetch_all_ga4_traffic()

    # 2. Xử lý dữ liệu & mapping taxonomy
    records = process_url_records(overall_rows, w2a_dict, monthly_pvs)

    # 3. Kết nối Google Sheets & chuẩn bị tab
    sheets_token = get_sheets_token()
    sheet_id = setup_sheet_tab(sheets_token, len(records))

    # 4. Tải dữ liệu theo batch
    upload_data_batches(sheets_token, records, batch_size=10000)

    # 5. Thống kê tổng hợp
    total_pv_all = sum(r["total_pv"] for r in records)
    total_sessions_all = sum(r["sessions"] for r in records)
    total_w2a_all = sum(r["w2a_clicks"] for r in records)
    avg_cvr = round(total_w2a_all / total_sessions_all * 100, 2) if total_sessions_all > 0 else 0.0

    total_time = time.time() - t_start
    print("=" * 70)
    print(f"✓ HOÀN THÀNH XUẤT DỮ LIỆU TRONG {total_time:.2f} GIÂY!")
    print(f" - Tổng số URL có traffic: {len(records):,} URLs")
    print(f" - Tổng Pageviews (3M+MTD): {total_pv_all:,}")
    print(f" - Tổng Sessions: {total_sessions_all:,}")
    print(f" - Tổng W2A Clicks: {total_w2a_all:,}")
    print(f" - W2A CVR trung bình toàn Web: {avg_cvr}%")
    print(f" - Đường dẫn xem trực tiếp: https://docs.google.com/spreadsheets/d/{TARGET_SHEET_ID}/edit#gid={sheet_id}")
    print("=" * 70)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC CINEMA PERFORMANCE SHEET - NOVEMBER 2026 MTD
Đồng bộ số liệu hiệu suất Tháng 11 (MTD 4 ngày) từ Master Tracking Sheet sang Cinema Roadmap Sheet:
- Master Sheet ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU (tab 'Cinema')
- Cinema Sheet ID: 1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg (tabs 'Web Performances' & 'Cinema')
- Local Excel SSOT: 05_HUBS/cinema/cinema_hub_roadmap_drive_sync.xlsx
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR / "scripts"))
from sync_to_google_sheet_api import get_sheets_token
from sync_cinema_roadmap_sheet import pull_all_to_local

MASTER_SPREADSHEET_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"
CINEMA_SPREADSHEET_ID = "1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg"

def get_sheet_values(sheet_id, range_name, opt="FORMATTED_VALUE", token=None):
    if not token:
        token = get_sheets_token()
    encoded = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{encoded}?valueRenderOption={opt}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8")).get("values", [])

def update_sheet_values(sheet_id, range_name, values, token=None):
    if not token:
        token = get_sheets_token()
    encoded = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{encoded}?valueInputOption=USER_ENTERED"
    payload = json.dumps({"range": range_name, "values": values}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, method="PUT")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def clear_sheet_range(sheet_id, range_name, token=None):
    if not token:
        token = get_sheets_token()
    encoded = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{encoded}:clear"
    req = urllib.request.Request(url, data=b"{}", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    print("1. Lấy token Google Sheets...")
    token = get_sheets_token()

    print("2. Đọc dữ liệu Master Sheet (tab Cinema)...")
    master_unformatted = get_sheet_values(MASTER_SPREADSHEET_ID, "Cinema!A1:R47", "UNFORMATTED_VALUE", token)

    print("3. Đọc cấu trúc công thức Cinema Sheet hiện tại...")
    cinema_formulas = get_sheet_values(CINEMA_SPREADSHEET_ID, "Cinema!A1:R47", "FORMULA", token)

    print("4. Xây dựng ma trận dữ liệu hợp nhất (Preserve Formulas + Sync Evaluated Channel Values)...")
    grid = []
    for r in range(47):
        row = []
        m_unf_row = master_unformatted[r] if r < len(master_unformatted) else []
        c_form_row = cinema_formulas[r] if r < len(cinema_formulas) else []
        for c in range(18):
            c_form = c_form_row[c] if c < len(c_form_row) else ""
            m_val = m_unf_row[c] if c < len(m_unf_row) else ""
            
            # Nếu ô có công thức chuẩn nội bộ thì giữ nguyên công thức
            if str(c_form).startswith("="):
                row.append(c_form)
            else:
                row.append(m_val)
        grid.append(row)

    # Đảm bảo header B1 là 'Update to: 4'
    grid[0][1] = "Update to: 4"

    print("5. Đẩy dữ liệu lên sheet 'Web Performances'...")
    res_perf = update_sheet_values(CINEMA_SPREADSHEET_ID, "Web Performances!A1:R47", grid, token)
    print("   -> Đã cập nhật Web Performances:", res_perf.get("updatedCells"), "cells")

    print("6. Xóa dòng thừa row 48 trên sheet 'Web Performances'...")
    clear_sheet_range(CINEMA_SPREADSHEET_ID, "Web Performances!A48:S50", token)
    print("   -> Đã xóa vùng Web Performances!A48:S50")

    print("7. Đẩy dữ liệu lên sheet 'Cinema'...")
    res_cin = update_sheet_values(CINEMA_SPREADSHEET_ID, "Cinema!A1:R47", grid, token)
    print("   -> Đã cập nhật Cinema:", res_cin.get("updatedCells"), "cells")

    print("8. Kiểm tra lại kết quả thực tế trên Cloud (Web Performances)...")
    val_check = get_sheet_values(CINEMA_SPREADSHEET_ID, "Web Performances!A1:R47", "FORMATTED_VALUE", token)
    print(f"   Header B1: {val_check[0][1]}")
    print(f"   Target T11 (R2): {val_check[1][17]}")
    print(f"   Actual T11 (R3): {val_check[2][17]}")
    print(f"   Net Change (R4): {val_check[3][17]}")
    print(f"   Growth Rate (R5): {val_check[4][17]}")
    print(f"   Gap T11 (R6): {val_check[5][17]}")
    print(f"   Trang Rạp phim (R8): {val_check[7][17]}")
    print(f"   Trang Chi tiết phim (R15): {val_check[14][17]}")
    print(f"   Blog Phim (R22): {val_check[21][17]}")
    print(f"   Trang chủ Cinema (R29): {val_check[28][17]}")
    print(f"   Tin tức Phim (R36): {val_check[35][17]}")
    print(f"   Landing Page (R43): {val_check[42][17]}")

    print("9. Đồng bộ toàn bộ dữ liệu về Local Excel SSOT và JSON...")
    pull_all_to_local()
    print("-> HOÀN TẤT ĐỒNG BỘ 100% THÁNH CÔNG!")

if __name__ == "__main__":
    main()

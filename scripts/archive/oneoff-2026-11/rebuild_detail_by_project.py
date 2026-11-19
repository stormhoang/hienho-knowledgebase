#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REBUILD PROJECT DETAIL FLOW ACCORDING TO USER MOCKUP
Tái cấu trúc toàn diện sheet 'Projects Detail Flow' theo layout Project x Channel:
- Mỗi dự án/Hub là một khối 10 dòng (Page views, Net change, % Growth rate, Tỷ trọng, Organic, Paid, Direct, Referral, Others)
- Header Bar dự án màu xanh nhạt (#D2E3FC)
- Khối MTD (Cols B..M) và Full Month (Cols O..Z)
- Cột Vs. SPLM (Col N và Col AA) với chỉ báo ▲ / ▼ và màu xanh/đỏ chuẩn xác
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID

SHEET_TITLE = "Projects Detail Flow"
SHEET_ID = 316527624

# Date serial numbers for 2026 (Jan..Dec)
MONTH_SERIALS = [46023, 46054, 46082, 46113, 46143, 46174, 46204, 46235, 46266, 46296, 46327, 46357]
MONTH_NAMES = ["Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "Oct 26", "Nov 26", "Dec 26"]

MTD_DATA_COLS = ["F", "G", "H", "I", "J", "K"] # May..Oct (cols 5..10)
FULL_DATA_COLS = ["S", "T", "U", "V", "W", "X"] # May..Oct (cols 18..23)

# Projects ordered by Oct traffic descending (matching screenshot: Cinema Hub, Download, Home MoMo)
PROJECTS = [
    "Cinema Hub",
    "Download",
    "Home MoMo",
    "Financial Hub",
    "Game",
    "Tiktok",
    "New User",
    "Hỏi đáp",
    "Merchant",
    "Vé Xe",
    "Vehicle Hub",
    "Guide",
    "Nước",
    "OTA",
    "Insurance Hub",
    "Application Store",
    "Khuyến mãi",
    "Vé số",
    "Sim",
    "Blog",
    "Tìm Kiếm",
    "Soundbox",
    "Campaign",
    "Trust",
    "Data",
    "Billpay",
    "P2P",
    "Dịch vụ liên kết",
    "Tin Tức",
    "Điện",
    "Hoàn Tiền Mua Sắm",
    "Cross Border",
    "Mở tài khoản ngân hàng",
    "Student Hub",
    "TnC",
    "Others"
]

def get_channel_filter(p_name, pivot_sheet="MTD Pivot"):
    """Trả về biểu thức lọc dự án trong SUMPRODUCT."""
    if p_name == "Cinema Hub":
        return f"('{pivot_sheet}'!$B$3:$B$400=\"Cinema Hub\")"
    elif p_name == "Financial Hub":
        return f"('{pivot_sheet}'!$B$3:$B$400=\"Financial Hub\")"
    elif p_name == "Vehicle Hub":
        return (
            f"(('{pivot_sheet}'!$A$3:$A$400=\"Phạt nguội\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Phạt Nguội\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Ô Tô\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Xe Máy\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Tiện Ích Giao Thông\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Phí Không Dừng\") > 0)"
        )
    elif p_name == "Insurance Hub":
        return (
            f"(('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Y Tế\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Sức Khỏe\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Xã Hội\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm\") > 0)"
        )
    elif p_name == "Student Hub":
        return (
            f"(('{pivot_sheet}'!$B$3:$B$400=\"Student Hub\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Student Hub\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Student Pass\") > 0)"
        )
    elif p_name == "Sim":
        return (
            f"(('{pivot_sheet}'!$B$3:$B$400=\"Sim\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Sim\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Esim\") > 0)"
        )
    else:
        return f"(('{pivot_sheet}'!$B$3:$B$400=$A${{r_proj}}) + ('{pivot_sheet}'!$A$3:$A$400=$A${{r_proj}}) > 0)"

def build_sheet_data():
    """Tạo toàn bộ dữ liệu (27 cột A..AA) cho sheet."""
    rows = []

    # ROW 1: Super Headers
    r1 = ["Web Performance - Detail by Project - Update MTD"]
    r1.append("MTD (Month to date)")
    r1.extend([""] * 11) # C1..M1 merged with B1
    r1.append("Vs. SPLM") # N1
    r1.append("Full month") # O1
    r1.extend([""] * 11) # P1..Z1 merged with O1
    r1.append("Vs. SPLM") # AA1
    rows.append(r1)

    # ROW 2: Column Headers
    r2 = ["Chỉ số"]
    r2.extend(MONTH_SERIALS) # B2..M2
    r2.append("MTD vs. cùng kỳ") # N2
    r2.extend(MONTH_SERIALS) # O2..Z2
    r2.append("Full vs. cùng kỳ") # AA2
    rows.append(r2)

    # Project Blocks (starting at Row 3)
    current_row = 3
    block_info = []

    for p_name in PROJECTS:
        r_proj = current_row
        r_pv = r_proj + 1
        r_net = r_proj + 2
        r_growth = r_proj + 3
        r_share = r_proj + 4
        r_org = r_proj + 5
        r_paid = r_proj + 6
        r_dir = r_proj + 7
        r_ref = r_proj + 8
        r_oth = r_proj + 9
        r_blank = r_proj + 10

        block_info.append({
            "name": p_name,
            "r_proj": r_proj,
            "r_pv": r_pv,
            "r_net": r_net,
            "r_growth": r_growth,
            "r_share": r_share,
            "r_org": r_org,
            "r_paid": r_paid,
            "r_dir": r_dir,
            "r_ref": r_ref,
            "r_oth": r_oth,
            "r_blank": r_blank
        })

        # 1. Project Header Row
        p_row = [p_name] + [""] * 26
        rows.append(p_row)

        # 2. Page views Row
        pv_row = ["Page views"]
        # MTD Jan..Apr
        pv_row.extend(["", "", "", ""])
        # MTD May..Oct: =SUM(F{r_org}:F{r_oth})
        for c in MTD_DATA_COLS:
            pv_row.append(f"=SUM({c}{r_org}:{c}{r_oth})")
        # MTD Nov..Dec
        pv_row.extend(["", ""])
        # Col N: MTD vs. cùng kỳ (=Oct/Sep - 1)
        pv_row.append(f'=IFERROR((K{r_pv}-J{r_pv})/J{r_pv}, "")')
        # Full Jan..Apr
        pv_row.extend(["", "", "", ""])
        # Full May..Oct: =SUM(S{r_org}:S{r_oth})
        for c in FULL_DATA_COLS:
            pv_row.append(f"=SUM({c}{r_org}:{c}{r_oth})")
        # Full Nov..Dec
        pv_row.extend(["", ""])
        # Col AA: Full vs. cùng kỳ (=Oct/Sep - 1)
        pv_row.append(f'=IFERROR((X{r_pv}-W{r_pv})/W{r_pv}, "")')
        rows.append(pv_row)

        # 3. Net change Row
        net_row = ["  Net change"]
        # MTD Jan..May: ""
        net_row.extend(["", "", "", "", ""])
        # MTD Jun..Oct: =Curr - Prev
        prev_cols_mtd = ["F", "G", "H", "I", "J"]
        curr_cols_mtd = ["G", "H", "I", "J", "K"]
        for pc, cc in zip(prev_cols_mtd, curr_cols_mtd):
            net_row.append(f'=IF(AND(ISNUMBER({cc}{r_pv}), ISNUMBER({pc}{r_pv}), {pc}{r_pv}>0), {cc}{r_pv}-{pc}{r_pv}, "")')
        # MTD Nov..Dec + Col N
        net_row.extend(["", "", ""])
        # Full Jan..May: ""
        net_row.extend(["", "", "", "", ""])
        # Full Jun..Oct: =Curr - Prev
        prev_cols_full = ["S", "T", "U", "V", "W"]
        curr_cols_full = ["T", "U", "V", "W", "X"]
        for pc, cc in zip(prev_cols_full, curr_cols_full):
            net_row.append(f'=IF(AND(ISNUMBER({cc}{r_pv}), ISNUMBER({pc}{r_pv}), {pc}{r_pv}>0), {cc}{r_pv}-{pc}{r_pv}, "")')
        # Full Nov..Dec + Col AA
        net_row.extend(["", "", ""])
        rows.append(net_row)

        # 4. % Growth rate Row
        gr_row = ["  % Growth rate"]
        # MTD Jan..May: ""
        gr_row.extend(["", "", "", "", ""])
        # MTD Jun..Oct: = (Curr - Prev) / Prev
        for pc, cc in zip(prev_cols_mtd, curr_cols_mtd):
            gr_row.append(f'=IFERROR(({cc}{r_pv}-{pc}{r_pv})/{pc}{r_pv}, "")')
        # MTD Nov..Dec + Col N
        gr_row.extend(["", "", ""])
        # Full Jan..May: ""
        gr_row.extend(["", "", "", "", ""])
        # Full Jun..Oct: = (Curr - Prev) / Prev
        for pc, cc in zip(prev_cols_full, curr_cols_full):
            gr_row.append(f'=IFERROR(({cc}{r_pv}-{pc}{r_pv})/{pc}{r_pv}, "")')
        # Full Nov..Dec + Col AA
        gr_row.extend(["", "", ""])
        rows.append(gr_row)

        # 5. Tỷ trọng trong tổng traffic Row
        share_row = ["Tỷ trọng trong tổng traffic"]
        # MTD Jan..Apr: ""
        share_row.extend(["", "", "", ""])
        # MTD May..Oct: =PV / Grand Total
        for c in MTD_DATA_COLS:
            share_row.append(f"=IFERROR({c}{r_pv}/INDEX('MTD Pivot'!$D$3:$K$400, MATCH(\"Grand Total\", 'MTD Pivot'!$A$3:$A$400, 0), MATCH({c}$2, 'MTD Pivot'!$D$2:$K$2, 0)), \"\")")
        # MTD Nov..Dec
        share_row.extend(["", ""])
        # Col N: Oct % - Sep %
        share_row.append(f'=IFERROR(K{r_share}-J{r_share}, "")')
        # Full Jan..Apr: ""
        share_row.extend(["", "", "", ""])
        # Full May..Oct: =PV / Grand Total Full
        for c in FULL_DATA_COLS:
            share_row.append(f"=IFERROR({c}{r_pv}/INDEX('Full month Pivot'!$D$3:$K$400, MATCH(\"Grand Total\", 'Full month Pivot'!$A$3:$A$400, 0), MATCH({c}$2, 'Full month Pivot'!$D$2:$K$2, 0)), \"\")")
        # Full Nov..Dec
        share_row.extend(["", ""])
        # Col AA: Oct % - Sep %
        share_row.append(f'=IFERROR(X{r_share}-W{r_share}, "")')
        rows.append(share_row)

        # 6..10. Channels: Organic, Paid, Direct, Referral, Others
        channels = ["  Organic", "  Paid", "  Direct", "  Referral", "  Others"]
        mtd_filter = get_channel_filter(p_name, "MTD Pivot")
        full_filter = get_channel_filter(p_name, "Full month Pivot")
        if "{r_proj}" in mtd_filter:
            mtd_filter = mtd_filter.format(r_proj=r_proj)
        if "{r_proj}" in full_filter:
            full_filter = full_filter.format(r_proj=r_proj)

        for ch_idx, ch_name in enumerate(channels):
            r_ch = r_org + ch_idx
            ch_row = [ch_name]
            # MTD Jan..Apr
            ch_row.extend(["", "", "", ""])
            # MTD May..Oct
            for c in MTD_DATA_COLS:
                ch_row.append(f"=SUMPRODUCT({mtd_filter} * (TRIM('MTD Pivot'!$C$3:$C$400)=TRIM($A{r_ch})) * ('MTD Pivot'!$D$2:$K$2={c}$2) * 'MTD Pivot'!$D$3:$K$400)")
            # MTD Nov..Dec
            ch_row.extend(["", ""])
            # Col N: MTD vs. cùng kỳ
            ch_row.append(f'=IFERROR((K{r_ch}-J{r_ch})/J{r_ch}, "")')
            # Full Jan..Apr
            ch_row.extend(["", "", "", ""])
            # Full May..Oct
            for c in FULL_DATA_COLS:
                ch_row.append(f"=SUMPRODUCT({full_filter} * (TRIM('Full month Pivot'!$C$3:$C$400)=TRIM($A{r_ch})) * ('Full month Pivot'!$D$2:$K$2={c}$2) * 'Full month Pivot'!$D$3:$K$400)")
            # Full Nov..Dec
            ch_row.extend(["", ""])
            # Col AA: Full vs. cùng kỳ
            ch_row.append(f'=IFERROR((X{r_ch}-W{r_ch})/W{r_ch}, "")')
            rows.append(ch_row)

        # 11. Blank Row
        blank_row = [""] * 27
        rows.append(blank_row)

        current_row += 11

    return rows, block_info

def run():
    print("[1/5] Khởi tạo dữ liệu và cấu trúc bảng theo Mockup...")
    table_rows, block_info = build_sheet_data()
    total_rows = len(table_rows)
    print(f"  ✓ Đã sinh {total_rows} dòng cho {len(block_info)} dự án/Hub.")

    sheets_token = get_sheets_token()

    # [2/5] Cấu hình Grid (tăng columns lên 30, hàng lên 600, frozen 2 rows, 1 col, show gridlines) & UNMERGE CŨ
    print("[2/5] Thiết lập kích thước bảng tính, dọn merges cũ và mở lại toàn bộ hàng/cột...")
    # Fetch existing merges & conditional format rules
    meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}?includeGridData=false"
    req_meta = urllib.request.Request(meta_url, headers={"Authorization": f"Bearer {sheets_token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta_data = json.loads(resp.read().decode())

    existing_merges = []
    num_cfs = 0
    for s in meta_data["sheets"]:
        if s["properties"]["sheetId"] == SHEET_ID:
            existing_merges = s.get("merges", [])
            num_cfs = len(s.get("conditionalFormats", []))
            break

    setup_reqs = [
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": SHEET_ID,
                    "gridProperties": {
                        "rowCount": max(total_rows + 50, 600),
                        "columnCount": 30,
                        "frozenRowCount": 2,
                        "frozenColumnCount": 1,
                        "hideGridlines": False
                    }
                },
                "fields": "gridProperties(rowCount,columnCount,frozenRowCount,frozenColumnCount,hideGridlines)"
            }
        },
        {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 600
                },
                "properties": {
                    "hiddenByUser": False
                },
                "fields": "hiddenByUser"
            }
        }
    ]

    # Unmerge các ô cũ TRƯỚC KHI ghi dữ liệu để không bị nuốt giá trị ô subordinate
    for m in existing_merges:
        setup_reqs.append({"unmergeCells": {"range": m}})

    # Xóa conditional formats cũ
    for c_idx in range(num_cfs - 1, -1, -1):
        setup_reqs.append({"deleteConditionalFormatRule": {"sheetId": SHEET_ID, "index": c_idx}})

    url_setup = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    req_setup = urllib.request.Request(
        url_setup,
        data=json.dumps({"requests": setup_reqs}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_setup) as resp:
        pass
    print("  ✓ Đã cấu hình gridProperties và unmerge sạch sẽ.")

    # Dọn sạch ô cũ
    clear_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(SHEET_TITLE + '!A1:AD600')}:clear"
    req_clear = urllib.request.Request(
        clear_url,
        data=b"{}",
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_clear) as resp:
        pass
    print("  ✓ Đã dọn sạch ô dữ liệu cũ.")

    # [3/5] Ghi toàn bộ dữ liệu và công thức vào sheet
    print(f"[3/5] Đang ghi {total_rows} dòng vào Google Sheets...")
    put_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(SHEET_TITLE + '!A1:AA' + str(total_rows))}?valueInputOption=USER_ENTERED"
    req_put = urllib.request.Request(
        put_url,
        data=json.dumps({"range": f"{SHEET_TITLE}!A1:AA{total_rows}", "majorDimension": "ROWS", "values": table_rows}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req_put) as resp:
        res_put = json.loads(resp.read().decode())
    print(f"  ✓ Ghi thành công {res_put.get('updatedCells', 0)} ô dữ liệu.")

    # [4/5] Áp dụng Formatting chuẩn chỉnh (Màu sắc, Font, Merges, Number Format)
    print("[4/5] Thiết lập styling, màu nền, font chữ và căn lề...")
    requests = []

    # Row 1 Merges:
    requests.append({
        "mergeCells": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 1, "endColumnIndex": 13},
            "mergeType": "MERGE_ALL"
        }
    })
    requests.append({
        "mergeCells": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 14, "endColumnIndex": 26},
            "mergeType": "MERGE_ALL"
        }
    })

    # Styling Row 1: Dark Navy #0F3D59
    navy_bg = {"red": 15/255, "green": 61/255, "blue": 89/255}
    white_text = {"foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}, "fontFamily": "Arial", "fontSize": 11, "bold": True}
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 27},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": navy_bg,
                    "textFormat": white_text,
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # A1 left-aligned
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 1},
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "LEFT"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    })

    # Styling Row 2: Soft ice blue #D2E3FC
    ice_blue_bg = {"red": 210/255, "green": 227/255, "blue": 252/255}
    navy_text = {"foregroundColor": {"red": 15/255, "green": 61/255, "blue": 89/255}, "fontFamily": "Arial", "fontSize": 10, "bold": True}
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 27},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": ice_blue_bg,
                    "textFormat": navy_text,
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "numberFormat": {"type": "DATE", "pattern": "mmm yy"}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
        }
    })

    # Column Widths
    requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 230},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 13},
            "properties": {"pixelSize": 85},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 13, "endIndex": 14},
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 14, "endIndex": 26},
            "properties": {"pixelSize": 85},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 26, "endIndex": 27},
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    })

    # Styling for each project block
    blue_header_text = {"foregroundColor": {"red": 17/255, "green": 85/255, "blue": 204/255}, "fontFamily": "Arial", "fontSize": 11, "bold": True}
    bold_text = {"fontFamily": "Arial", "fontSize": 10, "bold": True}
    italic_text = {"fontFamily": "Arial", "fontSize": 10, "italic": True}
    normal_text = {"fontFamily": "Arial", "fontSize": 10, "bold": False}

    for b in block_info:
        r_p_0 = b["r_proj"] - 1
        r_pv_0 = b["r_pv"] - 1
        r_net_0 = b["r_net"] - 1
        r_gr_0 = b["r_growth"] - 1
        r_sh_0 = b["r_share"] - 1
        r_org_0 = b["r_org"] - 1
        r_oth_0 = b["r_oth"] - 1

        # 1. Project Header Row: Light blue bar across A..AA
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_p_0, "endRowIndex": r_p_0 + 1, "startColumnIndex": 0, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": ice_blue_bg,
                        "textFormat": blue_header_text,
                        "horizontalAlignment": "LEFT",
                        "verticalAlignment": "MIDDLE"
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
            }
        })

        # 2. Page views Row: Bold
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_pv_0 + 1, "startColumnIndex": 0, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": bold_text,
                        "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}
                    }
                },
                "fields": "userEnteredFormat(textFormat,numberFormat)"
            }
        })

        # 3. Net change Row: Italic
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_net_0, "endRowIndex": r_net_0 + 1, "startColumnIndex": 0, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": italic_text,
                        "numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}
                    }
                },
                "fields": "userEnteredFormat(textFormat,numberFormat)"
            }
        })

        # 4. % Growth rate Row: Italic + percentage
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_gr_0, "endRowIndex": r_gr_0 + 1, "startColumnIndex": 0, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": italic_text,
                        "numberFormat": {"type": "PERCENT", "pattern": "▲ 0.0%;▼ 0.0%;-"}
                    }
                },
                "fields": "userEnteredFormat(textFormat,numberFormat)"
            }
        })

        # 5. Tỷ trọng trong tổng traffic Row: Normal + 0.0%
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_sh_0, "endRowIndex": r_sh_0 + 1, "startColumnIndex": 0, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": normal_text,
                        "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                    }
                },
                "fields": "userEnteredFormat(textFormat,numberFormat)"
            }
        })

        # 6..10. Channels Rows: Normal + #,##0
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_org_0, "endRowIndex": r_oth_0 + 1, "startColumnIndex": 0, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": normal_text,
                        "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}
                    }
                },
                "fields": "userEnteredFormat(textFormat,numberFormat)"
            }
        })

        # Col N & Col AA number format across all rows of block: ▲ 0.0% / ▼ 0.0%
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_oth_0 + 1, "startColumnIndex": 13, "endColumnIndex": 14},
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "PERCENT", "pattern": "▲ 0.0%;▼ 0.0%;-"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_oth_0 + 1, "startColumnIndex": 26, "endColumnIndex": 27},
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "PERCENT", "pattern": "▲ 0.0%;▼ 0.0%;-"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    # [5/5] Cấu hình Conditional Formatting (Green cho số dương, Red cho số âm)
    green_text_fmt = {
        "textFormat": {
            "foregroundColor": {"red": 19/255, "green": 115/255, "blue": 51/255}, # #137333
            "bold": True
        }
    }
    red_text_fmt = {
        "textFormat": {
            "foregroundColor": {"red": 197/255, "green": 34/255, "blue": 31/255}, # #C5221F
            "bold": True
        }
    }

    # Rule > 0 (Green) cho Col N & Col AA
    requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 13, "endColumnIndex": 14},
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 26, "endColumnIndex": 27}
                ],
                "booleanRule": {
                    "condition": {"type": "NUMBER_GREATER", "values": [{"userEnteredValue": "0"}]},
                    "format": green_text_fmt
                }
            },
            "index": 0
        }
    })
    # Rule < 0 (Red) cho Col N & Col AA
    requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 13, "endColumnIndex": 14},
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 26, "endColumnIndex": 27}
                ],
                "booleanRule": {
                    "condition": {"type": "NUMBER_LESS", "values": [{"userEnteredValue": "0"}]},
                    "format": red_text_fmt
                }
            },
            "index": 1
        }
    })

    # Net change & Growth rate rows formatting
    net_growth_ranges = []
    for b in block_info:
        r_net_0 = b["r_net"] - 1
        r_gr_0 = b["r_growth"] - 1
        net_growth_ranges.append({"sheetId": SHEET_ID, "startRowIndex": r_net_0, "endRowIndex": r_gr_0 + 1, "startColumnIndex": 1, "endColumnIndex": 27})

    requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": net_growth_ranges,
                "booleanRule": {
                    "condition": {"type": "NUMBER_GREATER", "values": [{"userEnteredValue": "0"}]},
                    "format": green_text_fmt
                }
            },
            "index": 2
        }
    })
    requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": net_growth_ranges,
                "booleanRule": {
                    "condition": {"type": "NUMBER_LESS", "values": [{"userEnteredValue": "0"}]},
                    "format": red_text_fmt
                }
            },
            "index": 3
        }
    })

    # Gửi batchUpdate
    url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    req_batch = urllib.request.Request(
        url_batch,
        data=json.dumps({"requests": requests}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_batch) as resp:
        res_batch = json.loads(resp.read().decode())
    print(f"  ✓ Hoàn tất cấu hình styling và formatting ({len(res_batch.get('replies', []))} thao tác)")

    print("\n[SUCCESS] Đã hoàn thành cấu trúc sheet Detail by Project theo đúng mockup thành công 100%!")

if __name__ == "__main__":
    run()

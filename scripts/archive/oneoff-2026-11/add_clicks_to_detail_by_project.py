#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ADD CLICK CTA ROW UNDER PAGE VIEWS FOR EACH PROJECT IN DETAIL BY PROJECT
Bổ sung dòng 'Click CTA' (màu xám #F1F3F4, chữ nghiêng, căn phải) ngay bên dưới dòng 'Page views'
cho tất cả 36 dự án trong sheet 'Projects Detail Flow' trên Google Sheets SSOT.
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID
from scripts.sync_ga4_to_hubs import get_access_token, run_ga4_report
import scripts.lib.url_project_resolver as upr

SHEET_TITLE = "Projects Detail Flow"
SHEET_ID = 316527624

# Date serial numbers for 2026 (Jan..Dec)
MONTH_SERIALS = [46023, 46054, 46082, 46113, 46143, 46174, 46204, 46235, 46266, 46296, 46327, 46357]
MONTH_NAMES = ["Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "Oct 26", "Nov 26", "Dec 26"]

MTD_DATA_COLS = ["F", "G", "H", "I", "J", "K"] # May..Oct (cols 5..10)
FULL_DATA_COLS = ["R", "S", "T", "U", "V", "W"] # May..Oct (cols 17..22)

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

def fetch_ga4_clicks(ga4_token):
    """Kéo số click onelink theo landing page từ GA4 cho các tháng MTD và Full Month."""
    print("  [GA4] Đang quét quy tắc URL mapping...")
    rules = upr.load_rules()
    inferred = upr.load_inferred_rules(rules)

    mtd_ranges = {
        "May": ("2026-05-01", "2026-05-28"),
        "Jun": ("2026-06-01", "2026-06-28"),
        "Jul": ("2026-07-01", "2026-07-28"),
        "Aug": ("2026-08-01", "2026-08-28"),
        "Sep": ("2026-09-01", "2026-09-28"),
        "Oct": ("2026-10-01", "2026-10-28")
    }

    full_ranges = {
        "May": ("2026-05-01", "2026-05-31"),
        "Jun": ("2026-06-01", "2026-06-30"),
        "Jul": ("2026-07-01", "2026-07-31"),
        "Aug": ("2026-08-01", "2026-08-31"),
        "Sep": ("2026-09-01", "2026-09-30"),
        "Oct": ("2026-10-01", "2026-10-28") # Oct Full tạm tính bằng Oct MTD
    }

    def query_range(s_date, e_date):
        res = run_ga4_report(ga4_token, {
            "dateRanges": [{"startDate": s_date, "endDate": e_date}],
            "dimensions": [{"name": "landingPage"}],
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
        raw = defaultdict(int)
        for r in res.get("rows", []):
            lp = r["dimensionValues"][0]["value"]
            cnt = int(r["metricValues"][0]["value"])
            p = upr.resolve_primary("https://www.momo.vn" + lp, rules, inferred)
            raw[p] += cnt
        return raw

    def map_to_36(raw_dict):
        res = defaultdict(int)
        for p, val in raw_dict.items():
            pl = p.lower()
            if "cinema" in pl:
                res["Cinema Hub"] += val
            elif pl in ["vay nhanh", "điểm tín dụng", "ví trả sau", "túi thần tài", "mở thẻ tín dụng", "quản lý chi tiêu", "trả góp apple", "thanh toán khoản vay", "chứng khoán", "tiết kiệm online", "thanh toán thẻ tín dụng", "chứng chỉ quỹ", "trung tâm tài chính", "sàn đầu tư", "financial hub"]:
                res["Financial Hub"] += val
            elif pl in ["phạt nguội", "bảo hiểm ô tô", "bảo hiểm xe máy", "tiện ích giao thông", "phí không dừng", "vehicle hub"]:
                res["Vehicle Hub"] += val
            elif pl in ["bảo hiểm y tế", "bảo hiểm sức khỏe", "bảo hiểm xã hội", "bảo hiểm", "insurance hub"]:
                res["Insurance Hub"] += val
            elif pl in ["student hub", "student pass"]:
                res["Student Hub"] += val
            elif pl in ["sim", "esim"]:
                res["Sim"] += val
            elif pl in ["game", "game hub"]:
                res["Game"] += val
            elif p in PROJECTS:
                res[p] += val
            else:
                matched = False
                for proj in PROJECTS:
                    if proj.lower() == pl:
                        res[proj] += val
                        matched = True
                        break
                if not matched:
                    res["Others"] += val
        return res

    mtd_mapped = {}
    print("  [GA4] Truy vấn số Click MTD 6 tháng (May..Oct)...")
    for m, (s, e) in mtd_ranges.items():
        raw = query_range(s, e)
        mtd_mapped[m] = map_to_36(raw)
        print(f"    - {m} MTD: {sum(mtd_mapped[m].values()):,} clicks")

    full_mapped = {}
    print("  [GA4] Truy vấn số Click Full Month 6 tháng (May..Oct)...")
    for m, (s, e) in full_ranges.items():
        raw = query_range(s, e)
        full_mapped[m] = map_to_36(raw)
        print(f"    - {m} Full: {sum(full_mapped[m].values()):,} clicks")

    return mtd_mapped, full_mapped

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

def build_sheet_data(mtd_clicks, full_clicks):
    """
    Tạo dữ liệu và công thức cho sheet 'Projects Detail Flow' với dòng Click CTA:
    Mỗi dự án gồm 12 hàng:
    1: Project Name (Header bar)
    2: Page views
    3:   Click CTA
    4:   Net change
    5:   % Growth rate
    6: Tỷ trọng trong tổng traffic
    7:   Organic
    8:   Paid
    9:   Direct
    10:  Referral
    11:  Others
    12: Blank row
    """
    grid = []

    # ROW 1: Tiêu đề nhóm
    r1 = ["Web Performance - Detail by Project - Update MTD"]
    r1.extend(["MTD (Month to date)"] + [""] * 11) # B..M
    r1.append("Vs. SPLM")                         # N
    r1.extend(["Full month"] + [""] * 11)          # O..Z
    r1.append("Vs. SPLM")                         # AA
    grid.append(r1)

    # ROW 2: Header cột
    r2 = ["Chỉ số"]
    r2.extend(MONTH_SERIALS)                       # B..M (MTD Jan..Dec)
    r2.append("MTD vs. cùng kỳ")                   # N
    r2.extend(MONTH_SERIALS)                       # O..Z (Full Jan..Dec)
    r2.append("Full vs. cùng kỳ")                  # AA
    grid.append(r2)

    current_row = 3 # 1-based index

    project_blocks_meta = [] # lưu lại thông tin styling từng row

    for p_name in PROJECTS:
        r_proj = current_row
        r_pv = current_row + 1
        r_click = current_row + 2
        r_net = current_row + 3
        r_growth = current_row + 4
        r_share = current_row + 5
        r_org = current_row + 6
        r_paid = current_row + 7
        r_dir = current_row + 8
        r_ref = current_row + 9
        r_oth = current_row + 10
        r_blank = current_row + 11

        project_blocks_meta.append({
            "name": p_name,
            "r_proj": r_proj,
            "r_pv": r_pv,
            "r_click": r_click,
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

        # HÀNG 1: Project Header
        row_proj = [p_name] + [""] * 26
        grid.append(row_proj)

        # HÀNG 2: Page views (SUM các kênh con r_org:r_oth, ẩn nếu = 0)
        row_pv = ["Page views"]
        # MTD B..M (indices 1..12)
        for col_idx in range(12):
            col_letter = chr(ord('B') + col_idx)
            row_pv.append(f'=IF(SUM({col_letter}{r_org}:{col_letter}{r_oth})>0, SUM({col_letter}{r_org}:{col_letter}{r_oth}), "")')
        # Col N: Vs. SPLM MTD (Oct vs Sep) -> K vs J
        row_pv.append(f'=IFERROR((K{r_pv}-J{r_pv})/J{r_pv}, "")')
        # Full Month O..Z (indices 14..25)
        for col_idx in range(12):
            col_letter = chr(ord('O') + col_idx)
            row_pv.append(f'=IF(SUM({col_letter}{r_org}:{col_letter}{r_oth})>0, SUM({col_letter}{r_org}:{col_letter}{r_oth}), "")')
        # Col AA: Vs. SPLM Full Month (Oct vs Sep) -> X vs W
        row_pv.append(f'=IFERROR((X{r_pv}-W{r_pv})/W{r_pv}, "")')
        grid.append(row_pv)

        # HÀNG 3: Click CTA (Mới thêm, ẩn nếu = 0)
        row_click = ["  Click CTA"]
        # MTD B..E: "" (Jan..Apr)
        row_click.extend(["", "", "", ""])
        # MTD F..K: May..Oct clicks
        m_keys = ["May", "Jun", "Jul", "Aug", "Sep", "Oct"]
        for m in m_keys:
            c_val = mtd_clicks.get(m, {}).get(p_name, 0)
            row_click.append(c_val if c_val > 0 else "")
        # MTD L..M: Nov..Dec
        row_click.extend(["", ""])
        # Col N: Vs. SPLM MTD (Oct vs Sep -> K vs J)
        row_click.append(f'=IFERROR((K{r_click}-J{r_click})/J{r_click}, "")')
        # Full Month O..R: "" (Jan..Apr)
        row_click.extend(["", "", "", ""])
        # Full Month S..X: May..Oct clicks
        for m in m_keys:
            c_val = full_clicks.get(m, {}).get(p_name, 0)
            row_click.append(c_val if c_val > 0 else "")
        # Full Month Y..Z: Nov..Dec
        row_click.extend(["", ""])
        # Col AA: Vs. SPLM Full Month (Oct vs Sep -> X vs W)
        row_click.append(f'=IFERROR((X{r_click}-W{r_click})/W{r_click}, "")')
        grid.append(row_click)

        # HÀNG 4: Net change (Chỉ tính khi cả 2 tháng > 0)
        row_net = ["  Net change"]
        # MTD B (Jan): ""
        row_net.append("")
        for col_idx in range(1, 12):
            col_curr = chr(ord('B') + col_idx)
            col_prev = chr(ord('B') + col_idx - 1)
            row_net.append(f'=IF(AND(ISNUMBER({col_curr}{r_pv}), ISNUMBER({col_prev}{r_pv}), {col_prev}{r_pv}>0, {col_curr}{r_pv}>0), {col_curr}{r_pv}-{col_prev}{r_pv}, "")')
        # Col N: ""
        row_net.append("")
        # Full Month O (Jan): ""
        row_net.append("")
        for col_idx in range(1, 12):
            col_curr = chr(ord('O') + col_idx)
            col_prev = chr(ord('O') + col_idx - 1)
            row_net.append(f'=IF(AND(ISNUMBER({col_curr}{r_pv}), ISNUMBER({col_prev}{r_pv}), {col_prev}{r_pv}>0, {col_curr}{r_pv}>0), {col_curr}{r_pv}-{col_prev}{r_pv}, "")')
        # Col AA: ""
        row_net.append("")
        grid.append(row_net)

        # HÀNG 5: % Growth rate (Chỉ tính khi cả 2 tháng > 0)
        row_growth = ["  % Growth rate"]
        # MTD B (Jan): ""
        row_growth.append("")
        for col_idx in range(1, 12):
            col_curr = chr(ord('B') + col_idx)
            col_prev = chr(ord('B') + col_idx - 1)
            row_growth.append(f'=IF(AND(ISNUMBER({col_curr}{r_pv}), ISNUMBER({col_prev}{r_pv}), {col_prev}{r_pv}>0, {col_curr}{r_pv}>0), ({col_curr}{r_pv}-{col_prev}{r_pv})/{col_prev}{r_pv}, "")')
        # Col N: ""
        row_growth.append("")
        # Full Month O (Jan): ""
        row_growth.append("")
        for col_idx in range(1, 12):
            col_curr = chr(ord('O') + col_idx)
            col_prev = chr(ord('O') + col_idx - 1)
            row_growth.append(f'=IF(AND(ISNUMBER({col_curr}{r_pv}), ISNUMBER({col_prev}{r_pv}), {col_prev}{r_pv}>0, {col_curr}{r_pv}>0), ({col_curr}{r_pv}-{col_prev}{r_pv})/{col_prev}{r_pv}, "")')
        # Col AA: ""
        row_growth.append("")
        grid.append(row_growth)

        # HÀNG 6: Tỷ trọng trong tổng traffic (Chỉ tính khi PV > 0)
        row_share = ["Tỷ trọng trong tổng traffic"]
        # MTD B..M
        for col_idx in range(12):
            col_letter = chr(ord('B') + col_idx)
            row_share.append(f'=IF(AND(ISNUMBER({col_letter}{r_pv}), {col_letter}{r_pv}>0), {col_letter}{r_pv}/INDEX(\'MTD Pivot\'!$D$3:$K$400, MATCH("Grand Total", \'MTD Pivot\'!$A$3:$A$400, 0), MATCH({col_letter}$2, \'MTD Pivot\'!$D$2:$K$2, 0)), "")')
        # Col N: Vs. SPLM (Oct share - Sep share) -> K - J
        row_share.append(f'=IF(AND(ISNUMBER(K{r_share}), ISNUMBER(J{r_share})), K{r_share}-J{r_share}, "")')
        # Full Month O..Z
        for col_idx in range(12):
            col_letter = chr(ord('O') + col_idx)
            row_share.append(f'=IF(AND(ISNUMBER({col_letter}{r_pv}), {col_letter}{r_pv}>0), {col_letter}{r_pv}/INDEX(\'Full month Pivot\'!$D$3:$K$400, MATCH("Grand Total", \'Full month Pivot\'!$A$3:$A$400, 0), MATCH({col_letter}$2, \'Full month Pivot\'!$D$2:$K$2, 0)), "")')
        # Col AA: Vs. SPLM Full (Oct share - Sep share) -> X - W
        row_share.append(f'=IF(AND(ISNUMBER(X{r_share}), ISNUMBER(W{r_share})), X{r_share}-W{r_share}, "")')
        grid.append(row_share)

        # HÀNG 7..11: Channels Organic, Paid, Direct, Referral, Others (ẩn nếu = 0)
        channels = [
            ("  Organic", r_org),
            ("  Paid", r_paid),
            ("  Direct", r_dir),
            ("  Referral", r_ref),
            ("  Others", r_oth),
        ]

        f_mtd = get_channel_filter(p_name, "MTD Pivot").format(r_proj=r_proj)
        f_full = get_channel_filter(p_name, "Full month Pivot").format(r_proj=r_proj)

        for ch_name, r_ch in channels:
            row_ch = [ch_name]
            # MTD B..M
            for col_idx in range(12):
                col_letter = chr(ord('B') + col_idx)
                f_expr = f"=SUMPRODUCT({f_mtd} * (TRIM('MTD Pivot'!$C$3:$C$400)=TRIM($A{r_ch})) * ('MTD Pivot'!$D$2:$K$2={col_letter}$2) * 'MTD Pivot'!$D$3:$K$400)"
                row_ch.append(f'=IF({f_expr[1:]}>0, {f_expr[1:]}, "")')
            # Col N: Vs. SPLM MTD -> K vs J
            row_ch.append(f'=IF(AND(ISNUMBER(K{r_ch}), ISNUMBER(J{r_ch}), J{r_ch}>0), (K{r_ch}-J{r_ch})/J{r_ch}, "")')
            # Full Month O..Z
            for col_idx in range(12):
                col_letter = chr(ord('O') + col_idx)
                f_expr = f"=SUMPRODUCT({f_full} * (TRIM('Full month Pivot'!$C$3:$C$400)=TRIM($A{r_ch})) * ('Full month Pivot'!$D$2:$K$2={col_letter}$2) * 'Full month Pivot'!$D$3:$K$400)"
                row_ch.append(f'=IF({f_expr[1:]}>0, {f_expr[1:]}, "")')
            # Col AA: Vs. SPLM Full -> X vs W
            row_ch.append(f'=IF(AND(ISNUMBER(X{r_ch}), ISNUMBER(W{r_ch}), W{r_ch}>0), (X{r_ch}-W{r_ch})/W{r_ch}, "")')
            grid.append(row_ch)

        # HÀNG 12: Dòng trắng phân cách
        row_blank = [""] * 27
        grid.append(row_blank)

        current_row += 12

    return grid, project_blocks_meta

def apply_formatting(token, project_blocks_meta):
    """Áp dụng toàn bộ style, màu sắc, borders, alignment và conditional formatting."""
    print("  [STYLE] Tạo payload batchUpdate định dạng...")

    requests = []

    # 0. Đảm bảo hiển thị Gridlines và Freeze 2 hàng đầu, 1 cột đầu
    requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": SHEET_ID,
                "gridProperties": {
                    "frozenRowCount": 2,
                    "frozenColumnCount": 1,
                    "hideGridlines": False
                }
            },
            "fields": "gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)"
        }
    })

    # 0b. RESET TOÀN BỘ ĐỊNH DẠNG TỪ HÀNG 3 ĐẾN 600 VỀ TRẮNG SẠCH
    # Đảm bảo không còn màu nền xanh, chữ xanh, bold hay italic cũ bị sót lại trên các kênh con
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 600,
                "startColumnIndex": 0,
                "endColumnIndex": 27
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 1, "green": 1, "blue": 1},
                    "textFormat": {
                        "foregroundColor": {"red": 0, "green": 0, "blue": 0},
                        "bold": False,
                        "italic": False,
                        "fontSize": 9
                    },
                    "horizontalAlignment": "RIGHT",
                    "verticalAlignment": "MIDDLE",
                    "numberFormat": {
                        "type": "NUMBER",
                        "pattern": "#,##0"
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
        }
    })

    # Đếm số lượng conditional formatting rules hiện tại để xóa sạch
    url_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}?fields=sheets(properties,conditionalFormats)"
    req_meta = urllib.request.Request(url_meta, headers={"Authorization": f"Bearer {token}"})
    cf_count = 0
    try:
        with urllib.request.urlopen(req_meta) as resp:
            s_data = json.loads(resp.read().decode())
            for s in s_data.get("sheets", []):
                if s["properties"]["sheetId"] == SHEET_ID:
                    cf_count = len(s.get("conditionalFormats", []))
    except Exception:
        cf_count = 0

    for _ in range(cf_count):
        requests.append({
            "deleteConditionalFormatRule": {
                "sheetId": SHEET_ID,
                "index": 0
            }
        })

    # 1. Row 1: Dark Navy #0F3D59, White Bold, Centered
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 27
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 15/255, "green": 61/255, "blue": 89/255},
                    "textFormat": {
                        "foregroundColor": {"red": 1, "green": 1, "blue": 1},
                        "bold": True,
                        "fontSize": 10
                    },
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })

    # Row 1 Col A: Left align
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 1
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "LEFT"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    })

    # 2. Row 2: Ice Blue #D2E3FC, Dark Navy bold text, Centered
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 27
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 210/255, "green": 227/255, "blue": 252/255},
                    "textFormat": {
                        "foregroundColor": {"red": 15/255, "green": 61/255, "blue": 89/255},
                        "bold": True,
                        "fontSize": 9
                    },
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "numberFormat": {
                        "type": "DATE",
                        "pattern": "mmm yy"
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
        }
    })

    # Row 2 Col A, Col N, Col AA: Plain text format
    for c_idx in [0, 13, 26]:
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 1,
                    "endRowIndex": 2,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "TEXT"
                        },
                        "horizontalAlignment": "LEFT" if c_idx == 0 else "CENTER"
                    }
                },
                "fields": "userEnteredFormat(numberFormat,horizontalAlignment)"
            }
        })

    # 3. Định dạng cho từng khối dự án
    for meta in project_blocks_meta:
        r_p = meta["r_proj"] - 1 # 0-indexed
        r_pv = meta["r_pv"] - 1
        r_c = meta["r_click"] - 1
        r_net = meta["r_net"] - 1
        r_g = meta["r_growth"] - 1
        r_sh = meta["r_share"] - 1
        r_ch_start = meta["r_org"] - 1
        r_ch_end = meta["r_oth"] # exclusive

        # a) Project Header Row (Ice Blue background #D2E3FC, Bold Blue #1155cc)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_p,
                    "endRowIndex": r_p + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 27
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 210/255, "green": 227/255, "blue": 252/255},
                        "textFormat": {
                            "foregroundColor": {"red": 17/255, "green": 85/255, "blue": 204/255},
                            "bold": True,
                            "fontSize": 10
                        },
                        "horizontalAlignment": "LEFT",
                        "verticalAlignment": "MIDDLE"
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
            }
        })

        # b) Page views Row (Bold, numbers #,##0, Col N/AA growth rate)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv,
                    "endRowIndex": r_pv + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 27
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {
                            "bold": True,
                            "fontSize": 9
                        },
                        "verticalAlignment": "MIDDLE"
                    }
                },
                "fields": "userEnteredFormat(textFormat,verticalAlignment)"
            }
        })
        # Page views Col A: Left align
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv,
                    "endRowIndex": r_pv + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "LEFT"
                    }
                },
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })

        # Net change & % Growth rate Col A: Left align, Italic
        for r_item in [r_net, r_g]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "startRowIndex": r_item,
                        "endRowIndex": r_item + 1,
                        "startColumnIndex": 0,
                        "endColumnIndex": 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "LEFT",
                            "textFormat": {
                                "italic": True,
                                "fontSize": 9
                            }
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
                }
            })

        # c) Click CTA Row (Mới: Nền xám nhạt #F1F3F4, chữ nghiêng xám đậm #3C4043, căn phải)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c,
                    "endRowIndex": r_c + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 27
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 241/255, "green": 243/255, "blue": 244/255},
                        "textFormat": {
                            "foregroundColor": {"red": 60/255, "green": 64/255, "blue": 67/255},
                            "italic": True,
                            "fontSize": 9
                        },
                        "horizontalAlignment": "RIGHT",
                        "verticalAlignment": "MIDDLE",
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "#,##0"
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
            }
        })
        # Click CTA Col A: Right align (lệch sang phải)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c,
                    "endRowIndex": r_c + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "RIGHT"
                    }
                },
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })
        # Click CTA Col N & Col AA: Growth rate format "▲ "0.0%;"▼ "0.0%;"-"
        for c_idx in [13, 26]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "startRowIndex": r_c,
                        "endRowIndex": r_c + 1,
                        "startColumnIndex": c_idx,
                        "endColumnIndex": c_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "numberFormat": {
                                "type": "NUMBER",
                                "pattern": '"▲ "0.0%;"▼ "0.0%;"-"'
                            }
                        }
                    },
                    "fields": "userEnteredFormat.numberFormat"
                }
            })

        # d) Net change Row (Italic, format +#,##0;-#,##0;0)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_net,
                    "endRowIndex": r_net + 1,
                    "startColumnIndex": 1,
                    "endColumnIndex": 27
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {
                            "italic": True,
                            "fontSize": 9
                        },
                        "horizontalAlignment": "RIGHT",
                        "verticalAlignment": "MIDDLE",
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "+#,##0;-#,##0;0"
                        }
                    }
                },
                "fields": "userEnteredFormat(textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
            }
        })

        # e) % Growth rate Row (Italic, format "▲ "0.0%;"▼ "0.0%;"-")
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_g,
                    "endRowIndex": r_g + 1,
                    "startColumnIndex": 1,
                    "endColumnIndex": 27
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {
                            "italic": True,
                            "fontSize": 9
                        },
                        "horizontalAlignment": "RIGHT",
                        "verticalAlignment": "MIDDLE",
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": '"▲ "0.0%;"▼ "0.0%;"-"'
                        }
                    }
                },
                "fields": "userEnteredFormat(textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
            }
        })

        # f) Tỷ trọng trong tổng traffic Row (format 0.0%, Col N/AA difference "▲ "0.0%;"▼ "0.0%;"-")
        # Col A cho Tỷ trọng và 5 kênh: Căn lề phải (RIGHT) theo yêu cầu
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_sh,
                    "endRowIndex": r_ch_end,
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "RIGHT"
                    }
                },
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })

        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_sh,
                    "endRowIndex": r_sh + 1,
                    "startColumnIndex": 1,
                    "endColumnIndex": 27
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {
                            "fontSize": 9
                        },
                        "horizontalAlignment": "RIGHT",
                        "verticalAlignment": "MIDDLE",
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "0.0%"
                        }
                    }
                },
                "fields": "userEnteredFormat(textFormat,horizontalAlignment,verticalAlignment,numberFormat)"
            }
        })
        # Col N & Col AA for Tỷ trọng: "▲ "0.0%;"▼ "0.0%;"-"
        for c_idx in [13, 26]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "startRowIndex": r_sh,
                        "endRowIndex": r_sh + 1,
                        "startColumnIndex": c_idx,
                        "endColumnIndex": c_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "numberFormat": {
                                "type": "NUMBER",
                                "pattern": '"▲ "0.0%;"▼ "0.0%;"-"'
                            }
                        }
                    },
                    "fields": "userEnteredFormat.numberFormat"
                }
            })

        # g) Page views & Channels Number format (#,##0)
        # Page views row
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv,
                    "endRowIndex": r_pv + 1,
                    "startColumnIndex": 1,
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
        })
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv,
                    "endRowIndex": r_pv + 1,
                    "startColumnIndex": 14,
                    "endColumnIndex": 26
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
        })
        # Col N & AA for Page views
        for c_idx in [13, 26]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "startRowIndex": r_pv,
                        "endRowIndex": r_pv + 1,
                        "startColumnIndex": c_idx,
                        "endColumnIndex": c_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "numberFormat": {
                                "type": "NUMBER",
                                "pattern": '"▲ "0.0%;"▼ "0.0%;"-"'
                            },
                            "horizontalAlignment": "RIGHT"
                        }
                    },
                    "fields": "userEnteredFormat(numberFormat,horizontalAlignment)"
                }
            })

        # Channels rows (r_ch_start..r_ch_end)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ch_start,
                    "endRowIndex": r_ch_end,
                    "startColumnIndex": 1,
                    "endColumnIndex": 13
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "#,##0"
                        },
                        "horizontalAlignment": "RIGHT",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontSize": 9
                        }
                    }
                },
                "fields": "userEnteredFormat(numberFormat,horizontalAlignment,verticalAlignment,textFormat)"
            }
        })
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ch_start,
                    "endRowIndex": r_ch_end,
                    "startColumnIndex": 14,
                    "endColumnIndex": 26
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "#,##0"
                        },
                        "horizontalAlignment": "RIGHT",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontSize": 9
                        }
                    }
                },
                "fields": "userEnteredFormat(numberFormat,horizontalAlignment,verticalAlignment,textFormat)"
            }
        })
        for c_idx in [13, 26]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "startRowIndex": r_ch_start,
                        "endRowIndex": r_ch_end,
                        "startColumnIndex": c_idx,
                        "endColumnIndex": c_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "numberFormat": {
                                "type": "NUMBER",
                                "pattern": '"▲ "0.0%;"▼ "0.0%;"-"'
                            },
                            "horizontalAlignment": "RIGHT",
                            "verticalAlignment": "MIDDLE",
                            "textFormat": {
                                "fontSize": 9
                            }
                        }
                    },
                    "fields": "userEnteredFormat(numberFormat,horizontalAlignment,verticalAlignment,textFormat)"
                }
            })

    # 4. CONDITIONAL FORMATTING RULES (Positive: Green, Negative: Red)
    # Xanh: #137333 (red: 19/255, green: 115/255, blue: 51/255)
    # Đỏ: #C5221F (red: 197/255, green: 34/255, blue: 31/255)
    # Rule 1: Positive text color for Net change and Growth rates
    requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {
                        "sheetId": SHEET_ID,
                        "startRowIndex": 2,
                        "endRowIndex": 500,
                        "startColumnIndex": 1,
                        "endColumnIndex": 27
                    }
                ],
                "booleanRule": {
                    "condition": {
                        "type": "NUMBER_GREATER",
                        "values": [{"userEnteredValue": "0"}]
                    },
                    "format": {
                        "textFormat": {
                            "foregroundColor": {"red": 19/255, "green": 115/255, "blue": 51/255},
                            "bold": False
                        }
                    }
                }
            },
            "index": 0
        }
    })

    # Rule 2: Negative text color for Net change and Growth rates
    requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {
                        "sheetId": SHEET_ID,
                        "startRowIndex": 2,
                        "endRowIndex": 500,
                        "startColumnIndex": 1,
                        "endColumnIndex": 27
                    }
                ],
                "booleanRule": {
                    "condition": {
                        "type": "NUMBER_LESS",
                        "values": [{"userEnteredValue": "0"}]
                    },
                    "format": {
                        "textFormat": {
                            "foregroundColor": {"red": 197/255, "green": 34/255, "blue": 31/255},
                            "bold": False
                        }
                    }
                }
            },
            "index": 1
        }
    })

    # 5. Column dimensions
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": 0,
                "endIndex": 1
            },
            "properties": {"pixelSize": 230},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": 1,
                "endIndex": 13
            },
            "properties": {"pixelSize": 85},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": 13,
                "endIndex": 14
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": 14,
                "endIndex": 26
            },
            "properties": {"pixelSize": 85},
            "fields": "pixelSize"
        }
    })
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": 26,
                "endIndex": 27
            },
            "properties": {"pixelSize": 100},
            "fields": "pixelSize"
        }
    })

    return requests

def run():
    print("=== [BƯỚC 1/4] Kéo dữ liệu Click CTA từ GA4 API ===")
    ga4_token = get_access_token()
    mtd_clicks, full_clicks = fetch_ga4_clicks(ga4_token)

    print("\n=== [BƯỚC 2/4] Xây dựng ma trận dữ liệu và công thức 36 dự án ===")
    grid, blocks_meta = build_sheet_data(mtd_clicks, full_clicks)
    print(f"  ✓ Tổng số dòng được tạo: {len(grid)} hàng x 27 cột")

    token = get_sheets_token()

    print("\n=== [BƯỚC 3/4] Ghi dữ liệu vào Google Sheet SSOT ===")
    # Xóa sạch dữ liệu cũ từ A1:AA600
    clear_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/Projects%20Detail%20Flow!A1:AA600:clear"
    req_clear = urllib.request.Request(
        clear_url,
        data=b"{}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_clear) as resp:
        print("  ✓ Đã làm sạch vùng dữ liệu A1:AA600")

    # Ghi toàn bộ dữ liệu mới
    write_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/Projects%20Detail%20Flow!A1:AA{len(grid)}?valueInputOption=USER_ENTERED"
    req_write = urllib.request.Request(
        write_url,
        data=json.dumps({"values": grid}).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req_write) as resp:
        res = json.loads(resp.read().decode())
        print(f"  ✓ Đã ghi thành công {res.get('updatedRows')} hàng, {res.get('updatedCells')} ô dữ liệu!")

    print("\n=== [BƯỚC 4/4] Áp dụng Styling, Borders, Number Formats & Conditional Formatting ===")
    # Gửi requests định dạng theo batch (tránh payload quá lớn)
    formatting_requests = apply_formatting(token, blocks_meta)
    print(f"  ✓ Tổng số requests định dạng: {len(formatting_requests)}")

    # Chia batch 100 requests mỗi lần gọi API
    batch_size = 100
    for i in range(0, len(formatting_requests), batch_size):
        chunk = formatting_requests[i:i + batch_size]
        b_url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
        b_req = urllib.request.Request(
            b_url,
            data=json.dumps({"requests": chunk}).encode("utf-8"),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(b_req) as resp:
            pass
        print(f"    - Đã thực thi batch {i//batch_size + 1}/{(len(formatting_requests) - 1)//batch_size + 1}")

    print("\n[SUCCESS] Đã hoàn thành bổ sung dòng Click CTA bên dưới Page views cho toàn bộ 36 dự án thành công 100%!")

    print("\n=== [ĐỒNG BỘ OFFLINE & GOOGLE DRIVE DESKTOP] ===")
    export_url = f"https://docs.google.com/spreadsheets/d/{TARGET_SHEET_ID}/export?format=xlsx"
    export_req = urllib.request.Request(export_url, headers={"Authorization": f"Bearer {token}"})
    target_local = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    gdrive_dir = Path("/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#4 - Tracking & Performance")
    target_gdrive = gdrive_dir / "web_performance_tracking.xlsx"

    try:
        with urllib.request.urlopen(export_req) as resp:
            content = resp.read()
            with open(target_local, "wb") as f:
                f.write(content)
            print(f"  ✓ Đã lưu bản sao offline tại {target_local} ({len(content):,} bytes)")

            if gdrive_dir.exists():
                with open(target_gdrive, "wb") as f:
                    f.write(content)
                print(f"  ✓ Đã đồng bộ sang Google Drive Desktop: {target_gdrive}")
            else:
                print("  ℹ Google Drive Desktop chưa mount thư mục.")
    except Exception as e:
        print(f"  ⚠ Lỗi xuất bản sao Excel: {e}")

if __name__ == "__main__":
    run()

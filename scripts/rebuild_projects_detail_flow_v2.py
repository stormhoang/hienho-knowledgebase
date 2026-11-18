#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REBUILD PROJECTS DETAIL FLOW V2 - CLEAN & MINIMALIST
- Thiết kế tối giản, chuyên nghiệp ("Không màu mè"): Nền trắng sạch, viền xám mảnh #DADCE0, tiêu đề xám nhạt #F8F9FA
- Mỗi Project khi xổ ra gồm:
  1. Total Pageviews của project (Dòng Header dự án, in đậm, =SUM 5 kênh)
  2. Total Clicks của project (Dòng Clicks W2A onelink kéo từ GA4)
  3. Channel Detail: Organic, Paid, Direct, Referral, Others (công thức SUMPRODUCT từ MTD Pivot & Full month Pivot)
- Hỗ trợ Row Grouping (Google Sheets +/-) để thu gọn hoặc bung ra ("xổ ra") linh hoạt
- Thiết lập Conditional Formatting (color condition) cho cột Chênh lệch MTD & % Chênh lệch:
  + Tăng trưởng dương (>0): Nền xanh dịu #E6F4EA, Chữ xanh đậm #137333
  + Tăng trưởng âm (<0): Nền đỏ dịu #FCE8E6, Chữ đỏ đậm #C5221F
- Đồng bộ trực tiếp Google Sheets SSOT và cập nhật file Excel local.
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from collections import defaultdict
import openpyxl

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID
from scripts.sync_ga4_to_hubs import get_access_token, run_ga4_report
import scripts.lib.url_project_resolver as upr

SHEET_TITLE = "Projects Detail Flow"
SHEET_ID = 316527624

# Date serial numbers for 2026 (May..Dec)
MTD_SERIALS = [46143, 46174, 46204, 46235, 46266, 46296, 46327, 46357] # May..Dec
MTD_MONTHS = ["May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "Oct 26", "Nov 26", "Dec 26"]

# 36 Projects chuẩn phủ 100% traffic Web Platform
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
    """Trả về biểu thức lọc dự án trong SUMPRODUCT từ Pivot."""
    if p_name == "Cinema Hub":
        return f"('{pivot_sheet}'!$B$3:$B$400=\"Cinema Hub\")"
    elif p_name == "Financial Hub":
        return (
            f"(('{pivot_sheet}'!$B$3:$B$400=\"Financial Hub\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Vay nhanh\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Quản lý chi tiêu\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Trung tâm tài chính\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Tiệm Vàng Online\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Tỷ Giá\") > 0)"
        )
    elif p_name == "Vehicle Hub":
        return (
            f"(('{pivot_sheet}'!$B$3:$B$400=\"Vehicle Hub\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Phạt nguội\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Phạt Nguội\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Ô Tô\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Xe Máy\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Tiện Ích Giao Thông\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Phí Không Dừng\") > 0)"
        )
    elif p_name == "Insurance Hub":
        return (
            f"(('{pivot_sheet}'!$B$3:$B$400=\"Insurance Hub\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Bảo Hiểm Y Tế\") + "
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
    elif p_name == "Game":
        return (
            f"(('{pivot_sheet}'!$B$3:$B$400=\"Game\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Game\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Game Hub\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Nạp thẻ Game\") > 0)"
        )
    elif p_name == "TnC":
        return f"(('{pivot_sheet}'!$A$3:$A$400=\"TnC\") + ('{pivot_sheet}'!$A$3:$A$400=\"Tnc\") > 0)"
    elif p_name == "Others":
        return (
            f"(('{pivot_sheet}'!$A$3:$A$400=\"Others\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"Donation\") + "
            f"('{pivot_sheet}'!$A$3:$A$400=\"XU\") > 0)"
        )
    else:
        return f"(('{pivot_sheet}'!$B$3:$B$400=\"{p_name}\") + ('{pivot_sheet}'!$A$3:$A$400=\"{p_name}\") > 0)"

def fetch_clicks_from_ga4(ga4_token):
    """Truy vấn chính xác số Onelink clicks từ GA4 API cho 36 dự án qua các tháng."""
    print("  [GA4] Đang quét mapping rules...")
    rules = upr.load_rules()
    inferred = upr.load_inferred_rules(rules)

    months_range = {
        "May": ("2026-05-01", "2026-05-31"),
        "Jun": ("2026-06-01", "2026-06-30"),
        "Jul": ("2026-07-01", "2026-07-31"),
        "Aug": ("2026-08-01", "2026-08-31"),
        "Sep": ("2026-09-01", "2026-09-30"),
        "Oct": ("2026-10-01", "2026-10-31")
    }

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
            elif pl in ["game", "game hub", "nạp thẻ game"]:
                res["Game"] += val
            elif pl in ["tnc", "điều khoản"]:
                res["TnC"] += val
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

    clicks_by_month = {}
    for m, (s, e) in months_range.items():
        print(f"    - Kéo clicks {m} ({s} -> {e})...")
        res = run_ga4_report(ga4_token, {
            "dateRanges": [{"startDate": s, "endDate": e}],
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
        clicks_by_month[m] = map_to_36(raw)
        print(f"      ✓ {m}: {sum(clicks_by_month[m].values()):,} clicks")

    return clicks_by_month

def build_sheet_data(clicks_by_month):
    """
    Xây dựng toàn bộ dữ liệu 23 cột (A..W) cho Projects Detail Flow.
    Mỗi dự án gồm 7 dòng:
    1: Project Name (Total Pageviews = SUM 5 kênh)
    2:   Total Clicks (Clicks onelink từ GA4)
    3:     Organic
    4:     Paid
    5:     Direct
    6:     Referral
    7:     Others
    """
    grid = []

    # ROW 1: Super Header
    r1 = ["Cấu trúc Dự Án & Kênh Web Platform"]
    # B1..I1: MTD May..Dec (8 cols)
    r1.append("LŨY KẾ MTD (Month to Date)")
    r1.extend([""] * 7)
    # J1, K1, L1: MTD MoM Diff & CVR
    r1.append("Chênh lệch MTD")
    r1.append("% Chênh lệch MTD")
    r1.append("W2A CVR")
    # M1: Blank separator
    r1.append("")
    # N1..U1: Full Month May..Dec (8 cols)
    r1.append("TOÀN BỘ TRỌN THÁNG (Full Month)")
    r1.extend([""] * 7)
    # V1, W1: Full MoM Diff & %
    r1.append("Chênh lệch Full Month")
    r1.append("% Chênh lệch Full Month")
    grid.append(r1)

    # ROW 2: Header Ngày/Chỉ số
    r2 = ["Chỉ số / Tên Dự Án"]
    # B..I (MTD May..Dec)
    r2.extend(MTD_SERIALS)
    # J, K, L
    r2.extend(["T11 vs T10", "% MoM", "CVR %"])
    # M
    r2.append("")
    # N..U (Full Month May..Dec)
    r2.extend(MTD_SERIALS)
    # V, W
    r2.extend(["T10 vs T9", "% MoM"])
    grid.append(r2)

    # Khởi tạo danh sách theo dõi vị trí các hàng
    project_meta = []
    current_row = 4 # Row 3 dành cho Tổng Toàn Web (sẽ điền công thức sum sau)

    for p_name in PROJECTS:
        r_proj = current_row
        r_click = current_row + 1
        r_org = current_row + 2
        r_paid = current_row + 3
        r_dir = current_row + 4
        r_ref = current_row + 5
        r_oth = current_row + 6

        project_meta.append({
            "name": p_name,
            "r_proj": r_proj,
            "r_click": r_click,
            "r_org": r_org,
            "r_paid": r_paid,
            "r_dir": r_dir,
            "r_ref": r_ref,
            "r_oth": r_oth
        })

        # --- DÒNG 1: PROJECT TOTAL PAGEVIEWS ---
        row_proj = [p_name]
        # MTD May..Dec (Cols B..I): =SUM(B{r_org}:B{r_oth})
        for c_idx in range(8):
            c_let = chr(ord('B') + c_idx)
            row_proj.append(f'=IF(SUM({c_let}{r_org}:{c_let}{r_oth})>0, SUM({c_let}{r_org}:{c_let}{r_oth}), "")')
        # Col J: Chênh lệch MTD (=G{r_proj}-F{r_proj})
        row_proj.append(f'=IF(AND(ISNUMBER(H{r_proj}), ISNUMBER(G{r_proj})), H{r_proj}-G{r_proj}, "")')
        # Col K: % Chênh lệch MTD
        row_proj.append(f'=IF(AND(ISNUMBER(H{r_proj}), ISNUMBER(G{r_proj}), G{r_proj}>0), (H{r_proj}-G{r_proj})/G{r_proj}, "")')
        # Col L: W2A CVR (=G{r_click}/G{r_proj})
        row_proj.append(f'=IFERROR(G{r_click}/G{r_proj}, "")')
        # Col M: Blank
        row_proj.append("")
        # Full Month May..Dec (Cols N..U): =SUM(N{r_org}:N{r_oth})
        for c_idx in range(8):
            c_let = chr(ord('N') + c_idx)
            row_proj.append(f'=IF(SUM({c_let}{r_org}:{c_let}{r_oth})>0, SUM({c_let}{r_org}:{c_let}{r_oth}), "")')
        # Col V: Chênh lệch Full Month (=S{r_proj}-R{r_proj})
        row_proj.append(f'=IF(AND(ISNUMBER(S{r_proj}), ISNUMBER(R{r_proj}), R{r_proj}>0), S{r_proj}-R{r_proj}, "")')
        # Col W: % Chênh lệch Full Month
        row_proj.append(f'=IFERROR((S{r_proj}-R{r_proj})/R{r_proj}, "")')
        grid.append(row_proj)

        # --- DÒNG 2: TOTAL CLICKS ---
        row_ck = ["  Total Clicks"]
        # MTD B..G (May..Oct): clicks from GA4
        m_keys = ["May", "Jun", "Jul", "Aug", "Sep", "Oct"]
        for m in m_keys:
            c_val = clicks_by_month.get(m, {}).get(p_name, 0)
            row_ck.append(c_val if c_val > 0 else "")
        # MTD H..I (Nov..Dec): ""
        row_ck.extend(["", ""])
        # Col J: Chênh lệch Click MTD (=G{r_click}-F{r_click})
        row_ck.append(f'=IF(AND(ISNUMBER(H{r_click}), ISNUMBER(G{r_click})), H{r_click}-G{r_click}, "")')
        # Col K: % Chênh lệch Click MTD
        row_ck.append(f'=IF(AND(ISNUMBER(H{r_click}), ISNUMBER(G{r_click}), G{r_click}>0), (H{r_click}-G{r_click})/G{r_click}, "")')
        # Col L: Blank
        row_ck.append("")
        # Col M: Blank
        row_ck.append("")
        # Full Month N..S (May..Oct): clicks from GA4
        for m in m_keys:
            c_val = clicks_by_month.get(m, {}).get(p_name, 0)
            row_ck.append(c_val if c_val > 0 else "")
        # Full Month T..U (Nov..Dec): ""
        row_ck.extend(["", ""])
        # Col V: Chênh lệch Click Full Month
        row_ck.append(f'=IF(AND(ISNUMBER(S{r_click}), ISNUMBER(R{r_click}), R{r_click}>0), S{r_click}-R{r_click}, "")')
        # Col W: % Chênh lệch Click Full Month
        row_ck.append(f'=IFERROR((S{r_click}-R{r_click})/R{r_click}, "")')
        grid.append(row_ck)

        # --- DÒNG 3..7: CHANNELS DETAIL ---
        filter_mtd = get_channel_filter(p_name, "MTD Pivot")
        filter_full = get_channel_filter(p_name, "Full month Pivot")
        channels = ["Organic", "Paid", "Direct", "Referral", "Others"]

        for ch_idx, ch_name in enumerate(channels):
            r_ch = r_org + ch_idx
            row_ch = [ch_name]

            # MTD B..I (May..Dec)
            for c_idx in range(8):
                c_let = chr(ord('B') + c_idx)
                row_ch.append(f"=SUMPRODUCT({filter_mtd} * (TRIM('MTD Pivot'!$C$3:$C$400)=\"{ch_name}\") * ('MTD Pivot'!$D$2:$K$2={c_let}$2) * 'MTD Pivot'!$D$3:$K$400)")

            # Col J: Chênh lệch MTD
            row_ch.append(f'=IF(AND(ISNUMBER(H{r_ch}), ISNUMBER(G{r_ch})), H{r_ch}-G{r_ch}, "")')
            # Col K: % Chênh lệch MTD
            row_ch.append(f'=IF(AND(ISNUMBER(H{r_ch}), ISNUMBER(G{r_ch}), G{r_ch}>0), (H{r_ch}-G{r_ch})/G{r_ch}, "")')
            # Col L: Blank
            row_ch.append("")
            # Col M: Blank
            row_ch.append("")

            # Full Month N..U (May..Dec)
            for c_idx in range(8):
                c_let = chr(ord('N') + c_idx)
                row_ch.append(f"=SUMPRODUCT({filter_full} * (TRIM('Full month Pivot'!$C$3:$C$400)=\"{ch_name}\") * ('Full month Pivot'!$D$2:$K$2={c_let}$2) * 'Full month Pivot'!$D$3:$K$400)")

            # Col V: Chênh lệch Full Month
            row_ch.append(f'=IF(AND(ISNUMBER(S{r_ch}), ISNUMBER(R{r_ch}), R{r_ch}>0), S{r_ch}-R{r_ch}, "")')
            # Col W: % Chênh lệch Full Month
            row_ch.append(f'=IFERROR((S{r_ch}-R{r_ch})/R{r_ch}, "")')
            grid.append(row_ch)

        current_row += 7

    # Xây dựng Row 3: Grand Total Toàn Website
    top_pv_rows = [pm["r_proj"] for pm in project_meta]
    top_ck_rows = [pm["r_click"] for pm in project_meta]

    r3 = ["Page views (Actual)"]
    # MTD B..I
    for c_idx in range(8):
        c_let = chr(ord('B') + c_idx)
        sum_args = ", ".join([f"{c_let}{r}" for r in top_pv_rows])
        r3.append(f"=SUM({sum_args})")
    # Col J: Chênh lệch MTD
    r3.append("=G3-F3")
    # Col K: % Chênh lệch MTD
    r3.append("=IFERROR((G3-F3)/F3, \"\")")
    # Col L: Total Web W2A CVR
    sum_ck_oct = ", ".join([f"G{r}" for r in top_ck_rows])
    r3.append(f"=SUM({sum_ck_oct})/G3")
    # Col M
    r3.append("")
    # Full Month N..U
    for c_idx in range(8):
        c_let = chr(ord('N') + c_idx)
        sum_args = ", ".join([f"{c_let}{r}" for r in top_pv_rows])
        r3.append(f"=SUM({sum_args})")
    # Col V
    r3.append("=S3-R3")
    # Col W
    r3.append("=IFERROR((S3-R3)/R3, \"\")")

    # Chèn Row 3 vào vị trí thứ 3 (index 2) trong grid
    grid.insert(2, r3)

    return grid, project_meta

def run():
    print("=" * 70)
    print("TÁI THIẾT SHEET 'Projects Detail Flow' CHUẨN MINIMALIST & CHUYÊN NGHIỆP")
    print("=" * 70)

    # [1/5] Kéo Clicks GA4
    print("[1/5] Kéo dữ liệu Onelink Clicks từ GA4 API cho 36 dự án (May..Oct)...")
    ga4_token = get_access_token()
    clicks_by_month = fetch_clicks_from_ga4(ga4_token)

    # [2/5] Tạo cấu trúc bảng
    print("[2/5] Xây dựng dữ liệu và công thức 36 dự án x 7 dòng...")
    grid, project_meta = build_sheet_data(clicks_by_month)
    total_rows = len(grid)
    print(f"  ✓ Tổng số dòng: {total_rows} dòng (từ Row 1 đến Row {total_rows})")

    sheets_token = get_sheets_token()

    # [3/5] Dọn dẹp sheet cũ và thiết lập Grid Properties
    print("[3/5] Dọn dẹp cấu trúc cũ (xóa merges cũ, xóa groups cũ, bật gridlines)...")
    # Lấy thông tin sheet hiện tại
    url_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}?fields=sheets(properties,rowGroups,merges)"
    req_meta = urllib.request.Request(url_meta, headers={"Authorization": f"Bearer {sheets_token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta_data = json.loads(resp.read().decode())

    target_sheet = None
    for s in meta_data["sheets"]:
        if s["properties"]["sheetId"] == SHEET_ID:
            target_sheet = s
            break

    clean_requests = []

    # Xóa merges cũ
    for m in target_sheet.get("merges", []):
        clean_requests.append({"unmergeCells": {"range": m}})

    # Xóa row groups cũ
    for rg in target_sheet.get("rowGroups", []):
        clean_requests.append({"deleteDimensionGroup": {"range": rg["range"]}})

    # Xóa toàn bộ đường viền/kẻ cũ
    clean_requests.append({
        "updateBorders": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 600,
                "startColumnIndex": 0,
                "endColumnIndex": 30
            },
            "top": {"style": "NONE"},
            "bottom": {"style": "NONE"},
            "left": {"style": "NONE"},
            "right": {"style": "NONE"},
            "innerHorizontal": {"style": "NONE"},
            "innerVertical": {"style": "NONE"}
        }
    })

    # Cập nhật grid properties: show gridlines, 300 rows, 26 cols, frozen 2 rows, 1 col
    clean_requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": SHEET_ID,
                "gridProperties": {
                    "rowCount": 300,
                    "columnCount": 26,
                    "frozenRowCount": 2,
                    "frozenColumnCount": 1,
                    "hideGridlines": False
                }
            },
            "fields": "gridProperties.rowCount,gridProperties.columnCount,gridProperties.frozenRowCount,gridProperties.frozenColumnCount,gridProperties.hideGridlines"
        }
    })

    if clean_requests:
        url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
        req = urllib.request.Request(
            url_batch,
            data=json.dumps({"requests": clean_requests}).encode("utf-8"),
            headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req) as resp:
            pass
        print(f"  ✓ Đã reset layout ({len(clean_requests)} clean actions)")

    # [4/5] Ghi toàn bộ dữ liệu vào Google Sheets
    print("[4/5] Ghi dữ liệu và công thức vào Google Sheets SSOT...")
    range_clear = f"'{SHEET_TITLE}'!A1:Z600"
    url_clear = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(range_clear)}:clear"
    req_clear = urllib.request.Request(url_clear, data=b"{}", headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req_clear) as resp:
        pass

    range_put = f"'{SHEET_TITLE}'!A1:W{total_rows}"
    url_put = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(range_put)}?valueInputOption=USER_ENTERED"
    req_put = urllib.request.Request(
        url_put,
        data=json.dumps({"range": range_put, "majorDimension": "ROWS", "values": grid}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req_put) as resp:
        res_put = json.loads(resp.read().decode())
    print(f"  ✓ Đã ghi thành công {res_put.get('updatedCells', 0)} ô.")

    # [5/5] Định dạng Minimalist ("Không màu mè"), Grouping và Conditional Formatting
    print("[5/5] Áp dụng styling tối giản, tạo Row Groups và thiết lập Color Conditions...")
    styling_requests = []

    # 1. Reset nền trắng toàn bộ bảng
    styling_requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": total_rows,
                "startColumnIndex": 0,
                "endColumnIndex": 23
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 1, "green": 1, "blue": 1},
                    "textFormat": {
                        "fontFamily": "Roboto",
                        "fontSize": 10,
                        "foregroundColor": {"red": 32/255, "green": 33/255, "blue": 36/255}
                    }
                }
            },
            "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat"
        }
    })

    # 2. Header Row 1 & 2: Nền xám nhạt #F8F9FA, Chữ bold #202124
    gray_header = {"red": 248/255, "green": 249/255, "blue": 250/255}
    styling_requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 23
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": gray_header,
                    "textFormat": {"bold": True, "foregroundColor": {"red": 32/255, "green": 33/255, "blue": 36/255}},
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
        }
    })
    styling_requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 1
            },
            "cell": {"userEnteredFormat": {"horizontalAlignment": "LEFT"}},
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    })

    # Header Row 2 Date format (May 26..Dec 26)
    styling_requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": 2,
                "startColumnIndex": 1,
                "endColumnIndex": 9
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "DATE", "pattern": "mmm yy"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    styling_requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": 2,
                "startColumnIndex": 13,
                "endColumnIndex": 21
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "DATE", "pattern": "mmm yy"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    # 3. Merges Header
    styling_requests.append({"mergeCells": {"range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 1, "endColumnIndex": 9}, "mergeType": "MERGE_ALL"}})
    styling_requests.append({"mergeCells": {"range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 13, "endColumnIndex": 21}, "mergeType": "MERGE_ALL"}})

    # 4. Row 3: Grand Total Website (Nền xám rất nhẹ #F1F3F4, bold)
    styling_requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 0,
                "endColumnIndex": 23
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 241/255, "green": 243/255, "blue": 244/255},
                    "textFormat": {"bold": True, "foregroundColor": {"red": 32/255, "green": 33/255, "blue": 36/255}}
                }
            },
            "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat"
        }
    })

    # 5. Định dạng Project Name Rows (Bold, không kẻ viền)
    gray_channel_color = {"red": 95/255, "green": 99/255, "blue": 104/255}
    for pm in project_meta:
        r_p_0 = pm["r_proj"] - 1
        styling_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_p_0,
                    "endRowIndex": r_p_0 + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 23
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"bold": True, "foregroundColor": {"red": 32/255, "green": 33/255, "blue": 36/255}}
                    }
                },
                "fields": "userEnteredFormat.textFormat"
            }
        })

        # Định dạng các dòng kênh: Canh phải, màu xám #5F6368
        styling_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": pm["r_org"] - 1,
                    "endRowIndex": pm["r_oth"],
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "RIGHT",
                        "textFormat": {
                            "foregroundColor": gray_channel_color,
                            "bold": False
                        }
                    }
                },
                "fields": "userEnteredFormat.horizontalAlignment,userEnteredFormat.textFormat.foregroundColor,userEnteredFormat.textFormat.bold"
            }
        })

    # 6. Number Formats toàn sheet:
    # Pageviews & Clicks: #,##0 cho B..I (1..9) và N..U (13..21)
    for col_range in [(1, 9), (13, 21)]:
        styling_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 2,
                    "endRowIndex": total_rows,
                    "startColumnIndex": col_range[0],
                    "endColumnIndex": col_range[1]
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    # Chênh lệch MTD (Col J, index 9) & Chênh lệch Full (Col V, index 21): #,##0;#,##0;0 (không hiển thị + và -)
    for c_idx in [9, 21]:
        styling_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 1,
                    "endRowIndex": total_rows,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0;#,##0;0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    # % Chênh lệch MTD (Col K, index 10), W2A CVR (Col L, index 11), % Chênh lệch Full (Col W, index 22): 0.0%
    for c_idx in [10, 11, 22]:
        styling_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 2,
                    "endRowIndex": total_rows,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    # 7. TẠO ROW GROUPS (XỔ RA / THU VÀO) CHO MỖI DỰ ÁN
    # Group từ dòng Total Clicks (r_click - 1) đến dòng Others (r_oth)
    for pm in project_meta:
        start_0 = pm["r_click"] - 1 # 0-indexed start
        end_0 = pm["r_oth"]         # 0-indexed end (exclusive)
        styling_requests.append({
            "addDimensionGroup": {
                "range": {
                    "sheetId": SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": start_0,
                    "endIndex": end_0
                }
            }
        })

    # 8. THIẾT LẬP CONDITIONAL FORMATTING (COLOR CONDITIONS)
    # Cột J & K (Chênh lệch MTD & % Chênh lệch MTD)
    green_bg = {"red": 230/255, "green": 244/255, "blue": 234/255} # #E6F4EA
    green_fg = {"red": 19/255, "green": 115/255, "blue": 51/255}   # #137333
    red_bg = {"red": 252/255, "green": 232/255, "blue": 230/255}   # #FCE8E6
    red_fg = {"red": 197/255, "green": 34/255, "blue": 31/255}     # #C5221F

    # Rule 1: Chênh lệch MTD > 0 (Green)
    styling_requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 9, "endColumnIndex": 11},
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 21, "endColumnIndex": 23}
                ],
                "booleanRule": {
                    "condition": {"type": "NUMBER_GREATER", "values": [{"userEnteredValue": "0"}]},
                    "format": {
                        "backgroundColor": green_bg,
                        "textFormat": {"foregroundColor": green_fg, "bold": True}
                    }
                }
            },
            "index": 0
        }
    })

    # Rule 2: Chênh lệch MTD < 0 (Red)
    styling_requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 9, "endColumnIndex": 11},
                    {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": total_rows, "startColumnIndex": 21, "endColumnIndex": 23}
                ],
                "booleanRule": {
                    "condition": {"type": "NUMBER_LESS", "values": [{"userEnteredValue": "0"}]},
                    "format": {
                        "backgroundColor": red_bg,
                        "textFormat": {"foregroundColor": red_fg, "bold": True}
                    }
                }
            },
            "index": 1
        }
    })

    # Gửi toàn bộ batchUpdate
    url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    req_batch = urllib.request.Request(
        url_batch,
        data=json.dumps({"requests": styling_requests}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_batch) as resp:
        res_batch = json.loads(resp.read().decode())
    print(f"  ✓ Đã áp dụng hoàn tất styling, {len(project_meta)} Dimension Groups và 2 Color Conditions!")

    # [6/6] Đồng bộ cập nhật vào file Excel local
    print("[6/6] Đồng bộ cập nhật vào Excel SSOT cục bộ...")
    excel_path = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    wb = openpyxl.load_workbook(excel_path)
    if SHEET_TITLE in wb.sheetnames:
        del wb[SHEET_TITLE]
    ws = wb.create_sheet(SHEET_TITLE, index=5)

    for r_idx, row in enumerate(grid, 1):
        for c_idx, val in enumerate(row, 1):
            ws.cell(row=r_idx, column=c_idx, value=val)

    wb.save(excel_path)
    print(f"  ✓ Đã lưu thành công vào {excel_path}")

    print("\n" + "=" * 70)
    print("HOÀN THÀNH TÁI THIẾT PROJECTS DETAIL FLOW XUẤT SẮC!")
    print("=" * 70)

if __name__ == "__main__":
    run()

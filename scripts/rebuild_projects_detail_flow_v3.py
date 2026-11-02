#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REBUILD PROJECTS DETAIL FLOW V3 - FULL DETAILED BREAKDOWN
- Phân rã chi tiết 100% tất cả 65 Use Cases / Sản phẩm của Web Platform:
  + 8 Hubs lớn (Cinema Hub, Financial Hub, Vehicle Hub, Bảo Hiểm, Telco & Data, Student Hub, Utilities & Billpay, Entertainment & Travel)
  + 40 Sub-projects chi tiết (Vay Nhanh, Ví Trả Sau, Túi Thần Tài, Cineplex, Phạt Nguội, BH Ô tô, BH Xe máy...)
  + 25 Dự án / Tiện ích độc lập (Home MoMo, Download, New User, Tìm Kiếm, OTA, Vé Xe, Game...)
- Mỗi Sub-project / Dự án độc lập khi xổ ra gồm:
  1. Dòng Header dự án (Tổng PV của dự án =SUM 5 kênh)
  2. Dòng Total Clicks (OneLink W2A clicks chính xác từ GA4)
  3. 5 Kênh chi tiết: Organic, Paid, Direct, Referral, Others (công thức SUMPRODUCT)
- Mỗi Hub lớn có dòng tổng Hub (=SUM các sub-projects con)
- Thiết lập 2 tầng Row Groups (Tier 1: Hub -> Sub-projects; Tier 2: Sub-project -> Kênh)
- Cột so sánh:
  + Cột J: T11 vs T10 (So sánh MTD Ngày 1 của T11 vs T10: =H - G)
  + Cột K: % MoM MTD
  + Cột L: W2A CVR (=G_click / G_proj)
  + Cột V: T10 vs T9 (So sánh Full Month của T10 vs T9: =S - R)
  + Cột W: % MoM Full Month
- Phong cách tối giản ("Không màu mè"): Nền trắng sạch, viền xám mảnh, kênh canh phải màu xám #5F6368.
- Đồng bộ trực tiếp Google Sheets Cloud SSOT và local Excel.
"""

import os
import sys
import json
import time
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

MTD_SERIALS = [46143, 46174, 46204, 46235, 46266, 46296, 46327, 46357] # May..Dec

# 8 HUBS LỚN VỚI 40 SUB-PROJECTS CHI TIẾT
HUB_STRUCTURE = {
    "Cinema Hub": [
        ("Cinema_Cineplex Page", ["Cinema_Cineplex Page"]),
        ("Cinema_Page", ["Cinema_Page"]),
        ("Cinema_Blog", ["Cinema_Blog"]),
        ("Cinema_Home Page", ["Cinema_Home Page"]),
        ("Cinema_Landing Page", ["Cinema_Landing Page"]),
        ("Cinema_News", ["Cinema_News"]),
    ],
    "Financial Hub": [
        ("Vay Nhanh", ["Vay Nhanh", "Vay nhanh"]),
        ("Ví Trả Sau", ["Ví Trả Sau"]),
        ("Túi Thần Tài", ["Túi Thần Tài"]),
        ("Điểm Tín Dụng", ["Điểm Tín Dụng"]),
        ("Mở Thẻ Tín Dụng", ["Mở Thẻ Tín Dụng"]),
        ("Chứng Khoán", ["Chứng Khoán"]),
        ("Tiết Kiệm Online", ["Tiết Kiệm Online"]),
        ("Quản Lý Chi Tiêu", ["Quản Lý Chi Tiêu", "Quản lý chi tiêu"]),
        ("Thanh Toán Khoản Vay", ["Thanh Toán Khoản Vay"]),
        ("Thanh Toán Thẻ Tín Dụng", ["Thanh Toán Thẻ Tín Dụng"]),
        ("Chứng Chỉ Quỹ", ["Chứng Chỉ Quỹ"]),
        ("Trung Tâm Tài Chính", ["Trung Tâm Tài Chính", "Trung tâm tài chính"]),
        ("Trả Góp Apple", ["Trả Góp Apple"]),
        ("Sàn Đầu Tư", ["Sàn Đầu Tư"]),
    ],
    "Vehicle Hub": [
        ("Phạt nguội", ["Phạt nguội", "Phạt Nguội"]),
        ("Bảo Hiểm Ô Tô", ["Bảo Hiểm Ô Tô"]),
        ("Bảo Hiểm Xe Máy", ["Bảo Hiểm Xe Máy"]),
        ("Tiện Ích Giao Thông", ["Tiện Ích Giao Thông", "Phí Không Dừng"]),
    ],
    "Bảo Hiểm (InsurTech)": [
        ("Bảo Hiểm Y Tế", ["Bảo Hiểm Y Tế"]),
        ("Bảo Hiểm Sức Khỏe", ["Bảo Hiểm Sức Khỏe"]),
        ("Bảo Hiểm Xã Hội", ["Bảo Hiểm Xã Hội"]),
        ("Bảo Hiểm Chung", ["Bảo Hiểm"]),
    ],
    "Telco & Data": [
        ("Sim", ["Sim"]),
        ("Esim", ["Esim"]),
        ("Data", ["Data"]),
    ],
    "Student Hub": [
        ("Student Pass", ["Student Pass"]),
        ("Student Hub", ["Student Hub"]),
    ],
    "Utilities & Billpay": [
        ("Billpay", ["Billpay"]),
        ("Điện", ["Điện"]),
        ("Nước", ["Nước"]),
    ],
    "Entertainment & Travel": [
        ("OTA", ["OTA"]),
        ("Vé Xe", ["Vé Xe"]),
        ("Vé số", ["Vé số"]),
        ("Game", ["Game", "Nạp thẻ Game"]),
    ]
}

# 25 DỰ ÁN ĐỘC LẬP
STANDALONE_PROJECTS = [
    ("Home MoMo", ["Home MoMo"]),
    ("Download", ["Download"]),
    ("New User", ["New User"]),
    ("Tìm Kiếm", ["Tìm Kiếm"]),
    ("Tiktok", ["Tiktok"]),
    ("Soundbox", ["Soundbox"]),
    ("Merchant", ["Merchant"]),
    ("Campaign", ["Campaign"]),
    ("Blog", ["Blog"]),
    ("Tin Tức", ["Tin Tức"]),
    ("Khuyến mãi", ["Khuyến mãi"]),
    ("Application Store", ["Application Store"]),
    ("Dịch vụ liên kết", ["Dịch vụ liên kết"]),
    ("P2P", ["P2P"]),
    ("Cross Border", ["Cross Border"]),
    ("Hoàn Tiền Mua Sắm", ["Hoàn Tiền Mua Sắm"]),
    ("Mở tài khoản ngân hàng", ["Mở tài khoản ngân hàng"]),
    ("Hỏi đáp", ["Hỏi đáp"]),
    ("TnC", ["TnC", "Tnc"]),
    ("Trust", ["Trust"]),
    ("Guide", ["Guide"]),
    ("Donation", ["Donation"]),
    ("Tiệm Vàng Online", ["Tiệm Vàng Online"]),
    ("Tỷ Giá", ["Tỷ Giá"]),
    ("Others", ["Others", "XU"]),
]

def make_filter(aliases, pivot_sheet="MTD Pivot"):
    if len(aliases) == 1:
        return f"('{pivot_sheet}'!$A$3:$A$400=\"{aliases[0]}\")"
    terms = [f"('{pivot_sheet}'!$A$3:$A$400=\"{a}\")" for a in aliases]
    return f"({' + '.join(terms)} > 0)"

def fetch_clicks_from_ga4(ga4_token):
    print("  [GA4] Đang quét mapping rules và lấy Clicks cho 65 projects...")
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

    # Bảng ánh xạ alias sang tên chuẩn
    alias_map = {}
    for hub, sublist in HUB_STRUCTURE.items():
        for sub_name, aliases in sublist:
            for a in aliases:
                alias_map[a.lower()] = sub_name
    for p_name, aliases in STANDALONE_PROJECTS:
        for a in aliases:
            alias_map[a.lower()] = p_name

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
        mapped = defaultdict(int)
        for r in res.get("rows", []):
            lp = r["dimensionValues"][0]["value"]
            cnt = int(r["metricValues"][0]["value"])
            resolved = upr.resolve_primary("https://www.momo.vn" + lp, rules, inferred)
            key = alias_map.get(resolved.lower(), resolved)
            mapped[key] += cnt
        clicks_by_month[m] = mapped
        print(f"      ✓ {m}: {sum(mapped.values()):,} clicks")

    return clicks_by_month

def plan_layout():
    """Tính toán trước số dòng 1-based cố định cho mọi Hub, Sub-project và Dự án độc lập."""
    cur_row = 3 # Row 1: Header, Row 2: Grand Total Web
    hub_plans = []
    top_level_pv_rows = []
    all_ck_oct_cells = []

    for hub_name, sublist in HUB_STRUCTURE.items():
        r_hub = cur_row
        top_level_pv_rows.append(r_hub)
        cur_row += 1
        sub_plans = []
        for sub_name, aliases in sublist:
            r_sub = cur_row
            r_ck = cur_row + 1
            r_org = cur_row + 2
            r_oth = cur_row + 6
            sub_plans.append({
                "name": sub_name,
                "aliases": aliases,
                "r_sub": r_sub,
                "r_ck": r_ck,
                "r_org": r_org,
                "r_oth": r_oth
            })
            all_ck_oct_cells.append(f"G{r_ck}")
            cur_row += 7
        hub_plans.append({
            "name": hub_name,
            "r_hub": r_hub,
            "subprojects": sub_plans,
            "sub_start": r_hub + 1,
            "sub_end": cur_row - 1
        })

    standalone_plans = []
    for p_name, aliases in STANDALONE_PROJECTS:
        r_p = cur_row
        top_level_pv_rows.append(r_p)
        r_ck = cur_row + 1
        r_org = cur_row + 2
        r_oth = cur_row + 6
        all_ck_oct_cells.append(f"G{r_ck}")
        standalone_plans.append({
            "name": p_name,
            "aliases": aliases,
            "r_p": r_p,
            "r_ck": r_ck,
            "r_org": r_org,
            "r_oth": r_oth
        })
        cur_row += 7

    return hub_plans, standalone_plans, top_level_pv_rows, all_ck_oct_cells

def build_grid(clicks_by_month):
    hub_plans, standalone_plans, top_level_pv_rows, all_ck_oct_cells = plan_layout()
    grid = []
    project_meta = []
    channels = ["Organic", "Paid", "Direct", "Referral", "Others"]
    m_keys = ["May", "Jun", "Jul", "Aug", "Sep", "Oct"]

    # ROW 1: Header Tháng & Chỉ số (Đã xóa Row 1 nhóm danh mục cũ)
    r1 = ["Chỉ số / Tên Dự Án"]
    r1.extend(MTD_SERIALS)
    r1.extend(["T11 vs T10", "% MoM", "CVR %", ""])
    r1.extend(MTD_SERIALS)
    r1.extend(["T11 vs T10", "% MoM"])
    grid.append(r1)

    # ROW 2: Grand Total Web (Toàn bộ website = SUM các Hubs + Dự án độc lập)
    r2 = ["Page views (Actual)"]
    for c_idx in range(8):
        c_let = chr(ord('B') + c_idx)
        sum_args = ", ".join([f"{c_let}{r}" for r in top_level_pv_rows])
        r2.append(f"=SUM({sum_args})")
    r2.append("=H2-G2")
    r2.append('=IF(AND(ISNUMBER(H2), ISNUMBER(G2), G2>0), (H2-G2)/G2, "")')
    # CVR toàn web = Tổng Clicks của tất cả 65 projects / G2
    all_ck_oct = ", ".join(all_ck_oct_cells)
    r2.append(f"=IFERROR(SUM({all_ck_oct})/G2, \"\")")
    r2.append("") # M
    for c_idx in range(8):
        c_let = chr(ord('N') + c_idx)
        sum_args = ", ".join([f"{c_let}{r}" for r in top_level_pv_rows])
        r2.append(f"=SUM({sum_args})")
    r2.append("=T2-S2")
    r2.append('=IF(AND(ISNUMBER(T2), ISNUMBER(S2), S2>0), (T2-S2)/S2, "")')
    grid.append(r2)

    # 1. DUYỆT 8 HUBS (Xây dựng tuần tự từ trên xuống dưới, không insert)
    for h in hub_plans:
        hub_name = h["name"]
        r_hub = h["r_hub"]
        sub_pv_rows = [sub["r_sub"] for sub in h["subprojects"]]
        sub_ck_rows = [sub["r_ck"] for sub in h["subprojects"]]

        # Dòng Header Hub
        row_hub = [hub_name]
        # MTD B..I: =SUM(các r_sub)
        for c_idx in range(8):
            c_let = chr(ord('B') + c_idx)
            sub_sum_args = ", ".join([f"{c_let}{r}" for r in sub_pv_rows])
            row_hub.append(f'=IF(SUM({sub_sum_args})>0, SUM({sub_sum_args}), "")')
        row_hub.append(f'=IF(AND(ISNUMBER(H{r_hub}), ISNUMBER(G{r_hub})), H{r_hub}-G{r_hub}, "")')
        row_hub.append(f'=IF(AND(ISNUMBER(H{r_hub}), ISNUMBER(G{r_hub}), G{r_hub}>0), (H{r_hub}-G{r_hub})/G{r_hub}, "")')
        hub_ck_sum_args = ", ".join([f"G{r}" for r in sub_ck_rows])
        row_hub.append(f'=IFERROR(SUM({hub_ck_sum_args})/G{r_hub}, "")')
        row_hub.append("") # M
        # Full Month N..U: =SUM(các r_sub)
        for c_idx in range(8):
            c_let = chr(ord('N') + c_idx)
            sub_sum_args = ", ".join([f"{c_let}{r}" for r in sub_pv_rows])
            row_hub.append(f'=IF(SUM({sub_sum_args})>0, SUM({sub_sum_args}), "")')
        row_hub.append(f'=IF(AND(ISNUMBER(T{r_hub}), ISNUMBER(S{r_hub})), T{r_hub}-S{r_hub}, "")')
        row_hub.append(f'=IF(AND(ISNUMBER(T{r_hub}), ISNUMBER(S{r_hub}), S{r_hub}>0), (T{r_hub}-S{r_hub})/S{r_hub}, "")')
        grid.append(row_hub)

        project_meta.append({
            "type": "hub",
            "r_hub": r_hub,
            "sub_start": h["sub_start"],
            "sub_end": h["sub_end"]
        })

        # Từng sub-project con trong Hub
        for sub in h["subprojects"]:
            sub_name = sub["name"]
            aliases = sub["aliases"]
            r_sub = sub["r_sub"]
            r_ck = sub["r_ck"]
            r_org = sub["r_org"]
            r_oth = sub["r_oth"]

            # Dòng Header Sub-project
            row_sub = [f"  {sub_name}"]
            # MTD B..I: =SUM(B_org:B_oth)
            for c_idx in range(8):
                c_let = chr(ord('B') + c_idx)
                row_sub.append(f'=IF(SUM({c_let}{r_org}:{c_let}{r_oth})>0, SUM({c_let}{r_org}:{c_let}{r_oth}), "")')
            # J: T11 vs T10 (=H - G)
            row_sub.append(f'=IF(AND(ISNUMBER(H{r_sub}), ISNUMBER(G{r_sub})), H{r_sub}-G{r_sub}, "")')
            # K: % MoM MTD
            row_sub.append(f'=IF(AND(ISNUMBER(H{r_sub}), ISNUMBER(G{r_sub}), G{r_sub}>0), (H{r_sub}-G{r_sub})/G{r_sub}, "")')
            # L: CVR (=Clicks / PV tháng 10)
            row_sub.append(f'=IFERROR(G{r_ck}/G{r_sub}, "")')
            # M: Blank
            row_sub.append("")
            # Full Month N..U: =SUM(N_org:N_oth)
            for c_idx in range(8):
                c_let = chr(ord('N') + c_idx)
                row_sub.append(f'=IF(SUM({c_let}{r_org}:{c_let}{r_oth})>0, SUM({c_let}{r_org}:{c_let}{r_oth}), "")')
            # V: T11 vs T10 (=T - S)
            row_sub.append(f'=IF(AND(ISNUMBER(T{r_sub}), ISNUMBER(S{r_sub})), T{r_sub}-S{r_sub}, "")')
            # W: % MoM Full
            row_sub.append(f'=IF(AND(ISNUMBER(T{r_sub}), ISNUMBER(S{r_sub}), S{r_sub}>0), (T{r_sub}-S{r_sub})/S{r_sub}, "")')
            grid.append(row_sub)

            # Dòng Total Clicks Sub-project
            row_ck = ["  Total Clicks"]
            for m in m_keys:
                c_val = clicks_by_month.get(m, {}).get(sub_name, 0)
                row_ck.append(c_val if c_val > 0 else "")
            row_ck.extend(["", ""]) # H, I
            row_ck.append(f'=IF(AND(ISNUMBER(H{r_ck}), ISNUMBER(G{r_ck})), H{r_ck}-G{r_ck}, "")')
            row_ck.append(f'=IF(AND(ISNUMBER(H{r_ck}), ISNUMBER(G{r_ck}), G{r_ck}>0), (H{r_ck}-G{r_ck})/G{r_ck}, "")')
            row_ck.extend(["", ""]) # L, M
            for m in m_keys:
                c_val = clicks_by_month.get(m, {}).get(sub_name, 0)
                row_ck.append(c_val if c_val > 0 else "")
            row_ck.extend(["", ""]) # T, U
            row_ck.append(f'=IF(AND(ISNUMBER(T{r_ck}), ISNUMBER(S{r_ck})), T{r_ck}-S{r_ck}, "")')
            row_ck.append(f'=IF(AND(ISNUMBER(T{r_ck}), ISNUMBER(S{r_ck}), S{r_ck}>0), (T{r_ck}-S{r_ck})/S{r_ck}, "")')
            grid.append(row_ck)

            # 5 Dòng Kênh Sub-project
            f_mtd = make_filter(aliases, "MTD Pivot")
            f_full = make_filter(aliases, "Full month Pivot")
            for ch_idx, ch_name in enumerate(channels):
                r_ch = r_org + ch_idx
                row_ch = [ch_name]
                # MTD B..I
                for c_idx in range(8):
                    c_let = chr(ord('B') + c_idx)
                    row_ch.append(f"=SUMPRODUCT({f_mtd} * ('MTD Pivot'!$C$3:$C$400=\"{ch_name}\") * ('MTD Pivot'!$D$2:$K$2={c_let}$1) * 'MTD Pivot'!$D$3:$K$400)")
                row_ch.append(f'=IF(AND(ISNUMBER(H{r_ch}), ISNUMBER(G{r_ch})), H{r_ch}-G{r_ch}, "")')
                row_ch.append(f'=IF(AND(ISNUMBER(H{r_ch}), ISNUMBER(G{r_ch}), G{r_ch}>0), (H{r_ch}-G{r_ch})/G{r_ch}, "")')
                row_ch.extend(["", ""]) # L, M
                # Full Month N..U
                for c_idx in range(8):
                    c_let = chr(ord('N') + c_idx)
                    row_ch.append(f"=SUMPRODUCT({f_full} * ('Full month Pivot'!$C$3:$C$400=\"{ch_name}\") * ('Full month Pivot'!$D$2:$K$2={c_let}$1) * 'Full month Pivot'!$D$3:$K$400)")
                row_ch.append(f'=IF(AND(ISNUMBER(T{r_ch}), ISNUMBER(S{r_ch})), T{r_ch}-S{r_ch}, "")')
                row_ch.append(f'=IF(AND(ISNUMBER(T{r_ch}), ISNUMBER(S{r_ch}), S{r_ch}>0), (T{r_ch}-S{r_ch})/S{r_ch}, "")')
                grid.append(row_ch)

            project_meta.append({
                "type": "sub_project",
                "r_proj": r_sub,
                "r_ck": r_ck,
                "r_org": r_org,
                "r_oth": r_oth
            })

    # 2. DUYỆT 25 DỰ ÁN ĐỘC LẬP
    for p in standalone_plans:
        p_name = p["name"]
        aliases = p["aliases"]
        r_p = p["r_p"]
        r_ck = p["r_ck"]
        r_org = p["r_org"]
        r_oth = p["r_oth"]

        # Dòng Header Dự án độc lập
        row_p = [p_name]
        for c_idx in range(8):
            c_let = chr(ord('B') + c_idx)
            row_p.append(f'=IF(SUM({c_let}{r_org}:{c_let}{r_oth})>0, SUM({c_let}{r_org}:{c_let}{r_oth}), "")')
        row_p.append(f'=IF(AND(ISNUMBER(H{r_p}), ISNUMBER(G{r_p})), H{r_p}-G{r_p}, "")')
        row_p.append(f'=IF(AND(ISNUMBER(H{r_p}), ISNUMBER(G{r_p}), G{r_p}>0), (H{r_p}-G{r_p})/G{r_p}, "")')
        row_p.append(f'=IFERROR(G{r_ck}/G{r_p}, "")')
        row_p.append("") # M
        for c_idx in range(8):
            c_let = chr(ord('N') + c_idx)
            row_p.append(f'=IF(SUM({c_let}{r_org}:{c_let}{r_oth})>0, SUM({c_let}{r_org}:{c_let}{r_oth}), "")')
        row_p.append(f'=IF(AND(ISNUMBER(T{r_p}), ISNUMBER(S{r_p})), T{r_p}-S{r_p}, "")')
        row_p.append(f'=IF(AND(ISNUMBER(T{r_p}), ISNUMBER(S{r_p}), S{r_p}>0), (T{r_p}-S{r_p})/S{r_p}, "")')
        grid.append(row_p)

        # Dòng Clicks
        row_ck = ["  Total Clicks"]
        for m in m_keys:
            c_val = clicks_by_month.get(m, {}).get(p_name, 0)
            row_ck.append(c_val if c_val > 0 else "")
        row_ck.extend(["", ""]) # H, I
        row_ck.append(f'=IF(AND(ISNUMBER(H{r_ck}), ISNUMBER(G{r_ck})), H{r_ck}-G{r_ck}, "")')
        row_ck.append(f'=IF(AND(ISNUMBER(H{r_ck}), ISNUMBER(G{r_ck}), G{r_ck}>0), (H{r_ck}-G{r_ck})/G{r_ck}, "")')
        row_ck.extend(["", ""]) # L, M
        for m in m_keys:
            c_val = clicks_by_month.get(m, {}).get(p_name, 0)
            row_ck.append(c_val if c_val > 0 else "")
        row_ck.extend(["", ""]) # T, U
        row_ck.append(f'=IF(AND(ISNUMBER(T{r_ck}), ISNUMBER(S{r_ck})), T{r_ck}-S{r_ck}, "")')
        row_ck.append(f'=IF(AND(ISNUMBER(T{r_ck}), ISNUMBER(S{r_ck}), S{r_ck}>0), (T{r_ck}-S{r_ck})/S{r_ck}, "")')
        grid.append(row_ck)

        # 5 Kênh
        f_mtd = make_filter(aliases, "MTD Pivot")
        f_full = make_filter(aliases, "Full month Pivot")
        for ch_idx, ch_name in enumerate(channels):
            r_ch = r_org + ch_idx
            row_ch = [ch_name]
            for c_idx in range(8):
                c_let = chr(ord('B') + c_idx)
                row_ch.append(f"=SUMPRODUCT({f_mtd} * ('MTD Pivot'!$C$3:$C$400=\"{ch_name}\") * ('MTD Pivot'!$D$2:$K$2={c_let}$1) * 'MTD Pivot'!$D$3:$K$400)")
            row_ch.append(f'=IF(AND(ISNUMBER(H{r_ch}), ISNUMBER(G{r_ch})), H{r_ch}-G{r_ch}, "")')
            row_ch.append(f'=IF(AND(ISNUMBER(H{r_ch}), ISNUMBER(G{r_ch}), G{r_ch}>0), (H{r_ch}-G{r_ch})/G{r_ch}, "")')
            row_ch.extend(["", ""]) # L, M
            for c_idx in range(8):
                c_let = chr(ord('N') + c_idx)
                row_ch.append(f"=SUMPRODUCT({f_full} * ('Full month Pivot'!$C$3:$C$400=\"{ch_name}\") * ('Full month Pivot'!$D$2:$K$2={c_let}$1) * 'Full month Pivot'!$D$3:$K$400)")
            row_ch.append(f'=IF(AND(ISNUMBER(T{r_ch}), ISNUMBER(S{r_ch})), T{r_ch}-S{r_ch}, "")')
            row_ch.append(f'=IF(AND(ISNUMBER(T{r_ch}), ISNUMBER(S{r_ch}), S{r_ch}>0), (T{r_ch}-S{r_ch})/S{r_ch}, "")')
            grid.append(row_ch)

        project_meta.append({
            "type": "standalone",
            "r_proj": r_p,
            "r_ck": r_ck,
            "r_org": r_org,
            "r_oth": r_oth
        })

    return grid, project_meta

def run():
    print("=" * 75)
    print("TÁI THIẾT SHEET 'Projects Detail Flow' CHI TIẾT 100% CÁC USE CASES (V3)")
    print("=" * 75)

    ga4_token = get_access_token()
    sheets_token = get_sheets_token()

    # 1. Kéo clicks
    clicks = fetch_clicks_from_ga4(ga4_token)

    # 2. Xây dựng grid
    print("\n[2/4] Xây dựng cấu trúc ma trận 466 hàng...")
    grid, meta = build_grid(clicks)
    total_rows = len(grid)
    print(f"  ✓ Đã sinh {total_rows} hàng, 23 cột hoàn chỉnh.")

    # 3. Ghi vào Google Sheets
    print("\n[3/4] Đồng bộ trực tiếp Google Sheets SSOT...")
    # Xóa rowGroups cũ, conditionalFormats cũ và borders cũ
    url_sheet_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}?fields=sheets(properties,merges,rowGroups,conditionalFormats)"
    req_meta = urllib.request.Request(url_sheet_meta, headers={"Authorization": f"Bearer {sheets_token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta_data = json.loads(resp.read().decode("utf-8"))

    target_sheet = next((s for s in meta_data.get("sheets", []) if s["properties"]["sheetId"] == SHEET_ID), None)
    clean_requests = []
    if target_sheet:
        for m in target_sheet.get("merges", []):
            clean_requests.append({"unmergeCells": {"range": m}})
        rgs = target_sheet.get("rowGroups", [])
        rgs_sorted = sorted(rgs, key=lambda x: x.get("depth", 1), reverse=True)
        for rg in rgs_sorted:
            clean_requests.append({"deleteDimensionGroup": {"range": rg["range"]}})
        cfs = target_sheet.get("conditionalFormats", [])
        for idx in reversed(range(len(cfs))):
            clean_requests.append({"deleteConditionalFormatRule": {"sheetId": SHEET_ID, "index": idx}})

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

    clean_requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": SHEET_ID,
                "gridProperties": {
                    "rowCount": total_rows + 20,
                    "columnCount": 26,
                    "frozenRowCount": 1,
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

    # Clear data & Ghi mới
    range_clear = f"'{SHEET_TITLE}'!A:Z"
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
        res = json.loads(resp.read().decode("utf-8"))
        print(f"  ✓ Đã ghi {res.get('updatedCells', 0):,} cells lên Google Sheets.")

    # 4. Định dạng nâng cao (Format, Styling, Row Groups, Conditional Formatting)
    format_requests = []

    # Reset toàn bộ background từ Row 2 trở xuống thành màu trắng thuần khiết (#FFFFFF) và font chuẩn
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows + 20, "startColumnIndex": 0, "endColumnIndex": 26},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                    "textFormat": {"bold": False, "fontSize": 10, "foregroundColor": {"red": 0.15, "green": 0.15, "blue": 0.15}}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)"
        }
    })

    # Styling Row 1 (Header Tháng & Chỉ số)
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 23},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.97, "green": 0.98, "blue": 0.98},
                    "textFormat": {"bold": True, "fontSize": 10, "foregroundColor": {"red": 0.12, "green": 0.14, "blue": 0.17}},
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })

    # Format Date Serial numbers in Row 1
    date_num_format = {"type": "DATE", "pattern": "mmm yy"}
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 1, "endColumnIndex": 9},
            "cell": {"userEnteredFormat": {"numberFormat": date_num_format}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 13, "endColumnIndex": 21},
            "cell": {"userEnteredFormat": {"numberFormat": date_num_format}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    # Format Grand Total Web (Row 2)
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 1},
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "LEFT",
                    "textFormat": {"bold": True, "fontSize": 11, "foregroundColor": {"red": 0.1, "green": 0.1, "blue": 0.1}}
                }
            },
            "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": 1, "endColumnIndex": 23},
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {"bold": True, "fontSize": 11, "foregroundColor": {"red": 0.1, "green": 0.1, "blue": 0.1}}
                }
            },
            "fields": "userEnteredFormat.textFormat"
        }
    })

    # Number Formats (Từ Row 2 trở xuống)
    num_fmt_int = {"type": "NUMBER", "pattern": "#,##0"}
    num_fmt_diff = {"type": "NUMBER", "pattern": "#,##0;#,##0;0"}
    num_fmt_pct = {"type": "PERCENT", "pattern": "0.0%"}

    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": 1, "endColumnIndex": 9},
            "cell": {"userEnteredFormat": {"numberFormat": num_fmt_int}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": 9, "endColumnIndex": 10},
            "cell": {"userEnteredFormat": {"numberFormat": num_fmt_diff}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": 10, "endColumnIndex": 12},
            "cell": {"userEnteredFormat": {"numberFormat": num_fmt_pct}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": 13, "endColumnIndex": 21},
            "cell": {"userEnteredFormat": {"numberFormat": num_fmt_int}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": 21, "endColumnIndex": 22},
            "cell": {"userEnteredFormat": {"numberFormat": num_fmt_diff}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    format_requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": 22, "endColumnIndex": 23},
            "cell": {"userEnteredFormat": {"numberFormat": num_fmt_pct}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    # Conditional Formatting cho Cột J, K, V, W (Chỉ đổi màu chữ text, không tô nền cell)
    cf_ranges = [
        {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": total_rows, "startColumnIndex": c, "endColumnIndex": c + 1}
        for c in [9, 10, 21, 22] # Cột J, K, V, W
    ]
    format_requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": cf_ranges,
                "booleanRule": {
                    "condition": {"type": "NUMBER_GREATER", "values": [{"userEnteredValue": "0"}]},
                    "format": {
                        "textFormat": {"foregroundColor": {"red": 0.07, "green": 0.45, "blue": 0.20}, "bold": True}
                    }
                }
            },
            "index": 0
        }
    })
    format_requests.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": cf_ranges,
                "booleanRule": {
                    "condition": {"type": "NUMBER_LESS", "values": [{"userEnteredValue": "0"}]},
                    "format": {
                        "textFormat": {"foregroundColor": {"red": 0.77, "green": 0.13, "blue": 0.12}, "bold": True}
                    }
                }
            },
            "index": 1
        }
    })

    # Row Grouping & Styling cho từng project
    for item in meta:
        if item["type"] == "hub":
            # Level 1 Group: sub_start -> sub_end
            format_requests.append({
                "addDimensionGroup": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "dimension": "ROWS",
                        "startIndex": item["sub_start"] - 1,
                        "endIndex": item["sub_end"]
                    }
                }
            })
            # Hub header: Canh trái, bold, pure white
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_hub"] - 1, "endRowIndex": item["r_hub"], "startColumnIndex": 0, "endColumnIndex": 1},
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "LEFT",
                            "textFormat": {"bold": True, "fontSize": 10, "foregroundColor": {"red": 0.12, "green": 0.14, "blue": 0.17}},
                            "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat,backgroundColor)"
                }
            })
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_hub"] - 1, "endRowIndex": item["r_hub"], "startColumnIndex": 1, "endColumnIndex": 23},
                    "cell": {
                        "userEnteredFormat": {
                            "textFormat": {"bold": True, "fontSize": 10},
                            "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                        }
                    },
                    "fields": "userEnteredFormat(textFormat,backgroundColor)"
                }
            })
        elif item["type"] in ["sub_project", "standalone"]:
            # Level 2 Group: r_ck -> r_oth
            format_requests.append({
                "addDimensionGroup": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "dimension": "ROWS",
                        "startIndex": item["r_ck"] - 1,
                        "endIndex": item["r_oth"]
                    }
                }
            })
            # 1. Tên dịch vụ: Canh trái, bold, dark charcoal
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_proj"] - 1, "endRowIndex": item["r_proj"], "startColumnIndex": 0, "endColumnIndex": 1},
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "LEFT",
                            "textFormat": {"bold": True, "fontSize": 10, "foregroundColor": {"red": 0.12, "green": 0.14, "blue": 0.17}},
                            "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat,backgroundColor)"
                }
            })
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_proj"] - 1, "endRowIndex": item["r_proj"], "startColumnIndex": 1, "endColumnIndex": 23},
                    "cell": {
                        "userEnteredFormat": {
                            "textFormat": {"bold": True},
                            "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                        }
                    },
                    "fields": "userEnteredFormat(textFormat,backgroundColor)"
                }
            })
            # 2. Total Clicks: Canh trái, màu text khác (MoMo Magenta #A50064)
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_ck"] - 1, "endRowIndex": item["r_ck"], "startColumnIndex": 0, "endColumnIndex": 1},
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "LEFT",
                            "textFormat": {
                                "bold": True,
                                "fontSize": 10,
                                "foregroundColor": {"red": 0.65, "green": 0.0, "blue": 0.39} # MoMo Magenta #A50064
                            }
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
                }
            })
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_ck"] - 1, "endRowIndex": item["r_ck"], "startColumnIndex": 1, "endColumnIndex": 23},
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "RIGHT",
                            "textFormat": {
                                "bold": True,
                                "foregroundColor": {"red": 0.65, "green": 0.0, "blue": 0.39} # MoMo Magenta #A50064
                            }
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
                }
            })
            # 3. Tên Channel: Canh phải, màu xám neutral (#5F6368)
            format_requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item["r_org"] - 1, "endRowIndex": item["r_oth"], "startColumnIndex": 0, "endColumnIndex": 1},
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "RIGHT",
                            "textFormat": {
                                "bold": False,
                                "fontSize": 9,
                                "foregroundColor": {"red": 0.37, "green": 0.39, "blue": 0.41} # #5F6368
                            }
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
                }
            })

    # Set column widths
    format_requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 260},
            "fields": "pixelSize"
        }
    })
    format_requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": SHEET_ID, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 23},
            "properties": {"pixelSize": 90},
            "fields": "pixelSize"
        }
    })

    # Gửi batch formatting
    print(f"  [Google Sheets] Đang thực thi {len(format_requests)} định dạng...")
    url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    req_batch = urllib.request.Request(
        url_batch,
        data=json.dumps({"requests": format_requests}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_batch) as resp:
        pass
    print("  ✓ Hoàn tất cấu trúc định dạng Google Sheets.")

    # 5. Lưu vào file Excel local
    print("\n[4/4] Cập nhật bản sao Excel SSOT cục bộ...")
    excel_path = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    wb = openpyxl.load_workbook(excel_path)
    if SHEET_TITLE in wb.sheetnames:
        ws = wb[SHEET_TITLE]
        # Xóa các dòng cũ
        for r in range(1, max(ws.max_row, total_rows) + 5):
            for c in range(1, 25):
                ws.cell(r, c).value = None
    else:
        ws = wb.create_sheet(SHEET_TITLE)

    from openpyxl.styles import Font, Alignment

    font_service = Font(name="Arial", size=10, bold=True, color="121417")
    font_clicks = Font(name="Arial", size=10, bold=True, color="A50064")
    font_channel = Font(name="Arial", size=9, color="5F6368")
    font_grand = Font(name="Arial", size=11, bold=True, color="101010")
    font_header = Font(name="Arial", size=10, bold=True, color="202124")

    align_left = Alignment(horizontal="left", vertical="center")
    align_right = Alignment(horizontal="right", vertical="center")
    align_center = Alignment(horizontal="center", vertical="center")

    for r_idx, row_vals in enumerate(grid, start=1):
        for c_idx, val in enumerate(row_vals, start=1):
            ws.cell(r_idx, c_idx).value = val

    # Áp dụng styling tương thích Excel cục bộ
    for c in range(1, 24):
        ws.cell(1, c).font = font_header
        ws.cell(1, c).alignment = align_center

    ws.cell(2, 1).font = font_grand
    ws.cell(2, 1).alignment = align_left
    for c in range(2, 24):
        ws.cell(2, c).font = font_grand
        ws.cell(2, c).alignment = align_right

    for item in meta:
        if item["type"] == "hub":
            ws.cell(item["r_hub"], 1).font = font_service
            ws.cell(item["r_hub"], 1).alignment = align_left
        elif item["type"] in ["sub_project", "standalone"]:
            ws.cell(item["r_proj"], 1).font = font_service
            ws.cell(item["r_proj"], 1).alignment = align_left
            ws.cell(item["r_ck"], 1).font = font_clicks
            ws.cell(item["r_ck"], 1).alignment = align_left
            for c in range(2, 24):
                ws.cell(item["r_ck"], c).font = font_clicks
                ws.cell(item["r_ck"], c).alignment = align_right
            for r_ch in range(item["r_org"], item["r_oth"] + 1):
                ws.cell(r_ch, 1).font = font_channel
                ws.cell(r_ch, 1).alignment = align_right
                for c in range(2, 24):
                    ws.cell(r_ch, c).alignment = align_right

    wb.save(excel_path)
    print(f"  ✓ Đã lưu file Excel: {excel_path}")
    print("\n" + "=" * 75)
    print("HOÀN TẤT TÁI THIẾT 'Projects Detail Flow' CHI TIẾT 100% CẢ CLOUD & LOCAL!")
    print("=" * 75)

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ALL-IN-ONE GA4 MTD PERFORMANCE SYNC (SINGLE COMMAND EXECUTION)
Đồng bộ trọn gói 1 lệnh duy nhất (One-Click) từ GA4 API sang:
1. Snapshot JSON & Consolidated (07_REPORTS/data/monthly_*.json)
2. Toàn bộ giao diện Hubs /dashboard (web-data.json & summary.json)
3. Bảng Retention Matrix & Funnel (page-retention-matrix.json)
4. Excel SSOT (web_performance_tracking.xlsx)
5. Markdown SSOT (WEB_PERFORMANCE_TRACKING_MASTER.md)
6. Tự động commit & push sang GitHub Hubs (main) qua REST API trong 10-15s.

Cách dùng:
    ./.venv/bin/python scripts/sync_ga4_master.py              # Tự động lấy MTD hôm qua
    ./.venv/bin/python scripts/sync_ga4_master.py --mtd 23     # Chỉ định cụ thể ngày MTD
    ./.venv/bin/python scripts/sync_ga4_master.py --no-push    # Chạy offline, không đẩy GitHub
"""

import os
import sys
import json
import time
import argparse
import subprocess
import zipfile
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

import openpyxl
from openpyxl.worksheet.formula import ArrayFormula
from openpyxl.workbook.views import BookView

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
if not HUBS_REPO.exists():
    HUBS_REPO = Path("/Users/hienhv/Klaus/Web-Idea/react-web-momo")

sys.path.insert(0, str(BASE_DIR))
from scripts.sync_ga4_to_hubs import get_access_token, PROPERTY_ID, run_ga4_report
from scripts.build_full_funnel_matrix import build_theme_matcher

NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace("", NS_MAIN)

def update_cell(root, coord, formula=None, val=None):
    c = root.find(f".//{{{NS_MAIN}}}c[@r=\"{coord}\"]")
    if c is None:
        m = re.match(r"([A-Z]+)(\d+)", coord)
        if not m:
            return
        col_str, row_str = m.groups()
        row_el = root.find(f".//{{{NS_MAIN}}}row[@r=\"{row_str}\"]")
        if row_el is None:
            sheet_data = root.find(f".//{{{NS_MAIN}}}sheetData")
            row_el = ET.SubElement(sheet_data, f"{{{NS_MAIN}}}row", {"r": row_str})
        c = ET.SubElement(row_el, f"{{{NS_MAIN}}}c", {"r": coord})
    
    # Formula
    f_el = c.find(f"{{{NS_MAIN}}}f")
    if formula is not None:
        if formula == "":
            if f_el is not None:
                c.remove(f_el)
        else:
            if f_el is None:
                f_el = ET.Element(f"{{{NS_MAIN}}}f")
                c.insert(0, f_el)
            f_el.text = formula
            f_el.attrib.pop("t", None)
            f_el.attrib.pop("ref", None)
            
    # Value
    v_el = c.find(f"{{{NS_MAIN}}}v")
    if val is not None:
        if v_el is None:
            v_el = ET.SubElement(c, f"{{{NS_MAIN}}}v")
        v_el.text = str(val)
        val_str = str(val)
        if not val_str.replace("-", "").replace(".", "").isdigit():
            c.attrib["t"] = "str"
        elif "t" in c.attrib:
            del c.attrib["t"]

def month_col(ws, month_str):
    """Cột của tháng trong pivot, dò theo header hàng 2 (datetime đầu tháng). Không có trả None."""
    year, month = map(int, month_str.split("-"))
    for c in range(1, ws.max_column + 1):
        v = ws.cell(2, c).value
        if isinstance(v, datetime) and v.year == year and v.month == month:
            return c
    return None

def rescale_pivot_column(ws, col, total_pv):
    """Co giãn cột tháng cho khớp total_pv, phần lệch làm tròn dồn vào dòng Others.
    Cột tháng mới còn toàn 0 thì lấy tỷ trọng cột tháng trước làm gốc, tránh dồn hết vào Others."""
    rows = [
        r for r in range(3, ws.max_row + 1)
        if str(ws.cell(r, 1).value).strip().lower() != "grand total"
    ]
    def col_vals(c):
        return {r: ws.cell(r, c).value for r in rows if isinstance(ws.cell(r, c).value, (int, float))}

    base = col_vals(col)
    if sum(base.values()) <= 0 and col > 4:
        base = col_vals(col - 1)
    s = sum(base.values())
    scale = total_pv / s if s > 0 else 1.0

    new_s = 0
    for r, val in base.items():
        new_val = round(val * scale)
        ws.cell(r, col, new_val)
        new_s += new_val
    diff = total_pv - new_s
    for r in range(3, ws.max_row + 1):
        if str(ws.cell(r, 1).value).strip() == "Others":
            ws.cell(r, col, (ws.cell(r, col).value or 0) + diff)
            break
    for r in range(3, ws.max_row + 1):
        if str(ws.cell(r, 1).value).strip().lower() == "grand total":
            ws.cell(r, col, total_pv)
            break

# Các layout sheet 3/4/5 được hỗ trợ patch cố định
XML_LAYOUT_MONTHS = ["2026-10", "2026-11"]
TARGET_OCT = 3665607
TARGET_NOV = 3829155

def patch_excel_dynamic(file_path, month_str, target_pv, days_elapsed, total_pv, organic_pv, paid_pv, direct_pv, referral_pv, others_pv, non_paid_pv, hubs_pv, cinema_sub):
    if not os.path.exists(file_path):
        print(f"Bỏ qua file không tồn tại: {file_path}")
        return

    # Cấu hình theo tháng
    if month_str == "2026-11":
        col_mtd = "L"
        col_full = "U"
        prev_mtd = "K"
        prev_full = "T"
        prev_actual = 3602023
    else:
        col_mtd = "K"
        col_full = "T"
        prev_mtd = "J"
        prev_full = "S"
        prev_actual = 3952859

    # PHASE 1: Openpyxl updates for Pivots, ArrayFormula, and Active Tab
    wb = openpyxl.load_workbook(file_path)
    for sheet_name in ("MTD Pivot", "Full month Pivot"):
        ws = wb[sheet_name]
        col = month_col(ws, month_str)
        if col is None:
            print(f"[Excel] '{sheet_name}' chưa có cột {month_str}: bỏ qua patch pivot (cần refresh pivot từ BigQuery).")
            continue
        rescale_pivot_column(ws, col, total_pv)

    # Active view
    idx = wb.sheetnames.index("Overall Performance")
    wb.active = idx
    wb.views = [BookView(activeTab=idx)]
    wb.save(file_path)

    # PHASE 2: XML Zipfile updates for Sheet 3, 4, 5, 8
    if month_str not in XML_LAYOUT_MONTHS:
        print(f"[Excel] Sheet Overall/PaidNonPaid/Target/Cinema chưa dựng cho {month_str}: bỏ qua patch XML.")
        print(f"✓ Đã patch pivot Excel SSOT: {file_path}")
        return
    temp_path = str(file_path) + ".tmp"
    cinema_tot = hubs_pv.get("cinema", 0)

    with zipfile.ZipFile(file_path, "r") as z_in, zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as z_out:
        for item in z_in.infolist():
            content = z_in.read(item.filename)
            
            # Sheet 3: Overall Performance
            if item.filename == "xl/worksheets/sheet3.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {days_elapsed}")
                update_cell(root, f"{col_mtd}5", formula=f"SUM({col_mtd}9:{col_mtd}13)", val=str(total_pv))
                update_cell(root, f"{col_mtd}6", formula=f"{col_mtd}5-{prev_mtd}5", val=str(total_pv - prev_actual))
                update_cell(root, f"{col_mtd}7", formula=f"IFERROR(({col_mtd}5/{prev_mtd}5)-1, 0)", val=str(round((total_pv / max(1, prev_actual)) - 1, 10)))
                update_cell(root, f"{col_mtd}9", formula="", val=str(organic_pv))
                update_cell(root, f"{col_mtd}10", formula="", val=str(paid_pv))
                update_cell(root, f"{col_mtd}11", formula="", val=str(direct_pv))
                update_cell(root, f"{col_mtd}12", formula="", val=str(referral_pv))
                update_cell(root, f"{col_mtd}13", formula="", val=str(others_pv))
                update_cell(root, f"{col_mtd}15", formula=f"{col_mtd}9/${col_mtd}$5", val=str(round(organic_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_mtd}16", formula=f"{col_mtd}10/${col_mtd}$5", val=str(round(paid_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_mtd}17", formula=f"{col_mtd}11/${col_mtd}$5", val=str(round(direct_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_mtd}18", formula=f"{col_mtd}12/${col_mtd}$5", val=str(round(referral_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_mtd}19", formula=f"{col_mtd}13/${col_mtd}$5", val=str(round(others_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_mtd}20", formula=f"{col_mtd}15+{col_mtd}17+{col_mtd}18+{col_mtd}19", val=str(round((organic_pv + direct_pv + referral_pv + others_pv) / max(1, total_pv), 10)))
                
                update_cell(root, f"{col_full}5", formula=f"SUM({col_full}9:{col_full}13)", val=str(total_pv))
                update_cell(root, f"{col_full}6", formula=f"{col_full}5-{prev_full}5", val=str(total_pv - prev_actual))
                update_cell(root, f"{col_full}7", formula=f"IFERROR(({col_full}5/{prev_full}5)-1, 0)", val=str(round((total_pv / max(1, prev_actual)) - 1, 10)))
                update_cell(root, f"{col_full}9", formula="", val=str(organic_pv))
                update_cell(root, f"{col_full}10", formula="", val=str(paid_pv))
                update_cell(root, f"{col_full}11", formula="", val=str(direct_pv))
                update_cell(root, f"{col_full}12", formula="", val=str(referral_pv))
                update_cell(root, f"{col_full}13", formula="", val=str(others_pv))
                update_cell(root, f"{col_full}15", formula=f"{col_full}9/${col_full}$5", val=str(round(organic_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_full}16", formula=f"{col_full}10/${col_full}$5", val=str(round(paid_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_full}17", formula=f"{col_full}11/${col_full}$5", val=str(round(direct_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_full}18", formula=f"{col_full}12/${col_full}$5", val=str(round(referral_pv / max(1, total_pv), 10)))
                update_cell(root, f"{col_full}19", formula=f"{col_full}13/${col_full}$5", val=str(round(others_pv / max(1, total_pv), 10)))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # Sheet 4: PaidNonPaid
            elif item.filename == "xl/worksheets/sheet4.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {days_elapsed}")
                update_cell(root, f"{col_mtd}5", formula=f"'Overall Performance'!{col_mtd}5", val=str(total_pv))
                update_cell(root, f"{col_mtd}6", formula=f"{col_mtd}5-{prev_mtd}5", val=str(total_pv - prev_actual))
                update_cell(root, f"{col_mtd}7", formula=f"IFERROR(({col_mtd}5/{prev_mtd}5)-1, 0)", val=str(round((total_pv / max(1, prev_actual)) - 1, 10)))
                update_cell(root, f"{col_mtd}8", formula=f"SUM({col_mtd}9:{col_mtd}12)", val=str(non_paid_pv))
                update_cell(root, f"{col_mtd}9", formula="", val=str(organic_pv))
                update_cell(root, f"{col_mtd}10", formula="", val=str(direct_pv))
                update_cell(root, f"{col_mtd}11", formula="", val=str(referral_pv))
                update_cell(root, f"{col_mtd}12", formula="", val=str(others_pv))
                update_cell(root, f"{col_mtd}13", formula="", val=str(paid_pv))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # Sheet 5: Target
            elif item.filename == "xl/worksheets/sheet5.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {days_elapsed}")
                update_cell(root, f"{col_mtd}6", formula=f"'Overall Performance'!{col_mtd}5", val=str(total_pv))
                update_cell(root, f"{col_mtd}7", formula=f"{col_mtd}6-{prev_mtd}6", val=str(total_pv - prev_actual))
                update_cell(root, f"{col_mtd}8", formula=f"IFERROR(({col_mtd}6/{prev_mtd}6)-1, 0)", val=str(round((total_pv / max(1, prev_actual)) - 1, 10)))
                prog_pct = round((total_pv / target_pv) * 100) if target_pv else 0
                update_cell(root, f"{col_mtd}9", formula=f'IFERROR(REPT("█", ROUND({col_mtd}6/{col_mtd}3*4,0)) & " " & TEXT({col_mtd}6/{col_mtd}3,"0%"), "")', val=f"█ {prog_pct}%")
                update_cell(root, f"{col_mtd}10", formula="", val=str(organic_pv))
                update_cell(root, f"{col_mtd}11", formula="", val=str(paid_pv))
                update_cell(root, f"{col_mtd}12", formula="", val=str(direct_pv))
                update_cell(root, f"{col_mtd}13", formula="", val=str(referral_pv))
                update_cell(root, f"{col_mtd}14", formula="", val=str(others_pv))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # Sheet 8: Cinema
            elif item.filename == "xl/worksheets/sheet8.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {days_elapsed}")
                update_cell(root, "H3", formula="SUM(H8,H15,H22,H29,H36,H43)", val=str(cinema_tot))
                update_cell(root, "H4", formula="H3-G3", val=str(cinema_tot - 863885))
                update_cell(root, "H5", formula="(H3/G3)-1", val=str(round((cinema_tot / 863885) - 1, 6)))
                update_cell(root, "H8", formula="sum(H9:H13)")
                update_cell(root, "H9", formula="SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Cineplex Page\", 'MTD Pivot'!$C:$C, $B9)")
                update_cell(root, "H15", formula="sum(H16:H20)")
                update_cell(root, "H16", formula="SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Page\", 'MTD Pivot'!$C:$C, $B16)")
                update_cell(root, "H22", formula="sum(H23:H27)")
                update_cell(root, "H23", formula="SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Blog\", 'MTD Pivot'!$C:$C, $B23)")
                update_cell(root, "H29", formula="sum(H30:H34)")
                update_cell(root, "H30", formula="SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Home Page\", 'MTD Pivot'!$C:$C, $B30)")
                update_cell(root, "H36", formula="sum(H37:H41)")
                update_cell(root, "H37", formula="SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_News\", 'MTD Pivot'!$C:$C, $B37)")
                update_cell(root, "H43", formula="sum(H44:H47)")
                update_cell(root, "H44", formula="SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Landing Page\", 'MTD Pivot'!$C:$C, $B44)")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            z_out.writestr(item, content)

    os.replace(temp_path, file_path)
    print(f"✓ Đã patch động Excel SSOT: {file_path}")

def main():
    start_time = time.time()
    
    parser = argparse.ArgumentParser(description="Sync GA4 MTD All-In-One")
    parser.add_argument("--mtd", type=int, default=None, help="Số ngày MTD (mặc định: ngày hôm qua)")
    parser.add_argument("--month", type=str, default=None, help="Tháng sync (YYYY-MM), mặc định tự phát hiện")
    parser.add_argument("--no-push", action="store_true", help="Không tự động push sang Hubs GitHub")
    args = parser.parse_args()

    # Xác định tháng và số ngày MTD
    now = datetime.now()
    if args.month:
        month_str = args.month
        year_val, month_val = map(int, month_str.split("-"))
    else:
        # Nếu chỉ định mtd >= 28 trong mấy ngày đầu tháng, ưu tiên sync chốt tháng trước
        if args.mtd and args.mtd >= 28 and now.day < 5:
            prev_month = now - timedelta(days=5)
            month_str = f"{prev_month.year}-{prev_month.month:02d}"
            year_val, month_val = prev_month.year, prev_month.month
        else:
            month_str = f"{now.year}-{now.month:02d}"
            year_val, month_val = now.year, now.month

    import calendar
    _, days_in_month = calendar.monthrange(year_val, month_val)

    if args.mtd:
        days_elapsed = args.mtd
    else:
        days_elapsed = max(1, (now - timedelta(days=1)).day if now.day > 1 else 1)

    days_elapsed = min(days_elapsed, days_in_month)
    start_date = f"{month_str}-01"
    end_date = f"{month_str}-{days_elapsed:02d}"
    # Tháng đủ ngày là tháng trọn: dashboard không còn "running" (khớp scripts/build-dashboard-data.py bên Hubs)
    closed = days_elapsed >= days_in_month
    report_name = f"monthly_{month_val:02d}_{year_val}_consolidated.json" if closed else f"monthly_{month_val:02d}_{year_val}_mtd_{days_elapsed}d.json"

    web_data_path = HUBS_REPO / "lib" / "dashboard" / "web-data.json"
    if not web_data_path.exists():
        sys.exit(f"Không thấy {web_data_path}: cần repo Hubs để lấy target tháng và ghi dashboard.")
    with open(web_data_path, "r", encoding="utf-8") as f:
        web_data = json.load(f)
    target_pv = web_data.get("monthTargets", {}).get(month_str)
    if not target_pv:
        print(f"⚠ Chưa có target {month_str} trong web-data.json monthTargets: bỏ qua các chỉ số % target.")
    # Target hub: lấy của tháng sync, chưa có thì dùng tháng gần nhất trước đó
    hub_targets_all = web_data.get("hubTargets", {})
    hub_target_month = max((m for m in hub_targets_all if m <= month_str), default=None)
    hub_targets = hub_targets_all.get(hub_target_month, {}) if hub_target_month else {}

    print("=" * 75)
    print(f"KHỞI CHẠY PIPELINE GA4 ALL-IN-ONE (CHU KỲ: {start_date} -> {end_date})")
    print("=" * 75)

    # 1. Xác thực Google OAuth
    print("[1/6] Xác thực Google OAuth 2.0...")
    token = get_access_token()
    date_ranges = [{"startDate": start_date, "endDate": end_date}]

    # 2. Kéo chỉ số tổng thể toàn Website (Deduplicated Property Totals)
    print("[2/6] Kéo chỉ số tổng thể toàn Website từ GA4...")
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
    row_p = res_prop["rows"][0]
    total_pv = int(row_p["metricValues"][0]["value"])
    total_sessions = int(row_p["metricValues"][1]["value"])
    total_users = int(row_p["metricValues"][2]["value"])
    total_engaged = int(row_p["metricValues"][3]["value"])
    total_duration = float(row_p["metricValues"][4]["value"])

    # 3. Kéo phân bổ kênh lưu lượng & W2A OneLink clicks
    print("[3/6] Kéo phân bổ kênh lưu lượng (Non-Paid vs. Paid)...")
    res_ch = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"}
        ],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"}
        ],
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

    w2a_map = {}
    for r in res_w2a.get("rows", []):
        ch = r["dimensionValues"][0]["value"]
        src = r["dimensionValues"][1]["value"]
        w2a_map[(ch, src)] = int(r["metricValues"][0]["value"])

    channel_stats = {}
    organic_pv = 0
    direct_pv = 0
    paid_pv = 0
    referral_pv = 0
    others_pv = 0
    non_paid_pv = 0

    for r in res_ch.get("rows", []):
        ch = r["dimensionValues"][0]["value"]
        src = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        us = int(r["metricValues"][2]["value"])
        w2a_cl = w2a_map.get((ch, src), 0)
        channel_stats[f"{ch} | {src}"] = {"pv": pv, "sessions": sess, "users": us, "w2a": w2a_cl}

        cn = ch.lower()
        sn = src.lower()
        # Quy tắc: sessionSource=in_app chuyển toàn bộ vào Referral
        if sn == "in_app" or sn.startswith("in_app"):
            referral_pv += pv
            non_paid_pv += pv
        elif "organic search" in cn:
            organic_pv += pv
            non_paid_pv += pv
        elif "direct" in cn:
            direct_pv += pv
            non_paid_pv += pv
        elif "referral" in cn:
            referral_pv += pv
            non_paid_pv += pv
        elif any(k in cn for k in ["paid", "cpc", "display"]):
            paid_pv += pv
        else:
            others_pv += pv
            non_paid_pv += pv

    # 4. Kéo phân bổ Hubs
    print("[4/6] Kéo phân bổ lưu lượng theo Hubs...")
    res_lp = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "metrics": [{"name": "screenPageViews"}],
        "limit": 10000
    })

    matcher = build_theme_matcher()
    hubs_pv = {
        "cinema": 0,
        "financial": 0,
        "new_user": 0,
        "vehicle": 0,
        "insurance": 0,
        "student": 0,
        "others": 0
    }
    cinema_sub = {
        "Trang Rạp phim": 0,
        "Trang phim chi tiết": 0,
        "Cinema_Home Page": 0,
        "Cinema_Blog": 0,
        "Cinema_Landing Page": 0,
        "Tin tức": 0,
        "Others": 0
    }

    for r in res_lp.get("rows", []):
        lp = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        t_info = matcher(lp)
        h_name = t_info[4] if t_info else "Khác"
        sec = t_info[2] if t_info else ""
        if h_name == "Cinema" or h_name.startswith("Cinema") or sec == "cinema":
            hubs_pv["cinema"] += pv
            clean_lp = lp.split("?")[0].rstrip("/")
            if clean_lp == "/cinema":
                cinema_sub["Cinema_Home Page"] += pv
            elif clean_lp.startswith("/cinema/rap"):
                cinema_sub["Trang Rạp phim"] += pv
            elif "/blog" in clean_lp or "/review" in clean_lp:
                cinema_sub["Cinema_Blog"] += pv
            elif "/tin-tuc" in clean_lp:
                cinema_sub["Tin tức"] += pv
            elif any(k in clean_lp for k in ["tang-", "ve-mien-phi", "uu-dai", "khuyen-mai", "landing"]):
                cinema_sub["Cinema_Landing Page"] += pv
            elif clean_lp.startswith("/cinema/"):
                cinema_sub["Trang phim chi tiết"] += pv
            else:
                cinema_sub["Others"] += pv
        elif h_name in ["Ví Trả Sau", "Điểm Tín Dụng", "Vay Nhanh", "Tiết Kiệm Online", "Mở Thẻ Tín Dụng", "Trung Tâm Tài Chính", "Chứng Chỉ Quỹ", "Chứng Khoán"] or sec == "Financial":
            hubs_pv["financial"] += pv
        elif h_name in ["New User"] or sec == "Brand" and ("/tai-app" in lp or "/chao-ban-moi" in lp):
            hubs_pv["new_user"] += pv
        elif h_name in ["Phạt Nguội", "Tiện Ích Giao Thông", "Phí Không Dừng", "Bảo Hiểm Ô Tô", "Bảo Hiểm Xe Máy", "Giá xăng", "Cây xăng", "Trạm sạc"] or sec == "vehicle-hub" or ("ô tô" in h_name.lower() or "xe máy" in h_name.lower()):
            hubs_pv["vehicle"] += pv
        elif h_name in ["Bảo Hiểm", "Bảo Hiểm Y Tế", "Bảo Hiểm Sức Khỏe", "Bảo Hiểm Xã Hội"] or sec == "insurtech" or "bảo hiểm" in h_name.lower():
            hubs_pv["insurance"] += pv
        elif h_name in ["Student Hub", "Student Pass"] or sec == "student":
            hubs_pv["student"] += pv
        else:
            hubs_pv["others"] += pv

    # Tính Pacing & Forecast
    daily_pace = round(total_pv / days_elapsed, 2)
    forecast_31d = round(daily_pace * days_in_month, 2)
    if target_pv:
        daily_needed = round((target_pv - total_pv) / max(1, days_in_month - days_elapsed), 2)
        forecast_pct = round((forecast_31d / target_pv) * 100, 2)
        progress_pct = round((total_pv / target_pv) * 100, 2)
    else:
        daily_needed = forecast_pct = progress_pct = None

    # 5. Cập nhật các đích dữ liệu (SSOT & Hubs)
    print("[5/6] Ghi dữ liệu đồng bộ vào SSOT Knowledge Base & Hubs /dashboard...")
    
    # 5.1 Snapshot JSON (Chỉ duy nhất 1 file SSOT consolidated của tháng, không sinh file mtd_XXd lẻ)
    consolidated_path = BASE_DIR / "07_REPORTS" / "data" / report_name
    snapshot_payload = {
        "file_source": f"GA4 Data API (Property {PROPERTY_ID})",
        "read_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "report_type": f"MTD {days_elapsed} Ngày (01/{month_val:02d} - {days_elapsed:02d}/{month_val:02d}/{year_val})",
        "days_elapsed": days_elapsed,
        "days_in_month": days_in_month,
        "target_pv": target_pv,
        "actual_mtd_pv": total_pv,
        "progress_pct": progress_pct,
        "daily_pace": daily_pace,
        "daily_needed": daily_needed,
        "forecast_31d": forecast_31d,
        "forecast_pct": forecast_pct,
        "users": total_users,
        "sessions": total_sessions,
        "channels": {
            "organic": {"pv": organic_pv, "pct": round(organic_pv / total_pv * 100, 2)},
            "direct": {"pv": direct_pv, "pct": round(direct_pv / total_pv * 100, 2)},
            "paid": {"pv": paid_pv, "pct": round(paid_pv / total_pv * 100, 2)},
            "referral": {"pv": referral_pv, "pct": round(referral_pv / total_pv * 100, 2)},
            "others": {"pv": others_pv, "pct": round(others_pv / total_pv * 100, 2)},
            "non_paid_total": {"pv": non_paid_pv, "pct": round(non_paid_pv / total_pv * 100, 2)}
        },
        "hubs": {
            h: {
                "pv": hubs_pv[h],
                "target": hub_targets.get(h),
                "pct": round(hubs_pv[h] / hub_targets[h] * 100, 2) if hub_targets.get(h) else None,
            }
            for h in ("cinema", "financial", "new_user", "vehicle", "insurance", "student")
        },
        "cinema_breakdown": {
            "Trang Rạp phim": cinema_sub["Trang Rạp phim"],
            "Trang phim chi tiết": cinema_sub["Trang phim chi tiết"],
            "Cinema_Home Page": cinema_sub["Cinema_Home Page"],
            "Cinema_Blog": cinema_sub["Cinema_Blog"],
            "Cinema_Landing Page": cinema_sub["Cinema_Landing Page"],
            "Tin tức": cinema_sub["Tin tức"],
            "Others": cinema_sub["Others"]
        }
    }
    with open(consolidated_path, "w", encoding="utf-8") as f:
        json.dump(snapshot_payload, f, ensure_ascii=False, indent=2)

    # 5.2 Web-data.json cho /dashboard
    months = web_data["months"]
    if month_str not in months:
        # Tháng mới chưa có trong dashboard: nối thêm cột rỗng cho mọi project
        months.append(month_str)
        for p in web_data["projects"]:
            p["full"].append([0, 0, 0, 0, 0])
            p["mtd"].append([0, 0, 0, 0, 0])
    m_idx = months.index(month_str)
    web_data["running"] = None if closed else {
        "month": month_str,
        "daysElapsed": days_elapsed,
        "daysInMonth": days_in_month,
        "report": report_name
    }
    web_data["generatedAt"] = datetime.now().isoformat()

    cur_ch = [0, 0, 0, 0, 0]
    for p in web_data["projects"]:
        for i in range(5):
            cur_ch[i] += p["full"][m_idx][i]
    # Kênh của tháng còn toàn 0 (tháng mới): phân bổ theo tỷ trọng project của tháng trước
    base_idx = [m_idx if cur_ch[i] > 0 or m_idx == 0 else m_idx - 1 for i in range(5)]
    base_ch = [sum(p["full"][base_idx[i]][i] for p in web_data["projects"]) for i in range(5)]
    tgt_ch = [organic_pv, paid_pv, direct_pv, referral_pv, others_pv]
    scales = [tgt_ch[i] / base_ch[i] if base_ch[i] > 0 else 1.0 for i in range(5)]

    new_ch = [0, 0, 0, 0, 0]
    for p in web_data["projects"]:
        for i in range(5):
            val = round(p["full"][base_idx[i]][i] * scales[i])
            p["full"][m_idx][i] = val
            p["mtd"][m_idx][i] = val
            new_ch[i] += val
    for i in range(5):
        d_val = tgt_ch[i] - new_ch[i]
        if d_val != 0:
            max_p = max(web_data["projects"], key=lambda p: p["full"][m_idx][i])
            max_p["full"][m_idx][i] += d_val
            max_p["mtd"][m_idx][i] += d_val

    with open(web_data_path, "w", encoding="utf-8") as f:
        json.dump(web_data, f, ensure_ascii=False, indent=2)

    # 5.3 Summary JSON: lastFull = tháng đang sync nếu đã đủ ngày, không thì tháng liền trước
    hub_name = {}
    hub_map_path = HUBS_REPO / "lib" / "dashboard" / "hub-map.json"
    if hub_map_path.exists():
        with open(hub_map_path, "r", encoding="utf-8") as f:
            hub_name = {h["id"]: h["name"] for h in json.load(f)["hubs"]}

    def month_total(i):
        return sum(sum(p["full"][i]) for p in web_data["projects"]) if i >= 0 else 0

    lf_idx = m_idx if closed else m_idx - 1
    lf_hub_pv = {}
    if lf_idx >= 0:
        for p in web_data["projects"]:
            lf_hub_pv[p["hub"]] = lf_hub_pv.get(p["hub"], 0) + sum(p["full"][lf_idx])
    last_full_hubs = [
        {"id": h, "name": hub_name.get(h, h), "pv": v}
        for h, v in sorted(lf_hub_pv.items(), key=lambda x: -x[1]) if h != "others"
    ][:6]
    running_hubs = [
        {"id": "cinema", "name": "Cinema Hub", "pv": hubs_pv["cinema"]},
        {"id": "financial", "name": "Financial Hub", "pv": hubs_pv["financial"]},
        {"id": "new_user", "name": "New User Hub", "pv": hubs_pv["new_user"]},
        {"id": "vehicle", "name": "Vehicle Hub", "pv": hubs_pv["vehicle"]},
        {"id": "insurance", "name": "Insurance Hub", "pv": hubs_pv["insurance"]},
        {"id": "student", "name": "Student Hub", "pv": hubs_pv["student"]}
    ]

    summary_payload = {
        "lastFull": {
            "month": months[lf_idx] if lf_idx >= 0 else None,
            "pv": month_total(lf_idx),
            "prevPv": month_total(lf_idx - 1),
            "target": web_data.get("monthTargets", {}).get(months[lf_idx]) if lf_idx >= 0 else None
        },
        "running": None if closed else {
            "month": month_str,
            "daysElapsed": days_elapsed,
            "daysInMonth": days_in_month,
            "report": report_name,
            "pv": total_pv,
            "target": target_pv,
            "dailyPace": round(daily_pace),
            "dailyNeeded": round(daily_needed) if daily_needed is not None else None,
            "forecast": round(forecast_31d),
            "forecastPct": forecast_pct
        },
        "hubs": last_full_hubs if closed else running_hubs,
        "lastFullHubs": last_full_hubs,
        "channels": {
            "organic": organic_pv,
            "direct": direct_pv,
            "referral": referral_pv,
            "paid": paid_pv,
            "others": others_pv
        }
    }
    with open(BASE_DIR / "07_REPORTS" / "data" / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, ensure_ascii=False, indent=2)
    with open(HUBS_REPO / "lib" / "dashboard" / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, ensure_ascii=False, indent=2)
    if (HUBS_REPO / "data" / "analytics").exists():
        with open(HUBS_REPO / "data" / "analytics" / "summary.json", "w", encoding="utf-8") as f:
            json.dump(summary_payload, f, ensure_ascii=False, indent=2)

    # 5.4 Patch Excel Tracking SSOT (BigQuery Connected Sheets)
    bq_excel = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    if bq_excel.exists():
        patch_excel_dynamic(
            str(bq_excel), month_str, target_pv, days_elapsed, total_pv,
            organic_pv, paid_pv, direct_pv, referral_pv, others_pv, non_paid_pv,
            hubs_pv, cinema_sub
        )

    # 5.5 Xuất bản lại file Excel Executive Presentation chuẩn 5 tabs
    build_script = BASE_DIR / "scripts" / "build_web_platform_performance.py"
    if build_script.exists():
        subprocess.run([sys.executable, str(build_script)], check=False)

    # 5.6 Tự động đồng bộ lên Google Sheets Native SSOT qua Cloud Sheets API
    try:
        from scripts.sync_to_google_sheet_api import sync_google_sheet
        sync_google_sheet(
            days_elapsed=days_elapsed,
            total_pv=total_pv,
            organic_pv=organic_pv,
            paid_pv=paid_pv,
            direct_pv=direct_pv,
            referral_pv=referral_pv,
            others_pv=others_pv,
            non_paid_pv=non_paid_pv,
            hubs_pv=hubs_pv,
            cinema_sub=cinema_sub,
            month=month_str
        )

        # Đồng bộ bảng Click to app by Project trong Projects Detail Flow
        try:
            from scripts.sync_projects_detail_flow_clicks import sync_google_sheet_clicks
            sync_google_sheet_clicks()
        except Exception as e:
            print(f"[Sheets-API] Lưu ý đồng bộ Click to app Projects Detail Flow: {e}")
    except Exception as e:
        print(f"[Sheets-API] Lưu ý đồng bộ Sheets API: {e}")

    # Đồng thời đồng bộ file Excel offline lên Google Drive Desktop
    gdrive_script = BASE_DIR / "scripts" / "upload_to_gdrive.py"
    if gdrive_script.exists():
        try:
            print("[Auto-Drive] Đang cập nhật bản sao tệp Excel lên Google Drive Desktop...")
            subprocess.run([sys.executable, str(gdrive_script)], check=False)
        except Exception as e:
            print(f"[Auto-Drive] Lưu ý đồng bộ Drive: {e}")

    # 5.7 Tự động đồng bộ biến động 7 ngày SERP (Gainers & Losers) vào /report và /dashboard
    try:
        print("[Auto-7D-SERP] Đang đồng bộ biến động 7 ngày SERP (Gainers & Losers) vào /report & /dashboard...")
        sync_7d_script = BASE_DIR / "scripts" / "sync_7d_performance_report.py"
        if sync_7d_script.exists():
            subprocess.run([sys.executable, str(sync_7d_script), "--no-push"], check=False)
    except Exception as e:
        print(f"[Auto-7D-SERP] Lưu ý đồng bộ 7D SERP: {e}")

    # 6. Push GitHub REST API
    if not args.no_push:
        print("[6/6] Tự động đẩy dữ liệu sang GitHub Hubs qua REST API...")
        push_script = BASE_DIR / "scripts" / "push_to_hubs_api.py"
        subprocess.run([
            sys.executable, str(push_script),
            "-m", f"data(ga4): automated all-in-one sync MTD {days_elapsed}d ({total_pv:,} PV)"
        ], check=True)
    else:
        print("[6/6] Chế độ no-push: Bỏ qua đẩy GitHub.")

    elapsed = time.time() - start_time
    print("=" * 75)
    print(f"HOÀN THÀNH TOÀN BỘ PIPELINE TRONG {elapsed:.1f} GIÂY")
    target_txt = f"{target_pv:,} ({progress_pct}%)" if target_pv else "chưa có target"
    print(f"- Lũy kế MTD {month_str}: {total_pv:,} PV / Target: {target_txt}")
    print(f"- Nhịp chạy : {daily_pace:,.0f} PV/ngày | Dự phóng {days_in_month}d: {forecast_31d:,.0f} ({forecast_pct}%)")
    print(f"- Non-Paid  : {non_paid_pv:,} PV ({non_paid_pv/total_pv*100:.1f}%) | Paid: {paid_pv:,} PV ({paid_pv/total_pv*100:.1f}%)")
    print("=" * 75)

if __name__ == "__main__":
    main()

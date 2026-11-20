# -*- coding: utf-8 -*-
"""
EXCEL PATCHER (SSOT) - trích xuất từ sync_ga4_master.py
Cập nhật Excel SSOT (web_performance_tracking.xlsx): pivot rescale,
ArrayFormula, và patch XML trực tiếp các sheet Overall/PaidNonPaid/Target/Cinema.
Pure local processing, KHÔNG gọi API ngoài.
"""

import os
import re
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

import openpyxl
from openpyxl.workbook.views import BookView

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

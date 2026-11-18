#!/usr/bin/env python3
"""
Patch Web Platform Performance Excel Workbook
- Giữ nguyên 100% cấu trúc sheet, format, màu sắc, font chữ từ file mẫu.
- Ẩn hoàn toàn các sheet Pivot ('Full month Pivot', 'MTD Pivot', 'Source Full Month', 'Source MTD', 'Structure', 'Details follow', 'Overall performance  ').
- Hiển thị đầy đủ 10 sheet nghiệp vụ:
    1. Overall Performance
    2. PaidNonPaid
    3. Target
    4. Projects Detail Flow
    5. Channel Detail Flow
    6. Cinema
    7. Financial
    8. New User
    9. Vehicle
    10. Student
- Cập nhật số liệu Tháng 10 MTD 21 ngày chuẩn xác từ GA4 & GSC.
- Bảo tồn 100% pre-calculated formula cache ở cấp độ XML nhị phân, không bị openpyxl xóa giá trị.
"""

import os
import zipfile
import re
import xml.etree.ElementTree as ET

BASE_DIR = "/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base"
SOURCE_ZIP = "/Users/hienhv/Downloads/Web Performance Tracking (1).xlsx"
DEST_ZIP = os.path.join(BASE_DIR, "07_REPORTS/web_platform_performance.xlsx")

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
    
    # Handle formula
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
            
    # Handle value
    v_el = c.find(f"{{{NS_MAIN}}}v")
    if val is not None:
        if v_el is None:
            v_el = ET.SubElement(c, f"{{{NS_MAIN}}}v")
        v_el.text = str(val)
        # Chuẩn hóa kiểu dữ liệu cho Excel (tránh lỗi sharedStrings khi ghi text trực tiếp)
        val_str = str(val)
        if not val_str.replace("-", "").replace(".", "").isdigit():
            c.attrib["t"] = "str"
        elif "t" in c.attrib:
            del c.attrib["t"]

def patch_workbook():
    print(f"Đọc file nguồn: {SOURCE_ZIP}")
    
    with zipfile.ZipFile(SOURCE_ZIP, "r") as z_in, zipfile.ZipFile(DEST_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as z_out:
        for item in z_in.infolist():
            content = z_in.read(item.filename)
            
            # 1. Update Sheet Visibility in xl/workbook.xml
            if item.filename == "xl/workbook.xml":
                root = ET.fromstring(content)
                sheets_el = root.find(f"{{{NS_MAIN}}}sheets")
                if sheets_el is not None:
                    for s in sheets_el:
                        name = s.attrib.get("name", "")
                        # Ẩn các sheet Pivot, Source, nháp
                        if any(p in name.lower() for p in ["pivot", "source", "structure", "details follow", "overall performance  "]):
                            s.attrib["state"] = "hidden"
                        else:
                            s.attrib["state"] = "visible"
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 2. Update Sheet 3: Overall Performance
            elif item.filename == "xl/worksheets/sheet3.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "K5", formula="SUM(K9:K13)", val="2507314")
                update_cell(root, "K6", formula="K5-J5", val="-1257121")
                update_cell(root, "K7", formula="IFERROR((K5/J5)-1, 0)", val="-0.3339468047")
                update_cell(root, "K9", formula="", val="1281703")   # Organic
                update_cell(root, "K10", formula="", val="276358")   # Paid
                update_cell(root, "K11", formula="", val="639195")   # Direct
                update_cell(root, "K12", formula="", val="104752")   # Referral
                update_cell(root, "K13", formula="", val="205306")   # Others
                update_cell(root, "T5", formula="SUM(T9:T13)", val="2507314")
                update_cell(root, "T6", formula="T5-S5", val="-147472")
                update_cell(root, "T7", formula="IFERROR((T5/S5)-1, 0)", val="-0.05555")
                update_cell(root, "T9", formula="", val="1281703")
                update_cell(root, "T10", formula="", val="276358")
                update_cell(root, "T11", formula="", val="639195")
                update_cell(root, "T12", formula="", val="104752")
                update_cell(root, "T13", formula="", val="205306")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 3. Update Sheet 4: PaidNonPaid
            elif item.filename == "xl/worksheets/sheet4.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "K5", formula="'Overall Performance'!K5", val="2507314")
                update_cell(root, "K6", formula="K5-J5", val="-1257121")
                update_cell(root, "K7", formula="IFERROR((K5/J5)-1, 0)", val="-0.3339468047")
                update_cell(root, "K8", formula="SUM(K9:K12)", val="2230956")
                update_cell(root, "K9", formula="", val="1281703")   # Organic
                update_cell(root, "K10", formula="", val="639195")   # Direct
                update_cell(root, "K11", formula="", val="104752")   # Referral
                update_cell(root, "K12", formula="", val="205306")   # Others
                update_cell(root, "K13", formula="", val="276358")   # Paid
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 4. Update Sheet 5: Target
            elif item.filename == "xl/worksheets/sheet5.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "K6", formula="'Overall Performance'!K5", val="2507314")
                update_cell(root, "K7", formula="K6-J6", val="-1257121")
                update_cell(root, "K8", formula="IFERROR((K6/J6)-1, 0)", val="-0.3339468047")
                update_cell(root, "K9", formula='IFERROR(REPT("█", ROUND(K6/K3*4,0)) & " " & TEXT(K6/K3,"0%"), "")', val="███ 68%")
                update_cell(root, "K10", formula="", val="1281703")  # Organic
                update_cell(root, "K11", formula="", val="276358")   # Paid
                update_cell(root, "K12", formula="", val="639195")   # Direct
                update_cell(root, "K13", formula="", val="104752")   # Referral
                update_cell(root, "K14", formula="", val="205306")   # Others
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 5. Update Sheet 8: Cinema
            elif item.filename == "xl/worksheets/sheet8.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "H3", formula="SUM(H9,H16,H23,H30,H37,H44)", val="845539")
                update_cell(root, "H4", formula="H3-G3", val="-18346")
                update_cell(root, "H5", formula="(H3/G3)-1", val="-0.021237")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 6. Update Sheet 9: Financial
            elif item.filename == "xl/worksheets/sheet9.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "H3", formula="SUM(H8,H15,H22,H36,H29,H50,H43,H64,H71,H78,H85,H92)", val="151654")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 7. Update Sheet 11: Vehicle
            elif item.filename == "xl/worksheets/sheet11.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "H2", formula="SUM(H6,H13,H20,H27,H34)", val="40386")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 8. Update Sheet 12: Student
            elif item.filename == "xl/worksheets/sheet12.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                update_cell(root, "H2", formula="SUM(H6,H13)", val="1322")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 9. Update Sheet 10: New User
            elif item.filename == "xl/worksheets/sheet10.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 21")
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            z_out.writestr(item, content)

    print(f"✓ Đã xuất bản thành công file chuẩn cấu trúc cũ tại: {DEST_ZIP}")

if __name__ == "__main__":
    patch_workbook()

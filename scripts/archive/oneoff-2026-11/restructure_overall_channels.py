"""
scripts/restructure_overall_channels.py
=============================================================================
Tái cấu trúc khối kênh truy cập (Rows 9-23) trong sheet 'Overall Performance':
  - Phân tách rõ ràng 2 nhóm lớn:
      1. Paid
      2. Non-Paid (Tổng Non-Paid = Organic + Direct + AI Traffic + Referral + Phần còn lại)
          - Organic
          - Direct
          - AI Traffic (Khai thác nguồn GA4 AI Assistant)
          - Referral
          - Phần còn lại (Others - AI Traffic)
  - Khối Số tuyệt đối (Traffic Volume): Rows 9-15
  - Khối Tỷ trọng (% Share): Rows 17-23
  - Row 5: Total page views (Actual) = Paid + Non-Paid
  - Đồng bộ trên Google Sheets SSOT (Spreadsheet ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU)
    và local Excel SSOT (07_REPORTS/web_performance_tracking.xlsx).
=============================================================================
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID

SPREADSHEET_ID = TARGET_SHEET_ID
LOCAL_EXCEL_PATH = ROOT_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
OVERALL_SHEET_ID = 1273714888

# Column mapping for Overall Performance
# B..M: Jan 26 to Dec 26 (Full Month)
# N: blank
# O..V: May 26 to Dec 26 (Month to Date)
ALL_COLS = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
FULL_COLS = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
MTD_COLS = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

# Data definitions
PAID_VALUES = {
    'B': 542134, 'C': 713478, 'D': 845345, 'E': 175402,
    'F': "='Channel Detail Flow'!V48",
    'G': "='Channel Detail Flow'!W48",
    'H': "='Channel Detail Flow'!X48",
    'I': "='Channel Detail Flow'!Y48",
    'J': "='Channel Detail Flow'!Z48",
    'K': 473481,
    'L': 210398,
    'M': "",
    'O': 97152, 'P': 356625, 'Q': 40430, 'R': 142589, 'S': 573416, 'T': 70440, 'U': 210398, 'V': ""
}

ORGANIC_VALUES = {
    'B': 1341520, 'C': 1778048, 'D': 1506731, 'E': 1513423,
    'F': "='Channel Detail Flow'!V7",
    'G': "='Channel Detail Flow'!W7",
    'H': "='Channel Detail Flow'!X7",
    'I': "='Channel Detail Flow'!Y7",
    'J': "='Channel Detail Flow'!Z7",
    'K': 1715771,
    'L': 566163,
    'M': "",
    'O': 516378, 'P': 569189, 'Q': 603654, 'R': 537049, 'S': 502226, 'T': 723081, 'U': 566163, 'V': ""
}

DIRECT_VALUES = {
    'B': 325968, 'C': 363331, 'D': 325975, 'E': 559600,
    'F': "='Channel Detail Flow'!V89",
    'G': "='Channel Detail Flow'!W89",
    'H': "='Channel Detail Flow'!X89",
    'I': "='Channel Detail Flow'!Y89",
    'J': "='Channel Detail Flow'!Z89",
    'K': 931731,
    'L': 298140,
    'M': "",
    'O': 178769, 'P': 158303, 'Q': 156283, 'R': 236645, 'S': 184996, 'T': 289733, 'U': 298140, 'V': ""
}

AI_TRAFFIC_VALUES = {
    'B': 0, 'C': 0, 'D': 0, 'E': 0,
    'F': 1301, 'G': 11742, 'H': 12750, 'I': 13563, 'J': 13238,
    'K': 18164, 'L': 9212, 'M': "",
    'O': 0, 'P': 4083, 'Q': 4303, 'R': 3997, 'S': 4236, 'T': 4747, 'U': 9212, 'V': ""
}

REFERRAL_VALUES = {
    'B': 222703, 'C': 454540, 'D': 293426, 'E': 283498,
    'F': "='Channel Detail Flow'!V130",
    'G': "='Channel Detail Flow'!W130",
    'H': "='Channel Detail Flow'!X130",
    'I': "='Channel Detail Flow'!Y130",
    'J': "='Channel Detail Flow'!Z130",
    'K': 350162,
    'L': 58826,
    'M': "",
    'O': 78163, 'P': 85791, 'Q': 64654, 'R': 93301, 'S': 106705, 'T': 102091, 'U': 58826, 'V': ""
}

REMAINDER_VALUES = {
    'B': 160088, 'C': 153070, 'D': 240949, 'E': 157039,
    'F': "='Channel Detail Flow'!V172 - F13",
    'G': "='Channel Detail Flow'!W172 - G13",
    'H': "='Channel Detail Flow'!X172 - H13",
    'I': "='Channel Detail Flow'!Y172 - I13",
    'J': "='Channel Detail Flow'!Z172 - J13",
    'K': 112714,
    'L': 46294,
    'M': "",
    'O': 41523, 'P': 26216, 'Q': 12186, 'R': 14782, 'S': 29807, 'T': 47693, 'U': 46294, 'V': ""
}


def insert_rows_if_needed(token):
    """Kiểm tra và chèn thêm 3 dòng nếu chưa chèn."""
    # Đọc cell A22 hiện tại
    sheet_name = urllib.parse.quote('Overall Performance')
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{sheet_name}!A21:A26"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    vals = [r[0] if r else "" for r in data.get("values", [])]
    print(f"[Check Grid] Rows 21-26 currently: {vals}")

    # Nếu row 22 là 'Notes', cần chèn 3 dòng giữa row 20 và row 21 để Notes lùi xuống row 25
    if len(vals) > 1 and vals[1] == "Notes":
        print("[Grid] Chèn 3 dòng tại row 21 (startIndex: 20, endIndex: 23)...")
        body = {
            "requests": [
                {
                    "insertDimension": {
                        "range": {
                            "sheetId": OVERALL_SHEET_ID,
                            "dimension": "ROWS",
                            "startIndex": 20,
                            "endIndex": 23
                        },
                        "inheritFromBefore": False
                    }
                }
            ]
        }
        b_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
        b_req = urllib.request.Request(
            b_url,
            data=json.dumps(body).encode("utf-8"),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        )
        with urllib.request.urlopen(b_req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print(f"[Grid] ✓ Đã chèn 3 dòng thành công.")
    else:
        print("[Grid] Dòng Notes đã ở vị trí thích hợp, không cần chèn thêm.")


def build_channel_updates():
    """Tạo payload cập nhật dữ liệu cho Google Sheets."""
    data = []

    # Row 5: Total page views (Actual) = Paid + Non-Paid
    for c in ['K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']:
        data.append({"range": f"'Overall Performance'!{c}5", "values": [[f"={c}9+{c}10"]]})

    # Row 8: Blank separator
    data.append({"range": "'Overall Performance'!A8", "values": [[""]]})

    # KHỐI TRAFFIC VOLUME
    # Row 9: Paid
    row9 = ["Paid"]
    for c in ALL_COLS:
        v = PAID_VALUES.get(c, "")
        row9.append(f"{v}" if str(v).startswith("=") or isinstance(v, (int, float)) else "")
    data.append({"range": "'Overall Performance'!A9:V9", "values": [
        [
            "Paid",
            PAID_VALUES['B'], PAID_VALUES['C'], PAID_VALUES['D'], PAID_VALUES['E'],
            PAID_VALUES['F'], PAID_VALUES['G'], PAID_VALUES['H'], PAID_VALUES['I'], PAID_VALUES['J'],
            PAID_VALUES['K'], PAID_VALUES['L'], PAID_VALUES['M'],
            "", # N
            PAID_VALUES['O'], PAID_VALUES['P'], PAID_VALUES['Q'], PAID_VALUES['R'], PAID_VALUES['S'], PAID_VALUES['T'], PAID_VALUES['U'], PAID_VALUES['V']
        ]
    ]})

    # Row 10: Non-Paid = SUM(B11:B15)
    row10 = ["Non-Paid"]
    for c in FULL_COLS:
        row10.append(f"=SUM({c}11:{c}15)" if c != 'M' else "=SUM(M11:M15)")
    row10.append("") # N
    for c in MTD_COLS:
        row10.append(f"=SUM({c}11:{c}15)" if c != 'V' else "=SUM(V11:V15)")
    data.append({"range": "'Overall Performance'!A10:V10", "values": [row10]})

    # Row 11:   Organic
    data.append({"range": "'Overall Performance'!A11:V11", "values": [
        [
            "  Organic",
            ORGANIC_VALUES['B'], ORGANIC_VALUES['C'], ORGANIC_VALUES['D'], ORGANIC_VALUES['E'],
            ORGANIC_VALUES['F'], ORGANIC_VALUES['G'], ORGANIC_VALUES['H'], ORGANIC_VALUES['I'], ORGANIC_VALUES['J'],
            ORGANIC_VALUES['K'], ORGANIC_VALUES['L'], ORGANIC_VALUES['M'],
            "",
            ORGANIC_VALUES['O'], ORGANIC_VALUES['P'], ORGANIC_VALUES['Q'], ORGANIC_VALUES['R'], ORGANIC_VALUES['S'], ORGANIC_VALUES['T'], ORGANIC_VALUES['U'], ORGANIC_VALUES['V']
        ]
    ]})

    # Row 12:   Direct
    data.append({"range": "'Overall Performance'!A12:V12", "values": [
        [
            "  Direct",
            DIRECT_VALUES['B'], DIRECT_VALUES['C'], DIRECT_VALUES['D'], DIRECT_VALUES['E'],
            DIRECT_VALUES['F'], DIRECT_VALUES['G'], DIRECT_VALUES['H'], DIRECT_VALUES['I'], DIRECT_VALUES['J'],
            DIRECT_VALUES['K'], DIRECT_VALUES['L'], DIRECT_VALUES['M'],
            "",
            DIRECT_VALUES['O'], DIRECT_VALUES['P'], DIRECT_VALUES['Q'], DIRECT_VALUES['R'], DIRECT_VALUES['S'], DIRECT_VALUES['T'], DIRECT_VALUES['U'], DIRECT_VALUES['V']
        ]
    ]})

    # Row 13:   AI Traffic
    data.append({"range": "'Overall Performance'!A13:V13", "values": [
        [
            "  AI Traffic",
            AI_TRAFFIC_VALUES['B'], AI_TRAFFIC_VALUES['C'], AI_TRAFFIC_VALUES['D'], AI_TRAFFIC_VALUES['E'],
            AI_TRAFFIC_VALUES['F'], AI_TRAFFIC_VALUES['G'], AI_TRAFFIC_VALUES['H'], AI_TRAFFIC_VALUES['I'], AI_TRAFFIC_VALUES['J'],
            AI_TRAFFIC_VALUES['K'], AI_TRAFFIC_VALUES['L'], AI_TRAFFIC_VALUES['M'],
            "",
            AI_TRAFFIC_VALUES['O'], AI_TRAFFIC_VALUES['P'], AI_TRAFFIC_VALUES['Q'], AI_TRAFFIC_VALUES['R'], AI_TRAFFIC_VALUES['S'], AI_TRAFFIC_VALUES['T'], AI_TRAFFIC_VALUES['U'], AI_TRAFFIC_VALUES['V']
        ]
    ]})

    # Row 14:   Referral
    data.append({"range": "'Overall Performance'!A14:V14", "values": [
        [
            "  Referral",
            REFERRAL_VALUES['B'], REFERRAL_VALUES['C'], REFERRAL_VALUES['D'], REFERRAL_VALUES['E'],
            REFERRAL_VALUES['F'], REFERRAL_VALUES['G'], REFERRAL_VALUES['H'], REFERRAL_VALUES['I'], REFERRAL_VALUES['J'],
            REFERRAL_VALUES['K'], REFERRAL_VALUES['L'], REFERRAL_VALUES['M'],
            "",
            REFERRAL_VALUES['O'], REFERRAL_VALUES['P'], REFERRAL_VALUES['Q'], REFERRAL_VALUES['R'], REFERRAL_VALUES['S'], REFERRAL_VALUES['T'], REFERRAL_VALUES['U'], REFERRAL_VALUES['V']
        ]
    ]})

    # Row 15:   Phần còn lại
    data.append({"range": "'Overall Performance'!A15:V15", "values": [
        [
            "  Phần còn lại",
            REMAINDER_VALUES['B'], REMAINDER_VALUES['C'], REMAINDER_VALUES['D'], REMAINDER_VALUES['E'],
            REMAINDER_VALUES['F'], REMAINDER_VALUES['G'], REMAINDER_VALUES['H'], REMAINDER_VALUES['I'], REMAINDER_VALUES['J'],
            REMAINDER_VALUES['K'], REMAINDER_VALUES['L'], REMAINDER_VALUES['M'],
            "",
            REMAINDER_VALUES['O'], REMAINDER_VALUES['P'], REMAINDER_VALUES['Q'], REMAINDER_VALUES['R'], REMAINDER_VALUES['S'], REMAINDER_VALUES['T'], REMAINDER_VALUES['U'], REMAINDER_VALUES['V']
        ]
    ]})

    # Row 16: Blank separator
    data.append({"range": "'Overall Performance'!A16:V16", "values": [[""] * 22]})

    # KHỐI TỶ TRỌNG (% SHARE)
    def make_pct_row(label, source_row):
        r = [label]
        for c in FULL_COLS:
            r.append(f"=IFERROR({c}{source_row}/${c}$5, \"\")")
        r.append("") # N
        for c in MTD_COLS:
            r.append(f"=IFERROR({c}{source_row}/${c}$5, \"\")")
        return r

    data.append({"range": "'Overall Performance'!A17:V17", "values": [make_pct_row("%Paid", 9)]})
    data.append({"range": "'Overall Performance'!A18:V18", "values": [make_pct_row("%Non-Paid", 10)]})
    data.append({"range": "'Overall Performance'!A19:V19", "values": [make_pct_row("  %Organic", 11)]})
    data.append({"range": "'Overall Performance'!A20:V20", "values": [make_pct_row("  %Direct", 12)]})
    data.append({"range": "'Overall Performance'!A21:V21", "values": [make_pct_row("  %AI Traffic", 13)]})
    data.append({"range": "'Overall Performance'!A22:V22", "values": [make_pct_row("  %Referral", 14)]})
    data.append({"range": "'Overall Performance'!A23:V23", "values": [make_pct_row("  %Phần còn lại", 15)]})

    # Row 24: Blank separator
    data.append({"range": "'Overall Performance'!A24:V24", "values": [[""] * 22]})

    return data


def build_formatting_requests():
    """Tạo định dạng visual: Bold, Background highlight, Number formats."""
    requests = []

    # 1. Reset background color rows 8-24 to clean/white
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": OVERALL_SHEET_ID,
                "startRowIndex": 7, # row 8 (0-indexed)
                "endRowIndex": 24,   # row 24 (0-indexed)
                "startColumnIndex": 0,
                "endColumnIndex": 22
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                    "textFormat": {"bold": False, "fontSize": 10, "fontFamily": "Arial"}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)"
        }
    })

    # 2. Highlight Non-Paid (Row 10 and Row 18) with light peach/beige
    highlight_color = {"red": 1.0, "green": 0.949, "blue": 0.8}
    for r_idx in [9, 17]: # Row 10 (index 9) and Row 18 (index 17)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": OVERALL_SHEET_ID,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 22
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": highlight_color,
                        "textFormat": {"bold": True}
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat.bold)"
            }
        })

    # 3. Bold for Paid (Row 9) and %Paid (Row 17)
    for r_idx in [8, 16]: # Row 9 (index 8) and Row 17 (index 16)
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": OVERALL_SHEET_ID,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 22
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"bold": True}
                    }
                },
                "fields": "userEnteredFormat(textFormat.bold)"
            }
        })

    # 4. Number format for Volume (Rows 9-15): Integer with comma #,##0
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": OVERALL_SHEET_ID,
                "startRowIndex": 8, # row 9
                "endRowIndex": 15,  # row 15
                "startColumnIndex": 1, # col B
                "endColumnIndex": 22   # col V
            },
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    # 5. Number format for Percentages (Rows 17-23): 0.0%
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": OVERALL_SHEET_ID,
                "startRowIndex": 16, # row 17
                "endRowIndex": 23,   # row 23
                "startColumnIndex": 1, # col B
                "endColumnIndex": 22   # col V
            },
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    return requests


def apply_google_sheets_sync(token):
    """Thực thi cập nhật Google Sheets qua API REST."""
    print("\n--- 1. Đồng bộ Google Sheets SSOT ---")
    insert_rows_if_needed(token)

    # 1. Update values
    updates = build_channel_updates()
    body = {
        "valueInputOption": "USER_ENTERED",
        "data": updates
    }
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values:batchUpdate"
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"✓ Đã cập nhật {res.get('totalUpdatedCells', 0)} cells giá trị trong Overall Performance.")

    # 2. Update formats
    format_requests = build_formatting_requests()
    b_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
    b_body = {"requests": format_requests}
    b_req = urllib.request.Request(
        b_url,
        data=json.dumps(b_body).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(b_req) as resp:
        print(f"✓ Đã áp dụng định dạng visual (Bold, Background, NumberFormat) thành công.")


def apply_local_excel_sync():
    """Đồng bộ cập nhật vào file Excel nội bộ 07_REPORTS/web_performance_tracking.xlsx."""
    print("\n--- 2. Đồng bộ Local Excel SSOT ---")
    if not LOCAL_EXCEL_PATH.exists():
        print(f"! Không tìm thấy file {LOCAL_EXCEL_PATH}")
        return

    wb = openpyxl.load_workbook(LOCAL_EXCEL_PATH)
    if "Overall Performance" not in wb.sheetnames:
        print("! Không tìm thấy sheet 'Overall Performance' trong file Excel.")
        return

    ws = wb["Overall Performance"]

    col_to_idx = {
        'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22
    }

    # Kiểm tra xem row 22 có phải Notes không
    val_a22 = ws.cell(22, 1).value
    if val_a22 == "Notes":
        print("[Excel] Chèn 3 dòng tại row 21...")
        ws.insert_rows(21, amount=3)

    # Xóa sạch dòng 8 (blank separator)
    for c_col in range(1, 23):
        ws.cell(8, c_col).value = None

    # Cập nhật Row 5
    for c_let, c_col in col_to_idx.items():
        if c_let in ['K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']:
            ws.cell(5, c_col).value = f"={c_let}9+{c_let}10"

    # Định nghĩa dữ liệu từng dòng
    rows_data = [
        (9, "Paid", PAID_VALUES, True, None, "#,##0"),
        (10, "Non-Paid", {c: f"=SUM({c}11:{c}15)" for c in ALL_COLS}, True, "FFF2CC", "#,##0"),
        (11, "  Organic", ORGANIC_VALUES, False, None, "#,##0"),
        (12, "  Direct", DIRECT_VALUES, False, None, "#,##0"),
        (13, "  AI Traffic", AI_TRAFFIC_VALUES, False, None, "#,##0"),
        (14, "  Referral", REFERRAL_VALUES, False, None, "#,##0"),
        (15, "  Phần còn lại", REMAINDER_VALUES, False, None, "#,##0"),
        (16, "", {c: "" for c in ALL_COLS}, False, None, None),
        (17, "%Paid", {c: f'=IFERROR({c}9/${c}$5, "")' for c in ALL_COLS}, True, None, "0.0%"),
        (18, "%Non-Paid", {c: f'=IFERROR({c}10/${c}$5, "")' for c in ALL_COLS}, True, "FFF2CC", "0.0%"),
        (19, "  %Organic", {c: f'=IFERROR({c}11/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (20, "  %Direct", {c: f'=IFERROR({c}12/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (21, "  %AI Traffic", {c: f'=IFERROR({c}13/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (22, "  %Referral", {c: f'=IFERROR({c}14/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (23, "  %Phần còn lại", {c: f'=IFERROR({c}15/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
    ]

    col_to_idx = {
        'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22
    }

    peach_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

    for r_num, label, val_dict, is_bold, bg_hex, num_fmt in rows_data:
        ws.cell(r_num, 1).value = label
        ws.cell(r_num, 1).font = Font(name="Arial", size=10, bold=is_bold)
        if bg_hex:
            ws.cell(r_num, 1).fill = peach_fill

        for c_let, c_col in col_to_idx.items():
            cell = ws.cell(r_num, c_col)
            val = val_dict.get(c_let, "")
            cell.value = val
            cell.font = Font(name="Arial", size=10, bold=is_bold)
            if bg_hex:
                cell.fill = peach_fill
            if num_fmt:
                cell.number_format = num_fmt

    wb.save(LOCAL_EXCEL_PATH)
    print(f"✓ Đã lưu thành công vào {LOCAL_EXCEL_PATH}")


def verify_sync(token):
    """Kiểm tra và xác thực kết quả sau khi đồng bộ."""
    print("\n--- 3. Kiểm tra & Xác thực kết quả ---")
    sheet_name = urllib.parse.quote('Overall Performance')
    
    # Đọc formatted values
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{sheet_name}!A5:V24?valueRenderOption=FORMATTED_VALUE"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    rows = data.get("values", [])
    print(f"\nBảng kết quả sau khi tái cấu trúc (Cols K: Oct 26 Full, L: Nov 26 Full, U: Nov 26 MTD):")
    print("-" * 85)
    print(f"{'Row':<4} | {'Kênh / Chỉ số':<22} | {'Oct 26 (Full)':<15} | {'Nov 26 (Full)':<15} | {'Nov 26 (MTD)':<15}")
    print("-" * 85)

    error_found = False
    for r_idx, r in enumerate(rows, start=5):
        label = r[0] if len(r) > 0 else ""
        k = r[10] if len(r) > 10 else ""
        l = r[11] if len(r) > 11 else ""
        u = r[20] if len(r) > 20 else ""
        
        # Check error
        for val in [k, l, u]:
            if any(err in str(val) for err in ["#REF!", "#VALUE!", "#NAME?", "#DIV/0!"]):
                error_found = True
                print(f"[!] PHÁT HIỆN LỖI CÔNG THỨC tại Row {r_idx}: {val}")

        if label or any([k, l, u]):
            print(f"{r_idx:2d}   | {label:<22} | {k:>15} | {l:>15} | {u:>15}")

    print("-" * 85)
    if not error_found:
        print("✓ XÁC THỰC HOÀN TOÀN: 0 lỗi công thức (#REF!, #VALUE!, #NAME?, #DIV/0!)!")
    else:
        print("! CẢNH BÁO: Có lỗi công thức cần khắc phục.")


def main():
    token = get_sheets_token()
    apply_google_sheets_sync(token)
    apply_local_excel_sync()
    verify_sync(token)


if __name__ == "__main__":
    main()

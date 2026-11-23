"""
scripts/merge_remainder_into_referral.py
=============================================================================
Gộp kênh 'Phần còn lại' vào 'Referral' trong sheet 'Overall Performance':
  - Nhóm Non-Paid gồm 4 kênh:
      1. Organic
      2. Direct
      3. AI Traffic
      4. Referral (đã gộp Phần còn lại / Others)
  - Khối Traffic Volume: Rows 9-14
  - Khối % Share: Rows 16-21
  - Row 5: Total page views (Actual) = Paid + Non-Paid
  - Xóa 2 dòng 'Phần còn lại' thừa (row 15 volume & row 23 percentage),
    đẩy dòng Notes về vị trí row 23.
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

ALL_COLS = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
FULL_COLS = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
MTD_COLS = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

col_to_idx = {
    'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22
}

# Merged Referral values: Referral + Others - AI Traffic
MERGED_REFERRAL_VALUES = {
    'B': 222703 + 160088 - 0,       # 382,791
    'C': 454540 + 153070 - 0,       # 607,610
    'D': 293426 + 240949 - 0,       # 534,375
    'E': 283498 + 157039 - 0,       # 440,537
    'F': "='Channel Detail Flow'!V130 + 'Channel Detail Flow'!V172 - F13",
    'G': "='Channel Detail Flow'!W130 + 'Channel Detail Flow'!W172 - G13",
    'H': "='Channel Detail Flow'!X130 + 'Channel Detail Flow'!X172 - H13",
    'I': "='Channel Detail Flow'!Y130 + 'Channel Detail Flow'!Y172 - I13",
    'J': "='Channel Detail Flow'!Z130 + 'Channel Detail Flow'!Z172 - J13",
    'K': 350162 + 130878 - 18164,   # 462,876
    'L': 58826 + 55506 - 9212,      # 105,120
    'M': "",
    'O': 78163 + 41523 - 0,         # 119,686
    'P': 85791 + 30299 - 4083,      # 112,007
    'Q': 64654 + 16489 - 4303,      # 76,840
    'R': 93301 + 18779 - 3997,      # 108,083
    'S': 106705 + 34043 - 4236,     # 136,512
    'T': 102091 + 52440 - 4747,     # 149,784
    'U': 58826 + 55506 - 9212,      # 105,120
    'V': ""
}

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


def delete_redundant_rows_if_needed(token):
    """Xóa 2 dòng Phần còn lại (row 23 và row 15) nếu chúng còn tồn tại."""
    sheet_name = urllib.parse.quote('Overall Performance')
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{sheet_name}!A14:A26"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    vals = [r[0] if r else "" for r in data.get("values", [])]
    print(f"[Check Grid] Current rows 14-26 in Col A: {vals}")

    requests = []
    # vals[1] is row 15 (0-indexed 14 in sheet)
    # vals[9] is row 23 (0-indexed 22 in sheet)
    has_remainder_row15 = len(vals) > 1 and "Phần còn lại" in vals[1]
    has_remainder_row23 = len(vals) > 9 and "Phần còn lại" in vals[9]

    if has_remainder_row23:
        print("[Grid] Xóa dòng 23 (%Phần còn lại - index 22)...")
        requests.append({
            "deleteDimension": {
                "range": {
                    "sheetId": OVERALL_SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": 22,
                    "endIndex": 23
                }
            }
        })

    if has_remainder_row15:
        print("[Grid] Xóa dòng 15 (Phần còn lại volume - index 14)...")
        requests.append({
            "deleteDimension": {
                "range": {
                    "sheetId": OVERALL_SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": 14,
                    "endIndex": 15
                }
            }
        })

    if requests:
        b_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
        b_body = {"requests": requests}
        b_req = urllib.request.Request(
            b_url,
            data=json.dumps(b_body).encode("utf-8"),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        )
        with urllib.request.urlopen(b_req) as resp:
            print("[Grid] ✓ Đã xóa các dòng Phần còn lại thừa.")
    else:
        print("[Grid] Cấu trúc dòng đã được điều chỉnh, không cần xóa dòng.")


def build_channel_updates():
    """Tạo payload cập nhật dữ liệu khi gộp Phần còn lại vào Referral."""
    data = []

    # Row 5: Total page views (Actual) = Paid + Non-Paid
    for c in ['K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']:
        data.append({"range": f"'Overall Performance'!{c}5", "values": [[f"={c}9+{c}10"]]})

    # Row 8: Blank separator
    data.append({"range": "'Overall Performance'!A8", "values": [[""]]})

    # KHỐI TRAFFIC VOLUME
    # Row 9: Paid
    data.append({"range": "'Overall Performance'!A9:V9", "values": [
        [
            "Paid",
            PAID_VALUES['B'], PAID_VALUES['C'], PAID_VALUES['D'], PAID_VALUES['E'],
            PAID_VALUES['F'], PAID_VALUES['G'], PAID_VALUES['H'], PAID_VALUES['I'], PAID_VALUES['J'],
            PAID_VALUES['K'], PAID_VALUES['L'], PAID_VALUES['M'],
            "",
            PAID_VALUES['O'], PAID_VALUES['P'], PAID_VALUES['Q'], PAID_VALUES['R'], PAID_VALUES['S'], PAID_VALUES['T'], PAID_VALUES['U'], PAID_VALUES['V']
        ]
    ]})

    # Row 10: Non-Paid = SUM(B11:B14)
    row10 = ["Non-Paid"]
    for c in FULL_COLS:
        row10.append(f"=SUM({c}11:{c}14)")
    row10.append("") # N
    for c in MTD_COLS:
        row10.append(f"=SUM({c}11:{c}14)")
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

    # Row 14:   Referral (đã gộp Phần còn lại)
    data.append({"range": "'Overall Performance'!A14:V14", "values": [
        [
            "  Referral",
            MERGED_REFERRAL_VALUES['B'], MERGED_REFERRAL_VALUES['C'], MERGED_REFERRAL_VALUES['D'], MERGED_REFERRAL_VALUES['E'],
            MERGED_REFERRAL_VALUES['F'], MERGED_REFERRAL_VALUES['G'], MERGED_REFERRAL_VALUES['H'], MERGED_REFERRAL_VALUES['I'], MERGED_REFERRAL_VALUES['J'],
            MERGED_REFERRAL_VALUES['K'], MERGED_REFERRAL_VALUES['L'], MERGED_REFERRAL_VALUES['M'],
            "",
            MERGED_REFERRAL_VALUES['O'], MERGED_REFERRAL_VALUES['P'], MERGED_REFERRAL_VALUES['Q'], MERGED_REFERRAL_VALUES['R'], MERGED_REFERRAL_VALUES['S'], MERGED_REFERRAL_VALUES['T'], MERGED_REFERRAL_VALUES['U'], MERGED_REFERRAL_VALUES['V']
        ]
    ]})

    # Row 15: Blank separator
    data.append({"range": "'Overall Performance'!A15:V15", "values": [[""] * 22]})

    # KHỐI TỶ TRỌNG (% SHARE)
    def make_pct_row(label, source_row):
        r = [label]
        for c in FULL_COLS:
            r.append(f"=IFERROR({c}{source_row}/${c}$5, \"\")")
        r.append("") # N
        for c in MTD_COLS:
            r.append(f"=IFERROR({c}{source_row}/${c}$5, \"\")")
        return r

    data.append({"range": "'Overall Performance'!A16:V16", "values": [make_pct_row("%Paid", 9)]})
    data.append({"range": "'Overall Performance'!A17:V17", "values": [make_pct_row("%Non-Paid", 10)]})
    data.append({"range": "'Overall Performance'!A18:V18", "values": [make_pct_row("  %Organic", 11)]})
    data.append({"range": "'Overall Performance'!A19:V19", "values": [make_pct_row("  %Direct", 12)]})
    data.append({"range": "'Overall Performance'!A20:V20", "values": [make_pct_row("  %AI Traffic", 13)]})
    data.append({"range": "'Overall Performance'!A21:V21", "values": [make_pct_row("  %Referral", 14)]})

    # Row 22: Blank separator
    data.append({"range": "'Overall Performance'!A22:V22", "values": [[""] * 22]})

    return data


def build_formatting_requests():
    """Tạo định dạng visual: Bold, Background highlight, Number formats cho 21 dòng."""
    requests = []

    # 1. Reset background color rows 8-22 to clean/white
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": OVERALL_SHEET_ID,
                "startRowIndex": 7,  # row 8
                "endRowIndex": 22,   # row 22
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

    # 2. Highlight Non-Paid (Row 10 and Row 17) with light peach/beige
    highlight_color = {"red": 1.0, "green": 0.949, "blue": 0.8}
    for r_idx in [9, 16]: # Row 10 (index 9) and Row 17 (index 16)
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

    # 3. Bold for Paid (Row 9) and %Paid (Row 16)
    for r_idx in [8, 15]: # Row 9 (index 8) and Row 16 (index 15)
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

    # 4. Number format for Volume (Rows 9-14): Integer with comma #,##0
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": OVERALL_SHEET_ID,
                "startRowIndex": 8, # row 9
                "endRowIndex": 14,  # row 14
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

    # 5. Number format for Percentages (Rows 16-21): 0.0%
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": OVERALL_SHEET_ID,
                "startRowIndex": 15, # row 16
                "endRowIndex": 21,   # row 21
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
    """Thực thi xóa dòng thừa và cập nhật Google Sheets."""
    print("\n--- 1. Đồng bộ Google Sheets SSOT ---")
    delete_redundant_rows_if_needed(token)

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
        print(f"✓ Đã áp dụng định dạng visual thành công.")


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

    # Kiểm tra và xóa 2 dòng Phần còn lại nếu có
    # Kiểm tra row 23
    val_a23 = ws.cell(23, 1).value
    if val_a23 and "Phần còn lại" in str(val_a23):
        print("[Excel] Xóa dòng 23 (%Phần còn lại)...")
        ws.delete_rows(23, 1)

    # Kiểm tra row 15
    val_a15 = ws.cell(15, 1).value
    if val_a15 and "Phần còn lại" in str(val_a15):
        print("[Excel] Xóa dòng 15 (Phần còn lại volume)...")
        ws.delete_rows(15, 1)

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
        (10, "Non-Paid", {c: f"=SUM({c}11:{c}14)" for c in ALL_COLS}, True, "FFF2CC", "#,##0"),
        (11, "  Organic", ORGANIC_VALUES, False, None, "#,##0"),
        (12, "  Direct", DIRECT_VALUES, False, None, "#,##0"),
        (13, "  AI Traffic", AI_TRAFFIC_VALUES, False, None, "#,##0"),
        (14, "  Referral", MERGED_REFERRAL_VALUES, False, None, "#,##0"),
        (15, "", {c: "" for c in ALL_COLS}, False, None, None),
        (16, "%Paid", {c: f'=IFERROR({c}9/${c}$5, "")' for c in ALL_COLS}, True, None, "0.0%"),
        (17, "%Non-Paid", {c: f'=IFERROR({c}10/${c}$5, "")' for c in ALL_COLS}, True, "FFF2CC", "0.0%"),
        (18, "  %Organic", {c: f'=IFERROR({c}11/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (19, "  %Direct", {c: f'=IFERROR({c}12/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (20, "  %AI Traffic", {c: f'=IFERROR({c}13/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (21, "  %Referral", {c: f'=IFERROR({c}14/${c}$5, "")' for c in ALL_COLS}, False, None, "0.0%"),
        (22, "", {c: "" for c in ALL_COLS}, False, None, None),
    ]

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
    
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{sheet_name}!A5:V24?valueRenderOption=FORMATTED_VALUE"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    rows = data.get("values", [])
    print(f"\nBảng kết quả sau khi gộp Phần còn lại vào Referral (Cols K: Oct 26 Full, L: Nov 26 Full, U: Nov 26 MTD):")
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

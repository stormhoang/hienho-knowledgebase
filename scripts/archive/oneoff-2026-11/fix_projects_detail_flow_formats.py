#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIX NUMBER FORMATS IN 'Projects Detail Flow' ON GOOGLE SHEETS SSOT
Chuẩn hóa toàn diện định dạng hiển thị:
- Các hàng Pageviews (8, 10, 12, ... 136): Chuyển từ '0.0%' / '+#,##0' về '#,##0'
- Cột chênh lệch (J, T): '+#,##0;-#,##0;0'
- Cột CVR (K) ở các hàng Click: '0.0%'
- Sửa nhãn A3 thành 'Page views (Actual)'
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

def run():
    print("[1/3] Đang kết nối Google Sheets API...")
    sheets_token = get_sheets_token()

    # 1. Cập nhật nhãn ô A3
    print("[2/3] Cập nhật nhãn A3 thành 'Page views (Actual)'...")
    url_a3 = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(SHEET_TITLE + '!A3')}?valueInputOption=USER_ENTERED"
    req_a3 = urllib.request.Request(
        url_a3,
        data=json.dumps({"range": f"{SHEET_TITLE}!A3", "majorDimension": "ROWS", "values": [["Page views (Actual)"]]}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req_a3) as resp:
        res_a3 = json.loads(resp.read().decode())
    print(f"  ✓ A3 updated ({res_a3.get('updatedCells', 0)} cell)")

    # 2. Xây dựng batchUpdate requests cho định dạng số
    print("[3/3] Chuẩn hóa toàn bộ Number Format từ hàng 3 đến hàng 137...")
    requests = []

    # Định dạng Row 3 (Tổng Pageviews toàn Website)
    # B3..I3: #,##0
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2, # row 3 (0-indexed)
                "endRowIndex": 3,
                "startColumnIndex": 1, # B
                "endColumnIndex": 9   # I (exclusive -> J)
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    # J3: Net change MTD
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 9, # J
                "endColumnIndex": 10
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    # K3: Total Web CVR %
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 10, # K
                "endColumnIndex": 11
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    # L3..S3: Full month #,##0
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 11, # L
                "endColumnIndex": 19   # S (exclusive -> T)
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    # T3: Net change Full month
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 19, # T
                "endColumnIndex": 20
            },
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}}},
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    # Duyệt qua tất cả 65 dự án (từ row 8 đến row 137)
    # Mỗi dự án gồm 2 hàng:
    # - Hàng PV: row 8 + 2*i (0-indexed: 7 + 2*i)
    # - Hàng Click: row 9 + 2*i (0-indexed: 8 + 2*i)
    for i in range(65):
        r_pv_0 = 7 + 2 * i
        r_ck_0 = 8 + 2 * i

        # --- FORMAT CHO HÀNG PAGEVIEWS (r_pv_0) ---
        # B..I (MTD PV): #,##0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv_0,
                    "endRowIndex": r_pv_0 + 1,
                    "startColumnIndex": 1, # B
                    "endColumnIndex": 9   # I
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # J (MTD VS. SPLM): +#,##0;-#,##0;0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv_0,
                    "endRowIndex": r_pv_0 + 1,
                    "startColumnIndex": 9, # J
                    "endColumnIndex": 10
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # L..S (Full Month PV): #,##0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv_0,
                    "endRowIndex": r_pv_0 + 1,
                    "startColumnIndex": 11, # L
                    "endColumnIndex": 19   # S
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # T (Full VS. SPLM): +#,##0;-#,##0;0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_pv_0,
                    "endRowIndex": r_pv_0 + 1,
                    "startColumnIndex": 19, # T
                    "endColumnIndex": 20
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })

        # --- FORMAT CHO HÀNG CLICKS (r_ck_0) ---
        # B..I (MTD Clicks): #,##0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ck_0,
                    "endRowIndex": r_ck_0 + 1,
                    "startColumnIndex": 1,
                    "endColumnIndex": 9
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # J (MTD VS. SPLM Clicks): +#,##0;-#,##0;0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ck_0,
                    "endRowIndex": r_ck_0 + 1,
                    "startColumnIndex": 9,
                    "endColumnIndex": 10
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # K (CVR %): 0.0%
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ck_0,
                    "endRowIndex": r_ck_0 + 1,
                    "startColumnIndex": 10, # K
                    "endColumnIndex": 11
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # L..S (Full Month Clicks): #,##0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ck_0,
                    "endRowIndex": r_ck_0 + 1,
                    "startColumnIndex": 11,
                    "endColumnIndex": 19
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # T (Full VS. SPLM Clicks): +#,##0;-#,##0;0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_ck_0,
                    "endRowIndex": r_ck_0 + 1,
                    "startColumnIndex": 19,
                    "endColumnIndex": 20
                },
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}}},
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    # Gửi batchUpdate
    url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    payload = {"requests": requests}
    req_batch = urllib.request.Request(
        url_batch,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_batch) as resp:
        res_batch = json.loads(resp.read().decode())
    print(f"  ✓ Đã áp dụng thành công {len(requests)} lệnh format ({len(res_batch.get('replies', []))} replies)!")

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script điền toàn diện dữ liệu Pageviews từ Tháng 1 đến Tháng 10 vào:
1. Google Sheets Cloud SSOT (ID 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU)
   - Sheet: 'Overall Performance'
   - Sheet: 'Overall performance  '
2. Local Excel SSOT: 07_REPORTS/web_performance_tracking.xlsx
3. Đồng bộ Google Drive Desktop
"""

import json
import urllib.request
import urllib.parse
from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).resolve().parents[1]
EXCEL_PATH = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
TARGET_SHEET_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"

MONTHLY_DATA = {
    # col: (Target, Actual, Organic, Paid, Direct, Referral, Others)
    "B": { "name": "Jan 26", "target": 2601280, "actual": 2601280, "organic": 1341520, "paid": 542134, "direct": 325968, "referral": 222703, "others": 160088 },
    "C": { "name": "Feb 26", "target": 3470470, "actual": 3470470, "organic": 1778048, "paid": 713478, "direct": 363331, "referral": 454540, "others": 153070 },
    "D": { "name": "Mar 26", "target": 3221705, "actual": 3221705, "organic": 1506731, "paid": 845345, "direct": 325975, "referral": 293426, "others": 240949 },
    "E": { "name": "Apr 26", "target": 2699883, "actual": 2699883, "organic": 1513423, "paid": 175402, "direct": 559600, "referral": 283498, "others": 157039 },
    "F": { "name": "May 26", "target": 3272867, "actual": 3273623, "organic": 1669709, "paid": 720891, "direct": 637057, "referral": 201216, "others": 44750 },
    "G": { "name": "Jun 26", "target": 3407958, "actual": 3408182, "organic": 1648740, "paid": 982492, "direct": 488592, "referral": 255134, "others": 33224 },
    "H": { "name": "Jul 26", "target": 3167821, "actual": 3167821, "organic": 1875191, "paid": 497958, "direct": 440855, "referral": 329659, "others": 24158 },
    "I": { "name": "Aug 26", "target": 3465363, "actual": 3465363, "organic": 1729694, "paid": 644539, "direct": 656271, "referral": 410305, "others": 24554 },
    "J": { "name": "Sep 26", "target": 3509044, "actual": 3952859, "organic": 1623796, "paid": 1197093, "direct": 755896, "referral": 345132, "others": 30942 },
    "K": { "name": "Oct 26", "target": 3665607, "actual": 3496864, "organic": 1665199, "paid": 456338, "direct": 907813, "referral": 340229, "others": 127285 },
}

def get_sheets_token():
    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        cdata = json.load(f)
    client_info = cdata.get("installed") or cdata.get("web")

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        tdata = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": client_info["client_id"],
        "client_secret": client_info["client_secret"],
        "refresh_token": tdata["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        return res["access_token"]

def update_google_sheets():
    token = get_sheets_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Chuẩn bị batch updates cho 'Overall Performance'
    updates = []

    # 1. Row 3: Target Jan - Apr (B3:E3)
    target_vals_b_e = [
        MONTHLY_DATA["B"]["target"],
        MONTHLY_DATA["C"]["target"],
        MONTHLY_DATA["D"]["target"],
        MONTHLY_DATA["E"]["target"]
    ]
    updates.append({
        "range": "'Overall Performance'!B3:E3",
        "values": [target_vals_b_e]
    })

    # 2. Row 4: % Growth Rate Target (C4:E4)
    updates.append({
        "range": "'Overall Performance'!C4:E4",
        "values": [["=C3/B3-1", "=D3/C3-1", "=E3/D3-1"]]
    })

    # 3. Row 5: Actual Jan - Oct (B5:K5)
    actual_vals = [MONTHLY_DATA[col]["actual"] for col in ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]]
    updates.append({
        "range": "'Overall Performance'!B5:K5",
        "values": [actual_vals]
    })

    # 4. Rows 9 to 13: Channels cho Jan - Apr (B9:E13)
    cols = ["B", "C", "D", "E"]
    organic_row = [MONTHLY_DATA[c]["organic"] for c in cols]
    paid_row = [MONTHLY_DATA[c]["paid"] for c in cols]
    direct_row = [MONTHLY_DATA[c]["direct"] for c in cols]
    referral_row = [MONTHLY_DATA[c]["referral"] for c in cols]
    others_row = [MONTHLY_DATA[c]["others"] for c in cols]

    updates.append({
        "range": "'Overall Performance'!B9:E13",
        "values": [
            organic_row,
            paid_row,
            direct_row,
            referral_row,
            others_row
        ]
    })

    # 5. Rows 15 to 20: Tỷ trọng % cho Jan - Apr (B15:E20)
    pct_organic = [f"={c}9/${c}$5" for c in cols]
    pct_paid = [f"={c}10/${c}$5" for c in cols]
    pct_direct = [f"={c}11/${c}$5" for c in cols]
    pct_referral = [f"={c}12/${c}$5" for c in cols]
    pct_others = [f"={c}13/${c}$5" for c in cols]
    non_paid = [f"={c}15+{c}17+{c}18+{c}19" for c in cols]

    updates.append({
        "range": "'Overall Performance'!B15:E20",
        "values": [
            pct_organic,
            pct_paid,
            pct_direct,
            pct_referral,
            pct_others,
            non_paid
        ]
    })

    # 6. Sửa lại Row 9-13 của Col K (Oct 26) cho chuẩn xác thứ tự kênh
    updates.append({
        "range": "'Overall Performance'!K9:K13",
        "values": [
            [MONTHLY_DATA["K"]["organic"]],
            [MONTHLY_DATA["K"]["paid"]],
            [MONTHLY_DATA["K"]["direct"]],
            [MONTHLY_DATA["K"]["referral"]],
            [MONTHLY_DATA["K"]["others"]]
        ]
    })

    # 7. Cập nhật sheet 'Overall performance  ' (Overview scenario/actual)
    updates.append({
        "range": "'Overall performance  '!B16:K20",
        "values": [
            [MONTHLY_DATA[c]["organic"] for c in ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]],
            [MONTHLY_DATA[c]["paid"] for c in ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]],
            [MONTHLY_DATA[c]["direct"] for c in ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]],
            [MONTHLY_DATA[c]["referral"] for c in ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]],
            [MONTHLY_DATA[c]["others"] for c in ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]]
        ]
    })

    # Gửi batchUpdate
    body = {
        "valueInputOption": "USER_ENTERED",
        "data": updates
    }
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values:batchUpdate"
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        print(f"✓ Google Sheets API cập nhật thành công {res.get('totalUpdatedCells')} ô trên {len(updates)} dải ô!")

def update_local_excel():
    wb = openpyxl.load_workbook(EXCEL_PATH)
    
    # Update sheet 'Overall Performance'
    if "Overall Performance" in wb.sheetnames:
        ws = wb["Overall Performance"]
        col_letters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        
        for idx, col_letter in enumerate(col_letters, start=2):
            m = MONTHLY_DATA[col_letter]
            ws.cell(row=3, column=idx, value=m["target"])
            ws.cell(row=5, column=idx, value=m["actual"])
            ws.cell(row=9, column=idx, value=m["organic"])
            ws.cell(row=10, column=idx, value=m["paid"])
            ws.cell(row=11, column=idx, value=m["direct"])
            ws.cell(row=12, column=idx, value=m["referral"])
            ws.cell(row=13, column=idx, value=m["others"])
            
            # Formulas for growth
            if idx > 2:
                prev_col = col_letters[idx - 3]
                ws.cell(row=4, column=idx, value=f"={col_letter}3/{prev_col}3-1")
                ws.cell(row=6, column=idx, value=f"={col_letter}5-{prev_col}5")
                ws.cell(row=7, column=idx, value=f"=IFERROR(({col_letter}5/{prev_col}5)-1, 0)")
            
            # Formulas for shares
            ws.cell(row=15, column=idx, value=f"={col_letter}9/${col_letter}$5")
            ws.cell(row=16, column=idx, value=f"={col_letter}10/${col_letter}$5")
            ws.cell(row=17, column=idx, value=f"={col_letter}11/${col_letter}$5")
            ws.cell(row=18, column=idx, value=f"={col_letter}12/${col_letter}$5")
            ws.cell(row=19, column=idx, value=f"={col_letter}13/${col_letter}$5")
            ws.cell(row=20, column=idx, value=f"={col_letter}15+{col_letter}17+{col_letter}18+{col_letter}19")

    # Update sheet 'Overall performance  '
    if "Overall performance  " in wb.sheetnames:
        ws2 = wb["Overall performance  "]
        for idx, col_letter in enumerate(col_letters, start=2):
            m = MONTHLY_DATA[col_letter]
            ws2.cell(row=16, column=idx, value=m["organic"])
            ws2.cell(row=17, column=idx, value=m["paid"])
            ws2.cell(row=18, column=idx, value=m["direct"])
            ws2.cell(row=19, column=idx, value=m["referral"])
            ws2.cell(row=20, column=idx, value=m["others"])
            ws2.cell(row=13, column=idx, value=f"=SUM({col_letter}16:{col_letter}20)")
            if idx > 2:
                prev_col = col_letters[idx - 3]
                ws2.cell(row=14, column=idx, value=f"={col_letter}13-{prev_col}13")
                ws2.cell(row=15, column=idx, value=f"=IFERROR(({col_letter}13/{prev_col}13)-1, 0)")

    wb.save(EXCEL_PATH)
    print(f"✓ Đã cập nhật thành công Excel cục bộ: {EXCEL_PATH}")

    # Copy sang Google Drive Desktop
    drive_dest = Path("/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#4 - Tracking & Performance/web_performance_tracking.xlsx")
    if drive_dest.parent.exists():
        import shutil
        shutil.copy2(EXCEL_PATH, drive_dest)
        print(f"✓ Đã đồng bộ sang Google Drive Desktop: {drive_dest}")

if __name__ == "__main__":
    print("=" * 70)
    print("BẮT ĐẦU ĐIỀN TOÀN BỘ DỮ LIỆU T1 - T10 VÀO SHEET OVERALL")
    print("=" * 70)
    update_google_sheets()
    update_local_excel()
    print("=" * 70)
    print("HOÀN THÀNH 100% CẬP NHẬT SHEET OVERALL!")
    print("=" * 70)

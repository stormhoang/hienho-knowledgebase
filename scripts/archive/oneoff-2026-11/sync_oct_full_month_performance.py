#!/usr/bin/env python3
"""
Sync Full Month October 2026 Performance into:
1. Google Sheet: [WP] Financial Hub | Web Product (1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A)
   Tab: Performances (Columns P & Q: Full Month 2026-10-01 & VS. LM)
2. Local Excel: 05_HUBS/financial/financial-hub-roadmap.xlsx
   Tab: Performance
3. Local Master Excel: 07_REPORTS/web_performance_tracking.xlsx
   Tab: Financial
Source of Truth:
   Google Sheet: [WP] Web Performance Tracking (1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU)
   Tab: Financial
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).resolve().parent.parent
FIN_EXCEL_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-roadmap.xlsx"
MASTER_EXCEL_PATH = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"

MASTER_SHEET_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"
FIN_SHEET_ID = "1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A"

def get_access_token():
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

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    with urllib.request.urlopen(req) as resp:
        tokens = json.loads(resp.read().decode("utf-8"))
        return tokens["access_token"]

def parse_val(v):
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    if s.endswith("%"):
        try:
            return round(float(s.replace("%", "").strip()) / 100.0, 4)
        except ValueError:
            return s
    # Check if integer or float with commas
    clean_s = s.replace(",", "")
    try:
        if "." in clean_s:
            return float(clean_s)
        return int(clean_s)
    except ValueError:
        return s

def main():
    token = get_access_token()

    # Step 1: Read Master Financial Tab from Google Sheets
    print("1. Fetching Full Month October data from Master Google Sheet Financial tab...")
    req = urllib.request.Request(
        f"https://sheets.googleapis.com/v4/spreadsheets/{MASTER_SHEET_ID}/values/Financial!A1:Q138?valueRenderOption=FORMATTED_VALUE",
        headers={"Authorization": f"Bearer {token}"}
    )
    with urllib.request.urlopen(req) as resp:
        master_data = json.loads(resp.read().decode("utf-8")).get("values", [])

    print(f"   Retrieved {len(master_data)} rows from Master Sheet.")

    # Prepare Columns P & Q values for row 1 to 138
    pq_values = []
    for r in master_data:
        p = r[15] if len(r) > 15 else ""
        q = r[16] if len(r) > 16 else ""
        pq_values.append([p, q])

    # Step 2: Update Google Sheet FinHub (Performances!P1:Q138)
    print("2. Updating Google Sheet FinHub (1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A) tab Performances...")
    url_update = f"https://sheets.googleapis.com/v4/spreadsheets/{FIN_SHEET_ID}/values/Performances!P1:Q138?valueInputOption=USER_ENTERED"
    payload = json.dumps({"values": pq_values}).encode("utf-8")
    req_update = urllib.request.Request(
        url_update,
        data=payload,
        method="PUT",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req_update) as resp:
        res_update = json.loads(resp.read().decode("utf-8"))
        print(f"   Google Sheet Performances updated: {res_update.get('updatedCells')} cells updated.")

    # Step 3: Update local Excel (financial-hub-roadmap.xlsx tab Performance)
    print("3. Updating local Excel (financial-hub-roadmap.xlsx) tab Performance...")
    wb_fin = openpyxl.load_workbook(FIN_EXCEL_PATH)
    ws_fin = wb_fin["Performance"]

    for r_idx, (p_val, q_val) in enumerate(pq_values, start=1):
        if r_idx == 1:
            ws_fin.cell(1, 16, "2026-10-01")
            ws_fin.cell(1, 17, "VS. LM")
        else:
            ws_fin.cell(r_idx, 16, parse_val(p_val))
            ws_fin.cell(r_idx, 17, parse_val(q_val))

    wb_fin.save(FIN_EXCEL_PATH)
    print("   Local Excel financial-hub-roadmap.xlsx updated successfully!")

    # Step 4: Update local Master Excel (web_performance_tracking.xlsx tab Financial)
    if MASTER_EXCEL_PATH.exists():
        print("4. Updating local Master Excel (web_performance_tracking.xlsx) tab Financial...")
        wb_master = openpyxl.load_workbook(MASTER_EXCEL_PATH)
        if "Financial" in wb_master.sheetnames:
            ws_m = wb_master["Financial"]
            for r_idx, (p_val, q_val) in enumerate(pq_values, start=1):
                if r_idx == 1:
                    ws_m.cell(1, 16, "2026-10-01")
                    ws_m.cell(1, 17, "VS. LM")
                else:
                    ws_m.cell(r_idx, 16, parse_val(p_val))
                    ws_m.cell(r_idx, 17, parse_val(q_val))
            wb_master.save(MASTER_EXCEL_PATH)
            print("   Local Master Excel updated successfully!")

    print("\nAll Full Month October performance updates completed successfully!")

if __name__ == "__main__":
    main()

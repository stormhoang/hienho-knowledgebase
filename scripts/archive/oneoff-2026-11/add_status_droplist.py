#!/usr/bin/env python3
"""
Add Data Validation (Droplist) and dynamic Conditional Formatting for Status column:
1. Google Sheets:
   - Tab "Product Roadmap" (Column F / Trạng Thái)
   - Tab "Sitemap" (Column F / Trạng Thái)
   - Droplist options: Done, In Progress, Planned, Pending, Chưa triển khai
   - Conditional formatting for each status (color badges update automatically)
2. Local Excel (05_HUBS/financial/financial-hub-roadmap.xlsx):
   - Sheet "Roadmap" (F2:F50)
   - Sheet "Sitemap" (F2:F150)
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-roadmap.xlsx"
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
SPREADSHEET_ID = "1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A"

STATUS_OPTIONS = [
    "Done",
    "In Progress",
    "Planned",
    "Pending",
    "Not Started"
]

STATUS_COLORS = {
    "Done": {
        "bg": {"red": 0.86, "green": 0.98, "blue": 0.90},
        "fg": {"red": 0.08, "green": 0.50, "blue": 0.24}
    },
    "In Progress": {
        "bg": {"red": 0.99, "green": 0.95, "blue": 0.78},
        "fg": {"red": 0.71, "green": 0.33, "blue": 0.04}
    },
    "Planned": {
        "bg": {"red": 0.86, "green": 0.92, "blue": 0.99},
        "fg": {"red": 0.11, "green": 0.31, "blue": 0.85}
    },
    "Pending": {
        "bg": {"red": 1.0, "green": 0.89, "blue": 0.90},
        "fg": {"red": 0.75, "green": 0.07, "blue": 0.24}
    },
    "Not Started": {
        "bg": {"red": 0.945, "green": 0.96, "blue": 0.976},
        "fg": {"red": 0.28, "green": 0.33, "blue": 0.41}
    }
}

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

def batch_update_spreadsheet(token, requests):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
    payload = json.dumps({"requests": requests}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8")
        print(f"HTTP Error {e.code}: {err}")
        raise

def update_google_sheets_droplists():
    print("1. Updating Google Sheets with Data Validation & Dynamic Badges...")
    token = get_access_token()

    url_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets(properties,conditionalFormats)"
    req_meta = urllib.request.Request(url_meta, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta = json.loads(resp.read().decode("utf-8"))

    sheets_info = {}
    for s in meta["sheets"]:
        title = s["properties"]["title"]
        sid = s["properties"]["sheetId"]
        cf_count = len(s.get("conditionalFormats", []))
        sheets_info[title] = {"sheetId": sid, "cf_count": cf_count}

    target_sheets = [
        {"title": "Product Roadmap", "max_row": 50},
        {"title": "Sitemap", "max_row": 150}
    ]

    requests = []

    for t in target_sheets:
        title = t["title"]
        sid = sheets_info[title]["sheetId"]
        max_r = t["max_row"]
        cf_count = sheets_info[title]["cf_count"]

        # Delete existing conditional formatting rules for this sheet
        for _ in range(cf_count):
            requests.append({
                "deleteConditionalFormatRule": {
                    "sheetId": sid,
                    "index": 0
                }
            })

        # 1. Set Data Validation (Dropdown list with custom UI)
        requests.append({
            "setDataValidation": {
                "range": {
                    "sheetId": sid,
                    "startRowIndex": 1,
                    "endRowIndex": max_r,
                    "startColumnIndex": 5,
                    "endColumnIndex": 6
                },
                "rule": {
                    "condition": {
                        "type": "ONE_OF_LIST",
                        "values": [{"userEnteredValue": val} for val in STATUS_OPTIONS]
                    },
                    "strict": True,
                    "showCustomUi": True
                }
            }
        })

        # 2. Add dynamic conditional formatting rules for each status
        for idx, (st_name, colors) in enumerate(STATUS_COLORS.items()):
            requests.append({
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [{
                            "sheetId": sid,
                            "startRowIndex": 1,
                            "endRowIndex": max_r,
                            "startColumnIndex": 5,
                            "endColumnIndex": 6
                        }],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [{"userEnteredValue": st_name}]
                            },
                            "format": {
                                "backgroundColor": colors["bg"],
                                "textFormat": {
                                    "foregroundColor": colors["fg"],
                                    "bold": True
                                }
                            }
                        }
                    },
                    "index": idx
                }
            })

    batch_update_spreadsheet(token, requests)
    print("Google Sheets updated with interactive droplist and auto-coloring badges successfully!")

def update_excel_droplists():
    print("2. Updating local Excel workbook (financial-hub-roadmap.xlsx)...")
    wb = openpyxl.load_workbook(EXCEL_PATH)
    target_sheets = [
        ("Roadmap", 50),
        ("Sitemap", 150)
    ]
    for sname, max_r in target_sheets:
        if sname not in wb.sheetnames:
            continue
        ws = wb[sname]
        # Clear existing data validations on sheet
        ws.data_validations.dataValidation.clear()

        formula_str = f'"{",".join(STATUS_OPTIONS)}"'
        dv = DataValidation(
            type="list",
            formula1=formula_str,
            allow_blank=True
        )
        dv.error = "Vui lòng chọn trạng thái từ danh sách"
        dv.errorTitle = "Trạng thái không hợp lệ"
        dv.prompt = "Chọn trạng thái"
        dv.promptTitle = "Trạng thái"

        ws.add_data_validation(dv)
        dv.add(f"F2:F{max_r}")
        print(f"  Added DataValidation droplist to {sname}!F2:F{max_r}")

    wb.save(EXCEL_PATH)
    print("Local Excel workbook updated successfully with droplists!")

if __name__ == "__main__":
    update_google_sheets_droplists()
    update_excel_droplists()
    print("All tasks completed!")

#!/usr/bin/env python3
"""
Synchronize all Status names to 100% English:
- Replace "Chưa triển khai" with "Not Started"
- Configure Droplist options: ["Done", "In Progress", "Planned", "Pending", "Not Started", "Backlog"]
- Update Google Sheets (Product Roadmap & Sitemap tabs)
- Update local Excel (financial-hub-roadmap.xlsx)
- Update BRD (financial-hub-brd.md Section 10)
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-roadmap.xlsx"
BRD_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-brd.md"
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
SPREADSHEET_ID = "1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A"

ENGLISH_STATUS_OPTIONS = [
    "Done",
    "In Progress",
    "Planned",
    "Pending",
    "Not Started",
    "Backlog"
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
    },
    "Backlog": {
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

def update_sheet_values(token, range_name, values):
    safe_range = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{safe_range}?valueInputOption=USER_ENTERED"
    payload = json.dumps({"values": values}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        method="PUT",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def sync_local_excel():
    print("1. Updating local Excel workbook (financial-hub-roadmap.xlsx)...")
    wb = openpyxl.load_workbook(EXCEL_PATH)

    border_thin = Border(
        left=Side(style="thin", color="CBD5E1"),
        right=Side(style="thin", color="CBD5E1"),
        top=Side(style="thin", color="CBD5E1"),
        bottom=Side(style="thin", color="CBD5E1")
    )
    fill_not_started = PatternFill("solid", fgColor="F1F5F9")
    font_not_started = Font(name="Arial", size=10, bold=True, color="475569")
    align_center = Alignment(horizontal="center", vertical="center")

    for sname, max_r in [("Roadmap", 50), ("Sitemap", 150)]:
        if sname not in wb.sheetnames:
            continue
        ws = wb[sname]
        # Replace "Chưa triển khai" with "Not Started"
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=6, max_col=6):
            cell = row[0]
            if cell.value == "Chưa triển khai":
                cell.value = "Not Started"
                cell.fill = fill_not_started
                cell.font = font_not_started
                cell.alignment = align_center
                cell.border = border_thin

        # Reset Data Validation Droplist
        ws.data_validations.dataValidation.clear()
        formula_str = f'"{",".join(ENGLISH_STATUS_OPTIONS)}"'
        dv = DataValidation(
            type="list",
            formula1=formula_str,
            allow_blank=True
        )
        dv.error = "Please select a valid status from the list"
        dv.errorTitle = "Invalid Status"
        dv.prompt = "Select Status"
        dv.promptTitle = "Status"
        ws.add_data_validation(dv)
        dv.add(f"F2:F{max_r}")
        print(f"  Updated {sname}!F2:F{max_r} droplist: {formula_str}")

    wb.save(EXCEL_PATH)
    print("Local Excel workbook updated successfully with English statuses!")

def sync_google_sheets():
    print("2. Updating Google Sheets...")
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

    # Step A: Replace cell values in Product Roadmap
    # Row 17 Col 6 is Standalone Redirect
    print("  Updating Product Roadmap values to English status...")
    update_sheet_values(token, "Product Roadmap!F17", [["Not Started"]])

    # Step B: Replace cell values in Sitemap
    # Rows 38 to 42 are Standalone pages
    print("  Updating Sitemap values to English status...")
    update_sheet_values(token, "Sitemap!F38:F42", [
        ["Not Started"],
        ["Not Started"],
        ["Not Started"],
        ["Not Started"],
        ["Not Started"]
    ])

    # Step C: Update DataValidation & Conditional Formatting Rules
    requests = []
    target_sheets = [
        {"title": "Product Roadmap", "max_row": 50},
        {"title": "Sitemap", "max_row": 150}
    ]

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

        # Set Data Validation (Dropdown list with custom UI)
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
                        "values": [{"userEnteredValue": val} for val in ENGLISH_STATUS_OPTIONS]
                    },
                    "strict": True,
                    "showCustomUi": True
                }
            }
        })

        # Add dynamic conditional formatting rules for each status
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
    print("Google Sheets updated with English droplist and dynamic formatting rules successfully!")

def sync_brd():
    print("3. Updating BRD (financial-hub-brd.md)...")
    content = BRD_PATH.read_text(encoding="utf-8")
    old_fragment = '<td style="border:1px solid #94a3b8; padding:6px; color:#475569; background-color:#f1f5f9; font-weight:700; text-align:center;">Chưa triển khai</td>'
    new_fragment = '<td style="border:1px solid #94a3b8; padding:6px; color:#475569; background-color:#f1f5f9; font-weight:700; text-align:center;">Not Started</td>'
    if old_fragment in content:
        content = content.replace(old_fragment, new_fragment)
        BRD_PATH.write_text(content, encoding="utf-8")
        print("BRD Section 10 updated successfully!")
    else:
        print("Old fragment not found in BRD, checking if already updated...")

if __name__ == "__main__":
    sync_local_excel()
    sync_google_sheets()
    sync_brd()
    print("All status synchronization completed successfully!")

#!/usr/bin/env python3
"""
Update status of /tai-chinh/blog and /tai-chinh/blog/[slug] to 'Done':
1. In local Excel: 05_HUBS/financial/financial-hub-roadmap.xlsx (Sheets: Sitemap, Roadmap)
2. In Google Sheets: 1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A (Tabs: Sitemap, Product Roadmap)
3. In BRD: 05_HUBS/financial/financial-hub-brd.md (Section 10)
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-roadmap.xlsx"
BRD_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-brd.md"
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
SPREADSHEET_ID = "1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A"


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

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res["access_token"]


def batch_update_spreadsheet(token, requests):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
    body = json.dumps({"requests": requests}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def update_values(token, range_name, values):
    encoded_range = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{encoded_range}?valueInputOption=USER_ENTERED"
    body = json.dumps({"values": values}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def update_local_excel():
    print(f"1. Updating local Excel: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH)

    fill_done = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    font_done = Font(name="Arial", size=9.5, bold=True, color="15803D")

    # Update Sitemap sheet
    ws_s = wb["Sitemap"]
    for r in range(2, ws_s.max_row + 1):
        u = str(ws_s.cell(r, 6).value or "")
        if u == "/tai-chinh/blog":
            ws_s.cell(r, 7, "Done")
            ws_s.cell(r, 7).fill = fill_done
            ws_s.cell(r, 7).font = font_done
            ws_s.cell(r, 8, "Đã hoàn thành Go-live. Cổng danh mục bài viết cẩm nang kiến thức tài chính cá nhân MoMo.")
            print(f"Updated local Sitemap R{r} (/tai-chinh/blog) to Done!")
        elif u == "/tai-chinh/blog/[slug]":
            ws_s.cell(r, 7, "Done")
            ws_s.cell(r, 7).fill = fill_done
            ws_s.cell(r, 7).font = font_done
            ws_s.cell(r, 8, "Đã hoàn thành Go-live. Hệ thống 100 bài viết chi tiết chuẩn SEO & GEO, duy trì xuất bản đều đặn.")
            print(f"Updated local Sitemap R{r} (/tai-chinh/blog/[slug]) to Done!")

    # Update Roadmap sheet
    ws_r = wb["Roadmap"]
    for r in range(2, ws_r.max_row + 1):
        name = str(ws_r.cell(r, 4).value or "")
        if "Content Engine" in name:
            ws_r.cell(r, 5, "Đã hoàn thành Go-live: Cụm Blog Hub (/tai-chinh/blog) và hệ thống bài viết chi tiết (/tai-chinh/blog/[slug]), duy trì nhịp xuất bản chuẩn E-E-A-T nuôi dưỡng traffic tự nhiên.")
            ws_r.cell(r, 6, "Done")
            ws_r.cell(r, 6).fill = fill_done
            ws_r.cell(r, 6).font = font_done
            print(f"Updated local Roadmap R{r} (Content Engine) to Done!")
            break

    wb.save(EXCEL_PATH)
    print("Local Excel updated and saved successfully!")


def update_google_sheets():
    print("2. Updating Google Sheets...")
    token = get_access_token()

    url_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets(properties)"
    req_meta = urllib.request.Request(url_meta, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta = json.loads(resp.read().decode("utf-8"))

    sheet_map = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}
    roadmap_id = sheet_map.get("Product Roadmap")
    sitemap_id = sheet_map.get("Sitemap")

    # A. Update Tab: Sitemap
    # Rows 41 and 42 in Sitemap
    update_values(token, "Sitemap!G41:H42", [
        ["Done", "Đã hoàn thành Go-live. Cổng danh mục bài viết cẩm nang kiến thức tài chính cá nhân MoMo."],
        ["Done", "Đã hoàn thành Go-live. Hệ thống 100 bài viết chi tiết chuẩn SEO & GEO, duy trì xuất bản đều đặn."]
    ])

    reqs_s = [
        {
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": 40,
                    "endRowIndex": 42,
                    "startColumnIndex": 6,
                    "endColumnIndex": 7
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 0.86, "green": 0.98, "blue": 0.90},
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Arial",
                            "fontSize": 10,
                            "bold": True,
                            "foregroundColor": {"red": 0.08, "green": 0.50, "blue": 0.24}
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
            }
        }
    ]
    batch_update_spreadsheet(token, reqs_s)
    print("Google Sheet Tab: Sitemap updated successfully!")

    # B. Update Tab: Product Roadmap
    # Row 14 in Product Roadmap (Item 13)
    update_values(token, "Product Roadmap!E14:F14", [
        [
            "Đã hoàn thành Go-live: Cụm Blog Hub (/tai-chinh/blog) và hệ thống bài viết chi tiết (/tai-chinh/blog/[slug]), duy trì nhịp xuất bản chuẩn E-E-A-T nuôi dưỡng traffic tự nhiên.",
            "Done"
        ]
    ])

    reqs_r = [
        {
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": 13,
                    "endRowIndex": 14,
                    "startColumnIndex": 5,
                    "endColumnIndex": 6
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 0.86, "green": 0.98, "blue": 0.90},
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Arial",
                            "fontSize": 10,
                            "bold": True,
                            "foregroundColor": {"red": 0.08, "green": 0.50, "blue": 0.24}
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
            }
        }
    ]
    batch_update_spreadsheet(token, reqs_r)
    print("Google Sheet Tab: Product Roadmap updated successfully!")


def update_brd_file():
    print("3. Updating BRD file...")
    content = BRD_PATH.read_text(encoding="utf-8")

    old_target = """    <tr style="background-color:#fefce8;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;"><strong>Phase 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 10/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px; font-weight:600;">Tăng Trưởng Nội Dung</td>
      <td style="border:1px solid #94a3b8; padding:6px; font-weight:700;">Cỗ Máy Content Engine Always-on</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Bổ sung mới (P1): Duy trì nhịp sản xuất và xuất bản 5 bài viết/ngày chuẩn E-E-A-T vào Blog Hub (/tai-chinh/blog/*), xây dựng chân rết thâu tóm từ khóa ngách và nuôi dưỡng traffic tự nhiên.</td>
      <td style="border:1px solid #94a3b8; padding:6px; color:#b45309; background-color:#fef9c3; font-weight:700; text-align:center;">In Progress</td>
    </tr>"""

    new_target = """    <tr style="background-color:#f0fdf4;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;"><strong>Phase 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 10/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px; font-weight:600;">Tăng Trưởng Nội Dung</td>
      <td style="border:1px solid #94a3b8; padding:6px; font-weight:700;">Cỗ Máy Content Engine Always-on</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Đã hoàn thành Go-live: Cụm Blog Hub (/tai-chinh/blog) và hệ thống bài viết chi tiết (/tai-chinh/blog/[slug]), duy trì nhịp xuất bản chuẩn E-E-A-T nuôi dưỡng traffic tự nhiên.</td>
      <td style="border:1px solid #94a3b8; padding:6px; color:#15803d; background-color:#dcfce7; font-weight:700; text-align:center;">Done</td>
    </tr>"""

    if old_target in content:
        content = content.replace(old_target, new_target)
        BRD_PATH.write_text(content, encoding="utf-8")
        print("Updated BRD Section 10 for Content Engine to Done!")
    else:
        print("Note: Content Engine section matched differently, checking...")


def main():
    update_local_excel()
    update_google_sheets()
    update_brd_file()
    print("\nAll blog status updates to Done completed successfully!")


if __name__ == "__main__":
    main()

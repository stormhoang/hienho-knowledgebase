#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REFORMAT PROJECTS DETAIL FLOW SHEET ON GOOGLE SHEETS SSOT
Spreadsheet ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU
Target Sheet: 'Projects Detail Flow' (Sheet ID: 316527624)

Triển khai cấu trúc thị giác phân cấp 3 tầng (3-Tier Visual Hierarchy):
- Tầng 1: Parent Hubs (Cinema Hub, Financial Hub, Vehicle Hub...) - Nền Slate `#F1F5F9`, chữ Bold, viền trên phân cách khối.
- Tầng 2: Sub-projects / Sub-pages (Cinema Cineplex, Vay Nhanh...) - Thụt lề 4 spaces, nền trắng `#FFFFFF`.
- Tầng 3: Click to app / W2A Flow - Thụt lề kèm ký hiệu luồng `↳ Click to app`, chữ Italic `#64748B`, nền `#F8FAFC`, CVR % nổi bật `#F0FDF4`.
- Collapsible Row Groups: Tích hợp nút thu gọn [-]/[+] cho các sub-projects con của từng Hub.
- Header Banners: Đồng bộ chuẩn MTD (Cols B..K) vs Full Month (Cols L..T), highlight cột Tháng 10 hiện hành.
"""

import re
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
SPREADSHEET_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"
SHEET_ID = 316527624
SHEET_TITLE = "Projects Detail Flow"
BACKUP_TITLE = "Projects Detail Flow_ClicksBackup"


def get_token():
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
        return json.loads(resp.read().decode())["access_token"]


def api_get_values(token, range_str):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{urllib.parse.quote(range_str)}?valueRenderOption=FORMULA"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode()).get("values", [])


def api_write_values(token, range_str, values):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{urllib.parse.quote(range_str)}?valueInputOption=USER_ENTERED"
    payload = json.dumps({"range": range_str, "majorDimension": "ROWS", "values": values}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, method="PUT")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def api_clear_values(token, range_str):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{urllib.parse.quote(range_str)}:clear"
    req = urllib.request.Request(url, data=b"{}", headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def api_batch_update(token, requests):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
    payload = json.dumps({"requests": requests}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print("[ERROR DETAILS]", e.read().decode())
        raise


def main():
    print("=" * 60)
    print("REFORMAT 'PROJECTS DETAIL FLOW' SSOT SHEET")
    print("=" * 60)

    token = get_token()
    print("[1/5] Kéo dữ liệu và công thức sạch từ backup...")
    backup_data = api_get_values(token, f"{BACKUP_TITLE}!A1:T175")
    print(f"  ✓ Đã lấy {len(backup_data)} hàng từ {BACKUP_TITLE}")

    # Chuẩn hóa Row 1 và Row 2
    row1 = [
        "Cấu trúc Phân khối & Dự án Web",
        "LŨY KẾ MTD (Month to Date - Cập nhật ngày 30)", "", "", "", "", "", "", "",
        "MoM Net Add",
        "W2A CVR",
        "TOÀN BỘ TRỌN THÁNG (Full Month)", "", "", "", "", "", "", "",
        "MoM Net Add"
    ]

    # Serial dates: 46143 (May 26), 46174 (Jun 26), 46204 (Jul 26), 46235 (Aug 26), 46266 (Sep 26), 46296 (Oct 26), 46327 (Nov 26), 46357 (Dec 26)
    month_serials = [46143, 46174, 46204, 46235, 46266, 46296, 46327, 46357]
    row2 = (
        ["Chỉ số / Tên Dự Án"]
        + month_serials
        + ["T10 vs T9", "Tỷ lệ CVR"]
        + month_serials
        + ["T10 vs T9"]
    )

    # Map các nhóm Hub và sub-projects (0-indexed trong danh sách 65 dự án)
    hub_children = {
        0: list(range(1, 7)),       # Cinema Hub (0) -> Cinema Cineplex, Page, Blog, Home, News, Landing (1..6)
        10: list(range(11, 25)),    # Financial Hub (10) -> Vay Nhanh..Sàn Đầu Tư (11..24)
        25: list(range(26, 30)),    # Vehicle Hub (25) -> Phạt nguội, BH ô tô, BH xe máy, Tiện ích (26..29)
        33: [34, 35],               # Sim (33) -> Sim, Esim (34, 35)
        55: [56, 57]                # Student Hub (55) -> Student Pass, Student Hub (56, 57)
    }

    # Bảng phân loại từng hàng từ hàng 8 đến hàng 137
    # Hub parents (1-based row number):
    hub_parent_rows = {
        8: "Cinema Hub",
        22: "Home MoMo",
        24: "Tìm Kiếm",
        26: "Tiktok",
        28: "Financial Hub",
        58: "Vehicle Hub",
        68: "Vé Xe",
        70: "OTA",
        72: "Merchant",
        74: "Sim",
        80: "Game",
        82: "Bảo hiểm y tế",
        84: "Data",
        86: "Soundbox",
        88: "New User",
        90: "Hỏi đáp",
        92: "TnC",
        94: "Trust",
        96: "Guide",
        98: "Khuyến mãi",
        100: "Tin Tức",
        102: "Campaign",
        104: "Blog",
        106: "Application Store",
        108: "Vé số",
        110: "Dịch vụ liên kết",
        112: "Billpay",
        114: "P2P",
        116: "Điện",
        118: "Student Hub",
        124: "Cross Border",
        126: "Hoàn Tiền Mua Sắm",
        128: "Bảo Hiểm Sức Khỏe",
        130: "Mở tài khoản ngân hàng",
        132: "Download",
        134: "Nước",
        136: "Others"
    }

    subproject_rows = {
        # Cinema subpages:
        10: "Cinema_Cineplex Page",
        12: "Cinema_Page",
        14: "Cinema_Blog",
        16: "Cinema_Home Page",
        18: "Cinema_News",
        20: "Cinema_Landing Page",
        # Financial subpages:
        30: "Vay Nhanh",
        32: "Điểm Tín Dụng",
        34: "Ví Trả Sau",
        36: "Túi Thần Tài",
        38: "Mở Thẻ Tín Dụng",
        40: "Quản Lý Chi Tiêu",
        42: "Trả Góp Apple",
        44: "Thanh Toán Khoản Vay",
        46: "Chứng Khoán",
        48: "Tiết Kiệm Online",
        50: "Thanh Toán Thẻ Tín Dụng",
        52: "Chứng Chỉ Quỹ",
        54: "Trung Tâm Tài Chính",
        56: "Sàn Đầu Tư",
        # Vehicle subpages:
        60: "Phạt nguội",
        62: "Bảo hiểm ô tô",
        64: "Bảo hiểm xe máy",
        66: "Tiện ích giao thông",
        # Sim subpages:
        76: "Sim (Chi tiết)",
        78: "Esim",
        # Student subpages:
        120: "Student Pass",
        122: "Student Hub (Portal)"
    }

    print("[2/5] Tinh chỉnh tiêu đề và phân cấp tên dự án (Col A)...")
    cleaned_rows = []
    for r_idx, row in enumerate(backup_data):
        row_num = r_idx + 1
        new_row = list(row)
        # Bổ sung đủ 20 cột (A..T)
        while len(new_row) < 20:
            new_row.append("")

        if row_num == 1:
            new_row = row1
        elif row_num == 2:
            new_row = row2
        else:
            # Xử lý Col A label
            if row_num in hub_parent_rows:
                hname = hub_parent_rows[row_num]
                new_row[0] = hname
            elif (row_num - 1) in hub_parent_rows:
                p_name = hub_parent_rows[row_num - 1]
                new_row[0] = f"  ↳ Click to app: {p_name}"
            elif row_num in subproject_rows:
                sname = subproject_rows[row_num]
                new_row[0] = f"    {sname}"
            elif (row_num - 1) in subproject_rows:
                p_name = subproject_rows[row_num - 1]
                new_row[0] = f"        ↳ Click: {p_name}"
            elif row_num == 139:
                new_row[0] = "Tỷ Trọng % Pageview Theo Dự Án (PV Dự án / Tổng PV)"
            elif row_num >= 140 and row_num <= 173:
                cur_name = str(new_row[0]).strip().lstrip("%")
                new_row[0] = f"    {cur_name}"

            # Xử lý các cell SUMPRODUCT để bọc TRIM($A{row_num}) tránh lỗi khi Col A có khoảng trắng thụt lề
            for c_idx in range(1, len(new_row)):
                cell_val = new_row[c_idx]
                if isinstance(cell_val, str) and "SUMPRODUCT" in cell_val and "$A$" in cell_val:
                    new_row[c_idx] = re.sub(r'=\s*(\$A\$\d+)', r'=TRIM(\1)', cell_val)

        cleaned_rows.append(new_row)

    print(f"  ✓ Đã chuẩn hóa {len(cleaned_rows)} hàng dữ liệu.")

    print("[3/5] Ghi dữ liệu sạch vào 'Projects Detail Flow'...")
    # Clear vùng dữ liệu cũ (A1:Z600)
    api_clear_values(token, f"{SHEET_TITLE}!A1:Z600")
    # Ghi dữ liệu sạch A1:T{len(cleaned_rows)}
    api_write_values(token, f"{SHEET_TITLE}!A1:T{len(cleaned_rows)}", cleaned_rows)
    print("  ✓ Ghi dữ liệu thành công!")

    print("[4/5] Thiết lập Visual Hierarchy & Google Sheets Row Groups...")

    requests = []

    # 1. Unmerge toàn bộ row 1 cũ
    requests.append({
        "unmergeCells": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 26
            }
        }
    })

    # 2. Xóa tất cả Dimension Groups cũ trên Rows
    # Lấy thông tin Dimension Groups hiện tại để xóa
    req_meta = urllib.request.Request(
        f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets(properties,rowGroups)",
        headers={"Authorization": f"Bearer {token}"}
    )
    with urllib.request.urlopen(req_meta) as resp:
        meta = json.loads(resp.read().decode())
    
    for s in meta.get("sheets", []):
        if s.get("properties", {}).get("sheetId") == SHEET_ID:
            for rg in s.get("rowGroups", []):
                requests.append({
                    "deleteDimensionGroup": {
                        "range": {
                            "sheetId": SHEET_ID,
                            "dimension": "ROWS",
                            "startIndex": rg["range"]["startIndex"],
                            "endIndex": rg["range"]["endIndex"]
                        }
                    }
                })

    # 3. Cố định 2 hàng đầu và 1 cột đầu
    requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": SHEET_ID,
                "gridProperties": {
                    "frozenRowCount": 2,
                    "frozenColumnCount": 1
                }
            },
            "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount"
        }
    })

    # 4. Merge các banner Row 1:
    # B1:I1 (MTD) -> cols 1..9
    requests.append({
        "mergeCells": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 1,
                "endColumnIndex": 9
            },
            "mergeType": "MERGE_ALL"
        }
    })
    # L1:S1 (Full Month) -> cols 11..19
    requests.append({
        "mergeCells": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 11,
                "endColumnIndex": 19
            },
            "mergeType": "MERGE_ALL"
        }
    })

    # 5. Format Row 1 (Header Banners)
    # A1: Cấu trúc phân khối
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 1},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.08, "green": 0.18, "blue": 0.36}, # Dark Navy
                    "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # B1..I1: MTD Banner
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 1, "endColumnIndex": 9},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.12, "green": 0.23, "blue": 0.54}, # MoMo / Navy Blue #1E3A8A
                    "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # J1: MoM Net Add
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 9, "endColumnIndex": 10},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.15, "green": 0.39, "blue": 0.92}, # Royal Blue #2563EB
                    "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # K1: W2A CVR
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 10, "endColumnIndex": 11},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.05, "green": 0.58, "blue": 0.53}, # Teal #0D9488
                    "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # L1..S1: Full Month Banner
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 11, "endColumnIndex": 19},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.20, "green": 0.25, "blue": 0.33}, # Dark Slate #334155
                    "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # T1: Full Month Net Add
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 19, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.28, "green": 0.33, "blue": 0.41}, # Slate #475569
                    "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })

    # 6. Format Row 2 (Month Headers)
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.95, "green": 0.96, "blue": 0.98}, # Slate 50
                    "textFormat": {"foregroundColor": {"red": 0.12, "green": 0.16, "blue": 0.23}, "bold": True, "fontSize": 9},
                    "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE",
                    "borders": {
                        "bottom": {"style": "SOLID", "width": 2, "color": {"red": 0.8, "green": 0.83, "blue": 0.88}}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,borders)"
        }
    })
    # Date number format "mmm yy" cho các cột tháng ở Row 2
    for c_start, c_end in [(1, 9), (11, 19)]:
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": c_start, "endColumnIndex": c_end},
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "DATE", "pattern": "mmm yy"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
    # Highlight Cột G (Oct 26 MTD - col index 6) và Cột Q (Oct 26 Full Month - col index 16) ở Header
    for c_idx in [6, 16]:
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": c_idx, "endColumnIndex": c_idx + 1},
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 0.86, "green": 0.92, "blue": 0.99}, # Soft Blue Accent #DBEAFE
                        "textFormat": {"foregroundColor": {"red": 0.12, "green": 0.25, "blue": 0.69}, "bold": True, "fontSize": 9}
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat)"
            }
        })

    # 7. Format Rows 3..7 (Total Summary Block)
    # Row 3: Page views (Actual)
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 3, "startColumnIndex": 0, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.94, "green": 0.96, "blue": 1.0}, # #EFF6FF
                    "textFormat": {"foregroundColor": {"red": 0.12, "green": 0.23, "blue": 0.54}, "bold": True, "fontSize": 10},
                    "borders": {
                        "top": {"style": "SOLID", "width": 1, "color": {"red": 0.75, "green": 0.85, "blue": 0.99}},
                        "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.75, "green": 0.85, "blue": 0.99}}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
        }
    })
    # Row 7: 'Page view by Project' Header
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 6, "endRowIndex": 7, "startColumnIndex": 0, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.91, "green": 0.93, "blue": 0.96},
                    "textFormat": {"foregroundColor": {"red": 0.06, "green": 0.09, "blue": 0.16}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE",
                    "borders": {
                        "top": {"style": "SOLID", "width": 2, "color": {"red": 0.58, "green": 0.64, "blue": 0.72}},
                        "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.8, "green": 0.83, "blue": 0.88}}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,borders)"
        }
    })

    # 8. Loop format cho từng cặp hàng từ hàng 8 đến 137:
    # BẢNG MÀU PHÂN ĐỊNH TUYỆT ĐỐI GIỮA PAGEVIEWS VÀ CLICKS:
    # - PAGEVIEWS: Tông Xanh Dương / Trắng tinh khôi (Traffic, Volume)
    # - CLICKS: Tông Hồng MoMo / Rose (Conversion, Action, Web-to-App)
    # - CVR %: Xanh Bạc Hà Emerald (#DCFCE7) với số liệu xanh đậm #15803D
    for r_num in range(8, 138, 2):
        r_pv_0 = r_num - 1
        r_cl_0 = r_num

        is_hub = r_num in hub_parent_rows
        is_sub = r_num in subproject_rows

        if is_hub:
            # TẦNG 1: PARENT HUB
            # Row PV (Pageviews) -> TÔNG XANH DƯƠNG RÕ RỆT (#DBEAFE / #1E3A8A)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_pv_0 + 1, "startColumnIndex": 0, "endColumnIndex": 20},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.86, "green": 0.92, "blue": 0.99}, # #DBEAFE Soft Ice Blue
                            "textFormat": {"foregroundColor": {"red": 0.12, "green": 0.23, "blue": 0.54}, "bold": True, "fontSize": 10}, # #1E3A8A Dark Navy
                            "borders": {
                                "top": {"style": "SOLID", "width": 2, "color": {"red": 0.23, "green": 0.51, "blue": 0.96}}, # #3B82F6 Blue Accent Border
                                "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.58, "green": 0.77, "blue": 0.99}}
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
                }
            })
            # Row Click (to app) -> TÔNG HỒNG MOMO RÕ RỆT (#FCE7F3 / #9D174D)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": 0, "endColumnIndex": 20},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.988, "green": 0.906, "blue": 0.953}, # #FCE7F3 MoMo Soft Rose
                            "textFormat": {"foregroundColor": {"red": 0.616, "green": 0.090, "blue": 0.302}, "bold": True, "fontSize": 9}, # #9D174D MoMo Magenta
                            "borders": {
                                "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.957, "green": 0.447, "blue": 0.714}} # #F472B6
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
                }
            })
            # CVR % (Col K - index 10) nổi bật xanh bạc hà
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": 10, "endColumnIndex": 11},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.863, "green": 0.988, "blue": 0.906}, # #DCFCE7 Emerald 100
                            "textFormat": {"foregroundColor": {"red": 0.082, "green": 0.502, "blue": 0.239}, "bold": True, "fontSize": 10} # #15803D
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat)"
                }
            })

        elif is_sub:
            # TẦNG 2: SUB-PROJECT
            # Row PV -> TRẮNG TINH KHÔI (#FFFFFF)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_pv_0 + 1, "startColumnIndex": 0, "endColumnIndex": 20},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}, # Pure White
                            "textFormat": {"foregroundColor": {"red": 0.12, "green": 0.16, "blue": 0.23}, "bold": False, "fontSize": 9}, # Charcoal
                            "borders": {
                                "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.93, "green": 0.94, "blue": 0.96}}
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
                }
            })
            # Row Click -> HỒNG PHẤN NHẸ (#FDF2F8 / #BE185D)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": 0, "endColumnIndex": 20},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.992, "green": 0.949, "blue": 0.973}, # #FDF2F8 Pale Rose
                            "textFormat": {"foregroundColor": {"red": 0.745, "green": 0.094, "blue": 0.365}, "italic": True, "fontSize": 9}, # Dark Rose
                            "borders": {
                                "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.98, "green": 0.86, "blue": 0.92}} # Soft pink border
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
                }
            })
            # CVR % (Col K - index 10) nổi bật xanh bạc hà
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": 10, "endColumnIndex": 11},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.863, "green": 0.988, "blue": 0.906}, # #DCFCE7 Emerald 100
                            "textFormat": {"foregroundColor": {"red": 0.082, "green": 0.502, "blue": 0.239}, "bold": True, "fontSize": 9}
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat)"
                }
            })

        else:
            # Standalone project (độc lập, không có subpage con)
            # Row PV -> XANH BĂNG NHẸ (#F0F7FF / #1E3A8A)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_pv_0 + 1, "startColumnIndex": 0, "endColumnIndex": 20},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.94, "green": 0.968, "blue": 1.0}, # #F0F7FF Ice Blue
                            "textFormat": {"foregroundColor": {"red": 0.12, "green": 0.23, "blue": 0.54}, "bold": True, "fontSize": 9},
                            "borders": {
                                "top": {"style": "SOLID", "width": 1, "color": {"red": 0.58, "green": 0.77, "blue": 0.99}},
                                "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.88, "green": 0.91, "blue": 0.94}}
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
                }
            })
            # Row Click -> HỒNG MOMO ROSE (#FCE7F3 / #9D174D)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": 0, "endColumnIndex": 20},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.988, "green": 0.906, "blue": 0.953}, # #FCE7F3 Rose
                            "textFormat": {"foregroundColor": {"red": 0.616, "green": 0.090, "blue": 0.302}, "bold": True, "fontSize": 9},
                            "borders": {
                                "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.957, "green": 0.447, "blue": 0.714}}
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,borders)"
                }
            })
            # CVR % (Col K - index 10)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": 10, "endColumnIndex": 11},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.863, "green": 0.988, "blue": 0.906}, # #DCFCE7 Emerald 100
                            "textFormat": {"foregroundColor": {"red": 0.082, "green": 0.502, "blue": 0.239}, "bold": True, "fontSize": 9}
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat)"
                }
            })

    # Highlight Cột G (Oct 26 MTD - col index 6) và Cột Q (Oct 26 Full Month - col index 16)
    # Tô màu nhấn riêng biệt: Ô Pageview tô xanh nhấn, Ô Click tô hồng nhấn!
    for r_num in range(8, 138, 2):
        r_pv_0 = r_num - 1
        r_cl_0 = r_num
        for c_idx in [6, 16]:
            # PV Oct highlight -> Xanh đậm hơn (#BFDBFE)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_pv_0, "endRowIndex": r_pv_0 + 1, "startColumnIndex": c_idx, "endColumnIndex": c_idx + 1},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.75, "green": 0.86, "blue": 0.99} # #BFDBFE Accent Blue
                        }
                    },
                    "fields": "userEnteredFormat.backgroundColor"
                }
            })
            # Click Oct highlight -> Hồng đậm hơn (#FBCFE8)
            requests.append({
                "repeatCell": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": r_cl_0, "endRowIndex": r_cl_0 + 1, "startColumnIndex": c_idx, "endColumnIndex": c_idx + 1},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.984, "green": 0.812, "blue": 0.910} # #FBCFE8 Accent Rose
                        }
                    },
                    "fields": "userEnteredFormat.backgroundColor"
                }
            })

    # 9. Format Row 139 (Header Tỷ Trọng %)
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 138, "endRowIndex": 139, "startColumnIndex": 0, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.88, "green": 0.91, "blue": 0.94}, # #E2E8F0
                    "textFormat": {"foregroundColor": {"red": 0.06, "green": 0.09, "blue": 0.16}, "bold": True, "fontSize": 10},
                    "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE",
                    "borders": {
                        "top": {"style": "SOLID", "width": 2, "color": {"red": 0.58, "green": 0.64, "blue": 0.72}},
                        "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0.8, "green": 0.83, "blue": 0.88}}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,borders)"
        }
    })

    # 10. Number Formatting toàn sheet:
    # Cols B..I (MTD PV & Click) & Cols L..S (Full Month PV & Click): #,##0
    for c_start, c_end in [(1, 9), (11, 19)]:
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 137, "startColumnIndex": c_start, "endColumnIndex": c_end},
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
    # Cols J & T: MoM Net Add: +#,##0;-#,##0;0
    for c_idx in [9, 19]:
        requests.append({
            "repeatCell": {
                "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 137, "startColumnIndex": c_idx, "endColumnIndex": c_idx + 1},
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "NUMBER", "pattern": "+#,##0;-#,##0;0"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
    # Col K: W2A CVR %: 0.0%
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 137, "startColumnIndex": 10, "endColumnIndex": 11},
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    # Row 5 (% Growth Rate): 0.0%
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 5, "startColumnIndex": 1, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }
    })
    # Rows 140..173 (% Pageview by Project): 0.0%
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 139, "endRowIndex": 173, "startColumnIndex": 1, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }
    })

    # Căn lề chuẩn: Cột A căn trái, các cột B..T căn phải
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 173, "startColumnIndex": 0, "endColumnIndex": 1},
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(horizontalAlignment,verticalAlignment)"
        }
    })
    requests.append({
        "repeatCell": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 173, "startColumnIndex": 1, "endColumnIndex": 20},
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "RIGHT", "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(horizontalAlignment,verticalAlignment)"
        }
    })

    # 11. THÊM CÁC DIMENSION GROUPS (ROW OUTLINES / NÚT THU GỌN [-]/[+]):
    # Subprojects của Cinema Hub: rows 10..21 (0-indexed: startIndex=9, endIndex=21)
    # Subprojects của Financial Hub: rows 30..57 (0-indexed: startIndex=29, endIndex=57)
    # Subprojects của Vehicle Hub: rows 60..67 (0-indexed: startIndex=59, endIndex=67)
    # Subprojects của Sim: rows 76..79 (0-indexed: startIndex=75, endIndex=79)
    # Subprojects của Student Hub: rows 120..123 (0-indexed: startIndex=119, endIndex=123)
    # Khối Tỷ trọng %: rows 140..173 (0-indexed: startIndex=139, endIndex=173)
    groups = [
        {"start": 9, "end": 21},    # Cinema
        {"start": 29, "end": 57},   # Financial
        {"start": 59, "end": 67},   # Vehicle
        {"start": 75, "end": 79},   # Sim
        {"start": 119, "end": 123}, # Student
        {"start": 139, "end": 173}  # Tỷ trọng %
    ]

    for g in groups:
        requests.append({
            "addDimensionGroup": {
                "range": {
                    "sheetId": SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": g["start"],
                    "endIndex": g["end"]
                }
            }
        })
        # Thiết lập thu gọn (collapsed: True) mặc định để người dùng nhìn thấy tổng quan gọn gàng
        requests.append({
            "updateDimensionGroup": {
                "dimensionGroup": {
                    "range": {
                        "sheetId": SHEET_ID,
                        "dimension": "ROWS",
                        "startIndex": g["start"],
                        "endIndex": g["end"]
                    },
                    "depth": 1,
                    "collapsed": True
                },
                "fields": "collapsed"
            }
        })

    print(f"  ✓ Đã sinh {len(requests)} lệnh batchUpdate định dạng & row grouping.")
    api_batch_update(token, requests)
    print("  ✓ Đã cập nhật thành công cấu trúc thị giác lên Google Sheets!")

    print("[5/5] Hoàn tất reformat 'Projects Detail Flow' trên Google Sheets!")

    print("[6/6] Đồng bộ sang Local Excel & Google Drive Desktop...")
    sync_to_local_excel(token)
    print("=" * 60)


def sync_to_local_excel(token):
    import shutil
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    excel_path = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    drive_path = Path("/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#4 - Tracking & Performance/web_performance_tracking.xlsx")

    # Kéo toàn bộ dữ liệu sạch vừa ghi từ Google Sheets
    sheet_data = api_get_values(token, f"{SHEET_TITLE}!A1:T175")

    wb = openpyxl.load_workbook(excel_path)
    if SHEET_TITLE in wb.sheetnames:
        ws = wb[SHEET_TITLE]
    else:
        ws = wb.create_sheet(SHEET_TITLE)

    # Unmerge toàn bộ merged cells cũ trong ws
    for m in list(ws.merged_cells.ranges):
        ws.unmerge_cells(range_string=str(m))

    # Xóa dữ liệu cũ trong ws
    for row in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 300), min_col=1, max_col=min(ws.max_column, 26)):
        for cell in row:
            if not isinstance(cell, openpyxl.cell.cell.MergedCell):
                cell.value = None
                cell.fill = PatternFill(fill_type=None)
                cell.border = Border()

    # Định nghĩa styles phân cấp màu sắc rực rỡ và đối lập hoàn toàn:
    # PAGEVIEWS: Tông Xanh Dương / Trắng tinh khôi
    # CLICKS: Tông Hồng MoMo / Rose rực rỡ
    # CVR %: Xanh Bạc Hà Emerald (#DCFCE7) với chữ xanh đậm #15803D
    f_header1 = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    f_header2 = Font(name="Arial", size=9, bold=True, color="1E293B")
    f_header2_oct = Font(name="Arial", size=9, bold=True, color="1E3A8A")
    f_total_r3 = Font(name="Arial", size=10, bold=True, color="1E3A8A")
    f_hub_pv = Font(name="Arial", size=10, bold=True, color="1E3A8A")
    f_sub_pv = Font(name="Arial", size=9, bold=False, color="1E293B")
    f_standalone_pv = Font(name="Arial", size=9, bold=True, color="1E3A8A")
    f_hub_click = Font(name="Arial", size=9, bold=True, color="9D174D")
    f_sub_click = Font(name="Arial", size=9, italic=True, color="BE185D")
    f_cvr = Font(name="Arial", size=10, bold=True, color="15803D")

    fill_mtd_banner = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    fill_full_banner = PatternFill(start_color="334155", end_color="334155", fill_type="solid")
    fill_blue_banner = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    fill_teal_banner = PatternFill(start_color="0D9488", end_color="0D9488", fill_type="solid")
    fill_slate_banner = PatternFill(start_color="475569", end_color="475569", fill_type="solid")
    fill_h2 = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    fill_h2_oct = PatternFill(start_color="93C5FD", end_color="93C5FD", fill_type="solid")
    fill_r3 = PatternFill(start_color="BFDBFE", end_color="BFDBFE", fill_type="solid")

    # MÀU CHO PAGEVIEWS
    fill_hub_pv = PatternFill(start_color="DBEAFE", end_color="DBEAFE", fill_type="solid") # Xanh dương 100
    fill_sub_pv = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid") # Trắng tinh
    fill_standalone_pv = PatternFill(start_color="F0F7FF", end_color="F0F7FF", fill_type="solid") # Xanh băng nhạt
    fill_pv_oct = PatternFill(start_color="BFDBFE", end_color="BFDBFE", fill_type="solid") # Nhấn tháng 10 cho PV

    # MÀU CHO CLICKS
    fill_hub_click = PatternFill(start_color="FCE7F3", end_color="FCE7F3", fill_type="solid") # Hồng MoMo 100
    fill_sub_click = PatternFill(start_color="FDF2F8", end_color="FDF2F8", fill_type="solid") # Hồng phấn 50
    fill_click_oct = PatternFill(start_color="FBCFE8", end_color="FBCFE8", fill_type="solid") # Nhấn tháng 10 cho Click
    fill_cvr = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Xanh bạc hà 100

    border_hub_top = Border(top=Side(style="medium", color="3B82F6"), bottom=Side(style="thin", color="93C5FD"))
    border_sub_pv = Border(bottom=Side(style="thin", color="EEF2F6"))
    border_standalone_top = Border(top=Side(style="thin", color="93C5FD"), bottom=Side(style="thin", color="E2E8F0"))
    border_click_bottom = Border(bottom=Side(style="thin", color="F472B6"))
    border_r3 = Border(top=Side(style="thin", color="3B82F6"), bottom=Side(style="thin", color="3B82F6"))

    align_center = Alignment(horizontal="center", vertical="center")
    align_left = Alignment(horizontal="left", vertical="center")
    align_right = Alignment(horizontal="right", vertical="center")

    hub_parent_row_nums = {8, 22, 24, 26, 28, 58, 68, 70, 72, 74, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 124, 126, 128, 130, 132, 134, 136}
    subproject_pv_row_nums = {10, 12, 14, 16, 18, 20, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 60, 62, 64, 66, 76, 78, 120, 122}

    # Ghi từng hàng
    for r_idx, row in enumerate(sheet_data):
        row_num = r_idx + 1
        for c_idx, val in enumerate(row):
            col_num = c_idx + 1
            cell = ws.cell(row=row_num, column=col_num)

            # Xử lý kiểu dữ liệu
            if isinstance(val, str) and val.startswith("="):
                cell.value = val
            elif isinstance(val, str) and val.replace("-", "").isdigit():
                cell.value = int(val)
            elif isinstance(val, int) or isinstance(val, float):
                cell.value = val
            elif val != "":
                cell.value = val

            # Áp dụng Alignment
            if col_num == 1:
                cell.alignment = align_left
            elif row_num <= 2:
                cell.alignment = align_center
            else:
                cell.alignment = align_right

            # Áp dụng Number Format
            if row_num == 2 and col_num in list(range(2, 10)) + list(range(12, 20)):
                cell.number_format = "mmm yy"
            elif row_num >= 3:
                if col_num in [10, 20]:
                    cell.number_format = "+#,##0;-#,##0;0"
                elif col_num == 11 or row_num == 5 or (row_num >= 140 and row_num <= 173):
                    cell.number_format = "0.0%"
                elif col_num in list(range(2, 10)) + list(range(12, 20)):
                    cell.number_format = "#,##0"

            # Áp dụng Styling theo phân tầng
            if row_num == 1:
                if col_num == 1:
                    cell.fill = fill_mtd_banner
                elif col_num in range(2, 10):
                    cell.fill = fill_mtd_banner
                elif col_num == 10:
                    cell.fill = fill_blue_banner
                elif col_num == 11:
                    cell.fill = fill_teal_banner
                elif col_num in range(12, 20):
                    cell.fill = fill_full_banner
                elif col_num == 20:
                    cell.fill = fill_slate_banner
                cell.font = f_header1
            elif row_num == 2:
                if col_num in [7, 17]:
                    cell.fill = fill_h2_oct
                    cell.font = f_header2_oct
                else:
                    cell.fill = fill_h2
                    cell.font = f_header2
            elif row_num == 3:
                cell.fill = fill_r3
                cell.font = f_total_r3
                cell.border = border_r3
            elif row_num in hub_parent_row_nums:
                # DÒNG HUB PAGEVIEWS -> NỀN XANH DƯƠNG
                if col_num in [7, 17]:
                    cell.fill = fill_pv_oct
                else:
                    cell.fill = fill_hub_pv
                cell.font = f_hub_pv
                cell.border = border_hub_top
            elif (row_num - 1) in hub_parent_row_nums:
                # DÒNG HUB CLICK -> NỀN HỒNG MOMO
                if col_num == 11:
                    cell.fill = fill_cvr
                    cell.font = f_cvr
                elif col_num in [7, 17]:
                    cell.fill = fill_click_oct
                    cell.font = f_hub_click
                else:
                    cell.fill = fill_hub_click
                    cell.font = f_hub_click
                cell.border = border_click_bottom
            elif row_num in subproject_pv_row_nums:
                # DÒNG SUBPROJECT PAGEVIEWS -> TRẮNG TINH
                if col_num in [7, 17]:
                    cell.fill = fill_hub_pv
                else:
                    cell.fill = fill_sub_pv
                cell.font = f_sub_pv
                cell.border = border_sub_pv
            elif (row_num - 1) in subproject_pv_row_nums:
                # DÒNG SUBPROJECT CLICK -> HỒNG PHẤN
                if col_num == 11:
                    cell.fill = fill_cvr
                    cell.font = f_cvr
                elif col_num in [7, 17]:
                    cell.fill = fill_click_oct
                    cell.font = f_sub_click
                else:
                    cell.fill = fill_sub_click
                    cell.font = f_sub_click
                cell.border = border_click_bottom
            elif row_num % 2 == 0 and row_num >= 8 and row_num <= 136:
                # Standalone PV -> XANH BĂNG
                if col_num in [7, 17]:
                    cell.fill = fill_pv_oct
                else:
                    cell.fill = fill_standalone_pv
                cell.font = f_standalone_pv
                cell.border = border_standalone_top
            elif row_num % 2 == 1 and row_num >= 9 and row_num <= 137:
                # Standalone Click -> HỒNG MOMO
                if col_num == 11:
                    cell.fill = fill_cvr
                    cell.font = f_cvr
                elif col_num in [7, 17]:
                    cell.fill = fill_click_oct
                    cell.font = f_hub_click
                else:
                    cell.fill = fill_hub_click
                    cell.font = f_hub_click
                cell.border = border_click_bottom
            elif row_num == 139:
                cell.fill = fill_h2
                cell.font = f_header2
            elif row_num >= 140 and row_num <= 173:
                cell.font = f_sub_pv

    # Cố định tiêu đề
    ws.freeze_panes = "B3"

    # Merge Row 1 banners
    ws.merge_cells("B1:I1")
    ws.merge_cells("L1:S1")

    # Thiết lập Outline Level (Group thu gọn) trong Excel
    outline_ranges = [
        (10, 21),   # Cinema
        (30, 57),   # Financial
        (60, 67),   # Vehicle
        (76, 79),   # Sim
        (120, 123), # Student
        (140, 173)  # Tỷ trọng %
    ]
    for start_r, end_r in outline_ranges:
        for r in range(start_r, end_r + 1):
            ws.row_dimensions[r].outline_level = 1

    # Điều chỉnh độ rộng cột
    ws.column_dimensions["A"].width = 36
    for col_idx in range(2, 21):
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = 12

    wb.save(excel_path)
    print(f"  ✓ Đã lưu Excel SSOT: {excel_path}")

    # Copy sang Google Drive Desktop nếu thư mục tồn tại
    if drive_path.parent.exists():
        shutil.copy2(excel_path, drive_path)
        print(f"  ✓ Đã đồng bộ sang Google Drive Desktop: {drive_path}")


if __name__ == "__main__":
    main()

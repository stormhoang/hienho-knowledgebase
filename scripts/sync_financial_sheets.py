#!/usr/bin/env python3
"""
Sync Financial Hub Sitemap & Roadmap to Google Sheets.
Target Sheet: https://docs.google.com/spreadsheets/d/1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A/edit
Spreadsheet ID: 1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).resolve().parent.parent
_CREDS_DIR = BASE_DIR / "07_REPORTS" / "data" / "credentials"
CREDS_FILE = next((p for p in (_CREDS_DIR / "ga4-credentials.json",
                              _CREDS_DIR / "ga4-credentials.json.disabled") if p.exists()),
                  _CREDS_DIR / "ga4-credentials.json")
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
EXCEL_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-roadmap.xlsx"
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

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as resp:
        token_data = json.loads(resp.read().decode("utf-8"))
    return token_data["access_token"]


def get_sheet_metadata(token):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets(properties)"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        meta = json.loads(resp.read().decode("utf-8"))
    sheet_map = {}
    for s in meta["sheets"]:
        p = s["properties"]
        sheet_map[p["title"]] = p["sheetId"]
    return sheet_map


def clear_range(token, range_name):
    encoded_range = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{encoded_range}:clear"
    req = urllib.request.Request(
        url,
        data=b"{}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
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


def batch_update_spreadsheet(token, requests):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
    body = json.dumps({"requests": requests}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode("utf-8")
        print("HTTPError details:", error_msg)
        raise


def sync_all():
    print("1. Fetching access token...")
    token = get_access_token()

    print("2. Getting sheet metadata...")
    sheet_map = get_sheet_metadata(token)
    print("Sheets available:", sheet_map)

    sitemap_id = sheet_map.get("Sitemap")
    roadmap_id = sheet_map.get("Product Roadmap")

    if sitemap_id is None:
        raise ValueError("Sheet 'Sitemap' not found in spreadsheet.")
    if roadmap_id is None:
        raise ValueError("Sheet 'Product Roadmap' not found in spreadsheet.")

    print(f"Sitemap Sheet ID: {sitemap_id}")
    print(f"Product Roadmap Sheet ID: {roadmap_id}")

    # 3. Read local Excel
    print("3. Reading local Excel: " + str(EXCEL_PATH))
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)

    # Sitemap rows
    ws_sitemap = wb["Sitemap"]
    sitemap_rows = []
    for r in range(1, ws_sitemap.max_row + 1):
        row_vals = [ws_sitemap.cell(r, c).value for c in range(1, ws_sitemap.max_column + 1)]
        sitemap_rows.append([str(v) if v is not None else "" for v in row_vals])

    # Roadmap rows
    ws_roadmap = wb["Roadmap"]
    roadmap_rows = []
    for r in range(1, ws_roadmap.max_row + 1):
        row_vals = [ws_roadmap.cell(r, c).value for c in range(1, ws_roadmap.max_column + 1)]
        roadmap_rows.append([str(v) if v is not None else "" for v in row_vals])

    # 4. Clear and write values
    print("4. Writing Sitemap data...")
    clear_range(token, "Sitemap!A1:D300")
    res_sitemap = update_values(token, f"Sitemap!A1:D{len(sitemap_rows)}", sitemap_rows)
    print(f"Sitemap updated: {res_sitemap.get('updatedCells')} cells across {len(sitemap_rows)} rows.")

    print("5. Writing Product Roadmap data...")
    clear_range(token, "Product Roadmap!A1:F50")
    res_roadmap = update_values(token, f"Product Roadmap!A1:F{len(roadmap_rows)}", roadmap_rows)
    print(f"Product Roadmap updated: {res_roadmap.get('updatedCells')} cells across {len(roadmap_rows)} rows.")

    # 5. Build styling requests
    print("6. Applying visual styling via batchUpdate...")
    requests = []

    # -------------------------------------------------------------
    # SITEMAP STYLING
    # -------------------------------------------------------------
    # Unmerge any existing merges on Sitemap to avoid conflicts
    requests.append({
        "unmergeCells": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": 118,
                "startColumnIndex": 0,
                "endColumnIndex": 4
            }
        }
    })

    # Freeze top 3 rows
    requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sitemap_id,
                "gridProperties": {
                    "frozenRowCount": 3
                }
            },
            "fields": "gridProperties.frozenRowCount"
        }
    })

    # Column widths for Sitemap: Col A (65), Col B (280), Col C (460), Col D (340)
    col_widths_sitemap = [65, 280, 460, 340]
    for col_idx, width in enumerate(col_widths_sitemap):
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sitemap_id,
                    "dimension": "COLUMNS",
                    "startIndex": col_idx,
                    "endIndex": col_idx + 1
                },
                "properties": {
                    "pixelSize": width
                },
                "fields": "pixelSize"
            }
        })

    # Row 1: Merged Title A1:D1
    requests.append({
        "mergeCells": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "mergeType": "MERGE_ALL"
        }
    })
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.85, "green": 0.88, "blue": 0.95},
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 11,
                        "bold": True,
                        "foregroundColor": {"red": 0.12, "green": 0.31, "blue": 0.47}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    })

    # Row 2: Merged Subtitle A2:D2
    requests.append({
        "mergeCells": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 1,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "mergeType": "MERGE_ALL"
        }
    })
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 1,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.95, "green": 0.96, "blue": 0.98},
                    "horizontalAlignment": "LEFT",
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "italic": False,
                        "foregroundColor": {"red": 0.28, "green": 0.33, "blue": 0.41}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,wrapStrategy,textFormat)"
        }
    })

    # Row 3: Header Row A3:D3
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.12, "green": 0.31, "blue": 0.47},
                    "horizontalAlignment": "LEFT",
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "bold": True,
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    })
    # STT header centered
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 0,
                "endColumnIndex": 1
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    })

    # Rows 4 to 117 (Data rows: index 3 to 117)
    # Default styling for all data cells
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 3,
                "endRowIndex": len(sitemap_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.12, "green": 0.16, "blue": 0.23}
                    }
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,textFormat)"
        }
    })

    # Alternating row background for Sitemap
    for r_idx in range(3, len(sitemap_rows)):
        bg = {"red": 0.97, "green": 0.98, "blue": 0.99} if r_idx % 2 == 1 else {"red": 1.0, "green": 1.0, "blue": 1.0}
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 4
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": bg
                    }
                },
                "fields": "userEnteredFormat.backgroundColor"
            }
        })

    # STT Col A: Center aligned
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 3,
                "endRowIndex": len(sitemap_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 1
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    })

    # Category Col B: Bold
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 3,
                "endRowIndex": len(sitemap_rows),
                "startColumnIndex": 1,
                "endColumnIndex": 2
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "bold": True
                    }
                }
            },
            "fields": "userEnteredFormat.textFormat.bold"
        }
    })

    # URL Col D: Consolas green
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 3,
                "endRowIndex": len(sitemap_rows),
                "startColumnIndex": 3,
                "endColumnIndex": 4
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "fontFamily": "Consolas",
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.016, "green": 0.47, "blue": 0.34}
                    }
                }
            },
            "fields": "userEnteredFormat.textFormat"
        }
    })

    # Borders for Sitemap table (rows 2 to 117)
    border_style = {
        "style": "SOLID",
        "width": 1,
        "color": {"red": 0.85, "green": 0.88, "blue": 0.92}
    }
    requests.append({
        "updateBorders": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 2,
                "endRowIndex": len(sitemap_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 4
            },
            "top": border_style,
            "bottom": border_style,
            "left": border_style,
            "right": border_style,
            "innerHorizontal": border_style,
            "innerVertical": border_style
        }
    })

    # -------------------------------------------------------------
    # PRODUCT ROADMAP STYLING
    # -------------------------------------------------------------
    # Unmerge any existing merges on Roadmap
    requests.append({
        "unmergeCells": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 0,
                "endRowIndex": 25,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            }
        }
    })

    # Freeze top 2 rows
    requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": roadmap_id,
                "gridProperties": {
                    "frozenRowCount": 2
                }
            },
            "fields": "gridProperties.frozenRowCount"
        }
    })

    # Column widths for Roadmap: Col A: 130, Col B: 110, Col C: 190, Col D: 260, Col E: 540, Col F: 110
    col_widths_roadmap = [130, 110, 190, 260, 540, 110]
    for col_idx, width in enumerate(col_widths_roadmap):
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": roadmap_id,
                    "dimension": "COLUMNS",
                    "startIndex": col_idx,
                    "endIndex": col_idx + 1
                },
                "properties": {
                    "pixelSize": width
                },
                "fields": "pixelSize"
            }
        })

    # Row 1: Merged Title A1:F1
    requests.append({
        "mergeCells": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "mergeType": "MERGE_ALL"
        }
    })
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.85, "green": 0.88, "blue": 0.95},
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 11,
                        "bold": True,
                        "foregroundColor": {"red": 0.12, "green": 0.31, "blue": 0.47}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    })

    # Row 2: Header Row A2:F2
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 1,
                "endRowIndex": 2,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.12, "green": 0.31, "blue": 0.47},
                    "horizontalAlignment": "LEFT",
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "bold": True,
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    })

    # Center header for Phase, Thời Gian, Trạng Thái
    for c_idx in [0, 1, 5]:
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": 1,
                    "endRowIndex": 2,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "CENTER"
                    }
                },
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })

    # Rows 3 to 20: Data rows
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 2,
                "endRowIndex": len(roadmap_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.12, "green": 0.16, "blue": 0.23}
                    }
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,textFormat)"
        }
    })

    # Wrap description in Col E
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 2,
                "endRowIndex": len(roadmap_rows),
                "startColumnIndex": 4,
                "endColumnIndex": 5
            },
            "cell": {
                "userEnteredFormat": {
                    "wrapStrategy": "WRAP"
                }
            },
            "fields": "userEnteredFormat.wrapStrategy"
        }
    })

    # Bold product name Col D
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 2,
                "endRowIndex": len(roadmap_rows),
                "startColumnIndex": 3,
                "endColumnIndex": 4
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "bold": True
                    }
                }
            },
            "fields": "userEnteredFormat.textFormat.bold"
        }
    })

    # Center Phase, Thời Gian
    for c_idx in [0, 1]:
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": 2,
                    "endRowIndex": len(roadmap_rows),
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "CENTER"
                    }
                },
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })

    # Alternating row background for Roadmap
    for r_idx in range(2, len(roadmap_rows)):
        bg = {"red": 0.97, "green": 0.98, "blue": 0.99} if r_idx % 2 == 1 else {"red": 1.0, "green": 1.0, "blue": 1.0}
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 5
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": bg
                    }
                },
                "fields": "userEnteredFormat.backgroundColor"
            }
        })

    # Status badge styling (Col F)
    for r_idx in range(2, len(roadmap_rows)):
        status_val = roadmap_rows[r_idx][5] if len(roadmap_rows[r_idx]) > 5 else ""
        if status_val == "Done":
            bg = {"red": 0.86, "green": 0.98, "blue": 0.90}  # Emerald 100
            fg = {"red": 0.08, "green": 0.50, "blue": 0.24}  # Emerald 700
        elif status_val == "In Progress":
            bg = {"red": 0.99, "green": 0.95, "blue": 0.78}  # Amber 100
            fg = {"red": 0.71, "green": 0.33, "blue": 0.04}  # Amber 700
        else:  # Planned
            bg = {"red": 0.88, "green": 0.91, "blue": 1.0}   # Indigo 100
            fg = {"red": 0.26, "green": 0.22, "blue": 0.79}  # Indigo 700

        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 5,
                    "endColumnIndex": 6
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": bg,
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Arial",
                            "fontSize": 10,
                            "bold": True,
                            "foregroundColor": fg
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
            }
        })

    # Borders for Roadmap
    requests.append({
        "updateBorders": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 1,
                "endRowIndex": len(roadmap_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "top": border_style,
            "bottom": border_style,
            "left": border_style,
            "right": border_style,
            "innerHorizontal": border_style,
            "innerVertical": border_style
        }
    })

    print(f"Executing batchUpdate with {len(requests)} requests...")
    batch_res = batch_update_spreadsheet(token, requests)
    print("batchUpdate completed successfully!")
    print(f"Total replies: {len(batch_res.get('replies', []))}")


if __name__ == "__main__":
    sync_all()

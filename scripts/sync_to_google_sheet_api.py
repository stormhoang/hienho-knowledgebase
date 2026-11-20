#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOOGLE SHEETS CLOUD-NATIVE API SYNC ENGINE
Đồng bộ trực tiếp Cloud-to-Cloud từ GA4 / Snapshot sang Google Sheet SSOT:
ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU
URL: https://docs.google.com/spreadsheets/d/1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU/edit

Ưu điểm tuyệt đối so với cách cũ (.xlsx + Drive Desktop):
1. Ghi trực tiếp qua Google Sheets API trong 1-2 giây, không phụ thuộc app Drive Desktop trên Mac.
2. Tự động lưu vết 100% trong Google Sheets Version History (Lịch sử phiên bản).
3. Google Sheets tự động tính toán lại toàn bộ công thức SUM, INDEX MATCH, ARRAYFORMULA.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
_CREDS_DIR = BASE_DIR / "07_REPORTS" / "data" / "credentials"
CREDS_FILE = next((p for p in (_CREDS_DIR / "ga4-credentials.json",
                              _CREDS_DIR / "ga4-credentials.json.disabled") if p.exists()),
                  _CREDS_DIR / "ga4-credentials.json")
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
TARGET_SHEET_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"

def get_sheets_token():
    """Lấy Access Token cho Google Sheets API từ refresh_token."""
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
    with urllib.request.urlopen(req, timeout=60) as resp:
        res = json.loads(resp.read().decode())
        return res["access_token"]

def sync_google_sheet(
    days_elapsed, total_pv,
    organic_pv, paid_pv, direct_pv, referral_pv, others_pv, non_paid_pv,
    hubs_pv, cinema_sub,
    spreadsheet_id=TARGET_SHEET_ID,
    month="2026-11",
    ai_traffic_pv=None
):
    """Cập nhật toàn bộ các sheet trong Google Sheet SSOT qua Sheets API."""
    token = get_sheets_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    print("\n" + "=" * 70)
    print(f"BẮT ĐẦU ĐỒNG BỘ CLOUD-TO-CLOUD GOOGLE SHEETS API ({month} MTD {days_elapsed}D)")
    print(f"Spreadsheet ID: {spreadsheet_id}")
    print("=" * 70)

    # Cấu hình cột theo tháng:
    # Full Month (B..M): Col L = Nov 26, Col K = Oct 26
    # Month to Date (O..V): Col U = Nov 26 MTD, Col T = Oct 26 MTD
    if month == "2026-11":
        col_full = "L"
        col_mtd = "U"
        col_pivot = "J"
        col_pivot_idx = 9
        baseline_col_idx = 8
    else:
        col_full = "K"
        col_mtd = "T"
        col_pivot = "I"
        col_pivot_idx = 8
        baseline_col_idx = 7

    # Xác định AI Traffic PV nếu chưa truyền vào
    if ai_traffic_pv is None:
        try:
            m_parts = month.split("-")
            cons_file = BASE_DIR / "07_REPORTS" / "data" / f"monthly_{m_parts[1]}_{m_parts[0]}_mtd_{days_elapsed}d.json"
            if cons_file.exists():
                with open(cons_file, "r", encoding="utf-8") as f:
                    _cdata = json.load(f)
                    ai_traffic_pv = _cdata.get("channels", {}).get("ai_traffic", {}).get("pv", 0)
        except Exception:
            ai_traffic_pv = 0
    if ai_traffic_pv is None:
        ai_traffic_pv = 0

    merged_referral_pv = max(0, non_paid_pv - (organic_pv + direct_pv + ai_traffic_pv))

    # 1. Chuẩn bị Batch Update cho các cell chính
    updates = []

    # Overall Performance: A1, Row 5 (=col9+col10), Rows 9:14 (Paid, Non-Paid=SUM, Organic, Direct, AI Traffic, Referral), Rows 16:21 (% share)
    updates.append({
        "range": "'Overall Performance'!A1",
        "values": [[f"Update to: {days_elapsed}"]]
    })

    for c_col in [col_full, col_mtd]:
        updates.append({
            "range": f"'Overall Performance'!{c_col}5",
            "values": [[f"={c_col}9+{c_col}10"]]
        })
        updates.append({
            "range": f"'Overall Performance'!{c_col}8",
            "values": [[""]]
        })
        updates.append({
            "range": f"'Overall Performance'!{c_col}9:{c_col}14",
            "values": [
                [paid_pv],
                [f"=SUM({c_col}11:{c_col}14)"],
                [organic_pv],
                [direct_pv],
                [ai_traffic_pv],
                [merged_referral_pv]
            ]
        })
        updates.append({
            "range": f"'Overall Performance'!{c_col}15",
            "values": [[""]]
        })
        updates.append({
            "range": f"'Overall Performance'!{c_col}16:{c_col}21",
            "values": [
                [f'=IFERROR({c_col}9/${c_col}$5, "")'],
                [f'=IFERROR({c_col}10/${c_col}$5, "")'],
                [f'=IFERROR({c_col}11/${c_col}$5, "")'],
                [f'=IFERROR({c_col}12/${c_col}$5, "")'],
                [f'=IFERROR({c_col}13/${c_col}$5, "")'],
                [f'=IFERROR({c_col}14/${c_col}$5, "")']
            ]
        })
        updates.append({
            "range": f"'Overall Performance'!{c_col}22",
            "values": [[""]]
        })

    # PaidNonPaid: A1, col_full & col_mtd 9:13
    updates.append({
        "range": "'PaidNonPaid'!A1",
        "values": [[f"Update to: {days_elapsed}"]]
    })
    for c_pnp in [col_full, col_mtd]:
        updates.append({
            "range": f"'PaidNonPaid'!{c_pnp}9:{c_pnp}13",
            "values": [
                [organic_pv],
                [direct_pv],
                [referral_pv],
                [others_pv],
                [paid_pv]
            ]
        })

    # Target: A1, col_full 10:14
    updates.append({
        "range": "'Target'!A1",
        "values": [[f"Update to: {days_elapsed}"]]
    })
    updates.append({
        "range": f"'Target'!{col_full}10:{col_full}14",
        "values": [
            [organic_pv],
            [paid_pv],
            [direct_pv],
            [referral_pv],
            [others_pv]
        ]
    })

    # Cinema: B1, H3, H8, H9, H15, H16, H22, H23, H29, H30, H36, H37, H43, H44 (Dùng công thức chuẩn tra cứu Pivot)
    updates.append({
        "range": "'Cinema'!B1",
        "values": [[f"Update to: {days_elapsed}"]]
    })
    updates.append({
        "range": "'Cinema'!H3",
        "values": [["=SUM(H8,H15,H22,H29,H36,H43)"]]
    })
    updates.append({
        "range": "'Cinema'!H8",
        "values": [["=sum(H9:H13)"]]
    })
    updates.append({
        "range": "'Cinema'!H9",
        "values": [["=SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Cineplex Page\", 'MTD Pivot'!$C:$C, $B9)"]]
    })
    updates.append({
        "range": "'Cinema'!H15",
        "values": [["=sum(H16:H20)"]]
    })
    updates.append({
        "range": "'Cinema'!H16",
        "values": [["=SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Page\", 'MTD Pivot'!$C:$C, $B16)"]]
    })
    updates.append({
        "range": "'Cinema'!H22",
        "values": [["=sum(H23:H27)"]]
    })
    updates.append({
        "range": "'Cinema'!H23",
        "values": [["=SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Blog\", 'MTD Pivot'!$C:$C, $B23)"]]
    })
    updates.append({
        "range": "'Cinema'!H29",
        "values": [["=sum(H30:H34)"]]
    })
    updates.append({
        "range": "'Cinema'!H30",
        "values": [["=SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Home Page\", 'MTD Pivot'!$C:$C, $B30)"]]
    })
    updates.append({
        "range": "'Cinema'!H36",
        "values": [["=sum(H37:H41)"]]
    })
    updates.append({
        "range": "'Cinema'!H37",
        "values": [["=SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_News\", 'MTD Pivot'!$C:$C, $B37)"]]
    })
    updates.append({
        "range": "'Cinema'!H43",
        "values": [["=sum(H44:H47)"]]
    })
    updates.append({
        "range": "'Cinema'!H44",
        "values": [["=SUMIFS('MTD Pivot'!I:I, 'MTD Pivot'!$A:$A, \"Cinema_Landing Page\", 'MTD Pivot'!$C:$C, $B44)"]]
    })
    # Financial: B1
    updates.append({
        "range": "'Financial'!B1",
        "values": [[f"Update to: {days_elapsed}"]]
    })

    for pivot_sheet in ["MTD Pivot", "Full month Pivot"]:
        q_range = urllib.parse.quote(f"'{pivot_sheet}'!A:{col_pivot}")
        url_get = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{q_range}?valueRenderOption=UNFORMATTED_VALUE"
        req_get = urllib.request.Request(url_get, headers=headers)
        with urllib.request.urlopen(req_get, timeout=60) as resp:
            rows = json.loads(resp.read().decode()).get("values", [])

        if not rows or len(rows) < 3:
            continue

        sum_items = 0
        grand_total_row_idx = None
        others_row_idx = None

        # Tính tổng cột hiện tại (nếu là tháng mới chưa có số, dùng baseline tháng trước làm tỷ trọng)
        for r_idx, r in enumerate(rows):
            if r_idx < 2:
                continue
            name = str(r[0]).strip() if r and len(r) > 0 else ""
            if name.lower() == "grand total":
                grand_total_row_idx = r_idx
                continue
            if name == "Others" and others_row_idx is None:
                others_row_idx = r_idx

            val = r[col_pivot_idx] if len(r) > col_pivot_idx and isinstance(r[col_pivot_idx], (int, float)) else 0
            sum_items += val

        use_baseline = (sum_items == 0)
        if use_baseline:
            # Dùng trọng số tháng trước (baseline_col_idx)
            for r_idx, r in enumerate(rows):
                if r_idx < 2:
                    continue
                name = str(r[0]).strip() if r and len(r) > 0 else ""
                if name.lower() != "grand total":
                    val = r[baseline_col_idx] if len(r) > baseline_col_idx and isinstance(r[baseline_col_idx], (int, float)) else 0
                    sum_items += val

        scale_factor = total_pv / sum_items if sum_items > 0 else 1.0

        new_col_values = []
        new_sum = 0
        for r_idx, r in enumerate(rows):
            if r_idx < 2:
                new_col_values.append([r[col_pivot_idx] if len(r) > col_pivot_idx else ""])
                continue
            name = str(r[0]).strip() if r and len(r) > 0 else ""
            if name.lower() == "grand total":
                new_col_values.append([total_pv])
                continue

            ref_idx = baseline_col_idx if use_baseline else col_pivot_idx
            val = r[ref_idx] if len(r) > ref_idx and isinstance(r[ref_idx], (int, float)) else 0
            scaled_val = round(val * scale_factor)
            new_col_values.append([scaled_val])
            new_sum += scaled_val

        # Cân bằng sai số làm tròn vào hàng Others
        diff = total_pv - new_sum
        if diff != 0 and others_row_idx is not None:
            new_col_values[others_row_idx][0] += diff

        updates.append({
            "range": f"'{pivot_sheet}'!{col_pivot}1:{col_pivot}{len(new_col_values)}",
            "values": new_col_values
        })

    # 3. Gửi batchUpdate lên Google Sheets API
    batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchUpdate"
    payload = json.dumps({
        "valueInputOption": "USER_ENTERED",
        "data": updates
    }).encode("utf-8")

    req_batch = urllib.request.Request(batch_url, data=payload, method="POST", headers=headers)
    with urllib.request.urlopen(req_batch, timeout=60) as resp:
        res = json.loads(resp.read().decode())
        print(f"✓ Cập nhật thành công {res.get('totalUpdatedCells', 0)} ô trên {len(updates)} dải ô!")
        print(f"✓ Liên kết trực tiếp: https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit?gid=1273714888#gid=1273714888")
        print("=" * 70)

        # Tự động co giãn toàn bộ các cột MTD lịch sử (T5..T11) theo chu kỳ N ngày cùng kỳ
        try:
            from scripts.sync_mtd_all_months import sync_all_mtd
            sync_all_mtd(days_elapsed=days_elapsed, override_m11_pv=total_pv if month == "2026-11" else None)
        except Exception as e_mtd:
            print(f"[Sheets-API] Lưu ý co giãn MTD đa tháng: {e_mtd}")

        return res

if __name__ == "__main__":
    # Test chạy trực tiếp với dữ liệu MTD 24
    consolidated_file = BASE_DIR / "07_REPORTS" / "data" / "monthly_10_2026_consolidated.json"
    if consolidated_file.exists():
        with open(consolidated_file, "r", encoding="utf-8") as f:
            d = json.load(f)
        ch = d["channels"]
        sync_google_sheet(
            days_elapsed=d["days_elapsed"],
            total_pv=d["actual_mtd_pv"],
            organic_pv=ch["organic"]["pv"],
            paid_pv=ch["paid"]["pv"],
            direct_pv=ch["direct"]["pv"],
            referral_pv=ch["referral"]["pv"],
            others_pv=ch["others"]["pv"],
            non_paid_pv=ch["non_paid_total"]["pv"],
            hubs_pv={k: v["pv"] for k, v in d["hubs"].items()},
            cinema_sub=d.get("cinema_breakdown", {})
        )

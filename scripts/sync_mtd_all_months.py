#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC MTD ALL MONTHS (LIKE-FOR-LIKE CÙNG KỲ)
Đồng bộ số liệu Month-To-Date chuẩn xác cho toàn bộ các tháng lịch sử (Tháng 5 -> Tháng 11)
đáp ứng đúng nguyên tắc so sánh cùng kỳ (N ngày đầu tháng).

Target:
- Google Sheets Cloud Native SSOT: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU
- Excel SSOT: 07_REPORTS/web_performance_tracking.xlsx & web_platform_performance.xlsx
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_ga4_to_hubs import get_access_token, PROPERTY_ID, run_ga4_report
from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID

def sync_all_mtd(days_elapsed=2):
    print("=" * 75)
    print(f"KHỞI CHẠY ĐỒNG BỘ MTD {days_elapsed} NGÀY CHO TOÀN BỘ CÁC THÁNG (T5 -> T11)")
    print(f"Spreadsheet ID: {TARGET_SHEET_ID}")
    print("=" * 75)

    ga4_token = get_access_token()
    sheets_token = get_sheets_token()
    sheets_headers = {
        "Authorization": f"Bearer {sheets_token}",
        "Content-Type": "application/json"
    }

    months = [
        ("2026-05", f"2026-05-01", f"2026-05-{days_elapsed:02d}"),
        ("2026-06", f"2026-06-01", f"2026-06-{days_elapsed:02d}"),
        ("2026-07", f"2026-07-01", f"2026-07-{days_elapsed:02d}"),
        ("2026-08", f"2026-08-01", f"2026-08-{days_elapsed:02d}"),
        ("2026-09", f"2026-09-01", f"2026-09-{days_elapsed:02d}"),
        ("2026-10", f"2026-10-01", f"2026-10-{days_elapsed:02d}"),
        ("2026-11", f"2026-11-01", f"2026-11-{days_elapsed:02d}"),
    ]

    # 1. Truy vấn GA4 lấy số liệu chuẩn từng tháng
    print(f"[1/5] Kéo dữ liệu GA4 MTD {days_elapsed} ngày cho 7 tháng...")
    month_metrics = {}
    for m_str, s_date, e_date in months:
        res_prop = run_ga4_report(ga4_token, {
            "dateRanges": [{"startDate": s_date, "endDate": e_date}],
            "metrics": [{"name": "screenPageViews"}, {"name": "totalUsers"}, {"name": "sessions"}]
        })
        row = res_prop.get("rows", [{}])[0].get("metricValues", [])
        tot_pv = int(row[0]["value"]) if row else 0
        tot_users = int(row[1]["value"]) if len(row) > 1 else 0
        tot_sess = int(row[2]["value"]) if len(row) > 2 else 0

        res_ch = run_ga4_report(ga4_token, {
            "dateRanges": [{"startDate": s_date, "endDate": e_date}],
            "dimensions": [{"name": "sessionDefaultChannelGroup"}, {"name": "sessionSource"}],
            "metrics": [{"name": "screenPageViews"}],
            "limit": 10000
        })

        org_pv = 0
        dir_pv = 0
        paid_pv = 0
        ref_pv = 0
        oth_pv = 0

        for r in res_ch.get("rows", []):
            ch = r["dimensionValues"][0]["value"]
            src = r["dimensionValues"][1]["value"]
            pv = int(r["metricValues"][0]["value"])

            cn = ch.lower()
            sn = src.lower()

            if sn == "in_app" or sn.startswith("in_app"):
                ref_pv += pv
            elif "organic search" in cn:
                org_pv += pv
            elif "direct" in cn:
                dir_pv += pv
            elif "referral" in cn:
                ref_pv += pv
            elif any(k in cn for k in ["paid", "cpc", "display"]):
                paid_pv += pv
            else:
                oth_pv += pv

        s_ch = org_pv + dir_pv + paid_pv + ref_pv + oth_pv
        if tot_pv != s_ch:
            oth_pv += (tot_pv - s_ch)

        month_metrics[m_str] = {
            "total_pv": tot_pv,
            "users": tot_users,
            "sessions": tot_sess,
            "organic": org_pv,
            "paid": paid_pv,
            "direct": dir_pv,
            "referral": ref_pv,
            "others": oth_pv,
            "non_paid": org_pv + dir_pv + ref_pv + oth_pv
        }
        print(f"  ✓ {m_str}: Total={tot_pv:,} | Org={org_pv:,} | Paid={paid_pv:,} | Dir={dir_pv:,} | Ref={ref_pv:,} | Oth={oth_pv:,}")

    # 2. Đọc MTD Pivot từ Google Sheets và co giãn tỷ lệ tất cả các cột
    print(f"\n[2/5] Co giãn tỷ lệ MTD Pivot cho toàn bộ 7 cột tháng (Col D..J)...")
    q_range = urllib.parse.quote("MTD Pivot!A1:J359")
    url_get = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{q_range}?valueRenderOption=UNFORMATTED_VALUE"
    req_get = urllib.request.Request(url_get, headers=sheets_headers)
    with urllib.request.urlopen(req_get) as resp:
        pivot_rows = json.loads(resp.read().decode()).get("values", [])

    grand_total_row_idx = None
    others_row_idx = None
    for r_idx, r in enumerate(pivot_rows):
        if not r: continue
        name = str(r[0]).strip()
        if name.lower() == "grand total":
            grand_total_row_idx = r_idx
        if name == "Others" and others_row_idx is None:
            others_row_idx = r_idx

    target_totals = [
        month_metrics["2026-05"]["total_pv"],
        month_metrics["2026-06"]["total_pv"],
        month_metrics["2026-07"]["total_pv"],
        month_metrics["2026-08"]["total_pv"],
        month_metrics["2026-09"]["total_pv"],
        month_metrics["2026-10"]["total_pv"],
        month_metrics["2026-11"]["total_pv"],
    ]

    new_pivot_data = [row[:] for row in pivot_rows]

    for idx, col_idx in enumerate(range(3, 10)):
        target = target_totals[idx]
        col_letter = chr(ord('D') + idx)
        
        # Lấy giá trị hiện tại các dòng dự án
        curr_vals = []
        for r_idx in range(2, grand_total_row_idx):
            r = pivot_rows[r_idx]
            val = r[col_idx] if len(r) > col_idx and isinstance(r[col_idx], (int, float)) else 0
            curr_vals.append((r_idx, val))
        
        curr_sum = sum(v for _, v in curr_vals)
        scale = target / curr_sum if curr_sum > 0 else 1.0

        new_sum = 0
        for r_idx, val in curr_vals:
            new_val = round(val * scale)
            while len(new_pivot_data[r_idx]) <= col_idx:
                new_pivot_data[r_idx].append(0)
            new_pivot_data[r_idx][col_idx] = new_val
            new_sum += new_val

        # Bù sai số làm tròn vào Others
        diff = target - new_sum
        if others_row_idx is not None:
            new_pivot_data[others_row_idx][col_idx] += diff

        # Cập nhật Grand Total
        while len(new_pivot_data[grand_total_row_idx]) <= col_idx:
            new_pivot_data[grand_total_row_idx].append(0)
        new_pivot_data[grand_total_row_idx][col_idx] = target
        print(f"  ✓ Col {col_letter} ({months[idx][0]}): {curr_sum:,} -> {target:,} (scale: {scale:.4f}, diff: {diff})")

    # 3. Chuẩn bị Batch Update toàn diện Google Sheets
    print(f"\n[3/5] Chuẩn bị Batch Update cho Google Sheets SSOT...")
    updates = []

    # 3.1 Cập nhật MTD Pivot
    updates.append({
        "range": "MTD Pivot!A1:J359",
        "values": new_pivot_data
    })

    # 3.2 Cập nhật Overall Performance (Tháng 5..11 MTD: Cột O..U)
    mtd_cols = ["O", "P", "Q", "R", "S", "T", "U"]
    updates.append({
        "range": "'Overall Performance'!A1",
        "values": [[f"Update to: {days_elapsed}"]]
    })

    # Row 5: Total PV
    updates.append({
        "range": "'Overall Performance'!O5:U5",
        "values": [[f"=SUM({c}9:{c}13)" for c in mtd_cols]]
    })
    # Row 6: Net add
    updates.append({
        "range": "'Overall Performance'!P6:U6",
        "values": [[f"={mtd_cols[i]}5-{mtd_cols[i-1]}5" for i in range(1, len(mtd_cols))]]
    })
    # Row 7: Growth Rate
    updates.append({
        "range": "'Overall Performance'!P7:U7",
        "values": [[f"=IFERROR(({mtd_cols[i]}5/{mtd_cols[i-1]}5)-1, 0)" for i in range(1, len(mtd_cols))]]
    })

    # Rows 9..13: Kênh Organic, Paid, Direct, Referral, Others cho 7 tháng
    for idx, (m_str, _, _) in enumerate(months):
        c_let = mtd_cols[idx]
        m_info = month_metrics[m_str]
        updates.append({
            "range": f"'Overall Performance'!{c_let}9:{c_let}13",
            "values": [
                [m_info["organic"]],
                [m_info["paid"]],
                [m_info["direct"]],
                [m_info["referral"]],
                [m_info["others"]]
            ]
        })
        # Rows 15..20: Tỷ lệ %
        updates.append({
            "range": f"'Overall Performance'!{c_let}15:{c_let}20",
            "values": [
                [f"={c_let}9/${c_let}$5"],
                [f"={c_let}10/${c_let}$5"],
                [f"={c_let}11/${c_let}$5"],
                [f"={c_let}12/${c_let}$5"],
                [f"={c_let}13/${c_let}$5"],
                [f"={c_let}15+{c_let}17+{c_let}18+{c_let}19"]
            ]
        })

    # Cập nhật Full Month Nov (Cột L) trong Overall Performance
    m11_info = month_metrics["2026-11"]
    updates.append({
        "range": "'Overall Performance'!L5",
        "values": [["=SUM(L9:L13)"]]
    })
    updates.append({
        "range": "'Overall Performance'!L9:L13",
        "values": [
            [m11_info["organic"]],
            [m11_info["paid"]],
            [m11_info["direct"]],
            [m11_info["referral"]],
            [m11_info["others"]]
        ]
    })
    updates.append({
        "range": "'Overall Performance'!L15:L20",
        "values": [
            ["=L9/$L$5"],
            ["=L10/$L$5"],
            ["=L11/$L$5"],
            ["=L12/$L$5"],
            ["=L13/$L$5"],
            ["=L15+L17+L18+L19"]
        ]
    })

    # 3.3 Cập nhật PaidNonPaid
    updates.append({
        "range": "'PaidNonPaid'!A1",
        "values": [[f"Update to: {days_elapsed}"]]
    })
    # Row 5: trỏ sang Overall Performance
    updates.append({
        "range": "'PaidNonPaid'!O5:U5",
        "values": [[f"='Overall Performance'!{c}5" for c in mtd_cols]]
    })
    # Row 6: Net add
    updates.append({
        "range": "'PaidNonPaid'!P6:U6",
        "values": [[f"={mtd_cols[i]}5-{mtd_cols[i-1]}5" for i in range(1, len(mtd_cols))]]
    })
    # Row 7: Growth Rate
    updates.append({
        "range": "'PaidNonPaid'!P7:U7",
        "values": [[f"=IFERROR(({mtd_cols[i]}5/{mtd_cols[i-1]}5)-1, 0)" for i in range(1, len(mtd_cols))]]
    })
    # Row 8: Non-Paid = SUM(9:12)
    updates.append({
        "range": "'PaidNonPaid'!O8:U8",
        "values": [[f"=SUM({c}9:{c}12)" for c in mtd_cols]]
    })

    # Rows 9..13: Kênh PaidNonPaid (Organic, Direct, Referral, Others, Paid)
    for idx, (m_str, _, _) in enumerate(months):
        c_let = mtd_cols[idx]
        m_info = month_metrics[m_str]
        updates.append({
            "range": f"'PaidNonPaid'!{c_let}9:{c_let}13",
            "values": [
                [m_info["organic"]],
                [m_info["direct"]],
                [m_info["referral"]],
                [m_info["others"]],
                [m_info["paid"]]
            ]
        })
        # Rows 15..20: Tỷ trọng
        updates.append({
            "range": f"'PaidNonPaid'!{c_let}15:{c_let}20",
            "values": [
                [f"={c_let}9/${c_let}$5"],
                [f"={c_let}13/${c_let}$5"],
                [f"={c_let}10/${c_let}$5"],
                [f"={c_let}11/${c_let}$5"],
                [f"={c_let}12/${c_let}$5"],
                [f"={c_let}15+{c_let}17+{c_let}18+{c_let}19"]
            ]
        })

    # Full month Nov (Col L) trong PaidNonPaid
    updates.append({
        "range": "'PaidNonPaid'!L5",
        "values": [["='Overall Performance'!L5"]]
    })
    updates.append({
        "range": "'PaidNonPaid'!L8",
        "values": [["=SUM(L9:L12)"]]
    })
    updates.append({
        "range": "'PaidNonPaid'!L9:L13",
        "values": [
            [m11_info["organic"]],
            [m11_info["direct"]],
            [m11_info["referral"]],
            [m11_info["others"]],
            [m11_info["paid"]]
        ]
    })

    # 3.4 Cập nhật Target sheet
    updates.append({
        "range": "'Target'!A1",
        "values": [[f"Update to: {days_elapsed}"]]
    })
    updates.append({
        "range": "'Target'!L6",
        "values": [["='Overall Performance'!L5"]]
    })
    updates.append({
        "range": "'Target'!L10:L14",
        "values": [
            [m11_info["organic"]],
            [m11_info["paid"]],
            [m11_info["direct"]],
            [m11_info["referral"]],
            [m11_info["others"]]
        ]
    })

    # 3.5 Bổ sung công thức Cột M (Nov 26) trong Channel Detail Flow
    c_m_updates = [
        {"range": "'Channel Detail Flow'!M3", "values": [["=SUM(M7,M48,M89,M130,M172)"]]},
        {"range": "'Channel Detail Flow'!M4", "values": [["=M3-L3"]]},
        {"range": "'Channel Detail Flow'!M5", "values": [["=IFERROR(M3/L3-1,0)"]]},
        {"range": "'Channel Detail Flow'!M7", "values": [["=SUM(M9:M46)"]]},
        {"range": "'Channel Detail Flow'!M8", "values": [["=M7-L7"]]},
        {"range": "'Channel Detail Flow'!M48", "values": [["=SUM(M50:M87)"]]},
        {"range": "'Channel Detail Flow'!M49", "values": [["=M48-L48"]]},
        {"range": "'Channel Detail Flow'!M89", "values": [["=SUM(M91:M128)"]]},
        {"range": "'Channel Detail Flow'!M90", "values": [["=M89-L89"]]},
        {"range": "'Channel Detail Flow'!M130", "values": [["=SUM(M132:M169)"]]},
        {"range": "'Channel Detail Flow'!M131", "values": [["=M130-L130"]]},
        {"range": "'Channel Detail Flow'!M172", "values": [["=SUM(M174:M211)"]]},
        {"range": "'Channel Detail Flow'!M173", "values": [["=M172-L172"]]},
    ]
    # Thêm SUMPRODUCT cho từng kênh
    for r in range(9, 47):
        c_m_updates.append({"range": f"'Channel Detail Flow'!M{r}", "values": [[f"=SUMPRODUCT(('MTD Pivot'!$B$3:$B$400=$B{r})*('MTD Pivot'!$C$3:$C$400=$A$7)*('MTD Pivot'!$D$2:$K$2=M$2)*'MTD Pivot'!$D$3:$K$400)"]]})
    for r in range(50, 88):
        c_m_updates.append({"range": f"'Channel Detail Flow'!M{r}", "values": [[f"=SUMPRODUCT(('MTD Pivot'!$B$3:$B$400=$B{r})*('MTD Pivot'!$C$3:$C$400=$A$48)*('MTD Pivot'!$D$2:$K$2=M$2)*'MTD Pivot'!$D$3:$K$400)"]]})
    for r in range(91, 129):
        c_m_updates.append({"range": f"'Channel Detail Flow'!M{r}", "values": [[f"=SUMPRODUCT(('MTD Pivot'!$B$3:$B$400=$B{r})*('MTD Pivot'!$C$3:$C$400=$A$89)*('MTD Pivot'!$D$2:$K$2=M$2)*'MTD Pivot'!$D$3:$K$400)"]]})
    for r in range(132, 170):
        c_m_updates.append({"range": f"'Channel Detail Flow'!M{r}", "values": [[f"=SUMPRODUCT(('MTD Pivot'!$B$3:$B$400=$B{r})*('MTD Pivot'!$C$3:$C$400=$A$130)*('MTD Pivot'!$D$2:$K$2=M$2)*'MTD Pivot'!$D$3:$K$400)"]]})
    for r in range(174, 212):
        c_m_updates.append({"range": f"'Channel Detail Flow'!M{r}", "values": [[f"=SUMPRODUCT(('MTD Pivot'!$B$3:$B$400=$B{r})*('MTD Pivot'!$C$3:$C$400=$A$172)*('MTD Pivot'!$D$2:$K$2=M$2)*'MTD Pivot'!$D$3:$K$400)"]]})
    updates.extend(c_m_updates)

    # 4. Ghi batchUpdate lên Google Sheets API
    print(f"\n[4/5] Đang đẩy {len(updates)} dải ô lên Google Sheets qua Sheets API...")
    url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values:batchUpdate"
    payload = {
        "valueInputOption": "USER_ENTERED",
        "data": updates
    }
    req_batch = urllib.request.Request(
        url_batch,
        data=json.dumps(payload).encode("utf-8"),
        headers=sheets_headers,
        method="POST"
    )
    with urllib.request.urlopen(req_batch) as resp:
        res_data = json.loads(resp.read().decode())
        print(f"  ✓ Đã cập nhật thành công {res_data.get('totalUpdatedCells', 0)} ô trên Google Sheets!")

    # 5. Patch file Excel SSOT cục bộ
    print(f"\n[5/5] Cập nhật bản sao Excel SSOT cục bộ...")
    local_excel = BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"
    if local_excel.exists():
        import openpyxl
        wb = openpyxl.load_workbook(local_excel)
        if "MTD Pivot" in wb.sheetnames:
            ws_m = wb["MTD Pivot"]
            for r_idx, row_vals in enumerate(new_pivot_data):
                for c_idx, val in enumerate(row_vals):
                    ws_m.cell(r_idx + 1, c_idx + 1, val)
        wb.save(local_excel)
        print(f"  ✓ Đã lưu cập nhật MTD Pivot vào {local_excel}")

    print("\n" + "=" * 75)
    print(f"HOÀN TẤT ĐỒNG BỘ TOÀN BỘ CÁC THÁNG (T5 -> T11) THEO CHU KỲ MTD {days_elapsed} NGÀY!")
    print(f"Google Sheets SSOT: https://docs.google.com/spreadsheets/d/{TARGET_SHEET_ID}/edit?gid=1273714888#gid=1273714888")
    print("=" * 75)

if __name__ == "__main__":
    sync_all_mtd(days_elapsed=2)

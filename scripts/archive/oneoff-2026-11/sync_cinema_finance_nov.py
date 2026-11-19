"""
scripts/sync_cinema_finance_nov.py
=============================================================================
Đồng bộ số tháng 11 cho sheet 'Cinema' và 'Financial' trên:
  1. Google Sheets SSOT (Spreadsheet ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU)
     - Sheet 'Cinema' (gid: 90960373)
     - Sheet 'Financial' (gid: 667003442)
  2. Local Excel SSOT (07_REPORTS/web_performance_tracking.xlsx)
=============================================================================
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
import openpyxl

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID

SPREADSHEET_ID = TARGET_SHEET_ID
LOCAL_EXCEL_PATH = Path(__file__).resolve().parent.parent / "07_REPORTS" / "web_performance_tracking.xlsx"


def build_cinema_updates():
    """Xây dựng toàn bộ cập nhật công thức tháng 11 cho sheet Cinema."""
    updates = []
    
    # Col I: Nov MTD
    # Col J: VS. SPLM (=I - H)
    # Col S: VS. LM (=R - Q)
    
    # Row 3..5: Summary
    updates.append({"range": "Cinema!I3", "values": [["=SUM(I8,I15,I22,I29,I36,I43)"]]})
    updates.append({"range": "Cinema!I4", "values": [["=I3-H3"]]})
    updates.append({"range": "Cinema!I5", "values": [["=(I3/H3)-1"]]})
    
    updates.append({"range": "Cinema!J3", "values": [["=I3-H3"]]})
    updates.append({"range": "Cinema!J4", "values": [["=I4-H4"]]})
    updates.append({"range": "Cinema!J5", "values": [["=I5-H5"]]})
    
    updates.append({"range": "Cinema!S3", "values": [["=R3-Q3"]]})
    updates.append({"range": "Cinema!S4", "values": [["=R4-Q4"]]})
    updates.append({"range": "Cinema!S5", "values": [["=R5-Q5"]]})
    
    # Sections in Cinema:
    # 1. Row 8-13: Trang Rạp phim (Cinema_Cineplex Page)
    # 2. Row 15-20: Trang phim chi tiết (Cinema_Page)
    # 3. Row 22-27: Blog Phim (Cinema_Blog)
    # 4. Row 29-34: Trang chủ Cinema (Cinema_Home Page)
    # 5. Row 36-41: Tin tức (Cinema_News)
    # 6. Row 43-47: Landing Page (Cinema_Landing Page)
    sections = [
        (8, 9, 13, "Cinema_Cineplex Page"),
        (15, 16, 20, "Cinema_Page"),
        (22, 23, 27, "Cinema_Blog"),
        (29, 30, 34, "Cinema_Home Page"),
        (36, 37, 41, "Cinema_News"),
        (43, 44, 47, "Cinema_Landing Page"),
    ]
    
    for head_r, start_r, end_r, proj_name in sections:
        # Header sum
        updates.append({"range": f"Cinema!I{head_r}", "values": [[f"=sum(I{start_r}:I{end_r})"]]})
        updates.append({"range": f"Cinema!J{head_r}", "values": [[f"=I{head_r}-H{head_r}"]]})
        updates.append({"range": f"Cinema!S{head_r}", "values": [[f"=R{head_r}-Q{head_r}"]]})
        
        # Channels
        for r in range(start_r, end_r + 1):
            f_mtd = f"=SUMIFS('MTD Pivot'!J:J, 'MTD Pivot'!$A:$A, \"{proj_name}\", 'MTD Pivot'!$C:$C, $B{r})"
            updates.append({"range": f"Cinema!I{r}", "values": [[f_mtd]]})
            updates.append({"range": f"Cinema!J{r}", "values": [[f"=I{r}-H{r}"]]})
            updates.append({"range": f"Cinema!S{r}", "values": [[f"=R{r}-Q{r}"]]})
            
    return updates


def build_financial_updates():
    """Xây dựng toàn bộ cập nhật công thức và số liệu tháng 11 cho sheet Financial."""
    updates = []
    
    # Col I: Nov MTD
    # Col J: VS. SPLM (=I - H)
    # Col R: Nov Full Month
    # Col S: VS. LM (=R - Q)
    
    # Row 3..6: Summary
    updates.append({"range": "Financial!I3", "values": [["=sum(I8,I15,I22,I29,I36,I43,I50,I57,I64,I71,I78,I85,I91,I98,I105,I112,I119,I126,I133)"]]})
    updates.append({"range": "Financial!I4", "values": [["=I3-H3"]]})
    updates.append({"range": "Financial!I5", "values": [["=(I3/H3)-1"]]})
    
    updates.append({"range": "Financial!R3", "values": [["=sum(R8,R15,R22,R29,R36,R43,R50,R57,R64,R71,R78,R85,R91,R98,R105,R112,R119,R126,R133)"]]})
    updates.append({"range": "Financial!R4", "values": [["=R3-Q3"]]})
    updates.append({"range": "Financial!R5", "values": [["=IFERROR((R3/Q3)-1, 0)"]]})
    updates.append({"range": "Financial!R6", "values": [["=R3/R2"]]})
    
    updates.append({"range": "Financial!J3", "values": [["=I3-H3"]]})
    updates.append({"range": "Financial!J4", "values": [["=I4-H4"]]})
    updates.append({"range": "Financial!J5", "values": [["=I5-H5"]]})
    
    updates.append({"range": "Financial!S3", "values": [["=R3-Q3"]]})
    updates.append({"range": "Financial!S4", "values": [["=R4-Q4"]]})
    updates.append({"range": "Financial!S5", "values": [["=R5-Q5"]]})
    
    # 13 sections with SUMIFS to Pivot
    pivot_sections = [
        (8, 9, 13, "Trung Tâm Tài Chính"),
        (15, 16, 20, "Vay Nhanh"),
        (22, 23, 27, "Điểm Tín Dụng"),
        (29, 30, 34, "Ví Trả Sau"),
        (36, 37, 41, "Túi Thần Tài"),
        (43, 44, 48, "Mở Thẻ Tín Dụng"),
        (50, 51, 55, "Trả Góp Apple"),
        (57, 58, 62, "Chứng Khoán"),
        (64, 65, 69, "Tiết Kiệm Online"),
        (71, 72, 76, "Thanh Toán Thẻ Tín Dụng"),
        (78, 79, 83, "Chứng Chỉ Quỹ"),
        (85, 86, 90, "Sàn đầu tư"),
        (91, 92, 96, "Tiệm Vàng Online"),
    ]
    
    for head_r, start_r, end_r, proj_name in pivot_sections:
        # Header sums
        updates.append({"range": f"Financial!I{head_r}", "values": [[f"=sum(I{start_r}:I{end_r})"]]})
        updates.append({"range": f"Financial!R{head_r}", "values": [[f"=sum(R{start_r}:R{end_r})"]]})
        updates.append({"range": f"Financial!J{head_r}", "values": [[f"=I{head_r}-H{head_r}"]]})
        updates.append({"range": f"Financial!S{head_r}", "values": [[f"=R{head_r}-Q{head_r}"]]})
        
        # Channels
        for r in range(start_r, end_r + 1):
            f_mtd = f"=SUMIFS('MTD Pivot'!J:J, 'MTD Pivot'!$A:$A, \"{proj_name}\", 'MTD Pivot'!$C:$C, $B{r})"
            f_full = f"=SUMIFS('Full month Pivot'!J:J, 'Full month Pivot'!$A:$A, \"{proj_name}\", 'Full month Pivot'!$C:$C, $B{r})"
            updates.append({"range": f"Financial!I{r}", "values": [[f_mtd]]})
            updates.append({"range": f"Financial!R{r}", "values": [[f_full]]})
            updates.append({"range": f"Financial!J{r}", "values": [[f"=I{r}-H{r}"]]})
            updates.append({"range": f"Financial!S{r}", "values": [[f"=R{r}-Q{r}"]]})
            
    # 6 feature sections with specific GA4 traffic values (matching historical tracking method)
    # Order of channels in each section: Organic, Direct, Paid, Referral, Others
    feature_sections = [
        # (head_r, start_r, end_r, name, [Organic, Direct, Paid, Referral, Others])
        (98, 99, 103, "Tỷ Giá (FX Rates)", [1780, 59, 0, 13, 8]),
        (105, 106, 110, "Giá Vàng (Gold Price)", [200, 25, 0, 0, 35]),
        (112, 113, 117, "Lãi Suất (Interest Rates)", [302, 30, 0, 17, 24]),
        (119, 120, 124, "Nhận Tiền Quốc Tế", [171, 32, 5, 4, 27]),
        (126, 127, 131, "Quỹ Nhóm", [470, 373, 499, 21, 20]),
        (133, 134, 138, "Quản Lý Chi Tiêu", [206, 46, 0, 9, 16]),
    ]
    
    for head_r, start_r, end_r, feat_name, vals in feature_sections:
        # Header sums
        updates.append({"range": f"Financial!I{head_r}", "values": [[f"=sum(I{start_r}:I{end_r})"]]})
        updates.append({"range": f"Financial!R{head_r}", "values": [[f"=sum(R{start_r}:R{end_r})"]]})
        updates.append({"range": f"Financial!J{head_r}", "values": [[f"=I{head_r}-H{head_r}"]]})
        updates.append({"range": f"Financial!S{head_r}", "values": [[f"=R{head_r}-Q{head_r}"]]})
        
        # Channels
        for idx, val in enumerate(vals):
            r = start_r + idx
            updates.append({"range": f"Financial!I{r}", "values": [[val]]})
            updates.append({"range": f"Financial!R{r}", "values": [[val]]})
            updates.append({"range": f"Financial!J{r}", "values": [[f"=I{r}-H{r}"]]})
            updates.append({"range": f"Financial!S{r}", "values": [[f"=R{r}-Q{r}"]]})
            
    return updates


def execute_batch_update(token, updates):
    """Gửi batchUpdate values lên Google Sheets."""
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values:batchUpdate"
    body = {
        "valueInputOption": "USER_ENTERED",
        "data": updates
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    return res


def update_local_excel(cinema_updates, financial_updates):
    """Cập nhật bản sao Excel SSOT cục bộ."""
    if not LOCAL_EXCEL_PATH.exists():
        print(f"Không tìm thấy local Excel: {LOCAL_EXCEL_PATH}")
        return
        
    print(f"Đang đồng bộ vào local Excel: {LOCAL_EXCEL_PATH}...")
    wb = openpyxl.load_workbook(LOCAL_EXCEL_PATH, data_only=False)
    
    for u in cinema_updates + financial_updates:
        rng = u["range"]
        sheet_name, cell_ref = rng.split("!")
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            val = u["values"][0][0]
            ws[cell_ref] = val
            
    wb.save(LOCAL_EXCEL_PATH)
    print("✓ Đã lưu thành công local Excel SSOT!")


def main():
    print("===========================================================================")
    print("BỔ SUNG SỐ THÁNG 11 CHO SHEET CINEMA & FINANCIAL")
    print("===========================================================================")
    
    token = get_sheets_token()
    print("1. Đang xây dựng danh sách công thức & số liệu...")
    cinema_updates = build_cinema_updates()
    financial_updates = build_financial_updates()
    
    total_cells = len(cinema_updates) + len(financial_updates)
    print(f"  - Cinema updates   : {len(cinema_updates)} cells")
    print(f"  - Financial updates: {len(financial_updates)} cells")
    print(f"  - Tổng cộng        : {total_cells} cells")
    
    print("\n2. Đang gửi dữ liệu lên Google Sheets SSOT...")
    all_updates = cinema_updates + financial_updates
    res = execute_batch_update(token, all_updates)
    print(f"✓ Đã cập nhật thành công {res.get('totalUpdatedCells', 0)} cells trên Google Sheets!")
    
    print("\n3. Đang cập nhật Excel SSOT cục bộ...")
    update_local_excel(cinema_updates, financial_updates)
    
    print("\n===========================================================================")
    print("HOÀN TẤT ĐỒNG BỘ THÁNG 11 CHO CINEMA VÀ FINANCIAL!")
    print("===========================================================================")


if __name__ == "__main__":
    main()

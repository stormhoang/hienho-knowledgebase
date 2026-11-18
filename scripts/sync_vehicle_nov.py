"""
scripts/sync_vehicle_nov.py
=============================================================================
Đồng bộ số tháng 11 cho sheet 'Vehicle' trên:
  1. Google Sheets SSOT (Spreadsheet ID: 1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU)
     - Sheet 'Vehicle' (gid: 2112931090)
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
LOCAL_EXCEL_PATH = ROOT_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"


def build_vehicle_updates():
    """Xây dựng toàn bộ cập nhật công thức và số liệu tháng 11 cho sheet Vehicle."""
    updates = []
    
    # Header B1
    updates.append({"range": "Vehicle!B1", "values": [["Update to: 9"]]})
    
    # Summary rows: Row 2..4
    updates.append({"range": "Vehicle!I2", "values": [["=sum(I6,I13,I20,I27,I34,I41,I48,I55,I62,I69)"]]})
    updates.append({"range": "Vehicle!I3", "values": [["=I2-H2"]]})
    updates.append({"range": "Vehicle!I4", "values": [["=(I2/H2)-1"]]})
    
    updates.append({"range": "Vehicle!R2", "values": [["=sum(R6,R13,R20,R27,R34,R41,R48,R55,R62,R69)"]]})
    updates.append({"range": "Vehicle!R3", "values": [["=R2-Q2"]]})
    updates.append({"range": "Vehicle!R4", "values": [["=IFERROR((R2/Q2)-1, 0)"]]})
    
    updates.append({"range": "Vehicle!J2", "values": [["=I2-H2"]]})
    updates.append({"range": "Vehicle!J3", "values": [["=I3-H3"]]})
    updates.append({"range": "Vehicle!J4", "values": [["=I4-H4"]]})
    
    updates.append({"range": "Vehicle!S2", "values": [["=R2-Q2"]]})
    updates.append({"range": "Vehicle!S3", "values": [["=R3-Q3"]]})
    updates.append({"range": "Vehicle!S4", "values": [["=R4-Q4"]]})
    
    # 5 sections with SUMIFS to Pivot
    # (head_r, start_r, end_r, proj_name)
    pivot_sections = [
        (6, 7, 11, "Tiện Ích Giao Thông"),
        (48, 49, 53, "Phạt Nguội"),
        (55, 56, 60, "Bảo Hiểm Ô Tô"),
        (62, 63, 67, "Bảo Hiểm Xe Máy"),
        (69, 70, 74, "Phí Không Dừng"),
    ]
    
    for head_r, start_r, end_r, proj_name in pivot_sections:
        # Header sums
        updates.append({"range": f"Vehicle!I{head_r}", "values": [[f"=sum(I{start_r}:I{end_r})"]]})
        updates.append({"range": f"Vehicle!R{head_r}", "values": [[f"=sum(R{start_r}:R{end_r})"]]})
        updates.append({"range": f"Vehicle!J{head_r}", "values": [[f"=I{head_r}-H{head_r}"]]})
        updates.append({"range": f"Vehicle!S{head_r}", "values": [[f"=R{head_r}-Q{head_r}"]]})
        
        # Channels
        for r in range(start_r, end_r + 1):
            f_mtd = f"=SUMIFS('MTD Pivot'!J:J, 'MTD Pivot'!$A:$A, \"{proj_name}\", 'MTD Pivot'!$C:$C, $B{r})"
            f_full = f"=SUMIFS('Full month Pivot'!J:J, 'Full month Pivot'!$A:$A, \"{proj_name}\", 'Full month Pivot'!$C:$C, $B{r})"
            updates.append({"range": f"Vehicle!I{r}", "values": [[f_mtd]]})
            updates.append({"range": f"Vehicle!R{r}", "values": [[f_full]]})
            updates.append({"range": f"Vehicle!J{r}", "values": [[f"=I{r}-H{r}"]]})
            updates.append({"range": f"Vehicle!S{r}", "values": [[f"=R{r}-Q{r}"]]})
            
    # 5 feature sections with specific GA4 traffic values (Nov 1-9)
    # Order of channels in each section: Organic, Direct, Paid, Referral, Others
    feature_sections = [
        # (head_r, start_r, end_r, name, [Organic, Direct, Paid, Referral, Others])
        (13, 14, 18, "Giá Xăng", [1273, 30, 0, 3, 7]),
        (20, 21, 25, "Garage", [40, 8, 0, 0, 4]),
        (27, 28, 32, "Cây Xăng", [160, 14, 0, 0, 9]),
        (34, 35, 39, "Trạm Sạc", [0, 0, 0, 0, 0]),
        (41, 42, 46, "Hãng Xe (VinFast)", [3, 0, 0, 0, 3]),
    ]
    
    for head_r, start_r, end_r, feat_name, vals in feature_sections:
        # Header sums
        updates.append({"range": f"Vehicle!I{head_r}", "values": [[f"=sum(I{start_r}:I{end_r})"]]})
        updates.append({"range": f"Vehicle!R{head_r}", "values": [[f"=sum(R{start_r}:R{end_r})"]]})
        updates.append({"range": f"Vehicle!J{head_r}", "values": [[f"=I{head_r}-H{head_r}"]]})
        updates.append({"range": f"Vehicle!S{head_r}", "values": [[f"=R{head_r}-Q{head_r}"]]})
        
        # Channels
        for idx, val in enumerate(vals):
            r = start_r + idx
            updates.append({"range": f"Vehicle!I{r}", "values": [[val]]})
            updates.append({"range": f"Vehicle!R{r}", "values": [[val]]})
            updates.append({"range": f"Vehicle!J{r}", "values": [[f"=I{r}-H{r}"]]})
            updates.append({"range": f"Vehicle!S{r}", "values": [[f"=R{r}-Q{r}"]]})
            
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


def update_local_excel(vehicle_updates):
    """Cập nhật bản sao Excel SSOT cục bộ."""
    if not LOCAL_EXCEL_PATH.exists():
        print(f"Không tìm thấy local Excel: {LOCAL_EXCEL_PATH}")
        return
        
    print(f"Đang đồng bộ vào local Excel: {LOCAL_EXCEL_PATH}...")
    wb = openpyxl.load_workbook(LOCAL_EXCEL_PATH, data_only=False)
    
    if "Vehicle" in wb.sheetnames:
        ws = wb["Vehicle"]
        for u in vehicle_updates:
            rng = u["range"]
            sheet_name, cell_ref = rng.split("!")
            val = u["values"][0][0]
            ws[cell_ref] = val
            
    wb.save(LOCAL_EXCEL_PATH)
    print("✓ Đã lưu thành công local Excel SSOT!")


def main():
    print("===========================================================================")
    print("BỔ SUNG SỐ THÁNG 11 CHO SHEET VEHICLE")
    print("===========================================================================")
    
    token = get_sheets_token()
    print("1. Đang xây dựng danh sách công thức & số liệu...")
    vehicle_updates = build_vehicle_updates()
    
    print(f"  - Vehicle updates : {len(vehicle_updates)} cells")
    
    print("\n2. Đang gửi dữ liệu lên Google Sheets SSOT...")
    res = execute_batch_update(token, vehicle_updates)
    print(f"✓ Đã cập nhật thành công {res.get('totalUpdatedCells', 0)} cells trên Google Sheets!")
    
    print("\n3. Đang cập nhật Excel SSOT cục bộ...")
    update_local_excel(vehicle_updates)
    
    print("\n===========================================================================")
    print("HOÀN TẤT ĐỒNG BỘ THÁNG 11 CHO SHEET VEHICLE!")
    print("===========================================================================")


if __name__ == "__main__":
    main()

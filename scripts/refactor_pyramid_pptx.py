#!/usr/bin/env python3
"""
Refactor and finalize Web_Platform_Thang_10_2026_Pyramid.pptx
Pixel-perfect polish:
1. Remove all 'Mục đích: ...' template instruction sentences across all slides.
2. Remove 'AppsFlyer GPD' from all footer source strings.
3. Remove Slide 4 (Paid Ads discussion), Slide 5 (Pilot Off-Page SEO 125M) and Slide 6 (Follow-up placeholder).
4. Put Luồng Tải App (/tai-app) 10K search volume as Proposal 1 in Slide 4 with zero overlap.
5. Replace Slide 9 with New User Flow (remove Paid landing pages table, clean commentary).
6. Clean Slide 8 (Hubs breakdown): remove Phạt Nguội and financial target text completely.
"""
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

BASE_DIR = Path("/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base")
PPTX_PATH = BASE_DIR / "07_REPORTS" / "docs" / "presentations" / "Web_Platform_Thang_10_2026_Pyramid.pptx"

COLOR_TEXT_MAIN = RGBColor(0x1C, 0x17, 0x1A)
COLOR_TEXT_MUTED = RGBColor(0x5C, 0x50, 0x60)
COLOR_GREEN = RGBColor(0x05, 0x96, 0x69)
COLOR_MAGENTA = RGBColor(0xA5, 0x00, 0x64)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def set_text(shape, text, font_size=None, bold=None, color=None, align=None):
    if not shape.has_text_frame:
        return
    tf = shape.text_frame
    tf.word_wrap = True
    for p in tf.paragraphs:
        p.text = ""
    p = tf.paragraphs[0]
    p.text = text
    if align:
        p.alignment = align
    if font_size or bold is not None or color:
        for run in p.runs:
            if font_size:
                run.font.size = Pt(font_size)
            if bold is not None:
                run.font.bold = bold
            if color:
                run.font.color.rgb = color

def set_cell(cell, text, font_size=8.5, bold=False, color=None, align=PP_ALIGN.LEFT):
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.text = str(text)
    p.alignment = align
    for run in p.runs:
        run.font.size = Pt(font_size)
        run.font.bold = bold
        if color:
            run.font.color.rgb = color

def delete_slide(prs, index):
    rId = prs.slides._sldIdLst[index].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[index]

def main():
    prs = Presentation(str(PPTX_PATH))
    TOTAL = len(prs.slides)
    print(f"Current slides count: {TOTAL}")

    # 1. Slide 0: Cover
    s0 = prs.slides[0]
    for sh in s0.shapes:
        if sh.has_text_frame:
            txt = sh.text_frame.text
            if "Mục đích:" in txt:
                sh.text_frame.text = ""
            elif "AppsFlyer" in txt or "Nguồn:" in txt or "Kỳ dữ liệu" in txt:
                sh.text_frame.text = "Kỳ dữ liệu 01/10 - 31/10/2026 (31 ngày, full month)"

    # 2. Slide 1: Executive Summary
    s1 = prs.slides[1]
    set_text(s1.shapes[0], "Tháng 10 Đạt 98,3% Kế Hoạch Nhờ Kênh Tự Nhiên Tăng +13,5% MoM; Tập Trung Tối Ưu Luồng Tải App 10.000 Tìm Kiếm", font_size=15.5, bold=True, color=COLOR_TEXT_MAIN)
    s1.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    set_text(s1.shapes[6], "Kết luận điều hành\nKênh tự nhiên (Non-Paid) là động lực tăng trưởng cốt lõi của Web Platform trong tháng 10 với 3.128.542 PVs (+13,5% MoM, chiếm 86,9% toàn sàn), tự bù đắp phần lớn lượng suy giảm do BU cắt giảm Paid Ads. Dự án New User xác lập kỷ lục 2.389 khách hàng liên kết ngân hàng (+5,0% MoM). Trọng tâm tháng 11 là chuẩn hóa luồng Tải App (/tai-app) để đón trọn 10.000 volume tìm kiếm thương hiệu.", font_size=9.5, color=COLOR_WHITE)
    set_text(s1.shapes[7], "1. Non-Paid tăng 13,5%, chiếm 86,9% lưu lượng\n- 3.128.542 PVs, tăng 372.776 PVs so với tháng 9.\n- Direct +23,3%, Referral/Others +27,9%, Organic +5,7%.\n- Tự bù đắp hơn 51% lượng suy giảm do BU cắt giảm 723K Paid Ads.", font_size=9.0, color=COLOR_TEXT_MAIN)
    set_text(s1.shapes[8], "2. Dự án New User lập kỷ lục 2.389 Map Bank (+5,0% MoM)\n- 11.143 App Installs (+6,1% MoM), nhịp chạy 359,5 lượt tải/ngày.\n- 3.902 Đăng Ký (35,0% CVR) và 2.389 Liên Kết Ngân Hàng (61,2% CVR).\n- Nguồn kéo chủ lực: Banner Ads C.CHAOMOMO (8.517 installs), Cinema Hub (1.931 installs, CVR 15,2%) và Minigame Một Mùa Quýt (7.097 active players).", font_size=9.0, color=COLOR_TEXT_MAIN)
    set_text(s1.shapes[9], "3. Cinema Hub vượt 101,4% Target, Financial bước đầu tích cực\n- Cinema Hub đạt 1.132.721 PVs (101,4% Target), Organic đạt 86,4% tự bù cho phim lẻ sau khi cắt 93% Paid.\n- Financial Hub đạt 273.705 PVs (+9,6% MoM), Trung tâm tài chính +442% nhờ cụm công cụ tỷ giá live.\n- Toàn sàn đón 1,24M New Users tự nhiên ghé thăm website.", font_size=9.0, color=COLOR_TEXT_MAIN)
    set_text(s1.shapes[10], "Điểm nổi bật\n- Toàn sàn đạt 3.602.023 PVs (98,3% Target); kênh tự nhiên tăng +13,5% MoM tự bù đắp 51% lượng Paid Ads sụt giảm.\n- Dự án New User lập kỷ lục lịch sử 2.389 Map Bank (+5,0% MoM); Cinema Hub hoàn thành xuất sắc 101,4% Target.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s1.shapes[11], "Cần theo dõi & Trọng tâm tháng 11\n- Paid Ads giảm 60,4% (-723K PVs) do BU cắt giảm chi phí -> Tiếp tục đẩy mạnh các sản phẩm tự nhiên để duy trì nhịp tăng trưởng.\n- Hoàn tất rà soát công thức Thuế TNCN với Pháp chế & Kế toán trước 10/11 để go-live đúng hạn.", font_size=8.5, color=COLOR_TEXT_MAIN)

    # 3. Slide 2: Discussion Topics
    s2 = prs.slides[2]
    set_text(s2.shapes[0], "Discussion Topics — 1 Chủ Đề Trọng Tâm: 0 Discuss, 1 Approve", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    s2.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    tbl2 = s2.shapes[6].table
    set_cell(tbl2.cell(1, 0), "1", align=PP_ALIGN.CENTER, bold=True)
    set_cell(tbl2.cell(1, 1), "Tối Ưu Luồng Tải App (/tai-app) Chiếm Lĩnh 10.000 Volume Tìm Kiếm Tự Nhiên", bold=True)
    set_cell(tbl2.cell(1, 2), "Approve", align=PP_ALIGN.CENTER, bold=True, color=COLOR_MAGENTA)
    set_cell(tbl2.cell(1, 3), "Phê duyệt cơ chế hợp nhất URL (/download -> /tai-app) và đồng bộ hệ thống liên kết nội bộ (Header/Footer/Top Bar) trên toàn bộ Web Platform trỏ về trang Tải App chính thức.")
    set_cell(tbl2.cell(1, 4), "Thu hút trọn vẹn 10.000 volume search/tháng cho cụm từ khóa 'tải app MoMo'; bảo vệ an toàn thương hiệu, ngăn chặn thất thoát vào các nguồn APK giả mạo.", color=COLOR_GREEN)
    set_cell(tbl2.cell(1, 5), "31/10", align=PP_ALIGN.CENTER, bold=True)
    set_cell(tbl2.cell(1, 6), "CAO", align=PP_ALIGN.CENTER, bold=True, color=COLOR_MAGENTA)
    set_cell(tbl2.cell(1, 7), "Slide 4", align=PP_ALIGN.CENTER, bold=True, color=COLOR_MAGENTA)
    set_text(s2.shapes[7], "Lưu ý\nChủ đề Approve duy nhất nhằm kịp lập chỉ mục Google và kích hoạt trọn vẹn luồng chuyển đổi người dùng trong tháng 11/2026. Web Platform tập trung tối ưu năng lực Organic và bảo vệ an toàn thương hiệu MoMo.", font_size=9.0, color=COLOR_TEXT_MAIN)

    # 4. Slide 3: Proposal 1 Deep-Dive
    s3 = prs.slides[3]
    set_text(s3.shapes[0], "Đề Xuất 1: Xây Dựng Luồng Tải App Chuẩn Hóa, Acquire 10.000 Volume Search 'Tải App MoMo'", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    s3.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    # Fit text so it doesn't overlap table:
    set_text(s3.shapes[6], "Problem statement & Bối cảnh\n• Nhu cầu tìm kiếm 'tải momo', 'cài đặt momo' đạt 10.000 lượt search/tháng. Lưu lượng đang bị phân tán vào APK ngoài hoặc landing page cũ.\n• Kỹ sư đã nghiệm thu trang /tai-app trên Production tích hợp Smart Device Routing (iOS mở App Store, Android mở Play Store, Desktop hiện QR Code). Cần quy tụ link toàn sàn.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[7], "Tác động dự kiến\n• Thu hút trọn vẹn 10.000 volume tìm kiếm tự nhiên/tháng vào trang chính chủ MoMo.\n• Bảo vệ an toàn thương hiệu: Ngăn ngừa rủi ro người dùng tải nhầm file APK giả mạo chứa mã độc.\n• Chi phí phát sinh: 0 VNĐ (tận dụng 100% tính năng và hạ tầng kỹ thuật đã build sẵn trên Production).", font_size=8.5, color=COLOR_TEXT_MAIN)
    tbl3 = s3.shapes[8].table
    set_cell(tbl3.cell(0, 0), "Phương án", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(0, 1), "Nội dung triển khai", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(0, 2), "Tác động lượng hóa & Lợi ích", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(0, 3), "Đánh giá rủi ro", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(1, 0), "Phương Án A (Khuyến nghị)", bold=True, color=COLOR_GREEN)
    set_cell(tbl3.cell(1, 1), "Hợp nhất các link tải cũ về /tai-app; tối ưu Schema SoftwareApplication chuẩn SEO Top 1; đồng bộ nút Tải App trên Header/Footer toàn sàn.")
    set_cell(tbl3.cell(1, 2), "Acquire 10.000 volume search/tháng; trải nghiệm 1-chạm tải app theo thiết bị; chi phí phát sinh 0 VNĐ.", color=COLOR_GREEN)
    set_cell(tbl3.cell(1, 3), "Rủi ro thấp: Trang /tai-app đã nghiệm thu Production, chỉ cần đồng bộ liên kết.")
    set_cell(tbl3.cell(2, 0), "Phương Án B (Hiện trạng)", bold=True)
    set_cell(tbl3.cell(2, 1), "Giữ nguyên các trang rải rác (/download, bài blog cũ) không có cơ chế Smart Device Routing thống nhất.")
    set_cell(tbl3.cell(2, 2), "Thất thoát 10.000 lượt search vào tay các trang download APK của bên thứ ba; trải nghiệm người dùng bị đứt gãy trên Desktop.", color=COLOR_MAGENTA)
    set_cell(tbl3.cell(2, 3), "Rủi ro cao: Nguy cơ bảo mật cho người dùng khi tải file nguồn không chính thống bên ngoài.")
    set_text(s3.shapes[9], "Đề nghị với CEO/BOM: Approve phương án A. Khuyến nghị BU: thông qua phương án A để kích hoạt chuyển đổi.\nNếu không quyết định: Tiếp tục để mất 10.000 lượt tìm kiếm mỗi tháng vào các trang trung gian tải APK ngoài, tăng nguy cơ rủi ro bảo mật thương hiệu.", font_size=8.5, color=COLOR_TEXT_MAIN)

    # 5. Slide 4: Tổng lượt xem (Slide 5 of deck)
    s4 = prs.slides[4]
    s4.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    set_text(s4.shapes[0], "Kênh Tự Nhiên Đạt 3.128.542 PVs (+13,5% MoM), Vượt 109,2% Kế Hoạch; Toàn Sàn Đạt 98,3% Do BU Cắt 723K Paid Ads", font_size=15.0, bold=True, color=COLOR_TEXT_MAIN)
    
    # Table shape 7: Clean channels breakdown
    tbl4_2 = s4.shapes[7].table
    set_cell(tbl4_2.cell(0, 0), "Kênh", bold=True, color=COLOR_WHITE)
    set_cell(tbl4_2.cell(0, 1), "T9 (Actual)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl4_2.cell(0, 2), "T10 (Target)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl4_2.cell(0, 3), "T10 (Actual)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl4_2.cell(0, 4), "% MoM", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl4_2.cell(0, 5), "% Target", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    
    channel_rows = [
        ("Non-Paid (Tự nhiên)", "2.755.766", "2.865.064", "3.128.542", "+13,5%", "109,2%", True, COLOR_GREEN),
        ("   Organic Search", "1.623.796", "1.566.630", "1.715.771", "+5,7%", "109,5%", False, COLOR_GREEN),
        ("   Direct", "755.896", "860.199", "931.731", "+23,3%", "108,3%", False, COLOR_GREEN),
        ("   Referral / Others", "376.074", "438.235", "481.040", "+27,9%", "109,8%", False, COLOR_GREEN),
        ("Paid Media", "1.197.093", "419.221", "473.481", "-60,4%", "112,9%", True, COLOR_TEXT_MUTED),
        ("Tổng Toàn Sàn", "3.952.859", "3.665.607", "3.602.023", "-8,9%", "98,3%", True, COLOR_TEXT_MAIN),
    ]
    for r_idx, (ch, t9, tgt, t10, mom, pct_tgt, is_bold, val_col) in enumerate(channel_rows, 1):
        set_cell(tbl4_2.cell(r_idx, 0), ch, bold=is_bold)
        set_cell(tbl4_2.cell(r_idx, 1), t9, align=PP_ALIGN.RIGHT, bold=is_bold)
        set_cell(tbl4_2.cell(r_idx, 2), tgt, align=PP_ALIGN.RIGHT, bold=is_bold)
        set_cell(tbl4_2.cell(r_idx, 3), t10, align=PP_ALIGN.RIGHT, bold=is_bold)
        set_cell(tbl4_2.cell(r_idx, 4), mom, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col if is_bold else None)
        set_cell(tbl4_2.cell(r_idx, 5), pct_tgt, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col)

    set_text(s4.shapes[8], "Nhận định & Hành động tiếp theo\n- Động lực tự nhiên vững chắc: Cả 3 kênh tự nhiên (Organic, Direct, Referral) đều tăng trưởng mạnh và vượt từ 108% - 109% chỉ tiêu kế hoạch. Direct tăng +23,3% phản ánh uy tín thương hiệu MoMo ngày càng vững chắc.\n- Tự bù đắp khoảng trống Paid Ads: Kênh Non-Paid tăng thêm +372.776 PVs (+13,5% MoM), bù đắp được hơn 51% lượng suy giảm do BU chủ động cắt giảm 60,4% ngân sách Paid Ads (-723.612 PVs toàn Web).\n- Trọng tâm tháng 11: Chuẩn hóa luồng Tải App (/tai-app) để thu hút 10.000 volume tìm kiếm tự nhiên, tiếp tục mở rộng các Hub cốt lõi (Cinema, Financial) để duy trì nhịp tăng trưởng nội sinh độc lập với Paid Media.", font_size=8.5, color=COLOR_TEXT_MAIN)
    s4.shapes[9].text_frame.text = "" # Clear duplicate bottom note

    # 6. Slide 5: Dự Án New User & Phễu Chuyển Đổi (Slide 6 of deck)
    s5 = prs.slides[5]
    set_text(s5.shapes[0], "Dự Án New User Xác Lập Kỷ Lục 2.389 Khách Hàng Map Bank (+5,0% MoM); Dẫn Dắt Bởi 11.143 App Installs Từ Ads Banner & Minigame Một Mùa Quýt", font_size=15.0, bold=True, color=COLOR_TEXT_MAIN)
    s5.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    
    # Left table title & table (Funnel)
    set_text(s5.shapes[6], "Phễu Chuyển Đổi Web-to-App Tháng 10 (Chốt Số 31 Ngày)", font_size=10.0, bold=True, color=COLOR_MAGENTA)
    tbl5_1 = s5.shapes[7].table
    set_cell(tbl5_1.cell(0, 0), "Bước phễu chuyển đổi", bold=True, color=COLOR_WHITE)
    set_cell(tbl5_1.cell(0, 1), "Tháng 10 (31 ngày)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl5_1.cell(0, 2), "Tỷ lệ CVR / MoM", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    
    funnel_rows = [
        ("1. Total App Installs", "11.143", "100% (▲ +6,1% MoM)", True, COLOR_TEXT_MAIN),
        ("2. Đăng ký tài khoản (REG)", "3.902", "35,0% CVR (▲ +9,3% MoM)", False, COLOR_TEXT_MAIN),
        ("3. Liên kết NH (Map Bank / N2MM)", "2.389", "61,2% CVR (▲ +5,0% MoM · KỶ LỤC)", True, COLOR_GREEN),
        ("4. Active MAU (Giao dịch đầu)", "1.284", "53,8% từ Map (End-to-End 11,5%)", True, COLOR_TEXT_MAIN),
        ("Phân rã Hệ điều hành: iOS", "5.707 (51,2%)", "1.364 Map Bank (57,1% N2MM)", False, COLOR_MAGENTA),
        ("Phân rã Hệ điều hành: Android", "5.436 (48,8%)", "1.025 Map Bank (42,9% N2MM)", False, COLOR_TEXT_MUTED),
        ("Tổng toàn Website MoMo", "11.143 Installs", "2.389 Map Bank · 1.284 MAU", True, COLOR_TEXT_MAIN),
    ]
    for r_idx, (step, val, cr, is_bold, val_col) in enumerate(funnel_rows, 1):
        set_cell(tbl5_1.cell(r_idx, 0), step, bold=is_bold)
        set_cell(tbl5_1.cell(r_idx, 1), val, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col if is_bold else None)
        set_cell(tbl5_1.cell(r_idx, 2), cr, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col)

    # Right table title & table (Sources & Placements)
    set_text(s5.shapes[8], "Cơ Cấu Đóng Góp Theo Kênh & Placement (Ads, Cinema, Game)", font_size=10.0, bold=True, color=COLOR_MAGENTA)
    tbl5_2 = s5.shapes[9].table
    set_cell(tbl5_2.cell(0, 0), "Placement / Kênh nguồn", bold=True, color=COLOR_WHITE)
    set_cell(tbl5_2.cell(0, 1), "Installs (Tỷ trọng)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl5_2.cell(0, 2), "Map Bank (CVR Map/Ins)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    
    placement_rows = [
        ("Banner Ads (C.CHAOMOMO & Balloon)", "8.517 (76,4%)", "1.798 (21,1% CVR)", True, COLOR_TEXT_MAIN),
        ("Cinema Hub (Cụm rạp & Đặt vé)", "1.931 (17,3%)", "484 (25,1% CVR · Top 1)", True, COLOR_GREEN),
        ("Game Một Mùa Quýt & Quà (BRT)", "264 (2,4%)", "41 (7.097 active players)", False, COLOR_MAGENTA),
        ("Merchant Hub (Đối tác liên kết)", "271 (2,4%)", "40 (14,8% CVR · 30 MAU)", False, COLOR_TEXT_MAIN),
        ("Bảo hiểm (InsurTech)", "91 (0,8%)", "22 (24,2% CVR · 13 MAU)", False, COLOR_TEXT_MAIN),
        ("Thử nghiệm Financial Health", "68 (0,6%)", "3 (Luồng mới từ 12/10)", False, COLOR_TEXT_MUTED),
    ]
    for r_idx, (plc, ins, map_b, is_bold, val_col) in enumerate(placement_rows, 1):
        set_cell(tbl5_2.cell(r_idx, 0), plc, bold=is_bold)
        set_cell(tbl5_2.cell(r_idx, 1), ins, align=PP_ALIGN.RIGHT, bold=is_bold)
        set_cell(tbl5_2.cell(r_idx, 2), map_b, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col)

    # Bottom commentary box
    bottom_commentary_s5 = (
        "Key Highlights & Nhận Định Chiến Lược Tăng Trưởng New User\n"
        "• Xác lập kỷ lục N2MM mới: Tháng 10 mang về 2.389 khách hàng liên kết ngân hàng (+4,96% MoM, phá đỉnh 2.276 của T9) với 11.143 lượt cài app. Kênh Web khẳng định vai trò là phễu thu hút khách hàng tài chính chất lượng cao.\n"
        "• Động cơ Cinema & Gamification bứt phá: Cinema Hub tăng +58,2% Installs và +92,1% Map Bank với CVR End-to-End 15,2% (gấp rưỡi banner đại trà). Game \"Một Mùa Quýt\" hút 7.097 active players tạo đà kéo chuyển đổi ngoài app.\n"
        "• iOS là mỏ vàng kinh doanh: Chiếm 51,2% lượng cài đặt nhưng đóng góp tới 57,1% Map Bank (1.364 users) và 58,6% Active MAU nhờ tỷ lệ Map/REG đạt 67,4% (cao hơn Android +12,8 pp).\n"
        "• Trọng tâm Tháng 11: Tích hợp luồng Tải App chuẩn hóa (/tai-app đón 10K search volume) và mở rộng Gamification để thúc đẩy tỷ lệ REG/Install từ 35% lên ≥45%."
    )
    set_text(s5.shapes[10], bottom_commentary_s5, font_size=8.0, color=COLOR_TEXT_MAIN)

    # 7. Xóa bỏ Slide 6 cũ nếu chưa xóa (Old Slide 7 with duplicate GA4 browser new users)
    if len(prs.slides) > 7:
        delete_slide(prs, 6)
    TOTAL = len(prs.slides)
    print(f"Updated slides count after removing duplicate slide: {TOTAL}")

    # 8. Slide 6 (previously Slide 7): Hubs Breakdown
    s6_hub = prs.slides[6]
    set_text(s6_hub.shapes[0], "Cinema Hub Vượt Kế Hoạch (101,4% Target), Financial Hub Bước Đầu Ghi Nhận Tín Hiệu Tích Cực (+9,6% MoM)", font_size=15.5, bold=True, color=COLOR_TEXT_MAIN)
    s6_hub.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    
    # Shape 9: Cinema Hub Card Text
    sh9 = s6_hub.shapes[9]
    sh9.text_frame.word_wrap = True
    sh9.text_frame.paragraphs[0].text = "Cinema Hub"
    sh9.text_frame.paragraphs[0].runs[0].font.size = Pt(8.0)
    sh9.text_frame.paragraphs[0].runs[0].font.bold = True
    sh9.text_frame.paragraphs[0].runs[0].font.color.rgb = COLOR_MAGENTA
    
    sh9.text_frame.paragraphs[1].text = "1,13M"
    sh9.text_frame.paragraphs[1].runs[0].font.size = Pt(18.0)
    sh9.text_frame.paragraphs[1].runs[0].font.bold = True
    sh9.text_frame.paragraphs[1].runs[0].font.color.rgb = COLOR_TEXT_MAIN
    
    sh9.text_frame.paragraphs[2].text = "▲ 101,4% vs Target"
    sh9.text_frame.paragraphs[2].runs[0].font.size = Pt(7.5)
    sh9.text_frame.paragraphs[2].runs[0].font.bold = True
    sh9.text_frame.paragraphs[2].runs[0].font.color.rgb = COLOR_GREEN
    
    # Shape 10: Cinema Hub Badge -> Vượt Target (+15,3K PVs)
    set_text(s6_hub.shapes[10], "Vượt Kế Hoạch (+15,3K PVs)", font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER)
    s6_hub.shapes[10].fill.solid()
    s6_hub.shapes[10].fill.fore_color.rgb = COLOR_GREEN

    # Shape 12: Financial Hub Badge
    set_text(s6_hub.shapes[12], "Bước đầu đầu tư tích cực", font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER)
    s6_hub.shapes[12].fill.solid()
    s6_hub.shapes[12].fill.fore_color.rgb = COLOR_GREEN

    # Shape 13: Non-Paid Card Text
    sh13 = s6_hub.shapes[13]
    sh13.text_frame.word_wrap = True
    sh13.text_frame.paragraphs[0].text = "Non-Paid"
    sh13.text_frame.paragraphs[0].runs[0].font.size = Pt(8.0)
    sh13.text_frame.paragraphs[0].runs[0].font.bold = True
    sh13.text_frame.paragraphs[0].runs[0].font.color.rgb = COLOR_MAGENTA
    
    sh13.text_frame.paragraphs[1].text = "3,13M"
    sh13.text_frame.paragraphs[1].runs[0].font.size = Pt(18.0)
    sh13.text_frame.paragraphs[1].runs[0].font.bold = True
    sh13.text_frame.paragraphs[1].runs[0].font.color.rgb = COLOR_TEXT_MAIN
    
    sh13.text_frame.paragraphs[2].text = "▲ +13,5% MoM"
    sh13.text_frame.paragraphs[2].runs[0].font.size = Pt(7.5)
    sh13.text_frame.paragraphs[2].runs[0].font.bold = True
    sh13.text_frame.paragraphs[2].runs[0].font.color.rgb = COLOR_GREEN

    # Shape 14: Non-Paid Badge -> Chiếm 86,9% Tổng Lưu Lượng (GREEN!)
    set_text(s6_hub.shapes[14], "Chiếm 86,9% Tổng Lưu Lượng", font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER)
    s6_hub.shapes[14].fill.solid()
    s6_hub.shapes[14].fill.fore_color.rgb = COLOR_GREEN

    # Shape 19: Clean commentary, evaluate based on Target:
    commentary_s7 = (
        "Key Highlights & Commentary\n"
        "Đánh giá hiệu suất theo Target\n"
        "- Cinema Hub (Vượt 101,4% Target): Đạt 1.132.721 PVs, hoàn thành 101,4% so với Target tháng (1.117.378 PVs, vượt +15.343 PVs). Dù tổng PV giảm nhẹ -7,2% MoM do BU chủ động cắt giảm 92,9% Paid Ads của trang phim lẻ (-272K PVs), Hub vẫn xuất sắc về đích vượt Target nhờ cụm rạp đối tác tăng +39,6% (đạt 700K PVs) và tỷ trọng Organic đạt kỷ lục 86,4%.\n"
        "- Financial Hub: Đạt 273.705 PVs (+9,6% MoM), bước đầu đầu tư bài bản ghi nhận tín hiệu tích cực từ thị trường (không áp chỉ tiêu cứng); 62,7% lưu lượng Non-Paid, Trung Tâm Tài Chính tăng +442,0% nhờ nhóm tiện ích ngoại tệ và giá vàng.\n"
        "Cơ cấu lưu lượng & Tối ưu chi phí\n"
        "- Kênh tự nhiên (Non-Paid): Đạt 3.128.542 PVs (+13,5% MoM, chiếm 86,9% toàn sàn), hoàn thành 109,2% tổng chỉ tiêu các kênh tự nhiên (Target 2,87M), tự bù đắp phần lớn khoảng trống do BU cắt giảm 60,4% ngân sách Paid Ads (-723K PVs toàn Website)."
    )
    set_text(s6_hub.shapes[19], commentary_s7, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Clean footers and page numbering across ALL slides
    for idx, s in enumerate(prs.slides):
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            txt = sh.text_frame.text.strip()
            # Clean template instruction
            if txt.startswith("Mục đích:"):
                sh.text_frame.text = ""
            # Clean footer source (remove completely as requested)
            elif txt.startswith("Nguồn:") or "Owner: Web Platform" in txt:
                sh.text_frame.text = ""
            # Update page number
            elif "/" in txt and any(c.isdigit() for c in txt) and len(txt) <= 8 and idx > 0:
                set_text(sh, f"{idx+1} / {TOTAL}", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Save to all 4 SSOT paths (including Google Drive Desktop)
    out_paths = [
        BASE_DIR / "07_REPORTS" / "docs" / "presentations" / "Web_Platform_Thang_10_2026_Pyramid.pptx",
        Path("/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Pyramid.pptx"),
        Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Pyramid.pptx"),
        Path("/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#6 - Report/Web_Platform_Thang_10_2026_Pyramid.pptx"),
    ]
    for p in out_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        prs.save(str(p))
        print(f"Saved: {p}")

if __name__ == "__main__":
    main()

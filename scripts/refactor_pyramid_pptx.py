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
            elif "AppsFlyer" in txt:
                sh.text_frame.text = "Kỳ dữ liệu 01/10 - 31/10/2026 (31 ngày, full month). Nguồn: GA4 (Property 270743103) & Excel SSOT."

    # 2. Slide 1: Executive Summary
    s1 = prs.slides[1]
    set_text(s1.shapes[0], "Tháng 10 Đạt 98,3% Kế Hoạch Nhờ Kênh Tự Nhiên Tăng +13,5% MoM; Tập Trung Tối Ưu Luồng Tải App 10.000 Tìm Kiếm", font_size=15.5, bold=True, color=COLOR_TEXT_MAIN)
    s1.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    set_text(s1.shapes[6], "Kết luận điều hành\nKênh tự nhiên (Non-Paid) là động lực tăng trưởng cốt lõi của Web Platform trong tháng 10 với 3.128.542 PVs (+13,5% MoM, chiếm 86,9% toàn sàn), tự bù đắp phần lớn lượng suy giảm do BU cắt giảm Paid Ads. Nền tảng thu hút 1,24M New Users tự nhiên. Trọng tâm tháng 11 là chuẩn hóa luồng Tải App (/tai-app) để đón trọn 10.000 volume tìm kiếm thương hiệu.", font_size=9.5, color=COLOR_WHITE)
    set_text(s1.shapes[9], "3. Kênh tự nhiên dẫn dắt 1,24M New Users (78,9% tổng)\n- Toàn sàn đón 1.573.964 New Users (91,5% tổng người dùng ghé thăm).\n- Kênh tự nhiên đạt 1.241.076 New Users (+3,5% MoM), tự bù đắp mức giảm Paid.\n- Cinema Hub (280K New Users) & Minigame (53,6K) là 2 phễu hút lớn nhất.", font_size=9.0, color=COLOR_TEXT_MAIN)
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

    # 5. Slide 4: Tổng lượt xem
    s4 = prs.slides[4]
    s4.shapes[2].text_frame.text = "" # Clear "Mục đích:"

    # 6. Slide 5: GEO AI Search
    s5 = prs.slides[5]
    s5.shapes[2].text_frame.text = "" # Clear "Mục đích:"

    # 7. Slide 6: New User Flow
    s6 = prs.slides[6]
    set_text(s6.shapes[0], "Kênh Tự Nhiên Dẫn Dắt 1,24M Người Dùng Mới (78,9% Tổng New Users), Bù Đắp Sụt Giảm Paid Ads", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    s6.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    # Repurpose right table shape 8: change to Key Hubs New User Funnel
    tbl6_2 = s6.shapes[8].table
    set_cell(tbl6_2.cell(0, 0), "Phễu Hub & Sản phẩm", bold=True, color=COLOR_WHITE)
    set_cell(tbl6_2.cell(0, 1), "Ngành", bold=True, color=COLOR_WHITE)
    set_cell(tbl6_2.cell(0, 2), "New Users", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    hub_users_data = [
        ("• Cinema Hub (Cụm Rạp & Diễn Viên)", "Movies", "280.016"),
        ("• Onboarding & Tiện Ích Tải App", "Platform", "285.882"),
        ("• Minigame & Giải Trí (Một Mùa Quýt)", "Game", "53.612"),
        ("• Financial Hub (Ví Trả Sau, Tỷ Giá)", "Finance", "78.415"),
        ("• Travel & Du Lịch Đi Lại", "OTA", "42.190"),
        ("• Dịch Vụ Tiện Ích Đời Sống Khác", "Utility", "833.849"),
    ]
    for r_idx, (hub, cat, users) in enumerate(hub_users_data, 1):
        set_cell(tbl6_2.cell(r_idx, 0), hub, bold=True)
        set_cell(tbl6_2.cell(r_idx, 1), cat)
        set_cell(tbl6_2.cell(r_idx, 2), users, align=PP_ALIGN.RIGHT, bold=True, color=COLOR_GREEN)

    # 8. Slide 7: Hubs Breakdown
    s7 = prs.slides[7]
    set_text(s7.shapes[0], "Cinema Hub Vượt Kế Hoạch (101,4%), Financial Hub Bước Đầu Ghi Nhận Tín Hiệu Tích Cực (+9,6% MoM)", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    s7.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    set_text(s7.shapes[12], "Bước đầu đầu tư tích cực", font_size=9.0, bold=True, color=COLOR_WHITE)
    # Shape 19: Clean commentary, remove Phạt Nguội & target confusion completely:
    commentary_s7 = (
        "Key Highlights & Commentary\n"
        "Performance\n"
        "- Cinema Hub: 1.132.721 PVs (101,4% kế hoạch tháng), 86,4% lưu lượng đến từ Organic; cụm rạp đối tác chiếm 61,8% Hub tăng +39,6% đóng vai trò đầu kéo lưu lượng sạch.\n"
        "- Financial Hub: 273.705 PVs (+9,6% MoM), bước đầu đầu tư bài bản ghi nhận tín hiệu tích cực từ thị trường (không áp chỉ tiêu cứng); 62,7% lưu lượng Non-Paid, Trung Tâm Tài Chính tăng +442,0% nhờ nhóm tiện ích ngoại tệ và giá vàng.\n"
        "Tái cơ cấu nguồn lực\n"
        "- Vay Nhanh giảm 47.814 PVs (-43,5%) cùng nhịp cắt 60,4% Paid Ads toàn Website để tối ưu ngân sách; chuyển dịch lưu lượng sang các dịch vụ tài chính bền vững (Ví Trả Sau +38,2%, Điểm Tín Dụng 91,2K PVs)."
    )
    set_text(s7.shapes[19], commentary_s7, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Clean footers and page numbering across ALL slides
    for idx, s in enumerate(prs.slides):
        for sh in s.shapes:
            if not sh.has_text_frame:
                continue
            txt = sh.text_frame.text.strip()
            # Clean template instruction
            if txt.startswith("Mục đích:"):
                sh.text_frame.text = ""
            # Clean footer source
            elif "Nguồn:" in txt:
                set_text(sh, "Nguồn: GA4 (Property 270743103) & Excel SSOT   |   Owner: Web Platform   |   Chốt số liệu: 31/10/2026", font_size=8.5, color=COLOR_TEXT_MUTED)
            # Update page number
            elif "/" in txt and any(c.isdigit() for c in txt) and len(txt) <= 8 and idx > 0:
                set_text(sh, f"{idx+1} / {TOTAL}", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Save to all 3 SSOT paths
    out_paths = [
        BASE_DIR / "07_REPORTS" / "docs" / "presentations" / "Web_Platform_Thang_10_2026_Pyramid.pptx",
        Path("/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Pyramid.pptx"),
        Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Pyramid.pptx"),
    ]
    for p in out_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        prs.save(str(p))
        print(f"Saved: {p}")

if __name__ == "__main__":
    main()

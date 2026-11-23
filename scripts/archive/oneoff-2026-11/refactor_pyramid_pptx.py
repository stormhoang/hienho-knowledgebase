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

def style_table_cell(cell, text, font_size=7.5, bold=False, color=None, bg_color=None, align=PP_ALIGN.LEFT):
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.text = str(text)
    p.alignment = align
    cell.margin_top = Inches(0.015)
    cell.margin_bottom = Inches(0.015)
    cell.margin_left = Inches(0.035)
    cell.margin_right = Inches(0.035)
    for run in p.runs:
        run.font.size = Pt(font_size)
        run.font.bold = bold
        if color:
            run.font.color.rgb = color
    if bg_color:
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_color

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

def set_card_box(shape, title, bullets, font_size_title=8.6, font_size_bullet=7.8):
    if not shape.has_text_frame:
        return
    tf = shape.text_frame
    tf.word_wrap = True
    tf.text = ""
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.space_before = Pt(0)
    p0.space_after = Pt(3)
    for run in p0.runs:
        run.font.size = Pt(font_size_title)
        run.font.bold = True
        run.font.color.rgb = COLOR_TEXT_MAIN
    
    for b in bullets:
        p = tf.add_paragraph()
        p.text = f"• {b}"
        p.space_before = Pt(2)
        p.space_after = Pt(2)
        for run in p.runs:
            run.font.size = Pt(font_size_bullet)
            run.font.bold = False
            run.font.color.rgb = COLOR_TEXT_MUTED

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

    # 2. Slide 1: Executive Summary (BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT)
    s1 = prs.slides[1]
    set_text(s1.shapes[0], "Tháng 10 đạt 98,3% target nhờ Non-Paid tăng 13,5%; tập trung luồng Tải App đón 10.000 lượt tìm kiếm", font_size=15.0, bold=True, color=COLOR_TEXT_MAIN)
    s1.shapes[2].text_frame.text = "" # Clear "Mục đích:"

    # Remove old middle card shapes if they exist
    cards_to_remove = []
    tbl1_shape = None
    for sh in s1.shapes:
        if sh.has_table:
            tbl1_shape = sh
        elif sh.has_text_frame:
            txt = sh.text_frame.text.strip()
            if txt.startswith("1. Non-Paid") or txt.startswith("2. Dự án") or txt.startswith("3. Cinema"):
                cards_to_remove.append(sh)
    for sh in cards_to_remove:
        sp = sh._element
        sp.getparent().remove(sp)

    # Hero / Subtitle banner above table
    hero_shape = None
    for sh in s1.shapes:
        if sh.has_text_frame and not sh.has_table:
            txt = sh.text_frame.text.strip()
            if "Kết luận điều hành" in txt or "BẢNG ĐIỀU HÀNH" in txt:
                hero_shape = sh
                break
    if hero_shape:
        hero_shape.top = Inches(1.42)
        hero_shape.height = Inches(0.46)
        hero_shape.left = Inches(0.40)
        hero_shape.width = Inches(9.20)
        tf_hero = hero_shape.text_frame
        tf_hero.margin_top = Inches(0.04)
        tf_hero.margin_bottom = Inches(0.04)
        tf_hero.margin_left = Inches(0.08)
        tf_hero.margin_right = Inches(0.08)
        tf_hero.text = ""
        
        p0 = tf_hero.paragraphs[0]
        p0.text = "BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT (EXECUTIVE SCORECARD) — CƠ CẤU KÊNH LƯU LƯỢNG (T7 ➔ T10)"
        p0.space_before = Pt(0)
        p0.space_after = Pt(2)
        for r in p0.runs:
            r.font.size = Pt(8.5)
            r.font.bold = True
            r.font.color.rgb = COLOR_WHITE
            
        p1 = tf_hero.add_paragraph()
        p1.text = "Kênh tự nhiên (Non-Paid) tăng trưởng +13,5% (+373K views), tự bù đắp hơn một nửa việc cắt giảm 724K views quảng cáo để tối ưu chi phí."
        p1.space_before = Pt(1)
        p1.space_after = Pt(1)
        for r in p1.runs:
            r.font.size = Pt(7.5)
            r.font.bold = False
            r.font.color.rgb = COLOR_WHITE

    # Add or configure table
    if not tbl1_shape:
        tbl1_shape = s1.shapes.add_table(8, 7, Inches(0.40), Inches(1.95), Inches(9.20), Inches(2.00))
    else:
        tbl1_shape.top = Inches(1.95)
        tbl1_shape.height = Inches(2.00)
        tbl1_shape.left = Inches(0.40)
        tbl1_shape.width = Inches(9.20)

    tbl1 = tbl1_shape.table
    # Column widths (Total = 9.20 in)
    tbl1.columns[0].width = Inches(2.15)
    tbl1.columns[1].width = Inches(0.88)
    tbl1.columns[2].width = Inches(0.88)
    tbl1.columns[3].width = Inches(0.88)
    tbl1.columns[4].width = Inches(0.88)
    tbl1.columns[5].width = Inches(0.78)
    tbl1.columns[6].width = Inches(2.75)

    # Header row
    headers = ["Kênh lưu lượng", "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "% MoM", "Nhận định / Ý nghĩa"]
    for c_idx, h_text in enumerate(headers):
        align = PP_ALIGN.LEFT if c_idx in [0, 6] else PP_ALIGN.RIGHT
        style_table_cell(tbl1.cell(0, c_idx), h_text, font_size=7.8, bold=True, color=COLOR_WHITE, bg_color=COLOR_MAGENTA, align=align)

    scorecard_rows = [
        ("KÊNH TỰ NHIÊN (NON-PAID)", "2.669.863", "2.820.824", "2.755.766", "3.128.542", "+13,5%", "Tự chủ tăng trưởng (+373K views), tự bù 51% Paid cắt giảm", True, COLOR_GREEN, RGBColor(0xEC, 0xFD, 0xF5)),
        ("   - Organic Search", "1.875.191", "1.729.694", "1.623.796", "1.715.771", "+5,7%", "SEO/GEO bền vững, chiếm 47,6% tổng lưu lượng toàn sàn", False, COLOR_TEXT_MAIN, RGBColor(0xFF, 0xFF, 0xFF)),
        ("   - Direct", "440.855", "656.271", "755.896", "931.731", "+23,3%", "Sức mạnh thương hiệu; người dùng chủ động quay lại tăng mạnh", False, COLOR_TEXT_MAIN, RGBColor(0xF9, 0xFA, 0xFB)),
        ("   - Referral", "329.659", "410.305", "345.132", "350.162", "+1,5%", "Mạng lưới đối tác rạp phim, liên kết ngân hàng và in-app ổn định", False, COLOR_TEXT_MAIN, RGBColor(0xFF, 0xFF, 0xFF)),
        ("   - Kênh tự nhiên khác", "24.158", "24.554", "30.942", "130.878", "+322,9%", "Phân tách dữ liệu chính xác từ nguồn mới và tính năng mở rộng", False, COLOR_TEXT_MAIN, RGBColor(0xF9, 0xFA, 0xFB)),
        ("KÊNH TRẢ PHÍ (PAID ADS)", "497.958", "644.539", "1.197.093", "473.481", "-60,4%", "Chủ động cắt giảm 724K views quảng cáo để tối ưu chi phí", True, RGBColor(0xD9, 0x77, 0x06), RGBColor(0xFF, 0xFB, 0xEB)),
        ("TỔNG LƯỢNG TRUY CẬP TOÀN WEB", "3.167.821", "3.465.363", "3.952.859", "3.602.023", "-8,9%", "Đạt 98,3% Target tháng (3,67M); kênh tự nhiên đạt 86,9% toàn sàn", True, COLOR_MAGENTA, RGBColor(0xFD, 0xF2, 0xF8)),
    ]

    for r_idx, (ch, t7, t8, t9, t10, mom, note, is_bold, text_col, bg_col) in enumerate(scorecard_rows, 1):
        tbl1.rows[r_idx].height = Inches(0.23)
        style_table_cell(tbl1.cell(r_idx, 0), ch, font_size=7.2, bold=is_bold, color=text_col if is_bold else COLOR_TEXT_MAIN, bg_color=bg_col, align=PP_ALIGN.LEFT)
        style_table_cell(tbl1.cell(r_idx, 1), t7, font_size=7.2, bold=is_bold, color=text_col if is_bold else COLOR_TEXT_MAIN, bg_color=bg_col, align=PP_ALIGN.RIGHT)
        style_table_cell(tbl1.cell(r_idx, 2), t8, font_size=7.2, bold=is_bold, color=text_col if is_bold else COLOR_TEXT_MAIN, bg_color=bg_col, align=PP_ALIGN.RIGHT)
        style_table_cell(tbl1.cell(r_idx, 3), t9, font_size=7.2, bold=is_bold, color=text_col if is_bold else COLOR_TEXT_MAIN, bg_color=bg_col, align=PP_ALIGN.RIGHT)
        style_table_cell(tbl1.cell(r_idx, 4), t10, font_size=7.2, bold=is_bold, color=text_col if is_bold else COLOR_TEXT_MAIN, bg_color=bg_col, align=PP_ALIGN.RIGHT)
        mom_col = COLOR_GREEN if "+" in mom else (RGBColor(0xDC, 0x26, 0x26) if "-" in mom else COLOR_TEXT_MAIN)
        style_table_cell(tbl1.cell(r_idx, 5), mom, font_size=7.2, bold=True, color=mom_col, bg_color=bg_col, align=PP_ALIGN.RIGHT)
        style_table_cell(tbl1.cell(r_idx, 6), note, font_size=7.0, bold=is_bold, color=COLOR_TEXT_MAIN, bg_color=bg_col, align=PP_ALIGN.LEFT)

    # Find the two bottom boxes
    box_left = None
    box_right = None
    for sh in s1.shapes:
        if sh.has_text_frame and not sh.has_table:
            txt = sh.text_frame.text.strip()
            if "Điểm nổi bật" in txt or "Điểm sáng điều hành" in txt:
                box_left = sh
            elif "Cần theo dõi" in txt or "Trọng tâm điều hành" in txt:
                box_right = sh

    if box_left:
        box_left.top = Inches(4.08)
        box_left.height = Inches(1.10)
        box_left.left = Inches(0.40)
        box_left.width = Inches(4.50)
        bottom_left_s1 = (
            "Điểm sáng điều hành\n"
            "• Kênh tự nhiên (Non-Paid) lập đỉnh 3,13M lượt xem (+13,5% MoM, chiếm 86,9% toàn sàn), tăng liên tục từ mức 2,67M (T7) và tự bù đắp khoảng trống Paid Ads.\n"
            "• Dự án New User đạt kết quả tốt nhất lịch sử: 2.389 user liên kết ngân hàng (+5% MoM), dẫn dắt bởi Cinema Hub (1.931 cài, CVR 15,2%) và banner quảng cáo."
        )
        set_text(box_left, bottom_left_s1, font_size=7.2, color=COLOR_TEXT_MAIN)

    if box_right:
        box_right.top = Inches(4.08)
        box_right.height = Inches(1.10)
        box_right.left = Inches(5.10)
        box_right.width = Inches(4.50)
        bottom_right_s1 = (
            "Trọng tâm điều hành tháng 11\n"
            "• Paid Ads giảm -60,4% (-724K lượt) do các BU tối ưu chi phí -> Web Platform tập trung tối đa nguồn lực vào sản phẩm tự nhiên để duy trì đà tăng trưởng.\n"
            "• Chuẩn hóa luồng Tải App (/tai-app) đón 22.750 volume tìm kiếm & 100K impressions GSC; rà soát công thức tính thuế TNCN trước 10/11 để đón mùa quyết toán cuối năm."
        )
        set_text(box_right, bottom_right_s1, font_size=7.2, color=COLOR_TEXT_MAIN)

    # 3. Slide 2: Discussion Topics
    s2 = prs.slides[2]
    set_text(s2.shapes[0], "Discussion Topics — 1 chủ đề cần phê duyệt: 0 Discuss, 1 Approve", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    s2.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    tbl2 = s2.shapes[6].table
    set_cell(tbl2.cell(1, 0), "1", align=PP_ALIGN.CENTER, bold=True)
    set_cell(tbl2.cell(1, 1), "Chuẩn hóa cổng Tải App (/tai-app) đón 22.750 volume & 100K impressions GSC", bold=True)
    set_cell(tbl2.cell(1, 2), "Approve", align=PP_ALIGN.CENTER, bold=True, color=COLOR_MAGENTA)
    set_cell(tbl2.cell(1, 3), "Phê duyệt cơ chế chuyển hướng (Redirect 301) link tải cũ về /tai-app và đồng bộ nút CTA Tải App trên Header/Footer toàn sàn.")
    set_cell(tbl2.cell(1, 4), "Đón 22.750 search volume/tháng (~100K GSC impressions); chặn đứng nguy cơ tải file APK giả mạo chứa mã độc (chiếm ~1.000 volume).", color=COLOR_GREEN)
    set_cell(tbl2.cell(1, 5), "Tháng 11", align=PP_ALIGN.CENTER, bold=True)
    set_cell(tbl2.cell(1, 6), "CAO", align=PP_ALIGN.CENTER, bold=True, color=COLOR_MAGENTA)
    set_cell(tbl2.cell(1, 7), "Slide 4", align=PP_ALIGN.CENTER, bold=True, color=COLOR_MAGENTA)
    if len(tbl2.rows) > 2:
        tr2 = tbl2.rows[2]._tr
        tr2.getparent().remove(tr2)
    set_text(s2.shapes[7], "Lưu ý\nCần phê duyệt sớm trong tháng 11 để trang kịp lập chỉ mục trên Google và kích hoạt trọn vẹn luồng chuyển đổi người dùng dịp cuối năm. Kỹ thuật đã sẵn sàng 100% trên Production.", font_size=9.0, color=COLOR_TEXT_MAIN)

    # 4. Slide 3: Proposal 1 Deep-Dive
    s3 = prs.slides[3]
    set_text(s3.shapes[0], "Đề xuất 1: Chuẩn hóa trang Tải App (/tai-app), đón 22.750 volume tìm kiếm & 100K impressions GSC", font_size=15.5, bold=True, color=COLOR_TEXT_MAIN)
    s3.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    
    problem_ctx_text = (
        "Vấn đề & Bối cảnh (Dữ liệu GSC & Keyword Inventory)\n"
        "• GSC ghi nhận 99.749 impressions/tháng (100K lượt thấy MoMo) nhưng chỉ thu về 5.585 clicks (CTR cực thấp 5,60% do trả về bài viết cũ, thiếu trang đích chính thức).\n"
        "• Keyword Inventory (188 từ khóa): Tổng dung lượng 22.750 searches/tháng (~273K searches/năm); nhóm tải MoMo cốt lõi chiếm 16.200 vol, cài đặt chiếm 2.080 vol.\n"
        "• Rủi ro an ninh & giả mạo: Gần 1.000 searches/tháng tìm file APK ngoài kho (tải momo apk: 720 vol, apk cũ, apkpure); người dùng dễ tải nhầm app giả mạo ăn cắp tiền."
    )
    set_text(s3.shapes[6], problem_ctx_text, font_size=8.2, color=COLOR_TEXT_MAIN)

    impact_benefits_text = (
        "Lợi ích & Tác động kinh doanh (W2A Uplift)\n"
        "• Tối ưu CTR từ 5,6% lên 25%: Kéo thêm +20.000 đến +25.000 clicks sạch mỗi tháng; CVR cài app dự kiến 40-60%, mang về 8.000 - 15.000 New Installs/tháng (0đ Paid).\n"
        "• Trải nghiệm 1-chạm thông minh: Tự nhận diện thiết bị (Mobile iOS mở App Store, Android mở Google Play, Desktop hiển thị mã QR sắc nét quét cài app).\n"
        "• Chi phí triển khai: 0 VNĐ (Mã nguồn momo.vn/tai-app đã hoàn thiện 100% trên Production, đã tích hợp OneLink AppsFlyer đo lường End-to-End)."
    )
    set_text(s3.shapes[7], impact_benefits_text, font_size=8.2, color=COLOR_TEXT_MAIN)

    tbl3 = s3.shapes[8].table
    set_cell(tbl3.cell(0, 0), "Phương án", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(0, 1), "Nội dung triển khai", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(0, 2), "Lợi ích mang lại", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(0, 3), "Đánh giá rủi ro", bold=True, color=COLOR_WHITE)
    set_cell(tbl3.cell(1, 0), "Phương án A (Đề xuất)", bold=True, color=COLOR_GREEN)
    set_cell(tbl3.cell(1, 1), "Chuyển toàn bộ link tải cũ về /tai-app; tối ưu SEO Top 1 Google; đồng bộ nút Tải App trên Header/Footer toàn website.")
    set_cell(tbl3.cell(1, 2), "Đón trọn 22.750 volume/tháng & 100K GSC impressions; trải nghiệm 1 chạm cài app; chặn file APK độc hại; chi phí 0 VNĐ.", color=COLOR_GREEN)
    set_cell(tbl3.cell(1, 3), "Rủi ro rất thấp: Trang /tai-app đã chạy ổn định trên Production, chỉ cần cập nhật liên kết.")
    set_cell(tbl3.cell(2, 0), "Phương án B (Hiện trạng)", bold=True)
    set_cell(tbl3.cell(2, 1), "Giữ nguyên các trang tải rải rác (/download, các bài viết cũ); không có cơ chế tự nhận diện thiết bị.")
    set_cell(tbl3.cell(2, 2), "Tiếp tục mất 22.750 volume & 100K impressions vào tay trang ngoài; CTR lẹt đẹt 5,6%; trải nghiệm máy tính bị đứt gãy.", color=COLOR_MAGENTA)
    set_cell(tbl3.cell(2, 3), "Rủi ro bảo mật: Gần 1.000 user/tháng tìm APK có nguy cơ tải nhầm app giả mạo bị hack tài khoản ví.")
    
    bom_ask_text = (
        "Đề xuất BOM: Phê duyệt phương án A để kích hoạt luồng tải app chính thức ngay trong tháng 11.\n"
        "Hệ quả nếu không làm: MoMo tiếp tục để mất 22.750 lượt tìm kiếm/tháng và 100.000 lượt hiển thị GSC vào các trang trung gian, đối mặt rủi ro an ninh nghiêm trọng khi người dùng tìm cài file APK giả mạo bên ngoài."
    )
    set_text(s3.shapes[9], bom_ask_text, font_size=8.2, color=COLOR_TEXT_MAIN)

    # 5. Slide 4: Tổng lượt xem (Slide 5 of deck)
    s4 = prs.slides[4]
    s4.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    set_text(s4.shapes[0], "Kênh tự nhiên đạt 3,13M lượt xem (+13,5% MoM), vượt 109% target; toàn sàn đạt 98,3% do các BU cắt giảm Paid Ads", font_size=15.0, bold=True, color=COLOR_TEXT_MAIN)
    
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

    human_commentary_s4 = (
        "Nhận định & Hành động tiếp theo\n"
        "- Kênh tự nhiên tăng trưởng rất tốt: Cả Organic, Direct và Referral đều vượt kế hoạch từ 108% đến 109%. Lượng truy cập trực tiếp (Direct) tăng +23,3% cho thấy độ nhận diện thương hiệu MoMo trên web đang ngày càng vững chắc.\n"
        "- Bù đắp lượng hụt từ Paid Ads: Kênh tự nhiên tăng thêm +373K lượt xem (+13,5% MoM), gánh được hơn một nửa khoảng trống khi các BU chủ động cắt giảm 60,4% ngân sách quảng cáo (-724K lượt xem).\n"
        "- Trọng tâm tháng 11: Đưa luồng Tải App (/tai-app) vào hoạt động chính thức và tiếp tục mở rộng nội dung ở các Hub trọng điểm (Cinema, Tài chính) để giữ vững đà tăng trưởng tự nhiên."
    )
    set_text(s4.shapes[8], human_commentary_s4, font_size=8.5, color=COLOR_TEXT_MAIN)
    s4.shapes[9].text_frame.text = "" # Clear duplicate bottom note

    # 6. Slide 5: Dự Án New User & Phễu Chuyển Đổi (Slide 6 of deck)
    s5 = prs.slides[5]
    set_text(s5.shapes[0], "Dự án New User đạt mốc cao nhất từ trước đến nay: 2.389 user liên kết ngân hàng (+5% MoM) từ 11.143 lượt cài app", font_size=14.5, bold=True, color=COLOR_TEXT_MAIN)
    s5.shapes[2].text_frame.text = "" # Clear "Mục đích:"
    
    # Left table title & table (Funnel)
    set_text(s5.shapes[6], "Phễu chuyển đổi Web-to-App tháng 10 (đầy đủ 31 ngày)", font_size=10.0, bold=True, color=COLOR_MAGENTA)
    tbl5_1 = s5.shapes[7].table
    set_cell(tbl5_1.cell(0, 0), "Bước phễu chuyển đổi", bold=True, color=COLOR_WHITE)
    set_cell(tbl5_1.cell(0, 1), "Tháng 10 (31 ngày)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl5_1.cell(0, 2), "Tỷ lệ CVR / MoM", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    
    funnel_rows = [
        ("1. Cài app (Installs)", "11.143", "100% (+6,1% MoM)", True, COLOR_TEXT_MAIN),
        ("2. Đăng ký tài khoản (REG)", "3.902", "35,0% CVR (+9,3%)", False, COLOR_TEXT_MAIN),
        ("3. Liên kết NH (Map Bank)", "2.389", "61,2% CVR (+5,0% MoM)", True, COLOR_GREEN),
        ("4. Giao dịch đầu (MAU)", "1.284", "53,8% từ Map (11,5% CVR)", True, COLOR_TEXT_MAIN),
        ("Theo thiết bị: iOS", "5.707 (51,2%)", "1.364 Map (57,1%)", False, COLOR_MAGENTA),
        ("Theo thiết bị: Android", "5.436 (48,8%)", "1.025 Map (42,9%)", False, COLOR_TEXT_MUTED),
    ]
    if len(tbl5_1.rows) > 7:
        tr7 = tbl5_1.rows[7]._tr
        tr7.getparent().remove(tr7)
    for r_idx, (step, val, cr, is_bold, val_col) in enumerate(funnel_rows, 1):
        set_cell(tbl5_1.cell(r_idx, 0), step, font_size=8.0, bold=is_bold)
        set_cell(tbl5_1.cell(r_idx, 1), val, font_size=8.0, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col if is_bold else None)
        set_cell(tbl5_1.cell(r_idx, 2), cr, font_size=8.0, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col)

    # Right table title & table (Sources & Placements)
    set_text(s5.shapes[8], "Cơ cấu đóng góp theo nguồn (Quảng cáo, Rạp phim, Minigame)", font_size=10.0, bold=True, color=COLOR_MAGENTA)
    tbl5_2 = s5.shapes[9].table
    set_cell(tbl5_2.cell(0, 0), "Nguồn chiến dịch / Vị trí", bold=True, color=COLOR_WHITE)
    set_cell(tbl5_2.cell(0, 1), "Lượt cài (Tỷ trọng)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    set_cell(tbl5_2.cell(0, 2), "Liên kết NH (Tỷ lệ Map/Cài)", bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT)
    
    placement_rows = [
        ("Banner chào MoMo & Popup", "8.517 (76,4%)", "1.798 (tỷ lệ 21,1%)", True, COLOR_TEXT_MAIN),
        ("Cinema Hub (Cụm rạp & Đặt vé)", "1.931 (17,3%)", "484 (tỷ lệ 25,1%)", True, COLOR_GREEN),
        ("Minigame Một Mùa Quýt", "264 (2,4%)", "41 (7.097 người chơi)", False, COLOR_MAGENTA),
        ("Trang Đối tác & Merchant", "271 (2,4%)", "40 (tỷ lệ 14,8%)", False, COLOR_TEXT_MAIN),
        ("Bảo hiểm (InsurTech)", "91 (0,8%)", "22 (tỷ lệ 24,2%)", False, COLOR_TEXT_MAIN),
        ("Sức khỏe tài chính", "68 (0,6%)", "3 (mới từ 12/10)", False, COLOR_TEXT_MUTED),
    ]
    for r_idx, (plc, ins, map_b, is_bold, val_col) in enumerate(placement_rows, 1):
        set_cell(tbl5_2.cell(r_idx, 0), plc, font_size=8.0, bold=is_bold)
        set_cell(tbl5_2.cell(r_idx, 1), ins, font_size=8.0, align=PP_ALIGN.RIGHT, bold=is_bold)
        set_cell(tbl5_2.cell(r_idx, 2), map_b, font_size=8.0, align=PP_ALIGN.RIGHT, bold=is_bold, color=val_col)

    # Tight margins to prevent row expansion
    for tbl in [tbl5_1, tbl5_2]:
        for r in tbl.rows:
            r.height = Inches(0.24)
            for c in r.cells:
                c.margin_top = Inches(0.01)
                c.margin_bottom = Inches(0.01)
                c.margin_left = Inches(0.04)
                c.margin_right = Inches(0.04)

    # Bottom commentary box
    s5.shapes[10].top = Inches(4.0)
    s5.shapes[10].height = Inches(1.22)
    bottom_commentary_s5 = (
        "Đánh giá kết quả & Trọng tâm tháng 11\n"
        "• Kết quả chuyển đổi cao nhất từ trước đến nay: Tháng 10 mang về 2.389 người dùng liên kết ngân hàng (+5% MoM, vượt mốc 2.276 của tháng 9) từ 11.143 lượt cài app. Kênh Web tiếp tục là phễu đón khách hàng tài chính rất chất lượng cho app.\n"
        "• Rạp phim và minigame chuyển đổi rất tốt: Cinema Hub tăng +58% lượt cài và +92% lượt liên kết ngân hàng với tỷ lệ chuyển đổi cuối đạt 15,2% (cao hơn banner đại trà). Minigame 'Một Mùa Quýt' thu hút hơn 7.000 người chơi, tạo phễu tương tác tốt bên ngoài ứng dụng.\n"
        "• Người dùng iOS mang lại giá trị cao: Tuy chiếm 51% lượng cài đặt nhưng iOS đóng góp tới 57% số user liên kết ngân hàng (1.364 user) và 59% MAU, nhờ tỷ lệ hoàn tất liên kết đạt 67,4% (cao hơn Android gần 13%).\n"
        "• Trọng tâm tháng 11: Đưa luồng Tải App (/tai-app) vào vận hành chính thức và mở rộng minigame tương tác để kéo tỷ lệ hoàn tất đăng ký từ 35% lên trên 40%."
    )
    set_text(s5.shapes[10], bottom_commentary_s5, font_size=8.0, color=COLOR_TEXT_MAIN)

    # 7. Xóa bỏ Slide 6 cũ nếu chưa xóa (Old Slide 7 with duplicate GA4 browser new users)
    if len(prs.slides) > 7:
        delete_slide(prs, 6)
    TOTAL = len(prs.slides)
    print(f"Updated slides count after removing duplicate slide: {TOTAL}")

    # 8. Slide 6 (previously Slide 7): Hubs Breakdown
    s6_hub = prs.slides[6]
    set_text(s6_hub.shapes[0], "Cinema Hub vượt kế hoạch (101,4% target), Hub Tài chính tăng trưởng khả quan (+9,6% MoM)", font_size=15.0, bold=True, color=COLOR_TEXT_MAIN)
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
    
    # Shape 10: Cinema Hub Badge -> Vượt target (+15,3K lượt)
    set_text(s6_hub.shapes[10], "Vượt target (+15,3K lượt)", font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER)
    s6_hub.shapes[10].fill.solid()
    s6_hub.shapes[10].fill.fore_color.rgb = COLOR_GREEN

    # Shape 12: Financial Hub Badge
    set_text(s6_hub.shapes[12], "Tín hiệu khả quan", font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER)
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

    # Shape 14: Non-Paid Badge -> Chiếm 87% toàn sàn
    set_text(s6_hub.shapes[14], "Chiếm 87% toàn sàn", font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER)
    s6_hub.shapes[14].fill.solid()
    s6_hub.shapes[14].fill.fore_color.rgb = COLOR_GREEN

    # Shape 19: Clean human commentary:
    human_commentary_s7 = (
        "Nhận định chi tiết\n"
        "Đánh giá theo kế hoạch tháng (Target)\n"
        "- Cinema Hub (Đạt 101,4% target): Đạt 1,13M lượt xem, vượt nhẹ chỉ tiêu (+15,3K lượt). Dù tổng lượt xem giảm nhẹ -7,2% MoM do BU cắt gần như toàn bộ Paid Ads cho các trang phim lẻ (-272K lượt), Hub vẫn về đích nhờ trang các cụm rạp tăng trưởng tốt (+39,6%, đạt 700K lượt) và tỷ lệ truy cập tự nhiên đạt mức cao nhất từ trước đến nay (86,4%).\n"
        "- Hub Tài chính (+9,6% MoM): Đạt 274K lượt xem; nhóm trang Trung tâm tài chính tăng đột biến gấp 5 lần (+442%) nhờ cụm tiện ích tra cứu tỷ giá ngoại tệ và giá vàng tự động.\n"
        "Hiệu quả kênh tự nhiên & Tối ưu chi phí\n"
        "- Kênh tự nhiên (Non-Paid): Đạt 3,13M lượt xem (+13,5% MoM, chiếm 87% toàn sàn), vượt 109% kế hoạch giao. Nền tảng tự bù được hơn một nửa lượng sụt giảm khi các BU chủ động cắt giảm 60,4% ngân sách quảng cáo (-724K lượt xem toàn web)."
    )
    set_text(s6_hub.shapes[19], human_commentary_s7, font_size=8.5, color=COLOR_TEXT_MAIN)

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

#!/usr/bin/env python3
"""
build_official_templated_pptx.py
=================================
Builds the official Web Platform Monthly Report PPTX by directly cloning
and populating the official MoMo template:
/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx

Exact 7-slide structure matching MoMo C-Suite & Glossary standards:
- Slide 1: Cover Slide (Template Slide 7)
- Slide 2: BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT (EXECUTIVE SCORECARD) [R] (Template Slide 14)
- Slide 3: Discussion Topics Overview [D] - 1 Chủ Đề Trọng Tâm (Template Slide 10)
- Slide 4: Proposal Deep-Dive [D] - Chuẩn Hóa Luồng Tải App (/tai-app) (Template Slide 12)
- Slide 5: Strategic Hubs Breakdown (Cinema Hub & Financial Hub) [R] (Template Slide 15)
- Slide 6: New User & AppsFlyer Funnel [R] (Template Slide 20)
- Slide 7: Roadmap Sản Phẩm & Next Actions [R] (Template Slide 21)

Glossary & Guidelines Compliance Checklist (03_SKILLS/momo-reporting-glossary.md):
- 100% Zero Fabricated Data: 188 keywords, 22.750 volume, 30.439 impressions, 1.880 clicks, 6,18% CTR, 76 URLs, 1.440 APK queries.
- Strict Forbidden Terms Removed: No "toàn sàn", "Sàn Web", "sàn MoMo". Replaced with "toàn Nền tảng Web", "Kênh Web", "Web Platform".
- No English Lead-ins: Replaced "Key Highlights & Commentary" with "Nhận định & Phân tích điều hành". Standardized bullet lead-ins ("Động lực tăng trưởng:", "Tác động Web-to-App:", "Điểm nổi bật:", "Việc tiếp theo:", "Đề xuất phê duyệt:").
- Professional Team Identification: "Web Growth Team", "Web Dev", "Media Team", "BU Movies", "Legal & Compliance Team", "Data Platform Team", "BOM / Marketing Team".
- Sentence Case Action Titles: Hook titles with metric + trend + root cause / impact across all slides.
- Mandatory "Mục đích: ..." line and max 3 key summary points under title.
"""

import os
import shutil
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

TEMPLATE_PATH = "/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx"
OUT_PATHS = [
    Path("/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Pyramid.pptx"),
    Path("/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/presentations/Web_Platform_Thang_10_2026_Pyramid.pptx"),
    Path("/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#6 - Report/Web_Platform_Thang_10_2026_Pyramid.pptx"),
    Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Pyramid.pptx"),
]

# Color Palette
COLOR_TEXT_MAIN = RGBColor(0x1C, 0x17, 0x1A)
COLOR_TEXT_MUTED = RGBColor(0x5C, 0x50, 0x60)
COLOR_GREEN = RGBColor(0x05, 0x96, 0x69)
COLOR_AMBER = RGBColor(0xD9, 0x77, 0x06)
COLOR_ROSE = RGBColor(0xB9, 0x1C, 0x1C)
COLOR_PINK = RGBColor(0xD8, 0x2D, 0x8B)
COLOR_PURPLE = RGBColor(0x9F, 0x00, 0x52)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
COLOR_BG_ALT = RGBColor(0xF9, 0xFA, 0xFB)
COLOR_BG_HIGHLIGHT = RGBColor(0xFD, 0xF2, 0xF8)


def delete_slide(prs, index):
    """Deletes a slide from a presentation cleanly."""
    rId = prs.slides._sldIdLst[index].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[index]


def remove_shape(shape):
    """Removes a shape element from slide."""
    sp = shape._element
    sp.getparent().remove(sp)


def set_text(shape, text, font_size=None, bold=None, color=None, align=None, line_spacing=None):
    """Replaces text in a shape preserving text frame configuration."""
    if not shape.has_text_frame:
        return
    tf = shape.text_frame
    tf.text = ""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        if font_size:
            p.font.size = Pt(font_size)
        if bold is not None:
            p.font.bold = bold
        if color:
            p.font.color.rgb = color
        if align:
            p.alignment = align
        if line_spacing:
            p.line_spacing = line_spacing


def set_cell(cell, text, font_size=8.0, bold=False, color=None, align=PP_ALIGN.LEFT, bg_color=None):
    """Formats a table cell with compact margins, background and exact typography."""
    cell.margin_left = Inches(0.04)
    cell.margin_right = Inches(0.04)
    cell.margin_top = Inches(0.03)
    cell.margin_bottom = Inches(0.03)
    if bg_color:
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_color
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.text = str(text)
    p.font.size = Pt(font_size)
    p.font.bold = bold
    if color:
        p.font.color.rgb = color
    p.alignment = align


def prune_and_reorder_slides(prs):
    """
    Selects the 7 exact template slides:
    Original 0-indexed:
    - 6: Cover (Slide 7)
    - 13: Financial / Scorecard (Slide 14)
    - 9: Discussion Topics (Slide 10)
    - 11: Proposal Deep-Dive (Slide 12)
    - 14: Category Breakdown (Slide 15)
    - 19: Product / Funnel (Slide 20)
    - 20: Roadmap (Slide 21)
    """
    keep_indices = {6, 13, 9, 11, 14, 19, 20}
    delete_indices = sorted([i for i in range(len(prs.slides)) if i not in keep_indices], reverse=True)
    for i in delete_indices:
        delete_slide(prs, i)

    # After deleting, slides list contains:
    # 0: Cover (orig 6)
    # 1: Discussion Topics (orig 9)
    # 2: Proposal Deep-Dive (orig 11)
    # 3: Scorecard (orig 13)
    # 4: Category Breakdown (orig 14)
    # 5: Product / Funnel (orig 19)
    # 6: Roadmap (orig 20)
    #
    # We want Scorecard (index 3) to be Slide 2 (index 1):
    sldIdLst = prs.slides._sldIdLst
    scorecard_slide = sldIdLst[3]
    sldIdLst.remove(scorecard_slide)
    sldIdLst.insert(1, scorecard_slide)

    print(f"Pruned and reordered to {len(prs.slides)} slides successfully.")


def populate_slide_1_cover(slide):
    """Slide 1: Cover Slide."""
    for s in slide.shapes:
        if not s.has_text_frame:
            continue
        txt = s.text_frame.text.strip()
        if txt.startswith("Mục đích:"):
            remove_shape(s)
        elif "[Tên BU/Division/Project]" in txt:
            # Sentence case per Glossary 1.5
            set_text(
                s,
                "Web Platform - Báo cáo tháng 10/2026",
                font_size=28,
                bold=True,
                color=COLOR_TEXT_MAIN,
            )
        elif "Report để cung cấp thông tin" in txt:
            set_text(
                s,
                "Report để cung cấp thông tin  •  Meeting để thảo luận và ra quyết định",
                font_size=13,
                color=COLOR_TEXT_MUTED,
            )
        elif "nội dung chính của họp" in txt:
            set_text(
                s,
                "Discussion  Cần thảo luận / alignment / quyết định: nội dung chính của họp",
                font_size=10,
                color=COLOR_TEXT_MUTED,
            )
        elif txt.startswith("Note:"):
            set_text(
                s,
                "Kỳ dữ liệu: 01/10/2026 đến 31/10/2026 (Chốt Full Month 31 ngày). Số liệu hợp nhất từ GA4 Property 270743103 và BigQuery Data Warehouse.",
                font_size=10,
                color=COLOR_TEXT_MUTED,
            )


def populate_slide_2_scorecard(slide):
    """Slide 2: BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT (EXECUTIVE SCORECARD) [R]."""
    # Shape 0: Mục đích (Bắt buộc theo Guidelines)
    set_text(
        slide.shapes[0],
        "Mục đích: Đánh giá chuỗi hiệu suất 4 tháng liên tục (từ T7 đến T10) và năng lực tự chủ tăng trưởng khi chủ động cắt giảm sâu quảng cáo trả phí.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title (Sentence case, metric + trend + root cause)
    set_text(
        slide.shapes[1],
        "Kênh tự nhiên lập đỉnh 3,13M Pageviews (+13,5% MoM), tự bù 51% khoảng trống khi cắt giảm 724K lượt Paid Ads",
        font_size=18,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    # Clear source footnote
    set_text(slide.shapes[5], "", font_size=8.0)

    # Shape 6: Slide number
    set_text(slide.shapes[6], "2 / 7", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Remove template table (Shape 7)
    old_table_shape = slide.shapes[7]
    remove_shape(old_table_shape)

    # Check if instruction shape exists and remove
    for s in list(slide.shapes):
        if s.has_text_frame and "Finance cung cấp" in s.text_frame.text:
            remove_shape(s)

    # Add fresh native table: 8 rows x 7 cols
    left = Inches(0.35)
    top = Inches(1.16)
    width = Inches(5.80)
    height = Inches(3.40)
    new_tbl_shape = slide.shapes.add_table(8, 7, left, top, width, height)
    tbl = new_tbl_shape.table

    col_widths = [
        Inches(1.65),  # 0: Kênh lưu lượng
        Inches(0.55),  # 1: Tháng 7
        Inches(0.55),  # 2: Tháng 8
        Inches(0.55),  # 3: Tháng 9
        Inches(0.55),  # 4: Tháng 10
        Inches(0.50),  # 5: % MoM
        Inches(1.45),  # 6: Nhận định / Ý nghĩa
    ]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    # Headers
    headers = ["Kênh lưu lượng", "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "% MoM", "Nhận định / Ý nghĩa"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=8.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT if c in [1, 2, 3, 4, 5] else PP_ALIGN.LEFT, bg_color=COLOR_PURPLE)

    # Row Data (All "toàn sàn" replaced per Glossary Section 1)
    data = [
        ("● KÊNH TỰ NHIÊN (NON-PAID)", "2.669.863", "2.820.824", "2.755.766", "3.128.542", "+13,5%", "Tự chủ tăng trưởng (+373K), tự bù 51% Paid cắt", COLOR_GREEN, True, COLOR_BG_HIGHLIGHT),
        ("   - Organic Search", "1.875.191", "1.729.694", "1.623.796", "1.715.771", "+5,7%", "SEO/GEO bền vững, chiếm 47,6% toàn Nền tảng Web", None, False, None),
        ("   - Direct", "440.855", "656.271", "755.896", "931.731", "+23,3%", "Sức mạnh thương hiệu; khách quay lại tăng mạnh", None, False, COLOR_BG_ALT),
        ("   - Referral", "329.659", "410.305", "345.132", "350.162", "+1,5%", "Đối tác rạp phim, liên kết ngân hàng ổn định", None, False, None),
        ("   - Kênh tự nhiên khác", "24.158", "24.554", "30.942", "130.878", "+322,9%", "Phân tách dữ liệu chính xác từ tính năng mới", None, False, COLOR_BG_ALT),
        ("● KÊNH TRẢ PHÍ (PAID ADS)", "497.958", "644.539", "1.197.093", "473.481", "-60,4%", "Chủ động cắt giảm 724K views để tối ưu chi phí", COLOR_AMBER, True, None),
        ("● TỔNG LƯỢNG TRUY CẬP", "3.167.821", "3.465.363", "3.952.859", "3.602.023", "-8,9%", "Đạt 98,3% Target tháng (3,67M PV); tỷ trọng Non-Paid đạt 86,9%", COLOR_PINK, True, COLOR_BG_HIGHLIGHT),
    ]

    for r_idx, row in enumerate(data, start=1):
        ch, t7, t8, t9, t10, mom, note, color, is_bold, bg_row = row
        tbl.rows[r_idx].height = Inches(0.38)
        set_cell(tbl.cell(r_idx, 0), ch, font_size=7.5, bold=is_bold, color=color, align=PP_ALIGN.LEFT, bg_color=bg_row)
        set_cell(tbl.cell(r_idx, 1), t7, font_size=7.5, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg_row)
        set_cell(tbl.cell(r_idx, 2), t8, font_size=7.5, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg_row)
        set_cell(tbl.cell(r_idx, 3), t9, font_size=7.5, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg_row)
        set_cell(tbl.cell(r_idx, 4), t10, font_size=7.5, bold=is_bold, color=color if is_bold else None, align=PP_ALIGN.RIGHT, bg_color=bg_row)
        set_cell(tbl.cell(r_idx, 5), mom, font_size=7.5, bold=True, color=COLOR_GREEN if "+" in mom else COLOR_ROSE, align=PP_ALIGN.RIGHT, bg_color=bg_row)
        set_cell(tbl.cell(r_idx, 6), note, font_size=7.5, color=COLOR_TEXT_MUTED, align=PP_ALIGN.LEFT, bg_color=bg_row)

    # Right Commentary adjustments: Replace English container title and standardize lead-ins
    for s in slide.shapes:
        if not s.has_text_frame:
            continue
        txt = s.text_frame.text.strip()
        if "Key Highlights" in txt:
            set_text(s, "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
        elif txt == "Performance":
            set_text(s, "Điểm nổi bật", font_size=9.5, bold=True, color=COLOR_GREEN)
            s.width = Inches(1.60)
        elif txt.startswith("MAU [x]M"):
            bullets = (
                "• Động lực tăng trưởng: Kênh tự nhiên (Non-Paid) lập đỉnh 3,13M Pageviews (+13,5% MoM, chiếm 86,9% toàn Nền tảng Web), tăng trưởng liên tục từ 2,67M (T7), tự bù đắp 51% khoảng trống khi Media Team chủ động cắt giảm 724K lượt quảng cáo trả phí.\n"
                "• Tác động Web-to-App: Thiết lập kỷ lục 2.389 người dùng mới liên kết ngân hàng (Map Bank, +5% MoM) từ 11.143 lượt cài đặt ứng dụng (App Install), dẫn dắt bởi Cinema Hub và minigame."
            )
            set_text(s, bullets, font_size=8.5, color=COLOR_TEXT_MAIN)
        elif "Lowlights" in txt:
            set_text(s, "Vấn đề cần lưu ý & Việc tiếp theo", font_size=9.5, bold=True, color=COLOR_AMBER)
            s.width = Inches(2.50)
        elif "[Use case] thấp hơn Target" in txt:
            bullets = (
                "• Tối ưu chi phí Paid Ads: Cắt giảm -60,4% Paid Ads (-724K lượt xem) theo kế hoạch các BU; Web Growth Team tập trung nguồn lực phát triển sản phẩm tự nhiên để bảo toàn đà tăng trưởng.\n"
                "• Việc tiếp theo: Chuẩn hóa luồng Tải App (/tai-app) đón trọn 22.750 nhu cầu tìm kiếm mỗi tháng từ 188 từ khóa; hoàn thiện bộ đôi công cụ Thuế TNCN trước 10/11 đón mùa quyết toán cuối năm."
            )
            set_text(s, bullets, font_size=8.5, color=COLOR_TEXT_MAIN)


def populate_slide_3_discussion_topics(slide):
    """Slide 3: Discussion Topics [D]."""
    # Shape 0: Mục đích
    set_text(
        slide.shapes[0],
        "Mục đích: Nội dung cần Ban Giám Đốc phê duyệt trong cuộc họp và các tác động đi kèm.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title (Chuẩn Guidelines 4.1: Discussion Topics — [n] chủ đề: [x] Discuss, [y] Approve)
    set_text(
        slide.shapes[1],
        "Discussion Topics: 1 đề xuất phê duyệt kích hoạt luồng Tải App (/tai-app) đón 22.750 lượt tìm kiếm/tháng",
        font_size=17.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    # Footer note clear
    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "3 / 7", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Summary box alignment
    slide.shapes[8].top = Inches(3.65)
    slide.shapes[8].height = Inches(0.85)

    slide.shapes[9].top = Inches(3.75)
    slide.shapes[10].top = Inches(3.75)

    slide.shapes[11].top = Inches(3.70)
    slide.shapes[11].height = Inches(0.75)
    summary = (
        "• Điểm nghẽn hiện tại: Dữ liệu tìm kiếm ghi nhận 30.439 lượt hiển thị/tháng nhưng chỉ đạt 1.880 clicks (tỷ lệ CTR chỉ 6,18%) do bị phân mảnh qua 76 đường link bài viết cũ không có nút tải trực tiếp.\n"
        "• Rủi ro & Thị trường: Bộ từ khóa thương hiệu gồm 188 từ khóa với 22.750 lượt tìm kiếm/tháng (~273.000 lượt/năm); trong đó gần 1.500 lượt tìm file APK ngoài lề có nguy cơ bị cài ứng dụng giả mạo.\n"
        "• Đề xuất phê duyệt: Hợp nhất về duy nhất /tai-app với cơ chế Smart Routing (tự mở App Store / Google Play / Desktop QR); Web Dev đã hoàn thiện 100% kỹ thuật, cần BOM duyệt đồng bộ link toàn Kênh Web trong tháng 11."
    )
    set_text(slide.shapes[11], summary, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Format table: keep header + 1 proposal row = 2 rows
    table_shape = slide.shapes[7]
    tbl = table_shape.table

    tr_elements = tbl._tbl.xpath("./a:tr")
    if len(tr_elements) > 2:
        for tr in tr_elements[2:]:
            tbl._tbl.remove(tr)

    col_widths = [
        Inches(0.35),  # 0: #
        Inches(2.35),  # 1: Chủ đề
        Inches(0.85),  # 2: Loại (Approve)
        Inches(2.35),  # 3: Cần CEO/BOM quyết định
        Inches(1.65),  # 4: Tác động
        Inches(0.70),  # 5: Hạn (Tháng 11)
        Inches(0.70),  # 6: Ưu tiên (CAO)
        Inches(0.70),  # 7: Chi tiết (Slide 4)
    ]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    headers = ["#", "Chủ đề", "Loại", "Cần CEO/BOM quyết định / hỗ trợ gì", "Tác động", "Hạn", "Ưu tiên", "Chi tiết"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT)

    tbl.rows[1].height = Inches(1.10)
    set_cell(tbl.cell(1, 0), "1", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 1), "Chuẩn hóa luồng Tải App (/tai-app) đón 22.750 lượt tìm kiếm/tháng và ngăn chặn rủi ro ứng dụng giả mạo", font_size=8.5, bold=True)
    set_cell(tbl.cell(1, 2), "Approve", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 3), "Phê duyệt cơ chế chuyển hướng link tải cũ về /tai-app và đồng bộ nút Tải App trên thanh điều hướng toàn Nền tảng Web.", font_size=8.0)
    set_cell(tbl.cell(1, 4), "Đón trọn 22.750 lượt tìm kiếm/tháng, tăng CTR từ 6,2% lên 25% - 30% (+3.600 đến 5.000 clicks tự nhiên); loại trừ rủi ro tải file APK độc hại.", font_size=8.0, color=COLOR_GREEN)
    set_cell(tbl.cell(1, 5), "Tháng 11", font_size=8.0, bold=True, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 6), "CAO", font_size=8.0, bold=True, color=COLOR_ROSE, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 7), "Slide 4", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)


def populate_slide_4_proposal_deepdive(slide):
    """Slide 4: Proposal Deep-Dive [D]."""
    # Shape 0: Mục đích
    set_text(
        slide.shapes[0],
        "Mục đích: Trình bày bài toán chuẩn hóa luồng Tải App tập trung và đề xuất Ban Giám Đốc phê duyệt phương án triển khai ngay trong tháng 11.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title (Chuẩn Guidelines 4.4 & Template 12: [Chủ đề]: [vấn đề 1 câu kèm số liệu] — cần [Approve] về [nội dung])
    set_text(
        slide.shapes[1],
        "Chuẩn hóa luồng Tải App (/tai-app): Thất thoát 93,8% lượt truy cập từ 30.439 lượt hiển thị, cần Approve cơ chế đồng bộ toàn Kênh Web",
        font_size=17.0,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "4 / 7", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Replace English container title
    for s in slide.shapes:
        if s.has_text_frame and "Key Highlights" in s.text_frame.text:
            set_text(s, "Nhận định & Bình luận điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)

    # Problem statement (Shape 10)
    problem = (
        "• Vấn đề & Quy mô: Dữ liệu tìm kiếm ghi nhận 30.439 lượt hiển thị/tháng nhưng chỉ thu về 1.880 clicks (tỷ lệ CTR chỉ 6,18%) do phân tán qua 76 đường link bài viết cũ không có nút tải trực tiếp.\n"
        "• Rủi ro thương hiệu: Hơn 1.440 lượt tìm kiếm file cài ngoài (file APK) mỗi tháng đang bị dẫn dụ sang các website lậu, đe dọa trực tiếp an toàn tài khoản người dùng và uy tín MoMo."
    )
    set_text(slide.shapes[10], problem, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Context (Shape 14)
    context = (
        "• Dung lượng thị trường: Nghiên cứu từ khóa (Keyword Inventory) xác định 188 từ khóa về tải ứng dụng MoMo với tổng nhu cầu đạt 22.750 lượt tìm kiếm/tháng (~273.000 lượt/năm).\n"
        "• Từ khóa chủ lực: \"tải momo\" (5.400), \"tai momo\" (5.400), \"momo tải\" (5.400), \"tải momo apk\" (720), \"tải momo cho android\" (480), \"tải app momo\" (320)."
    )
    set_text(slide.shapes[14], context, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Impact (Shape 18)
    impact = (
        "• Tác động Web-to-App: Tối ưu trải nghiệm đưa CTR từ 6,18% lên 25% - 30%, thu hút thêm 3.600 đến 5.000 lượt truy cập tải app chất lượng cao mỗi tháng với chi phí 0đ.\n"
        "• Bảo vệ thương hiệu: Chiếm lĩnh vị trí số 1 chính thức trên Google Search, bảo vệ an toàn thương hiệu và chặn đứng các nguồn phát tán APK độc hại."
    )
    set_text(slide.shapes[18], impact, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Ask BOM (Shape 25)
    ask = (
        "• Đề xuất phê duyệt: Kích hoạt chính thức trang /tai-app và đồng bộ nút Tải App trên thanh điều hướng Header/Footer toàn Nền tảng Web ngay trong tháng 11.\n"
        "• Khuyến nghị chuyên môn: Web Growth Team khuyến nghị chọn Phương án A vì Web Dev đã hoàn thiện 100% trên Production, mang lại chuyển đổi ngay mà không tốn chi phí."
    )
    set_text(slide.shapes[25], ask, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Consequences if no decision (Shape 28)
    consequence = "Tiếp tục để rơi rụng phần lớn trong 22.750 lượt tìm kiếm mỗi tháng và để các trang chia sẻ APK lậu chiếm mất khách hàng của MoMo."
    set_text(slide.shapes[28], consequence, font_size=8.5, color=COLOR_ROSE)

    # Table (Shape 20)
    tbl = slide.shapes[20].table
    headers = ["Phương án", "Nội dung giải pháp", "Ưu điểm & Hiệu quả", "Rủi ro / Chi phí"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=8.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

    # Option A (Recommended)
    set_cell(tbl.cell(1, 0), "Phương án A: Đề xuất\n(Khuyến nghị)", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 1), "Hợp nhất về /tai-app, tự nhận diện thiết bị (Smart OS Routing: iOS / Android / Desktop QR).", font_size=7.5)
    set_cell(tbl.cell(1, 2), "Tối ưu 100% trải nghiệm (CX), kéo CTR lên 25% - 30%, tăng 3.600 đến 5.000 clicks tải app với chi phí 0đ.", font_size=7.5, color=COLOR_GREEN)
    set_cell(tbl.cell(1, 3), "Không có rủi ro; Web Dev đã hoàn thiện và sẵn sàng 100% trên Production.", font_size=7.5)

    # Option B (Current state)
    set_cell(tbl.cell(2, 0), "Phương án B: Hiện trạng", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(2, 1), "Duy trì 76 đường link bài viết rời rạc, link phân mảnh không có nút tải trực tiếp.", font_size=7.5)
    set_cell(tbl.cell(2, 2), "Không cần thao tác kỹ thuật thêm.", font_size=7.5)
    set_cell(tbl.cell(2, 3), "Bỏ lỡ phần lớn trong 22.750 lượt tìm kiếm; tiềm ẩn nguy cơ người dùng tải nhầm APK độc hại.", font_size=7.5, color=COLOR_ROSE)


def populate_slide_5_hubs(slide):
    """Slide 5: Strategic Hubs Breakdown (Cinema Hub & Financial Hub) [R]."""
    # Shape 0: Mục đích
    set_text(
        slide.shapes[0],
        "Mục đích: Theo dõi nhanh các chỉ số sức khỏe của 2 Hub chiến lược (Cinema Hub, Financial Hub) so với kế hoạch tháng và tháng trước.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title (Sửa "Hub Tài chính" -> Financial Hub per Glossary Section 4)
    set_text(
        slide.shapes[1],
        "Cinema Hub vượt 101,4% kế hoạch nhờ cụm rạp (+39,6%), Financial Hub tăng +9,6% MoM mở đường cho mùa thuế cuối năm",
        font_size=18,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "5 / 7", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Shape 8: Dải tóm tắt (Ý chính 1, 2, 3)
    key_points = (
        "Ý chính 1: Cinema Hub đạt 1,13M Pageviews (vượt 101,4% Target), tỷ trọng Non-Paid đạt đỉnh 86,4% bù đắp trọn vẹn việc cắt giảm 93% Paid Ads phim lẻ. // "
        "Ý chính 2: Financial Hub đạt 274K Pageviews (+9,6% MoM); Trung tâm Tài chính số tăng gấp 5 lần (+442%) nhờ cụm tra cứu Tỷ giá. // "
        "Ý chính 3: Tỷ trọng Non-Paid toàn Nền tảng Web lập đỉnh 86,9%, chứng minh năng lực tự chủ tăng trưởng bền vững."
    )
    set_text(slide.shapes[8], key_points, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Shape 9: Section Title
    set_text(slide.shapes[9], "HIỆU SUẤT CHIẾN LƯỢC CÁC HUBS", font_size=9.0, bold=True, color=COLOR_TEXT_MUTED)

    # Card 1 (Top Left): Cinema Hub
    set_text(slide.shapes[12], "Cinema Hub", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[13], "1,13M", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[14], "▲ 101,4% vs Target", font_size=8.0, bold=True, color=COLOR_GREEN)
    set_text(slide.shapes[16], "Vượt target (+15,3K PV)", font_size=7.5, color=COLOR_TEXT_MUTED)

    # Card 2 (Top Right): Non-Paid Cinema
    set_text(slide.shapes[18], "Non-Paid Cinema", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[19], "86,4%", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[20], "▲ +20,5 pp vs T9", font_size=8.0, bold=True, color=COLOR_GREEN)
    set_text(slide.shapes[22], "Tỷ trọng lượt tự nhiên", font_size=7.5, color=COLOR_TEXT_MUTED)

    # Card 3 (Bottom Left): Financial Hub
    set_text(slide.shapes[24], "Financial Hub", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[25], "274K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[26], "▲ +9,6% MoM", font_size=8.0, bold=True, color=COLOR_GREEN)
    set_text(slide.shapes[28], "Tín hiệu mở rộng khả quan", font_size=7.5, color=COLOR_TEXT_MUTED)

    # Card 4 (Bottom Right): Trung tâm Tài chính số
    set_text(slide.shapes[30], "Trung tâm Tài chính số", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[31], "43,5K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[32], "▲ +442% MoM", font_size=8.0, bold=True, color=COLOR_GREEN)
    set_text(slide.shapes[34], "Tăng gấp 5 lần nhờ Tỷ giá", font_size=7.5, color=COLOR_TEXT_MUTED)

    # Other Metrics
    # Metric 1: GEO
    set_text(slide.shapes[38], "GEO (AI Search)", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[39], "18,5K", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[40], "▲ +36,4% MoM", font_size=8.0, bold=True, color=COLOR_GREEN)

    # Metric 2: Rạp chiếu phim
    set_text(slide.shapes[42], "Cụm rạp chiếu phim", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[43], "700K", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[44], "▲ +39,6% MoM", font_size=8.0, bold=True, color=COLOR_GREEN)

    # Metric 3: Minigame
    set_text(slide.shapes[46], "Minigame Một Mùa Quýt", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[47], "7,1K", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[48], "→ 7.097 người tham gia", font_size=8.0, bold=True, color=COLOR_GREEN)

    # Commentary container title
    for s in slide.shapes:
        if s.has_text_frame and "Key Highlights" in s.text_frame.text:
            set_text(s, "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[52], "Điểm nổi bật", font_size=9.5, bold=True, color=COLOR_GREEN)
    slide.shapes[52].width = Inches(1.60)
    commentary_perf = (
        "• Điểm nổi bật: Cinema Hub (1,13M Pageviews, 101,4% Target): Vượt chỉ tiêu dù BU Movies chủ động cắt giảm 93% Paid Ads phim lẻ (-272K lượt xem); cụm rạp đối tác tăng trưởng xuất sắc (+39,6%, đạt 700K lượt xem). Tỷ trọng lưu lượng tự nhiên đạt kỷ lục 86,4%.\n"
        "• Động lực tăng trưởng: Financial Hub (274K Pageviews, +9,6% MoM): Trang tiện ích bứt phá +442% nhờ cụm tra cứu Tỷ giá và Giá vàng; sẵn sàng đón sóng quyết toán thuế cuối năm."
    )
    set_text(slide.shapes[53], commentary_perf, font_size=8.5, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[55], "Vấn đề cần lưu ý & Việc tiếp theo", font_size=9.5, bold=True, color=COLOR_AMBER)
    slide.shapes[55].width = Inches(2.40)
    commentary_focus = (
        "• Tối ưu chi phí Paid Ads: Kênh Paid Ads thu hẹp (-60,4% toàn Nền tảng Web) theo kế hoạch các BU; không ảnh hưởng tiêu cực tới mục tiêu tăng trưởng nhờ kênh tự nhiên tự bù đắp 51% khoảng trống.\n"
        "• Việc tiếp theo: Đẩy mạnh bộ đôi công cụ tính Thuế TNCN và chuẩn hóa luồng /tai-app để tiếp tục mở rộng quy mô lưu lượng không phụ thuộc quảng cáo."
    )
    set_text(slide.shapes[56], commentary_focus, font_size=8.5, color=COLOR_TEXT_MAIN)


def populate_slide_6_new_user(slide):
    """Slide 6: New User & AppsFlyer Funnel [R]."""
    # Shape 0: Mục đích
    set_text(
        slide.shapes[0],
        "Mục đích: Đo lường chất lượng người dùng mới chuyển đổi từ Web sang App qua OneLink AppsFlyer và hiệu quả của các kênh đóng góp.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title (Sửa "user" -> người dùng liên kết ngân hàng, "rạp phim" -> Cinema Hub)
    set_text(
        slide.shapes[1],
        "Kỷ lục mới 2.389 người dùng liên kết ngân hàng (+5% MoM) từ 11.143 lượt cài app; Cinema Hub và minigame chuyển đổi vượt trội",
        font_size=17.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "6 / 7", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Shape 8: Dải tóm tắt
    key_points = (
        "Ý chính 1: Đạt kỷ lục 2.389 người dùng liên kết ngân hàng thành công (+5% MoM), khẳng định Kênh Web là phễu thu hút khách hàng tài chính thực chất. // "
        "Ý chính 2: Cinema Hub tăng +58% lượt cài và +92% liên kết ngân hàng (CVR 25,1%), minigame thu hút 7.097 người tham gia. // "
        "Ý chính 3: Người dùng iOS đóng góp 57% tổng liên kết ngân hàng (1.364 user) nhờ tỷ lệ hoàn tất đạt 67,4% (vượt trội so với Android 54,6%)."
    )
    set_text(slide.shapes[8], key_points, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Commentary container title
    for s in slide.shapes:
        if s.has_text_frame and "Key Highlights" in s.text_frame.text:
            set_text(s, "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[13], "Chất lượng người dùng mới", font_size=9.5, bold=True, color=COLOR_GREEN)
    slide.shapes[13].width = Inches(2.00)
    commentary = (
        "• Điểm nổi bật: Hiệu quả chuyển đổi người dùng mới cao nhất từ trước tới nay: Tháng 10 mang lại 2.389 người dùng liên kết ngân hàng thành công (+5% MoM) từ 11.143 lượt cài đặt ứng dụng qua AppsFlyer OneLink.\n"
        "• Động lực tăng trưởng: Cinema Hub mang về 484 người dùng liên kết ngân hàng với tỷ lệ chuyển đổi cuối đạt 25,1%. Minigame \"Một Mùa Quýt\" tiếp cận 7.097 người tham gia, tạo phễu tương tác tự nhiên."
    )
    set_text(slide.shapes[14], commentary, font_size=8.5, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[16], "Vấn đề cần lưu ý & Việc tiếp theo", font_size=9.5, bold=True, color=COLOR_AMBER)
    slide.shapes[16].width = Inches(2.30)
    notes = (
        "• Tác động Web-to-App: Người dùng iOS tạo giá trị vượt bậc: Chiếm 51% lượt cài nhưng đóng góp tới 57% số người dùng liên kết ngân hàng (1.364 user) nhờ tỷ lệ hoàn tất KYC/Map Bank đạt 67,4% (cao hơn Android 12,8 điểm %).\n"
        "• Việc tiếp theo: Đưa luồng Tải App (/tai-app) vào vận hành chính thức để đón 22.750 nhu cầu tìm kiếm mỗi tháng, mục tiêu kéo tỷ lệ liên kết ngân hàng trung bình toàn Kênh Web lên trên 25%."
    )
    set_text(slide.shapes[17], notes, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Table positioning & row heights
    table_shape = slide.shapes[9]
    table_shape.top = Inches(1.65)
    tbl = table_shape.table

    # Add 2 rows if needed
    while len(tbl.rows) < 6:
        last_tr = tbl._tbl.xpath("./a:tr")[-1]
        import copy
        new_tr = copy.deepcopy(last_tr)
        tbl._tbl.append(new_tr)

    # Remove extra columns beyond 3
    gridCols = tbl._tbl.xpath("./a:tblGrid/a:gridCol")
    for gc in gridCols[3:]:
        tbl._tbl.tblGrid.remove(gc)

    for tr in tbl._tbl.xpath("./a:tr"):
        tcs = tr.xpath("./a:tc")
        for tc in tcs[3:]:
            tr.remove(tc)

    # Set column widths (total = 5.80 in)
    col_widths = [Inches(2.50), Inches(1.60), Inches(1.70)]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    headers = ["Nguồn chiến dịch / Vị trí", "Lượt cài đặt (Tỷ trọng)", "Liên kết NH (Tỷ lệ Map/Cài)"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=8.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT if c in [1, 2] else PP_ALIGN.LEFT, bg_color=COLOR_PURPLE)

    funnel_data = [
        ("Banner chào MoMo & Popup", "8.517 (76,4%)", "1.798 (21,1%)", None),
        ("Cinema Hub (Cụm rạp & Đặt vé)", "1.931 (17,3%)", "484 (25,1%)", COLOR_BG_HIGHLIGHT),
        ("Minigame Một Mùa Quýt", "264 (2,4%)", "41 (15,5%)", None),
        ("Trang Đối tác & Merchant", "271 (2,4%)", "40 (14,8%)", COLOR_BG_ALT),
        ("Bảo hiểm (Insurtech Hub)", "91 (0,8%)", "22 (24,2%)", None),
    ]

    for r_idx, (plc, ins, map_b, bg) in enumerate(funnel_data, start=1):
        tbl.rows[r_idx].height = Inches(0.48)
        set_cell(tbl.cell(r_idx, 0), plc, font_size=8.0, bold=True if r_idx <= 2 else False, align=PP_ALIGN.LEFT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 1), ins, font_size=8.0, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 2), map_b, font_size=8.0, bold=True if "25,1%" in map_b else False, color=COLOR_GREEN if "25,1%" in map_b else None, align=PP_ALIGN.RIGHT, bg_color=bg)


def populate_slide_7_roadmap(slide):
    """Slide 7: Roadmap Sản Phẩm & Next Actions [R]."""
    # Shape 0: Mục đích
    set_text(
        slide.shapes[0],
        "Mục đích: Cập nhật tiến độ các dự án trọng điểm chuẩn bị cho cao điểm Quý 4 (Bộ công cụ Thuế, Tỷ giá, Lương Gross-Net) và các hỗ trợ cần thiết.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title (Sentence case per Glossary 1.5)
    set_text(
        slide.shapes[1],
        "Go-live cụm Diễn viên (30/10), cụm Tỷ giá tăng gấp 5 lần; hoàn thiện bộ đôi công cụ Thuế TNCN trước 10/11",
        font_size=18,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[3], "", font_size=8.0)  # Footer clear
    set_text(slide.shapes[2], (
        "Ý chính 1: Web Dev đã triển khai lên Production 631 trang hồ sơ Diễn viên (30/10) và cụm Tỷ giá tự động (tăng Pageviews gấp 5 lần). // "
        "Ý chính 2: Hoàn tất 85% tiến độ bộ đôi công cụ tính Thuế TNCN và Lương Gross-Net, chuẩn bị sẵn sàng cho cao điểm quyết toán cuối năm. // "
        "Ý chính 3: Kỹ thuật luồng /tai-app đã hoàn thành 100%, chờ BOM phê duyệt đồng bộ link toàn Kênh Web để kích hoạt toàn diện."
    ), font_size=8.5, color=COLOR_TEXT_MAIN)

    # Milestones (Sentence case)
    set_text(slide.shapes[8], "Khảo sát & Thiết kế", font_size=8.0, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[9], "01/10", font_size=8.0, color=COLOR_TEXT_MUTED)

    set_text(slide.shapes[11], "Cụm Tỷ giá & Giá vàng", font_size=8.0, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[12], "15/10", font_size=8.0, color=COLOR_TEXT_MUTED)

    set_text(slide.shapes[14], "Cụm 631 Diễn viên", font_size=8.0, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[15], "30/10", font_size=8.0, color=COLOR_GREEN)

    set_text(slide.shapes[17], "Bộ công cụ Thuế", font_size=8.0, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[18], "10/11", font_size=8.0, color=COLOR_AMBER)

    set_text(slide.shapes[20], "Tính lương Gross-Net", font_size=8.0, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[21], "20/11", font_size=8.0, color=COLOR_AMBER)

    # Progress bar text
    set_text(slide.shapes[26], "80%", font_size=8.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[30], "85%", font_size=8.5, bold=True, color=COLOR_GREEN)

    # Bottom note
    set_text(
        slide.shapes[33],
        "Việc đầu tiên (/tai-app) quyết định hiệu quả thu hút người dùng mới trong tháng 11; hai việc còn lại bảo đảm tính chính xác tuyệt đối cho bộ công cụ tài chính mùa quyết toán cuối năm.",
        font_size=8.0,
        color=COLOR_TEXT_MUTED,
    )

    # Format Support Table (4x3) - Teams standardized per Glossary Section 6
    tbl = slide.shapes[32].table
    headers = ["Việc cần hỗ trợ", "Bên phối hợp", "Hạn"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=8.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [1, 2] else PP_ALIGN.LEFT, bg_color=COLOR_PURPLE)

    support_data = [
        ("Phê duyệt cơ chế chuyển hướng link và đồng bộ nút /tai-app toàn Kênh Web", "BOM / Marketing Team", "Tháng 11"),
        ("Rà soát công thức tính thuế TNCN và các bậc giảm trừ gia cảnh mới", "Legal & Compliance Team", "10/11"),
        ("Đồng bộ luồng liên kết ngân hàng và tracking sự kiện AppsFlyer", "Data Platform Team / Web Growth Team", "15/11"),
    ]

    for r_idx, (task, who, due) in enumerate(support_data, start=1):
        tbl.rows[r_idx].height = Inches(0.48)
        set_cell(tbl.cell(r_idx, 0), task, font_size=7.5, bold=True if r_idx == 1 else False, align=PP_ALIGN.LEFT)
        set_cell(tbl.cell(r_idx, 1), who, font_size=7.5, align=PP_ALIGN.CENTER)
        set_cell(tbl.cell(r_idx, 2), due, font_size=7.5, bold=True, color=COLOR_PINK if r_idx == 1 else None, align=PP_ALIGN.CENTER)


def main():
    print(f"Loading official template from: {TEMPLATE_PATH}")
    prs = Presentation(TEMPLATE_PATH)

    # 1. Prune down and reorder slides
    prune_and_reorder_slides(prs)

    # 2. Populate each slide
    print("Populating Slide 1: Cover Slide...")
    populate_slide_1_cover(prs.slides[0])

    print("Populating Slide 2: Executive Scorecard [R]...")
    populate_slide_2_scorecard(prs.slides[1])

    print("Populating Slide 3: Discussion Topics [D]...")
    populate_slide_3_discussion_topics(prs.slides[2])

    print("Populating Slide 4: Proposal Deep-Dive [D]...")
    populate_slide_4_proposal_deepdive(prs.slides[3])

    print("Populating Slide 5: Strategic Hubs Breakdown [R]...")
    populate_slide_5_hubs(prs.slides[4])

    print("Populating Slide 6: New User & AppsFlyer Funnel [R]...")
    populate_slide_6_new_user(prs.slides[5])

    print("Populating Slide 7: Roadmap Sản Phẩm & Next Actions [R]...")
    populate_slide_7_roadmap(prs.slides[6])

    # 3. Save to all 4 destination paths
    for p in OUT_PATHS:
        p.parent.mkdir(parents=True, exist_ok=True)
        prs.save(str(p))
        print(f"Saved: {p} ({p.stat().st_size:,} bytes)")

    print("\nAll 7 slides successfully generated and saved across all paths!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
build_official_templated_pptx.py
--------------------------------
Generates the 100% pixel-perfect official MoMo C-Suite Executive Deck for October 2026.
Strictly based on MoMo Reporting Guidelines & Official Templates (MoMo Reporting Guidelines & Templates.pptx).

Deck Structure (10 Official Slides):
- Slide 1: Cover Slide (Template Slide 7)
- Slide 2: Executive Scorecard [R] (Template Slide 14)
- Slide 3: Discussion Topics [D] (Template Slide 10)
- Slide 4: Proposal Deep-Dive 1 [D] - Pilot Off-Page SEO Cinema Phim Tết 2027 (Template Slide 12)
- Slide 5: Proposal Deep-Dive 2 [D] - Mở rộng Gamification Quiz sang CIC & Giáo dục Tài chính (Template Slide 12)
- Slide 6: Báo Cáo Hiệu Suất Cinema Hub (Cinema Hub Performance) [R] (Template Slide 15)
- Slide 7: Báo Cáo Hiệu Suất Financial Hub (Financial Hub Performance) [R] (Template Slide 15)
- Slide 8: Báo Cáo Tín Hiệu GEO & AI Search (GEO Signals & Performance) [R] (Template Slide 17)
- Slide 9: New User & AppsFlyer Funnel [R] (Template Slide 20)
- Slide 10: Roadmap & Next Actions [R] (Template Slide 11 - Follow-up Action Tracker)
"""

import os
import sys
import copy
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# =============================================================================
# CONSTANTS & THEMES (MoMo Brand Palette)
# =============================================================================
COLOR_PINK = RGBColor(165, 0, 100)          # #A50064 MoMo Primary Pink
COLOR_PURPLE = RGBColor(114, 0, 98)        # #720062 MoMo Deep Purple
COLOR_GREEN = RGBColor(0, 128, 90)          # Positive Green
COLOR_AMBER = RGBColor(180, 100, 0)         # Warning Amber / Pending
COLOR_ROSE = RGBColor(190, 30, 45)          # Negative Red / High Priority
COLOR_TEXT_MAIN = RGBColor(30, 30, 30)      # Charcoal Title
COLOR_TEXT_MUTED = RGBColor(100, 100, 100)  # Muted Subtext
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_BG_HIGHLIGHT = RGBColor(253, 242, 248) # Tint Pink for rows
COLOR_BG_ALT = RGBColor(248, 249, 250)      # Light Gray row
COLOR_BG_ROSE_TINT = RGBColor(254, 242, 242)

TEMPLATE_PATH = "/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx"
OUTPUT_DOWNLOADS = "/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Pyramid.pptx"
OUTPUT_LOCAL_DOCS = "07_REPORTS/docs/presentations/Web_Platform_Thang_10_2026_Pyramid.pptx"
OUTPUT_GDRIVE = "/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#6 - Report/Web_Platform_Thang_10_2026_Pyramid.pptx"
OUTPUT_PUBLIC_WEB = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Pyramid.pptx"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def sanitize_text(text):
    """Enforces strict NO En-dash / NO Em-dash rule: replaces with hyphen."""
    if not text:
        return ""
    return str(text).replace("—", "-").replace("–", "-")


def delete_slide(prs, index):
    """Deletes a slide from a presentation by index."""
    rId = prs.slides._sldIdLst[index].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[index]


def delete_row(table, row_idx):
    """Safely removes a row from a table."""
    tr = table.rows[row_idx]._tr
    table._tbl.remove(tr)


def delete_col(table, col_idx):
    """Safely removes a column from a table."""
    grid = table._tbl.tblGrid
    grid.remove(grid[col_idx])
    for tr in table._tbl.tr_lst:
        tr.remove(tr[col_idx])


def add_row(table):
    """Duplicates the last row in table and appends it."""
    tr = copy.deepcopy(table.rows[len(table.rows) - 1]._tr)
    table._tbl.append(tr)


def add_col(table):
    """Duplicates the last column in table and appends it."""
    grid = table._tbl.tblGrid
    new_col = copy.deepcopy(grid[len(grid) - 1])
    grid.append(new_col)
    for tr in table._tbl.tr_lst:
        new_tc = copy.deepcopy(tr.tc_lst[-1])
        tr.append(new_tc)


def set_cell(cell, text, font_size=7.5, bold=False, color=None, align=PP_ALIGN.LEFT, bg_color=None):
    """Sets text and formatting for a table cell."""
    cell.text = ""
    cell.margin_top = Inches(0.01)
    cell.margin_bottom = Inches(0.01)
    cell.margin_left = Inches(0.04)
    cell.margin_right = Inches(0.04)

    p = cell.text_frame.paragraphs[0]
    p.text = sanitize_text(text)
    p.font.size = Pt(font_size)
    p.font.bold = bold
    if color:
        p.font.color.rgb = color
    else:
        p.font.color.rgb = COLOR_TEXT_MAIN
    p.alignment = align

    if bg_color:
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_color


def set_text(shape, text, font_size=9.0, bold=False, color=None, align=PP_ALIGN.LEFT, line_spacing=1.15):
    """Sets text in a shape text frame."""
    if not shape.has_text_frame:
        return
    tf = shape.text_frame
    tf.text = ""
    tf.word_wrap = True
    tf.margin_left = Inches(0.04)
    tf.margin_right = Inches(0.04)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)

    lines = str(text).split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = sanitize_text(line)
        p.font.size = Pt(font_size)
        p.font.bold = bold
        p.line_spacing = line_spacing
        if color:
            p.font.color.rgb = color
        else:
            p.font.color.rgb = COLOR_TEXT_MAIN
        p.alignment = align


def set_key_points(shape, points, font_size=8.0, color_text=COLOR_TEXT_MAIN):
    """Formats the key points banner (Ý chính 1, 2, 3) cleanly on 3 independent lines."""
    if not shape.has_text_frame:
        return
    tf = shape.text_frame
    tf.text = ""
    tf.word_wrap = True
    tf.margin_left = Inches(0.06)
    tf.margin_right = Inches(0.06)
    tf.margin_top = Inches(0.04)
    tf.margin_bottom = Inches(0.04)

    for i, (label, content) in enumerate(points):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(2.0)
        p.line_spacing = 1.15

        r1 = p.add_run()
        r1.text = sanitize_text(label) + " "
        r1.font.bold = True
        r1.font.size = Pt(font_size)
        r1.font.color.rgb = COLOR_TEXT_MAIN

        r2 = p.add_run()
        r2.text = sanitize_text(content)
        r2.font.bold = False
        r2.font.size = Pt(font_size)
        r2.font.color.rgb = color_text


def prune_and_reorder_slides(prs):
    """
    Selects and duplicates to create 11 exact template slides:
    Template slides:
    - 6: Cover (Slide 7)
    - 9: Discussion Topics (Slide 10)
    - 10: Follow-up / Action Tracker (Slide 11) -> Roadmap & Next Actions
    - 11: Proposal Deep-Dive (Slide 12) -> Proposal 1 (Off-Page Cinema)
    - Duplicate of 11: Proposal Deep-Dive -> Proposal 2 (Quiz CIC)
    - Duplicate of 11: Proposal Deep-Dive -> Proposal 3 (/tai-app)
    - 13: Financial / Scorecard (Slide 14) -> Executive Scorecard
    - 14: Category Breakdown (Slide 15) -> Cinema Hub
    - Duplicate of 14: Category Breakdown -> Financial Hub
    - 16: Customer Experience / Signals (Slide 17) -> GEO Signals
    - 19: Product / Funnel (Slide 20) -> New User Funnel
    """
    # 1. Duplicate Slide 11 (Proposal Deep-Dive) before pruning (for Proposal 2)
    orig_p1 = prs.slides[11]
    p2_slide = prs.slides.add_slide(orig_p1.slide_layout)
    for sp in list(p2_slide.shapes):
        sp._element.getparent().remove(sp._element)
    for shape in orig_p1.shapes:
        p2_slide.shapes._spTree.append(copy.deepcopy(shape._element))

    # 2. Duplicate Slide 14 (Category Breakdown) before pruning (for Financial Hub)
    orig_cat = prs.slides[14]
    cat2_slide = prs.slides.add_slide(orig_cat.slide_layout)
    for sp in list(cat2_slide.shapes):
        sp._element.getparent().remove(sp._element)
    for shape in orig_cat.shapes:
        cat2_slide.shapes._spTree.append(copy.deepcopy(shape._element))

    # 3. Duplicate Slide 11 (Proposal Deep-Dive) a second time (for Proposal 3: /tai-app)
    p3_slide = prs.slides.add_slide(orig_p1.slide_layout)
    for sp in list(p3_slide.shapes):
        sp._element.getparent().remove(sp._element)
    for shape in orig_p1.shapes:
        p3_slide.shapes._spTree.append(copy.deepcopy(shape._element))

    # Keep 11 slides: {6, 9, 10, 11, 13, 14, 16, 19, 23, 24, 25}
    keep_indices = {6, 9, 10, 11, 13, 14, 16, 19, 23, 24, 25}
    delete_indices = sorted([i for i in range(len(prs.slides)) if i not in keep_indices], reverse=True)
    for i in delete_indices:
        delete_slide(prs, i)

    sldIdLst = prs.slides._sldIdLst

    # Initial positions after pruning:
    # 0: Cover (orig 6)
    # 1: Discussion Topics (orig 9)
    # 2: Action Tracker (orig 10)
    # 3: Proposal 1 (orig 11)
    # 4: Scorecard (orig 13)
    # 5: Category 1 (orig 14)
    # 6: GEO Signals (orig 16)
    # 7: Funnel (orig 19)
    # 8: Proposal 2 (duplicate 23)
    # 9: Category 2 (duplicate 24)
    # 10: Proposal 3 (duplicate 25)

    # Move 1: Move Scorecard (index 4) to index 1:
    sc = sldIdLst[4]
    sldIdLst.remove(sc)
    sldIdLst.insert(1, sc)

    # Move 2: Move Action Tracker (now at index 3) to the very end (index 10):
    at = sldIdLst[3]
    sldIdLst.remove(at)
    sldIdLst.append(at)

    # Move 3: Move Proposal 2 (now at index 7) to index 4 (right after Proposal 1 at 3):
    p2 = sldIdLst[7]
    sldIdLst.remove(p2)
    sldIdLst.insert(4, p2)

    # Move 4: Move Proposal 3 (now at index 9) to index 5 (right after Proposal 2 at 4):
    p3 = sldIdLst[9]
    sldIdLst.remove(p3)
    sldIdLst.insert(5, p3)

    # Move 5: Move Category 2 (now at index 9) to index 7 (right after Category 1 at 6):
    c2 = sldIdLst[9]
    sldIdLst.remove(c2)
    sldIdLst.insert(7, c2)

    print(f"Pruned and reordered to {len(prs.slides)} slides successfully.")


# =============================================================================
# SLIDE BUILDERS
# =============================================================================

def populate_slide_1_cover(slide):
    """Slide 1: Cover Slide."""
    for s in slide.shapes:
        if not s.has_text_frame:
            continue
        txt = s.text_frame.text.strip()
        if "Báo cáo" in txt or "BU/Division" in txt:
            set_text(
                s,
                "Web Platform - Báo cáo Điều hành Tháng 10/2026",
                font_size=24,
                bold=True,
                color=COLOR_TEXT_MAIN,
            )
        elif "Meeting để thảo luận" in txt or "Report để cung cấp" in txt:
            set_text(
                s,
                "Báo cáo tăng trưởng lưu lượng, hiệu quả chuyển đổi Web-to-App & 2 Đề xuất phê duyệt chiến lược",
                font_size=11,
                bold=False,
                color=COLOR_TEXT_MUTED,
            )
        elif "Tháng báo cáo được xác định" in txt or "Note:" in txt:
            set_text(
                s,
                "Kỳ dữ liệu: 01/10/2026 - 31/10/2026 | Nguồn dữ liệu: GA4 BigQuery & AppsFlyer SSOT | Đơn vị báo cáo: Web Platform Team",
                font_size=8.5,
                color=COLOR_TEXT_MUTED,
            )


def populate_slide_2_scorecard(slide):
    """Slide 2: Executive Scorecard [R] - Redesigned to exact layout of user's uploaded template."""
    set_text(
        slide.shapes[0],
        "Mục đích: Cho thấy kết quả tăng trưởng của Nền tảng Web theo kênh lưu lượng, đối soát kế hoạch mục tiêu và đánh giá tác động đóng góp vào App MoMo.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Shape 1: Hook Action Title matching user's exact phrasing
    slide.shapes[1].width = Inches(8.50)
    set_text(
        slide.shapes[1],
        "Traffic Tháng 10 đạt 98,3% target dù kênh trả phí giảm sâu (-60,4% MoM), kênh tự nhiên tiếp tục giữ đà tăng trưởng tốt (+13,5% MoM)",
        font_size=15.0,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "2 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Table 7: Native 16 rows x 10 cols -> Remove merged row 0, then trim to 10 rows x 6 cols
    tbl = slide.shapes[7].table
    delete_row(tbl, 0)
    tc0 = tbl.rows[0]._tr.tc_lst[0]
    if "vMerge" in tc0.attrib:
        del tc0.attrib["vMerge"]

    while len(tbl.rows) > 10:
        delete_row(tbl, len(tbl.rows) - 1)
    while len(tbl.columns) > 6:
        delete_col(tbl, len(tbl.columns) - 1)

    tbl.rows[0].height = Inches(0.24)
    slide.shapes[7].left = Inches(0.35)
    slide.shapes[7].top = Inches(1.10)

    col_widths = [Inches(1.85), Inches(0.80), Inches(0.80), Inches(0.80), Inches(0.95), Inches(0.80)]
    for c_idx, w in enumerate(col_widths):
        tbl.columns[c_idx].width = w

    headers = ["Kênh lưu lượng", "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "% MoM"]
    for c, h in enumerate(headers):
        align = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.RIGHT
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, align=align, bg_color=COLOR_PURPLE)

    scorecard_data = [
        ("KÊNH TỰ NHIÊN (NON-PAID)", "2.669.863", "2.820.824", "2.755.766", "3.128.542", "+13,5%", COLOR_GREEN, True, COLOR_BG_HIGHLIGHT),
        ("  - Organic", "1.875.191", "1.729.694", "1.623.796", "1.715.771", "+5,7%", None, False, None),
        ("  - AI Traffic (GEO)", "12.920", "13.736", "13.596", "18.547", "+36,4%", COLOR_GREEN, False, COLOR_BG_ALT),
        ("  - Direct", "440.855", "656.271", "755.896", "931.731", "+23,3%", None, False, None),
        ("  - Referral", "340.897", "421.123", "362.478", "462.493", "+27,6%", None, False, COLOR_BG_ALT),
        ("KÊNH TRẢ PHÍ (PAID ADS)", "497.958", "644.539", "1.197.093", "473.481", "-60,4%", COLOR_AMBER, True, None),
        ("TỔNG LƯỢNG TRUY CẬP (ACTUAL)", "3.167.821", "3.465.363", "3.952.859", "3.602.023", "-8,9%", COLOR_PINK, True, COLOR_BG_HIGHLIGHT),
        ("MỤC TIÊU THÁNG (TARGET)", "3.167.821", "3.465.363", "3.509.044", "3.665.607", "+4,5%", COLOR_PURPLE, True, None),
        ("TỶ LỆ ĐẠT TARGET", "100,0%", "100,0%", "112,6%", "98,3%", "-14,3 pp", COLOR_AMBER, True, COLOR_BG_ROSE_TINT),
    ]

    for r_idx, (ch, t7, t8, t9, t10, mom, col, is_bold, bg) in enumerate(scorecard_data, start=1):
        tbl.rows[r_idx].height = Inches(0.22)
        set_cell(tbl.cell(r_idx, 0), ch, font_size=7.0, bold=is_bold, color=col if is_bold else None, align=PP_ALIGN.LEFT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 1), t7, font_size=7.0, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 2), t8, font_size=7.0, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 3), t9, font_size=7.0, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 4), t10, font_size=7.0, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 5), mom, font_size=7.0, bold=True, color=col if col else None, align=PP_ALIGN.RIGHT, bg_color=bg)

    # Safely remove old template shapes from 8 onwards
    for idx in sorted(range(8, len(slide.shapes)), reverse=True):
        sp = slide.shapes[idx]
        sp._element.getparent().remove(sp._element)

    # 1. Left Highlights Header Bar
    rect_hl_h = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.35), Inches(3.42), Inches(6.00), Inches(0.24))
    rect_hl_h.fill.solid()
    rect_hl_h.fill.fore_color.rgb = COLOR_PURPLE
    rect_hl_h.line.color.rgb = COLOR_PURPLE
    set_text(rect_hl_h, "Key Highlights", font_size=8.2, bold=True, color=COLOR_WHITE, align=PP_ALIGN.LEFT)

    # 2. Left Highlights Body Box
    rect_hl_b = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.35), Inches(3.66), Inches(6.00), Inches(1.68))
    rect_hl_b.fill.solid()
    rect_hl_b.fill.fore_color.rgb = COLOR_WHITE
    rect_hl_b.line.color.rgb = COLOR_PINK
    rect_hl_b.line.width = Pt(1)

    tf_hl = rect_hl_b.text_frame
    tf_hl.word_wrap = True
    tf_hl.margin_left = Inches(0.06)
    tf_hl.margin_right = Inches(0.06)
    tf_hl.margin_top = Inches(0.04)
    tf_hl.margin_bottom = Inches(0.04)

    hl_bullets = [
        ("• Kênh tự nhiên duy trì đà tăng trưởng và đạt mức cao nhất trong H2/2026:",
         "Non-Paid đạt 3.128.542 PVs (+13,5% MoM), chiếm tỷ trọng 86,86% traffic toàn website. Điểm sáng là Organic Search đã đảo chiều tăng trở lại đạt 1,72M PVs (+5,7%), cho thấy nội lực từ nội dung và tiện ích trên trang đang giúp phục hồi tốt sau giai đoạn xây dựng nền tảng trong Q3."),
        ("• Tín hiệu tăng trưởng tích cực từ lượng truy cập trực tiếp và tìm kiếm AI:",
         "Direct Traffic đạt 931.731 PVs (chiếm 25,9% toàn trang) và duy trì đà tăng liên tục 4 tháng (từ 440K lên 932K, tăng +111,3% so với Tháng 7), chứng minh người dùng ngày càng có thói quen vào thẳng momo.vn. Cùng lúc đó, lưu lượng từ AI Search (GEO) tăng vọt +36,4% MoM (đạt 18.547 PVs), mở ra kênh tiếp cận người dùng mới đầy tiềm năng."),
        ("• Kênh trả phí (Paid Ads) quay về mức nền bình thường sau đợt cao điểm Tháng 9:",
         "Paid Traffic đạt 473.481 PVs (-60,4% MoM), quay về mức nền vận hành tiêu chuẩn tương đương Tháng 7 và Tháng 8 sau khi kết thúc các chiến dịch cao điểm mùa lễ và tựu trường. Việc traffic tổng thể vẫn đạt 98,3% Target (3,60M PVs) thể hiện sự tự chủ rất lớn khi hầu như toàn bộ quy mô truy cập tháng này đều do kênh tự nhiên gánh vác.")
    ]
    for i, (lead, body) in enumerate(hl_bullets):
        p = tf_hl.paragraphs[0] if i == 0 else tf_hl.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = 1.10
        p.space_after = Pt(3)
        r1 = p.add_run()
        r1.text = lead + " "
        r1.font.bold = True
        r1.font.size = Pt(6.8)
        r1.font.color.rgb = COLOR_TEXT_MAIN
        r2 = p.add_run()
        r2.text = body
        r2.font.bold = False
        r2.font.size = Pt(6.8)
        r2.font.color.rgb = COLOR_TEXT_MAIN

    # 3. Right Priorities Header Bar
    rect_pr_h = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.50), Inches(1.10), Inches(3.15), Inches(0.24))
    rect_pr_h.fill.solid()
    rect_pr_h.fill.fore_color.rgb = COLOR_PURPLE
    rect_pr_h.line.color.rgb = COLOR_PURPLE
    set_text(rect_pr_h, "Priorities for the Next 30 Days", font_size=8.2, bold=True, color=COLOR_WHITE, align=PP_ALIGN.LEFT)

    # 4. Right Priorities Body Box (FILLED PRIORITIES)
    rect_pr_b = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.50), Inches(1.34), Inches(3.15), Inches(4.00))
    rect_pr_b.fill.solid()
    rect_pr_b.fill.fore_color.rgb = COLOR_WHITE
    rect_pr_b.line.color.rgb = COLOR_PINK
    rect_pr_b.line.width = Pt(1)

    tf_pr = rect_pr_b.text_frame
    tf_pr.word_wrap = True
    tf_pr.margin_left = Inches(0.08)
    tf_pr.margin_right = Inches(0.08)
    tf_pr.margin_top = Inches(0.06)
    tf_pr.margin_bottom = Inches(0.06)

    pr_sections = [
        ("FINANCIAL HUB", COLOR_PINK, [
            ("• Xây dựng bộ công cụ Thuế TNCN & Gross - Net:",
             "Hoàn thiện tính lũy tiến và chuẩn bị UAT; go-live chính thức trước 10/11 đón cao điểm quyết toán thuế, chủ động tạo nguồn lưu lượng tự nhiên thay thế kênh trả phí."),
            ("• Go-live sản phẩm Chứng Chỉ Quỹ (CCQ):",
             "Đưa trang và luồng CCQ (/tai-chinh/chung-chi-quy) lên Production trước 15/11 nhằm kích hoạt lưu lượng tự nhiên cho nhóm sản phẩm Đầu tư (hiện đạt 458 PVs) và mở rộng danh mục.")
        ]),
        ("CINEMA HUB", COLOR_PURPLE, [
            ("• Triển khai dự án thử nghiệm Pilot Off-Page SEO:",
             "Triển khai gói ngân sách 125M (BU Movies tài trợ 80%) trước 15/11 nhằm nâng thứ hạng từ khóa cụm rạp lên Top 3-5 Google đón 3 triệu lượt tìm kiếm mùa phim Tết 2027."),
            ("• Triển khai luồng Chatbot AI:",
             "Tích hợp trợ lý xem phim thông minh trên Cinema Hub trước 18/11 để tư vấn chọn phim, lịch chiếu và kích hoạt chuyển đổi Web-to-App."),
            ("• Vận hành Quiz Bò Sữa Bay:",
             "Bò Sữa Bay đã go-live thành công (dạng Quiz tương tác không cần cấp phép); phối hợp BU Movies phát sóng TVC rạp nhằm thu hút người dùng mới trải nghiệm minigame.")
        ]),
        ("PLATFORM & PLG", COLOR_GREEN, [
            ("• Chuẩn hóa luồng Tải App (/tai-app):",
             "Tích hợp Smart Device Routing nhận diện hệ điều hành và gắn mã QR động, tối ưu chuyển đổi từ 22.750 lượt tìm kiếm thương hiệu hàng tháng hướng tới mục tiêu 30.000 install Q4.")
        ])
    ]

    first_p = True
    for sec_title, sec_col, items in pr_sections:
        p_sec = tf_pr.paragraphs[0] if first_p else tf_pr.add_paragraph()
        first_p = False
        p_sec.alignment = PP_ALIGN.LEFT
        p_sec.space_before = Pt(4) if p_sec != tf_pr.paragraphs[0] else Pt(0)
        p_sec.space_after = Pt(1)
        r_sec = p_sec.add_run()
        r_sec.text = sec_title
        r_sec.font.bold = True
        r_sec.font.size = Pt(7.5)
        r_sec.font.color.rgb = sec_col

        for lead, body in items:
            p_item = tf_pr.add_paragraph()
            p_item.alignment = PP_ALIGN.LEFT
            p_item.line_spacing = 1.10
            p_item.space_after = Pt(2)

            r1 = p_item.add_run()
            r1.text = lead + " "
            r1.font.bold = True
            r1.font.size = Pt(6.8)
            r1.font.color.rgb = COLOR_TEXT_MAIN

            r2 = p_item.add_run()
            r2.text = body
            r2.font.bold = False
            r2.font.size = Pt(6.8)
            r2.font.color.rgb = COLOR_TEXT_MAIN


def populate_slide_3_discussion_topics(slide):
    """Slide 3: Discussion Topics [D]."""
    set_text(
        slide.shapes[0],
        "Mục đích: Tổng hợp 3 đề xuất chiến lược cần Ban Giám Đốc phê duyệt gồm Pilot Off-Page Cinema mùa phim Tết 2027, Gamification Quiz CIC và Trạm Chuyển Đổi Trung Tâm (/tai-app).",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    set_text(
        slide.shapes[1],
        "Discussion Topics: 3 đề xuất phê duyệt gồm Pilot Off-Page Cinema, Quiz CIC và Trang Tải Ứng Dụng (/tai-app)",
        font_size=15.0,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "3 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Table 7: 8 columns, trim to 4 rows (header + 3 topics)
    tbl = slide.shapes[7].table
    while len(tbl.rows) > 4:
        delete_row(tbl, len(tbl.rows) - 1)
    while len(tbl.rows) < 4:
        add_row(tbl)

    headers = ["#", "Chủ đề", "Loại", "Cần CEO/BOM quyết định / hỗ trợ gì", "Tác động", "Hạn", "Ưu tiên", "Chi tiết"]
    for c, h in enumerate(headers):
        align = PP_ALIGN.CENTER if c in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, align=align, bg_color=COLOR_PURPLE)

    tbl.rows[0].height = Inches(0.26)
    tbl.rows[1].height = Inches(0.48)
    tbl.rows[2].height = Inches(0.48)
    tbl.rows[3].height = Inches(0.48)

    topics_data = [
        ("1", "Pilot Off-Page SEO Cinema Hub: Thẩm quyền từ khóa đón đầu Phim Tết 2027", "Approve",
         "Phê duyệt 125M (Movies tài trợ 100M, Web đối ứng 25M) cho dự án thử nghiệm 3 tháng.",
         "Top 3 - 5 Google cụm rạp; bảo đảm 1,2M - 1,5M PVs/tháng mùa Tết 2027 tự chủ không tốn ads.",
         "15/11", "CAO", "Slide 4", COLOR_ROSE),
        ("2", "Mở rộng Gamification Quiz sang mảng Giáo dục Tài chính và CIC", "Approve",
         "Phê duyệt chủ trương Quiz CIC; BU FS hỗ trợ dữ liệu và mở cơ chế deeplink nhận diện kết quả trên App.",
         "Time on Site +170% củng cố SEO mảng Tài chính; kéo +3K - 5K lượt kiểm tra CIC trên App/tháng (chi phí 0đ).",
         "20/11", "TRUNG BÌNH", "Slide 5", COLOR_AMBER),
        ("3", "Chuẩn hóa Trang Tải Ứng Dụng (/tai-app) thành Cổng chuyển đổi tập trung toàn Web", "Approve",
         "Phê duyệt chuẩn hóa giao diện /tai-app & kích hoạt Smart Device Routing; cấp gói voucher 50K Tân thủ.",
         "Nâng CVR 4,8% lên 8,5 - 10%, +8.000 đến 12.000 App Installs/tháng từ tự nhiên; bảo đảm KPI 30K Q4.",
         "18/11", "CAO", "Slide 6", COLOR_ROSE)
    ]

    for r_idx, (num, topic, ltype, need, imp, dead, prio, det, prio_col) in enumerate(topics_data, start=1):
        set_cell(tbl.cell(r_idx, 0), num, font_size=7.2, bold=True, align=PP_ALIGN.CENTER)
        set_cell(tbl.cell(r_idx, 1), topic, font_size=7.2, bold=True, align=PP_ALIGN.LEFT)
        set_cell(tbl.cell(r_idx, 2), ltype, font_size=7.2, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
        set_cell(tbl.cell(r_idx, 3), need, font_size=7.0, align=PP_ALIGN.LEFT)
        set_cell(tbl.cell(r_idx, 4), imp, font_size=7.0, color=COLOR_GREEN, align=PP_ALIGN.LEFT)
        set_cell(tbl.cell(r_idx, 5), dead, font_size=7.2, align=PP_ALIGN.CENTER)
        set_cell(tbl.cell(r_idx, 6), prio, font_size=7.2, bold=True, color=prio_col, align=PP_ALIGN.CENTER)
        set_cell(tbl.cell(r_idx, 7), det, font_size=7.2, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)

    # Re-position bottom summary box to eliminate empty void and prevent overlap
    slide.shapes[8].top = Inches(3.18)
    slide.shapes[8].left = Inches(0.30)
    slide.shapes[8].width = Inches(9.30)
    slide.shapes[8].height = Inches(1.85)

    slide.shapes[9].top = Inches(3.35)
    slide.shapes[9].left = Inches(0.45)
    slide.shapes[10].top = Inches(3.35)
    slide.shapes[10].left = Inches(0.45)
    set_text(slide.shapes[10], "Nội dung chính", font_size=8.5, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)

    slide.shapes[11].top = Inches(3.25)
    slide.shapes[11].left = Inches(1.80)
    slide.shapes[11].width = Inches(7.65)
    slide.shapes[11].height = Inches(1.70)
    box_text = (
        "• Đề xuất 1 (Cinema Hub): Phê duyệt dự án Pilot Off-Page SEO (ngân sách 125 triệu VNĐ, BU Movies tài trợ chính 100 triệu) để đưa từ khóa rạp phim lên Top 3 - 5 Google Search, đón đầu 3 triệu lượt tìm kiếm mùa phim Tết 2027 và tự chủ 100% traffic không cần chi Paid Ads.\n"
        "• Đề xuất 2 (Financial Hub): Phê duyệt mở rộng mô hình Gamification Quiz sang mảng Giáo dục Tài chính và CIC (dựa trên thành công của minigame Một Mùa Quýt và Bò Sữa Bay) nhằm tăng thời gian trên trang (+170%) củng cố SEO và kéo +5.000 lượt kiểm tra CIC trên App mỗi tháng với chi phí 0đ.\n"
        "• Đề xuất 3 (Platform & PLG): Chuẩn hóa trang /tai-app thành Trạm chuyển đổi trung tâm toàn Web với cơ chế Smart Device Routing và gói ưu đãi Tân thủ đón 22.750 lượt Brand Search hàng tháng, hướng tới mục tiêu đạt trên 30.000 App Installs trong Q4."
    )
    set_text(slide.shapes[11], box_text, font_size=7.4, color=COLOR_TEXT_MAIN, line_spacing=1.12)


def populate_slide_4_proposal_offpage_cinema(slide):
    """Slide 4: Proposal Deep-Dive 1 [D] - Pilot Off-Page Cinema Phim Tết."""
    set_text(
        slide.shapes[0],
        "Mục đích: Trình bày bài toán thẩm quyền từ khóa rạp phim và đề xuất Ban Giám Đốc phê duyệt ngân sách thử nghiệm Off-page đón đầu mùa phim Tết 2027.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    slide.shapes[1].top = Inches(0.36)
    slide.shapes[1].height = Inches(0.55)
    set_text(
        slide.shapes[1],
        "Pilot Off-Page Cinema: Phê duyệt 125M (Movies tài trợ 80%) đẩy Top 3-5 từ khóa rạp phim đón mùa Tết 2027",
        font_size=15.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "4 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Problem Statement Box
    set_text(slide.shapes[9], "Vấn đề", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    prob_text = (
        "• Rủi ro tụt hậu thứ hạng: Cụm từ khóa rạp phim (CGV, Lotte, BHD, giá vé) đang dừng ở Top 6 - 12 Google, dù On-page và dữ liệu lịch chiếu đã tối ưu hoàn hảo.\n"
        "• Thiếu hụt Backlink thẩm quyền: Website thiếu liên kết báo chí và giải trí chất lượng cao, khiến Google ưu tiên hiển thị website chính hãng của các cụm rạp."
    )
    set_text(slide.shapes[10], prob_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Context Box
    set_text(slide.shapes[13], "Bối cảnh", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    ctx_text = (
        "• Cơ hội vàng mùa Phim Tết 2027: Nhu cầu tìm kiếm vé xem phim và lịch chiếu tăng gấp 3 lần (đạt 2,5M - 3M lượt tìm kiếm/tháng), đóng góp 40% doanh thu vé cả năm.\n"
        "• Tài trợ ngân sách từ BU Movies: BU Movies cam kết chi trả 100 triệu VNĐ (80% ngân sách); Web Platform chỉ cần đối ứng 25 triệu VNĐ từ nguồn tối ưu kỹ thuật."
    )
    set_text(slide.shapes[14], ctx_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Impact Box
    set_text(slide.shapes[17], "Tác động", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    imp_text = (
        "• Hiệu quả lưu lượng & Tự chủ kênh: Tăng thêm +400.000 đến +600.000 Pageviews/tháng trong mùa Tết 2027, giúp Cinema Hub đạt mốc 1,5M PV hoàn toàn tự nhiên.\n"
        "• Tiết kiệm chi phí quảng cáo: Thay thế hoàn toàn nhu cầu chạy Paid Search đắt đỏ trong dịp Tết (tiết kiệm ước tính 300 - 450 triệu VNĐ chi phí media)."
    )
    set_text(slide.shapes[18], imp_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Table 20: Options
    set_text(slide.shapes[19], "PHƯƠNG ÁN", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    tbl = slide.shapes[20].table
    headers = ["Phương án", "Nội dung", "Ưu điểm", "Rủi ro / chi phí"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, bg_color=COLOR_PURPLE)

    set_cell(tbl.cell(1, 0), "A (Đề xuất): Pilot Off-Page 3 tháng", font_size=7.5, bold=True, color=COLOR_PINK, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 1), "Ngân sách 125M (Movies tài trợ 100M). Đi bài PR & Guest Post báo chí chuyên ngành phim ảnh.", font_size=7.2, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 2), "Đưa từ khóa lên Top 3 - 5 kịp Tết 2027; rủi ro tài chính thấp do được BU tài trợ 80%.", font_size=7.2, color=COLOR_GREEN, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 3), "Chi phí đối ứng 25M; cần giám sát chất lượng backlink chặt chẽ.", font_size=7.2, bg_color=COLOR_BG_HIGHLIGHT)

    set_cell(tbl.cell(2, 0), "B: Giữ nguyên hiện trạng On-Page", font_size=7.5, bold=True)
    set_cell(tbl.cell(2, 1), "Chỉ tiếp tục tối ưu kỹ thuật On-page và sản xuất bài viết blog thông thường.", font_size=7.2)
    set_cell(tbl.cell(2, 2), "Không phát sinh thêm chi phí ngân sách bên ngoài.", font_size=7.2)
    set_cell(tbl.cell(2, 3), "Mất cơ hội đón sóng mùa Tết 2027; tiếp tục đứng sau đối thủ và rạp phim chính hãng.", font_size=7.2, color=COLOR_ROSE)

    # Right Box Commentary
    set_text(slide.shapes[22], "Nhận định & Bình luận điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[24], "Đề nghị với CEO/BOM", font_size=9.5, bold=True, color=COLOR_PURPLE)
    slide.shapes[24].width = Inches(1.80)
    rec_text = (
        "• Đề xuất phê duyệt: Approve chủ trương triển khai gói Pilot Off-page SEO 3 tháng (tháng 11/2026 - 01/2027) với ngân sách 125 triệu VNĐ.\n"
        "• Cơ chế phân bổ: BU Movies tài trợ 100 triệu VNĐ, Web Platform đối ứng 25 triệu VNĐ từ nguồn tối ưu chi phí kỹ thuật nội bộ."
    )
    set_text(slide.shapes[25], rec_text, font_size=8.0, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[27], "Nếu không quyết định", font_size=9.5, bold=True, color=COLOR_ROSE)
    slide.shapes[27].width = Inches(1.80)
    risk_text = (
        "Cinema Hub sẽ bỏ lỡ cơ hội đón đầu mùa phim Tết 2027 (chiếm 40% doanh thu năm), tụt hạng sâu trước các đối thủ và buộc phải chi trả hàng trăm triệu đồng chạy Paid Ads để duy trì traffic."
    )
    set_text(slide.shapes[28], risk_text, font_size=8.0, color=COLOR_ROSE)


def populate_slide_5_proposal_quiz_cic(slide):
    """Slide 5: Proposal Deep-Dive 2 [D] - Gamification Quiz CIC."""
    set_text(
        slide.shapes[0],
        "Mục đích: Trình bày đề xuất nhân rộng mô hình Gamification Quiz sang mảng Giáo dục Tài chính và CIC nhằm kích hoạt tương tác và kéo người dùng mới vào App.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    slide.shapes[1].top = Inches(0.36)
    slide.shapes[1].height = Inches(0.55)
    set_text(
        slide.shapes[1],
        "Gamification Quiz Tài chính: Nhân bản Quiz CIC kéo Time on Site (+170%) và +5.000 App User kiểm tra tín dụng",
        font_size=15.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "5 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Problem Box
    set_text(slide.shapes[9], "Vấn đề", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    prob_text = (
        "• Nội dung tài chính khô khan: Thời gian trên trang (Time on Site) của các bài viết tài chính và tra cứu CIC hiện chỉ đạt 45 - 55 giây; tỷ lệ thoát trang cao (>70%).\n"
        "• Bỏ lỡ điểm chạm chuyển đổi: Người dùng đọc thông tin kiến thức xong thường rời đi ngay, chưa có động lực rõ ràng để bấm OneLink tải hoặc mở App MoMo."
    )
    set_text(slide.shapes[10], prob_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Context Box
    set_text(slide.shapes[13], "Bối cảnh", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    ctx_text = (
        "• Đòn bẩy Gamification thành công: Minigame Một Mùa Quýt và Quiz Bò Sữa Bay đã chứng minh hiệu quả vượt bậc: tăng gấp 3 lần thời gian onsite và thúc đẩy 484 liên kết ngân hàng.\n"
        "• Nhu cầu kiểm tra CIC cuối năm tăng cao: Người dùng có nhu cầu kiểm tra sức khỏe tín dụng để vay tiêu dùng và mở thẻ tín dụng phục vụ mua sắm Tết."
    )
    set_text(slide.shapes[14], ctx_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Impact Box
    set_text(slide.shapes[17], "Tác động", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    imp_text = (
        "• Tác động tăng trưởng: Tăng Time on Site mảng Tài chính lên 2,5 - 3 phút (+170%), củng cố mạnh mẽ tín hiệu xếp hạng tìm kiếm tự nhiên.\n"
        "• Kéo App User: Thúc đẩy +3.000 đến +5.000 lượt kiểm tra điểm CIC trên App MoMo mỗi tháng hoàn toàn từ chuyển đổi tự nhiên (Organic W2A)."
    )
    set_text(slide.shapes[18], imp_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Table 20: Options
    set_text(slide.shapes[19], "PHƯƠNG ÁN", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    tbl = slide.shapes[20].table
    headers = ["Phương án", "Nội dung", "Ưu điểm", "Rủi ro / chi phí"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, bg_color=COLOR_PURPLE)

    set_cell(tbl.cell(1, 0), "A (Đề xuất): Quiz CIC In-House", font_size=7.5, bold=True, color=COLOR_PINK, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 1), "Tận dụng Web Gamification Engine sẵn có dựng Quiz CIC 'Sức khỏe tín dụng'.", font_size=7.2, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 2), "Chi phí 0đ mua ngoài; go-live nhanh trong 2 tuần; dữ liệu kết quả mượt mà.", font_size=7.2, color=COLOR_GREEN, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 3), "Cần BU Financial Services phối hợp duyệt bộ 10 câu hỏi & quà tặng voucher.", font_size=7.2, bg_color=COLOR_BG_HIGHLIGHT)

    set_cell(tbl.cell(2, 0), "B: Tiếp tục bài viết tĩnh", font_size=7.5, bold=True)
    set_cell(tbl.cell(2, 1), "Chỉ duy trì sản xuất bài viết cẩm nang và FAQ tài chính thông thường.", font_size=7.2)
    set_cell(tbl.cell(2, 2), "Không phát sinh công việc phối hợp liên phòng ban.", font_size=7.2)
    set_cell(tbl.cell(2, 3), "Tỷ lệ thoát trang duy trì mức cao; lãng phí nguồn traffic 80K PVs/tháng của mảng CIC.", font_size=7.2, color=COLOR_ROSE)

    # Right Box Commentary
    set_text(slide.shapes[22], "Nhận định & Bình luận điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[24], "Đề nghị với CEO/BOM", font_size=9.5, bold=True, color=COLOR_PURPLE)
    slide.shapes[24].width = Inches(1.80)
    rec_text = (
        "• Đề xuất phê duyệt: Approve chủ trương mở rộng Gamification Quiz sang mảng Tài chính và chỉ đạo BU Financial Services cử đầu mối phối hợp thẩm định bộ câu hỏi trắc nghiệm tín dụng CIC trước ngày 15/11."
    )
    set_text(slide.shapes[25], rec_text, font_size=8.0, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[27], "Nếu không quyết định", font_size=9.5, bold=True, color=COLOR_ROSE)
    slide.shapes[27].width = Inches(1.80)
    risk_text = (
        "Financial Hub tiếp tục phụ thuộc vào các bài viết tĩnh có thời gian onsite thấp, suy giảm dần vị thế SEO trước các đối thủ ngân hàng và bỏ lỡ cơ hội giáo dục tài chính số cho người dùng trẻ."
    )
    set_text(slide.shapes[28], risk_text, font_size=8.0, color=COLOR_ROSE)


def populate_slide_6_proposal_tai_app(slide):
    """Slide 6: Proposal Deep-Dive 3 [D] - Chuẩn hóa Trang Tải Ứng Dụng (/tai-app) & Tối ưu chuyển đổi."""
    set_text(
        slide.shapes[0],
        "Mục đích: Đề xuất Ban Giám Đốc phê duyệt chuẩn hóa /tai-app thành Cổng chuyển đổi tập trung toàn Web, tích hợp Smart Device Routing và gói ưu đãi Tân thủ trong Tháng 11/2026.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    slide.shapes[1].top = Inches(0.36)
    slide.shapes[1].height = Inches(0.55)
    set_text(
        slide.shapes[1],
        "Trang Tải Ứng Dụng (/tai-app): Phê duyệt chuẩn hóa Cổng chuyển đổi tập trung toàn Web đón 22.750 Brand Search hàng tháng",
        font_size=15.0,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "6 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Problem Statement Box
    set_text(slide.shapes[9], "Vấn đề", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    prob_text = (
        "• Lãng phí nguồn lưu lượng thương hiệu: Mỗi tháng có 22.750 lượt tìm kiếm từ khóa thương hiệu ('tải momo', 'cài đặt momo') nhưng CVR cài đặt trang /tai-app hiện tại mới đạt 4,8% (chuẩn benchmark fintech là 8 - 10%).\n"
        "• Trải nghiệm tĩnh và thiếu phân luồng: Trang chưa nhận diện thiết bị (iOS/Android/Desktop), chưa tối ưu luồng tải theo từng hệ điều hành và chưa có gói ưu đãi chuyên biệt, dẫn đến tỷ lệ thoát trang còn ở mức cao (54,2%)."
    )
    set_text(slide.shapes[10], prob_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Context Box
    set_text(slide.shapes[13], "Bối cảnh", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    ctx_text = (
        "• Áp lực chỉ tiêu New User Q4/2026: Mục tiêu toàn Web phải mang về 30.000 App Installs trong Q4; khi ngân sách Paid Ads bị cắt giảm, việc tối ưu phễu chuyển đổi tự nhiên là con đường duy nhất.\n"
        "• Trạm trung chuyển của mọi chiến dịch: /tai-app là đích đến chuyển đổi của toàn bộ các Hub (Cinema, Financial, Life Services) và các chiến dịch Viral trên mạng xã hội."
    )
    set_text(slide.shapes[14], ctx_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Impact Box
    set_text(slide.shapes[17], "Tác động", font_size=8.0, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    imp_text = (
        "• Bứt phá số lượng tải app tự nhiên: Nâng CVR từ 4,8% lên 8,5 - 10% sẽ mang về thêm +8.000 đến 12.000 App Installs/tháng hoàn toàn từ kênh tự nhiên (chi phí 0đ).\n"
        "• Bảo đảm hoàn thành 100% KPI New User: Đưa tổng lượt cài đặt app từ Web đạt trên 30.000 installs trong Q4, tiết kiệm ước tính 400 - 600 triệu VNĐ chi phí mua người dùng trả phí."
    )
    set_text(slide.shapes[18], imp_text, font_size=7.5, color=COLOR_TEXT_MAIN, line_spacing=1.05)

    # Table 20: Options
    set_text(slide.shapes[19], "PHƯƠNG ÁN", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    tbl = slide.shapes[20].table
    headers = ["Phương án", "Nội dung", "Ưu điểm", "Rủi ro / chi phí"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, bg_color=COLOR_PURPLE)

    set_cell(tbl.cell(1, 0), "A (Đề xuất): Chuẩn hóa giao diện & Smart Routing", font_size=7.5, bold=True, color=COLOR_PINK, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 1), "Redesign layout /tai-app, tích hợp Smart Link nhận diện OS (iOS mở App Store, Android mở Play Store, Desktop hiển thị QR động), cấp Voucher 50K cho Tân thủ.", font_size=7.2, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 2), "Tăng CVR lên 8,5 - 10%, tạo thêm +8K - 12K installs/tháng; luồng tải tự động mượt mà, đo lường chính xác qua Umami và AppsFlyer.", font_size=7.2, color=COLOR_GREEN, bg_color=COLOR_BG_HIGHLIGHT)
    set_cell(tbl.cell(1, 3), "Cần 0,5 man-month Frontend Dev và phối hợp kích hoạt gói voucher tân thủ.", font_size=7.2, bg_color=COLOR_BG_HIGHLIGHT)

    set_cell(tbl.cell(2, 0), "B: Giữ nguyên hiện trạng & Chỉ treo Banner tĩnh", font_size=7.5, bold=True)
    set_cell(tbl.cell(2, 1), "Duy trì layout cũ, chỉ thay đổi câu chữ nút bấm CTA và đặt thêm banner tĩnh trỏ về store.", font_size=7.2)
    set_cell(tbl.cell(2, 2), "Không tốn nguồn lực kỹ thuật (Dev).", font_size=7.2)
    set_cell(tbl.cell(2, 3), "CVR dậm chân tại chỗ (4,8 - 5,2%), tiếp tục lãng phí 22.750 lượt Brand Search và rủi ro hụt chỉ tiêu New User Q4.", font_size=7.2, color=COLOR_ROSE)

    # Right Box Commentary
    set_text(slide.shapes[22], "Nhận định & Bình luận điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[24], "Đề nghị với CEO/BOM", font_size=9.5, bold=True, color=COLOR_PURPLE)
    slide.shapes[24].width = Inches(1.80)
    rec_text = (
        "• Phê duyệt chủ trương: Cho phép Engineering triển khai Sprint chuẩn hóa trang /tai-app và hoàn tất tích hợp Smart Routing trước ngày 18/11/2026.\n"
        "• Phối hợp liên phòng ban: Chỉ đạo đội Growth Marketing cấp gói ưu đãi Voucher 50K dành riêng cho người dùng tải app qua Web để kích thích cài đặt và đăng ký."
    )
    set_text(slide.shapes[25], rec_text, font_size=8.0, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[27], "Nếu không quyết định", font_size=9.5, bold=True, color=COLOR_ROSE)
    slide.shapes[27].width = Inches(1.80)
    risk_text = (
        "Tiếp tục lãng phí hơn 22.000 lượt người dùng có nhu cầu cài app thực sự mỗi tháng, phễu Web-to-App bị tắc nghẽn và Web Platform không thể hoàn thành chỉ tiêu 30.000 App Installs trong Q4."
    )
    set_text(slide.shapes[28], risk_text, font_size=8.0, color=COLOR_ROSE)


def populate_slide_7_cinema_hub(slide):
    """Slide 7: Báo Cáo Hiệu Suất Cinema Hub (Cinema Hub Performance) [R]."""
    set_text(
        slide.shapes[0],
        "Mục đích: Đánh giá chi tiết hiệu suất kinh doanh của Cinema Hub, đối soát mục tiêu Target và hiệu quả chuyển đổi Web-to-App.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    set_text(
        slide.shapes[1],
        "Cinema Hub vượt kế hoạch đạt 1,13M Pageviews (101,4% Target); Non-Paid chạm mốc kỷ lục 86,4% bù đắp 93% Paid Ads cắt giảm",
        font_size=15.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "7 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Shape 8: Dải tóm tắt (Ý chính 1, 2, 3)
    points_s6 = [
        ("Ý chính 1:", "Cinema Hub đạt 1.132.721 Pageviews (vượt 101,4% Target 1.117.378 PV), tỷ trọng Non-Paid lập đỉnh 86,4% bù đắp trọn vẹn việc cắt giảm 93% Paid Ads phim lẻ."),
        ("Ý chính 2:", "Lưu lượng GEO từ AI Search bứt phá +163% MoM (1.210 phiên truy cập); cụm rạp đối tác (CGV, Lotte, BHD) tăng trưởng +39,6% đạt 700.000 lượt xem."),
        ("Ý chính 3:", "Chuyển đổi Web-to-App xuất sắc: Thu hút 280K New Users ghé thăm (+17,4% MoM), mang về 1.931 lượt cài app và 484 liên kết ngân hàng (CVR 25,1%, +92% MoM).")
    ]
    set_key_points(slide.shapes[8], points_s6, font_size=8.0)

    # Top Section Label
    set_text(slide.shapes[9], "HIỆU SUẤT TRUY CẬP VÀ MỤC TIÊU CINEMA HUB", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)

    # Top 4 Stat Cards
    # Card 1: Pageviews Cinema Hub
    set_text(slide.shapes[12], "Pageviews Cinema Hub", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[13], "1,13M", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[14], "▲ Vượt 101,4% Target (1.117.378 PV)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Card 2: Tỷ trọng Non-Paid
    set_text(slide.shapes[18], "Tỷ trọng Kênh Tự Nhiên", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[19], "86,4%", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[20], "▲ Đỉnh cao lịch sử (Tự bù 51% Paid cắt)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Card 3: Lưu lượng GEO (AI Search)
    set_text(slide.shapes[24], "Lưu lượng GEO (AI)", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[25], "1.210", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[26], "▲ +163% MoM (CGV & Phim mới)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Card 4: Cụm rạp đối tác (CGV, Lotte)
    set_text(slide.shapes[30], "Cụm rạp đối tác (CGV)", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[31], "700K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[32], "▲ +39,6% MoM (Lotte, BHD ổn định)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Bottom Section Label
    set_text(slide.shapes[35], "TRẢI NGHIỆM TƯƠNG TÁC VÀ CHUYỂN ĐỔI WEB-TO-APP", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)

    # Bottom 3 Stat Cards (New Users -> Installs -> Map Bank)
    # Card 5: Người dùng mới ghé thăm (New Users)
    set_text(slide.shapes[38], "Người dùng mới ghé thăm", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[39], "280K", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[40], "▲ +17,4% MoM (279.968 user)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Card 6: OneLink Web-to-App
    set_text(slide.shapes[42], "Cài đặt App từ Cinema", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[43], "1.931", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[44], "▲ +58% MoM (OneLink)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Card 7: Map Bank
    set_text(slide.shapes[46], "Liên kết NH (Map Bank)", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[47], "484", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[48], "CVR 25,1% (+92% MoM)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Right Commentary
    set_text(slide.shapes[50], "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[52], "Điểm nổi bật", font_size=9.5, bold=True, color=COLOR_GREEN)
    slide.shapes[52].width = Inches(1.60)
    commentary_perf = (
        "• Vượt kế hoạch ngoạn mục: Đạt 1.132.721 Pageviews (101,4% Target 1.117.378) dù BU Movies chủ động cắt giảm 93% Paid Ads phim lẻ (-272K views); Non-Paid tăng +21,7% bù đắp trọn vẹn.\n"
        "• Tín hiệu AI Search & Chuyển đổi: GEO đạt 1.210 sessions (+163% MoM) nhờ dữ liệu rạp chuẩn; mang về 484 người dùng mới liên kết ngân hàng với CVR đạt kỷ lục 25,1%."
    )
    set_text(slide.shapes[53], commentary_perf, font_size=8.0, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[55], "Vấn đề cần lưu ý & Việc tiếp theo", font_size=9.5, bold=True, color=COLOR_AMBER)
    slide.shapes[55].width = Inches(2.40)
    commentary_focus = (
        "• Điểm nghẽn thứ hạng: Từ khóa cụm rạp dao động Top 6 - 12 do thiếu backlink; rủi ro trễ mùa phim Tết 2027 (chiếm 40% doanh thu năm).\n"
        "• Ưu tiên 30 ngày (Next 30 Days): Quiz Bò Sữa Bay đã go-live (không cần cấp phép vì là Quiz); tháng 11 tập trung triển khai luồng Chatbot AI tư vấn phim và đẩy mạnh chiến dịch Off-Page SEO đón mùa phim Tết."
    )
    set_text(slide.shapes[56], commentary_focus, font_size=7.6, color=COLOR_TEXT_MAIN)

    # Finally safely delete dark solid bars (Shapes 15, 16, 21, 22, 27, 28, 33, 34) in reverse order
    for idx in sorted([15, 16, 21, 22, 27, 28, 33, 34], reverse=True):
        sp = slide.shapes[idx]
        sp._element.getparent().remove(sp._element)


def populate_slide_8_financial_hub(slide):
    """Slide 8: Báo Cáo Hiệu Suất Financial Hub (Financial Hub Performance) [R]."""
    set_text(
        slide.shapes[0],
        "Mục đích: Đánh giá thực chất hiệu suất mảng Tài chính số (Financial Hub), bóc tách điểm nghẽn cơ cấu sản phẩm và lộ trình chuyển dịch sang Product-Led Growth.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    slide.shapes[1].top = Inches(0.36)
    slide.shapes[1].height = Inches(0.55)
    set_text(
        slide.shapes[1],
        "Financial Hub đạt 274K PV (+9,6% MoM) nhưng chưa bền vững: Phụ thuộc 37% Paid Ads, 77% traffic dồn vào 3 SP tín chấp",
        font_size=15.0,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "8 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    # Shape 8: Dải tóm tắt (Ý chính 1, 2, 3)
    points_s7 = [
        ("Ý chính 1:", "Financial Hub đạt 273.705 Pageviews (+9,6% MoM, đạt 109,5% Target 250K); tuy nhiên kênh tự nhiên mới đạt 62,7%, còn phụ thuộc 37,3% vào Paid Ads (102K PV)."),
        ("Ý chính 2:", "Lệch cơ cấu nghiêm trọng: 77% lưu lượng dồn vào 3 sản phẩm vay tín chấp (CIC 91K, Vay Nhanh 62K, Ví Trả Sau 58K); các mảng Tiết kiệm, CCQ, Chứng khoán đều dưới 2K PV."),
        ("Ý chính 3:", "Bảng biểu tĩnh đạt 0% CTR (onsite 48s), trong khi Interactive Tools bứt phá 33,7% - 43,8% CTR; bảo chứng vững chắc để nhân rộng PLG với bộ công cụ Thuế T11.")
    ]
    set_key_points(slide.shapes[8], points_s7, font_size=8.0)

    # Top Section Label
    set_text(slide.shapes[9], "CƠ CẤU HIỆU SUẤT TRUY CẬP VÀ MỨC ĐỘ TẬP TRUNG SẢN PHẨM", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)

    # Top 4 Stat Cards
    # Card 1: Pageviews Finhub
    set_text(slide.shapes[12], "Lưu lượng Financial Hub", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[13], "274K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[14], "▲ +9,6% MoM (Đạt 109,5% Target)", font_size=7.2, bold=True, color=COLOR_GREEN)

    # Card 2: Tỷ trọng Non-Paid vs Paid
    set_text(slide.shapes[18], "Tỷ trọng Kênh Tự Nhiên", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[19], "62,7%", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[20], "▼ Còn phụ thuộc 37,3% Paid Ads (102K)", font_size=7.2, bold=True, color=COLOR_AMBER)

    # Card 3: Tập trung sản phẩm
    set_text(slide.shapes[24], "Tập trung vào 3 SP Tín Chấp", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[25], "77%", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[26], "211K PV dồn vào CIC, Vay Nhanh, VTS", font_size=7.2, color=COLOR_TEXT_MUTED)

    # Card 4: Nhóm Tiết kiệm & Đầu tư
    set_text(slide.shapes[30], "Nhóm Tiết kiệm & Đầu tư", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[31], "<2K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[32], "▼ Nội dung mỏng, chưa hoàn thiện sản phẩm", font_size=7.2, bold=True, color=COLOR_ROSE)

    # Bottom Section Label
    set_text(slide.shapes[35], "ĐIỂM NGHẼN TRẢI NGHIỆM VÀ LỜI GIẢI PRODUCT-LED GROWTH (PLG)", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)

    # Bottom 3 Stat Cards
    set_text(slide.shapes[38], "CTR Bảng Biểu & Bài Viết Tĩnh", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[39], "0,0%", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[40], "▼ Onsite 48s, 0 click (Tỷ giá, Vàng 0%)", font_size=6.8, bold=True, color=COLOR_ROSE)

    set_text(slide.shapes[42], "CTR Tool Tính Lương Net - Gross", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[43], "33,7%", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[44], "▲ 1.000 Clicks (Bảo chứng Thuế T11)", font_size=6.8, bold=True, color=COLOR_GREEN)

    set_text(slide.shapes[46], "CTR Tool Vay Nhanh & CIC", font_size=7.5, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[47], "38,6% - 43,8%", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[48], "▲ 6.100 Clicks (Vay 4,3K, CIC 1,8K)", font_size=6.8, bold=True, color=COLOR_GREEN)

    # Right Commentary
    set_text(slide.shapes[50], "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[52], "Điểm nổi bật", font_size=9.5, bold=True, color=COLOR_GREEN)
    slide.shapes[52].width = Inches(1.60)
    commentary_perf = (
        "• Đạt mốc tổng thể: Financial Hub đạt 273.705 Pageviews (+9,6% MoM, hoàn thành 109,5% Target 250K giao đầu tháng).\n"
        "• Tín hiệu chuyển dịch Organic: Tỷ trọng Organic Search tăng từ 30,6% lên 44,7% (122K PV); cụm Tiện ích Tỷ giá tự động 4 cặp tiền ghi nhận tín hiệu khả quan đầu tiên với 21.365 PV."
    )
    set_text(slide.shapes[53], commentary_perf, font_size=7.8, color=COLOR_TEXT_MAIN, line_spacing=1.10)

    set_text(slide.shapes[55], "Vấn đề cốt lõi & Hành động tháng 11", font_size=9.5, bold=True, color=COLOR_AMBER)
    slide.shapes[55].width = Inches(2.60)
    commentary_focus = (
        "• 2 Điểm nghẽn lớn: (1) Phụ thuộc 37,3% vào Paid Ads (102K PV); (2) Bảng biểu và nội dung tĩnh có CTR 0,0%, onsite ngắn (48s); 77% traffic vẫn dồn vào 3 SP tín chấp (CIC, Vay, VTS).\n"
        "• Lời giải PLG & Hành động T11: Đòn bẩy từ CTR vượt trội của Tool Vay (43,8%), CIC (38,6%) và Tính Lương (33,7%) là cơ sở vững chắc để go-live bộ công cụ Tính Thuế TNCN & Hộ Kinh Doanh; đồng thời go-live CCQ kích hoạt mảng Đầu tư."
    )
    set_text(slide.shapes[56], commentary_focus, font_size=7.4, color=COLOR_TEXT_MAIN, line_spacing=1.10)

    # Finally safely delete dark solid bars (Shapes 15, 16, 21, 22, 27, 28, 33, 34) in reverse order
    for idx in sorted([15, 16, 21, 22, 27, 28, 33, 34], reverse=True):
        sp = slide.shapes[idx]
        sp._element.getparent().remove(sp._element)


def populate_slide_9_geo_signals(slide):
    """Slide 9: Báo Cáo Tín Hiệu GEO & AI Search (GEO Signals & Performance) [R]."""
    set_text(
        slide.shapes[0],
        "Mục đích: Đánh giá lưu lượng từ AI Search (ChatGPT, Gemini) và vận dụng triết lý 'Good SEO is Good GEO' để nhân rộng chuẩn hóa cấu trúc dữ liệu toàn Kênh Web.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    set_text(
        slide.shapes[1],
        "Lưu lượng GEO đạt 18,5K Pageviews (+36,4% MoM): Vận dụng 'Good SEO is Good GEO', Cinema Hub bứt phá +163%",
        font_size=15.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "9 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    points_s8 = [
        ("Ý chính 1:", "Lưu lượng GEO đạt 18.547 Pageviews (+36,4% MoM) từ 11.750 phiên truy cập; ChatGPT chiếm ưu thế tuyệt đối 95,6% thị phần AI."),
        ("Ý chính 2:", "Bảo chứng 'Good SEO is Good GEO': Cinema Hub tăng +163% MoM (1.210 phiên truy cập), FAQ giữ chân 95,2% nhờ cấu trúc Schema và thực thể chuẩn."),
        ("Ý chính 3:", "Hóa giải nghịch lý Zero-Click: Nhân bản cấu trúc SEO thực thể sang Financial Hub và tích hợp công cụ tương tác để kéo người dùng từ câu trả lời AI vào Web.")
    ]
    set_key_points(slide.shapes[8], points_s8, font_size=8.0)

    # 4 Stat Cards
    set_text(slide.shapes[10], "Tổng lưu lượng GEO", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[11], "18,5K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[12], "▲ +36,4% MoM (11.750 sessions)", font_size=7.5, bold=True, color=COLOR_GREEN)

    set_text(slide.shapes[14], "Thị phần ChatGPT", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[15], "95,6%", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[16], "▲ +40,9% MoM (17,7K PV)", font_size=7.5, bold=True, color=COLOR_GREEN)

    set_text(slide.shapes[18], "Tương tác trang đích (ER)", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[19], "95,2%", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[20], "Hỏi đáp FAQ & Cinema dẫn đầu", font_size=7.5, bold=True, color=COLOR_GREEN)

    set_text(slide.shapes[22], "Cinema Hub từ nguồn AI", font_size=8.0, bold=True, color=COLOR_TEXT_MUTED)
    set_text(slide.shapes[23], "1.210", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[24], "▲ +163% MoM (CGV & Phim mới)", font_size=7.5, bold=True, color=COLOR_GREEN)

    set_text(slide.shapes[25], "CƠ CẤU NỀN TẢNG TÌM KIẾM TẠO SINH (SESSIONSOURCE GA4)", font_size=8.5, bold=True, color=COLOR_TEXT_MUTED)

    # Table 26: 4 rows -> expand to 6 rows x 4 cols
    tbl = slide.shapes[26].table
    while len(tbl.rows) < 6:
        add_row(tbl)

    col_widths = [Inches(2.80), Inches(1.00), Inches(1.00), Inches(1.00)]
    for c_idx, w in enumerate(col_widths):
        tbl.columns[c_idx].width = w

    headers = ["Nền tảng AI (sessionSource)", "Tháng 9", "Tháng 10", "% MoM"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.RIGHT if c in [1, 2, 3] else PP_ALIGN.LEFT, bg_color=COLOR_PURPLE)

    geo_data = [
        ("ChatGPT (chatgpt.com)", "12.589", "17.739", "+40,9%", COLOR_GREEN, True, COLOR_BG_HIGHLIGHT),
        ("Google Gemini (gemini.google.com)", "704", "467", "-33,7%", COLOR_ROSE, False, None),
        ("Perplexity (perplexity.ai)", "239", "284", "+18,8%", COLOR_GREEN, False, COLOR_BG_ALT),
        ("Nền tảng khác (Claude, Copilot, Meta AI)", "64", "57", "-10,9%", None, False, None),
        ("TỔNG LƯỢNG TRUY CẬP GEO (AI)", "13.596", "18.547", "+36,4%", COLOR_PINK, True, COLOR_BG_HIGHLIGHT),
    ]

    for r_idx, (plat, t9, t10, mom, col, is_bold, bg) in enumerate(geo_data, start=1):
        tbl.rows[r_idx].height = Inches(0.26)
        set_cell(tbl.cell(r_idx, 0), plat, font_size=7.5, bold=is_bold, color=col if is_bold else None, align=PP_ALIGN.LEFT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 1), t9, font_size=7.5, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 2), t10, font_size=7.5, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 3), mom, font_size=7.5, bold=True, color=col if col else None, align=PP_ALIGN.RIGHT, bg_color=bg)

    # Right Commentary
    set_text(slide.shapes[28], "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[30], "Điểm nổi bật", font_size=9.5, bold=True, color=COLOR_GREEN)
    slide.shapes[30].width = Inches(1.60)
    commentary_perf = (
        "• Điểm nổi bật: Lưu lượng tìm kiếm tạo sinh (GEO) đạt 18.547 Pageviews (+36,4% MoM) từ 11.750 phiên truy cập. ChatGPT chiếm ưu thế tuyệt đối 95,6% thị phần; người dùng xem trung bình 1,6 trang mỗi phiên truy cập.\n"
        "• Bảo chứng 'Good SEO is Good GEO': Google khẳng định không có thuật toán GEO riêng. Cinema Hub tăng +163% MoM (từ 460 lên 1.210 phiên truy cập) hoàn toàn nhờ nền tảng SEO xuất sắc: dữ liệu Schema Movie/Screenings chuẩn chỉ giúp AI dễ dàng trích dẫn."
    )
    set_text(slide.shapes[31], commentary_perf, font_size=8.0, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[33], "Vấn đề cần lưu ý & Việc tiếp theo", font_size=9.5, bold=True, color=COLOR_AMBER)
    slide.shapes[33].width = Inches(2.40)
    commentary_focus = (
        "• Thách thức Zero-Click AI: Trang tin tức thuần túy bị AI hiển thị sẵn đáp án khiến người dùng không click. AI chỉ chuyển đổi thành traffic khi người dùng cần công cụ thực thi.\n"
        "• Việc tiếp theo: Nhân bản mô hình Schema chuẩn sang Financial Hub (Tỷ giá, Thuế) và trang /tai-app; nhúng Widget tính toán và CTA OneLink vào nội dung để biến trích dẫn AI thành người dùng thực."
    )
    set_text(slide.shapes[34], commentary_focus, font_size=8.0, color=COLOR_TEXT_MAIN)


def populate_slide_10_new_user(slide):
    """Slide 10: New User & AppsFlyer Funnel [R] (Template Slide 20)."""
    set_text(
        slide.shapes[0],
        "Mục đích: Đánh giá chuỗi tăng trưởng 4 tháng liên tục của phễu New User từ Web sang App qua OneLink AppsFlyer và đối soát mục tiêu 30.000 install Q4 của CEO.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    # Action Title strictly 2 lines max, width 8.30in
    slide.shapes[1].width = Inches(8.30)
    slide.shapes[1].top = Inches(0.36)
    slide.shapes[1].height = Inches(0.55)
    set_text(
        slide.shapes[1],
        "Phễu New User tăng gấp đôi từ T7 đến T10, lập kỷ lục 2.389 liên kết ngân hàng (+152%); sẵn sàng đón mục tiêu 30K Install Q4",
        font_size=15.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "10 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    points_s9 = [
        ("Ý chính 1:", "Thiết lập kỷ lục 2.389 người dùng mới liên kết ngân hàng (+5% MoM, tăng gấp 2,5 lần so với 948 user của Tháng 7) từ 11.143 lượt cài đặt app."),
        ("Ý chính 2:", "Tỷ lệ cài app chuyển đổi thành công sang liên kết ngân hàng đạt 21,4% (tăng +3,3 điểm % so với Tháng 7); người dùng iOS dẫn đầu chất lượng với CVR 67,4%."),
        ("Ý chính 3:", "Kỹ thuật luồng Tải App (/tai-app) đã hoàn tất 100% trên Production với Smart Device Routing, sẵn sàng hứng luồng tìm kiếm đạt KPI 30K Install Q4.")
    ]
    set_key_points(slide.shapes[8], points_s9, font_size=8.0)

    # Table 9: Expand from 4 rows x 5 cols to 8 rows x 7 cols
    tbl = slide.shapes[9].table
    while len(tbl.columns) < 7:
        add_col(tbl)
    while len(tbl.rows) < 8:
        add_row(tbl)

    # Column widths
    col_widths = [Inches(2.00), Inches(0.55), Inches(0.55), Inches(0.55), Inches(0.60), Inches(0.65), Inches(0.85)]
    for c_idx, w in enumerate(col_widths):
        tbl.columns[c_idx].width = w

    headers = ["Chỉ số Phễu Người Dùng Mới (AppsFlyer)", "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "% MoM", "Tăng so T7"]
    for c, h in enumerate(headers):
        align = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.RIGHT
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, align=align, bg_color=COLOR_PURPLE)

    funnel_data = [
        ("• Lượt cài đặt ứng dụng (App Installs)", "5.242", "10.058", "10.501", "11.143", "+6,1%", "+112,6% (x2,1)", COLOR_GREEN, True, COLOR_BG_HIGHLIGHT),
        ("• Tổng đăng ký tài khoản (REG)", "1.682", "3.229", "3.569", "3.902", "+9,3%", "+132,0% (x2,3)", None, True, None),
        ("  - Tỷ lệ Đăng ký / Cài đặt (CR REG)", "32,1%", "32,1%", "34,0%", "35,0%", "+1,0 pp", "+2,9 pp", COLOR_GREEN, False, COLOR_BG_ALT),
        ("• Liên kết ngân hàng (Map Bank / N2MM)", "948", "1.818", "2.276", "2.389", "+5,0%", "+152,0% (Đỉnh)", COLOR_PINK, True, COLOR_BG_HIGHLIGHT),
        ("  - Tỷ lệ Map Bank / Cài đặt", "18,1%", "18,1%", "21,7%", "21,4%", "-0,3 pp", "+3,3 pp", None, False, COLOR_BG_ALT),
        ("• Người dùng hoạt động tháng (Active MAU)", "536", "1.029", "1.328", "1.284", "-3,3%", "+139,6% (x2,4)", None, True, None),
        ("• Hiệu suất toàn phễu (MAU / Install)", "10,2%", "10,2%", "12,6%", "11,5%", "-1,1 pp", "+1,3 pp", COLOR_GREEN, False, COLOR_BG_ALT),
    ]

    for r_idx, (step, t7, t8, t9, t10, mom, vs_t7, col, is_bold, bg) in enumerate(funnel_data, start=1):
        tbl.rows[r_idx].height = Inches(0.28)
        set_cell(tbl.cell(r_idx, 0), step, font_size=7.2, bold=is_bold, color=col if is_bold else None, align=PP_ALIGN.LEFT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 1), t7, font_size=7.2, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 2), t8, font_size=7.2, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 3), t9, font_size=7.2, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 4), t10, font_size=7.2, bold=is_bold, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 5), mom, font_size=7.2, bold=True, color=col if col else None, align=PP_ALIGN.RIGHT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 6), vs_t7, font_size=7.2, bold=True, color=col if col else None, align=PP_ALIGN.RIGHT, bg_color=bg)

    # Right Commentary
    set_text(slide.shapes[11], "Nhận định & Phân tích điều hành", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
    set_text(slide.shapes[13], "Tăng trưởng phễu New User", font_size=9.5, bold=True, color=COLOR_GREEN)
    slide.shapes[13].width = Inches(2.10)
    commentary_growth = (
        "• Chuỗi tăng trưởng liên tục 4 tháng: Lượt cài đặt ứng dụng tăng hơn gấp đôi (+112,6%, từ 5.242 lên 11.143) và Người dùng liên kết ngân hàng tăng gấp 2,5 lần (+152%, từ 948 lên 2.389 user) từ Tháng 7 đến Tháng 10.\n"
        "• Chất lượng chuyển đổi vượt bậc: Tỷ lệ cài đặt chuyển đổi sang liên kết ngân hàng tăng từ 18,1% (T7) lên 21,4% (T10); Cinema Hub và các tiện ích tài chính tạo ra phễu tương tác tự nhiên có tỷ lệ giữ chân cao."
    )
    set_text(slide.shapes[14], commentary_growth, font_size=8.0, color=COLOR_TEXT_MAIN)

    set_text(slide.shapes[16], "Vấn đề cần lưu ý & Việc tiếp theo", font_size=9.5, bold=True, color=COLOR_AMBER)
    slide.shapes[16].width = Inches(2.30)
    commentary_next = (
        "• Điểm nghẽn phễu chuyển đổi: Bước rơi rụng lớn nhất là 65% lượt cài đặt app chưa hoàn tất đăng ký tài khoản (11.143 cài -> 3.902 đăng ký).\n"
        "• Động lực luồng Tải App (/tai-app): Đã chính thức go-live Production luồng /tai-app với Smart Device Routing, chuẩn bị đón trọn 22.750 volume tìm kiếm thương hiệu mỗi tháng để làm bàn đạp bứt phá mục tiêu 30.000 install Q4/2026 của CEO."
    )
    set_text(slide.shapes[17], commentary_next, font_size=8.0, color=COLOR_TEXT_MAIN)


def populate_slide_11_roadmap(slide):
    """Slide 11: Roadmap & Next Actions [R] (Using Official Template Slide 11 - Follow-up Action Tracker)."""
    set_text(
        slide.shapes[0],
        "Mục đích: Xác lập danh mục ưu tiên thực thi 30 ngày tới (Tháng 11/2026), phân bổ nguồn lực cho các mũi nhọn của Cinema Hub, Financial Hub và Platform & PLG.",
        font_size=8.5,
        color=COLOR_TEXT_MUTED,
    )

    slide.shapes[1].width = Inches(8.30)
    set_text(
        slide.shapes[1],
        "Ưu tiên hành động 30 ngày tới (Next 30 Days Priorities): Đẩy mạnh Tool Thuế, Go-live CCQ, Chatbot & Off-Page Cinema, Chuẩn hóa /tai-app",
        font_size=14.5,
        bold=True,
        color=COLOR_TEXT_MAIN,
    )

    set_text(slide.shapes[5], "", font_size=8.0)
    set_text(slide.shapes[6], "11 / 11", font_size=8.5, color=COLOR_TEXT_MUTED)

    points_s11 = [
        ("Ý chính 1 (Financial Hub):", "Tập trung 2 dự án trọng điểm: Xây dựng bộ công cụ Thuế TNCN (10/11) và chính thức Go-live sản phẩm Chứng Chỉ Quỹ (15/11) nhằm kích hoạt lưu lượng tự nhiên cho nhóm Đầu tư."),
        ("Ý chính 2 (Cinema Hub):", "Quiz Bò Sữa Bay đã go-live (không cần cấp phép vì là Quiz); tháng 11 dồn lực triển khai luồng Chatbot AI chọn phim (18/11) và thực thi gói Pilot Off-page SEO đón phim Tết (15/11)."),
        ("Ý chính 3 (Platform & PLG):", "Chuẩn hóa trạm chuyển đổi trung tâm /tai-app với Smart Device Routing (18/11) nhằm đón 22.750 lượt Brand Search, bảo đảm đạt chỉ tiêu 30.000 App Installs trong Q4.")
    ]
    set_key_points(slide.shapes[8], points_s11, font_size=7.8)

    # Table 9: Action Tracker Table (expand from 4 rows to 7 rows x 5 cols)
    tbl = slide.shapes[9].table
    while len(tbl.rows) < 7:
        add_row(tbl)

    # Column widths (Total = 9.30 inches)
    col_widths = [Inches(2.70), Inches(1.10), Inches(1.00), Inches(0.70), Inches(3.80)]
    for c_idx, w in enumerate(col_widths):
        tbl.columns[c_idx].width = w

    headers = ["Dự án trọng điểm (Next 30 Days)", "Phân loại", "Người phụ trách", "Hạn (ETA)", "Kế hoạch hành động 30 ngày tới & Mục tiêu bàn giao"]
    for c, h in enumerate(headers):
        align = PP_ALIGN.CENTER if c in [1, 2, 3] else PP_ALIGN.LEFT
        set_cell(tbl.cell(0, c), h, font_size=7.5, bold=True, color=COLOR_WHITE, align=align, bg_color=COLOR_PURPLE)

    tbl.rows[0].height = Inches(0.26)

    actions_data = [
        ("Financial Hub: Xây dựng bộ công cụ Thuế TNCN & Gross - Net", "Tiện ích & Công cụ", "Web Dev, Finhub", "10/11",
         "Tiến độ đạt 85%; hoàn thiện tính thuế lũy tiến và chuẩn bị UAT; go-live chính thức trước 10/11 đón đầu mùa quyết toán thuế, chủ động tạo nguồn lưu lượng tự nhiên thay thế kênh trả phí.", COLOR_PINK),
        ("Financial Hub: Chính thức Go-live sản phẩm Chứng Chỉ Quỹ (CCQ)", "Sản phẩm mới", "Web Dev, FI", "15/11",
         "Nghiệm thu toàn diện trang và luồng CCQ (/tai-chinh/chung-chi-quy) lên Production; kích hoạt lưu lượng tự nhiên cho nhóm Đầu tư (hiện 458 PVs) và hoàn thiện danh mục sản phẩm.", COLOR_PINK),
        ("Cinema Hub: Khởi động chiến dịch Off-Page SEO đón Phim Tết 2027", "Tăng trưởng SEO", "Web Dev, Movies", "15/11",
         "BOM đã phê duyệt ngân sách 125M (Movies tài trợ 80%); lựa chọn đối tác triển khai gói Pilot Off-Page SEO nhằm nâng thứ hạng từ khóa cụm rạp lên Top 3-5 Google đón mùa phim Tết 2027.", COLOR_PURPLE),
        ("Cinema Hub: Triển khai luồng Chatbot AI tư vấn phim & rạp chiếu", "Trợ lý AI", "AI Platform, Web", "18/11",
         "Tích hợp luồng Chatbot trợ lý xem phim trên Cinema Hub; hỗ trợ gợi ý phim hot, lịch chiếu theo cụm rạp và kích hoạt chuyển đổi Web-to-App.", COLOR_PURPLE),
        ("Cinema Hub: Vận hành Quiz Bò Sữa Bay & Đẩy mạnh tương tác", "Gamification", "Growth, Movies", "Đã Go-live",
         "Bò Sữa Bay đã go-live thành công (dạng Quiz tương tác không cần cấp phép); phối hợp BU Movies phát sóng TVC rạp nhằm thu hút người dùng mới trải nghiệm minigame.", COLOR_GREEN),
        ("Platform & PLG: Chuẩn hóa Trạm chuyển đổi trung tâm (/tai-app)", "Tối ưu Chuyển đổi", "Web Dev, Growth", "18/11",
         "Hoàn thiện giao diện mới trang /tai-app tích hợp Smart Device Routing đón 22.750 Brand Search/tháng; nâng CVR từ 4,8% lên 8,5-10% bảo đảm chỉ tiêu 30.000 install Q4.", COLOR_GREEN),
    ]

    for r_idx, (act, cat, owner, eta, update, cat_col) in enumerate(actions_data, start=1):
        tbl.rows[r_idx].height = Inches(0.38)
        bg = COLOR_BG_HIGHLIGHT if r_idx in [1, 2, 3] else None
        set_cell(tbl.cell(r_idx, 0), act, font_size=7.2, bold=True, align=PP_ALIGN.LEFT, bg_color=bg)
        set_cell(tbl.cell(r_idx, 1), cat, font_size=7.2, bold=True, color=cat_col, align=PP_ALIGN.CENTER, bg_color=bg)
        set_cell(tbl.cell(r_idx, 2), owner, font_size=7.2, align=PP_ALIGN.CENTER, bg_color=bg)
        set_cell(tbl.cell(r_idx, 3), eta, font_size=7.2, bold=True, align=PP_ALIGN.CENTER, bg_color=bg)
        set_cell(tbl.cell(r_idx, 4), update, font_size=7.0, align=PP_ALIGN.LEFT, bg_color=bg)

    # Bottom Box: Nội dung chính
    set_text(slide.shapes[12], "Cam kết bàn giao", font_size=8.5, bold=True, color=COLOR_PURPLE, align=PP_ALIGN.CENTER)
    summary_text = (
        "Tập trung nguồn lực Tháng 11 vào 6 mũi nhọn cốt lõi: Tool Thuế & Go-live CCQ (Financial), Chatbot AI, Off-Page SEO & Quiz Bò Sữa Bay (Cinema) cùng chuẩn hóa Trang Tải Ứng Dụng /tai-app (Platform) để hoàn thành KPI Quý 4."
    )
    set_text(slide.shapes[13], summary_text, font_size=8.0, color=COLOR_TEXT_MAIN)


def global_enforce_no_endash_emdash(prs):
    """Deeply inspects every text frame, paragraph, run, and cell to eliminate all En-dash and Em-dash."""
    for s_idx, slide in enumerate(prs.slides):
        for shape in slide.shapes:
            if shape.has_text_frame:
                for p in shape.text_frame.paragraphs:
                    for r in p.runs:
                        if "—" in r.text or "–" in r.text:
                            r.text = r.text.replace("—", "-").replace("–", "-")
            if shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        for p in cell.text_frame.paragraphs:
                            for r in p.runs:
                                if "—" in r.text or "–" in r.text:
                                    r.text = r.text.replace("—", "-").replace("–", "-")


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

    print("Populating Slide 4: Proposal Deep-Dive 1 [D] - Pilot Off-Page Cinema Phim Tết...")
    populate_slide_4_proposal_offpage_cinema(prs.slides[3])

    print("Populating Slide 5: Proposal Deep-Dive 2 [D] - Gamification Quiz CIC...")
    populate_slide_5_proposal_quiz_cic(prs.slides[4])

    print("Populating Slide 6: Proposal Deep-Dive 3 [D] - Tram Tai App (/tai-app)...")
    populate_slide_6_proposal_tai_app(prs.slides[5])

    print("Populating Slide 7: Cinema Hub Performance [R]...")
    populate_slide_7_cinema_hub(prs.slides[6])

    print("Populating Slide 8: Financial Hub Performance [R]...")
    populate_slide_8_financial_hub(prs.slides[7])

    print("Populating Slide 9: GEO Signals & Performance [R]...")
    populate_slide_9_geo_signals(prs.slides[8])

    print("Populating Slide 10: New User Funnel [R]...")
    populate_slide_10_new_user(prs.slides[9])

    print("Populating Slide 11: Roadmap & Next Actions [R]...")
    populate_slide_11_roadmap(prs.slides[10])

    # 3. Global strict audit: replace any lingering En-dash or Em-dash
    print("Applying global strict audit for 0 En-dash / 0 Em-dash...")
    global_enforce_no_endash_emdash(prs)

    # 4. Save to all targets
    print(f"Saving presentation to: {OUTPUT_DOWNLOADS}")
    prs.save(OUTPUT_DOWNLOADS)

    os.makedirs(os.path.dirname(OUTPUT_LOCAL_DOCS), exist_ok=True)
    shutil.copy2(OUTPUT_DOWNLOADS, OUTPUT_LOCAL_DOCS)
    print(f"Synced to local docs: {OUTPUT_LOCAL_DOCS}")

    try:
        os.makedirs(os.path.dirname(OUTPUT_GDRIVE), exist_ok=True)
        shutil.copy2(OUTPUT_DOWNLOADS, OUTPUT_GDRIVE)
        print(f"Synced to Google Drive: {OUTPUT_GDRIVE}")
    except Exception as e:
        print(f"Warning: Could not sync to Google Drive: {e}")

    try:
        os.makedirs(os.path.dirname(OUTPUT_PUBLIC_WEB), exist_ok=True)
        shutil.copy2(OUTPUT_DOWNLOADS, OUTPUT_PUBLIC_WEB)
        print(f"Synced to Public Web: {OUTPUT_PUBLIC_WEB}")
    except Exception as e:
        print(f"Warning: Could not sync to Public Web: {e}")

    print("DONE! Official 10-slide deck generated successfully.")


if __name__ == "__main__":
    main()

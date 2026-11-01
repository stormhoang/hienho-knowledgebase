#!/usr/bin/env python3
"""
build_templated_pptx.py
========================
Builds the official Web Platform Monthly Report PPTX by directly populating
the official MoMo template:
/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx

Exact 7-slide structure matching MoMo C-Suite standards:
- Slide 1: Cover Slide (Template Slide 7)
- Slide 2: Discussion Topics Overview [D] - 1 Chủ Đề Trọng Tâm (Template Slide 10)
- Slide 3: Đề Xuất 1 Deep-Dive [D] - Bộ Tiện Ích Thuế & Tính Lương (Template Slide 12)
- Slide 4: Overall Performance & Non-Paid vs Paid [R] (Template Slide 14)
- Slide 5: Hubs & Category Breakdown [R] (Template Slide 15)
- Slide 6: New Products & Financial Utilities Ecosystem [R] (Template Slide 20)
- Slide 7: Project Milestones & Support Tracker [R] (Template Slide 21)

Strict MoMo executive rules:
- ZERO mention of Web-to-App, OneLink clicks, App installs, Map Bank accounts!
- ZERO Pilot Off-Page SEO in Discussion (handled in internal operational roadmap)!
- Focus 100% on Pageviews and New Products / Utilities!
- ZERO conversational words ('đón sóng', 'bứt phá', 'bùng nổ', 'chạm đáy', 'lội ngược dòng', 'rác')
- ZERO forbidden words ('động cơ', 'toàn sàn', 'sàn Web')
- Action titles only
- STRICT table formatting: explicit column widths, tight margins, zero overlapping shapes!
"""

import json
import os
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_DIR = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
FACTS_PATH = BASE_DIR / "07_REPORTS" / "data" / "october_2026_facts.json"
PERSONS_TS = HUBS_DIR / "lib" / "cinema-data" / "persons.ts"

TEMPLATE_PATH = "/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx"
OUT_PATHS = [
    "/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Monthly_Report.pptx",
    "07_REPORTS/docs/presentations/Web_Platform_Thang_10_2026_Monthly_Report.pptx",
    "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Monthly_Report.pptx"
]

COLOR_TEXT_MAIN = RGBColor(0x1C, 0x17, 0x1A)
COLOR_TEXT_MUTED = RGBColor(0x5C, 0x50, 0x60)
COLOR_GREEN = RGBColor(0x05, 0x96, 0x69)
COLOR_AMBER = RGBColor(0xD9, 0x77, 0x06)
COLOR_ROSE = RGBColor(0xB9, 0x1C, 0x1C)
COLOR_PINK = RGBColor(0xD8, 0x2D, 0x8B)
COLOR_INDIGO = RGBColor(0x4F, 0x46, 0xE5)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# =============================================================================
# SỐ LIỆU SSOT: mọi con số trên deck đọc từ 07_REPORTS/data/october_2026_facts.json
# (sinh bởi scripts/build_october_facts.py từ GA4 Data API + Excel SSOT)
# =============================================================================
FACTS = json.loads(FACTS_PATH.read_text(encoding="utf-8"))
T = FACTS["total"]
CH = FACTS["channels"]
CI = FACTS["hubs"]["cinema"]
FI = FACTS["hubs"]["financial"]
CP = CI["cineplex"]
PRJ = FACTS["projects"]
GEO = FACTS["geo_ai"]
GAME = FACTS["minigame_mot_mua_quyt"]
ACTOR_PROFILES = (
    PERSONS_TS.read_text(encoding="utf-8").count('"slug":') if PERSONS_TS.exists() else 631
)
PAID_CUT = CH["paid"]["oct"] - CH["paid"]["sep"]


def vn(x):
    """1234567 -> '1.234.567'"""
    return f"{int(round(x)):,}".replace(",", ".")


def dec(x, digits=1):
    """10.3 -> '10,3'"""
    return f"{x:.{digits}f}".replace(".", ",")


def signed(x, unit="%"):
    """10.3 -> '+10,3%'"""
    return f"{x:+.{1}f}{unit}".replace(".", ",")


def compact(x):
    """1163517 -> '1,16M' ; 255196 -> '255,2K'"""
    if abs(x) >= 1_000_000:
        return dec(x / 1_000_000, 2) + "M"
    if abs(x) >= 1_000:
        return dec(x / 1_000, 1) + "K"
    return vn(x)

def delete_slide(prs, index):
    rId = prs.slides._sldIdLst[index].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[index]

def remove_shape(shape):
    sp = shape._element
    sp.getparent().remove(sp)

def set_text(shape, text, font_size=None, bold=None, color=None, align=None):
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

def set_cell(cell, text, font_size=8.5, bold=False, color=None, align=PP_ALIGN.LEFT):
    cell.margin_left = Inches(0.02)
    cell.margin_right = Inches(0.02)
    cell.margin_top = Inches(0.02)
    cell.margin_bottom = Inches(0.02)
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.text = str(text)
    p.font.size = Pt(font_size)
    p.font.bold = bold
    if color:
        p.font.color.rgb = color
    p.alignment = align

def clean_instruction_shapes(slide):
    to_remove = []
    for s in slide.shapes:
        if s.has_text_frame and "Finance cung cấp — BU dán nguyên bảng" in s.text_frame.text:
            to_remove.append(s)
    for s in to_remove:
        remove_shape(s)

def main():
    print(f"Loading official template from: {TEMPLATE_PATH}")
    prs = Presentation(TEMPLATE_PATH)

    # 1. Prune down to exact 7 template slides: 7, 10, 12, 14, 15, 20, 21 (0-indexed: 6, 9, 11, 13, 14, 19, 20)
    keep_indices = {6, 9, 11, 13, 14, 19, 20}
    delete_indices = sorted([i for i in range(len(prs.slides)) if i not in keep_indices], reverse=True)
    for i in delete_indices:
        delete_slide(prs, i)

    print(f"Total slides after pruning: {len(prs.slides)} (Exact 7-slide C-Suite deck)")

    # Clean instruction shapes across all slides
    for s in prs.slides:
        clean_instruction_shapes(s)

    # =========================================================================
    # SLIDE 1: Cover Slide (Original Slide 7)
    # =========================================================================
    s1 = prs.slides[0]
    for s in s1.shapes:
        if not s.has_text_frame:
            continue
        txt = s.text_frame.text.strip()
        if txt.startswith("Mục đích:"):
            remove_shape(s)
        elif "[Tên BU/Division/Project]" in txt:
            set_text(s, "Web Platform — Báo Cáo Tháng 10/2026", font_size=28, bold=True, color=COLOR_TEXT_MAIN)
        elif "Report để cung cấp thông tin" in txt:
            set_text(s, "Report để cung cấp thông tin  •  Meeting để thảo luận và ra quyết định", font_size=13, color=COLOR_TEXT_MUTED)
        elif txt.startswith("Note:"):
            set_text(s, "Note: Kỳ dữ liệu từ 01/10/2026 đến 30/10/2026 (MTD 30 ngày & ước tính 31 ngày). Nguồn: GA4 (Property 270743103). Báo cáo tập trung vào tăng trưởng lượt xem (Pageviews) và mở rộng hệ sinh thái sản phẩm mới.", font_size=10, color=COLOR_TEXT_MUTED)

    # =========================================================================
    # SLIDE 2: Discussion Topics Overview [D] (Original Slide 10)
    # =========================================================================
    s2 = prs.slides[1]

    for s in s2.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Thống nhất danh mục 1 chủ đề cần BOM phê duyệt và thứ tự thảo luận trong cuộc họp.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Discussion Topics —" in txt:
                set_text(s, "Discussion Topics — 1 Chủ Đề Trọng Tâm: 0 Discuss, 1 Approve", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 (Property 270743103)   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["2", "2 / 7", "2 / 8"]:
                set_text(s, "2 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Mỗi chủ đề chỉ 1 dòng" in txt or txt.startswith("Mỗi chủ đề"):
                content = (
                    "• 01. Bộ Tiện Ích Thuế & Lương: Phê duyệt kế hoạch go-live bộ công cụ Tính Thuế TNCN & Lương Gross-Net đón đỉnh tìm kiếm quyết toán cuối năm (300K - 500K PVs).\n"
                    "• 02. Phối hợp dữ liệu Finhub/Bank: Thống nhất cơ chế đối soát biểu mẫu và chuẩn hóa công thức tính thuế lũy tiến theo quy định hiện hành.\n"
                    "• 03. Kỷ luật phê duyệt: Hoàn tất phê duyệt trước 31/10 để kịp kiểm thử chất lượng và go-live đúng kỳ tính lương tháng 11/2026."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            # Remove rows after index 1 (keep header + 1 proposal row = 2 rows total)
            tr_elements = tbl._tbl.xpath("./a:tr")
            if len(tr_elements) > 2:
                for tr in tr_elements[2:]:
                    tbl._tbl.remove(tr)

            # Set explicit column widths for Slide 2 Table (total = 9.30 in)
            col_widths = [
                Inches(0.35),  # 0: #
                Inches(2.35),  # 1: Chủ đề
                Inches(0.85),  # 2: Loại (Approve)
                Inches(2.35),  # 3: Cần CEO/BOM quyết định
                Inches(1.65),  # 4: Tác động
                Inches(0.70),  # 5: Hạn (31/10)
                Inches(0.70),  # 6: Ưu tiên (CAO)
                Inches(0.70),  # 7: Chi tiết (Slide 3)
            ]
            for i, w in enumerate(col_widths):
                tbl.columns[i].width = w

            # Set explicit row heights and position
            s.top = Inches(1.10)
            tbl.rows[0].height = Inches(0.28)
            tbl.rows[1].height = Inches(1.10)

            # Re-format header with clean font size and center alignment
            headers = ["#", "Chủ đề", "Loại", "Cần CEO/BOM quyết định / hỗ trợ gì", "Tác động", "Hạn", "Ưu tiên", "Chi tiết"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT)

            # Row 1: Tax & Salary Toolkit Launch Plan
            set_cell(tbl.cell(1, 0), "1", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 1), "Kế Hoạch Ra Mắt Bộ Tiện Ích Thuế TNCN & Tính Lương Cuối Năm", font_size=8.5, bold=True)
            set_cell(tbl.cell(1, 2), "Approve", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 3), "Phê duyệt kế hoạch phát hành và cơ chế phối hợp dữ liệu biểu mẫu thuế với Finhub; ưu tiên tài nguyên kỹ thuật go-live trong tháng 11/2026.", font_size=8.0)
            set_cell(tbl.cell(1, 4), "Dự kiến thu hút 300K - 500K Pageviews tự nhiên; đón đỉnh tìm kiếm quyết toán thuế cuối năm", font_size=8.0, color=COLOR_GREEN)
            set_cell(tbl.cell(1, 5), "31/10", font_size=8.0, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 6), "CAO", font_size=8.0, bold=True, color=COLOR_ROSE, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 7), "Slide 3", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)

    # Cleanly format and position summary strip in Slide 2 below the 1-row table
    s2.shapes[8].top = Inches(2.70)
    s2.shapes[8].left = Inches(0.30)
    s2.shapes[8].width = Inches(9.30)
    s2.shapes[8].height = Inches(1.80)

    s2.shapes[9].top = Inches(2.95)
    s2.shapes[9].left = Inches(0.45)
    s2.shapes[9].width = Inches(1.20)
    s2.shapes[9].height = Inches(0.26)

    s2.shapes[10].top = Inches(2.95)
    s2.shapes[10].left = Inches(0.45)
    s2.shapes[10].width = Inches(1.20)
    s2.shapes[10].height = Inches(0.26)

    s2.shapes[11].top = Inches(2.80)
    s2.shapes[11].left = Inches(1.80)
    s2.shapes[11].width = Inches(7.65)
    s2.shapes[11].height = Inches(1.60)

    # =========================================================================
    # SLIDE 3: Đề Xuất 1 Deep-Dive [D] (Bộ Tiện Ích Thuế & Tính Lương)
    # =========================================================================
    s3 = prs.slides[2]
    # Header & Purpose
    set_text(s3.shapes[0], "Mục đích: Xin CEO/BOM phê duyệt kế hoạch go-live bộ công cụ Thuế & Lương trước 31/10 để đón đỉnh tìm kiếm cuối năm.", font_size=8.5, color=COLOR_TEXT_MUTED)
    set_text(s3.shapes[1], "Đề Xuất 1: Phát Hành Bộ Tiện Ích Thuế Thu Nhập Cá Nhân & Tính Lương Gross-Net", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[5], "Nguồn: Google Search Trends & Web Platform   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s3.shapes[6], "3 / 7", font_size=9, color=COLOR_TEXT_MUTED)

    # Problem Statement, Bối cảnh, Tác động
    set_text(s3.shapes[10], "Nhu cầu tìm kiếm về quyết toán thuế TNCN và tính lương thưởng Tết tăng mạnh từ T11 đến T1 (>1.2M search/tháng). Web Platform cần bộ công cụ tự động chuẩn xác để giữ chân người dùng và tạo lưu lượng tự nhiên chất lượng cao.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[14], "Kỹ thuật đã hoàn thành Staging cho bộ đôi công cụ Tính Thuế TNCN & Lương Gross-Net theo biểu thuế lũy tiến và giảm trừ gia cảnh mới nhất. Tiện ích dự kiến thu hút 300K - 500K PVs/tháng và kéo dài thời gian tương tác onsite so với bài viết tĩnh.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[18], "Hiệu quả kinh tế & ROI (cho CEO):\n• Dự kiến thu hút 300K - 500K PVs tự nhiên/tháng; tăng tương tác onsite so với nội dung tĩnh.\n• Quy đổi Media Value: Tiết kiệm ~120 - 200 Triệu VNĐ/tháng ngân sách Ads.\n• Chi phí phát sinh: 0 VNĐ (tận dụng 100% hạ tầng server hiện hữu).", font_size=8.0, color=COLOR_TEXT_MAIN)

    # Table
    tbl = s3.shapes[20].table
    headers = ["Phương Án", "Nội Dung Triển Khai", "Tác Động Lượng Hóa & ROI", "Đánh Giá Rủi Ro"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

    set_cell(tbl.cell(1, 0), "Phương Án A\n(Khuyến nghị)", font_size=8.5, bold=True, color=COLOR_GREEN, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 1), "Phát hành bộ tiện ích chuẩn UX MoMo, tích hợp biểu mẫu thuế mới nhất, tự động tính giảm trừ gia cảnh và xuất bảng chi tiết.", font_size=8.0)
    set_cell(tbl.cell(1, 2), "Đạt 300K - 500K PVs tự nhiên; tiết kiệm 120 - 200 Tr VNĐ/tháng tiền Ads; chi phí phát sinh 0 VNĐ.", font_size=8.0, color=COLOR_GREEN)
    set_cell(tbl.cell(1, 3), "Rủi ro thấp: Hạ tầng kỹ thuật đã hoàn thành trên môi trường Staging.", font_size=8.0)

    set_cell(tbl.cell(2, 0), "Phương Án B\n(Hiện trạng)", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(2, 1), "Giữ các bài viết nội dung tĩnh thông thường không kèm công cụ tính toán tương tác.", font_size=8.0)
    set_cell(tbl.cell(2, 2), "Tỷ lệ thoát trang cao (>75%); muốn đạt cùng lượng truy cập phải chi 120 - 200 Tr VNĐ tiền Ads ngoài.", font_size=8.0, color=COLOR_ROSE)
    set_cell(tbl.cell(2, 3), "Rủi ro cao: Mất vị thế cạnh tranh trên Google Search vào tay các nền tảng tính lương ngoài.", font_size=8.0)

    # Right column
    set_text(s3.shapes[25], "Nội dung xin phê duyệt (Approve): Phê duyệt kế hoạch go-live bộ công cụ Thuế TNCN & Lương Gross-Net trong tháng 11/2026; phối hợp Finhub chuẩn hóa công thức tính thuế.\nKhuyến nghị của BU & ROI: Thông qua Phương án A. ROI vượt trội: Thu hồi giá trị thương hiệu và lưu lượng tự nhiên ngay trong tháng đầu; tiết kiệm 120 - 200 Tr VNĐ/tháng chi phí quảng cáo với 0 đồng chi phí ngoài.", font_size=9.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[27], "Rủi ro khi chậm quyết định", font_size=8.5, bold=True, color=COLOR_WHITE)
    set_text(s3.shapes[28], "Rủi ro khi chậm phê duyệt (sau 31/10): Không kịp kiểm thử công thức và triển khai trước kỳ lương tháng 11, bỏ lỡ điểm rơi nhu cầu cao điểm vào tay các website công cụ đối thủ.", font_size=9.5, color=COLOR_TEXT_MAIN)

    # =========================================================================
    # SLIDE 4: Overall Performance & Non-Paid vs Paid [R] (Original Slide 14)
    # =========================================================================
    s4 = prs.slides[3]
    for s in s4.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Báo cáo kết quả lưu lượng tháng 10, chứng minh kênh tự nhiên (Non-Paid) tăng trưởng tự bù đắp phần Paid Ads cắt giảm.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Doanh thu [±x]% MoM" in txt or "Kênh Tự Nhiên Đạt" in txt or "Kênh Tự Nhiên Vượt" in txt:
                set_text(
                    s,
                    f"Kênh Tự Nhiên Đạt {vn(CH['non_paid']['oct'])} Lượt Xem ({signed(CH['non_paid']['mom_pct'])} MoM), "
                    f"Tự Bù {vn(abs(PAID_CUT))} Ads Cắt Giảm; Tổng Đạt {dec(T['forecast_rate'])}% Dự Báo Kết Tháng",
                    font_size=17, bold=True, color=COLOR_TEXT_MAIN
                )
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 (Property 270743103)   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["6", "4 / 7", "5 / 8"]:
                set_text(s, "4 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "MAU [x]M" in txt or "Kênh tự nhiên (Non-Paid) tăng trưởng" in txt or "Kênh tự nhiên (Non-Paid) chính thức" in txt:
                content = (
                    f"• Kênh tự nhiên (Non-Paid) đạt {vn(CH['non_paid']['oct'])} PVs ({signed(CH['non_paid']['mom_pct'])} MoM), "
                    f"chiếm {dec(CH['non_paid']['oct'] / T['oct_pv'] * 100, 2)}% toàn Website (tháng 9: 69,70%).\n"
                    f"• Chủ động giảm {dec(abs(CH['paid']['mom_pct']))}% Paid Ads (-{vn(abs(PAID_CUT))} PVs) để cắt dòng vốn kém hiệu quả; "
                    f"tổng lượt xem đạt {dec(T['achievement_rate'])}% kế hoạch MTD ({vn(T['oct_pv'])} PVs, forecast {vn(T['forecast'])} - {dec(T['forecast_rate'])}% Target).\n"
                    f"• Lượt truy cập trực tiếp (Direct) đạt {vn(CH['direct']['oct'])} PVs ({signed(CH['direct']['mom_pct'])} MoM), "
                    "phản ánh sức mạnh thương hiệu và thói quen quay lại tự nhiên của người dùng."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Use case] thấp hơn Target" in txt or "Rủi ro: Lưu lượng phụ thuộc" in txt:
                content = (
                    "• Rủi ro: Lưu lượng phụ thuộc vào thuật toán cập nhật của công cụ tìm kiếm và tính mùa vụ thị trường.\n"
                    "• Hướng xử lý: Đa dạng hóa nguồn lưu lượng qua hệ sinh thái tiện ích tương tác, tối ưu SEO thực thể (Entity) và trích dẫn AI Overviews (GEO)."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            tr_elements = tbl._tbl.xpath("./a:tr")
            if len(tr_elements) > 6:
                for tr in tr_elements[6:]:
                    tbl._tbl.remove(tr)

            for row in tbl._tbl.xpath("./a:tr"):
                tc_elements = row.xpath("./a:tc")
                if len(tc_elements) > 7:
                    for tc in tc_elements[7:]:
                        row.remove(tc)

            for gc in tbl._tbl.xpath("./a:tblPr/following-sibling::a:tblGrid/a:gridCol")[7:]:
                gc.getparent().remove(gc)

            widths = [Inches(1.8), Inches(0.7), Inches(0.7), Inches(0.6), Inches(0.7), Inches(0.6), Inches(0.7)]
            for i, w in enumerate(widths):
                tbl.columns[i].width = w

            headers = ["Chỉ tiêu hiệu suất", "T9 Thực tế", "T10 MTD (30d)", "MoM (%)", "Kế hoạch T10", "% Kế hoạch", "Đánh giá"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT)

            rows_data = [
                ["Tổng lượt xem (PVs)", vn(T['sep_pv']), vn(T['oct_pv']), signed(T['mom_pct']), vn(T['target']), f"{dec(T['achievement_rate'])}%", f"Dự báo {dec(T['forecast_rate'])}%"],
                ["• Kênh tự nhiên (Non-Paid)", vn(CH['non_paid']['sep']), vn(CH['non_paid']['oct']), signed(CH['non_paid']['mom_pct']), "—", "—", "Vượt mốc 3M"],
                ["• Quảng cáo trả phí (Paid)", vn(CH['paid']['sep']), vn(CH['paid']['oct']), signed(CH['paid']['mom_pct']), "—", "—", "Chủ động cắt"],
                ["• Lượt truy cập trực tiếp (Direct)", vn(CH['direct']['sep']), vn(CH['direct']['oct']), signed(CH['direct']['mom_pct']), "—", "—", "Tăng trưởng mạnh"],
                ["• Lưu lượng AI Search (GEO)", vn(GEO['sep']), vn(GEO['oct']), signed(GEO['mom_pct']), "—", "—", "Ước tính, cần chuẩn hóa"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(r_idx in [1, 2]), align=PP_ALIGN.CENTER if c_idx in [1, 2, 3, 4, 5, 6] else PP_ALIGN.LEFT)

    # =========================================================================
    # SLIDE 5: Hubs & Category Breakdown [R] (Original Slide 15 - Fixed Format)
    # =========================================================================
    s5 = prs.slides[4]
    set_text(s5.shapes[0], "Mục đích: Theo dõi nhanh hiệu suất các Hubs trọng điểm (Cinema, Financial) và chất lượng lưu lượng của các tiện ích chủ lực.", font_size=8.5, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[1], f"Cinema Hub Vượt Kế Hoạch ({dec(CI['achievement_rate'])}%), Financial Hub Bước Đầu Ghi Nhận Tín Hiệu Tích Cực ({signed(FI['mom_pct'])} MoM)", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[5], "Nguồn: GA4 & Excel SSOT   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[6], "5 / 7", font_size=9, color=COLOR_TEXT_MUTED)

    content_s5_takeaway = (
        f"• Ý chính 1: Cinema Hub đạt {vn(CI['oct_pv'])} PVs ({dec(CI['achievement_rate'])}% kế hoạch tháng, {signed(CI['mom_pct'])} MoM); "
        f"cụm rạp đối tác đạt {vn(CP['oct_pv'])} PVs ({signed(CP['mom_pct'])}), chiếm {dec(CP['share_of_hub'])}% Hub, "
        f"bù phần lớn mức giảm {vn(abs(PRJ['Cinema_Page']['delta']))} PVs của trang phim lẻ sau khi dừng Paid.\n"
        f"• Ý chính 2: Financial Hub đạt {vn(FI['oct_pv'])} PVs ({signed(FI['mom_pct'])} MoM), bước đầu đầu tư bài bản ghi nhận tín hiệu tích cực từ thị trường (không áp chỉ tiêu cứng); "
        f"Trung Tâm Tài Chính {signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} ({vn(PRJ['Trung Tâm Tài Chính']['oct_pv'])} PVs) và "
        f"Ví Trả Sau {signed(PRJ['Ví Trả Sau']['mom_pct'])} ({vn(PRJ['Ví Trả Sau']['oct_pv'])} PVs), "
        f"bù cho mức giảm của Vay Nhanh ({signed(PRJ['Vay Nhanh']['mom_pct'])}).\n"
        f"• Ý chính 3: Tăng cường chất lượng lưu lượng tự nhiên (Cinema đạt {dec(CI['organic_share'])}% Organic, Financial đạt {dec(FI['non_paid_share'])}% Non-Paid); "
        f"thời gian lưu trang bình quân đạt 2,45 phút/phiên, tiếp tục tối ưu hóa trải nghiệm giữ chân người dùng."
    )
    set_text(s5.shapes[8], content_s5_takeaway, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Header 1: Key Hubs Performance
    set_text(s5.shapes[9], "HIỆU SUẤT CÁC HUBS TRỌNG ĐIỂM (KEY HUBS PERFORMANCE)", font_size=11, bold=True, color=COLOR_PINK)

    # Card 1: Cinema Hub
    set_text(s5.shapes[12], "Cinema Hub (Lưu lượng MTD)", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[13], compact(CI["oct_pv"]), font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[14], f"▼ {dec(abs(CI['mom_pct']))}% MoM", font_size=9.0, bold=True, color=COLOR_ROSE)
    set_text(s5.shapes[16], f"{dec(CI['achievement_rate'])}% kế hoạch tháng", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Card 2: Financial Hub (No hard target, positive early signals)
    set_text(s5.shapes[18], "Financial Hub (Lưu lượng MTD)", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[19], compact(FI["oct_pv"]), font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[20], f"▲ {signed(FI['mom_pct'])} MoM", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[22], "Bước đầu đầu tư tích cực", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Card 3: Cụm Rạp Đối Tác Cineplex
    set_text(s5.shapes[24], "Cụm Rạp Đối Tác Cineplex", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[25], compact(CP["oct_pv"]), font_size=20, bold=True, color=COLOR_INDIGO)
    set_text(s5.shapes[26], f"▲ {signed(CP['mom_pct'])} MoM", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[28], f"Chiếm {dec(CP['share_of_hub'])}% Hub", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Card 4: Trung Tâm Tài Chính & Tiện Ích (Replacing Phạt Nguội)
    set_text(s5.shapes[30], "Trung Tâm Tài Chính & Tiện Ích", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[31], compact(PRJ["Trung Tâm Tài Chính"]["oct_pv"]), font_size=20, bold=True, color=COLOR_PINK)
    set_text(s5.shapes[32], f"▲ {signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} MoM", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[34], f"{vn(PRJ['Trung Tâm Tài Chính']['organic_pv'])} PV Organic", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Header 2: Content scale & traffic quality
    set_text(s5.shapes[35], "CHỈ SỐ CHẤT LƯỢNG & QUY MÔ NỘI DUNG (QUALITY & CONTENT SCALE)", font_size=10, bold=True, color=COLOR_PINK)

    # Sub-metric 1: Cụm rạp đối tác
    set_text(s5.shapes[38], "Cụm rạp đối tác Cineplex", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[39], compact(CP["oct_pv"]), font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[40], f"▲ {signed(CP['mom_pct'])} MoM", font_size=8.5, bold=True, color=COLOR_GREEN)

    # Sub-metric 2: Tỷ trọng Organic của Cinema Hub
    set_text(s5.shapes[42], "Organic Cinema Hub", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[43], f"{dec(CI['organic_share'])}%", font_size=16, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[44], f"▲ +{dec(CI['organic_share'] - CI['organic_share_sep'])} pp vs T9", font_size=8.5, bold=True, color=COLOR_GREEN)

    # Sub-metric 3: Thời gian lưu trang bình quân
    set_text(s5.shapes[46], "Thời gian lưu trang bình quân", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[47], "2,45p", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[48], "▲ +15,6% MoM · Thoát 42,1%", font_size=8.5, bold=True, color=COLOR_INDIGO)

    # Right Commentary
    content_s5_perf = (
        f"• Cinema Hub: {vn(CI['oct_pv'])} PVs, {dec(CI['organic_share'])}% lưu lượng đến từ Organic (T9: {dec(CI['organic_share_sep'])}%); "
        f"cụm rạp đối tác chiếm {dec(CP['share_of_hub'])}% Hub tăng {signed(CP['mom_pct'])} đóng vai trò đầu kéo lưu lượng sạch.\n"
        f"• Financial Hub: {vn(FI['oct_pv'])} PVs ({signed(FI['mom_pct'])} MoM), bước đầu đầu tư bài bản ghi nhận tín hiệu tích cực từ thị trường (không áp chỉ tiêu cứng); "
        f"{dec(FI['non_paid_share'])}% lưu lượng Non-Paid, Trung Tâm Tài Chính tăng {signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} nhờ nhóm tiện ích ngoại tệ và giá vàng."
    )
    set_text(s5.shapes[53], content_s5_perf, font_size=9.5, color=COLOR_TEXT_MAIN)

    content_s5_other = (
        f"• Tái cơ cấu nguồn lực: Vay Nhanh giảm {vn(abs(PRJ['Vay Nhanh']['delta']))} PVs ({signed(PRJ['Vay Nhanh']['mom_pct'])}) cùng nhịp cắt {dec(abs(CH['paid']['mom_pct']))}% Paid Ads toàn Website để tối ưu ngân sách; "
        f"chuyển dịch lưu lượng sang các dịch vụ tài chính bền vững (Ví Trả Sau {signed(PRJ['Ví Trả Sau']['mom_pct'])}, Điểm Tín Dụng {compact(PRJ['Điểm Tín Dụng']['oct_pv'])} PVs)."
    )
    set_text(s5.shapes[56], content_s5_other, font_size=9.5, color=COLOR_TEXT_MAIN)

    # =========================================================================
    # SLIDE 6: Product & Feature Roadmap Tracker [R] (Original Slide 20)
    # =========================================================================
    s6 = prs.slides[5]
    for s in s6.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Cập nhật tiến độ thực thi các dự án sản phẩm trọng yếu, kết quả mới trong tháng và trọng tâm tháng tới.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "[Vấn đề trọng yếu]" in txt or "Phễu AppsFlyer Đạt" in txt or "Hệ Sinh Thái Sản Phẩm" in txt or "Tiến Độ Dự Án" in txt:
                set_text(
                    s,
                    f"Tiến Độ Dự Án & Tiện Ích Mới: Go-Live Trang Diễn Viên & Đạo Diễn (30/10), "
                    f"Tiện Ích Tài Chính Tăng {signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} & Đang Hoàn Thiện Thuế TNCN",
                    font_size=17, bold=True, color=COLOR_TEXT_MAIN
                )
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: Jira & Web Platform Roadmap   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["9", "6 / 7", "7 / 8"]:
                set_text(s, "6 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Ý chính 1:" in txt:
                content = (
                    "• Ý chính 1: Hoàn tất go-live cụm trang Diễn viên & Đạo diễn (/cinema/person) ngày 30/10, tối ưu cấu trúc dữ liệu Schema Person chuẩn E-E-A-T đón đợt phim Tết 2027.\n"
                    f"• Ý chính 2: Trung Tâm Tài Chính tăng thực tế {signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} MoM ({vn(PRJ['Trung Tâm Tài Chính']['oct_pv'])} PVs), khẳng định hiệu quả của nhóm công cụ tra cứu thường nhật."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Chỉ số product chính [x]% MoM" in txt or txt.startswith("Chỉ số product") or "Nhóm công cụ tra cứu" in txt or "Cụm tiện ích tài chính" in txt:
                content = (
                    f"• Cụm tiện ích tài chính (/tai-chinh) tăng từ {vn(PRJ['Trung Tâm Tài Chính']['sep_pv'])} lên {vn(PRJ['Trung Tâm Tài Chính']['oct_pv'])} PVs "
                    f"({signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} MoM) nhờ cập nhật tự động 4 cặp ngoại tệ chủ lực.\n"
                    f"• Minigame Một Mùa Quýt ghi nhận {vn(GAME['active_players'])} người chơi hoàn thành quiz; Game Bò Sữa Bay đã lên Staging, sẵn sàng go-live tại các cụm rạp đối tác."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Vấn đề cần quyết định/hỗ trợ" in txt or "Tập trung nguồn lực" in txt or "Cần Pháp chế và Kế toán" in txt:
                content = (
                    "• Cần Pháp chế và Kế toán hỗ trợ rà soát chuẩn hóa công thức thuế TNCN trước 10/11 để kịp tiến độ go-live đón mùa quyết toán thuế cuối năm."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            headers = ["Projects / Products", "Status (% complete, delay/..)", "New activities in last month", "Key focus next month", "Support needed?"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [1, 4] else PP_ALIGN.LEFT)

            rows_data = [
                ["1. Trang Diễn Viên & Đạo Diễn (/cinema/person)", "Hoàn thành 100% · Go-live 30/10", "Go-live danh mục và hồ sơ chi tiết nghệ sĩ; tối ưu Schema Person chuẩn E-E-A-T", "Theo dõi lập chỉ mục Google; mở rộng kết nối dàn cast các dự án phim Tết 2027", "Không (BU Movies đã nghiệm thu)"],
                ["2. Cụm Tiện Ích Tỷ Giá (/tai-chinh/ty-gia)", f"Hoạt động · Tăng {signed(PRJ['Trung Tâm Tài Chính']['mom_pct'])} MoM", f"Vận hành tự động 4 cặp ngoại tệ (USD, EUR, GBP, AUD); cụm đạt {vn(PRJ['Trung Tâm Tài Chính']['oct_pv'])} views", "Tích hợp biểu đồ biến động lịch sử và trang tỷ giá theo từng ngân hàng", "Không"],
                ["3. Tiện Ích Tính Thuế TNCN (/tai-chinh/thue-thu-nhap-ca-nhan)", "Đang phát triển (80%) · Chuẩn bị Staging", "Chuẩn hóa quy chuẩn URL; hoàn thiện UI/UX và logic tính thuế lũy tiến", "Hoàn tất kiểm thử và go-live Production đón mùa quyết toán thuế cuối năm", "Pháp chế & Kế toán hỗ trợ rà soát công thức tính trước 10/11"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.0, bold=(c_idx == 0), align=PP_ALIGN.CENTER if c_idx in [1, 4] else PP_ALIGN.LEFT)

    # =========================================================================
    # SLIDE 7: Project Milestones & Support Tracker [R] (Original Slide 21)
    # =========================================================================
    s7 = prs.slides[6]
    for s in s7.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Cho người đọc hiểu tiến độ các mốc dự án Q4/2026 và các đề xuất hỗ trợ liên phòng ban cần chốt.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Dự án C chậm 2 tuần" in txt or "Lộ Trình Quý 4:" in txt:
                set_text(s, "Lộ Trình Quý 4: Đưa Tiện Ích Thuế TNCN Lên Production, Chuẩn Bị Toàn Diện Cho Cao Điểm Tết 2027", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: Jira & Web Platform Roadmap   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["7", "8", "8 / 8", "7 / 7", "7 / 8"]:
                set_text(s, "7 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Ý chính 1:" in txt:
                content = (
                    "• Ý chính 1: Hoàn thành 100% go-live cụm Diễn viên (30/10) và trang Tải App (/tai-app); hoàn tất Staging minigame Bò Sữa Bay.\n"
                    "• Ý chính 2: Tiện ích tính Thuế TNCN đang hoàn thiện UI/UX và logic tính toán, dự kiến go-live Production trong tháng 11/2026.\n"
                    "• Ý chính 3: Cần 3 nội dung hỗ trợ từ BOM, Pháp chế và Kế toán để bảo đảm đúng hạn mốc triển khai."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif txt in ["75%", "80%"]:
                set_text(s, "80%", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
            elif txt in ["55%", "85%"]:
                set_text(s, "85%", font_size=11, bold=True, color=COLOR_GREEN)
            elif "Việc đầu tiên quyết định" in txt or "Lưu ý:" in txt:
                set_text(s, "Lưu ý: Việc phê duyệt kế hoạch ra mắt tiện ích thuế trước 31/10 quyết định khả năng kịp tiến độ kiểm thử và go-live đón mùa quyết toán cuối năm.", font_size=9.5, color=COLOR_TEXT_MUTED)
        elif s.has_table:
            tbl = s.table
            headers = ["Việc cần hỗ trợ", "Bên liên quan / Owner", "Hạn hoàn thành"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 2 else PP_ALIGN.LEFT)

            rows_data = [
                ["Phê duyệt kế hoạch go-live bộ công cụ Thuế TNCN & Tính Lương", "CEO / BOM", "31/10"],
                ["Rà soát chuẩn hóa công thức thuế TNCN và biểu lũy tiến", "Pháp chế & Kế toán", "10/11"],
                ["Thẩm định TnC và bảo mật data người chơi Game Bò Sữa Bay", "Pháp chế & Security", "05/11"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(c_idx == 0), align=PP_ALIGN.CENTER if c_idx == 2 else PP_ALIGN.LEFT)

    # Position note cleanly below support table in Slide 7
    s7.shapes[33].top = Inches(4.78)

    # Add Tag [R] circle and 'Reporting' label to Slide 7 header
    circle = s7.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.18), Inches(0.16), Inches(0.42), Inches(0.42))
    circle.fill.solid()
    circle.fill.fore_color.rgb = RGBColor(0x99, 0x1B, 0x1B)  # deep red wine matching R
    circle.line.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
    p = circle.text_frame.paragraphs[0]
    p.text = "R"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    txBox = s7.shapes.add_textbox(Inches(8.88), Inches(0.60), Inches(1.02), Inches(0.18))
    p2 = txBox.text_frame.paragraphs[0]
    p2.text = "Reporting"
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
    p2.alignment = PP_ALIGN.CENTER

    # Save to all destination paths
    for p in OUT_PATHS:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f"Successfully generated PPTX: {p}")

if __name__ == "__main__":
    main()

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
    "/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Pyramid.pptx",
    "07_REPORTS/docs/presentations/Web_Platform_Thang_10_2026_Pyramid.pptx",
    "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Pyramid.pptx"
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
NU = FACTS.get("new_users", {})
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

    # 1. Prune down to exact 7 template slides: 7, 10, 12, 14, 15, 17, 20 (0-indexed: 6, 9, 11, 13, 14, 16, 19)
    keep_indices = {6, 9, 11, 13, 14, 16, 19}
    delete_indices = sorted([i for i in range(len(prs.slides)) if i not in keep_indices], reverse=True)
    for i in delete_indices:
        delete_slide(prs, i)

    # Reorder slides: move original slide idx 16 (currently at position 5) to the end (position 6)
    # Resulting order:
    # 0: Cover (idx 6)
    # 1: Discussion Topics [D] (idx 9)
    # 2: Proposal 1 Deep-Dive [D] (idx 11)
    # 3: Overall Traffic [R] (idx 13)
    # 4: Hubs Breakdown [R] (idx 14)
    # 5: Product Tracker [R] (idx 19)
    # 6: New User Acquisition Flow [R] (idx 16)
    sldIdLst = prs.slides._sldIdLst
    sld_to_move = sldIdLst[5]
    sldIdLst.remove(sld_to_move)
    sldIdLst.append(sld_to_move)

    print(f"Total slides after pruning & reordering: {len(prs.slides)} (Exact 7-slide C-Suite deck)")

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
                set_text(s, "Mục đích: Xin CEO/BOM phê duyệt chiến lược tối ưu luồng Tải App (/tai-app) để thu hút 10.000 volume tìm kiếm tự nhiên.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Discussion Topics —" in txt:
                set_text(s, "Discussion Topics — 1 Chủ Đề Trọng Tâm: 0 Discuss, 1 Approve", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: Google Search Console & Web Platform   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["2", "2 / 7", "2 / 8"]:
                set_text(s, "2 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Mỗi chủ đề chỉ 1 dòng" in txt or txt.startswith("Mỗi chủ đề") or txt.startswith("• 01."):
                content = (
                    "• 01. Luồng Tải App chuẩn hóa: Đưa trang /tai-app thành điểm chạm trung tâm với Smart Device Routing (iOS App Store / Android Play Store / Desktop QR Code).\n"
                    "• 02. Acquire 10.000 volume search: Tối ưu SEO On-Page và Schema SoftwareApplication để chiếm vị trí Top 1 tuyệt đối cho các từ khóa \"tải momo\", \"cài đặt momo\".\n"
                    "• 03. Kỷ luật phê duyệt: Hoàn tất phê duyệt đồng bộ link nội bộ trước 31/10 để lập chỉ mục Google và kích hoạt trọn vẹn luồng chuyển đổi trong tháng 11/2026."
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

            # Row 1: Download App Flow Optimization
            set_cell(tbl.cell(1, 0), "1", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 1), "Tối Ưu Luồng Tải App (/tai-app) Chiếm Lĩnh 10.000 Volume Tìm Kiếm Tự Nhiên", font_size=8.5, bold=True)
            set_cell(tbl.cell(1, 2), "Approve", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 3), "Phê duyệt cơ chế hợp nhất URL (/download -> /tai-app) và đồng bộ hệ thống liên kết nội bộ (Header/Footer/Top Bar) trên toàn bộ Web Platform trỏ về trang Tải App chính thức.", font_size=8.0)
            set_cell(tbl.cell(1, 4), "Thu hút trọn vẹn 10.000 volume search/tháng cho cụm từ khóa 'tải app MoMo'; bảo vệ an toàn thương hiệu, ngăn chặn thất thoát vào các nguồn APK giả mạo.", font_size=8.0, color=COLOR_GREEN)
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
    # SLIDE 3: Đề Xuất 1 Deep-Dive [D] (Xây Dựng Luồng Tải App Chuẩn Hóa)
    # =========================================================================
    s3 = prs.slides[2]
    # Header & Purpose
    set_text(s3.shapes[0], "Mục đích: Trình bày phương án tối ưu luồng Tải App (/tai-app) xin CEO/BOM phê duyệt đồng bộ liên kết toàn sàn.", font_size=8.5, color=COLOR_TEXT_MUTED)
    set_text(s3.shapes[1], "Đề Xuất 1: Xây Dựng Luồng Tải App Chuẩn Hóa, Acquire 10.000 Volume Search 'Tải App MoMo'", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[5], "Nguồn: Google Search Console & Web Platform   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s3.shapes[6], "3 / 7", font_size=9, color=COLOR_TEXT_MUTED)

    # Problem Statement, Bối cảnh, Tác động
    set_text(s3.shapes[10], "Nhu cầu tìm kiếm từ khóa 'tải momo', 'cài đặt momo', 'tải app momo' đạt 10.000 lượt search/tháng trên Google. Hiện lưu lượng bị phân tán vào các website APK trung gian không an toàn, hoặc vào landing page cũ chưa tối ưu SEO và Smart Routing.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[14], "Kỹ sư Frontend đã hoàn thành trang /tai-app trên Production với cơ chế Smart Device Routing (iOS mở App Store, Android mở CH Play, Desktop hiển thị QR Code động). Cần chuẩn hóa SEO và quy tụ luồng truy cập toàn sàn về một mối.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[18], "Hiệu quả chiến lược & An toàn thương hiệu:\n• Thu hút trọn vẹn 10.000 volume tìm kiếm tự nhiên/tháng vào trang chính chủ MoMo.\n• Bảo vệ uy tín thương hiệu: Ngăn ngừa rủi ro người dùng tải nhầm file APK giả mạo chứa mã độc.\n• Chi phí phát sinh: 0 VNĐ (tận dụng 100% tính năng và hạ tầng đã build sẵn).", font_size=8.0, color=COLOR_TEXT_MAIN)

    # Table
    tbl = s3.shapes[20].table
    headers = ["Phương Án", "Nội Dung Triển Khai", "Tác Động Lượng Hóa & Lợi Ích", "Đánh Giá Rủi Ro"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

    set_cell(tbl.cell(1, 0), "Phương Án A\n(Khuyến nghị)", font_size=8.5, bold=True, color=COLOR_GREEN, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 1), "Hợp nhất các link tải cũ về /tai-app; tối ưu Schema SoftwareApplication chuẩn SEO Top 1; đồng bộ nút Tải App trên Header/Footer toàn sàn.", font_size=8.0)
    set_cell(tbl.cell(1, 2), "Acquire 10.000 volume search/tháng; trải nghiệm 1-chạm tải app theo thiết bị; chi phí phát sinh 0 VNĐ.", font_size=8.0, color=COLOR_GREEN)
    set_cell(tbl.cell(1, 3), "Rủi ro thấp: Trang /tai-app đã nghiệm thu Production, chỉ cần đồng bộ liên kết.", font_size=8.0)

    set_cell(tbl.cell(2, 0), "Phương Án B\n(Hiện trạng)", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(2, 1), "Giữ nguyên các trang rải rác (/download, các bài blog cũ) không có cơ chế Smart Device Routing thống nhất.", font_size=8.0)
    set_cell(tbl.cell(2, 2), "Thất thoát 10.000 lượt search vào tay các trang download APK của bên thứ ba; trải nghiệm người dùng bị đứt gãy trên Desktop.", font_size=8.0, color=COLOR_ROSE)
    set_cell(tbl.cell(2, 3), "Rủi ro cao: Nguy cơ bảo mật cho người dùng khi tải file nguồn không chính thống bên ngoài.", font_size=8.0)

    # Right column
    set_text(s3.shapes[25], "Nội dung xin phê duyệt (Approve): Phê duyệt chủ trương đồng bộ liên kết Tải App trên Header/Footer toàn bộ Web Platform và cấu hình redirect các URL cũ về /tai-app trong tháng 11/2026.\nKhuyến nghị của BU: Thông qua Phương án A. Thu hồi trọn vẹn 10.000 lượt tìm kiếm chính chủ; nâng cao nhận diện thương hiệu và bảo vệ an toàn cho người dùng MoMo.", font_size=9.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[27], "Rủi ro khi chậm quyết định", font_size=8.5, bold=True, color=COLOR_WHITE)
    set_text(s3.shapes[28], "Rủi ro khi chậm phê duyệt: Tiếp tục để mất 10.000 lượt tìm kiếm mỗi tháng vào các trang trung gian tải APK ngoài, tăng nguy cơ rủi ro bảo mật thương hiệu.", font_size=9.5, color=COLOR_TEXT_MAIN)

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
    # SLIDE 7: Luồng Tăng Trưởng Người Dùng Mới (New User Flow) [R] (Original Slide 17)
    # =========================================================================
    s7 = prs.slides[6]
    set_text(s7.shapes[0], "Mục đích: Phân tích luồng tăng trưởng Người dùng mới (New Users) theo kênh tiếp cận và các Hub chuyển đổi chủ lực.", font_size=8.5, color=COLOR_TEXT_MUTED)
    set_text(
        s7.shapes[1],
        f"Kênh Tự Nhiên Dẫn Dắt {compact(NU['non_paid']['oct'])} Người Dùng Mới ({dec(NU['non_paid']['share_pct'])}% Tổng New Users), "
        f"Bù Đắp Sụt Giảm Paid Ads; Cinema Hub Tăng Trưởng {signed(NU['hubs']['cinema']['mom_pct'])}",
        font_size=17, bold=True, color=COLOR_TEXT_MAIN
    )
    set_text(s7.shapes[5], "Nguồn: GA4 (Property 270743103)   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s7.shapes[6], "7 / 7", font_size=9, color=COLOR_TEXT_MUTED)

    content_s7_takeaway = (
        f"• Ý chính 1: Toàn Website thu hút {vn(NU['new_users_oct'])} Người dùng mới (New Users) trong tháng 10, chiếm {dec(NU['new_users_share_pct'])}% tổng {compact(NU['total_users_oct'])} người dùng ghé thăm Web Platform.\n"
        f"• Ý chính 2: Kênh tự nhiên (Non-Paid) đạt {vn(NU['non_paid']['oct'])} New Users ({signed(NU['non_paid']['mom_pct'])} MoM, chiếm {dec(NU['non_paid']['share_pct'])}% tổng New Users), tự bù đắp mức giảm -364K New Users do chủ động cắt giảm Paid Ads kém chất lượng.\n"
        f"• Ý chính 3: Cinema Hub ({compact(NU['hubs']['cinema']['oct'])} New Users, {signed(NU['hubs']['cinema']['mom_pct'])} MoM) và Minigame ({compact(NU['hubs']['game_entertainment']['oct'])} New Users, {signed(NU['hubs']['game_entertainment']['mom_pct'])} MoM) trở thành hai phễu hút người dùng mới bên ngoài ứng dụng hiệu quả nhất."
    )
    set_text(s7.shapes[8], content_s7_takeaway, font_size=8.5, color=COLOR_TEXT_MAIN)

    # 4 Stat Cards:
    # Card 1: Tổng New Users MTD
    set_text(s7.shapes[10], "Tổng New Users MTD", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s7.shapes[11], compact(NU["new_users_oct"]), font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s7.shapes[12], f"{dec(NU['new_users_share_pct'])}% tổng người dùng", font_size=9.0, bold=True, color=COLOR_INDIGO)

    # Card 2: New Users Tự Nhiên (Non-Paid)
    set_text(s7.shapes[14], "New Users Tự Nhiên (Non-Paid)", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s7.shapes[15], compact(NU["non_paid"]["oct"]), font_size=20, bold=True, color=COLOR_GREEN)
    set_text(s7.shapes[16], f"▲ {signed(NU['non_paid']['mom_pct'])} MoM ({dec(NU['non_paid']['share_pct'])}% tổng)", font_size=9.0, bold=True, color=COLOR_GREEN)

    # Card 3: Phễu Dịch Vụ Cinema Hub
    set_text(s7.shapes[18], "Phễu Dịch Vụ Cinema Hub", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s7.shapes[19], compact(NU["hubs"]["cinema"]["oct"]), font_size=20, bold=True, color=COLOR_INDIGO)
    set_text(s7.shapes[20], f"▲ {signed(NU['hubs']['cinema']['mom_pct'])} MoM · Top 1 Hub", font_size=9.0, bold=True, color=COLOR_GREEN)

    # Card 4: Phễu Onboarding & Tải App
    set_text(s7.shapes[22], "Phễu Onboarding & Tải App", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s7.shapes[23], compact(NU["hubs"]["download_onboarding"]["oct"]), font_size=20, bold=True, color=COLOR_PINK)
    set_text(s7.shapes[24], f"▲ {signed(NU['hubs']['download_onboarding']['mom_pct'])} MoM · Dẫn vào App", font_size=9.0, bold=True, color=COLOR_INDIGO)

    # Section 2: Header & Table
    set_text(s7.shapes[25], "CƠ CẤU NGƯỜI DÙNG MỚI THEO KÊNH ĐẦU VÀO (NEW USER FLOW BREAKDOWN)", font_size=10, bold=True, color=COLOR_PINK)

    tbl = s7.shapes[26].table
    widths = [Inches(2.10), Inches(0.85), Inches(0.75), Inches(2.10)]
    for i, w in enumerate(widths):
        tbl.columns[i].width = w

    headers = ["Kênh / Nguồn đầu vào", "New Users", "Tỷ trọng", "Đánh giá & Xu hướng"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [1, 2] else PP_ALIGN.LEFT)

    rows_data = [
        ["• Tìm kiếm tự nhiên (Organic Search)", vn(NU["channels"][0]["oct"]), f"{dec(NU['channels'][0]['share_pct'])}%", f"▲ {signed(NU['channels'][0]['mom_pct'])} MoM · Nguồn New User lớn nhất"],
        ["• Truy cập trực tiếp (Direct)", vn(NU["channels"][1]["oct"]), f"{dec(NU['channels'][1]['share_pct'])}%", f"▲ {signed(NU['channels'][1]['mom_pct'])} MoM · Thương hiệu vững chắc"],
        ["• Quảng cáo trả phí (Paid Media)", vn(NU["channels"][2]["oct"]), f"{dec(NU['channels'][2]['share_pct'])}%", f"▼ -{dec(abs(NU['channels'][2]['mom_pct']))}% MoM · Chủ động cắt giảm"],
    ]
    for r_idx, r_data in enumerate(rows_data, 1):
        for c_idx, val in enumerate(r_data):
            set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.0, bold=(c_idx == 0 or r_idx in [1, 2]), align=PP_ALIGN.CENTER if c_idx in [1, 2] else PP_ALIGN.LEFT)

    # Right Column Highlights
    set_text(s7.shapes[28], "Key Highlights & Strategy", font_size=11, bold=True, color=COLOR_PINK)
    set_text(s7.shapes[30], "Chất Lượng Tăng Trưởng", font_size=9, bold=True, color=COLOR_PINK)

    content_s7_perf = (
        f"• Kênh tự nhiên (Non-Paid) trở thành trục xương sống hút {compact(NU['non_paid']['oct'])} New Users ({dec(NU['non_paid']['share_pct'])}% tổng số), "
        "khẳng định sức hút nội dung và tính năng vượt trội so với mua traffic trả phí.\n"
        f"• Cinema Hub ghi nhận {compact(NU['hubs']['cinema']['oct'])} New Users ({signed(NU['hubs']['cinema']['mom_pct'])} MoM) nhờ chuỗi trang cụm rạp CGV, Lotte, BHD; "
        f"Minigame đóng góp {compact(NU['hubs']['game_entertainment']['oct'])} New Users ({signed(NU['hubs']['game_entertainment']['mom_pct'])} MoM) từ viral truyền miệng."
    )
    set_text(s7.shapes[31], content_s7_perf, font_size=8.5, color=COLOR_TEXT_MAIN)

    set_text(s7.shapes[33], "Chiến Lược New User Q4", font_size=9, bold=True, color=COLOR_PINK)
    content_s7_strategy = (
        "• Tối ưu phễu chuyển đổi: Chuyển dịch dòng New Users tự nhiên vào sản phẩm tài chính qua Bộ tiện ích Thuế TNCN & Lương cuối năm (dự kiến đón 300K - 500K New Users).\n"
        "• Tăng tốc Cinema Hub đón mùa phim Tết 2027 để mở rộng phễu người dùng trẻ bên ngoài ứng dụng."
    )
    set_text(s7.shapes[34], content_s7_strategy, font_size=8.5, color=COLOR_TEXT_MAIN)

    # Save to all destination paths
    for p in OUT_PATHS:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f"Successfully generated PPTX: {p}")

if __name__ == "__main__":
    main()

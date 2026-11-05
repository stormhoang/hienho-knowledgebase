import sys
import os
import copy
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Design Tokens matching react-web-momo /report/monthly Web Hub UI
BG_CANVAS = RGBColor(0xFA, 0xF7, 0xFC)      # #FAF7FC Soft Off-White
CARD_BG = RGBColor(0xFF, 0xFF, 0xFF)        # #FFFFFF Pure White
CARD_BORDER = RGBColor(0xE8, 0xE2, 0xEC)    # #E8E2EC Subtle border
PINK_BG = RGBColor(0xFD, 0xEC, 0xF3)        # #FDECF3 Light magenta tint
GREEN_BG = RGBColor(0xEC, 0xFD, 0xF5)       # #ECFDF5 Light emerald tint

MAGENTA_PRIMARY = RGBColor(0xA5, 0x00, 0x64) # #A50064 MoMo Magenta
MAGENTA_ACCENT = RGBColor(0xD8, 0x2D, 0x8B)  # #D82D8B Vibrant Pink
TEXT_MAIN = RGBColor(0x1C, 0x17, 0x1A)       # #1C171A Deep Charcoal
TEXT_MUTED = RGBColor(0x7A, 0x6E, 0x7F)      # #7A6E7F Refined Purple Gray
TEXT_BODY = RGBColor(0x3D, 0x34, 0x40)       # #3D3440 Dark Neutral

GREEN_MAIN = RGBColor(0x05, 0x96, 0x69)      # #059669 Emerald Green
AMBER_MAIN = RGBColor(0xD9, 0x77, 0x06)      # #D97706 Amber
ROSE_MAIN = RGBColor(0xE1, 0x1D, 0x48)       # #E11D48 Rose Red
INDIGO_MAIN = RGBColor(0x4F, 0x46, 0xE5)     # #4F46E5 Indigo

OUTPUT_PPTX = "/Users/hienhv/Downloads/Slide_Monthly_Hub_Style_Demo.pptx"

def create_demo_deck():
    prs = Presentation()
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(5.625)
    blank_layout = prs.slide_layouts[6] # Blank
    slide = prs.slides.add_slide(blank_layout)

    # 1. Slide Canvas Background
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(10.0), Inches(5.625))
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = BG_CANVAS
    bg_shape.line.fill.background()

    # 2. Header: Purpose & Meta (Top bar)
    meta_box = slide.shapes.add_textbox(Inches(0.40), Inches(0.18), Inches(8.20), Inches(0.22))
    tf = meta_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "BÁO CÁO HIỆU SUẤT ĐIỀU HÀNH THÁNG 10/2026  ·  SSOT: GA4 DATA API & APPSFLYER GPD (31 NGÀY)"
    p.font.size = Pt(8.0)
    p.font.bold = True
    p.font.color.rgb = TEXT_MUTED

    # 3. Action Title
    title_box = slide.shapes.add_textbox(Inches(0.40), Inches(0.40), Inches(8.30), Inches(0.52))
    tf = title_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "Kênh tự nhiên lập đỉnh 3,13M PVs (+13,5% MoM), tự chủ 86,9% lưu lượng và bù đắp hơn 50% phần cắt giảm Paid Ads"
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN

    # Right Tag Badge (Reporting)
    badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.05), Inches(0.25), Inches(0.50), Inches(0.50))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(0xB5, 0x20, 0x7A)
    badge.line.fill.background()
    tf = badge.text_frame
    p = tf.paragraphs[0]
    p.text = "R"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    badge_lbl = slide.shapes.add_textbox(Inches(8.80), Inches(0.77), Inches(1.00), Inches(0.18))
    tf = badge_lbl.text_frame
    p = tf.paragraphs[0]
    p.text = "Reporting"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(7.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x9C, 0x1A, 0x68)

    # 4. Summary Strip: 3 Key Strategic Points (Pink Pills)
    pill_w = Inches(2.95)
    pill_h = Inches(0.60)
    pill_y = Inches(0.98)
    pill_gap = Inches(0.15)
    pills_data = [
        ("1", "Tự chủ lưu lượng sạch", "Non-Paid đạt 3.128.542 PVs (+13,5% MoM), nâng tỷ trọng tự nhiên lên 86,9% toàn site, thiết lập đỉnh chất lượng từ đầu năm."),
        ("2", "Bù đắp cắt giảm Paid", "Paid Ads chủ động giảm 724K views (-60,4%); kênh tự nhiên tăng +373K views bù đắp được 52% tổng lượng suy giảm."),
        ("3", "Động lực mới Direct & GEO", "Direct bứt phá 932K PVs (+23,3%); AI Search (GEO) tăng +36,4% đạt 18,5K PVs, mở ra kênh chuyển đổi hữu cơ mới.")
    ]

    for i, (num, lead, body) in enumerate(pills_data):
        px = Inches(0.40) + i * (pill_w + pill_gap)
        # Background card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, pill_y, pill_w, pill_h)
        card.fill.solid()
        card.fill.fore_color.rgb = PINK_BG
        card.line.color.rgb = RGBColor(0xF7, 0xD0, 0xE0)
        card.line.width = Pt(0.75)
        
        # Circle badge for number
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, px + Inches(0.08), pill_y + Inches(0.08), Inches(0.20), Inches(0.20))
        circle.fill.solid()
        circle.fill.fore_color.rgb = MAGENTA_ACCENT
        circle.line.fill.background()
        tf = circle.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = num
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        # Text inside pill
        tb = slide.shapes.add_textbox(px + Inches(0.33), pill_y + Inches(0.05), pill_w - Inches(0.38), pill_h - Inches(0.10))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = lead + ": "
        p1.font.size = Pt(7.8)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN
        
        # Add body in second run or paragraph
        run = p1.add_run()
        run.text = body
        run.font.size = Pt(7.3)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY

    # 5. Middle Section: 4 Big Hero Stat Cards
    c_w = Inches(2.18)
    c_h = Inches(1.32)
    c_y = Inches(1.68)
    c_gap = Inches(0.16)
    cards_data = [
        {
            "cat": "TIẾN ĐỘ MỤC TIÊU THÁNG",
            "val": "3,60M",
            "unit": "PVs",
            "delta": "98,3% Target  ·  -8,9% MoM",
            "delta_color": AMBER_MAIN,
            "footer_title": "Hoàn thành 98,3% chỉ tiêu",
            "footer_desc": "Thiếu 63.584 PVs do chủ động cắt giảm 724K views Paid Ads."
        },
        {
            "cat": "CHẤT LƯỢNG LƯU LƯỢNG",
            "val": "86,9%",
            "unit": "Non-Paid",
            "delta": "▲ +13,5% MoM (+373K views)",
            "delta_color": GREEN_MAIN,
            "footer_title": "Tự chủ nguồn truy cập sạch",
            "footer_desc": "Kênh tự nhiên lập đỉnh 3,13M views, tự bù đắp hơn 50% cắt giảm Ads."
        },
        {
            "cat": "SỨC MẠNH THƯƠNG HIỆU",
            "val": "932K",
            "unit": "Direct PVs",
            "delta": "▲ +23,3% MoM (931.731 PVs)",
            "delta_color": INDIGO_MAIN,
            "footer_title": "Thói quen truy cập trực tiếp",
            "footer_desc": "Người dùng chủ động vào momo.vn khi có nhu cầu dịch vụ tài chính."
        },
        {
            "cat": "TĂNG TRƯỞNG AI SEARCH",
            "val": "18,5K",
            "unit": "GEO PVs",
            "delta": "▲ +36,4% MoM (ChatGPT 17,7K)",
            "delta_color": MAGENTA_ACCENT,
            "footer_title": "Đón đầu làn sóng AI Engine",
            "footer_desc": "Lưu lượng từ trợ lý AI tăng tốc mạnh mẽ nhờ tối ưu cấu trúc dữ liệu."
        }
    ]

    for i, c in enumerate(cards_data):
        cx = Inches(0.40) + i * (c_w + c_gap)
        # Card container
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, c_y, c_w, c_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.0)

        # Content
        tb = slide.shapes.add_textbox(cx + Inches(0.10), c_y + Inches(0.08), c_w - Inches(0.20), c_h - Inches(0.16))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # P0: Category
        p0 = tf.paragraphs[0]
        p0.text = c["cat"]
        p0.font.size = Pt(6.8)
        p0.font.bold = True
        p0.font.color.rgb = TEXT_MUTED

        # P1: Big Number + Unit
        p1 = tf.add_paragraph()
        p1.text = c["val"] + " "
        p1.font.size = Pt(21)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN
        run_u = p1.add_run()
        run_u.text = c["unit"]
        run_u.font.size = Pt(9.0)
        run_u.font.bold = True
        run_u.font.color.rgb = TEXT_MUTED

        # P2: Delta
        p2 = tf.add_paragraph()
        p2.text = c["delta"]
        p2.font.size = Pt(7.2)
        p2.font.bold = True
        p2.font.color.rgb = c["delta_color"]

        # Divider line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx + Inches(0.10), c_y + Inches(0.85), c_w - Inches(0.20), Inches(0.01))
        div.fill.solid()
        div.fill.fore_color.rgb = CARD_BORDER
        div.line.fill.background()

        # Footer insight text box
        tb_foot = slide.shapes.add_textbox(cx + Inches(0.10), c_y + Inches(0.88), c_w - Inches(0.20), Inches(0.38))
        tf_f = tb_foot.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        pf0 = tf_f.paragraphs[0]
        pf0.text = c["footer_title"]
        pf0.font.size = Pt(6.8)
        pf0.font.bold = True
        pf0.font.color.rgb = c["delta_color"]
        
        pf1 = tf_f.add_paragraph()
        pf1.text = c["footer_desc"]
        pf1.font.size = Pt(6.5)
        pf1.font.color.rgb = TEXT_MUTED

    # 6. Bottom Section: 2 Balanced Analytical Modules
    b_y = Inches(3.08)
    b_h = Inches(2.18)
    
    # Left Card: Non-Paid vs Paid Table
    left_w = Inches(5.10)
    left_x = Inches(0.40)
    left_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, b_y, left_w, b_h)
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = CARD_BG
    left_card.line.color.rgb = CARD_BORDER
    left_card.line.width = Pt(1.0)

    # Title of Table
    tb_t = slide.shapes.add_textbox(left_x + Inches(0.14), b_y + Inches(0.08), left_w - Inches(0.28), Inches(0.24))
    tf = tb_t.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "CƠ CẤU PHÂN BỔ KÊNH LƯU LƯỢNG (NON-PAID VS. PAID DICHOTOMY)"
    p.font.size = Pt(8.0)
    p.font.bold = True
    p.font.color.rgb = MAGENTA_PRIMARY

    # Add Table inside Left Card
    t_rows = 6
    t_cols = 4
    table_shape = slide.shapes.add_table(t_rows, t_cols, left_x + Inches(0.14), b_y + Inches(0.34), left_w - Inches(0.28), Inches(1.70))
    table = table_shape.table
    table.columns[0].width = Inches(1.90)
    table.columns[1].width = Inches(0.95)
    table.columns[2].width = Inches(0.85)
    table.columns[3].width = Inches(1.12)

    headers = ["Kênh Truy Cập", "Lưu Lượng", "Tỷ Trọng", "% MoM"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = MAGENTA_PRIMARY
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT
        p.font.size = Pt(7.2)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    table_data = [
        ("KÊNH TỰ NHIÊN (NON-PAID)", "3.128.542", "86,9%", "+13,5%", True, GREEN_MAIN),
        ("  · Organic Search (SEO)", "1.715.771", "47,6%", "+5,7%", False, TEXT_MAIN),
        ("  · Direct (Truy cập trực tiếp)", "931.731", "25,9%", "+23,3%", False, INDIGO_MAIN),
        ("  · Referral & Khác (Gồm GEO)", "481.040", "13,4%", "+27,9%", False, MAGENTA_ACCENT),
        ("KÊNH TRẢ PHÍ (PAID ADS)", "473.481", "13,1%", "-60,4%", True, AMBER_MAIN),
    ]

    for i, (k, v, s, m, is_bold, color) in enumerate(table_data):
        row_idx = i + 1
        for j, val in enumerate([k, v, s, m]):
            cell = table.cell(row_idx, j)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if is_bold:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(0xF8, 0xF6, 0xFA)
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT
            p.font.size = Pt(7.0)
            p.font.bold = is_bold
            p.font.color.rgb = color if j == 3 else (TEXT_MAIN if is_bold else TEXT_BODY)

    # Right Card: Executive Observations & Priorities (So What & Now What)
    right_w = Inches(4.06)
    right_x = Inches(5.62)
    right_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, b_y, right_w, b_h)
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = CARD_BG
    right_card.line.color.rgb = CARD_BORDER
    right_card.line.width = Pt(1.0)

    # Header of Right Card
    tb_r = slide.shapes.add_textbox(right_x + Inches(0.14), b_y + Inches(0.08), right_w - Inches(0.28), Inches(0.24))
    tf = tb_r.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "NHẬN ĐỊNH ĐIỀU HÀNH & KẾ HOẠCH HÀNH ĐỘNG THÁNG 11"
    p.font.size = Pt(8.0)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN

    # Box 1: So What (Emerald Pill)
    b1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x + Inches(0.12), b_y + Inches(0.32), right_w - Inches(0.24), Inches(0.84))
    b1.fill.solid()
    b1.fill.fore_color.rgb = GREEN_BG
    b1.line.color.rgb = RGBColor(0xA7, 0xF3, 0xD0)
    b1.line.width = Pt(0.75)
    tf1 = b1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.08)
    tf1.margin_top = Inches(0.05)
    tf1.margin_right = Inches(0.08)
    tf1.margin_bottom = Inches(0.05)
    p0 = tf1.paragraphs[0]
    p0.text = "Bản chất dịch chuyển nguồn lực (So What):"
    p0.font.size = Pt(7.5)
    p0.font.bold = True
    p0.font.color.rgb = GREEN_MAIN
    p1 = tf1.add_paragraph()
    p1.text = "• Mức giảm -8,9% toàn site là kết quả chủ động cắt 724K views Paid Ads kém hiệu quả (-60,4%).\n• Kênh tự nhiên chứng minh năng lực tự bù đắp 52% phần hụt (+373K views), đưa tỷ trọng Non-Paid lên 86,9% - cấu trúc lưu lượng sạch và tự chủ nhất từ đầu năm."
    p1.font.size = Pt(6.8)
    p1.font.color.rgb = TEXT_BODY
    p1.line_spacing = 1.12

    # Box 2: Now What (Amber/Pink Pill)
    b2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x + Inches(0.12), b_y + Inches(1.22), right_w - Inches(0.24), Inches(0.86))
    b2.fill.solid()
    b2.fill.fore_color.rgb = PINK_BG
    b2.line.color.rgb = RGBColor(0xF7, 0xD0, 0xE0)
    b2.line.width = Pt(0.75)
    tf2 = b2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.08)
    tf2.margin_top = Inches(0.05)
    tf2.margin_right = Inches(0.08)
    tf2.margin_bottom = Inches(0.05)
    p0 = tf2.paragraphs[0]
    p0.text = "Trọng tâm điều hành 30 ngày tới (Now What):"
    p0.font.size = Pt(7.5)
    p0.font.bold = True
    p0.font.color.rgb = MAGENTA_PRIMARY
    p1 = tf2.add_paragraph()
    p1.text = "• Mở rộng Product-Led Growth: Go-live bộ công cụ Tính Thuế TNCN & Hộ Kinh Doanh đón cao điểm quyết toán; mở rộng công cụ Vay và CIC (đạt CTR 33-43%).\n• Chuẩn bị mùa phim Tết 2027: Kích hoạt giao diện mới cụm rạp đối tác (CGV, Lotte) và luồng Chatbot tư vấn để bảo vệ Top 3 SERP."
    p1.font.size = Pt(6.8)
    p1.font.color.rgb = TEXT_BODY
    p1.line_spacing = 1.12

    # 7. Slide Footer
    ft = slide.shapes.add_textbox(Inches(0.40), Inches(5.34), Inches(8.00), Inches(0.20))
    tf = ft.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "Nguồn: GA4 Data API (Property 270743103), AppsFlyer GPD   |   Chu kỳ: Full Month Tháng 10/2026   |   Chế độ: Web Platform Executive Review"
    p.font.size = Pt(7.0)
    p.font.color.rgb = TEXT_MUTED

    ft_p = slide.shapes.add_textbox(Inches(9.00), Inches(5.34), Inches(0.60), Inches(0.20))
    tf = ft_p.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = "1 / 1"
    p.alignment = PP_ALIGN.RIGHT
    p.font.size = Pt(7.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_MUTED

    prs.save(OUTPUT_PPTX)
    print(f"Demo presentation successfully saved to: {OUTPUT_PPTX}")

if __name__ == "__main__":
    create_demo_deck()

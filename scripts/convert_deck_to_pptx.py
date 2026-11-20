#!/usr/bin/env python3
"""
Convert Website 2031 Research Deck (HTML) to PowerPoint (PPTX)
Strictly adheres to:
- No En Dash / No Em Dash (converts to standard hyphen '-')
- No priority ranking tags (P-tags)
- Paper & Ink editorial minimalist aesthetic (Georgia serif typography)
- 16:9 widescreen layout (13.333 x 7.5 inches)
"""

import os
import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# COLOR PALETTE (Paper & Ink Editorial Minimalist)
# ==============================================================================
# Light Theme
BG_LIGHT = RGBColor(250, 249, 246)          # #faf9f6
TEXT_PRIMARY_LIGHT = RGBColor(28, 26, 23)   # #1c1a17
TEXT_SECONDARY_LIGHT = RGBColor(107, 102, 92) # #6b665c
TEXT_FAINT_LIGHT = RGBColor(163, 157, 146)  # #a39d92
ACCENT = RGBColor(179, 53, 44)               # #b3352c (Editorial Crimson)
ACCENT_SOFT = RGBColor(243, 227, 224)       # #f3e3e0
RULE_LIGHT = RGBColor(217, 212, 200)        # #d9d4c8
CARD_BG_LIGHT = RGBColor(243, 241, 236)     # #f3f1ec
CARD_BORDER_LIGHT = RGBColor(220, 216, 207) # #dcd8cf

# Dark Theme
BG_DARK = RGBColor(28, 26, 23)              # #1c1a17
TEXT_PRIMARY_DARK = RGBColor(245, 242, 236) # #f5f2ec
TEXT_SECONDARY_DARK = RGBColor(184, 178, 166) # #b8b2a6
TEXT_FAINT_DARK = RGBColor(122, 116, 104)   # #7a7468
ACCENT_DARK = RGBColor(217, 141, 132)       # #d98d84
RULE_DARK = RGBColor(58, 54, 47)            # #3a362f
CARD_BG_DARK = RGBColor(35, 32, 28)         # #23201c
CARD_BORDER_DARK = RGBColor(65, 60, 52)     # #413c34

# Fonts
FONT_DISPLAY = 'Georgia'
FONT_BODY = 'Georgia'

def clean_text(text: str) -> str:
    """Sanitize text: enforce NO EN DASH and NO EM DASH per workspace rules."""
    if not text:
        return ""
    # Replace en dash (\u2013) and em dash (\u2014) with hyphen '-'
    t = text.replace('\u2013', '-').replace('\u2014', '-')
    # Replace non-breaking space
    t = t.replace('\xa0', ' ')
    # Normalize excessive spaces
    t = re.sub(r'[ \t]+', ' ', t)
    return t.strip()

def init_presentation() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def create_base_slide(prs: Presentation, is_dark: bool = False):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    
    # Set slide background
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BG_DARK if is_dark else BG_LIGHT
    
    # Add full bleed background rectangle to guarantee cross-viewer rendering
    bg_rect = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5)
    )
    bg_rect.fill.solid()
    bg_rect.fill.fore_color.rgb = BG_DARK if is_dark else BG_LIGHT
    bg_rect.line.fill.background()
    
    return slide

def add_footer(slide, is_dark: bool, foot_left: str, foot_right: str):
    foot_left = clean_text(foot_left)
    foot_right = clean_text(foot_right)
    rule_color = RULE_DARK if is_dark else RULE_LIGHT
    text_color = TEXT_FAINT_DARK if is_dark else TEXT_FAINT_LIGHT
    
    # Footer hairline rule
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.92), Inches(11.733), Pt(0.75)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = rule_color
    line.line.fill.background()
    
    # Footer left text
    tx_left = slide.shapes.add_textbox(Inches(0.8), Inches(6.98), Inches(9.0), Inches(0.35))
    tf_l = tx_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    p_l = tf_l.paragraphs[0]
    p_l.text = foot_left
    p_l.font.name = FONT_BODY
    p_l.font.size = Pt(9)
    p_l.font.color.rgb = text_color
    
    # Footer right text (page number)
    tx_right = slide.shapes.add_textbox(Inches(10.5), Inches(6.98), Inches(2.033), Inches(0.35))
    tf_r = tx_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0
    p_r = tf_r.paragraphs[0]
    p_r.alignment = PP_ALIGN.RIGHT
    p_r.text = foot_right
    p_r.font.name = FONT_BODY
    p_r.font.size = Pt(9)
    p_r.font.color.rgb = text_color

def add_header(slide, is_dark: bool, kicker: str, title: str, meta_num: str = None, meta_tag: str = None):
    kicker = clean_text(kicker)
    title = clean_text(title)
    meta_num = clean_text(meta_num) if meta_num else ""
    meta_tag = clean_text(meta_tag) if meta_tag else ""
    
    accent_color = ACCENT_DARK if is_dark else ACCENT
    primary_color = TEXT_PRIMARY_DARK if is_dark else TEXT_PRIMARY_LIGHT
    faint_color = TEXT_FAINT_DARK if is_dark else TEXT_FAINT_LIGHT
    
    top_pos = Inches(0.46)
    
    if kicker:
        tx_k = slide.shapes.add_textbox(Inches(0.8), top_pos, Inches(11.733), Inches(0.25))
        tf_k = tx_k.text_frame
        tf_k.word_wrap = True
        tf_k.margin_left = tf_k.margin_top = tf_k.margin_right = tf_k.margin_bottom = 0
        p_k = tf_k.paragraphs[0]
        p_k.text = kicker.upper()
        p_k.font.name = FONT_DISPLAY
        p_k.font.size = Pt(9.5)
        p_k.font.bold = True
        p_k.font.color.rgb = accent_color
        top_pos += Inches(0.24)
        
    tx_t = slide.shapes.add_textbox(Inches(0.8), top_pos, Inches(11.733), Inches(0.58))
    tf_t = tx_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_DISPLAY
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = primary_color
    top_pos += Inches(0.56)
    
    if meta_num or meta_tag:
        tx_m = slide.shapes.add_textbox(Inches(0.8), top_pos, Inches(11.733), Inches(0.24))
        tf_m = tx_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        p_m = tf_m.paragraphs[0]
        
        if meta_num:
            r1 = p_m.add_run()
            r1.text = meta_num + ("   " if meta_tag else "")
            r1.font.name = FONT_DISPLAY
            r1.font.italic = True
            r1.font.size = Pt(10.5)
            r1.font.color.rgb = faint_color
            
        if meta_tag:
            r2 = p_m.add_run()
            r2.text = f"[{meta_tag}]"
            r2.font.name = FONT_BODY
            r2.font.bold = True
            r2.font.size = Pt(9.5)
            r2.font.color.rgb = accent_color
            
        top_pos += Inches(0.25)
        
    return top_pos + Inches(0.06)

def add_card(slide, is_dark: bool, left, top, width, height, title: str = "", body: str = "", 
             kicker: str = "", top_accent: bool = False, hot: bool = False, 
             title_size: int = 12, body_size: int = 10, bg_fill: bool = True):
    title = clean_text(title)
    body = clean_text(body)
    kicker = clean_text(kicker)
    
    primary_color = TEXT_PRIMARY_DARK if is_dark else TEXT_PRIMARY_LIGHT
    secondary_color = TEXT_SECONDARY_DARK if is_dark else TEXT_SECONDARY_LIGHT
    accent_color = ACCENT_DARK if is_dark else ACCENT
    card_bg = CARD_BG_DARK if is_dark else CARD_BG_LIGHT
    card_border = CARD_BORDER_DARK if is_dark else CARD_BORDER_LIGHT
    
    # Outer card box
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    rect.fill.solid()
    if bg_fill:
        rect.fill.fore_color.rgb = card_bg
    else:
        rect.fill.background()
    
    rect.line.color.rgb = accent_color if hot else card_border
    rect.line.width = Pt(1.5 if hot else 0.75)
    
    # Top accent line
    if top_accent:
        tline = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Pt(2.5))
        tline.fill.solid()
        tline.fill.fore_color.rgb = accent_color
        tline.line.fill.background()
        
    # Text container
    pad_h = Inches(0.18)
    pad_v = Inches(0.14)
    tx = slide.shapes.add_textbox(left + pad_h, top + pad_v, width - (pad_h * 2), height - (pad_v * 2))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    first = True
    if kicker:
        p_k = tf.paragraphs[0]
        p_k.text = kicker.upper()
        p_k.font.name = FONT_DISPLAY
        p_k.font.size = Pt(8.5)
        p_k.font.bold = True
        p_k.font.color.rgb = accent_color
        p_k.space_after = Pt(2)
        first = False
        
    if title:
        p_t = tf.paragraphs[0] if first else tf.add_paragraph()
        p_t.text = title
        p_t.font.name = FONT_DISPLAY
        p_t.font.size = Pt(title_size)
        p_t.font.bold = True
        p_t.font.color.rgb = primary_color
        p_t.space_after = Pt(4)
        first = False
        
    if body:
        p_b = tf.paragraphs[0] if first else tf.add_paragraph()
        p_b.text = body
        p_b.font.name = FONT_BODY
        p_b.font.size = Pt(body_size)
        p_b.font.color.rgb = secondary_color
        p_b.line_spacing = 1.15

def add_stat_box(slide, is_dark: bool, left, top, width, height, stat_num: str, stat_unit: str, label: str, src: str = ""):
    stat_num = clean_text(stat_num)
    stat_unit = clean_text(stat_unit)
    label = clean_text(label)
    src = clean_text(src)
    
    primary_color = TEXT_PRIMARY_DARK if is_dark else TEXT_PRIMARY_LIGHT
    secondary_color = TEXT_SECONDARY_DARK if is_dark else TEXT_SECONDARY_LIGHT
    faint_color = TEXT_FAINT_DARK if is_dark else TEXT_FAINT_LIGHT
    accent_color = ACCENT_DARK if is_dark else ACCENT
    card_bg = CARD_BG_DARK if is_dark else CARD_BG_LIGHT
    card_border = CARD_BORDER_DARK if is_dark else CARD_BORDER_LIGHT
    
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    rect.fill.solid()
    rect.fill.fore_color.rgb = card_bg
    rect.line.color.rgb = card_border
    rect.line.width = Pt(0.75)
    
    # Top accent line
    tline = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Pt(2))
    tline.fill.solid()
    tline.fill.fore_color.rgb = accent_color
    tline.line.fill.background()
    
    tx = slide.shapes.add_textbox(left + Inches(0.14), top + Inches(0.14), width - Inches(0.28), height - Inches(0.28))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    # Number + unit
    p_num = tf.paragraphs[0]
    r_num = p_num.add_run()
    r_num.text = stat_num
    r_num.font.name = FONT_DISPLAY
    r_num.font.size = Pt(36)
    r_num.font.bold = True
    r_num.font.color.rgb = primary_color
    
    if stat_unit:
        r_unit = p_num.add_run()
        r_unit.text = " " + stat_unit
        r_unit.font.name = FONT_DISPLAY
        r_unit.font.size = Pt(17)
        r_unit.font.bold = True
        r_unit.font.color.rgb = accent_color
        
    p_num.space_after = Pt(4)
    
    # Label
    p_lbl = tf.add_paragraph()
    p_lbl.text = label
    p_lbl.font.name = FONT_BODY
    p_lbl.font.size = Pt(9.5)
    p_lbl.font.color.rgb = secondary_color
    p_lbl.line_spacing = 1.15
    p_lbl.space_after = Pt(4)
    
    # Source
    if src:
        p_src = tf.add_paragraph()
        p_src.text = src
        p_src.font.name = FONT_BODY
        p_src.font.size = Pt(8.5)
        p_src.font.italic = True
        p_src.font.color.rgb = faint_color

def add_bullets_box(slide, is_dark: bool, left, top, width, height, bullets: list, kicker: str = "", title: str = ""):
    primary_color = TEXT_PRIMARY_DARK if is_dark else TEXT_PRIMARY_LIGHT
    secondary_color = TEXT_SECONDARY_DARK if is_dark else TEXT_SECONDARY_LIGHT
    accent_color = ACCENT_DARK if is_dark else ACCENT
    card_bg = CARD_BG_DARK if is_dark else CARD_BG_LIGHT
    card_border = CARD_BORDER_DARK if is_dark else CARD_BORDER_LIGHT
    
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    rect.fill.solid()
    rect.fill.fore_color.rgb = card_bg
    rect.line.color.rgb = card_border
    rect.line.width = Pt(0.75)
    
    pad_h = Inches(0.2)
    pad_v = Inches(0.16)
    tx = slide.shapes.add_textbox(left + pad_h, top + pad_v, width - (pad_h * 2), height - (pad_v * 2))
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    first = True
    if kicker:
        p_k = tf.paragraphs[0]
        p_k.text = clean_text(kicker).upper()
        p_k.font.name = FONT_DISPLAY
        p_k.font.size = Pt(8.5)
        p_k.font.bold = True
        p_k.font.color.rgb = accent_color
        p_k.space_after = Pt(2)
        first = False
        
    if title:
        p_t = tf.paragraphs[0] if first else tf.add_paragraph()
        p_t.text = clean_text(title)
        p_t.font.name = FONT_DISPLAY
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = primary_color
        p_t.space_after = Pt(4)
        first = False
        
    for item in bullets:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(4)
        p.line_spacing = 1.15
        
        # Check if item is tuple (prefix, text)
        if isinstance(item, tuple):
            prefix, txt = item
            r_pre = p.add_run()
            r_pre.text = clean_text(prefix) + " "
            r_pre.font.name = FONT_BODY
            r_pre.font.bold = True
            r_pre.font.size = Pt(9.5)
            r_pre.font.color.rgb = accent_color if is_dark else primary_color
            
            r_txt = p.add_run()
            r_txt.text = clean_text(txt)
            r_txt.font.name = FONT_BODY
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = secondary_color
        else:
            r = p.add_run()
            r.text = "- " + clean_text(item)
            r.font.name = FONT_BODY
            r.font.size = Pt(9.5)
            r.font.color.rgb = secondary_color

# ==============================================================================
# SLIDE BUILDERS (1 to 22)
# ==============================================================================

def build_slide_1(prs):
    """Slide 1: Cover Slide"""
    slide = create_base_slide(prs, is_dark=False)
    
    # Accent bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.8), Inches(1.2), Pt(3.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()
    
    # Title
    tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.733), Inches(1.3))
    tf_t = tx_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    
    r1 = p_t.add_run()
    r1.text = "Website "
    r1.font.name = FONT_DISPLAY
    r1.font.size = Pt(64)
    r1.font.bold = True
    r1.font.color.rgb = TEXT_PRIMARY_LIGHT
    
    r2 = p_t.add_run()
    r2.text = "2031"
    r2.font.name = FONT_DISPLAY
    r2.font.size = Pt(64)
    r2.font.bold = True
    r2.font.italic = True
    r2.font.color.rgb = ACCENT
    
    # Subtitle
    tx_s = slide.shapes.add_textbox(Inches(0.8), Inches(3.45), Inches(10.5), Inches(1.1))
    tf_s = tx_s.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
    p_s = tf_s.paragraphs[0]
    p_s.text = clean_text("Từ \"điểm đến để đọc\" thành lớp phân phối, xác thực và giao dịch của Internet. "
                          "Tổng hợp hai báo cáo Deep Research về trạng thái thị trường, công nghệ và vai trò mới của website giai đoạn 2026-2031.")
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(17)
    p_s.font.color.rgb = TEXT_SECONDARY_LIGHT
    p_s.line_spacing = 1.3
    
    # Hairline divider
    div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(5.1), Inches(11.733), Pt(0.75))
    div.fill.solid()
    div.fill.fore_color.rgb = RULE_LIGHT
    div.line.fill.background()
    
    # Meta columns
    meta_items = [
        ("BIÊN SOẠN", "Văn Hiến - Web Product Lead, GPD"),
        ("NGUỒN", "2 Deep Research reports - kiểm chứng đến 20/11/2026"),
        ("NGÀY", "20/11/2026")
    ]
    col_w = Inches(3.7)
    for idx, (label, val) in enumerate(meta_items):
        tx_m = slide.shapes.add_textbox(Inches(0.8 + idx * 3.9), Inches(5.3), col_w, Inches(0.9))
        tf_m = tx_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        p_l = tf_m.paragraphs[0]
        p_l.text = label
        p_l.font.name = FONT_BODY
        p_l.font.size = Pt(9.5)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_FAINT_LIGHT
        p_l.space_after = Pt(2)
        
        p_v = tf_m.add_paragraph()
        p_v.text = val
        p_v.font.name = FONT_BODY
        p_v.font.size = Pt(13)
        p_v.font.color.rgb = TEXT_PRIMARY_LIGHT
        
    add_footer(slide, is_dark=False, foot_left="WEBSITE 2031 - DEEP RESEARCH SYNTHESIS", foot_right="01 / 22")

def build_slide_2(prs):
    """Slide 2: Table of Contents"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Mục lục", title="Năm phần, một câu hỏi chiến lược")
    
    cards = [
        ("01 - Bối cảnh: pageview economy thu hẹp", 
         "Zero-click, AI answers và bot traffic đang viết lại phương trình traffic của website. Dữ liệu định lượng 2025-2026."),
        ("02 - Chuyển dịch vai trò Web 2026 → 2031", 
         "Mười dimension thay đổi: từ ranking/CTR sang retrieval eligibility, citation và actionability."),
        ("03 - Kiến trúc mới: entity + capability-first", 
         "Ba representation layers, giao thức tác nhân (WebMCP, MCP, A2A), controlled generative UI và edge compute."),
        ("04 - Trust, identity và transaction layer", 
         "WebAuthn, digital credentials, content provenance, agent identity và thanh toán gốc của Internet."),
        ("05 - Vai trò mới theo từng lĩnh vực", 
         "E-commerce, B2B SaaS, báo chí nội dung và phản trào lưu anti-slop / Small Web."),
        ("06 - Kịch bản, framework đầu tư và roadmap", 
         "Ba kịch bản 2031, sáu lớp đầu tư, agent gateway levels, roadmap 2027-2031 và hypothesis cần bác bỏ.")
    ]
    
    grid_w = Inches(5.72)
    grid_h = Inches(1.3)
    gap_x = Inches(0.29)
    gap_y = Inches(0.18)
    
    for idx, (t, b) in enumerate(cards):
        col = idx % 2
        row = idx // 2
        x = Inches(0.8) + col * (grid_w + gap_x)
        y = top_pos + row * (grid_h + gap_y)
        add_card(slide, is_dark=False, left=x, top=y, width=grid_w, height=grid_h, 
                 title=t, body=b, top_accent=True, title_size=12, body_size=10)
        
    # Bottom core question
    y_bot = top_pos + 3 * (grid_h + gap_y) + Inches(0.04)
    add_card(slide, is_dark=False, left=Inches(0.8), top=y_bot, width=Inches(11.733), height=Inches(0.68),
             title="Câu hỏi trung tâm:", 
             body="Nếu người dùng không còn \"vào website để đọc\", thì website tồn tại để làm gì cho doanh nghiệp và người dùng?",
             kicker="", top_accent=False, hot=True, title_size=11, body_size=11)
    
    add_footer(slide, is_dark=False, foot_left="WEBSITE 2031 - DEEP RESEARCH SYNTHESIS", foot_right="02 / 22")

def build_slide_3(prs):
    """Slide 3: Executive Summary (Dark)"""
    slide = create_base_slide(prs, is_dark=True)
    top_pos = add_header(slide, is_dark=True, kicker="Executive Summary", 
                         title="Website không chết - vai trò destination mới là thứ suy giảm")
    
    # Big callout lede
    add_card(slide, is_dark=True, left=Inches(0.8), top=top_pos, width=Inches(11.733), height=Inches(1.2),
             title="",
             body="Khả năng cao trong 2026-2031, website tăng giá trị như một infrastructure layer: "
                  "discovery, canonical data, trust, identity, transaction, deep-link routing và machine-to-machine interaction "
                  "- chứ không còn là \"điểm đến bắt buộc để lấy thông tin\".",
             kicker="LUẬN ĐIỂM CHỦ ĐẠO", top_accent=True, hot=True, title_size=13, body_size=12.5)
    
    y_cards = top_pos + Inches(1.36)
    c_w = Inches(3.72)
    gap = Inches(0.28)
    
    cards_data = [
        ("Câu hỏi chiến lược mới",
         "Không còn \"làm sao tăng web traffic?\" mà là: làm sao biến Web Platform thành lớp phân phối mở giúp con người, "
         "search engines, LLMs và agents cùng truy cập, trích dẫn, xác thực và thực hiện hành động?",
         "ĐỊNH HƯỚNG TƯ DUY"),
        ("Ba cấp độ chắc chắn",
         "Dữ kiện đã quan sát/chuẩn hóa · Dự báo có cơ sở suy luận từ nhiều tín hiệu · Kịch bản khả năng có điều kiện. "
         "Báo cáo phân định rành mạch ba mức này để tránh thiên lệch tương lai.",
         "KHUNG ĐÁNH GIÁ"),
        ("Bet chiến lược 2027-2031",
         "Không phải \"giữ SEO traffic bằng mọi giá\" mà là xây Web Platform thành Open Distribution Layer: nơi Search Engine, "
         "AI Answer Engine và Transaction Agent có thể khám phá, trích dẫn và kích hoạt tác vụ thực tế.",
         "HÀNH ĐỘNG CỐT LÕI")
    ]
    
    for idx, (t, b, k) in enumerate(cards_data):
        x = Inches(0.8) + idx * (c_w + gap)
        add_card(slide, is_dark=True, left=x, top=y_cards, width=c_w, height=Inches(3.4),
                 title=t, body=b, kicker=k, top_accent=True, title_size=13, body_size=10.5)
        
    add_footer(slide, is_dark=True, foot_left="EXECUTIVE SUMMARY", foot_right="03 / 22")

def build_section_slide(prs, num_str: str, title_str: str, lede_str: str, foot_left: str, foot_right: str, is_dark: bool = False):
    """Reusable section divider slide"""
    slide = create_base_slide(prs, is_dark=is_dark)
    
    faint_color = TEXT_FAINT_DARK if is_dark else TEXT_FAINT_LIGHT
    primary_color = TEXT_PRIMARY_DARK if is_dark else TEXT_PRIMARY_LIGHT
    secondary_color = TEXT_SECONDARY_DARK if is_dark else TEXT_SECONDARY_LIGHT
    
    # Section Big Number
    tx_num = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(4.0), Inches(1.6))
    tf_num = tx_num.text_frame
    tf_num.word_wrap = True
    tf_num.margin_left = tf_num.margin_top = tf_num.margin_right = tf_num.margin_bottom = 0
    p_num = tf_num.paragraphs[0]
    p_num.text = clean_text(num_str)
    p_num.font.name = FONT_DISPLAY
    p_num.font.size = Pt(96)
    p_num.font.bold = True
    p_num.font.color.rgb = faint_color
    
    # Section Title
    tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(3.2), Inches(11.5), Inches(1.0))
    tf_t = tx_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = clean_text(title_str)
    p_t.font.name = FONT_DISPLAY
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = primary_color
    
    # Section Lede
    tx_l = slide.shapes.add_textbox(Inches(0.8), Inches(4.4), Inches(10.5), Inches(1.6))
    tf_l = tx_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    p_l = tf_l.paragraphs[0]
    p_l.text = clean_text(lede_str)
    p_l.font.name = FONT_BODY
    p_l.font.size = Pt(17)
    p_l.font.color.rgb = secondary_color
    p_l.line_spacing = 1.35
    
    add_footer(slide, is_dark=is_dark, foot_left=foot_left, foot_right=foot_right)

def build_slide_5(prs):
    """Slide 5: Quantitative Evidence"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Bằng chứng định lượng", 
                         title="Answer layer đang hấp thụ nhu cầu trước khi người dùng tới website",
                         meta_num="01.1", meta_tag="Dữ kiện 2024-2026")
    
    # 4 Stat blocks
    stats = [
        ("8", "%", "Tỷ lệ click vào kết quả truyền thống khi AI summary xuất hiện - so với 15% khi không có summary",
         "Pew Research Center - 68.879 searches, 900 người dùng, 3/2025"),
        ("~1", "%", "Click trực tiếp vào nguồn bên trong AI summary",
         "Pew Research Center, cùng nghiên cứu"),
        ("58-60", "%", "Google Search kết thúc không có click ra ngoài (zero-click)",
         "Datos/SparkToro clickstream panel Mỹ + EU, 2024"),
        ("2,5", "T+", "Monthly active users của AI Overviews; AI Mode vượt 1 tỷ MAU",
         "Google công bố, giữa 2026")
    ]
    
    stat_w = Inches(2.72)
    stat_gap = Inches(0.28)
    for idx, (num, unit, lbl, src) in enumerate(stats):
        x = Inches(0.8) + idx * (stat_w + stat_gap)
        add_stat_box(slide, is_dark=False, left=x, top=top_pos, width=stat_w, height=Inches(2.55),
                     stat_num=num, stat_unit=unit, label=lbl, src=src)
        
    # 2 Mini-cards below
    y_cards = top_pos + Inches(2.72)
    card_w = Inches(5.72)
    card_gap = Inches(0.29)
    
    cards_data = [
        ("Áp lực hạ tầng từ máy móc",
         "Lưu lượng tự động vượt 57,5% tổng HTML requests (5-6/2026), 35,2% nếu tính cả traffic máy khác. "
         "Khi bot vượt người, chi phí hạ tầng web tăng trong khi doanh thu quảng cáo / click giảm. (Nguồn: Cloudflare Radar Bot Report 2026)"),
        ("AI referral vẫn nhỏ - nhưng citation thì lớn",
         "Conductor 2025 (1.215 domains): trợ lý AI đóng góp ~ 1% referral traffic. Nghịch lý: AI engines trích dẫn website liên tục "
         "để tạo câu trả lời, nhưng rất ít người click vào link trích dẫn. (Nguồn: Conductor State of AI Search 2025)")
    ]
    
    for idx, (t, b) in enumerate(cards_data):
        x = Inches(0.8) + idx * (card_w + card_gap)
        add_card(slide, is_dark=False, left=x, top=y_cards, width=card_w, height=Inches(2.1),
                 title=t, body=b, top_accent=True, title_size=12, body_size=10.5)
        
    add_footer(slide, is_dark=False, 
               foot_left="LƯU Ý: dữ liệu Pew/Datos là thị trường Mỹ-EU, không ngoại suy trực tiếp sang Việt Nam", 
               foot_right="05 / 22")

def build_slide_6(prs):
    """Slide 6: Forecast - Outcome KPI Shift"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Dự báo có cơ sở", 
                         title="KPI tối thượng dịch chuyển từ traffic sang outcome",
                         meta_num="01.2", meta_tag="Dự báo có cơ sở")
    
    # Subtitle / lede
    tx_l = slide.shapes.add_textbox(Inches(0.8), top_pos, Inches(11.733), Inches(0.52))
    tf_l = tx_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    p_l = tf_l.paragraphs[0]
    p_l.text = clean_text("Trong 5 năm tới, traffic informational có xác suất cao tiếp tục mất vị trí như KPI tối thượng. "
                          "Giá trị dịch chuyển dọc chuỗi sau - website 2031 sống hay chết phụ thuộc việc đứng ở đoạn nào:")
    p_l.font.name = FONT_BODY
    p_l.font.size = Pt(11.5)
    p_l.font.color.rgb = TEXT_SECONDARY_LIGHT
    
    # Horizontal flow funnel: 6 steps
    flow_steps = [
        ("Visibility", "Impressions, AI citations"),
        ("Citation", "Được AI engine trích dẫn"),
        ("Qualified Visit", "Visit có intent thực tế"),
        ("Action", "Dùng utility, thực hiện tác vụ"),
        ("Authenticated", "Identity verified, consent"),
        ("Transaction", "Doanh thu đo được")
    ]
    
    y_flow = top_pos + Inches(0.6)
    step_w = Inches(1.85)
    step_gap = Inches(0.12)
    
    for idx, (st_t, st_sub) in enumerate(flow_steps):
        x = Inches(0.8) + idx * (step_w + step_gap)
        # Node box
        box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y_flow, step_w, Inches(1.3))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG_LIGHT
        box.line.color.rgb = CARD_BORDER_LIGHT
        box.line.width = Pt(0.75)
        
        # Top line
        tl = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y_flow, step_w, Pt(2))
        tl.fill.solid()
        tl.fill.fore_color.rgb = ACCENT
        tl.line.fill.background()
        
        tx_box = slide.shapes.add_textbox(x + Inches(0.1), y_flow + Inches(0.12), step_w - Inches(0.2), Inches(1.05))
        tf_b = tx_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        
        para_title = tf_b.paragraphs[0]
        para_title.text = st_t
        para_title.font.name = FONT_DISPLAY
        para_title.font.size = Pt(11)
        para_title.font.bold = True
        para_title.font.color.rgb = TEXT_PRIMARY_LIGHT
        para_title.space_after = Pt(2)
        
        para_sub = tf_b.add_paragraph()
        para_sub.text = st_sub
        para_sub.font.name = FONT_BODY
        para_sub.font.size = Pt(8.5)
        para_sub.font.color.rgb = TEXT_SECONDARY_LIGHT
        
        # Right arrow between nodes
        if idx < len(flow_steps) - 1:
            arr_x = x + step_w + Inches(0.01)
            tx_arr = slide.shapes.add_textbox(arr_x, y_flow + Inches(0.4), step_gap, Inches(0.4))
            tf_a = tx_arr.text_frame
            tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
            pa = tf_a.paragraphs[0]
            pa.alignment = PP_ALIGN.CENTER
            pa.text = "→"
            pa.font.name = FONT_DISPLAY
            pa.font.size = Pt(14)
            pa.font.bold = True
            pa.font.color.rgb = ACCENT
            
    # 2 Mini-cards below
    y_cards = y_flow + Inches(1.5)
    card_w = Inches(5.72)
    card_gap = Inches(0.29)
    
    cards_data = [
        ("Đo lường phải đổi theo",
         "Bổ sung KPI: qualified action/session, activation/session, transaction/session, web-to-app activated user "
         "- bên cạnh organic sessions truyền thống."),
        ("Nghịch lý intent density",
         "AI answers có thể làm giảm số visitor nhưng tăng intent density của phần còn lại. "
         "Google ghi nhận click từ AI Overviews có chất lượng cao hơn, thời gian trên trang lâu hơn và conversion rate cao hơn.")
    ]
    
    for idx, (t, b) in enumerate(cards_data):
        x = Inches(0.8) + idx * (card_w + card_gap)
        add_card(slide, is_dark=False, left=x, top=y_cards, width=card_w, height=Inches(2.5),
                 title=t, body=b, top_accent=True, title_size=13, body_size=11)
        
    add_footer(slide, is_dark=False, foot_left="FUNNEL 2031 - VISIBILITY ĐẾN TRANSACTION", foot_right="06 / 22")

def build_slide_8(prs):
    """Slide 8: Ma trận chuyển dịch Web 2026 -> Web 2031 (Table)"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Ma trận chuyển dịch", 
                         title="Web 2026 → Web 2031",
                         meta_num="02.1", meta_tag="Cột 2031 là dự báo, không phải trạng thái đã xác nhận")
    
    headers = ["Dimension", "Web 2026", "Web 2031 - dự báo"]
    table_rows = [
        ("Discovery", "SERP, social, direct", "AI answers, agents, multimodal search, feeds, SERP"),
        ("Unit cạnh tranh", "Web page / keyword", "Entity, fact, capability, product, answer, API"),
        ("SEO", "Ranking và CTR", "Retrieval eligibility + citation + actionability"),
        ("Content", "Human-readable page", "Human-readable + machine-readable representation"),
        ("Conversion", "Click → landing page → CTA", "Answer/agent → action endpoint → web/app/transaction"),
        ("Web-to-App", "Banner, deferred deep link", "Intent-aware routing layer"),
        ("Data", "Analytics + cookies", "First-party identity + event graph + server-side attribution"),
        ("Identity", "Password/session", "Passkeys, WebAuthn, wallet credentials"),
        ("Payments", "Checkout UI", "Web payment APIs + tokenized/agent-assisted payment"),
        ("Distribution", "Browser-centric", "Browser + search + LLM + agent + OS + app"),
        ("Kiến trúc", "Page/content platform", "Capability and distribution platform")
    ]
    
    # Table shape
    num_rows = len(table_rows) + 1
    num_cols = 3
    t_left = Inches(0.8)
    t_top = top_pos + Inches(0.05)
    t_width = Inches(11.733)
    t_height = Inches(4.9)
    
    tbl_shape = slide.shapes.add_table(num_rows, num_cols, t_left, t_top, t_width, t_height)
    table = tbl_shape.table
    
    # Column widths
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(4.3)
    table.columns[2].width = Inches(5.233)
    
    # Header row
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG_LIGHT
        cell.margin_left = Inches(0.12)
        cell.margin_right = Inches(0.12)
        cell.margin_top = Inches(0.06)
        cell.margin_bottom = Inches(0.06)
        
        p = cell.text_frame.paragraphs[0]
        p.text = clean_text(h_text).upper()
        p.font.name = FONT_DISPLAY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT if c_idx == 2 else TEXT_PRIMARY_LIGHT
        
    # Content rows
    for r_idx, row_data in enumerate(table_rows):
        is_even = (r_idx % 2 == 0)
        for c_idx, cell_text in enumerate(row_data):
            cell = table.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BG_LIGHT if is_even else CARD_BG_LIGHT
            cell.margin_left = Inches(0.12)
            cell.margin_right = Inches(0.12)
            cell.margin_top = Inches(0.04)
            cell.margin_bottom = Inches(0.04)
            
            p = cell.text_frame.paragraphs[0]
            p.text = clean_text(cell_text)
            p.font.name = FONT_BODY
            p.font.size = Pt(9)
            
            if c_idx == 0:
                p.font.bold = True
                p.font.color.rgb = TEXT_PRIMARY_LIGHT
            elif c_idx == 1:
                p.font.color.rgb = TEXT_SECONDARY_LIGHT
            else:
                p.font.color.rgb = TEXT_PRIMARY_LIGHT
                p.font.bold = True
                
    add_footer(slide, is_dark=False, foot_left="MA TRẬN CHUYỂN DỊCH VAI TRÒ - 11 DIMENSIONS", foot_right="08 / 22")

def build_slide_9(prs):
    """Slide 9: Search, GEO & Machine-Readable Web"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Search, GEO và machine-readable web", 
                         title="SEO không bị thay thế bởi GEO - GEO là distribution layer phía trên",
                         meta_num="02.2", meta_tag="Google Search Central 2026")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left column: 2 cards
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos, width=col_w, height=Inches(2.4),
             title="Sai lầm phổ biến: 'SEO → GEO migration'",
             body="Mô hình hợp lý: Technical SEO → Entity/Data Layer → Retrieval Optimization → GEO Distribution. "
                  "Cơ sở dữ liệu và cấu trúc thực thể là nền tảng; không có nền tảng đó, GEO không có gì để trích dẫn.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos + Inches(2.55), width=col_w, height=Inches(2.4),
             title="Utilities-Led SEO có lợi thế tương đối",
             body="Google 2026 nhấn mạnh unique, non-commodity content. Bài 'Chuyển tiền quốc tế là gì?' dễ bị AI summary thay thế; "
                  "trang tính 'Phí chuyển tiền 5 triệu sang Nhật' có logic tính toán và tỷ giá real-time sẽ được AI trích dẫn và gửi người dùng đến để thực hiện.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    # Right column: Vertical representations + 1 card
    rx = Inches(0.8) + col_w + gap
    
    # Box for 3 representations
    rep_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, rx, top_pos, col_w, Inches(3.0))
    rep_box.fill.solid()
    rep_box.fill.fore_color.rgb = CARD_BG_LIGHT
    rep_box.line.color.rgb = CARD_BORDER_LIGHT
    rep_box.line.width = Pt(0.75)
    
    tx_rep = slide.shapes.add_textbox(rx + Inches(0.18), top_pos + Inches(0.14), col_w - Inches(0.36), Inches(2.72))
    tf_rep = tx_rep.text_frame
    tf_rep.word_wrap = True
    tf_rep.margin_left = tf_rep.margin_top = tf_rep.margin_right = tf_rep.margin_bottom = 0
    
    pk = tf_rep.paragraphs[0]
    pk.text = "WEBSITE 2031 TỒN TẠI DƯỚI 3 REPRESENTATION"
    pk.font.name = FONT_DISPLAY
    pk.font.size = Pt(9.5)
    pk.font.bold = True
    pk.font.color.rgb = ACCENT
    pk.space_after = Pt(6)
    
    reps = [
        ("1. Human representation", "Page / interface cho con người đọc và thao tác"),
        ("2. Machine semantic representation", "Structured data, feeds, entity relationships, metadata"),
        ("3. Executable representation", "APIs / tools / actions mà agent có thể gọi")
    ]
    for r_title, r_sub in reps:
        p_t = tf_rep.add_paragraph()
        p_t.text = r_title
        p_t.font.name = FONT_DISPLAY
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_PRIMARY_LIGHT
        
        p_s = tf_rep.add_paragraph()
        p_s.text = r_sub
        p_s.font.name = FONT_BODY
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = TEXT_SECONDARY_LIGHT
        p_s.space_after = Pt(4)
        
    add_card(slide, is_dark=False, left=rx, top=top_pos + Inches(3.15), width=col_w, height=Inches(1.8),
             title="Từ page-first sang entity + capability-first",
             body="\"Tỷ giá USD/VND\", \"phí chuyển tiền\", \"điều kiện vay\", \"merchant\", \"product catalog\" - mỗi capability cần cả 3 tầng trên để vừa phục vụ người dùng vừa phục vụ AI agents.",
             top_accent=True, title_size=12, body_size=10)
    
    add_footer(slide, is_dark=False, foot_left="KIẾN TRÚC MACHINE-READABLE WEB", foot_right="09 / 22")

def build_slide_10(prs):
    """Slide 10: Agentic Web (Dark)"""
    slide = create_base_slide(prs, is_dark=True)
    top_pos = add_header(slide, is_dark=True, kicker="Agentic Web - thay đổi lớn hơn GEO", 
                         title="Website user ≠ chỉ con người: human + crawler + LLM + agent",
                         meta_num="03.1", meta_tag="Dự báo có cơ sở")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left column: Bullet list card + Distribution shift card
    left_bullets = [
        ("Browser agents đã hoạt động:", "đọc DOM, accessibility tree, screenshot; truy cập website và thực hiện task thay người dùng (Google Search Central 2026)."),
        ("Commerce chuyển sang protocol:", "UCP (Google, 1/2026) chuẩn hóa interaction agent-merchant-payment qua REST API, MCP, A2A; MCP transport beta cho Native Checkout 11/2026."),
        ("MCP stateless (spec 7/2026):", "routing, cache semantics, authorization hardening - phù hợp Internet-scale."),
        ("OpenAI Agentic Commerce Protocol:", "mở rộng product discovery (3/2026); ChatGPT Wallet + merchant agent guidance (11/2026). Chưa thể kết luận protocol nào thắng cuộc.")
    ]
    add_bullets_box(slide, is_dark=True, left=Inches(0.8), top=top_pos, width=col_w, height=Inches(3.3),
                    bullets=left_bullets, kicker="ĐỘNG LỰC CÔNG NGHỆ 2025-2026", title="Bốn lực đẩy phía giao thức")
    
    add_card(slide, is_dark=True, left=Inches(0.8), top=top_pos + Inches(3.45), width=col_w, height=Inches(1.5),
             title="Distribution dịch chuyển",
             body="Từ \"index my page\" sang \"discover my capability → inspect conditions → authorize → execute action\". Với fintech, đây là thay đổi lớn hơn GEO.",
             top_accent=True, hot=True, title_size=12, body_size=10.5)
    
    # Right column: Example, Native UI risk, Caution
    rx = Inches(0.8) + col_w + gap
    add_card(slide, is_dark=True, left=rx, top=top_pos, width=col_w, height=Inches(1.65),
             title="\"Tìm cách thanh toán hóa đơn này có cashback cao nhất và trả trước 8 giờ tối\"",
             body="Agent cần: discover provider → read offer eligibility → verify user/account → request payment quote → obtain authorization → execute transaction → return receipt.",
             kicker="VÍ DỤ TƯƠNG LAI GẦN", top_accent=True, title_size=11.5, body_size=10)
    
    add_card(slide, is_dark=True, left=rx, top=top_pos + Inches(1.8), width=col_w, height=Inches(1.45),
             title="Nếu business logic chỉ nằm trong native UI...",
             body="Fintech sẽ khó tham gia vào ecosystem agentic này. Web domain trở thành ownership và routing authority giữa open web và app ecosystem (App Links / Universal Links).",
             top_accent=True, title_size=11.5, body_size=10)
    
    add_card(slide, is_dark=True, left=rx, top=top_pos + Inches(3.4), width=col_w, height=Inches(1.55),
             title="Cảnh giác với hype chu kỳ ngắn",
             body="Không xây llms.txt hay proprietary AI markup chỉ vì hype - Google nói rõ không cần AI-specific machine-readable files. Nghiên cứu độc lập cũng cho thấy llms.txt chưa được kiểm chứng.",
             kicker="CẢNH BÁO KỸ THUẬT", top_accent=True, title_size=11.5, body_size=10)
    
    add_footer(slide, is_dark=True, foot_left="AGENTIC WEB - UCP / MCP / A2A / WEBMCP", foot_right="10 / 22")

def build_slide_11(prs):
    """Slide 11: Architectural Shifts (Generative UI & Edge Compute)"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Hai chuyển biến kiến trúc", 
                         title="Generative UI có kiểm soát & compute về edge",
                         meta_num="03.2", meta_tag="Dự báo có cơ sở")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left column: Controlled Generative UI & Edge Compute
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos, width=col_w, height=Inches(2.4),
             title="Controlled Generative UI",
             body="Kịch bản \"LLM tự viết HTML/CSS real-time cho từng user\" hấp dẫn nhưng có hai rào cản: (1) benchmark OpenUI cho thấy lợi thế DSL chưa áp đảo; "
                  "(2) cognitive load + trí nhớ không gian của con người - hiệu suất web dựa mạnh vào tính nhất quán không gian (NN/g). "
                  "Xu hướng thực tế: generative UI có kiểm soát trong khung thiết kế hệ thống, không phải free-form.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos + Inches(2.55), width=col_w, height=Inches(2.4),
             title="Compute & AI cục bộ",
             body="WebGPU, Wasm 3.0, SLM on-device, PWA, WebXR đang dịch chuyển suy luận AI về thiết bị. "
                  "Khoảng cách năng lực web app vs native app thu hẹp mạnh ở hầu hết tác vụ nghiệp vụ, sáng tạo nội dung, thương mại. "
                  "PWA là công cụ, không phải chiến lược mặc định - phù hợp utility repeat-usage cao, không phù hợp core wallet.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    # Right column: Multimodal UX & Web Platform Impact
    rx = Inches(0.8) + col_w + gap
    add_card(slide, is_dark=False, left=rx, top=top_pos, width=col_w, height=Inches(2.4),
             title="Multimodal UX thay chatbot gắn góc",
             body="Thời kỳ hộp chatbot góc màn hình đang khép lại; tương tác đa phương thức hợp nhất trở thành chuẩn. "
                  "Website phải thiết kế cho nhiều phương thức input, không chỉ gõ + nhấp.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=rx, top=top_pos + Inches(2.55), width=col_w, height=Inches(2.4),
             title="Hệ quả cho Web Platform",
             body="Đầu tư vào design system chặt và component runtime có kiểm soát sẽ đáng giá hơn chạy theo mọi AI UI framework nhất thời "
                  "- Forrester cảnh báo làn sóng cắt giảm ngân sách khi chi phí triển khai AI UI vượt giá trị thu về.",
             top_accent=True, hot=True, title_size=12.5, body_size=10.5)
    
    add_footer(slide, is_dark=False, foot_left="KIẾN TRÚC 2031 - GENERATIVE UI & EDGE", foot_right="11 / 22")

def build_slide_13(prs):
    """Slide 13: Three Trust Protocol Layers"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Ba lớp giao thức tin cậy mới", 
                         title="Identity, provenance và thanh toán gốc của Internet",
                         meta_num="03.1", meta_tag="Chuẩn W3C / Android / Apple đã công bố")
    
    # Top 3 cards
    c_w = Inches(3.72)
    gap = Inches(0.28)
    top_cards = [
        ("Identity con người",
         "WebAuthn Level 3 là W3C Recommendation (25/8/2026) - nền của passkeys. Digital Credentials API tích hợp Chrome 141+, Edge 141+, Safari 26 (cuối 2025). "
         "Flow tương lai: anonymous → passkey → verified credential → authenticated customer. Web = identity bridge trước khi cài app."),
        ("Provenance nội dung",
         "Ước tính ~ 52% bài viết mới trên web do AI tạo (giữa 2025) + làn sóng AI slop → nhu cầu chứng thực nguồn gốc tăng. "
         "robots.txt (1994) và User-Agent tự khai đã lỗi thời; agent identity cần cơ chế mật mã cưỡng chế được."),
        ("Thanh toán gốc",
         "Payment Request API (W3C CR Draft 11/2026) + Secure Payment Confirmation. x402 (Coinbase) hồi sinh HTTP 402 cho micropayment agent-native. "
         "AP2/UCP dùng cryptographically signed mandates cho agent-led payments.")
    ]
    
    for idx, (t, b) in enumerate(top_cards):
        x = Inches(0.8) + idx * (c_w + gap)
        add_card(slide, is_dark=False, left=x, top=top_pos, width=c_w, height=Inches(2.55),
                 title=t, body=b, top_accent=True, title_size=12.5, body_size=10)
        
    # Bottom 2 cards
    y_bot = top_pos + Inches(2.7)
    bot_w = Inches(5.72)
    bot_gap = Inches(0.29)
    bot_cards = [
        ("Phân vai Web ↔ Native app",
         "Web: acquisition, trial, lightweight task, identity initiation, cross-platform transaction. "
         "Native app: high-frequency use, deep personalization, device-sensitive capability, loyalty, retention. "
         "Website trở thành activation surface, không chỉ marketing surface."),
        ("Bối cảnh pháp lý & an ninh",
         "Án lệ Amazon kiện Perplexity (trình duyệt AI Comet) cho thấy mở cửa agent = mặt trận pháp lý mới. "
         "OWASP Top 10 for Agentic Applications 2026 chuẩn hóa rủi ro. Agent gateway phải là security product, không chỉ API gateway.")
    ]
    
    for idx, (t, b) in enumerate(bot_cards):
        x = Inches(0.8) + idx * (bot_w + bot_gap)
        add_card(slide, is_dark=False, left=x, top=y_bot, width=bot_w, height=Inches(2.2),
                 title=t, body=b, top_accent=True, hot=(idx==1), title_size=12.5, body_size=10.5)
        
    add_footer(slide, is_dark=False, foot_left="TRUST LAYER - IDENTITY / PROVENANCE / PAYMENT", foot_right="13 / 22")

def build_slide_15(prs):
    """Slide 15: Two Domains with Strongest Signals (E-commerce & B2B)"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Hai lĩnh vực có tín hiệu mạnh nhất", 
                         title="E-commerce tách \"buying\" khỏi \"shopping\" - B2B đề cao con người ở tầng quyết định",
                         meta_num="04.1", meta_tag="Dữ kiện thị trường 2025-2026")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left: E-commerce
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos, width=col_w, height=Inches(2.55),
             title="E-commerce: giao dịch trong AI surface đã đảo chiều",
             body="McKinsey ước agentic commerce $3-5 nghìn tỷ USD vào 2030. OpenAI ra Instant Checkout cùng Stripe qua Agentic Commerce Protocol (ACP, 3/2026). "
                  "Shopify: agentic buying cho hàng lặp lại (mua lại, bổ sung); shopping truyền thống (khám phá, cảm hứng, thương hiệu) vẫn ở trên website giàu trải nghiệm.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos + Inches(2.7), width=col_w, height=Inches(2.2),
             title="Tiêu chí sống còn của web thương mại",
             body="Feed/API chuẩn máy đọc (product feeds, signed agent requests), transactional endpoints chuẩn hóa, chính sách giá minh bạch cho bot, và cơ chế chống arbitrage tự động.",
             top_accent=True, title_size=12, body_size=10.5)
    
    # Right: B2B SaaS
    rx = Inches(0.8) + col_w + gap
    add_card(slide, is_dark=False, left=rx, top=top_pos, width=col_w, height=Inches(2.55),
             title="B2B SaaS: nghịch lý củng cố website",
             body="Agent xử lý quy trình, nhưng Gartner (5/2026, 645 buyers): 67% thích tự tìm hiểu không qua rep; website nhà cung cấp là kênh số 1 ở giai đoạn cân nhắc và ra quyết định. "
                  "Website B2B không bị thay thế - nó trở thành validation & due diligence center.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=rx, top=top_pos + Inches(2.7), width=col_w, height=Inches(2.2),
             title="Lưu ý methodology",
             body="Các ước tính agentic commerce dao động rất rộng tùy định nghĩa ($3-5T McKinsey vs các nguồn khác) - dùng làm hướng, không dùng làm con số tuyệt đối cho business case ngắn hạn.",
             kicker="PHƯƠNG PHÁP LUẬN", top_accent=True, title_size=12, body_size=10.5)
    
    add_footer(slide, is_dark=False, foot_left="VAI TRÒ THEO LĨNH VỰC - E-COMMERCE & B2B", foot_right="15 / 22")

def build_slide_16(prs):
    """Slide 16: Journalism, Content & Anti-Slop"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Báo chí, nội dung và phản trào lưu", 
                         title="Pageview economy phân cực - giá trị khan hiếm quay về nội dung nhân bản",
                         meta_num="04.2", meta_tag="Dữ kiện 2025-2026")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left column
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos, width=col_w, height=Inches(2.4),
             title="Nội dung đại trà suy thoái kinh tế",
             body="Nhiều ấn phẩm tin công nghệ mất 62-97% referral traffic. ~ 50 thỏa thuận bản quyền AI đã công bố từ 2023 (NYT và các vụ kiện khác vẫn tiếp diễn). "
                  "Mô hình dựa trên pageview và programmatic ads đang sụp đổ ở phân khúc tin tức đại trà.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=Inches(0.8), top=top_pos + Inches(2.55), width=col_w, height=Inches(2.4),
             title="Anti-slop: giá trị khan hiếm mới",
             body="\"AI slop\" được Merriam-Webster và AAAS chọn là Từ của năm 2025. Song song: Small Web / IndieWeb, blog cá nhân, email newsletters, "
                  "cộng đồng kín tăng trưởng phản ánh sự mệt mỏi với nội dung tổng hợp. Giá trị dịch chuyển về con người, kinh nghiệm thực chứng và danh tiếng cá nhân.",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    # Right column
    rx = Inches(0.8) + col_w + gap
    add_card(slide, is_dark=False, left=rx, top=top_pos, width=col_w, height=Inches(2.4),
             title="Search volume chưa sụp đổ - traffic mới phân hóa",
             body="Sắc thái quan trọng thường bị diễn giải sai: khối lượng tìm kiếm thực tế chưa sụp; tác động của AI Search phân hóa mạnh theo loại truy vấn "
                  "(informational giảm click mạnh nhất; navigational và transactional giữ ổn định hơn nhiều).",
             top_accent=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=rx, top=top_pos + Inches(2.55), width=col_w, height=Inches(2.4),
             title="Bài học cho MoMo",
             body="Nội dung tài chính YMYL phải đi hướng E-E-A-T + dữ liệu gốc, tránh commodity content - cùng kết luận với chiến lược Utility Hubs và Entity Graph đang triển khai.",
             top_accent=True, hot=True, title_size=12.5, body_size=10.5)
    
    add_footer(slide, is_dark=False, foot_left="NỘI DUNG & ANTI-SLOP - PHÂN CỰC THỊ TRƯỜNG", foot_right="16 / 22")

def build_slide_18(prs):
    """Slide 18: Three Scenarios to 2031"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Ba kịch bản tới 2031", 
                         title="Web Companion · Web as API · Closed AI Platforms",
                         meta_num="05.1", meta_tag="Scenario planning - không chọn một")
    
    # 3 Scenario cards
    c_w = Inches(3.72)
    gap = Inches(0.28)
    
    scenarios = [
        ("Kịch bản A - xác suất cao nhất", "Web Companion",
         "AI Search tăng mạnh nhưng website vẫn nhận direct traffic đáng kể. Agents chủ yếu hỗ trợ research/navigation, chưa tự động hóa nhiều transaction tài chính. "
         "Web giữ vai trò: Search acquisition → utility → trust → app activation.\n\n"
         "Early indicators: AI referral tăng nhưng human sessions ổn định · agent transaction thấp · utility giữ conversion advantage · deep-link activation tăng."),
        ("Kịch bản B", "Web as API",
         "AI interfaces thành primary discovery layer. Người dùng xem ít pages hơn nhưng agents truy vấn business data nhiều hơn. "
         "Website = canonical entity store + tool endpoint + transaction gateway.\n\n"
         "Early indicators: AI API traffic > referral · open action APIs · identity hội tụ.\nRủi ro: disintermediation, commoditization, fraud automation."),
        ("Kịch bản C - rủi ro lớn nhất", "Closed AI Platforms",
         "AI ecosystems thành 'super-distributors': discovery, comparison, transaction diễn ra trong platform lớn. Website traffic giảm mạnh, mỗi platform đòi feed/API riêng.\n\n"
         "Early indicators: direct checkout trong AI surfaces tăng · organic clicks giảm liên tục · proprietary integrations.\nRủi ro: Web thành backend commodity.")
    ]
    
    for idx, (k, t, b) in enumerate(scenarios):
        x = Inches(0.8) + idx * (c_w + gap)
        add_card(slide, is_dark=False, left=x, top=top_pos, width=c_w, height=Inches(3.3),
                 title=t, body=b, kicker=k, top_accent=True, hot=(idx==2), title_size=13, body_size=9.5)
        
    # Bottom box: Optionality Strategy
    y_bot = top_pos + Inches(3.45)
    add_card(slide, is_dark=False, left=Inches(0.8), top=y_bot, width=Inches(11.733), height=Inches(1.5),
             title="Chiến lược Optionality & Giả định bác bỏ",
             body="Optionality: platform được thiết kế sao cho Scenario A có UX tốt, Scenario B có APIs/tools tốt, Scenario C có distribution portability tốt.\n"
                  "Giả định bác bỏ: A - agents hoàn thành phần lớn low-risk transactions; B - users không tin agents đủ để giao quyền; C - regulators/merchants yêu cầu interoperability.",
             kicker="CHIẾN LƯỢC ĐẦU TƯ", top_accent=True, hot=True, title_size=11.5, body_size=10.5)
    
    add_footer(slide, is_dark=False, foot_left="SCENARIO PLANNING 2031", foot_right="18 / 22")

def build_slide_19(prs):
    """Slide 19: Investment Framework 2027-2031 (6 Layers)"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Framework đầu tư 2027-2031", 
                         title="Từ SEO Platform sang Open Distribution Platform - sáu lớp",
                         meta_num="05.2", meta_tag="Dự báo có cơ sở")
    
    layers = [
        ("1. Discoverability",
         "Mọi public capability phải discoverable bởi search, AI, agents: crawl/index architecture, entity architecture, canonical URLs, structured data, dynamic sitemap/feeds, machine-readable metadata, source freshness, AI visibility monitoring."),
        ("2. Utility",
         "Ưu tiên sản phẩm có đủ 4 đặc điểm: search demand + dynamic data + computation + downstream fintech action. Growth loop: Organic impression → utility computation → trust validation → app action / transaction."),
        ("3. Identity",
         "WebAuthn/passkeys, consistent account identity, permission model, credential verification, consent state, bot/agent identity. Web là nơi chuyển đổi anonymous visitor thành authenticated user với friction thấp nhất."),
        ("4. Web-App Continuity",
         "Deep links = shared infrastructure. Canonical URL map: URL → web content → Android App Link → iOS Universal Link → desktop web. Web Platform là router thông minh phân bổ theo intent, device và user state."),
        ("5. Agent Gateway",
         "Thứ tự: Read → Quote → Prepare → Authenticate → Confirm → Execute. Financial actions chỉ lên Level 4-5 khi authentication, authorization, liability và dispute resolution đủ rõ."),
        ("6. Measurement",
         "Distribution Observatory: Human Search + AI Search + Agent + Web-to-App + Business. North Star dịch từ Organic Traffic sang Qualified Actions và Incremental Activated Users.")
    ]
    
    c_w = Inches(3.72)
    c_h = Inches(2.35)
    gap_x = Inches(0.28)
    gap_y = Inches(0.2)
    
    for idx, (t, b) in enumerate(layers):
        col = idx % 3
        row = idx // 3
        x = Inches(0.8) + col * (c_w + gap_x)
        y = top_pos + row * (c_h + gap_y)
        add_card(slide, is_dark=False, left=x, top=y, width=c_w, height=c_h,
                 title=t, body=b, top_accent=True, title_size=12, body_size=9.5)
        
    add_footer(slide, is_dark=False, foot_left="SÁU LỚP ĐẦU TƯ - OPEN DISTRIBUTION PLATFORM", foot_right="19 / 22")

def build_slide_20(prs):
    """Slide 20: Agent Gateway - Controlled Escalation (Dark)"""
    slide = create_base_slide(prs, is_dark=True)
    top_pos = add_header(slide, is_dark=True, kicker="Agent Gateway - leo thang có kiểm soát", 
                         title="Sáu levels: từ public data đến delegated transaction",
                         meta_num="05.3", meta_tag="Fintech chỉ lên Level 4-5 khi đủ auth/mandate/fraud/liability")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left column: Ladder
    rungs = [
        ("L0", "Public factual data", "Thông tin công khai, không cần auth", False),
        ("L1", "Calculator / API", "Utility tính toán, tra cứu read-only", False),
        ("L2", "Personalized quote", "Quote theo profile, chưa cần auth mạnh", False),
        ("L3", "Authenticated preparation", "Chuẩn bị giao dịch sau xác thực", False),
        ("L4", "User-confirmed transaction", "User xác nhận cuối - an toàn cho tiền thật", True),
        ("L5", "Delegated agent transaction", "Agent ủy quyền thực hiện - cần mandate/liability", True)
    ]
    
    rung_h = Inches(0.74)
    rung_gap = Inches(0.08)
    
    for idx, (lv, name, desc, is_hot) in enumerate(rungs):
        y = top_pos + idx * (rung_h + rung_gap)
        box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y, col_w, rung_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG_DARK
        box.line.color.rgb = ACCENT_DARK if is_hot else CARD_BORDER_DARK
        box.line.width = Pt(1.5 if is_hot else 0.75)
        
        tx = slide.shapes.add_textbox(Inches(0.95), y + Inches(0.1), col_w - Inches(0.3), rung_h - Inches(0.2))
        tf = tx.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        r_lv = p.add_run()
        r_lv.text = lv + "  "
        r_lv.font.name = FONT_DISPLAY
        r_lv.font.size = Pt(12)
        r_lv.font.bold = True
        r_lv.font.color.rgb = ACCENT_DARK if is_hot else TEXT_PRIMARY_DARK
        
        r_name = p.add_run()
        r_name.text = name + " - "
        r_name.font.name = FONT_DISPLAY
        r_name.font.size = Pt(10.5)
        r_name.font.bold = True
        r_name.font.color.rgb = TEXT_PRIMARY_DARK
        
        r_desc = p.add_run()
        r_desc.text = desc
        r_desc.font.name = FONT_BODY
        r_desc.font.size = Pt(9.5)
        r_desc.font.color.rgb = TEXT_SECONDARY_DARK
        
    # Right column: Metric utility & Discovery
    rx = Inches(0.8) + col_w + gap
    
    utility_bullets = [
        ("Utility Action Rate:", "Qualified Web User / Total Visits"),
        ("W2A Activation Rate:", "Activated User / Organic Impression"),
        ("Transaction Value:", "Giá trị giao dịch / Qualified Visit"),
        ("AI Citation Share:", "Share of Answers trong category fintech")
    ]
    add_bullets_box(slide, is_dark=True, left=rx, top=top_pos, width=col_w, height=Inches(2.55),
                    bullets=utility_bullets, kicker="ĐO LƯỜNG MỚI", title="Metric utility không đo bằng sessions")
    
    add_card(slide, is_dark=True, left=rx, top=top_pos + Inches(2.7), width=col_w, height=Inches(2.2),
             title="Discovery phải tính cả non-click visibility",
             body="Acquisition 2031 đo cả AI citations, agent actions - không chỉ impressions → click → session truyền thống.",
             top_accent=True, hot=True, title_size=12.5, body_size=11)
    
    add_footer(slide, is_dark=True, foot_left="AGENTIC GATEWAY - LEVELS 0-5", foot_right="20 / 22")

def build_slide_21(prs):
    """Slide 21: Priority Roadmap 2027-2031"""
    slide = create_base_slide(prs, is_dark=False)
    top_pos = add_header(slide, is_dark=False, kicker="Roadmap ưu tiên 2027-2031", 
                         title="Năm giai đoạn - từ Foundation đến Distribution OS",
                         meta_num="05.4", meta_tag="Dự báo có cơ sở")
    
    # 5 Timeline stages horizontal
    stages = [
        ("2027", "Foundation", "Entity Graph + Utility Platform + Deep Link Platform + First-party Measurement. Audit canonical data, passkeys, app-link coverage, bot policies."),
        ("2028", "AI Distribution", "GEO Observatory + machine-readable content APIs + answer-quality monitoring. Mỗi key entity: canonical page + structured data + public quote API."),
        ("2029", "Agent Readiness", "Agent Gateway + signed agent identity + permission scopes + observable APIs. Thử nghiệm low-risk: search, calculate, compare, prepare transaction."),
        ("2030", "Transaction Readiness", "Agent-assisted authenticated flows. Không tự động hóa transaction nếu chưa rõ: intent, authorization, liability, dispute resolution."),
        ("2031", "Distribution OS", "Platform sở hữu: URL architecture, entity graph, public product data, utility runtime, identity bridge, deep-link engine, agent gateway, unified attribution.")
    ]
    
    tl_w = Inches(2.22)
    tl_gap = Inches(0.15)
    tl_h = Inches(2.4)
    
    for idx, (year, stage_name, desc) in enumerate(stages):
        x = Inches(0.8) + idx * (tl_w + tl_gap)
        box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, top_pos, tl_w, tl_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG_LIGHT
        box.line.color.rgb = CARD_BORDER_LIGHT
        box.line.width = Pt(0.75)
        
        # Top accent bar
        tbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, top_pos, tl_w, Pt(2.5))
        tbar.fill.solid()
        tbar.fill.fore_color.rgb = ACCENT
        tbar.line.fill.background()
        
        tx = slide.shapes.add_textbox(x + Inches(0.12), top_pos + Inches(0.12), tl_w - Inches(0.24), tl_h - Inches(0.24))
        tf = tx.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_yr = tf.paragraphs[0]
        p_yr.text = year
        p_yr.font.name = FONT_DISPLAY
        p_yr.font.size = Pt(16)
        p_yr.font.bold = True
        p_yr.font.color.rgb = ACCENT
        p_yr.space_after = Pt(2)
        
        p_st = tf.add_paragraph()
        p_st.text = stage_name
        p_st.font.name = FONT_DISPLAY
        p_st.font.size = Pt(11)
        p_st.font.bold = True
        p_st.font.color.rgb = TEXT_PRIMARY_LIGHT
        p_st.space_after = Pt(4)
        
        p_dsc = tf.add_paragraph()
        p_dsc.text = desc
        p_dsc.font.name = FONT_BODY
        p_dsc.font.size = Pt(8.5)
        p_dsc.font.color.rgb = TEXT_SECONDARY_LIGHT
        p_dsc.line_spacing = 1.15
        
    # Bottom 2 cards: No-regret bets vs Contingent bets
    y_bot = top_pos + Inches(2.6)
    bot_w = Inches(5.72)
    bot_gap = Inches(0.29)
    
    add_card(slide, is_dark=False, left=Inches(0.8), top=y_bot, width=bot_w, height=Inches(2.3),
             title="Nên đầu tư bất kể scenario nào (No-regret bets)",
             body="Canonical entity/data layer · utilities · structured data hygiene · deep-link infrastructure · "
                  "WebAuthn/passkeys · first-party measurement · anti-bot hygiene.",
             kicker="ĐẦU TƯ BẮT BUỘC", top_accent=True, hot=True, title_size=12.5, body_size=10.5)
    
    add_card(slide, is_dark=False, left=Inches(0.8) + bot_w + bot_gap, top=y_bot, width=bot_w, height=Inches(2.3),
             title="Chưa nên over-invest (Contingent bets / Hype traps)",
             body="Một GEO scoring proprietary duy nhất · một agent protocol duy nhất · fully autonomous financial agents · "
                  "PWA replace app hoàn toàn · AI slop/content farming.",
             kicker="TRÁNH BẪY QUÁ TẢI", top_accent=True, title_size=12.5, body_size=10.5)
    
    add_footer(slide, is_dark=False, foot_left="ROADMAP 2027-2031 - OPTION CHO AGENTIC FUTURE", foot_right="21 / 22")

def build_slide_22(prs):
    """Slide 22: Strategic Hypotheses & MoMo Implications (Dark)"""
    slide = create_base_slide(prs, is_dark=True)
    top_pos = add_header(slide, is_dark=True, kicker="Hypothesis cần chủ động bác bỏ + hàm ý cho MoMo", 
                         title="Năm giả thuyết chiến lược - và vị trí của Web Platform hôm nay")
    
    col_w = Inches(5.72)
    gap = Inches(0.29)
    
    # Left column: 5 hypotheses
    hypos = [
        ("H1:", "AI Search tiếp tục làm giảm informational CTR → bác bỏ nếu qualified organic traffic tăng bền trên nhóm query có AI answers."),
        ("H2:", "Utility pages chống zero-click tốt hơn editorial → bác bỏ bằng controlled cohorts nếu utility không uplift activation/conversion."),
        ("H3:", "Open Web thành agent capability layer → bác bỏ nếu agent platforms chủ yếu dùng proprietary integrations."),
        ("H4:", "Website là W2A acquisition layer tốt hơn paid install flow ở high-intent queries → bác bỏ bằng CAC → activated user và LTV cohort."),
        ("H5:", "Entity architecture tạo lợi thế GEO → bác bỏ nếu entity coverage/structured data không tương quan với AI citation sau khi kiểm soát authority + content quality.")
    ]
    add_bullets_box(slide, is_dark=True, left=Inches(0.8), top=top_pos, width=col_w, height=Inches(4.9),
                    bullets=hypos, kicker="TIÊU CHÍ BÁC BỎ THỰC NGHIỆM", title="Năm giả thuyết chiến lược cần falsify")
    
    # Right column: 3 cards
    rx = Inches(0.8) + col_w + gap
    add_card(slide, is_dark=True, left=rx, top=top_pos, width=col_w, height=Inches(1.55),
             title="Dữ liệu thực tế MoMo (Clarity + Bing AI, YTD 11/2026)",
             body="353.193 page citations · 28.701 AI referral sessions · SoA 19,26% · đỉnh 11.920 citations/ngày (12/11). "
                  "Citations tăng 3-4x từ Q3 nhưng tập trung vào ít page hơn - concentration risk. "
                  "Cụm utility (giá xăng, tra cứu BHYT) là citation magnet; cụm tài chính PFM gần như vắng mặt.",
             top_accent=True, title_size=11.5, body_size=9)
    
    add_card(slide, is_dark=True, left=rx, top=top_pos + Inches(1.68), width=col_w, height=Inches(1.55),
             title="5 nguyên tắc hành động 2026 (từ research)",
             body="1. Đo riêng bot vs human traffic, đừng đánh giá sức khỏe web chỉ qua pageviews. "
                  "2. Sở hữu data gốc + điểm chốt giao dịch. 3. An ninh cho agent như mặt trận riêng. "
                  "4. Phân tầng chi phí AI theo giá trị đo được. 5. Đầu tư giá trị máy không tự tạo được: data độc quyền, research thực địa, community xác thực.",
             top_accent=True, title_size=11.5, body_size=9)
    
    add_card(slide, is_dark=True, left=rx, top=top_pos + Inches(3.35), width=col_w, height=Inches(1.55),
             title="Ba câu hỏi research tiếp theo giá trị nhất",
             body="AI Search đang thay đổi click curve của query fintech Việt Nam thế nào · "
                  "utility nào tạo incremental activated users thay vì cannibalize app · "
                  "Agent-Ready Financial Capability Standard cần data contract, identity, authorization, security, measurement ra sao.",
             top_accent=True, hot=True, title_size=11.5, body_size=9)
    
    add_footer(slide, is_dark=True, foot_left="HYPOTHESES & HÀM Ý - WEBSITE 2031", foot_right="22 / 22")

# ==============================================================================
# MAIN CONVERTER PIPELINE
# ==============================================================================

def main():
    prs = init_presentation()
    
    print("Building Slide 1: Cover...")
    build_slide_1(prs)
    
    print("Building Slide 2: Table of Contents...")
    build_slide_2(prs)
    
    print("Building Slide 3: Executive Summary...")
    build_slide_3(prs)
    
    print("Building Slide 4: Section 01...")
    build_section_slide(prs, "01", "Bối cảnh: pageview economy đang thu hẹp",
                        "Search đã chuyển từ \"query → danh sách link → website\" sang \"query → synthesized answer → optional exploration\". "
                        "Discovery không còn đồng nghĩa với click - và bot traffic đang viết lại kinh tế vận hành của website.",
                        "PHẦN 01 - BỐI CẢNH", "04 / 22", is_dark=False)
    
    print("Building Slide 5: Quantitative Evidence...")
    build_slide_5(prs)
    
    print("Building Slide 6: Forecast...")
    build_slide_6(prs)
    
    print("Building Slide 7: Section 02...")
    build_section_slide(prs, "02", "Chuyển dịch vai trò: mười dimension thay đổi",
                        "Website không biến mất, nhưng đơn vị cạnh tranh, định nghĩa SEO, kiến trúc nội dung và "
                        "mô hình phân phối đều đang được định nghĩa lại.",
                        "PHẦN 02 - CHUYỂN DỊCH VAI TRÒ", "07 / 22", is_dark=True)
    
    print("Building Slide 8: Shift Matrix (Table)...")
    build_slide_8(prs)
    
    print("Building Slide 9: Search, GEO & Machine-Readable Web...")
    build_slide_9(prs)
    
    print("Building Slide 10: Agentic Web...")
    build_slide_10(prs)
    
    print("Building Slide 11: Architectural Shifts...")
    build_slide_11(prs)
    
    print("Building Slide 12: Section 03...")
    build_section_slide(prs, "03", "Trust, identity và transaction layer",
                        "Sự tiến hóa bị đánh giá thấp nhất: domain trở thành trust anchor, web trở thành "
                        "low-friction identity bridge và transaction gateway - trước khi người dùng tải native app.",
                        "PHẦN 03 - TRUST & TRANSACTION", "12 / 22", is_dark=False)
    
    print("Building Slide 13: Trust Protocols...")
    build_slide_13(prs)
    
    print("Building Slide 14: Section 04...")
    build_section_slide(prs, "04", "Vai trò mới theo từng lĩnh vực",
                        "Tiến hóa công nghệ không tác động đồng nhất. E-commerce, B2B, báo chí và "
                        "nội dung đại trà đang đi về bốn hướng rất khác nhau.",
                        "PHẦN 04 - THEO LĨNH VỰC", "14 / 22", is_dark=True)
    
    print("Building Slide 15: E-commerce & B2B...")
    build_slide_15(prs)
    
    print("Building Slide 16: Content & Anti-Slop...")
    build_slide_16(prs)
    
    print("Building Slide 17: Section 05...")
    build_section_slide(prs, "05", "Kịch bản, framework đầu tư và roadmap",
                        "Không chọn một kịch bản - thiết kế platform để sống được trong cả ba. "
                        "Đó là một optionality strategy.",
                        "PHẦN 05 - KỊCH BẢN & FRAMEWORK", "17 / 22", is_dark=False)
    
    print("Building Slide 18: Three Scenarios...")
    build_slide_18(prs)
    
    print("Building Slide 19: Investment Framework...")
    build_slide_19(prs)
    
    print("Building Slide 20: Agent Gateway...")
    build_slide_20(prs)
    
    print("Building Slide 21: Priority Roadmap...")
    build_slide_21(prs)
    
    print("Building Slide 22: Strategic Hypotheses & MoMo...")
    build_slide_22(prs)
    
    out_path = "07_REPORTS/docs/strategy/website-2031-research-deck.pptx"
    prs.save(out_path)
    print(f"\nSuccessfully generated {len(prs.slides)} slides in {out_path}!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Convert markdown to .docx theo MoMo brand style của docx Reflection V1.

Dùng một docx mẫu (template) để giữ nguyên styles, numbering, header/footer, khổ A4,
rồi dựng lại body từ markdown.

Mapping:
  #     -> Title (viền dưới hồng)
  ##    -> Heading 1 (viền trái hồng, nền hồng nhạt)
  ###   -> Heading 2
  ####  -> Heading 2 (cỡ nhỏ hơn)
  - / * -> bullet (numId 2, hỗ trợ lồng 2 cấp theo thụt lề)
  1.    -> danh sách số, số màu hồng đậm
  >     -> đoạn trích, viền trái hồng
  |..|  -> bảng: header hồng, dòng xen màu, dòng Tổng/Lũy kế tô đậm

Usage:
  ./.venv/bin/python scripts/md_to_docx_momo.py <input.md> <output.docx> [--template <v1.docx>]
"""
import argparse
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml import parse_xml

W_NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
PINK = "AF0171"
GREEN = "15803D"  # kết quả tốt
RED = "C00000"  # điểm nghẽn / rủi ro
FONT = '<w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/>'
TABLE_WIDTH = 9638
DEFAULT_TEMPLATE = "07_REPORTS/docs/strategy/2027 Direction - Web Platform (Framework).docx"


def run(text, bold=False, italic=False, color=None, size=None, font=None):
    rpr = f'<w:rFonts w:ascii="{font}" w:cs="{font}" w:eastAsia="{font}" w:hAnsi="{font}"/>' if font else FONT
    if bold:
        rpr += "<w:b/><w:bCs/>"
    if italic:
        rpr += "<w:i/><w:iCs/>"
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    if size:
        rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    return f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


HL_COLORS = {"g": GREEN, "r": RED}
INLINE_RE = re.compile(r"(\[\[[gr]:[^\]]+\]\]|\*\*[^*\n]+\*\*|\*[^*\n]+\*|`[^`\n]+`)")


def runs(text, bold=False, italic=False, color=None, size=None, font=None):
    out = []
    for seg in INLINE_RE.split(text):
        if not seg:
            continue
        if seg.startswith("[[") and seg.endswith("]]") and len(seg) > 6:
            out.append(runs(seg[4:-2], True, italic, HL_COLORS[seg[2]], size, font))
        elif seg.startswith("**") and seg.endswith("**") and len(seg) > 4:
            out.append(runs(seg[2:-2], True, italic, color, size, font))
        elif seg.startswith("*") and seg.endswith("*") and len(seg) > 2:
            out.append(runs(seg[1:-1], bold, True, color, size, font))
        elif seg.startswith("`") and seg.endswith("`") and len(seg) > 2:
            out.append(run(seg[1:-1], bold, italic, color, size, font=font or "Consolas"))
        else:
            out.append(run(seg, bold, italic, color, size, font=font))
    return "".join(out)


def para(ppr, body):
    return f"<w:p {W_NS}><w:pPr>{ppr}</w:pPr>{body}</w:p>"


DARK = "2B1A24"
MUTED = "7A6470"
BAND = "F7EAF2"


def title(text):
    return para(
        f'<w:pStyle w:val="Title"/><w:pBdr><w:bottom w:val="single" w:color="{PINK}" w:sz="24" w:space="8"/></w:pBdr>'
        '<w:spacing w:after="280" w:before="0"/>',
        run(text),
    )


def cover(text, toc):
    """Trang bìa + mục lục tĩnh, kết thúc bằng ngắt trang."""
    parts = text.split(" - ")
    main, sub = (" - ".join(parts[:-1]), parts[-1]) if len(parts) > 1 else (text, "")
    out = [
        para('<w:spacing w:before="1800" w:after="120"/>', run("MOMO.VN  |  " + (sub or "WEB PLATFORM").upper(), bold=True, color=PINK, size=20)),
        para(
            f'<w:pBdr><w:left w:val="single" w:color="{PINK}" w:sz="48" w:space="14"/></w:pBdr>'
            '<w:spacing w:before="120" w:after="0" w:line="216" w:lineRule="auto"/><w:ind w:left="300"/>',
            run(main.upper(), bold=True, color=DARK, size=60),
        ),
        para(
            f'<w:pBdr><w:bottom w:val="single" w:color="{PINK}" w:sz="24" w:space="16"/></w:pBdr>'
            '<w:spacing w:before="0" w:after="600"/>',
            "",
        ),
    ]
    if toc:
        out.append(para('<w:spacing w:before="200" w:after="160"/>', run("NỘI DUNG", bold=True, color=PINK, size=20)))
        for lvl, t in toc:
            if lvl == 2:
                out.append(para('<w:spacing w:before="200" w:after="60"/>', run(t, bold=True, color=PINK, size=22)))
            else:
                out.append(para('<w:spacing w:before="0" w:after="20"/><w:ind w:left="360"/>', run(t, color=MUTED, size=19)))
    # ngắt trang do Heading 1 (pageBreakBefore) đảm nhận
    return out


def h1(text):
    return para(
        '<w:pStyle w:val="Heading1"/><w:pageBreakBefore/><w:keepNext/>'
        f'<w:pBdr><w:left w:val="single" w:color="{PINK}" w:sz="8" w:space="10"/></w:pBdr>'
        f'<w:shd w:fill="{PINK}" w:color="auto" w:val="clear"/><w:spacing w:after="240" w:before="0"/><w:ind w:left="140" w:right="0"/>',
        run(text, bold=True, color="FFFFFF", size=30),
    )


def h2(text):
    return para(
        '<w:pStyle w:val="Heading2"/><w:keepNext/>'
        f'<w:pBdr><w:left w:val="single" w:color="{PINK}" w:sz="30" w:space="8"/>'
        '<w:bottom w:val="single" w:color="E5C2D9" w:sz="4" w:space="4"/></w:pBdr>'
        '<w:spacing w:after="140" w:before="360"/><w:ind w:left="160"/>',
        run(text, bold=True, color=DARK, size=26),
    )


def h3(text):
    return para(
        f'<w:keepNext/><w:shd w:fill="{BAND}" w:color="auto" w:val="clear"/>'
        '<w:spacing w:after="100" w:before="240"/><w:ind w:left="0"/>',
        run(text, bold=True, color=PINK, size=22),
    )


def label(text):
    """Dòng chỉ có chữ đậm: nhãn mục con."""
    return para(
        '<w:keepNext/><w:spacing w:after="80" w:before="220"/>',
        run(text.rstrip(":"), bold=True, color=PINK, size=21),
    )


def callout(text):
    """Đoạn dài in đậm toàn bộ: hộp tóm tắt."""
    return para(
        f'<w:pBdr><w:top w:val="single" w:color="{BAND}" w:sz="4" w:space="8"/>'
        f'<w:left w:val="single" w:color="{PINK}" w:sz="36" w:space="10"/>'
        f'<w:bottom w:val="single" w:color="{BAND}" w:sz="4" w:space="8"/>'
        f'<w:right w:val="single" w:color="{BAND}" w:sz="4" w:space="10"/></w:pBdr>'
        f'<w:shd w:fill="{BAND}" w:color="auto" w:val="clear"/>'
        '<w:spacing w:after="240" w:before="80" w:line="300" w:lineRule="auto"/><w:ind w:left="220" w:right="220"/>',
        runs(text, color=DARK, size=22),
    )


BOLD_LINE_RE = re.compile(r"^\*\*([^*]+)\*\*:?$")


def normal(text):
    m = BOLD_LINE_RE.match(text)
    if m:
        return callout(m.group(1)) if len(m.group(1)) > 140 else label(m.group(1))
    return para('<w:spacing w:after="120" w:line="276" w:lineRule="auto"/>', runs(text))


def quote(text):
    return para(
        f'<w:pBdr><w:left w:val="single" w:color="{PINK}" w:sz="18" w:space="8"/></w:pBdr>'
        '<w:shd w:fill="FBF6F9" w:color="auto" w:val="clear"/><w:spacing w:after="100"/><w:ind w:left="240"/>',
        runs(text, italic=True),
    )


def bullet(text, level=0):
    return para(
        f'<w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="2"/></w:numPr>'
        '<w:spacing w:after="60"/>',
        runs(text),
    )


def numbered(n, text):
    return para(
        '<w:tabs><w:tab w:val="left" w:pos="720"/></w:tabs><w:spacing w:after="80"/><w:ind w:left="720" w:hanging="360"/>',
        run(f"{n}.\t", bold=True, color=PINK) + runs(text),
    )


def separator():
    return para(
        '<w:pBdr><w:bottom w:val="single" w:color="E5C2D9" w:sz="6" w:space="1"/></w:pBdr><w:spacing w:after="160" w:before="120"/>',
        "",
    )


def spacer():
    return para('<w:spacing w:after="60"/>', "")


def col_widths(header, rows):
    ncol = len(header)
    weights = []
    for j in range(ncol):
        cells = [header[j]] + [r[j] if j < len(r) else "" for r in rows]
        longest = max(len(c.replace("**", "")) for c in cells)
        weights.append(min(longest, 70) + 8)
    total = sum(weights)
    widths = [int(TABLE_WIDTH * w / total) for w in weights]
    widths[-1] += TABLE_WIDTH - sum(widths)
    return widths


NUM_RE = re.compile(r"^[\s*~+\-−]*[\d.,]+\s*(%|M|K|tỷ|triệu|đ)?[\s\d.,%MKtỷriệuđ()+\-−/a-zA-Z]*$")


def is_num(text):
    plain = text.replace("**", "").strip()
    return bool(plain) and len(plain) <= 22 and bool(NUM_RE.match(plain))


def cell(text, width, fill, bold=False, color=None, header=False, last=False, right=False):
    line = "E8D3E0" if not header else PINK
    bottom = f'<w:bottom w:val="single" w:color="{PINK if last else line}" w:sz="{8 if last else 4}"/>'
    borders = '<w:top w:val="nil"/><w:left w:val="nil"/><w:right w:val="nil"/>' + bottom
    mar = '<w:top w:type="dxa" w:w="80"/><w:left w:type="dxa" w:w="120"/><w:bottom w:type="dxa" w:w="80"/><w:right w:type="dxa" w:w="120"/>'
    align = '<w:jc w:val="right"/>' if right else ""
    return (
        f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{width}"/><w:tcBorders>{borders}</w:tcBorders>'
        f'<w:shd w:fill="{fill}" w:color="auto" w:val="clear"/><w:tcMar>{mar}</w:tcMar><w:vAlign w:val="center"/></w:tcPr>'
        f'<w:p><w:pPr>{"<w:keepNext/>" if header else ""}<w:spacing w:after="0" w:line="264" w:lineRule="auto"/>{align}</w:pPr>'
        f'{runs(text, bold=bold, color=color, size=18)}</w:p></w:tc>'
    )


TOTAL_RE = re.compile(r"^\**\s*(Tổng|Lũy kế|Total|Cộng)", re.I)


def table(header, rows):
    ncol = len(header)
    widths = col_widths(header, rows)
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    borders = "".join(f'<w:{s} w:val="nil"/>' for s in ("top", "left", "bottom", "right", "insideH", "insideV"))
    xml = [
        f'<w:tbl {W_NS}><w:tblPr><w:tblW w:type="dxa" w:w="{TABLE_WIDTH}"/><w:tblBorders>{borders}</w:tblBorders>'
        '<w:tblLayout w:type="fixed"/></w:tblPr>'
        f"<w:tblGrid>{grid}</w:tblGrid>"
    ]
    body = [(r + [""] * ncol)[:ncol] for r in rows]
    right = [
        j > 0 and all(is_num(r[j]) for r in body if r[j].replace("**", "").strip()) and any(r[j].strip() for r in body)
        for j in range(ncol)
    ]
    xml.append('<w:tr><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>')
    xml.extend(cell(header[j], widths[j], PINK, bold=True, color="FFFFFF", header=True, right=right[j]) for j in range(ncol))
    xml.append("</w:tr>")
    for i, r in enumerate(rows):
        r = (r + [""] * ncol)[:ncol]
        is_total = bool(TOTAL_RE.match(r[0]))
        last = i == len(rows) - 1
        fill = "F7E4EF" if is_total else ("FFFFFF" if i % 2 == 0 else "FCF7FA")
        xml.append('<w:tr><w:trPr><w:cantSplit/><w:tblHeader w:val="off"/></w:trPr>')
        xml.extend(
            cell(r[j], widths[j], fill, bold=is_total or j == 0, color=(PINK if is_total else (DARK if j == 0 else None)), last=last, right=right[j])
            for j in range(ncol)
        )
        xml.append("</w:tr>")
    xml.append("</w:tbl>")
    return "".join(xml)


def is_table_sep(line):
    return bool(re.match(r"^\s*\|[\s:|-]+\|\s*$", line))


def split_row(line):
    line = line.strip().strip("|")
    return [c.strip() for c in line.split("|")]


def codeblock(lines_buf):
    ppr = (
        '<w:pBdr><w:left w:val="single" w:color="DCC6D3" w:sz="12" w:space="8"/></w:pBdr>'
        '<w:shd w:fill="FBF6F9" w:color="auto" w:val="clear"/>'
        '<w:spacing w:after="120" w:before="80" w:line="240"/><w:ind w:left="180"/>'
    )
    parts = []
    for idx, ln in enumerate(lines_buf):
        if idx > 0:
            parts.append("<w:r><w:br/></w:r>")
        parts.append(run(ln, size=17, font="Courier New"))
    return para(ppr, "".join(parts))


def build(md_lines):
    out = []
    i = 0
    after_title = False
    toc = []
    for ln in md_lines:
        mm = re.match(r"^(#{2,3})\s+(.*)", ln.strip())
        if mm:
            toc.append((len(mm.group(1)), re.sub(r"\*\*|\*|`", "", mm.group(2))))
    while i < len(md_lines):
        raw = md_lines[i]
        s = raw.strip()
        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(md_lines) and not md_lines[i].strip().startswith("```"):
                buf.append(md_lines[i].rstrip())
                i += 1
            if i < len(md_lines) and md_lines[i].strip().startswith("```"):
                i += 1
            if buf:
                out.append(codeblock(buf))
            continue
        if s.startswith("|") and i + 1 < len(md_lines) and is_table_sep(md_lines[i + 1]):
            header = split_row(s)
            i += 2
            rows = []
            while i < len(md_lines) and md_lines[i].strip().startswith("|"):
                rows.append(split_row(md_lines[i]))
                i += 1
            out.append(table(header, rows))
            out.append(spacer())
            continue
        i += 1
        if not s:
            continue
        if s == "---":
            if after_title:
                out.append(separator())
                after_title = False
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            lvl = len(m.group(1))
            text = re.sub(r"\*\*|\*|`", "", m.group(2))
            if lvl == 1:
                out.extend(cover(text, toc))
            else:
                out.append({2: h1, 3: h2, 4: h3}[lvl](text))
            continue
        if s.startswith(">"):
            out.append(quote(s.lstrip(">").strip()))
            continue
        m = re.match(r"^(\s*)[-*]\s+(.*)", raw)
        if m:
            level = min(len(m.group(1).expandtabs(2)) // 2, 3)
            out.append(bullet(m.group(2), level))
            continue
        m = re.match(r"^(\d+)\.\s+(.*)", s)
        if m:
            out.append(numbered(int(m.group(1)), m.group(2)))
            continue
        out.append(normal(s))
    return out


def mark_highlights(lines, colors_path):
    """Bọc lần xuất hiện đầu tiên của mỗi cụm trong colors.json bằng [[g:..]] / [[r:..]]."""
    spec = json.loads(Path(colors_path).read_text(encoding="utf-8"))
    missing = []
    for key, tag in (("green", "g"), ("red", "r")):
        for phrase in spec.get(key, []):
            for idx, line in enumerate(lines):
                # bỏ qua dòng heading và phần đã được bọc
                if line.lstrip().startswith("#"):
                    continue
                plain = re.sub(r"\[\[[gr]:[^\]]+\]\]", lambda m: "\0" * len(m.group(0)), line)
                pos = plain.find(phrase)
                if pos >= 0:
                    lines[idx] = line[:pos] + f"[[{tag}:{phrase}]]" + line[pos + len(phrase):]
                    break
            else:
                missing.append(phrase)
    if missing:
        print("không tìm thấy:", missing)
    return lines


def convert(md_path, docx_path, template, colors=None):
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()
    if colors is None:
        sidecar = Path(md_path).with_suffix(".colors.json")
        colors = sidecar if sidecar.exists() else None
    if colors:
        lines = mark_highlights(lines, colors)
    doc = Document(template)
    body = doc.element.body
    for child in list(body):
        if not child.tag.endswith("}sectPr"):
            body.remove(child)
    sect = body[-1]
    for frag in build(lines):
        sect.addprevious(parse_xml(frag))
    doc.save(docx_path)
    print(f"saved: {docx_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("docx")
    ap.add_argument("--template", default=DEFAULT_TEMPLATE)
    ap.add_argument("--colors", help="JSON {green:[..], red:[..]}; mặc định dùng <md>.colors.json nếu có")
    a = ap.parse_args()
    convert(a.md, a.docx, a.template, a.colors)

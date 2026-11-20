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
DEFAULT_TEMPLATE = "07_REPORTS/docs/strategy/Budget 2027 - 2026 Reflection - Web Platform.docx"


def run(text, bold=False, italic=False, color=None, size=None):
    rpr = FONT
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


def runs(text, bold=False, italic=False, color=None, size=None):
    out = []
    for seg in re.split(r"(\*\*[^*]+\*\*|\[\[[gr]:[^\]]+\]\])", text):
        if not seg:
            continue
        if seg.startswith("[[") and seg.endswith("]]"):
            out.append(run(seg[4:-2], True, italic, HL_COLORS[seg[2]], size))
        elif seg.startswith("**") and seg.endswith("**") and len(seg) > 4:
            out.append(runs(seg[2:-2], True, italic, color, size))
        else:
            out.append(run(seg, bold, italic, color, size))
    return "".join(out)


def para(ppr, body):
    return f"<w:p {W_NS}><w:pPr>{ppr}</w:pPr>{body}</w:p>"


def title(text):
    return para(
        f'<w:pStyle w:val="Title"/><w:pBdr><w:bottom w:val="single" w:color="{PINK}" w:sz="24" w:space="8"/></w:pBdr>'
        '<w:spacing w:after="280" w:before="0"/>',
        run(text),
    )


def h1(text):
    return para(
        f'<w:pStyle w:val="Heading1"/><w:pBdr><w:left w:val="single" w:color="{PINK}" w:sz="36" w:space="8"/>'
        '<w:bottom w:val="single" w:color="E5C2D9" w:sz="6" w:space="4"/></w:pBdr>'
        '<w:shd w:fill="F7EAF2" w:color="auto" w:val="clear"/><w:spacing w:after="160" w:before="360"/><w:ind w:left="120"/>',
        run(text),
    )


def h2(text):
    return para('<w:pStyle w:val="Heading2"/>', run(text))


def h3(text):
    return para(
        '<w:pStyle w:val="Heading2"/><w:spacing w:after="80" w:before="200"/>',
        run(text, color=PINK, size=21),
    )


def normal(text):
    return para('<w:spacing w:after="100"/>', runs(text))


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


def cell(text, width, fill, bold=False, color=None):
    borders = "".join(
        f'<w:{s} w:val="single" w:color="DCC6D3" w:sz="4"/>' for s in ("top", "left", "bottom", "right")
    )
    mar = '<w:top w:type="dxa" w:w="70"/><w:left w:type="dxa" w:w="110"/><w:bottom w:type="dxa" w:w="70"/><w:right w:type="dxa" w:w="110"/>'
    return (
        f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{width}"/><w:tcBorders>{borders}</w:tcBorders>'
        f'<w:shd w:fill="{fill}" w:color="auto" w:val="clear"/><w:tcMar>{mar}</w:tcMar></w:tcPr>'
        f'<w:p><w:pPr><w:spacing w:after="0" w:line="260"/></w:pPr>{runs(text, bold=bold, color=color, size=18)}</w:p></w:tc>'
    )


TOTAL_RE = re.compile(r"^\**\s*(Tổng|Lũy kế|Total|Cộng)", re.I)


def table(header, rows):
    ncol = len(header)
    widths = col_widths(header, rows)
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    borders = "".join(
        f'<w:{s} w:val="single" w:color="auto" w:sz="4"/>'
        for s in ("top", "left", "bottom", "right", "insideH", "insideV")
    )
    xml = [
        f'<w:tbl {W_NS}><w:tblPr><w:tblW w:type="dxa" w:w="{TABLE_WIDTH}"/><w:tblBorders>{borders}</w:tblBorders></w:tblPr>'
        f"<w:tblGrid>{grid}</w:tblGrid>"
    ]
    xml.append('<w:tr><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>')
    xml.extend(cell(header[j], widths[j], "F3E1EE", bold=True, color=PINK) for j in range(ncol))
    xml.append("</w:tr>")
    for i, r in enumerate(rows):
        r = (r + [""] * ncol)[:ncol]
        is_total = bool(TOTAL_RE.match(r[0]))
        fill = "F1DCEA" if is_total else ("FFFFFF" if i % 2 == 0 else "FBF6F9")
        xml.append('<w:tr><w:trPr><w:cantSplit/><w:tblHeader w:val="off"/></w:trPr>')
        xml.extend(cell(r[j], widths[j], fill, bold=is_total) for j in range(ncol))
        xml.append("</w:tr>")
    xml.append("</w:tbl>")
    return "".join(xml)


def is_table_sep(line):
    return bool(re.match(r"^\s*\|[\s:|-]+\|\s*$", line))


def split_row(line):
    line = line.strip().strip("|")
    return [c.strip() for c in line.split("|")]


def build(md_lines):
    out = []
    i = 0
    num = 0
    after_title = False
    while i < len(md_lines):
        raw = md_lines[i]
        s = raw.strip()
        if s.startswith("|") and i + 1 < len(md_lines) and is_table_sep(md_lines[i + 1]):
            header = split_row(s)
            i += 2
            rows = []
            while i < len(md_lines) and md_lines[i].strip().startswith("|"):
                rows.append(split_row(md_lines[i]))
                i += 1
            out.append(table(header, rows))
            out.append(spacer())
            num = 0
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
            lvl, text = len(m.group(1)), m.group(2).replace("**", "")
            out.append({1: title, 2: h1, 3: h2, 4: h3}[lvl](text))
            after_title = lvl == 1
            num = 0
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
        num = 0
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

#!/usr/bin/env python3
"""Convert a markdown file to .docx using python-docx (headings, tables, lists, bold)."""
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


def add_runs(par, text):
    """Add text to paragraph handling **bold** segments."""
    for seg in re.split(r"(\*\*[^*]+\*\*)", text):
        if not seg:
            continue
        if seg.startswith("**") and seg.endswith("**"):
            r = par.add_run(seg[2:-2])
            r.bold = True
        else:
            par.add_run(seg)


def is_table_sep(line):
    return bool(re.match(r"^\s*\|[\s:|-]+\|\s*$", line))


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def convert(md_path, docx_path):
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10.5)

    i = 0
    in_list = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # table block
        if stripped.startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            header = split_row(stripped)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            table = doc.add_table(rows=1 + len(rows), cols=len(header))
            table.style = "Table Grid"
            for j, h in enumerate(header):
                cell = table.rows[0].cells[j]
                cell.text = ""
                add_runs(cell.paragraphs[0], h)
                for r in cell.paragraphs[0].runs:
                    r.bold = True
            for ri, row in enumerate(rows):
                for j in range(min(len(row), len(header))):
                    cell = table.rows[ri + 1].cells[j]
                    cell.text = ""
                    add_runs(cell.paragraphs[0], row[j])
            doc.add_paragraph()
            continue

        if not stripped:
            i += 1
            continue
        if stripped == "---":
            i += 1
            continue

        if stripped.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            add_runs(p, stripped.lstrip(">").strip())
            for r in p.runs:
                r.italic = True
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)", stripped)
        if m:
            level = len(m.group(1))
            doc.add_heading("", level=min(level, 4))
            p = doc.paragraphs[-1]
            p.text = ""
            add_runs(p, m.group(2))
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, re.sub(r"^[-*]\s+", "", stripped))
            i += 1
            continue

        if re.match(r"^\d+\.\s+", stripped):
            p = doc.add_paragraph(style="List Number")
            add_runs(p, re.sub(r"^\d+\.\s+", "", stripped))
            i += 1
            continue

        p = doc.add_paragraph()
        add_runs(p, stripped)
        i += 1

    doc.save(docx_path)
    print(f"saved: {docx_path}")


if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])

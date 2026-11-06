"""Parse Tasklist export (markdown table hoac xlsx) -> ghi vao 12_TASK_MANAGEMENT/<thang>/week_0X.md.

Input md: bang 5 cot chuan:
  | Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
Input xlsx: sheet dau tien, header giong tren.

ghi de week file tuong ung (week param hoac suy tu header ngay).
"""

import glob
import os
import re
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TASK_ROOT = os.path.join(BASE_DIR, "12_TASK_MANAGEMENT")

HEADER_LINE = (
    "| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |\n"
    "| :--- | :--- | :--- | :--- | :---: |"
)


def _parse_md(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    table_rows = []
    in_table = False
    for line in lines:
        if "Hạng mục Công việc" in line and "Trạng thái" in line:
            in_table = True
            continue
        if in_table:
            s = line.strip()
            if s.startswith("|") and not re.match(r"^\|[\s:-]+\|", s):
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) >= 5:
                    status = cells[4].replace("`", "").strip() or "To Do"
                    table_rows.append((cells[0], cells[1], cells[2], cells[3], status))
            elif s.startswith("###") or s.startswith("##"):
                break
    return table_rows


def _parse_xlsx(path):
    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    if not rows:
        return []
    header = [str(c or "").strip().lower() for c in rows[0]]
    # Van de header xlsx co the khac, chi can co du 5 cot
    table_rows = []
    for r in rows[1:]:
        if not r or not r[0]:
            continue
        cells = [str(c or "").strip() for c in r[:5]]
        while len(cells) < 5:
            cells.append("")
        status = cells[4].replace("`", "").strip() or "To Do"
        table_rows.append((cells[0], cells[1], cells[2], cells[3], status))
    return table_rows


def _find_target_week(week_hint=None):
    """Tra ve (thu_muc_thang, duong_dan_file_week)."""
    month_dirs = sorted(glob.glob(os.path.join(TASK_ROOT, "????-??")))
    if not month_dirs:
        now = datetime.now()
        month_dir = os.path.join(TASK_ROOT, now.strftime("%Y-%m"))
        os.makedirs(month_dir, exist_ok=True)
    else:
        month_dir = month_dirs[-1]

    week_files = sorted(glob.glob(os.path.join(month_dir, "week_*.md")))
    if week_hint:
        target = os.path.join(month_dir, f"week_{int(week_hint):02d}.md")
        return month_dir, target
    if week_files:
        return month_dir, week_files[-1]
    now = datetime.now()
    target = os.path.join(month_dir, f"week_{((now.day - 1) // 7) + 1:02d}.md")
    return month_dir, target


def parse(file_path, week=None, overwrite=False):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".md":
        rows = _parse_md(file_path)
    elif ext == ".xlsx":
        rows = _parse_xlsx(file_path)
    else:
        raise RuntimeError(f"Tasklist parser khong ho tro dinh dang {ext}")

    if not rows:
        raise RuntimeError("Khong trich duoc task nao tu file.")

    month_dir, target = _find_target_week(week)
    if os.path.exists(target) and not overwrite:
        raise RuntimeError(
            f"Target {target} da ton tai. Dung --overwrite de ghi de, hoac chon --week khac."
        )
    week_no = int(re.search(r"week_(\d+)", target).group(1))

    content = [
        f"# KẾ HOẠCH & QUẢN LÝ ĐẦU VIỆC TUẦN {week_no} (sync từ intake)",
        "",
        "> **Lead Quản trị chung:** Hiến (Nắm overall các dự án, tham gia linh hoạt, không gán task cụ thể)",
        f"> **Cập nhật:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "> **Nguồn:** intake parser (drop file)",
        "",
        "---",
        "",
        "## I. TASKLIST",
        "",
        HEADER_LINE,
    ]
    for title, desc, pic, coord, status in rows:
        safe_status = status if status in ("To Do", "In Progress", "Done", "Blocked") else "To Do"
        content.append(f"| {title} | {desc} | {pic} | {coord} | `{safe_status}` |")
    content.append("")

    os.makedirs(month_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print(f"Da ghi {len(rows)} task vao {target}")
    return {"parser": "tasks", "source": file_path, "tasks": len(rows), "target": target}

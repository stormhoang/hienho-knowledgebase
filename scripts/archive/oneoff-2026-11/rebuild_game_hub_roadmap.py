import openpyxl
import xlsxwriter
from openpyxl.utils import get_column_letter

src_path = '05_HUBS/game-hub-roadmap.xlsx'
backup_path = '/tmp/game-hub-roadmap-openpyxl-backup.xlsx'
dst_path = '05_HUBS/game-hub-roadmap.xlsx'

# Backup current file first
import shutil
shutil.copyfile(src_path, backup_path)

src_wb = openpyxl.load_workbook(backup_path, data_only=False)
dst_wb = xlsxwriter.Workbook(dst_path, {'constant_memory': False})

def rgb_to_hex(color):
    if not color:
        return None
    rgb = getattr(color, 'rgb', None)
    if not rgb:
        return None
    rgb_str = str(rgb)
    if len(rgb_str) == 8:
        # AARRGGBB -> #RRGGBB
        return '#' + rgb_str[2:]
    elif len(rgb_str) == 6:
        return '#' + rgb_str
    return None

format_cache = {}

def get_format(dst_wb, cell):
    font = cell.font
    fill = cell.fill
    alignment = cell.alignment
    border = cell.border
    num_fmt = cell.number_format

    bold = font.bold if font else False
    italic = font.italic if font else False
    font_size = font.size if font and font.size else 10
    font_name = 'Arial'  # Clean, cross-platform font fully supported on Mac & Windows
    font_color = rgb_to_hex(font.color) if font else None

    bg_color = None
    if fill and fill.fill_type == 'solid':
        bg_color = rgb_to_hex(fill.start_color)

    align_h = alignment.horizontal if alignment else None
    align_v = alignment.vertical if alignment else None
    wrap = alignment.wrap_text if alignment else False

    has_border = False
    if border and (border.left.style or border.right.style or border.top.style or border.bottom.style):
        has_border = True

    key = (bold, italic, font_size, font_name, font_color, bg_color, align_h, align_v, wrap, has_border, num_fmt)
    if key in format_cache:
        return format_cache[key]

    props = {
        'font_name': font_name,
        'font_size': font_size,
        'bold': bold,
        'italic': italic,
    }
    if font_color:
        props['font_color'] = font_color
    if bg_color and bg_color.lower() != '#000000':
        props['bg_color'] = bg_color
    if align_h:
        props['align'] = align_h
    if align_v:
        props['valign'] = align_v
    if wrap:
        props['text_wrap'] = True
    if has_border:
        props['border'] = 1
        props['border_color'] = '#CBD5E1'
    if num_fmt and num_fmt != 'General':
        props['num_format'] = num_fmt

    fmt = dst_wb.add_format(props)
    format_cache[key] = fmt
    return fmt

for sheet_name in src_wb.sheetnames:
    src_ws = src_wb[sheet_name]
    dst_ws = dst_wb.add_worksheet(sheet_name)

    # Column widths
    for col_letter, col_dim in src_ws.column_dimensions.items():
        if col_dim.width:
            col_idx = openpyxl.utils.column_index_from_string(col_letter) - 1
            dst_ws.set_column(col_idx, col_idx, col_dim.width)

    # Track merged top-left cells
    merged_map = {}
    for rng in src_ws.merged_cells.ranges:
        min_col, min_row, max_col, max_row = rng.min_col - 1, rng.min_row - 1, rng.max_col - 1, rng.max_row - 1
        merged_map[(min_row, min_col)] = (max_row, max_col)

    # Cells
    for r in range(1, src_ws.max_row + 1):
        row_dim = src_ws.row_dimensions.get(r)
        if row_dim and row_dim.height:
            dst_ws.set_row(r - 1, row_dim.height)

        for c in range(1, src_ws.max_column + 1):
            cell = src_ws.cell(r, c)
            r_idx = r - 1
            c_idx = c - 1

            # Check if this cell is inside a merged range (not top-left)
            is_subsumed = False
            for (m_min_r, m_min_c), (m_max_r, m_max_c) in merged_map.items():
                if m_min_r <= r_idx <= m_max_r and m_min_c <= c_idx <= m_max_c:
                    if (r_idx, c_idx) != (m_min_r, m_min_c):
                        is_subsumed = True
                    break

            if is_subsumed:
                continue

            val = cell.value
            fmt = get_format(dst_wb, cell)

            if (r_idx, c_idx) in merged_map:
                m_max_r, m_max_c = merged_map[(r_idx, c_idx)]
                if val is not None:
                    dst_ws.merge_range(r_idx, c_idx, m_max_r, m_max_c, val, fmt)
                else:
                    dst_ws.merge_range(r_idx, c_idx, m_max_r, m_max_c, '', fmt)
            else:
                if val is not None:
                    if isinstance(val, (int, float)):
                        dst_ws.write_number(r_idx, c_idx, val, fmt)
                    else:
                        dst_ws.write(r_idx, c_idx, str(val), fmt)
                else:
                    if fmt:
                        dst_ws.write_blank(r_idx, c_idx, None, fmt)

dst_wb.close()
print("Rebuilt successfully with pure xlsxwriter -> 05_HUBS/game-hub-roadmap.xlsx")

"""Signature registry: nhận diện format file drop vào intake zone.

Chiến lược deterministic (không dùng LLM):
- Quét top-down, file match rule đầu tiên dừng.
- Dùng combination của: đuôi file, tên file, và header/sheet content (đọc thử).
"""

import csv
import os
import zipfile


TRACKING = "tracking"
CRAWL = "crawl_stats"
BACKLINK = "backlink"
UNKNOWN = "unknown"


def _peek_csv_header(path, max_rows=3):
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                if i >= max_rows:
                    break
                rows.append([c.strip().lower() for c in row])
            return rows
    except Exception:
        return []


def _peek_xlsx_sheets(path):
    try:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        names = list(wb.sheetnames)
        wb.close()
        return names
    except Exception:
        return []


def _is_zip(path):
    return zipfile.is_zipfile(path)


def _zip_contains(path, *keywords):
    if not _is_zip(path):
        return False
    try:
        with zipfile.ZipFile(path) as zf:
            names = [n.lower() for n in zf.namelist()]
        return any(all(k.lower() in n for k in keywords) for n in names)
    except Exception:
        return False


def detect(path):
    """Trả về format id (TRACKING/CRAWL/BACKLINK/UNKNOWN)."""
    name = os.path.basename(path).lower()
    ext = os.path.splitext(name)[1].lower()

    # 1. Tracking xlsx (sheet MTD Pivot)
    if ext == ".xlsx":
        sheets = [s.lower() for s in _peek_xlsx_sheets(path)]
        if "mtd pivot" in sheets and "full month pivot" in sheets:
            return TRACKING
        if any("crawl" in s for s in sheets):
            return CRAWL

    # 2. Crawl stats (zip gsc export)
    if ext == ".zip" and _zip_contains(path, "crawl"):
        return CRAWL
    if "crawl" in name and ext in (".csv", ".tsv"):
        return CRAWL

    # 3. Backlink CSV
    if ext == ".csv":
        header_rows = _peek_csv_header(path, 1)
        if header_rows:
            h = header_rows[0]
            if any("linking pages" in c for c in h) and any(c in ("site", "domain", "source") for c in h):
                return BACKLINK

    # 4. Fallback theo tên file (tracking xlsx không đọc được sheet)
    if ext == ".xlsx" and ("tracking" in name or "performance" in name):
        return TRACKING

    return UNKNOWN

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC PROJECTS DETAIL FLOW CLICKS TO GOOGLE SHEETS
Cập nhật dòng 'Click [Project Name]' (màu xám #F1F3F4) xen kẽ ngay bên dưới mỗi dự án
trong sheet 'Projects Detail Flow' trên Google Sheets SSOT.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.rebuild_projects_detail_flow_v3 import run as sync_google_sheet_clicks

if __name__ == "__main__":
    sync_google_sheet_clicks()

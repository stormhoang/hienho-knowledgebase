#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REBUILD PROJECTS DETAIL FLOW (REDIRECT TO V3 SSOT)
Chuyển hướng toàn bộ các lệnh gọi sang scripts/rebuild_projects_detail_flow_v3.py
để đảm bảo tính toàn vẹn SSOT và tránh ghi đè lỗi #REF! lên Google Sheets.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.rebuild_projects_detail_flow_v3 import run, build_grid

if __name__ == "__main__":
    run()

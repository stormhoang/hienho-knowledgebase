"""Cổng ghi duy nhất từ KB sang /dashboard của repo Hubs.

lib/dashboard/web-data.json chỉ có một writer: scripts/build-dashboard-data.py trong repo Hubs.
Script KB muốn bổ sung một khối dữ liệu thì ghi patch qua write_patch(), rồi gọi rebuild_dashboard().
Build đọc patch trong 07_REPORTS/data/dashboard_patches/ và gộp vào web-data.json.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PATCH_DIR = BASE_DIR / "07_REPORTS" / "data" / "dashboard_patches"

HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
if not HUBS_REPO.exists():
    HUBS_REPO = Path("/Users/hienhv/Klaus/Web-Idea/react-web-momo")

# Khóa build chấp nhận từ patch. Thêm khóa mới thì thêm cả ở PATCH_KEYS trong build-dashboard-data.py.
PATCH_KEYS = {"performance7d", "breakoutPages7d"}


def write_patch(key, value):
    if key not in PATCH_KEYS:
        raise ValueError(f"Khóa patch '{key}' chưa được whitelist: {sorted(PATCH_KEYS)}")
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    path = PATCH_DIR / f"{key}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
    print(f"Đã ghi patch dashboard: {path}")
    return path


def rebuild_dashboard():
    build = HUBS_REPO / "scripts" / "build-dashboard-data.py"
    res = subprocess.run([sys.executable, str(build), "--base", str(BASE_DIR)], cwd=HUBS_REPO)
    if res.returncode != 0:
        print(f"⚠ build-dashboard-data.py lỗi (exit {res.returncode})")
        return False
    return True

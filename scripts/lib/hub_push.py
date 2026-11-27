#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HUB PUSH HELPER - commit + push file du lieu sang repo react-web-momo.

Gom logic git add/commit/push bi duplicate giua cac ingest script
(ingest_ga4_daily, ingest_gsc_mtd). Khi `git push` that bai (firewall
van phong chan git-receive-pack), tu dong fallback sang push_to_hubs_api.py
(day du lieu qua GitHub REST API, chi upload file thuoc ALLOWED_DATA_PREFIXES).

Cach dung:
    from scripts.lib.hub_push import commit_and_push_hub
    ok = commit_and_push_hub(hub_repo, ["data/analytics/page_mtd.json"], "data(gsc): ...")
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
API_SCRIPT = BASE_DIR / "scripts" / "push_to_hubs_api.py"


def commit_and_push_hub(hub_repo, commit_files, commit_msg, api_fallback=True):
    """git add + commit + push origin main cho hub_repo.

    Tra ve True neu du lieu da len remote (git push hoac REST API).
    File da commit local nhung push fail ca 2 duong -> tra ve False (commit
    van nam tren local HEAD, co the day sau bang push_to_hubs_api.py).
    """
    hub_repo = Path(hub_repo)
    if not hub_repo.exists():
        print(f"  ⚠ Không tìm thấy hub repo {hub_repo}")
        return False
    try:
        subprocess.run(["git", "-C", str(hub_repo), "add"] + commit_files, check=True)
        diff_chk = subprocess.run(
            ["git", "-C", str(hub_repo), "diff", "--cached", "--quiet"]
        )
        if diff_chk.returncode == 0:
            print("  ✓ Dữ liệu trên Hubs repo đã ở trạng thái mới nhất, không có commit mới.")
            return True
        subprocess.run(["git", "-C", str(hub_repo), "commit", "-m", commit_msg], check=True)
        push_res = subprocess.run(
            ["git", "-C", str(hub_repo), "push", "origin", "main"],
            capture_output=True, text=True,
        )
        if push_res.returncode == 0:
            print("  ✓ Đã commit và push trực tiếp sang GitHub vanhien26/hubs-momo:main")
            return True
        print(f"  ⚠ git push thất bại: {push_res.stderr.strip()[:300]}")
        if not api_fallback:
            return False
        if not API_SCRIPT.exists():
            print("  ⚠ Không tìm thấy push_to_hubs_api.py - bỏ qua fallback REST API")
            return False
        print("  → Thử fallback REST API (push_to_hubs_api.py)...")
        api_res = subprocess.run(
            [sys.executable, str(API_SCRIPT), "--message", commit_msg],
            capture_output=True, text=True,
        )
        tail = ((api_res.stdout or "") + (api_res.stderr or "")).strip()
        if tail:
            print("\n".join("  " + line for line in tail.splitlines()[-15:]))
        if api_res.returncode == 0:
            print("  ✓ Đã đẩy dữ liệu lên GitHub qua REST API (firewall bypass)")
            return True
        print(f"  ⚠ REST API fallback cũng thất bại (exit {api_res.returncode})")
        return False
    except Exception as ge:
        print(f"  ⚠ Lỗi commit/push Hubs: {ge}")
        return False

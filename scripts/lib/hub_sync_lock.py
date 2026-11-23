#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HUB SYNC MUTEX LOCK
Chống chạy song song các pipeline đồng bộ dữ liệu sang react-web-momo / hubs-momo.

Bối cảnh: nhiều script (sync_ga4_master, sync_7d_performance_report, sync_hybrid_report,
sync_data_to_hubs_dashboard, sync_all_data) cùng ghi vào clone local react-web-momo
các file JSON SSOT (summary.json, web-data.json, gsc_7d_performance.json...).
Chạy song song gây last-writer-wins: file cuối ghi đè, dashboard hiển thị số liệu
trộn 2 thời điểm snapshot khác nhau mà không báo lỗi.

Cách dùng:
    from scripts.lib.hub_sync_lock import hub_sync_lock
    ...
    with hub_sync_lock("sync_ga4_master"):
        main()

Cơ chế:
- Lock file: 07_REPORTS/data/cache/hub_sync.lock (thư mục cache đã gitignore).
- Chứa JSON {owner, pid, token, started_at}. Token (uuid) tránh xóa nhầm lock
  của process khác sau khi takeover lock hết hạn.
- TTL mặc định 2 giờ (sync_all_data chạy nhiều step có thể lâu). Lock cũ hơn TTL
  bị coi là stale (process chết giữa chừng / kill -9) và bị chiếm lại.
- Process bị kill -9 để lại lock stale: tự hết hạn sau TTL, hoặc xóa tay file lock.
"""

import json
import os
import sys
import time
import uuid
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LOCK_PATH = REPO_ROOT / "07_REPORTS" / "data" / "cache" / "hub_sync.lock"
DEFAULT_TTL_SECONDS = 2 * 60 * 60  # 2 giờ


def _read_lock():
    try:
        with open(LOCK_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _lock_age_seconds(info):
    try:
        started = datetime.fromisoformat(info.get("started_at", ""))
        return (datetime.now() - started).total_seconds()
    except Exception:
        return float("inf")  # không parse được timestamp -> coi như stale


def acquire(owner: str, ttl_seconds: int = DEFAULT_TTL_SECONDS):
    """Chiếm lock. Thất bại (đang có sync khác chạy) -> sys.exit(2)."""
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = _read_lock()
    if existing:
        age = _lock_age_seconds(existing)
        if age < ttl_seconds:
            started = existing.get("started_at", "?")
            print("=" * 70)
            print("[HUB SYNC LOCK] Đang có tiến trình đồng bộ Hub khác chạy:")
            print(f"  Owner   : {existing.get('owner', '?')} (pid {existing.get('pid', '?')})")
            print(f"  Bắt đầu: {started}")
            print(f"  Tuổi lock: {age / 60:.0f} phút (TTL {ttl_seconds / 60:.0f} phút)")
            print("=> Từ chối chạy để tránh last-writer-wins trên JSON SSOT của Hub.")
            print("   Chờ tiến trình kia xong, hoặc xóa tay:", LOCK_PATH)
            print("=" * 70)
            sys.exit(2)
        print(f"[HUB SYNC LOCK] Lock cũ của '{existing.get('owner', '?')}' đã stale "
              f"({age / 60:.0f} phút > TTL), chiếm lại.")

    token = uuid.uuid4().hex[:12]
    info = {
        "owner": owner,
        "pid": os.getpid(),
        "token": token,
        "started_at": datetime.now().isoformat(timespec="seconds"),
    }
    tmp = LOCK_PATH.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False)
    os.replace(tmp, LOCK_PATH)  # atomic
    print(f"[HUB SYNC LOCK] Đã khóa bởi '{owner}' (pid {os.getpid()}, token {token})")
    return token


def release(token: str):
    """Nhả lock nếu token khớp (tránh xóa lock của process đã takeover)."""
    existing = _read_lock()
    if existing and existing.get("token") == token:
        try:
            LOCK_PATH.unlink()
            print("[HUB SYNC LOCK] Đã nhả khóa.")
        except FileNotFoundError:
            pass


@contextmanager
def hub_sync_lock(owner: str, ttl_seconds: int = DEFAULT_TTL_SECONDS):
    token = acquire(owner, ttl_seconds)
    try:
        yield
    finally:
        release(token)

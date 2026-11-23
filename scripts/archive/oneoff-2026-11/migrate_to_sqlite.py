#!/usr/bin/env python3
"""
MIGRATION SCRIPT: FLAT JSON -> SQLITE
Chuyển đổi toàn bộ dữ liệu hiệu suất GSC và GA4 từ các file JSON phẳng khổng lồ
vào cơ sở dữ liệu SQLite hiệu năng cao (07_REPORTS/data/performance.sqlite).
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# Đảm bảo import được repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
from scripts.lib.db import get_connection, init_db, DEFAULT_DB_PATH, DATA_DIR


def clean_query(val: str) -> str:
    """Loại bỏ artifact Excel =\"...\" nếu có."""
    if not val:
        return ""
    val = val.strip()
    if val.startswith('="') and val.endswith('"'):
        return val[2:-1].strip()
    if val.startswith('"') and val.endswith('"'):
        return val[1:-1].strip()
    return val


def migrate_gsc_30d_cache(conn) -> int:
    cache_file = DATA_DIR / "cache" / "gsc_30d_cache.json"
    if not cache_file.exists():
        cache_file = DATA_DIR / "gsc_30d_cache.json"
    if not cache_file.exists():
        print(f"[SKIP] Không tìm thấy gsc_30d_cache.json")
        return 0

    print(f"\n[1/3] Đang nạp {cache_file.name} ({cache_file.stat().st_size / (1024*1024):.1f} MB)...")
    start = time.time()
    with open(cache_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"  -> Đã đọc {len(data):,} bản ghi trong {time.time() - start:.2f}s")

    synced_at = datetime.utcnow().isoformat()
    rows_to_insert = []
    for item in data:
        keys = item.get("keys", [])
        if len(keys) < 2:
            continue
        page_url = keys[0]
        query = clean_query(keys[1])
        if not page_url or not query:
            continue
        clicks = int(item.get("clicks", 0))
        impressions = int(item.get("impressions", 0))
        ctr = float(item.get("ctr", 0.0))
        position = float(item.get("position", 0.0))
        rows_to_insert.append((page_url, query, clicks, impressions, ctr, position, synced_at))

    print(f"  -> Đang ghi {len(rows_to_insert):,} bản ghi vào SQLite...")
    t_insert = time.time()
    with conn:
        conn.executemany("""
            INSERT OR REPLACE INTO gsc_search_analytics 
            (page_url, query, clicks, impressions, ctr, position, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, rows_to_insert)
    print(f"  -> Hoàn thành ghi SQLite trong {time.time() - t_insert:.2f}s")
    return len(rows_to_insert)


def migrate_ga4_landing_pages(conn) -> int:
    ga4_file = DATA_DIR / "ga4" / "landing-pages.json"
    if not ga4_file.exists():
        print(f"[SKIP] Không tìm thấy {ga4_file}")
        return 0

    print(f"\n[2/3] Đang nạp {ga4_file.name} ({ga4_file.stat().st_size / (1024*1024):.1f} MB)...")
    start = time.time()
    with open(ga4_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    rows = data.get("rows", [])
    print(f"  -> Đã đọc {len(rows):,} bản ghi trong {time.time() - start:.2f}s")

    synced_at = datetime.utcnow().isoformat()
    rows_to_insert = []
    for r in rows:
        landing_page = r.get("landing_page", "").strip()
        if not landing_page:
            continue
        channel = r.get("channel_group", "")
        source = r.get("source", "")
        sessions = int(r.get("sessions", 0))
        engaged = int(r.get("engaged_sessions", 0))
        track1 = int(r.get("onelink_clicks_track1", 0))
        track2 = int(r.get("onelink_clicks_track2", 0))
        rows_to_insert.append((landing_page, channel, source, sessions, engaged, track1, track2, synced_at))

    print(f"  -> Đang ghi {len(rows_to_insert):,} bản ghi vào SQLite...")
    t_insert = time.time()
    with conn:
        conn.executemany("""
            INSERT OR REPLACE INTO ga4_landing_pages 
            (landing_page, channel_group, source, sessions, engaged_sessions,
             onelink_clicks_track1, onelink_clicks_track2, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, rows_to_insert)
    print(f"  -> Hoàn thành ghi SQLite trong {time.time() - t_insert:.2f}s")
    return len(rows_to_insert)


def migrate_gsc_keyword_ranking(conn) -> int:
    ranking_file = DATA_DIR / "cache" / "gsc_keyword_ranking.json"
    if not ranking_file.exists():
        ranking_file = DATA_DIR / "gsc_keyword_ranking.json"
    if not ranking_file.exists():
        print(f"[SKIP] Không tìm thấy gsc_keyword_ranking.json")
        return 0

    print(f"\n[3/3] Đang nạp {ranking_file.name} ({ranking_file.stat().st_size / (1024*1024):.1f} MB)...")
    start = time.time()
    with open(ranking_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    keywords = data.get("keywords", [])
    print(f"  -> Đã đọc {len(keywords):,} từ khóa trong {time.time() - start:.2f}s")

    synced_at = data.get("generated_at", datetime.utcnow().isoformat())
    rows_to_insert = []
    for item in keywords:
        raw_query = item.get("query", "")
        query = clean_query(raw_query)
        if not query:
            continue
        clicks = int(item.get("clicks", 0))
        impressions = int(item.get("impressions", 0))
        position = float(item.get("position", 0.0))
        rounded_pos = int(item.get("rounded_position", 0))
        opp_score = float(item.get("opportunity_score", 0.0))
        rows_to_insert.append((query, clicks, impressions, position, rounded_pos, opp_score, synced_at))

    print(f"  -> Đang ghi {len(rows_to_insert):,} bản ghi vào SQLite...")
    t_insert = time.time()
    with conn:
        conn.executemany("""
            INSERT OR REPLACE INTO gsc_keyword_ranking 
            (query, clicks, impressions, position, rounded_position, opportunity_score, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, rows_to_insert)
    print(f"  -> Hoàn thành ghi SQLite trong {time.time() - t_insert:.2f}s")
    return len(rows_to_insert)


def benchmark_test(conn):
    print("\n=== ĐO LƯỜNG TỐC ĐỘ TRUY VẤN (BENCHMARK) ===")
    test_queries = ["momo", "nạp xu tiktok", "vay tiền", "vé xem phim", "giá vàng hôm nay"]
    cur = conn.cursor()
    for q in test_queries:
        t0 = time.time()
        cur.execute("""
            SELECT page_url, query, clicks, impressions, ctr, position 
            FROM gsc_search_analytics 
            WHERE query = ? 
            ORDER BY clicks DESC LIMIT 5;
        """, (q,))
        res = cur.fetchall()
        elapsed_ms = (time.time() - t0) * 1000
        print(f"Query '{q}': {len(res)} URLs tìm thấy | Thời gian: {elapsed_ms:.2f} ms")


def main():
    print("=== BẮT ĐẦU CHUYỂN ĐỔI DỮ LIỆU SANG SQLITE ===")
    init_db()
    conn = get_connection()

    total_gsc = migrate_gsc_30d_cache(conn)
    total_ga4 = migrate_ga4_landing_pages(conn)
    total_rank = migrate_gsc_keyword_ranking(conn)

    benchmark_test(conn)

    # Thống kê dung lượng file DB
    db_size_mb = DEFAULT_DB_PATH.stat().st_size / (1024 * 1024)
    print("\n=== KẾT QUẢ TỔNG HỢP ===")
    print(f"- File SQLite: {DEFAULT_DB_PATH}")
    print(f"- Dung lượng SQLite: {db_size_mb:.2f} MB")
    print(f"- Tổng bản ghi GSC Search Analytics: {total_gsc:,}")
    print(f"- Tổng bản ghi GA4 Landing Pages: {total_ga4:,}")
    print(f"- Tổng từ khóa GSC Keyword Ranking: {total_rank:,}")
    print("[SUCCESS] Hoàn tất di chuyển dữ liệu sang SQLite!\n")
    conn.close()


if __name__ == "__main__":
    main()

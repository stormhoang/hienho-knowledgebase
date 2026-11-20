"""
MoMo Web Platform - SQLite Database Layer SSOT
Quản lý tập trung dữ liệu hiệu suất Google Search Console (GSC) và Google Analytics 4 (GA4).
Tối ưu hóa:
- Zero dependency (dùng built-in sqlite3 của Python)
- Portable: đường dẫn tương đối, chạy được trên mọi máy
- O(1) query latency nhờ B-Tree Indexing trên (page_url, query)
- WAL Mode: Đọc ghi đồng thời hiệu năng cao
"""

import os
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "07_REPORTS" / "data"
CACHE_DIR = DATA_DIR / "cache"
DEFAULT_DB_PATH = CACHE_DIR / "performance.sqlite" if (CACHE_DIR / "performance.sqlite").exists() else DATA_DIR / "performance.sqlite"


def get_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Khởi tạo kết nối SQLite với cấu hình hiệu năng cao."""
    path = db_path or DEFAULT_DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    # Tối ưu WAL mode và Cache size
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA cache_size = -64000;")  # 64MB cache
    return conn


def init_db(db_path: Optional[Path] = None) -> None:
    """Tạo bảng và các chỉ mục (Indexes) nếu chưa tồn tại."""
    conn = get_connection(db_path)
    with conn:
        # 1. Bảng Search Console Analytics (GSC Raw & Filtered)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS gsc_search_analytics (
                page_url TEXT NOT NULL,
                query TEXT NOT NULL,
                clicks INTEGER NOT NULL DEFAULT 0,
                impressions INTEGER NOT NULL DEFAULT 0,
                ctr REAL NOT NULL DEFAULT 0.0,
                position REAL NOT NULL DEFAULT 0.0,
                synced_at TEXT,
                PRIMARY KEY (page_url, query)
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_query ON gsc_search_analytics(query);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_page ON gsc_search_analytics(page_url);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_clicks ON gsc_search_analytics(clicks DESC);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_impressions ON gsc_search_analytics(impressions DESC);")

        # 2. Bảng GA4 Landing Pages & W2A Funnel
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ga4_landing_pages (
                landing_page TEXT NOT NULL,
                channel_group TEXT NOT NULL DEFAULT '',
                source TEXT NOT NULL DEFAULT '',
                sessions INTEGER NOT NULL DEFAULT 0,
                engaged_sessions INTEGER NOT NULL DEFAULT 0,
                onelink_clicks_track1 INTEGER NOT NULL DEFAULT 0,
                onelink_clicks_track2 INTEGER NOT NULL DEFAULT 0,
                synced_at TEXT,
                PRIMARY KEY (landing_page, channel_group, source)
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ga4_page ON ga4_landing_pages(landing_page);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ga4_sessions ON ga4_landing_pages(sessions DESC);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ga4_channel ON ga4_landing_pages(channel_group);")

        # 3. Bảng GSC Keyword Ranking Inventory Matching
        conn.execute("""
            CREATE TABLE IF NOT EXISTS gsc_keyword_ranking (
                query TEXT PRIMARY KEY,
                clicks INTEGER NOT NULL DEFAULT 0,
                impressions INTEGER NOT NULL DEFAULT 0,
                position REAL NOT NULL DEFAULT 0.0,
                rounded_position INTEGER NOT NULL DEFAULT 0,
                opportunity_score REAL NOT NULL DEFAULT 0.0,
                synced_at TEXT
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ranking_pos ON gsc_keyword_ranking(position);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ranking_opp ON gsc_keyword_ranking(opportunity_score DESC);")

        # 4. Bảng Chiều URL -> Dự án & Hub (DIM_URL_PROJECT)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS dim_url_project (
                url TEXT PRIMARY KEY,
                path TEXT NOT NULL DEFAULT '',
                primary_project TEXT NOT NULL DEFAULT '',
                hub_id TEXT NOT NULL DEFAULT '',
                hub_name TEXT NOT NULL DEFAULT '',
                match_type TEXT NOT NULL DEFAULT '',
                synced_at TEXT
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_dim_path ON dim_url_project(path);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_dim_hub ON dim_url_project(hub_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_dim_proj ON dim_url_project(primary_project);")

        # 5. Bảng Chu kỳ Mùa vụ Theo Theme (DIM_THEME_SEASONALITY)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS dim_theme_seasonality (
                theme_id TEXT PRIMARY KEY,
                name TEXT NOT NULL DEFAULT '',
                sector TEXT NOT NULL DEFAULT '',
                pillar TEXT NOT NULL DEFAULT '',
                volume INTEGER NOT NULL DEFAULT 0,
                m1 INTEGER NOT NULL DEFAULT 0,
                m2 INTEGER NOT NULL DEFAULT 0,
                m3 INTEGER NOT NULL DEFAULT 0,
                m4 INTEGER NOT NULL DEFAULT 0,
                m5 INTEGER NOT NULL DEFAULT 0,
                m6 INTEGER NOT NULL DEFAULT 0,
                m7 INTEGER NOT NULL DEFAULT 0,
                m8 INTEGER NOT NULL DEFAULT 0,
                m9 INTEGER NOT NULL DEFAULT 0,
                m10 INTEGER NOT NULL DEFAULT 0,
                m11 INTEGER NOT NULL DEFAULT 0,
                m12 INTEGER NOT NULL DEFAULT 0,
                synced_at TEXT
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_season_sector ON dim_theme_seasonality(sector);")

        # 6. Bảng Lũy Kế Hiệu Suất Hàng Ngày (FACT_DAILY_PERFORMANCE)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS fact_daily_performance (
                date TEXT PRIMARY KEY,
                days_elapsed INTEGER NOT NULL DEFAULT 0,
                days_in_month INTEGER NOT NULL DEFAULT 31,
                total_pv INTEGER NOT NULL DEFAULT 0,
                target_pv INTEGER NOT NULL DEFAULT 0,
                organic_pv INTEGER NOT NULL DEFAULT 0,
                direct_pv INTEGER NOT NULL DEFAULT 0,
                paid_pv INTEGER NOT NULL DEFAULT 0,
                referral_pv INTEGER NOT NULL DEFAULT 0,
                others_pv INTEGER NOT NULL DEFAULT 0,
                non_paid_pv INTEGER NOT NULL DEFAULT 0,
                sessions INTEGER NOT NULL DEFAULT 0,
                users INTEGER NOT NULL DEFAULT 0,
                progress_pct REAL NOT NULL DEFAULT 0.0,
                forecast_pv REAL NOT NULL DEFAULT 0.0,
                forecast_pct REAL NOT NULL DEFAULT 0.0,
                synced_at TEXT
            );
        """)

        # 7. Views Phân Tích Tổng Hợp (Analytical Views)
        conn.execute("""
            CREATE VIEW IF NOT EXISTS v_hub_performance AS
            SELECT 
                COALESCE(d.hub_name, 'Khác / Chưa phân loại') AS hub_name,
                COALESCE(d.hub_id, 'others') AS hub_id,
                COUNT(DISTINCT g.landing_page) AS active_pages,
                SUM(g.sessions) AS total_sessions,
                SUM(g.engaged_sessions) AS engaged_sessions,
                ROUND(SUM(g.engaged_sessions) * 100.0 / NULLIF(SUM(g.sessions), 0), 2) AS engagement_rate_pct,
                SUM(g.onelink_clicks_track1 + g.onelink_clicks_track2) AS w2a_clicks,
                ROUND(SUM(g.onelink_clicks_track1 + g.onelink_clicks_track2) * 100.0 / NULLIF(SUM(g.sessions), 0), 3) AS w2a_cvr_pct
            FROM ga4_landing_pages g
            LEFT JOIN dim_url_project d ON (
                g.landing_page = d.path 
                OR ('https://www.momo.vn' || g.landing_page) = d.url
            )
            GROUP BY COALESCE(d.hub_name, 'Khác / Chưa phân loại'), COALESCE(d.hub_id, 'others');
        """)

        conn.execute("""
            CREATE VIEW IF NOT EXISTS v_keyword_quick_wins AS
            SELECT 
                query,
                page_url,
                clicks,
                impressions,
                ROUND(ctr * 100, 2) AS ctr_pct,
                ROUND(position, 1) AS avg_position,
                ROUND(impressions * (1.0 - ctr), 0) AS potential_gain
            FROM gsc_search_analytics
            WHERE position BETWEEN 4.0 AND 15.0
              AND impressions >= 500
              AND ctr < 0.05
            ORDER BY potential_gain DESC;
        """)

    conn.close()


def query_gsc_by_keyword(query: str, limit: int = 20, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu nhanh các URL xếp hạng theo từ khóa (O(1) latency)."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT page_url, query, clicks, impressions, ctr, position
        FROM gsc_search_analytics
        WHERE query = ?
        ORDER BY clicks DESC, impressions DESC
        LIMIT ?;
    """, (query, limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_gsc_by_url(url: str, limit: int = 50, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu các từ khóa đem lại lượt click nhiều nhất cho một URL."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT query, clicks, impressions, ctr, position
        FROM gsc_search_analytics
        WHERE page_url = ?
        ORDER BY clicks DESC, impressions DESC
        LIMIT ?;
    """, (url, limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_ga4_by_path(path_pattern: str, limit: int = 50, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu hiệu suất GA4 theo đường dẫn landing page."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT landing_page, channel_group, source, sessions, engaged_sessions,
               onelink_clicks_track1, onelink_clicks_track2
        FROM ga4_landing_pages
        WHERE landing_page LIKE ?
        ORDER BY sessions DESC
        LIMIT ?;
    """, (f"{path_pattern}%", limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_hubs_summary(db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu hiệu suất tổng thể các Hubs (Sessions, Engagement Rate, W2A, CVR)."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT hub_name, hub_id, active_pages, total_sessions, engaged_sessions,
               engagement_rate_pct, w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        ORDER BY total_sessions DESC;
    """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_top_w2a_drivers(limit: int = 20, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu các URL đóng vai trò chuyển đổi Web-to-App mạnh nhất."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            g.landing_page,
            COALESCE(d.hub_name, 'Khác') AS hub_name,
            COALESCE(d.primary_project, 'Khác') AS primary_project,
            SUM(g.sessions) AS sessions,
            SUM(g.onelink_clicks_track1 + g.onelink_clicks_track2) AS total_w2a,
            ROUND(SUM(g.onelink_clicks_track1 + g.onelink_clicks_track2) * 100.0 / NULLIF(SUM(g.sessions), 0), 2) AS w2a_cvr_pct
        FROM ga4_landing_pages g
        LEFT JOIN dim_url_project d ON (
            g.landing_page = d.path 
            OR ('https://www.momo.vn' || g.landing_page) = d.url
        )
        GROUP BY g.landing_page, d.hub_name, d.primary_project
        HAVING total_w2a > 0
        ORDER BY total_w2a DESC
        LIMIT ?;
    """, (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_quick_wins(min_impressions: int = 500, limit: int = 20, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu từ khóa Quick Wins (Top 4-15, nhiều impression nhưng CTR thấp)."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT query, page_url, clicks, impressions, ctr_pct, avg_position, potential_gain
        FROM v_keyword_quick_wins
        WHERE impressions >= ?
        LIMIT ?;
    """, (min_impressions, limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_gsc_hubs_summary(db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu hiệu suất SEO Google Search Console 2026 gom nhóm theo từng Hub."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            COALESCE(NULLIF(d.hub_name, ''), 'Chưa phân loại') AS hub_name,
            COUNT(g.page_url) AS pages_count,
            SUM(g.clicks) AS total_clicks,
            SUM(g.impressions) AS total_impressions,
            ROUND(SUM(g.clicks) * 100.0 / NULLIF(SUM(g.impressions), 0), 2) AS avg_ctr,
            ROUND(AVG(g.position), 2) AS avg_position
        FROM gsc_top_pages_2026 g
        LEFT JOIN dim_url_project d ON (
            g.page_url = d.url OR 
            g.page_url = 'https://www.momo.vn' || d.path OR
            g.page_url = 'https://momo.vn' || d.path
        )
        GROUP BY hub_name
        ORDER BY total_clicks DESC;
    """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_gsc_devices(db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu hiệu suất tìm kiếm phân bổ theo Thiết bị (Mobile vs Desktop vs Tablet)."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT device, clicks, impressions, ctr, position FROM gsc_devices_2026;")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


if __name__ == "__main__":
    init_db()
    print(f"[OK] Đã khởi tạo thành công cấu trúc SQLite tại: {DEFAULT_DB_PATH}")


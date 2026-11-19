# -*- coding: utf-8 -*-
"""
BIGQUERY CLIENT (SSOT) - GA4 raw export
Query BigQuery project `momovn-prod`, dataset GA4 export `analytics_270743103`.
Dùng khi cần dữ liệu raw event-level mà GA4 Data API không trả được
(event_params, user properties, intraday tables).

Usage:
    from scripts.lib.bq_client import query
    rows = query('''
        SELECT event_name, COUNT(*) AS cnt
        FROM `momovn-prod.analytics_270743103.events_intraday_*`
        WHERE _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 3 DAY))
        GROUP BY event_name
    ''')
    # rows = [{"event_name": "page_view", "cnt": 12345}, ...]

Lưu ý:
- events_intraday_* : dữ liệu intraday (nhanh, chưa finalize, ~30-40 ngày gần nhất)
- events_*          : daily tables đã finalize (dùng cho phân tích lịch sử)
- Wildcard _TABLE_SUFFIX lọc theo ngày YYYYMMDD.

GIỚI HẠN ĐÃ BIẾT: BigQuery API có thể bị VPC Service Controls chặn
(HttpError 403 policyViolation) nếu máy/credential nằm ngoài perimeter.
Nếu gặp lỗi này: báo user cần chạy trong môi trường được phép, hoặc
xác nhận với team Data có đường truy cập BQ chính thức.
"""

import argparse
import json
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CREDS_FILE = os.path.join(REPO_ROOT, "07_REPORTS", "data", "credentials", "gsc-credentials.json")
PROJECT_ID = "momovn-prod"
DATASET = "analytics_270743103"

_client = {"service": None}


def _service():
    if _client["service"] is None:
        creds = service_account.Credentials.from_service_account_file(
            CREDS_FILE, scopes=["https://www.googleapis.com/auth/bigquery.readonly"])
        _client["service"] = build("bigquery", "v2", credentials=creds, cache_discovery=False)
    return _client["service"]


def query(sql: str, max_rows: int = 10000, timeout_ms: int = 120000) -> list:
    """
    Chạy SQL (Standard SQL) và trả về list of dict {column_name: value}.
    Tự động paginate getQueryResults tới khi hết hoặc đạt max_rows.
    """
    bq = _service()
    job = bq.jobs().query(
        projectId=PROJECT_ID,
        body={"query": sql, "useLegacySql": False, "timeoutMs": timeout_ms},
    ).execute()

    job_ref = job.get("jobReference", {})
    job_id = job_ref.get("jobId")
    location = job_ref.get("location", "US")

    res = bq.jobs().getQueryResults(
        projectId=PROJECT_ID, jobId=job_id, location=location,
        maxResults=min(10000, max_rows)).execute()
    fields = res.get("schema", {}).get("fields", [])

    rows = []
    page_token = None
    while True:
        params = {"projectId": PROJECT_ID, "jobId": job_id, "location": location,
                  "maxResults": min(10000, max_rows - len(rows))}
        if page_token:
            params["pageToken"] = page_token
        res = bq.jobs().getQueryResults(**params).execute()
        schema = res.get("schema", {}).get("fields", fields)
        for r in res.get("rows", []):
            rows.append({f["name"]: _cell(f.get("type"), v.get("v"))
                         for f, v in zip(schema, r["f"])})
        page_token = res.get("pageToken")
        if not page_token or len(rows) >= max_rows:
            break
    return rows


def _cell(bq_type: str, value):
    """Convert BigQuery cell value sang Python type cơ bản."""
    if value is None:
        return None
    if bq_type in ("INTEGER", "INT64"):
        return int(value)
    if bq_type in ("FLOAT", "FLOAT64", "NUMERIC", "BIGNUMERIC"):
        return float(value)
    if bq_type == "BOOLEAN":
        return value == "true"
    return value


def _main():
    ap = argparse.ArgumentParser(description="BigQuery ad-hoc query (GA4 export)")
    ap.add_argument("sql", nargs="?", help="SQL query hoặc @file.sql")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()

    if args.demo or args.sql == "--demo":
        sql = f"""
            SELECT event_name, COUNT(*) AS cnt
            FROM `{PROJECT_ID}.{DATASET}.events_intraday_*`
            WHERE _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
            GROUP BY event_name ORDER BY cnt DESC LIMIT 10
        """
    else:
        sql = open(args.sql[1:]).read() if args.sql.startswith("@") else args.sql

    for r in query(sql)[:args.limit]:
        print(json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    _main()
# -*- coding: utf-8 -*-
"""
GA4 DATA API CLIENT (SSOT)
Client dùng chung cho mọi truy vấn ad-hoc GA4 Data API (runReport).
Thay thế pattern copy-paste `get_ga4_access_token()` trong ~55 script/scratch file.

Usage:
    from scripts.lib.ga4_client import run_report

    rows = run_report(
        dimensions=["pagePath", "eventName"],
        metrics=["eventCount", "totalUsers"],
        start_date="30daysAgo", end_date="today",
        dimension_filter={
            "filter": {"fieldName": "pagePath",
                       "stringFilter": {"matchType": "EXACT", "value": "/tai-chinh"}}
        },
    )
    # rows = [{"pagePath": "/tai-chinh", "eventName": "page_view",
    #          "eventCount": "123", "totalUsers": "45"}, ...]
"""

import json
import urllib.request
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PROPERTY_ID = "270743103"
REPORT_URL = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"

_CREDS_FILE = REPO_ROOT / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
_TOKEN_FILE = REPO_ROOT / "07_REPORTS" / "data" / "credentials" / "ga4-token.json"

_token_cache = {"value": None}


def get_access_token() -> str:
    """Lấy OAuth access token từ refresh token đã lưu. Cache trong process."""
    if _token_cache["value"]:
        return _token_cache["value"]

    creds_data = json.loads(_CREDS_FILE.read_text(encoding="utf-8"))
    token_data = json.loads(_TOKEN_FILE.read_text(encoding="utf-8"))
    installed = creds_data.get("installed") or creds_data.get("web")

    body = urllib.parse.urlencode({
        "client_id": installed["client_id"],
        "client_secret": installed["client_secret"],
        "refresh_token": token_data["refresh_token"],
        "grant_type": "refresh_token",
    }).encode()

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    with urllib.request.urlopen(req) as resp:
        _token_cache["value"] = json.loads(resp.read().decode())["access_token"]
    return _token_cache["value"]


def _post_report(payload: dict) -> dict:
    req = urllib.request.Request(
        REPORT_URL,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {get_access_token()}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def run_report(
    dimensions: list,
    metrics: list,
    start_date: str = "30daysAgo",
    end_date: str = "today",
    dimension_filter: dict = None,
    dimension_order_bys: list = None,
    metric_order_bys: list = None,
    order_bys: list = None,
    limit: int = 100000,
    offset: int = 0,
    return_raw: bool = False,
) -> list:
    """
    Chạy GA4 runReport, tự phân trang tới hết.

    Args:
        dimensions: list tên dimension, vd ["pagePath", "eventName", "date"]
        metrics: list tên metric, vd ["eventCount", "totalUsers", "sessions"]
        start_date/end_date: "30daysAgo", "today", "2026-11-01", ...
        dimension_filter: GA4 FilterExpression (xem docstring đầu file)
        dimension_order_bys/metric_order_bys/order_bys: list orderBy spec
        limit/offset: phân trang (mặc định lấy hết, page size 10000)
        return_raw: True -> trả raw API rows; False -> list of dict

    Returns:
        list of dict {dimension_name: value, metric_name: value(str)} theo thứ tự
        dimensions rồi metrics trong response.
    """
    payload = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "dimensions": [{"name": d} for d in dimensions],
        "metrics": [{"name": m} for m in metrics],
        "limit": min(limit, 10000),
        "offset": offset,
    }
    if dimension_filter:
        payload["dimensionFilter"] = dimension_filter
    obs = []
    if order_bys:
        obs = order_bys
    elif dimension_order_bys or metric_order_bys:
        obs = [{"dimension": {"dimensionName": d}} for d in (dimension_order_bys or [])]
        obs += [{"metric": {"metricName": m}} for m in (metric_order_bys or [])]
    if obs:
        payload["orderBys"] = obs

    out = []
    page_offset = offset
    page_size = payload["limit"]
    remaining = limit - offset

    while remaining > 0:
        payload["offset"] = page_offset
        payload["limit"] = min(page_size, remaining)
        res = _post_report(payload)
        rows = res.get("rows", [])
        dim_headers = [h["name"] for h in res.get("dimensionHeaders", [])]
        met_headers = [h["name"] for h in res.get("metricHeaders", [])]

        for r in rows:
            if return_raw:
                out.append(r)
                continue
            item = {}
            for i, name in enumerate(dim_headers):
                item[name] = r["dimensionValues"][i]["value"]
            for i, name in enumerate(met_headers):
                item[name] = r["metricValues"][i]["value"]
            out.append(item)

        if len(rows) < payload["limit"]:
            break
        page_offset += payload["limit"]
        remaining -= payload["limit"]

    return out


def run_report_all(
    dimensions: list,
    metrics: list,
    start_date: str = "30daysAgo",
    end_date: str = "today",
    dimension_filter: dict = None,
    order_bys: list = None,
) -> list:
    """Wrapper run_report không giới hạn số dòng (lấy hết)."""
    return run_report(
        dimensions=dimensions,
        metrics=metrics,
        start_date=start_date,
        end_date=end_date,
        dimension_filter=dimension_filter,
        order_bys=order_bys,
        limit=10_000_000,
    )


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="GA4 ad-hoc query tool")
    ap.add_argument("--dimensions", required=True, help="Comma-separated, vd pagePath,eventName")
    ap.add_argument("--metrics", required=True, help="Comma-separated, vd eventCount,totalUsers")
    ap.add_argument("--start", default="30daysAgo")
    ap.add_argument("--end", default="today")
    ap.add_argument("--filter-field")
    ap.add_argument("--filter-value")
    ap.add_argument("--filter-type", default="EXACT", choices=["EXACT", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "REGEXP"])
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()

    f = None
    if args.filter_field and args.filter_value:
        f = {"filter": {"fieldName": args.filter_field,
                        "stringFilter": {"matchType": args.filter_type, "value": args.filter_value}}}

    dims = [d.strip() for d in args.dimensions.split(",") if d.strip()]
    mets = [m.strip() for m in args.metrics.split(",") if m.strip()]
    rows = run_report(dims, mets, args.start, args.end, dimension_filter=f, limit=args.limit)
    for r in rows[:args.limit]:
        print(r)
    print(f"# {len(rows)} rows")

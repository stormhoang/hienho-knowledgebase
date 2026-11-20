#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO NEWS INSIGHTS ENGINE
Gan field "insight" cho tung tin trong seo-news.json dua tren du lieu THAT
(GSC Search Analytics API, Bing AI Performance, Clarity, GSC Crawl Stats).
Nguyen tac bat buoc: chi gan khi tinh duoc tu du lieu that, khong suy dien;
khong tinh duoc thi BO field insight. Moi so trong "finding" phai xuat hien
trong "evidence" (kem source + period). "data_as_of" khong cu hon 14 ngay.

Cach tinh theo category:
- google_update / serp_feature (nguon GSC):
  So sanh clicks, impressions, avg position L ngay sau vs L ngay truoc moc
  published_at (moc = published_at, L toi da 7 ngay; du lieu GSC tre 3 ngay).
  affected = clicks toan site giam >= 10% VA muc giam vuot do lech chuan ngay
  cua 8 tuan truoc moc; affected list = top 5 URL giam clicks manh nhat
  (loc URL co >= 100 clicks ky truoc).
  watch = giam 5-10% hoac du lieu sau moc chua du 7 ngay.
  not_affected = cac truong hop con lai.
- ai_search / geo (nguon geo-ai-visibility.json cua hubs-momo):
  So sanh luot trich dan momo.vn tren Bing AI (daily citations, cited pages)
  theo cung cong thuc cua so. Kem evidence referral tu AI engines (Clarity)
  khi snapshot con moi (<= 14 ngay).
- technical (nguon GSC + Crawl Stats):
  Doi chieu so URL co impressions trong GSC (proxy index coverage) theo cung
  cong thuc cua so + requests/ngay tu Googlebot (Crawl Stats) khi file con moi.
  Vi du tin Indexing API: neu khong co du lieu URL-level chuyen biet thi chi
  bao cao index coverage proxy, khong suy dien viec momo.vn co dung API hay khong.
- industry: khong gan insight (thuong khong co so lieu do luong duoc).

Caching: moi query GSC duoc cache theo (site, start, end, dimensions) tai
07_REPORTS/data/cache/gsc_insights/ de tranh goi lai API.

Su dung:
  python3 scripts/seo_news_insights.py            # test tren SSOT, khong ghi
  python3 scripts/seo_news_insights.py --write    # test + ghi de SSOT
"""

import argparse
import hashlib
import json
import os
import statistics
import time
from datetime import date, datetime, timedelta
from urllib.parse import urlsplit

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"
SSOT_PATH = os.path.join(BASE_DIR, "07_REPORTS", "data", "seo_news_latest.json")
GEO_AI_PATH = os.path.join(HUBS_REPO, "data", "geo-ai-visibility.json")
CRAWL_STATS_PATH = os.path.join(
    BASE_DIR, "07_REPORTS", "technical_seo", "crawl_stats", "gsc_crawl_stats_latest.json")
CACHE_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data", "cache", "gsc_insights")
CRED_PATHS = [
    os.path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "gsc-credentials.json"),
    os.path.join(BASE_DIR, "07_REPORTS", "data", "gsc-credentials.json"),
]

GSC_SITE_FALLBACK = "https://www.momo.vn/"
GSC_LAG_DAYS = 3
MAX_DATA_AGE_DAYS = 14
WINDOW_DAYS = 7
BASELINE_DAYS = 56
MIN_BEFORE_CLICKS = 100
TOP_URLS = 5
AFFECTED_PCT = -10.0
WATCH_PCT = -5.0

_service = None
_site = None
_gsc_disabled = False
_geo_cache = None


# === Helpers ===

def fmt_num(n):
    try:
        n = float(n)
    except (TypeError, ValueError):
        return str(n)
    if abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.2f}M".replace(".00M", "M").replace(".0M", "M")
    if abs(n) >= 1000:
        return f"{n / 1000:.1f}K".replace(".0K", "K")
    return f"{n:.0f}"


def fmt_pct(x):
    return f"{x:.1f}".replace(".", ",") + "%"


def task_date_str(anchor):
    return f"{anchor.day}/{anchor.month}"


# === GSC layer ===

def _get_gsc():
    global _service, _site, _gsc_disabled
    if _gsc_disabled:
        return None, None
    if _service is not None:
        return _service, _site
    try:
        import warnings
        warnings.filterwarnings("ignore")
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        key_file = next((p for p in CRED_PATHS if os.path.exists(p)), None)
        if not key_file:
            raise FileNotFoundError("gsc-credentials.json")
        creds = service_account.Credentials.from_service_account_file(
            key_file, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
        _service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
        entries = _service.sites().list().execute().get("siteEntry", [])
        _site = next((e["siteUrl"] for e in entries if "momo" in e["siteUrl"]), GSC_SITE_FALLBACK)
        return _service, _site
    except Exception as e:
        print(f"  [WARN] Insight: khong ket noi duoc GSC API ({str(e)[:70]}) -> bo qua insight GSC")
        _gsc_disabled = True
        return None, None


def _gsc_query(start, end, dimensions, row_limit=25000):
    svc, site = _get_gsc()
    if svc is None:
        return None
    key = hashlib.sha1(f"{site}|{start}|{end}|{','.join(dimensions)}|{row_limit}".encode()).hexdigest()[:16]
    cache_file = os.path.join(CACHE_DIR, key + ".json")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    body = {"startDate": str(start), "endDate": str(end), "dimensions": dimensions, "rowLimit": row_limit}
    try:
        resp = svc.searchanalytics().query(siteUrl=site, body=body).execute()
        rows = resp.get("rows", [])
    except Exception as e:
        print(f"  [WARN] Insight GSC query {start}->{end} {dimensions}: {str(e)[:70]}")
        return None
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False)
    except Exception:
        pass
    time.sleep(0.2)
    return rows


def _daily_series(start, end):
    """{date_str: {clicks, impressions, position}} toan site."""
    rows = _gsc_query(start, end, ["date"], row_limit=500)
    if rows is None:
        return None
    out = {}
    for r in rows:
        out[r["keys"][0]] = {"clicks": r.get("clicks", 0.0),
                             "impressions": r.get("impressions", 0.0),
                             "position": r.get("position", 0.0)}
    return out


def _page_map(start, end):
    """{page_url: {clicks, impressions}}."""
    rows = _gsc_query(start, end, ["page"])
    if rows is None:
        return None
    return {r["keys"][0]: {"clicks": r.get("clicks", 0.0), "impressions": r.get("impressions", 0.0)}
            for r in rows}


def _avg(series, d1, d2, field):
    days = (d2 - d1).days + 1
    if days <= 0:
        return None
    total = 0.0
    for i in range(days):
        row = series.get(str(d1 + timedelta(days=i)))
        if row:
            total += row.get(field, 0.0)
    return total / days


def _weighted_position(series, d1, d2):
    num = den = 0.0
    for i in range((d2 - d1).days + 1):
        row = series.get(str(d1 + timedelta(days=i)))
        if row and row.get("impressions"):
            num += row["position"] * row["impressions"]
            den += row["impressions"]
    return num / den if den else None


def _sigma(series, end_date, field):
    d1 = end_date - timedelta(days=BASELINE_DAYS - 1)
    vals = []
    for i in range(BASELINE_DAYS):
        row = series.get(str(d1 + timedelta(days=i)))
        vals.append(row.get(field, 0.0) if row else 0.0)
    if len([v for v in vals if v]) < 20:
        return None
    return statistics.pstdev(vals)


def _windows(anchor, data_max):
    """Tra ve (L, before_tuple, after_tuple) hoac None neu khong co du lieu sau moc."""
    if anchor > data_max:
        return None
    L = min(WINDOW_DAYS, (data_max - anchor).days)
    if L < 1:
        return None
    before = (anchor - timedelta(days=L), anchor - timedelta(days=1))
    after = (anchor + timedelta(days=1), anchor + timedelta(days=L))
    return L, before, after


def _period_str(L, anchor):
    base = f"{L} ngày sau vs {L} ngày trước {task_date_str(anchor)}"
    if L < WINDOW_DAYS:
        base += " (chưa đủ 7 ngày dữ liệu sau mốc)"
    return base


def _status_from(recent_avg, before_avg, sigma, L):
    if recent_avg is None or before_avg is None or before_avg < 1:
        return None, None
    pct = (recent_avg - before_avg) / before_avg * 100
    if L < WINDOW_DAYS:
        return "watch", pct
    if pct <= AFFECTED_PCT:
        if sigma is not None and (recent_avg - before_avg) <= -sigma:
            return "affected", pct
        return "watch", pct
    if pct <= WATCH_PCT:
        return "watch", pct
    return "not_affected", pct


def _move_word(pct):
    if pct > 0:
        return "tăng"
    if pct < 0:
        return "giảm"
    return "biến động"


# === Insight: google_update / serp_feature ===

def _insight_update(anchor, data_max):
    svc, _ = _get_gsc()
    if svc is None:
        return None
    w = _windows(anchor, data_max)
    if not w:
        return None
    L, before, after = w
    series = _daily_series(anchor - timedelta(days=BASELINE_DAYS), after[1])
    if series is None:
        return None

    b_clicks = _avg(series, before[0], before[1], "clicks")
    a_clicks = _avg(series, after[0], after[1], "clicks")
    sigma = _sigma(series, anchor - timedelta(days=1), "clicks")
    status, pct = _status_from(a_clicks, b_clicks, sigma, L)
    if status is None:
        return None

    period = _period_str(L, anchor)
    evidence = [{
        "label": "Clicks organic toàn site",
        "value": fmt_num(a_clicks),
        "delta_pct": round(pct, 1),
        "source": "GSC",
        "period": period,
    }]

    b_imp = _avg(series, before[0], before[1], "impressions")
    a_imp = _avg(series, after[0], after[1], "impressions")
    if b_imp and a_imp is not None:
        evidence.append({
            "label": "Impressions toàn site",
            "value": fmt_num(a_imp),
            "delta_pct": round((a_imp - b_imp) / b_imp * 100, 1),
            "source": "GSC",
            "period": period,
        })

    b_pos = _weighted_position(series, before[0], before[1])
    a_pos = _weighted_position(series, after[0], after[1])
    if b_pos and a_pos:
        evidence.append({
            "label": "Vị trí trung bình (impression-weighted)",
            "value": f"{a_pos:.1f}",
            "delta_pct": round((a_pos - b_pos) / b_pos * 100, 1),
            "source": "GSC",
            "period": period,
        })

    affected = []
    if status == "affected":
        pm_b = _page_map(before[0], before[1])
        pm_a = _page_map(after[0], after[1])
        if pm_b is not None and pm_a is not None:
            rows = []
            for page, bv in pm_b.items():
                if bv["clicks"] < MIN_BEFORE_CLICKS:
                    continue
                av = pm_a.get(page, {"clicks": 0.0})
                rows.append((av["clicks"] - bv["clicks"], page, bv["clicks"]))
            rows.sort(key=lambda x: x[0])
            for delta, page, bc in rows[:TOP_URLS]:
                affected.append({
                    "name": urlsplit(page).path or "/",
                    "url": page,
                    "clicks_delta_pct": round(delta / bc * 100, 1),
                })

    dstr = task_date_str(anchor)
    if status == "affected":
        tail = f"; {len(affected)} URL mất clicks nhiều nhất được liệt kê bên dưới." if affected else "."
        finding = (f"Clicks organic toàn site giảm {fmt_pct(abs(pct))} trong {L} ngày sau {dstr} "
                   f"so với {L} ngày trước đó, vượt biến động chuẩn 8 tuần" + tail)
        if affected:
            extra = len(affected) - 1
            next_step = (f"Rà soát {affected[0]['name']}"
                         + (f" và {extra} URL còn lại" if extra else "")
                         + " trong danh sách affected trên GSC (on-page, internal link, trạng thái index) trước khi kết luận.")
        else:
            next_step = "Rà soát top URL giảm clicks trên GSC (on-page, internal link, trạng thái index) trước khi kết luận."
    elif L < WINDOW_DAYS:
        finding = (f"Dữ liệu sau mốc {dstr} mới có {L}/7 ngày: clicks organic toàn site "
                   f"{_move_word(pct)} {fmt_pct(abs(pct))} tạm tính so với {L} ngày liền trước.")
        nxt = anchor + timedelta(days=WINDOW_DAYS)
        next_step = (f"Chạy lại kiểm tra GSC sau {task_date_str(nxt)} khi đủ 7 ngày dữ liệu sau mốc; "
                     "nếu clicks giảm ≥10% thì rà top URL theo cùng khung so sánh.")
    elif status == "watch":
        finding = (f"Clicks organic toàn site giảm {fmt_pct(abs(pct))} trong 7 ngày sau {dstr} "
                   "so với 7 ngày trước đó, dưới ngưỡng 10%.")
        next_step = "Theo dõi thêm 7 ngày tiếp theo trên GSC; nếu mức giảm vượt 10% thì rà top URL."
    else:
        finding = (f"Clicks organic toàn site {_move_word(pct)} {fmt_pct(abs(pct))} trong 7 ngày sau {dstr} "
                   "so với 7 ngày trước đó, không vượt ngưỡng 5%.")
        next_step = "Không cần hành động ngay; duy trì theo dõi GSC định kỳ."

    insight = {
        "status": status,
        "finding": finding,
        "evidence": evidence,
        "next_step": next_step,
        "data_as_of": str(data_max),
    }
    if affected:
        insight["affected"] = affected
    return insight


# === Insight: ai_search / geo ===

def _load_geo():
    global _geo_cache
    if _geo_cache is not None:
        return _geo_cache
    try:
        with open(GEO_AI_PATH, "r", encoding="utf-8") as f:
            d = json.load(f)
        daily = {}
        for row in d.get("daily", []):
            if row.get("date"):
                daily[row["date"]] = row
        _geo_cache = {"daily": daily, "clarity": d.get("clarity", {})}
    except Exception as e:
        print(f"  [WARN] Insight: khong doc duoc geo-ai-visibility.json ({str(e)[:60]})")
        _geo_cache = {"daily": {}, "clarity": {}}
    return _geo_cache


def _insight_geo_ai(anchor):
    geo = _load_geo()
    daily = geo["daily"]
    if not daily:
        return None
    series_end = date.fromisoformat(max(daily.keys()))
    if (date.today() - series_end).days > MAX_DATA_AGE_DAYS:
        return None
    w = _windows(anchor, series_end)
    if not w:
        return None
    L, before, after = w
    series = {d: {"clicks": v.get("citations", 0), "impressions": v.get("cited_pages", 0)}
              for d, v in daily.items()}

    b = _avg(series, before[0], before[1], "clicks")
    a = _avg(series, after[0], after[1], "clicks")
    sigma = _sigma(series, anchor - timedelta(days=1), "clicks")
    status, pct = _status_from(a, b, sigma, L)
    if status is None:
        return None

    period = _period_str(L, anchor)
    evidence = [{
        "label": "Lượt trích dẫn momo.vn trên Bing AI (TB/ngày)",
        "value": fmt_num(a),
        "delta_pct": round(pct, 1),
        "source": "Bing AI Performance",
        "period": period,
    }]
    b_pages = _avg(series, before[0], before[1], "impressions")
    a_pages = _avg(series, after[0], after[1], "impressions")
    if b_pages and a_pages is not None:
        evidence.append({
            "label": "Page được Bing AI trích dẫn (TB/ngày)",
            "value": fmt_num(a_pages),
            "delta_pct": round((a_pages - b_pages) / b_pages * 100, 1),
            "source": "Bing AI Performance",
            "period": period,
        })

    clarity = geo.get("clarity", {})
    fetched = str(clarity.get("fetched_at", ""))[:10]
    if fetched:
        try:
            fresh = (date.today() - date.fromisoformat(fetched)).days <= MAX_DATA_AGE_DAYS
        except ValueError:
            fresh = False
        by_source = clarity.get("by_ai_source", {})
        total = sum(v for v in by_source.values() if isinstance(v, (int, float)))
        if fresh and total:
            evidence.append({
                "label": "Referral từ AI engines (Clarity)",
                "value": fmt_num(total),
                "delta_pct": None,
                "source": "Clarity",
                "period": f"snapshot {fetched}",
            })

    dstr = task_date_str(anchor)
    if status == "affected":
        finding = (f"Lượt trích dẫn momo.vn trên Bing AI giảm {fmt_pct(abs(pct))} trong {L} ngày sau {dstr} "
                   "so với kỳ trước, vượt biến động chuẩn 8 tuần.")
        next_step = ("Đối chiếu danh sách page được Bing AI trích dẫn và tăng cường direct answer/schema "
                     "cho nhóm nội dung liên quan.")
    elif L < WINDOW_DAYS:
        finding = (f"Dữ liệu Bing AI sau mốc {dstr} mới có {L}/7 ngày: lượt trích dẫn momo.vn "
                   f"{_move_word(pct)} {fmt_pct(abs(pct))} tạm tính so với {L} ngày liền trước.")
        nxt = anchor + timedelta(days=WINDOW_DAYS)
        next_step = f"Theo dõi citations đến {task_date_str(nxt)} khi đủ 7 ngày dữ liệu sau mốc."
    elif status == "watch":
        finding = (f"Lượt trích dẫn momo.vn trên Bing AI giảm {fmt_pct(abs(pct))} trong 7 ngày sau {dstr} "
                   "so với 7 ngày trước đó, dưới ngưỡng 10%.")
        next_step = "Theo dõi citations thêm 7 ngày; kiểm tra page được trích dẫn nếu mức giảm mở rộng."
    else:
        finding = (f"Lượt trích dẫn momo.vn trên Bing AI {_move_word(pct)} {fmt_pct(abs(pct))} trong 7 ngày sau {dstr} "
                   "so với 7 ngày trước đó, không vượt ngưỡng 5%.")
        next_step = "Không cần hành động; duy trì theo dõi citations định kỳ."

    return {
        "status": status,
        "finding": finding,
        "evidence": evidence,
        "next_step": next_step,
        "data_as_of": str(series_end),
    }


# === Insight: technical ===

def _crawl_evidence():
    try:
        with open(CRAWL_STATS_PATH, "r", encoding="utf-8") as f:
            d = json.load(f)
        export = d.get("export_date", "")
        if (date.today() - date.fromisoformat(export)).days > MAX_DATA_AGE_DAYS:
            return None
        months = sorted(d.get("monthly_run_rate", {}).keys())
        if len(months) < 2:
            return None
        last, prev = months[-1], months[-2]
        lr = d["monthly_run_rate"][last].get("requests_per_day")
        pr = d["monthly_run_rate"][prev].get("requests_per_day")
        if not lr or not pr:
            return None
        return {
            "label": "Requests/ngày từ Googlebot (Crawl Stats)",
            "value": fmt_num(lr),
            "delta_pct": round((lr - pr) / pr * 100, 1),
            "source": "GSC Crawl Stats",
            "period": f"{last} vs {prev} (export {export})",
        }
    except Exception:
        return None


def _insight_technical(anchor, data_max):
    svc, _ = _get_gsc()
    if svc is None:
        return None
    w = _windows(anchor, data_max)
    if not w:
        return None
    L, before, after = w
    pm_b = _page_map(before[0], before[1])
    pm_a = _page_map(after[0], after[1])
    if pm_b is None or pm_a is None:
        return None
    pages_b = sum(1 for v in pm_b.values() if v["impressions"] > 0)
    pages_a = sum(1 for v in pm_a.values() if v["impressions"] > 0)
    if pages_b < 100:
        return None
    pct = (pages_a - pages_b) / pages_b * 100
    if L < WINDOW_DAYS:
        status = "watch"
    elif pct <= AFFECTED_PCT:
        status = "affected"
    elif pct <= WATCH_PCT:
        status = "watch"
    else:
        status = "not_affected"

    period = _period_str(L, anchor)
    evidence = [{
        "label": "URL có impressions trong GSC (proxy index coverage)",
        "value": fmt_num(pages_a),
        "delta_pct": round(pct, 1),
        "source": "GSC",
        "period": period,
    }]
    crawl = _crawl_evidence()
    if crawl:
        evidence.append(crawl)

    dstr = task_date_str(anchor)
    if status == "affected":
        finding = (f"Số URL có impressions trong GSC giảm {fmt_pct(abs(pct))} trong {L} ngày sau {dstr} "
                   "so với kỳ trước (proxy index coverage).")
        next_step = ("Kiểm tra sitemap và Pages report trong GSC UI cho nhóm URL mất impressions; "
                     "đối chiếu crawl stats trước khi kết luận.")
    elif L < WINDOW_DAYS:
        finding = (f"Dữ liệu sau mốc {dstr} mới có {L}/7 ngày: số URL có impressions trong GSC "
                   f"{_move_word(pct)} {fmt_pct(abs(pct))} tạm tính so với {L} ngày liền trước.")
        nxt = anchor + timedelta(days=WINDOW_DAYS)
        next_step = f"Chạy lại kiểm tra sau {task_date_str(nxt)} khi đủ 7 ngày dữ liệu; đối chiếu Pages report."
    elif status == "watch":
        finding = (f"Số URL có impressions trong GSC giảm {fmt_pct(abs(pct))} trong 7 ngày sau {dstr} "
                   "so với 7 ngày trước đó, dưới ngưỡng 10%.")
        next_step = "Theo dõi thêm 7 ngày; nếu mức giảm mở rộng thì kiểm tra sitemap và Pages report."
    else:
        finding = (f"Số URL có impressions trong GSC {_move_word(pct)} {fmt_pct(abs(pct))} trong 7 ngày sau {dstr} "
                   "so với 7 ngày trước đó, không vượt ngưỡng 5%.")
        next_step = "Không cần hành động; duy trì theo dõi index coverage định kỳ."

    return {
        "status": status,
        "finding": finding,
        "evidence": evidence,
        "next_step": next_step,
        "data_as_of": str(data_max),
    }


# === Entry point ===

def attach_insights(items, verbose=False):
    """Gan insight cho tung item (in-place). Tra ve so item duoc gan."""
    data_max = date.today() - timedelta(days=GSC_LAG_DAYS)
    n = 0
    for it in items:
        cat = it.get("category")
        if cat not in ("google_update", "serp_feature", "ai_search", "geo", "technical"):
            continue
        try:
            anchor = date.fromisoformat(str(it.get("published_at", ""))[:10])
        except (ValueError, TypeError):
            continue
        try:
            if cat in ("google_update", "serp_feature"):
                insight = _insight_update(anchor, data_max)
            elif cat in ("ai_search", "geo"):
                insight = _insight_geo_ai(anchor)
            else:
                insight = _insight_technical(anchor, data_max)
        except Exception as e:
            insight = None
            if verbose:
                print(f"  [WARN] Insight loi tai {str(it.get('url'))[:60]}: {str(e)[:80]}")
        if insight:
            it["insight"] = insight
            n += 1
            if verbose:
                print(f"  [insight] {insight['status']:12s} | {it['title'][:60]}")
    return n


def main():
    ap = argparse.ArgumentParser(description="SEO News Insights Engine (test mode)")
    ap.add_argument("--source", default=SSOT_PATH, help="File JSON nguon (mac dinh SSOT)")
    ap.add_argument("--write", action="store_true", help="Ghi de ket qua vao file nguon")
    ap.add_argument("--limit", type=int, default=0, help="Chi xu ly N item dau (0 = tat ca)")
    args = ap.parse_args()

    with open(args.source, "r", encoding="utf-8") as f:
        payload = json.load(f)
    items = payload.get("items", [])
    if args.limit:
        items = items[: args.limit]
    print(f"Nguon: {args.source} | {len(items)} tin")
    n = attach_insights(items, verbose=True)
    print(f"\nGan insight: {n}/{len(items)} tin")

    if args.write:
        with open(args.source, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"Da ghi: {args.source}")


if __name__ == "__main__":
    main()

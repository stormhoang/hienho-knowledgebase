#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC SEO NEWS -> HUBS-MOMO PIPELINE
Job tổng hợp tin tức SEO/GEO/AI Search từ các nguồn chính thống (RSS / Status Dashboard),
chuẩn hóa theo schema data/seo-news.json và đẩy sang hubs-momo (react-web-momo).

Nguồn dữ liệu (ưu tiên nguồn chính thống):
  - Google Search Central Blog (RSS)         -> cập nhật thuật toán, tài liệu chính thức
  - Google Search Status Dashboard (JSON)    -> xác nhận update chính thức (core/spam/ranking)
  - Search Engine Journal (RSS)              -> phân tích thị trường
  - Search Engine Roundtable (RSS)           -> tổng hợp biến động SERP

Quy tắc bắt buộc:
  - Chỉ lấy tin trong 60 ngày gần nhất, bỏ trùng theo URL.
  - Ưu tiên nguồn chính thống: Google Search Central Blog + Status Dashboard LẤY HẾT;
    báo ngoài (Search Engine Journal, Search Engine Roundtable) tối đa 25 tin.
  - Tiêu đề dịch sang tiếng Việt, ngắn gọn dưới 90 ký tự, giữ thuật ngữ
    (Core Update, AI Overview, Indexing API...). Lưu bản gốc vào field title_en.
  - Thay mọi dấu gạch dài (– —) bằng dấu gạch ngang thông thường (-).
  - impact=high khi tin ảnh hưởng trực tiếp ranking/traffic hoặc nội dung YMYL tài chính.
  - Không bịa tin: tin nào không có URL gốc thì bỏ.

Cơ chế làm giàu nội dung (enrichment) - 2 lớp:
  1) Gemini Spark daily reports (11_NEWS_FEED/daily/*_daily_report.md):
     - Trích tiêu đề VN, tóm tắt, action, category, impact, tags theo từng section có citation.
     - Bổ sung vào feed các tin được report trích dẫn nhưng RSS không lấy được
       (vd Search Engine Land, Reddit) với published_at = ngày report.
     - Tin được report trích dẫn được ưu tiên giữ slot trong cap 25 external.
  2) File overlay thủ công: 07_REPORTS/data/seo_news_enriched.json
     Dạng: [{ "url": "...", "title": "...", "summary": "...", "action": "...",
              "category": "...", "impact": "...", "tags": [...] }]
  Thứ tự ưu tiên merge theo từng field: Spark > overlay > fallback tự động.
  - "title": tiêu đề tiếng Việt (<90 ký tự). Bản gốc tiếng Anh luôn lưu ở field title_en.

Gan insight (field "insight" - xem scripts/seo_news_insights.py):
  Chi gan khi tinh duoc tu du lieu that (GSC API, Bing AI Performance, Clarity, Crawl Stats);
  khong tinh duoc thi BO field, khong suy dien. Moi so trong finding deu co trong evidence
  kem source + period; data_as_of khong cu hon 14 ngay.

Su dung:
  python3 scripts/sync_seo_news.py                  # fetch + validate + insight + push hubs-momo
  python3 scripts/sync_seo_news.py --no-push        # chi ghi SSOT local
  python3 scripts/sync_seo_news.py --dump-raw       # xuat raw items de lam giau (enrichment)
  python3 scripts/sync_seo_news.py --skip-insights  # bo qua gan insight (chay nhanh)
"""

import argparse
import glob
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlsplit

import requests

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"
DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data")
NEWS_FEED_DIR = os.path.join(BASE_DIR, "11_NEWS_FEED")

SSOT_PATH = os.path.join(DATA_DIR, "seo_news_latest.json")
RAW_PATH = os.path.join(DATA_DIR, "seo_news_raw.json")
ENRICHED_PATH = os.path.join(DATA_DIR, "seo_news_enriched.json")
HUBS_OUTPUT = os.path.join(HUBS_REPO, "data", "seo-news.json")

EXTERNAL_MAX = 25
WINDOW_DAYS = 60
UA = {"User-Agent": "Mozilla/5.0 (compatible; MoMoWebPlatformBot/1.0; +https://momo.vn)"}

SOURCES = [
    {"name": "Google Search Central", "url": "https://developers.google.com/search/blog/feed.xml", "type": "rss", "official": True},
    {"name": "Google Search Status Dashboard", "url": "https://status.search.google.com/incidents.json", "type": "status", "official": True},
    {"name": "Search Engine Journal", "url": "https://www.searchenginejournal.com/feed/", "type": "rss", "official": False},
    {"name": "Search Engine Roundtable", "url": "https://www.seroundtable.com/index.xml", "type": "rss", "official": False},
]

# === Gemini Spark daily reports (11_NEWS_FEED) ===
NEWS_DOMAINS = (
    "seroundtable.com", "searchengineland.com", "searchenginejournal.com",
    "developers.google.com", "status.search.google.com",
    "reddit.com", "x.com", "twitter.com",
    "semrush.com", "ahrefs.com", "ziptie.ai", "botrank.ai",
    "digitalapplied.com", "optimizegeo.ai", "arxiv.org",
)
SOURCE_BY_DOMAIN = {
    "seroundtable.com": "Search Engine Roundtable",
    "searchengineland.com": "Search Engine Land",
    "searchenginejournal.com": "Search Engine Journal",
    "developers.google.com": "Google Search Central",
    "status.search.google.com": "Google Search Status Dashboard",
    "reddit.com": "Reddit r/TechSEO",
    "x.com": "X/Twitter",
    "twitter.com": "X/Twitter",
    "semrush.com": "Semrush",
    "ahrefs.com": "Ahrefs",
    "ziptie.ai": "Ziptie.ai",
    "botrank.ai": "BotRank.ai",
    "digitalapplied.com": "DigitalApplied",
    "optimizegeo.ai": "OptimizeGEO",
    "arxiv.org": "arXiv",
}
SOURCE_PREFIX_RE = re.compile(
    r"^(Search Engine Roundtable|Search Engine Land|Search Engine Journal|Search Engine Status Dashboard"
    r"|Google Status Dashboard|Google Search Central|Google Search Status Dashboard"
    r"|Reddit r/TechSEO|Reddit|X/Twitter|Semrush|Ahrefs|Ziptie\.ai|BotRank\.ai|DigitalApplied|OptimizeGEO|arXiv)\s*:\s*",
    re.IGNORECASE)
ACTION_LABEL_KEYWORDS = ["tactic", "chiến thuật", "hành động", "format", "đề xuất", "giải pháp",
                         "checklist", "triển khai", "next action"]
BOLD_LABEL_RE = re.compile(r"^-\s+\*\*(.+?)\*\*")
SUB_BULLET_RE = re.compile(r"^\s{2,}[-*]\s+(.+)$")
GENERIC_PATHS = {"/", "/search/news", "/search/blog", "/search/docs", "/search/docs/fundamentals"}

# === Phan loai category theo tu khoa (keyword heuristic) ===
CATEGORY_RULES = [
    ("google_update", ["core update", "spam update", "ranking update", "algorithm update",
                        "broad core", "google update", "helpful content", "reviews system",
                        "product reviews update", "link spam", "google confirmed"]),
    ("ai_search", ["ai overview", "ai mode", "ai search", "chatgpt", "perplexity", "gemini",
                    "llm", "large language model", "generative ai", "ai chatbot", "sge"]),
    ("geo", ["geo", "generative engine", "aeo", "answer engine", "llms.txt", "citation",
             "ai visibility", "answer engine optimization"]),
    ("technical", ["indexing", "index", "crawl", "crawler", "sitemap", "robots.txt", "robots",
                    "core web vitals", "page experience", "structured data", "schema",
                    "canonical", "javascript", "rendering", "mobile-first", "https",
                    "search console", "url inspection", "xml sitemap"]),
    ("serp_feature", ["featured snippet", "rich result", "people also ask", "knowledge panel",
                       "serp feature", "discover", "local pack", "top stories", "sit links",
                       "image pack", "video carousel"]),
]

# === Danh gia impact ===
HIGH_KEYWORDS = ["core update", "spam update", "ranking update", "algorithm update", "manual action",
                 "penalty", "deindex", "traffic drop", "broad core update", "search ranking"]
MEDIUM_KEYWORDS = ["search console", "indexing", "crawl", "sitemap", "structured data", "schema",
                   "core web vitals", "rich result", "ai overview", "featured snippet", "verify"]

# === Tag extraction ===
TAG_VOCAB = ["core update", "spam update", "ai overview", "ai mode", "geo", "aeo", "llms.txt",
             "indexing api", "search console", "core web vitals", "schema", "structured data",
             "sitemap", "robots.txt", "featured snippet", "rich result", "chatgpt", "perplexity",
             "gemini", "local seo", "e-e-a-t", "ymyl", "backlink", "cannibalization", "ecommerce"]

YMYL_FINANCE = ["ymyl", "finance", "financial", "banking", "loan", "credit", "insurance",
                "investment", "tax", "interest rate", "money", "ecommerce"]


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def strip_html(text):
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_title(text):
    """Loai bo rac RSS khoi tieu de (via @author, 'appeared first on ...')."""
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r"\s+via\s+@[\w\s,@\.\-]+$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*[-–—]\s*SEO Pulse\s+via\s+@.*$", " - SEO Pulse", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*The post .*? appeared first on .*$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -|·").strip("-–—")


def fix_dashes(text):
    """Thay moi dau gach dai (– — ‒ ―) bang gach ngang thong thuong (-)."""
    if not text:
        return text
    for d in "–—‒―":
        text = text.replace(d, "-")
    return text


def parse_date(raw):
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        pass
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:80].strip("-") or "item"


def norm_url(url):
    return (url or "").split("#")[0].rstrip("/").lower()


def truncate(text, limit):
    """Cat chuoi theo ranh gioi tu, dam bao tong do dai <= limit."""
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[: limit - 3]
    idx = cut.rfind(" ")
    if idx > 40:
        cut = cut[:idx]
    return cut.rstrip(" ,;:-") + "..."


def strip_md(text):
    """Bo marker markdown, giu lai noi dung chu."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.strip()


def slugify_url(url):
    tail = urlsplit(url).path.rstrip("/").split("/")[-1]
    tail = re.sub(r"\.(html?|php|aspx?)$", "", tail)
    return slugify(tail) if tail else ""


def domain_of(url):
    return urlsplit(url).netloc.lower().replace("www.", "")


def source_from(link_text, url):
    dom = domain_of(url)
    for known, name in SOURCE_BY_DOMAIN.items():
        if dom == known or dom.endswith("." + known):
            m = SOURCE_PREFIX_RE.match(link_text or "")
            return m.group(1) if m else name
    return dom


def strip_source_prefix(link_text):
    """Bo tien to 'Ten nguon:' khoi link text de lay tieu de goc tieng Anh."""
    text = (link_text or "").strip()
    m = SOURCE_PREFIX_RE.match(text)
    if m:
        return text[m.end():].strip()
    return ""


def rss_localname(tag):
    return tag.split("}")[-1]


def parse_rss(content, source_name):
    items = []
    try:
        root = ET.fromstring(content)
    except Exception:
        return items

    # RSS 2.0: channel/item ; Atom: feed/entry
    nodes = root.findall(".//item")
    if not nodes:
        nodes = root.findall(".//{http://www.w3.org/2005/Atom}entry")

    for node in nodes:
        def txt(*names):
            for n in names:
                el = node.find(n)
                if el is None:
                    el = node.find("{http://www.w3.org/2005/Atom}" + n)
                if el is not None and el.text:
                    return el.text
                # link href (atom)
                if el is not None and el.get("href"):
                    return el.get("href")
            return ""

        title = clean_title(txt("title"))
        link = txt("link", "id").strip()
        if link and not link.startswith("http") and link.startswith("incidents"):
            link = "https://status.search.google.com/" + link
        pub = txt("pubDate", "published", "updated")
        desc = strip_html(txt("description", "summary", "content"))
        if title and link.startswith("http"):
            items.append({
                "title": title,
                "url": link,
                "source": source_name,
                "published_at": pub,
                "raw_desc": desc[:600],
            })
    return items


def parse_status_dashboard(content, source_name):
    items = []
    try:
        data = json.loads(content)
    except Exception:
        return items
    if not isinstance(data, list):
        return items
    for inc in data:
        desc = (inc.get("external_desc") or "").strip()
        begin = inc.get("begin") or inc.get("modified")
        uri = inc.get("uri") or ""
        if not desc or not uri:
            continue
        url = "https://status.search.google.com/" + uri if not uri.startswith("http") else uri
        items.append({
            "title": desc,
            "url": url,
            "source": source_name,
            "published_at": begin,
            "raw_desc": desc,
            "official_update": True,
            "status_impact": inc.get("status_impact"),
        })
    return items


# === Gemini Spark daily reports (11_NEWS_FEED): parse -> enrichment + supplemental ===

def parse_report_file(path):
    """Doc 1 file *_daily_report.md -> {date, priority, tags, sections[]}."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    fm = {}
    body = text
    m = re.match(r"^---\n(.*?)\n---\s*", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip().lower()] = v.strip()
        body = text[m.end():]

    date = fm.get("date", "")
    if not re.match(r"^\d{4}-\d{2}-\d{2}", date or ""):
        fd = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
        date = fd.group(1) if fd else ""

    tags = []
    if fm.get("tags"):
        tags = [t.strip() for t in fm["tags"].strip("[]").split(",") if t.strip()]

    sections = []
    parts = re.split(r"(?m)^###\s+(.+?)\s*$", body)
    for i in range(1, len(parts), 2):
        heading = strip_md(parts[i]).strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        content = re.split(r"(?m)^##\s", content)[0]
        content = re.split(r"(?m)^---\s*$", content)[0]
        sections.append({"heading": heading, "content": content})

    return {"date": date, "priority": fm.get("priority", ""),
            "category": fm.get("category", ""), "tags": tags, "sections": sections}


def extract_section_urls(content):
    """Trich cac citation URL tin tuc (article-level) trong 1 section."""
    out = []
    seen = set()
    for link_text, url in re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", content):
        url = url.strip().rstrip(".,")
        dom = domain_of(url)
        if not any(dom == d or dom.endswith("." + d) for d in NEWS_DOMAINS):
            continue
        path = urlsplit(url).path
        if path in GENERIC_PATHS:
            continue  # bo link trang chu / trang danh sach chung
        if "status.search.google.com" in dom and not path.startswith("/incidents"):
            continue  # bo link dashboard chung
        key = norm_url(url)
        if key in seen:
            continue
        seen.add(key)
        out.append((link_text.strip(), url))
    return out


def build_section_summary(content):
    lines = []
    for line in content.splitlines():
        s = strip_md(line.strip())
        if not s.startswith(("- ", "* ")):
            continue
        s = s[2:].strip()
        if not s or s.lower().startswith(("nguồn", "source")):
            continue
        lines.append(s)
        if len(lines) >= 3:
            break
    return truncate(" ".join(lines), 400)


def build_section_action(content):
    actions = []
    current_label = ""
    for line in content.splitlines():
        stripped = line.strip()
        m = BOLD_LABEL_RE.match(stripped)
        if m:
            current_label = m.group(1).strip(" :").lower()
            continue
        if stripped.startswith(("- ", "* ")):
            current_label = ""
            continue
        sm = SUB_BULLET_RE.match(line)
        if sm and current_label and any(k in current_label for k in ACTION_LABEL_KEYWORDS):
            text = strip_md(sm.group(1).strip())
            if text:
                actions.append(text)
                if len(actions) >= 2:
                    break
    return truncate(" ".join(actions), 300)


def parse_news_feed():
    """Doc toan bo Gemini Spark daily reports -> (enrich dict, cited set, stats)."""
    enrich = {}
    cited = set()
    paths = sorted(glob.glob(os.path.join(NEWS_FEED_DIR, "**", "*_daily_report.md"), recursive=True))
    reports = [r for r in (parse_report_file(p) for p in paths) if r["date"]]
    reports.sort(key=lambda r: r["date"])  # report moi hon ghi de report cu
    n_sections = 0
    for rep in reports:
        for sec in rep["sections"]:
            heading = re.sub(r"^\d+\.\s*", "", sec["heading"]).strip()
            low = heading.lower()
            if not heading or "tóm tắt" in low or "executive summary" in low:
                continue
            urls = extract_section_urls(sec["content"])
            if not urls:
                continue
            blob = f"{heading} {strip_md(sec['content'])}"
            category = classify_category(blob, "")
            impact = classify_impact(blob, {"official_update": False})
            tags = extract_tags(blob) or [t.replace("_", " ") for t in rep["tags"][:3]]
            summary = build_section_summary(sec["content"])
            action = build_section_action(sec["content"])
            n_sections += 1
            for link_text, url in urls:
                key = norm_url(url)
                cited.add(key)
                if len(urls) > 1:
                    suffix = f" ({source_from(link_text, url)})"
                    title_vi = truncate(heading, 90 - len(suffix)) + suffix
                else:
                    title_vi = truncate(heading, 90)
                enrich[key] = {
                    "title": title_vi,
                    "title_en": strip_source_prefix(link_text),
                    "summary": summary,
                    "action": action,
                    "category": category,
                    "impact": impact,
                    "tags": tags,
                    "source": source_from(link_text, url),
                    "url": url,
                    "report_date": rep["date"],
                    "priority": rep["priority"],
                }
    stats = {"n_reports": len(reports), "n_sections": n_sections}
    return enrich, cited, stats


def classify_category(text, source):
    low = text.lower()
    for cat, kws in CATEGORY_RULES:
        if any(k in low for k in kws):
            return cat
    return "industry"


def classify_impact(text, item):
    low = text.lower()
    if item.get("official_update"):
        return "high"
    if any(k in low for k in HIGH_KEYWORDS):
        return "high"
    if any(k in low for k in YMYL_FINANCE):
        return "high"
    if any(k in low for k in MEDIUM_KEYWORDS):
        return "medium"
    return "low"


def extract_tags(text):
    low = text.lower()
    return [t for t in TAG_VOCAB if t in low][:5]


def fallback_summary(item):
    src = item["source"]
    date = (item.get("published_at") or "")[:10]
    return f"{src} cập nhật ngày {date}. Cần bổ sung tóm tắt tiếng Việt cho bản tin này."


def fallback_action(category):
    mapping = {
        "google_update": "Rà soát tác động xếp hạng toàn bộ URL tài chính YMYL trên momo.vn trong Search Console ngay sau khi update kết thúc.",
        "ai_search": "Bổ sung cấu trúc trả lời trực tiếp (Direct Answer) để tăng khả năng được AI engine trích dẫn cho các câu hỏi tài chính.",
        "geo": "Chuẩn hóa entity, schema và off-web citation để cải thiện tỉ lệ xuất hiện trong AI Overviews.",
        "technical": "Kiểm tra lại crawl/index/sitemap cho các Hub trọng điểm để đảm bảo không thất thoát lưu lượng organic.",
        "serp_feature": "Tối ưu định dạng nội dung để chiếm SERP Feature cho các truy vấn tài chính tiềm năng cao.",
        "industry": "",
    }
    return mapping.get(category, "")


def fetch_all():
    raw = []
    for src in SOURCES:
        try:
            r = requests.get(src["url"], timeout=20, headers=UA)
            if r.status_code != 200:
                print(f"  [WARN] {src['name']}: HTTP {r.status_code}")
                continue
            if src["type"] == "status":
                items = parse_status_dashboard(r.content.decode("utf-8", "replace"), src["name"])
            else:
                items = parse_rss(r.content, src["name"])
            for it in items:
                it["source_official"] = src.get("official", False)
            raw.extend(items)
            print(f"  [OK] {src['name']}: {len(items)} tin")
        except Exception as e:
            print(f"  [WARN] {src['name']}: {str(e)[:80]}")
    return raw


def normalize_and_filter(raw, spark_cited=None):
    """Loc 60 ngay, bo trung URL. Nguon chinh thong lay het; bao ngoai toi da EXTERNAL_MAX.
    Tin duoc Gemini Spark trich dan duoc uu tien giu slot trong cap external."""
    spark_cited = spark_cited or set()
    cutoff = datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)
    seen = set()

    def clean(items):
        out = []
        for it in items:
            url = (it.get("url") or "").strip()
            if not url or not url.startswith("http"):
                continue  # rule: bo tin khong co url goc
            norm = norm_url(url)
            if norm in seen:
                continue
            dt = parse_date(it.get("published_at"))
            if dt is None or dt < cutoff:
                continue
            seen.add(norm)
            it["_dt"] = dt
            it["published_at"] = dt.astimezone(timezone.utc).strftime("%Y-%m-%d")
            out.append(it)
        return out

    official = clean([it for it in raw if it.get("source_official")])
    external = clean([it for it in raw if not it.get("source_official")])
    official.sort(key=lambda x: x["_dt"], reverse=True)
    external.sort(key=lambda x: (norm_url(x["url"]) in spark_cited, x["_dt"]), reverse=True)
    external = external[:EXTERNAL_MAX]
    out = official + external
    out.sort(key=lambda x: x["_dt"], reverse=True)
    return out


def load_enrichment():
    if not os.path.exists(ENRICHED_PATH):
        return {}
    try:
        with open(ENRICHED_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        overlay = {}
        for row in data if isinstance(data, list) else []:
            u = norm_url((row.get("url") or "").strip())
            if u:
                overlay[u] = row
        return overlay
    except Exception as e:
        print(f"  [WARN] Khong doc duoc enrichment overlay: {e}")
        return {}


IMPACT_RANK = {"high": 3, "medium": 2, "low": 1}


def rank_max(*impacts):
    best = None
    for imp in impacts:
        if imp and IMPACT_RANK.get(imp, 0) > IMPACT_RANK.get(best, 0):
            best = imp
    return best or "low"


def build_item(raw_item, overlay, spark=None):
    """Merge 3 lop: Spark (uu tien) > overlay thu cong > fallback tu dong."""
    spark = spark or {}
    url = raw_item["url"]
    ov = overlay.get(norm_url(url), {})
    blob = f"{raw_item['title']} {raw_item.get('raw_desc','')}"

    category = spark.get("category") or ov.get("category") or classify_category(blob, raw_item["source"])
    impact = rank_max(spark.get("impact"), ov.get("impact"), classify_impact(blob, raw_item))
    tags = [fix_dashes(t) for t in (spark.get("tags") or ov.get("tags") or extract_tags(blob))][:5]
    summary = (spark.get("summary") or ov.get("summary") or "").strip() or fallback_summary(raw_item)
    action = spark.get("action") if spark.get("action") is not None else ov.get("action", None)
    if action is None:
        action = fallback_action(category)

    title_en = fix_dashes(raw_item["title"])
    title_vi = fix_dashes((spark.get("title") or ov.get("title") or "").strip()) or title_en

    return {
        "id": slugify_url(url) or slugify(title_en),
        "title": title_vi,
        "title_en": title_en,
        "summary": fix_dashes(summary),
        "source": raw_item["source"],
        "url": url,
        "published_at": raw_item["published_at"],
        "category": category,
        "impact": impact,
        "tags": tags,
        "action": fix_dashes(action),
    }


def main():
    ap = argparse.ArgumentParser(description="Sync SEO/GEO news -> hubs-momo")
    ap.add_argument("--no-push", action="store_true", help="Chi ghi SSOT local, khong push")
    ap.add_argument("--dump-raw", action="store_true", help="Chi xuat raw items de lam giau")
    ap.add_argument("--skip-insights", action="store_true", help="Bo qua gan insight (chay nhanh)")
    args = ap.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)
    print("Bat dau thu thap tin SEO/GEO tu cac nguon chinh thong...")
    raw = fetch_all()
    print(f"Tong raw: {len(raw)} tin")

    spark_enrich, spark_cited, spark_stats = parse_news_feed()
    print(f"Gemini Spark News Feed: {spark_stats['n_reports']} report, "
          f"{spark_stats['n_sections']} section, {len(spark_enrich)} URL duoc lam giau")

    items = normalize_and_filter(raw, spark_cited)
    print(f"Sau loc (<= {WINDOW_DAYS} ngay; chinh thong lay het + bao ngoai <= {EXTERNAL_MAX}): {len(items)} tin")

    if args.dump_raw:
        with open(RAW_PATH, "w", encoding="utf-8") as f:
            json.dump({"generated_at": now_iso(), "items": [
                {k: v for k, v in it.items() if not k.startswith("_")} for it in items
            ]}, f, ensure_ascii=False, indent=2)
        print(f"Da xuat raw: {RAW_PATH}")
        return

    overlay = load_enrichment()
    if overlay:
        print(f"Da nap enrichment overlay: {len(overlay)} muc")

    built = [build_item(it, overlay, spark_enrich.get(norm_url(it["url"]))) for it in items]
    n_spark = sum(1 for it in items if norm_url(it["url"]) in spark_enrich)

    feed_urls = {norm_url(i["url"]) for i in built}
    supplemental = []
    for key, en in spark_enrich.items():
        if key in feed_urls:
            continue
        spark = dict(en)
        if spark["impact"] == "low" and spark.get("priority", "").startswith("P0"):
            spark["impact"] = "medium"
        raw_item = {
            "title": en["title_en"] or en["title"],
            "url": en["url"],
            "source": en["source"],
            "published_at": en["report_date"],
            "raw_desc": en["summary"],
        }
        supplemental.append(build_item(raw_item, overlay, spark))
        feed_urls.add(key)
    if supplemental:
        print(f"Bo sung tu News Feed (RSS khong lay duoc): {len(supplemental)} tin")

    payload_items = sorted(built + supplemental, key=lambda x: x["published_at"], reverse=True)
    payload = {"generated_at": now_iso(), "items": payload_items}

    if not args.skip_insights:
        try:
            from seo_news_insights import attach_insights
            n_ins = attach_insights(payload["items"], verbose=False)
            print(f"Insight: gan {n_ins}/{len(payload['items'])} tin (chi tin co du lieu that, khong suy dien)")
        except Exception as e:
            print(f"  [WARN] Bo qua gan insight: {str(e)[:90]}")

    with open(SSOT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Da ghi SSOT: {SSOT_PATH} ({len(payload['items'])} tin)")

    if args.no_push:
        print("[no-push] Bo qua push sang hubs-momo.")
        return

    if not os.path.exists(HUBS_REPO):
        print(f"[WARN] Khong tim thay hubs-momo: {HUBS_REPO}")
        return
    os.makedirs(os.path.dirname(HUBS_OUTPUT), exist_ok=True)
    with open(HUBS_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Da push sang hubs-momo: {HUBS_OUTPUT}")

    n_high = sum(1 for i in payload["items"] if i["impact"] == "high")
    print(f"Tong ket: {len(payload['items'])} tin | high={n_high} | lam giau tu Spark: {n_spark} "
          f"| generated_at={payload['generated_at']}")


if __name__ == "__main__":
    main()

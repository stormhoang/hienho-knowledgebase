# -*- coding: utf-8 -*-
"""
URL PROJECT RESOLVER (CORE LIBRARY)
Xác định URL thuộc Project nào dựa trên bảng DIM: WEB_DIM_PAGE_URL (url_info).

Nguồn SSOT: 07_REPORTS/data/web_dim_page_url.csv
Schema: project_name, page_type, type, page_rule

Cơ chế khớp:
- Rule tĩnh (không có '*')  -> khớp chính xác.
- Rule glob (có '*')        -> khớp theo mẫu, ưu tiên rule có tiền tố literal dài nhất (cụ thể nhất).
- Một URL có thể khớp nhiều Project (trùng lặp Blog/News/Tin tức dùng chung) -> trả toàn bộ trong
  `projects`, kèm `primary` (Project chuyên biệt nhất, tức ít rule nhất trong cùng section) và cờ `ambiguous`.
  Khi cộng PV theo Project, dùng `primary` để không đếm trùng.
"""

import os
import re
import csv
import sys
import json
import argparse
import urllib.parse
from collections import Counter, defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_CSV = os.path.join(BASE_DIR, "07_REPORTS", "data", "web_dim_page_url.csv")

# Tự động nạp danh mục dự án SSOT từ hub-map.json của react-web-momo
_HUB_MAP_PATH = os.path.join(BASE_DIR, "..", "Web-Idea", "react-web-momo", "lib", "dashboard", "hub-map.json")
if not os.path.exists(_HUB_MAP_PATH):
    _HUB_MAP_PATH = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/hub-map.json"

_HUB_MAP_PROJECTS = set()
_HUB_MAP_BY_LOWER = {}
if os.path.exists(_HUB_MAP_PATH):
    try:
        with open(_HUB_MAP_PATH, "r", encoding="utf-8") as f:
            _hm = json.load(f)
            for _h in _hm.get("hubs", []):
                for _p in _h.get("projects", []):
                    _p_clean = _p.strip()
                    _HUB_MAP_PROJECTS.add(_p_clean)
                    _HUB_MAP_BY_LOWER[_p_clean.lower()] = _p_clean
    except Exception:
        pass

# Chuẩn hóa tên Project (chỉ dùng khi project không nằm trong hub-map.json)
CANONICAL_PROJECT = {
    "vay nhanh": "Vay Nhanh",
    "phạt nguội": "Phạt Nguội",
    "tnc": "TnC",
    "dịch vụ liên kết": "Dịch vụ liên kết",
    "quản lý chi tiêu": "Quản Lý Chi Tiêu",
    "trung tâm tài chính": "Trung Tâm Tài Chính",
}


# Biến thể chưa khai báo ở trên: tự gộp về cách viết xuất hiện nhiều nhất trong DIM (điền khi load_rules)
_AUTO_CANONICAL = {}


def _canonical_project(name: str, page_type: str = "") -> str:
    n = name.strip()
    # Dự án Cinema: Phân rã theo page_type thành Cinema_Cineplex Page, Cinema_Page, ...
    if n.lower() == "cinema":
        pt = (page_type or "").strip()
        if pt in ("Cineplex Page", "Page", "Home Page", "Blog", "News", "Landing Page"):
            return f"Cinema_{pt}"
        elif pt:
            return f"Cinema_{pt}"
        return "Cinema_Page"

    # Nếu tên đã được khai báo chính xác trong hub-map.json (kể cả case-sensitive), giữ nguyên
    if n in _HUB_MAP_PROJECTS:
        return n

    key = n.lower()
    if key in CANONICAL_PROJECT:
        return CANONICAL_PROJECT[key]
    if key in _HUB_MAP_BY_LOWER:
        return _HUB_MAP_BY_LOWER[key]
    return _AUTO_CANONICAL.get(key) or n


def _build_auto_canonical(names) -> None:
    by_key = defaultdict(Counter)
    for n in names:
        by_key[n.strip().lower()][n.strip()] += 1
    _AUTO_CANONICAL.clear()
    for key, spellings in by_key.items():
        if len(spellings) > 1:
            _AUTO_CANONICAL[key] = sorted(spellings.items(), key=lambda x: (-x[1], x[0]))[0][0]


# ---------------------------------------------------------------------------
# FALLBACK SUY LUẬN (INFERRED) - chỉ dùng khi DIM không khớp.
# Bổ sung rule catch-all cho các section nội dung mà DIM chưa liệt kê.
# specificity: code rule (120) > prefix rule (110) > generic blog (100).
# confidence: high = ánh xạ 1:1 rõ ràng | low = umbrella mặc định.
# ---------------------------------------------------------------------------
# Mã category blog (c116, c193...) -> Project được tính từ DIM trong load_inferred_rules().
# Một mã chỉ được dùng để suy luận khi Project lớn nhất chiếm >= BLOG_CODE_MIN_SHARE số rule của mã đó.
# Mã dùng chung nhiều Project (vd c116: BHYT, Ví Trả Sau, BH xe máy, Vay Nhanh...) không suy luận theo mã,
# URL rơi về rule /blog/* (confidence low) để audit bổ sung vào DIM.
BLOG_CODE_MIN_SHARE = 0.9
BLOG_CODE_MIN_RULES = 3
_BLOG_CODE_RX = re.compile(r"/blog/.*-(c\d+)dt[^/]*$")


def blog_code_owners(rules: list) -> dict:
    """{mã: (project, share, số rule)} cho mọi mã blog xuất hiện trong rule DIM exact."""
    counts = defaultdict(Counter)
    for r in rules:
        if r["kind"] != "exact":
            continue
        m = _BLOG_CODE_RX.search(normalize_url(r["rule"]))
        if m:
            counts[m.group(1)][r["project"]] += 1
    owners = {}
    for code, c in counts.items():
        total = sum(c.values())
        project, n = sorted(c.items(), key=lambda x: (-x[1], x[0]))[0]
        owners[code] = (project, n / total, total)
    return owners


INFERRED_PREFIX = [
    (r"^momo\.vn/cinema/rap(?:/.*)?$", "Cinema_Cineplex Page", "Cineplex Page", "high"),
    (r"^momo\.vn/cinema/blog(?:/.*)?$", "Cinema_Blog", "Blog", "high"),
    (r"^momo\.vn/cinema/lp(?:/.*)?$", "Cinema_Landing Page", "Landing Page", "high"),
    (r"^momo\.vn/cinema/?$", "Cinema_Home Page", "Home Page", "high"),
    (r"^momo\.vn/cinema(?:/.*)?$", "Cinema_Page", "Page", "high"),
    (r"^momo\.vn/tai-chinh/ty-gia(?:/.*)?$", "Tỷ Giá", "Tool Page", "high"),
    (r"^momo\.vn/tai-chinh/gia-vang(?:/.*)?$", "Giá Vàng", "Tool Page", "high"),
    (r"^momo\.vn/tai-chinh/(?:lai-suat|gui-tiet-kiem)(?:/.*)?$", "Lãi Suất", "Tool Page", "high"),
    (r"^momo\.vn/tai-chinh(?:/.*)?$", "Trung Tâm Tài Chính", "Page", "high"),
    (r"^momo\.vn/nhan-tien-quoc-te(?:/.*)?$", "Nhận Tiền Quốc Tế", "Landing Page", "high"),
    (r"^momo\.vn/quy-nhom(?:/.*)?$", "Quỹ Nhóm", "Landing Page", "high"),
    (r"^momo\.vn/quan-ly-chi-tieu(?:/.*)?$", "Quản Lý Chi Tiêu", "Landing Page", "high"),
    (r"^momo\.vn/(?:tien-ich-giao-thong/)?gia-xang(?:/.*)?$", "Giá Xăng", "Tool Page", "high"),
    (r"^momo\.vn/(?:tien-ich-giao-thong/)?garage(?:/.*)?$", "Garage", "Tool Page", "high"),
    (r"^momo\.vn/(?:tien-ich-giao-thong/)?cay-xang(?:/.*)?$", "Cây Xăng", "Tool Page", "high"),
    (r"^momo\.vn/(?:tien-ich-giao-thong/)?tram-sac(?:/.*)?$", "Trạm Sạc", "Tool Page", "high"),
    (r"^momo\.vn/(?:tien-ich-giao-thong/)?hang-xe(?:/.*)?$", "Hãng Xe", "Tool Page", "high"),
    (r"^momo\.vn/tien-ich-giao-thong(?:/.*)?$", "Tiện Ích Giao Thông", "Hub Page", "high"),
    (r"^momo\.vn/(?:hoi-dap|tro-giup|ho-tro)(?:/.*)?$", "Hỏi đáp", "FAQ", "high"),
    (r"^momo\.vn/huong-dan(?:/.*)?$", "Guide", "Guide", "high"),
    (r"^momo\.vn/tin-tuc(?:/.*)?$", "Tin Tức", "News", "high"),
    (r"^momo\.vn/(?:chao-ban-moi|hellomomo|welcome|curated-onboarding)(?:/.*)?$", "New User", "Landing Page", "high"),
    (r"^momo\.vn/download(?:/.*)?$", "Download", "Landing Page", "high"),
    (r"^momo\.vn/tai-app(?:/.*)?$", "Download", "Landing Page", "high"),
    (r"^momo\.vn/?$", "Home MoMo", "Home Page", "high"),
    (r"^momo\.vn/internet(?:/.*)?$", "Internet", "Landing Page", "high"),
    (r"^momo\.vn/nap-tien-dien-thoai(?:/.*)?$", "Nạp tiền điện thoại", "Landing Page", "high"),
    (r"^momo\.vn/(?:tuyen-dung|career)(?:/.*)?$", "Tuyển Dụng", "Career", "high"),
    (r"^momo\.vn/campaign(?:/.*)?$", "Campaign", "Campaign", "high"),
    (r"^momo\.vn/(?:chuong-trinh|voucher)(?:/.*)?$", "Khuyến mãi", "Promotion", "high"),
    (r"^momo\.vn/(?:lixi|nhat-ky-lacxi)(?:/.*)?$", "Game Hub", "Game", "high"),
    (r"^momo\.vn/an-to(?:a|à)n(?:[-/].*)?$", "Trust", "Trust", "high"),
    (r"^momo\.vn/tags(?:/.*)?$", "Blog", "Blog", "high"),
    (r"^momo\.vn/nhantien(?:/.*)?$", "P2P", "Transfer", "high"),
    (r"^momo\.vn/thanh-toan-ung-dung(?:/.*)?$", "Application Store", "Landing Page", "high"),
    (r"^momo\.vn/(?:dieu-khoan|dieu-kien|chinh-sach)(?:[-/].*)?$", "TnC", "Terms", "high"),
    (r"^momo\.vn/napxu(?:-)?tiktok(?:/.*)?$", "Tiktok", "Landing Page", "high"),
    (r"^momo\.vn/vay-nhanh(?:[-/].*)?$", "Vay Nhanh", "Landing Page", "high"),
    (r"^momo\.vn/qua-tang-ban-moi(?:/.*)?$", "New User", "Landing Page", "high"),
    (r"^momo\.vn/xe(?:/.*)?$", "Vé Xe", "Page", "high"),
    (r"^momo\.vn/esim(?:[-/].*)?$", "Esim", "Landing Page", "high"),
    (r"^momo\.vn/bao-hiem(?:[-/].*)?$", "Bảo Hiểm", "Landing Page", "high"),
]


def load_inferred_rules(dim_rules: list = None) -> list:
    """Rule suy luận bổ sung khi DIM không khớp (source='inferred')."""
    if dim_rules is None:
        dim_rules = load_rules()
    rules = []
    for rx, project, ptype, conf in INFERRED_PREFIX:
        rules.append({"project": project, "page_type": ptype, "type": "Inferred",
                      "rule": f"(inferred) {rx}", "regex": re.compile(rx),
                      "kind": "inferred", "specificity": 110, "confidence": conf,
                      "source": "inferred"})
    for code, (project, share, total) in blog_code_owners(dim_rules).items():
        if share < BLOG_CODE_MIN_SHARE or total < BLOG_CODE_MIN_RULES:
            continue
        rx = re.compile(r"^momo\.vn/blog/.*-" + code + r"dt[^/]*$")
        rules.append({"project": project, "page_type": "Blog", "type": "Inferred",
                      "rule": f"(inferred) /blog/*-{code}dt* ({share:.0%} / {total} rule)", "regex": rx,
                      "kind": "inferred", "specificity": 120, "confidence": "high",
                      "source": "inferred"})
    rules.append({"project": "Blog", "page_type": "Blog", "type": "Inferred",
                  "rule": "(inferred) /blog/*", "regex": re.compile(r"^momo\.vn/blog/.*$"),
                  "kind": "inferred", "specificity": 100, "confidence": "low",
                  "source": "inferred"})
    return rules


def normalize_url(url: str) -> str:
    """Chuẩn hóa URL để so khớp: bỏ scheme khác biệt, www, query, fragment, trailing slash, unquote, lowercase."""
    if not url:
        return ""
    u = url.strip()
    if u.startswith("//"):
        u = "https:" + u
    elif u.startswith("/"):
        u = "https://momo.vn" + u
    elif not u.startswith("http"):
        u = "https://" + u
    p = urllib.parse.urlsplit(u)
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    raw_path = urllib.parse.unquote(p.path or "")
    clean_path = re.sub(r"/+", "/", raw_path).rstrip("/")
    clean_path = re.sub(r"/index\.(html?|php)$", "", clean_path, flags=re.I)
    return f"{host}{clean_path}".lower()


def _project_slug(name: str) -> str:
    import unicodedata
    t = str(name).replace("đ", "d").replace("Đ", "D")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("utf-8")
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[-\s]+", "-", t)


def _rule_to_regex(rule: str):
    """Chuyển rule thành (regex, kind, specificity). specificity = độ dài literal (không tính *)."""
    norm = normalize_url(rule)
    if "*" in norm:
        pattern = re.escape(norm).replace(r"\*", ".*")
        spec = len(norm.replace("*", ""))
        return re.compile("^" + pattern + "$", re.IGNORECASE), "glob", spec
    return re.compile("^" + re.escape(norm) + "$", re.IGNORECASE), "exact", len(norm)


_RULES_INDEX = {}


def load_rules(csv_path: str = DEFAULT_CSV) -> list:
    """Nạp và biên dịch toàn bộ rule từ bảng DIM."""
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f)
                if (r.get("project_name") or "").strip().upper() not in ("", "STRING")
                and (r.get("page_rule") or "").strip().startswith("http")]
    _build_auto_canonical(r["project_name"] for r in rows)

    rules = []
    exact_map = defaultdict(list)
    glob_list = []
    for row in rows:
        rule = row["page_rule"].strip()
        rx, kind, spec = _rule_to_regex(rule)
        ptype = (row.get("page_type") or "").strip()
        pname = _canonical_project(row["project_name"], ptype)
        r_item = {
            "project": pname,
            "page_type": ptype,
            "type": (row.get("type") or "").strip(),
            "rule": rule,
            "regex": rx,
            "kind": kind,
            "specificity": spec,
            "source": "dim",
            "confidence": "authoritative",
        }
        rules.append(r_item)
        if kind == "exact":
            norm = normalize_url(rule)
            exact_map[norm].append(r_item)
        else:
            glob_list.append(r_item)
    _RULES_INDEX[id(rules)] = (exact_map, glob_list)
    return rules


def _section(nurl: str) -> str:
    """Section của URL đã chuẩn hóa: mã blog nếu là bài blog, ngược lại là segment đầu của path."""
    m = _BLOG_CODE_RX.search(nurl)
    if m:
        return "blog:" + m.group(1)
    parts = nurl.split("/", 2)
    return parts[1] if len(parts) > 1 else ""


_SECTION_OWNERS = {}


def _section_owners(rules: list) -> dict:
    """{section: Counter(project -> số rule)}, cache theo danh sách rule."""
    cached = _SECTION_OWNERS.get(id(rules))
    if cached is not None and cached[0] is rules:
        return cached[1]
    owners = defaultdict(Counter)
    for r in rules:
        owners[_section(normalize_url(r["rule"]).replace("*", ""))][r["project"]] += 1
    _SECTION_OWNERS[id(rules)] = (rules, owners)
    return owners


def resolve(url: str, rules: list, inferred_rules: list = None) -> dict:
    """
    Xác định Project của 1 URL. DIM luôn ưu tiên tuyệt đối; chỉ khi DIM không khớp
    mới dùng rule suy luận (source='inferred').
    Trả về dict: {url, normalized, matched, source, projects[], primary, ambiguous, matches[]}.
    """
    nurl = normalize_url(url)
    unmatched = {"url": url, "normalized": nurl, "matched": False, "source": None,
                 "projects": [], "primary": "", "ambiguous": False, "matches": []}
    exact, globs = [], []
    exact_map, glob_list = _RULES_INDEX.get(id(rules), (None, None))

    if exact_map is not None:
        if nurl in exact_map:
            exact = exact_map[nurl]
        else:
            for r in glob_list:
                if r["regex"].match(nurl):
                    globs.append(r)
    else:
        for r in rules:
            if r["regex"].match(nurl):
                (exact if r["kind"] == "exact" else globs).append(r)

    if exact:
        matches, match_type, source = exact, "exact", "dim"
    elif globs:
        best = max(r["specificity"] for r in globs)
        matches, match_type, source = [r for r in globs if r["specificity"] == best], "glob", "dim"
    elif inferred_rules:
        inf = [r for r in inferred_rules if r["regex"].match(nurl)]
        if not inf:
            return unmatched
        best = max(r["specificity"] for r in inf)
        matches, match_type, source = [r for r in inf if r["specificity"] == best], "inferred", "inferred"
    else:
        return unmatched

    projects = sorted({r["project"] for r in matches})
    # Nhiều Project cùng khớp:
    # 1. Nếu tên Project có slug khớp trực tiếp với section của URL (vd 'Internet' với section 'internet',
    #    'Nạp tiền điện thoại' với 'nap-tien-dien-thoai', 'Nhận Tiền Quốc Tế' với 'nhan-tien-quoc-te'),
    #    ưu tiên Project chuyên biệt này trước các nhóm bao trùm như 'Billpay', 'Data', 'P2P'.
    # 2. Ngược lại (như trong /blog/*), chọn Project ngách có ít rule nhất trong section. Hòa thì theo tên.
    sec = _section(nurl)
    owners = _section_owners(rules).get(sec, Counter())

    def _p_tiebreak(p):
        p_slug = _project_slug(p)
        exact_sec_match = 0 if (p_slug == sec or p_slug.replace("-", "") == sec.replace("-", "")) else 1
        return (exact_sec_match, owners.get(p, 0), p)

    primary = sorted(projects, key=_p_tiebreak)[0]
    return {
        "url": url,
        "normalized": nurl,
        "matched": True,
        "match_type": match_type,
        "source": source,
        "projects": projects,
        "primary": primary,
        "ambiguous": len(projects) > 1,
        "matches": [{"project": r["project"], "page_type": r["page_type"],
                     "rule": r["rule"], "match_type": r["kind"],
                     "source": r.get("source", "dim"),
                     "confidence": r.get("confidence", "authoritative")} for r in matches],
    }


def resolve_primary(url: str, rules: list, inferred_rules: list = None) -> str:
    """Trả về tên Project chính của URL hoặc '' nếu không khớp."""
    return resolve(url, rules, inferred_rules)["primary"]


def main():
    parser = argparse.ArgumentParser(description="Xác định URL thuộc Project nào (WEB_DIM_PAGE_URL)")
    parser.add_argument("urls", nargs="*", help="Danh sách URL cần phân loại")
    parser.add_argument("--input", help="File chứa danh sách URL (mỗi dòng 1 URL)")
    parser.add_argument("--csv", default=DEFAULT_CSV, help="Đường dẫn bảng DIM (mặc định: SSOT trong repo)")
    parser.add_argument("--json", action="store_true", help="Xuất kết quả dạng JSON")
    parser.add_argument("--list-projects", action="store_true", help="Chỉ liệt kê Project & số rule")
    parser.add_argument("--no-infer", action="store_true", help="Tắt fallback suy luận (chỉ dùng DIM)")
    parser.add_argument("--audit-codes", action="store_true", help="Liệt kê mã blog và Project sở hữu theo DIM")
    args = parser.parse_args()

    rules = load_rules(args.csv)
    inferred = [] if args.no_infer else load_inferred_rules(rules)

    if args.audit_codes:
        print(f"{'MÃ':<6} | {'PROJECT LỚN NHẤT':<26} | {'SHARE':>6} | {'RULE':>5} | SUY LUẬN")
        print("-" * 64)
        for code, (project, share, total) in sorted(blog_code_owners(rules).items(), key=lambda x: -x[1][2]):
            used = share >= BLOG_CODE_MIN_SHARE and total >= BLOG_CODE_MIN_RULES
            print(f"{code:<6} | {project[:26]:<26} | {share:>6.0%} | {total:>5} | {'có' if used else 'không'}")
        return

    if args.list_projects:
        from collections import Counter
        counts = Counter(r["project"] for r in rules)
        print(f"Tổng rule: {len(rules)} | Project: {len(counts)}")
        for p, c in counts.most_common():
            print(f"  {p}: {c}")
        return

    urls = list(args.urls)
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            urls += [ln.strip() for ln in f if ln.strip()]
    if not urls:
        parser.error("Cần cung cấp URL (tham số) hoặc --input")

    results = [resolve(u, rules, inferred) for u in urls]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f"{'URL':<66} | {'PROJECT(S)':<34} | SOURCE/MATCH")
    print("-" * 130)
    for r in results:
        proj = r["primary"] + (f" (+{len(r['projects']) - 1})" if r["ambiguous"] else "") if r["projects"] else "(UNMATCHED)"
        tag = f"{r.get('source','-')}/{r.get('match_type','-')}" if r["matched"] else "-"
        print(f"{r['normalized'][:66]:<66} | {proj[:34]:<34} | {tag}")


if __name__ == "__main__":
    main()

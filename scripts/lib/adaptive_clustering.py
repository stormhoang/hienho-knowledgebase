#!/usr/bin/env python3
"""Động cơ gom cụm từ khóa thích ứng 3 tầng (Adaptive Clustering Engine v2).

SSOT Module: scripts/lib/adaptive_clustering.py
Domain: 05_HUBS / Keyword Intelligence
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any

MIN_CLUSTER_KEYWORDS = 5
MAX_CLUSTERS_NORMAL = 5
MAX_CLUSTERS_MEGA = 10
MEGA_THEME_KW = 5000
MEGA_BRAND_MIN_SHARE = 0.005
CONCEPT_SHARE_MAX = 0.20
MIN_ENTITY_KEYWORDS = 3

GENERIC_TOKENS = {
    "tra", "cuu", "chi", "nhanh", "phong", "giao", "dich", "tong", "dai", "hotline",
    "dia", "chi", "swift", "phi", "bieu", "thu", "tuc", "ho", "so", "dieu", "kien",
    "huong", "dan", "cach", "gia", "lai", "suat", "tiet", "kiem", "gui", "tien",
    "han", "rut", "vay", "von", "tin", "chap", "the", "chap", "tra", "gop", "han",
    "muc", "mo", "khai", "so", "tai", "khoan", "phat", "hanh", "don", "ty", "gia",
    "ngoai", "te", "chuyen", "doi", "euro", "usd", "vnd", "dxy", "kim", "loai",
    "quy", "nhan", "tron", "tay", "mua", "ban", "thanh", "toan", "chuyen", "ke",
    "nhanh", "cau", "hien", "dien", "banh", "thay", "nhot", "chi", "phi", "nuoi",
    "xe", "tieu", "hao", "dang", "kiem", "sang", "ten", "gara", "garage", "cuu",
    "ho", "sua", "rua", "vac", "keo", "phanh", "viem", "pham", "nghi", "dinh",
    "cham", "diem", "bang", "giay", "phep", "camera", "truc", "tuyen", "sinh",
    "nam", "hoc", "hoc", "phu", "bosch", "cong", "viec", "ky", "nang", "sinh",
    "vien", "cong", "thong", "tin", "cuu", "lien", "he", "ve", "chuyen", "di",
    "chuyen", "doi", "diem", "den", "dia", "pham", "mo", "khoa", "lich", "chi",
    "cuoc", "gia", "ban", "cau", "hoc", "den", "nam", "so", "sinh", "vien",
    "cong", "viec", "tuyen", "dung", "khoang", "thu", "le", "am", "lich",
    "tarot", "tranh", "anh", "tu", "vi", "kich", "du", "lien", "tuong",
    "xem", "ket", "qua", "soi", "cau", "thong", "ke", "tuyen", "dau", "duoi",
    "giai", "thuong", "don", "ve", "so", "giai", "thuong", "cau", "keu", "viec",
    "bao", "hiem", "mua", "online", "truc", "tuyen", "cham", "mat", "benh",
    "vien", "gia", "kham", "suc", "khoe", "chi", "so", "index", "bmi", "tdee",
    "calo", "can", "nang", "the", "gioi", "du", "bao", "gia", "vang", "bac",
    "kim", "loai", "quy", "ty", "gia", "co", "phieu", "chung", "khoan", "co",
    "tuc", "lai", "suat", "dau", "tu", "chuyen", "khoan", "giao", "dich",
    "cong", "cuu", "diem", "tin", "dung", "no", "tra", "gop", "the", "tai",
    "san", "co", "tuc", "chung", "chi", "quy", "tien", "gui", "ky", "han",
    "khoa", "vay", "tin", "chay", "the", "chap", "vay", "mua", "nha", "xe",
    "oto", "giao", "dich", "vung", "keu", "vay", "tinh", "dung", "cong",
    "phat", "nguoi", "giao", "thong", "cam", "ung", "dung", "tra", "gop",
    "the", "tai", "khoan", "chuyen", "khoan", "ngan", "hang", "ngan", "hang",
    "dia", "chi", "pho", "giao", "dich", "mua", "ban", "gia", "xe", "lam",
    "banh", "dinh", "nghia", "vay", "tinh", "chap", "phu", "thu", "dich",
    "vay", "muon", "tra", "gop", "hang", "thang", "nam", "chi", "su", "dung",
    "phu", "thu", "hop", "dong", "chi", "tiet", "su", "dung", "cua", "ban",
    "mo", "the", "mo", "the", "tin", "dung", "the", "tinh", "dung", "so",
    "tai", "khoan", "ngan", "hang", "the", "phat", "hanh", "lien", "he",
    "ngan", "hang", "so", "tai", "chi", "nhanh", "giao", "dich", "thanh",
    "toan", "chuyen", "khoan", "ngoai", "te", "chuyen", "doi", "ty", "gia",
    "chuyen", "doi", "ngoai", "te", "mua", "ban", "the", "va", "gi", "la",
    "gi", "nhu", "nao", "bao", "nhieu", "co", "nen", "khong", "khi", "sao",
    "hom", "nay", "nam", "thang", "ngay", "tuan", "nam", "giam", "tang",
    "moi", "nhat", "tai", "day", "tinh", "phu", "thu", "chi", "dich",
}

STOPWORD_HINTS = {
    "la", "gi", "nhu", "nao", "bao", "nhieu", "co", "nen", "khong", "khi",
    "sao", "hom", "nay", "nam", "thang", "ngay", "tuan", "moi", "nhat",
    "tai", "day", "va", "cua", "cho", "cac", "toi", "voi", "tu", "theo",
    "tinh", "phu", "thu", "chi", "dich", "vu", "hay", "bi", "duoc", "nhan",
}

VI_CHARS = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộờớởỡợùúủũụưừứửữựỳýỷỹỵđ")
TOKEN_RE = re.compile(r"[a-zA-Zà-ỹĐđ0-9]+")

CURATED_ENTITIES: dict[str, dict[str, str]] = {
    'Financial': {
        'vietcombank': 'Vietcombank', 'vietcom': 'Vietcombank', 'vcom': 'Vietcombank', 'vcb': 'Vietcombank',
        'techcombank': 'Techcombank', 'techcom': 'Techcombank', 'tcb': 'Techcombank',
        'mbbank': 'MBB', 'mb bank': 'MBB', 'acb': 'ACB', 'bidv': 'BIDV', 'agribank': 'Agribank',
        'vpbank': 'VPBank', 'scb': 'SCB', 'vib': 'VIB', 'shb': 'SHB', 'msb': 'MSB',
        'ocb': 'OCB', 'tpbank': 'TPBank', 'hdbank': 'HDBank',
        'vietinbank': 'VietinBank', 'viettinbank': 'VietinBank', 'vtb': 'VietinBank',
        'eximbank': 'Eximbank', 'seabank': 'Seabank', 'sacombank': 'Sacombank',
        'vndirect': 'VNDirect', 'futu': 'Futu', 'tiger': 'Tiger', 'econstock': 'econstock',
    },
    'cinema': {
        'cgv': 'CGV', 'lotte': 'Lotte', 'galaxy': 'Galaxy', 'bhd': 'BHD', 'beta': 'Beta',
        'cinestar': 'Cinestar', 'quoc gia': 'Quốc Gia', 'dcine': 'Dcine', 'megags': 'MegaGS',
    },
    'vehicle-hub': {
        'honda': 'Honda', 'yamaha': 'Yamaha', 'toyota': 'Toyota', 'suzuki': 'Suzuki',
        'vespa': 'Vespa', 'ban tay ga': 'Bản tay ga',
    },
    'insurtech': {
        'bao viet': 'Bảo Việt', 'baoviet': 'Bảo Việt', 'manulife': 'Manulife',
        'prudential': 'Prudential', 'aia': 'AIA', 'pvi': 'PVI', 'bao minh': 'Bảo Minh',
    },
    'telco': {
        'viettel': 'Viettel', 'vinaphone': 'Vinaphone', 'mobifone': 'Mobifone',
        'vietnamobile': 'VinaMobile', 'gvn': 'g.vn', 'vinacomm': 'Vinacomm',
    },
    'ota': {
        'traveloka': 'Traveloka', 'klook': 'Klook', 'booking': 'Booking', 'agoda': 'Agoda',
    },
    'other': {
        'momo': 'MoMo', 'zalopay': 'ZaloPay', 'vnpay': 'VNPay',
    },
}


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]


def significant_tokens(text: str) -> list[str]:
    return [t for t in tokenize(text) if t not in STOPWORD_HINTS and len(t) > 1]


def title_case(name: str) -> str:
    def cap(w: str) -> str:
        return w[0].upper() + w[1:] if w else w
    parts = (name or "").split(" ")
    out = [cap(p) if p and p[0].islower() and p.isalpha() else p for p in parts]
    return " ".join(out)


def clean_seed_name(keyword: str, max_words: int = 4) -> str:
    k = re.sub(r"[^a-zA-Zà-ỹĐđ0-9\s]", " ", keyword or "")
    k = re.sub(r"\s+", " ", k).strip()
    words = k.split(" ")
    if len(words) > max_words:
        k = " ".join(words[:max_words])
    return title_case(k)


def _has_diacritic(token: str) -> bool:
    return any(ch in token for ch in VI_CHARS)


def _fold(text: str) -> str:
    s = "".join(ch for ch in (text or "").lower() if not _has_diacritic(ch))
    return re.sub(r"[^a-z0-9]+", "", s)


def _is_vietnamese(text: str) -> bool:
    return any(ch in VI_CHARS for ch in (text or "").lower())


def _display_entity(token: str) -> str:
    if len(token) <= 4 and token.isalpha() and not _has_diacritic(token):
        return token.upper()
    return title_case(token)


def slugify(name: str) -> str:
    s = _fold(name).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def catchall_base_name(theme_name: str, pillar_keyword: str) -> str:
    base = (theme_name or "").strip()
    for prefix in ("He Thong ", "Hệ Thống "):
        if base.startswith(prefix):
            base = base[len(prefix):]
            break
    if not base:
        base = (pillar_keyword or "Chu de").strip()
    return title_case(base)


def mine_entities(
    items: list[dict[str, Any]],
    theme_tokens: set[str],
    curated: dict[str, str] | None = None,
    concept_tokens: set[str] | None = None,
    strict: bool = True
) -> dict[str, int]:
    curated = curated or {}
    concept_tokens = concept_tokens or set()
    token_kw = defaultdict(list)
    for it in items:
        for t in set(tokenize(it["keyword"])):
            token_kw[t].append(it)

    n = max(len(items), 1)
    candidates: dict[str, int] = {}
    for tok, kws in token_kw.items():
        if len(kws) < MIN_ENTITY_KEYWORDS:
            continue
        if tok in STOPWORD_HINTS or tok in GENERIC_TOKENS:
            continue
        if tok in theme_tokens or tok in concept_tokens:
            continue
        if tok.isdigit() or len(tok) < 2:
            continue
        share = len(kws) / n
        if share > CONCEPT_SHARE_MAX:
            continue
        if strict and _has_diacritic(tok):
            continue
        vi_ctx = sum(1 for it in kws if _is_vietnamese(it["keyword"]))
        if vi_ctx / len(kws) < 0.6:
            continue
        candidates[tok] = len(kws)

    out: dict[str, int] = {}
    for tok, cnt in sorted(candidates.items(), key=lambda x: -len(x[0])):
        if any(tok != other and tok in other for other in candidates):
            continue
        out[tok] = cnt
    for c_tok in curated:
        c_tok_l = c_tok.lower()
        if c_tok_l in token_kw and len(token_kw[c_tok_l]) >= MIN_ENTITY_KEYWORDS:
            out[c_tok_l] = len(token_kw[c_tok_l])
    return out


def collect_concept_tokens(
    items: list[dict[str, Any]],
    rules: list[Any],
    theme_tokens: set[str],
    top_n: int = 8
) -> set[str]:
    concept: set[str] = set(theme_tokens)
    for rule in rules:
        for tr in rule[1]:
            concept.update(tokenize(tr))
    kw_counter = Counter()
    for it in items[:min(len(items), 100)]:
        for t in tokenize(it["keyword"]):
            if t not in STOPWORD_HINTS and len(t) > 2:
                kw_counter[t] += 1
    for tok, _ in kw_counter.most_common(top_n):
        concept.add(tok)
    return concept


def assign_intent_tier(items: list[dict[str, Any]], rules: list[Any]) -> tuple[list[tuple[str, dict[str, Any]]], list[dict[str, Any]]]:
    assigned: list[tuple[str, dict[str, Any]]] = []
    residual: list[dict[str, Any]] = []

    compiled_rules = []
    for r in rules:
        topic, triggers = r[0], r[1]
        sorted_tr = sorted(triggers, key=lambda t: -len(t.strip()))
        compiled_rules.append((topic, sorted_tr))

    for it in items:
        kw = it["keyword"].lower()
        best_match = None
        best_len = 0
        for topic, triggers in compiled_rules:
            for tr in triggers:
                tr_l = tr.lower()
                if tr_l in kw and len(tr_l) > best_len:
                    best_match = topic
                    best_len = len(tr_l)
        if best_match:
            assigned.append((best_match, it))
        else:
            residual.append(it)
    return assigned, residual


def cluster_residual(items: list[dict[str, Any]], max_clusters: int, pool: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    if not items:
        return []
    items_by_vol = sorted(items, key=lambda x: -x.get("volume", 0))
    clusters: list[dict[str, Any]] = []
    unassigned = list(items_by_vol)

    while unassigned and len(clusters) < max_clusters:
        seed = unassigned[0]
        seed_toks = set(significant_tokens(seed["keyword"]))
        if not seed_toks:
            seed_toks = set(tokenize(seed["keyword"]))

        members = []
        next_unassigned = []
        for it in unassigned:
            it_toks = set(tokenize(it["keyword"]))
            if it == seed or (seed_toks and len(seed_toks & it_toks) >= 1):
                members.append(it)
            else:
                next_unassigned.append(it)

        if len(members) < MIN_CLUSTER_KEYWORDS and len(clusters) > 0:
            clusters[0]["members"].extend(members)
            unassigned = next_unassigned
            continue

        name = clean_seed_name(seed["keyword"])
        clusters.append({
            "name": name,
            "members": members,
            "tier": "residual",
            "seed_volume": seed.get("volume", 0),
        })
        unassigned = next_unassigned

    if unassigned and clusters:
        clusters[0]["members"].extend(unassigned)
    return clusters


def name_has_overlap(name: str, items: list[dict[str, Any]]) -> bool:
    name_toks = set(significant_tokens(name))
    if not name_toks:
        return True
    top_toks = set()
    for it in (items or [])[:min(len(items), 10)]:
        top_toks.update(tokenize(it.get("keyword", "")))
    return bool(name_toks & top_toks)


def refine_cluster_name(cluster: dict[str, Any], pillar_keyword: str, theme_tokens: set[str], rules: list[Any]) -> str:
    name = cluster.get("cluster_name", "")
    members = cluster.get("members", [])
    if not members:
        return name
    if cluster.get("tier") == "entity":
        return name
    if name_has_overlap(name, members):
        return name
    top_kw = members[0].get("keyword", "")
    return clean_seed_name(top_kw)


def merge_shells(clusters: list[dict[str, Any]], min_kw: int = MIN_CLUSTER_KEYWORDS) -> list[dict[str, Any]]:
    healthy: list[dict[str, Any]] = []
    shells: list[dict[str, Any]] = []
    for c in clusters:
        if c.get("count", 0) >= min_kw:
            healthy.append(c)
        else:
            shells.append(c)
    if not healthy:
        return clusters
    for sh in shells:
        sh_toks = set(tokenize(sh.get("cluster_name", "")))
        best = None
        best_sim = -1
        for hc in healthy:
            hc_toks = set(tokenize(hc.get("cluster_name", "")))
            sim = len(sh_toks & hc_toks)
            if sim > best_sim:
                best_sim = sim
                best = hc
        target = best or healthy[0]
        target["members"].extend(sh.get("members", []))
        target["count"] = len(target["members"])
        target["total_volume"] = sum(m.get("volume", 0) for m in target["members"])
    return healthy


def select_clusters(
    clusters: list[dict[str, Any]],
    max_n: int,
    is_mega: bool,
    theme_name: str,
    total_kw: int = 0
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if len(clusters) <= max_n:
        return clusters, []
    intent_c = [c for c in clusters if c.get("tier") == "intent"]
    entity_c = [c for c in clusters if c.get("tier") == "entity"]
    residual_c = [c for c in clusters if c.get("tier") == "residual"]

    selected: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []

    if is_mega:
        selected.extend(intent_c[:3])
        dropped.extend(intent_c[3:])
        min_share_kw = int(total_kw * MEGA_BRAND_MIN_SHARE)
        for ec in sorted(entity_c, key=lambda x: -x.get("count", 0)):
            if ec.get("count", 0) >= min_share_kw:
                selected.append(ec)
            else:
                dropped.append(ec)
        if residual_c:
            selected.append(residual_c[0])
            dropped.extend(residual_c[1:])
    else:
        sorted_all = sorted(clusters, key=lambda x: -x.get("total_volume", 0))
        selected = sorted_all[:max_n]
        dropped = sorted_all[max_n:]
    return selected, dropped


def build_adaptive_clusters_v2(
    canonical_clusters: list[dict[str, Any]],
    sector: str | None = None,
    usecase_slug: str | None = None,
    usecase_name: str | None = None,
    rules: list[Any] | None = None,
    pillar_keyword: str | None = None,
    top_n_clusters: int = 5
) -> list[dict[str, Any]]:
    """Gom cụm thích ứng 3 tầng (Adaptive Clustering v2):

    Tier 1 (Intent Specificity) -> Tier 2 (Entity Mining) -> Tier 3 (Residual Seed & Absorb).
    Triệt tiêu hoàn toàn lỗi fallback dồn rác vào rules[-1].
    """
    total_kw = len(canonical_clusters)
    theme_name = usecase_name or usecase_slug or "Chủ đề"
    pillar_kw = pillar_keyword or (canonical_clusters[0]["keyword"] if canonical_clusters else "")
    theme_tokens = set(significant_tokens(theme_name)) | set(significant_tokens(pillar_kw))
    is_mega = total_kw >= MEGA_THEME_KW
    max_clusters = MAX_CLUSTERS_MEGA if is_mega else top_n_clusters

    active_rules = rules or []

    def to_cluster(name: str, members: list[dict[str, Any]], tier: str, entity: str | None = None) -> dict[str, Any]:
        members_sorted = sorted(members, key=lambda x: (x.get("opportunity_score", 0), x.get("volume", 0)), reverse=True)
        vol = sum(m.get("volume", 0) for m in members_sorted)
        top = members_sorted[:15]
        return {
            "cluster_name": name,
            "count": len(members_sorted),
            "total_volume": vol,
            "tier": tier,
            "entity": entity,
            "slug": slugify(name),
            "no_page": len(members_sorted) < MIN_CLUSTER_KEYWORDS,
            "members": members_sorted,
            "top_keywords": [
                {
                    "keyword": k["keyword"],
                    "volume": k.get("volume", 0),
                    "cluster_volume": k.get("total_cluster_volume", k.get("volume", 0)),
                    "cpc": k.get("cpc", 0.0),
                    "competition": k.get("competition", "Low"),
                    "kd": k.get("kd", 0),
                    "trending": k.get("trending", False),
                    "intent": k.get("intent", "Informational"),
                    "score": k.get("opportunity_score", 0),
                    "quadrant": k.get("quadrant", "Supporting"),
                    "secondary_synonyms": (k.get("secondary_keywords") or [])[:3],
                } for k in top
            ],
        }

    clusters: list[dict[str, Any]] = []
    curated = CURATED_ENTITIES.get(sector or "", {})
    concept_tokens = collect_concept_tokens(canonical_clusters, active_rules, theme_tokens)
    entities = mine_entities(canonical_clusters, theme_tokens, curated, concept_tokens, strict=True)
    curated_tokens = set(curated.keys())

    rule_mentions_entity = any(
        any(ent in [t.lower() for t in tokenize(tr)] or ent in tr.lower()
            for ent in curated_tokens for tr in rule[1])
        for rule in active_rules
    ) if curated_tokens else False

    entity_hits = defaultdict(list)
    groups = defaultdict(list)
    for ent in entities:
        disp = curated.get(ent) or _display_entity(ent)
        groups[disp].append(ent)

    for disp, tokens in groups.items():
        is_curated = any(t in curated_tokens for t in tokens)
        if not is_mega and (not is_curated or rule_mentions_entity):
            continue
        for it in canonical_clusters:
            toks = tokenize(it["keyword"])
            if any(t in toks for t in tokens):
                entity_hits[disp].append(it)

    min_entity_kw = MIN_ENTITY_KEYWORDS if is_mega else max(MIN_ENTITY_KEYWORDS, int(total_kw * 0.03))
    entity_hits = {e: v for e, v in entity_hits.items() if len(v) >= min_entity_kw}

    if is_mega and entity_hits:
        used: set[str] = set()
        for disp, members in sorted(entity_hits.items(), key=lambda x: -len(x[1])):
            if len(members) < MIN_ENTITY_KEYWORDS:
                continue
            valid_m = [m for m in members if m["keyword"] not in used]
            if not valid_m:
                continue
            used.update(m["keyword"] for m in valid_m)
            clusters.append(to_cluster(disp, valid_m, "entity", disp))

        rest = [it for it in canonical_clusters if it["keyword"] not in used]
        assigned, residual = assign_intent_tier(rest, active_rules)
        by_topic = defaultdict(list)
        for topic, it in assigned:
            by_topic[topic].append(it)
        for topic, members in by_topic.items():
            clusters.append(to_cluster(topic, members, "intent"))
        clusters.extend(
            to_cluster(c["name"], c["members"], c["tier"])
            for c in cluster_residual(residual, max_clusters, canonical_clusters)
        )
    else:
        assigned, residual = assign_intent_tier(canonical_clusters, active_rules)
        by_topic = defaultdict(list)
        for topic, it in assigned:
            by_topic[topic].append(it)
        for topic, members in by_topic.items():
            clusters.append(to_cluster(topic, members, "intent"))

        used = set()
        for disp, members in sorted(entity_hits.items(), key=lambda x: -len(x[1])):
            if len(members) < MIN_ENTITY_KEYWORDS:
                continue
            valid_m = [m for m in members if m["keyword"] not in used]
            if not valid_m:
                continue
            used.update(m["keyword"] for m in valid_m)
            clusters.append(to_cluster(disp, valid_m, "entity", disp))

        leftover = [it for it in residual if it["keyword"] not in used]
        clusters.extend(
            to_cluster(c["name"], c["members"], c["tier"])
            for c in cluster_residual(leftover, max_clusters, canonical_clusters)
        )

    for c in clusters:
        c["cluster_name"] = refine_cluster_name(c, pillar_kw, theme_tokens, active_rules)
        if not name_has_overlap(c["cluster_name"], c["top_keywords"]):
            c["cluster_name"] = clean_seed_name(c["top_keywords"][0]["keyword"]) if c["top_keywords"] else c["cluster_name"]

    clusters = merge_shells(clusters)
    selected, dropped = select_clusters(clusters, max_clusters, is_mega, theme_name, total_kw)

    if dropped:
        catch_members = [m for c in dropped for m in c.get("members", [])]
        if len(catch_members) >= MIN_CLUSTER_KEYWORDS:
            catch = to_cluster(f"{catchall_base_name(theme_name, pillar_kw)} khác", catch_members, "catchall")
            selected.append(catch)

    return selected

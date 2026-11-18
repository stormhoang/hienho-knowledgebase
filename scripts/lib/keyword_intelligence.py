# -*- coding: utf-8 -*-
"""
KEYWORD INTELLIGENCE ENGINE (CORE LIBRARY)
Giải quyết 2 lỗ hổng cốt lõi:
1. Multi-signal Weighted Intent Scoring & Dynamic Semantic Outlier Filtering (Không dùng Regex cứng đơn giản).
2. SERP Intent Fingerprinting & Anti-Cannibalization Shield (Triệt tiêu xung đột từ khóa cùng Intent).
"""

import os
import re
import json
import math
import ssl
import urllib.request
import urllib.parse
from collections import defaultdict, Counter

try:
    import lxml.html
    HAS_LXML = True
except ImportError:
    HAS_LXML = False

# Bỏ qua kiểm tra chứng chỉ SSL cho môi trường cào dữ liệu
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

# Từ điển chuẩn hóa thực thể đồng nghĩa & viết tắt (Synonyms & Entities Dictionary)
SYNONYM_MAP = {
    'tiền gửi': 'tiết kiệm',
    'gửi tiết kiệm': 'tiết kiệm',
    'lãi xuất': 'lãi suất',
    'vcb': 'vietcombank',
    'viet com bank': 'vietcombank',
    'tcb': 'techcombank',
    'tech com bank': 'techcombank',
    'ctg': 'vietinbank',
    'viet in bank': 'vietinbank',
    'bid': 'bidv',
    'scb': 'sacombank',
    'vpb': 'vpbank',
    'mbb': 'mbbank',
    'mb bank': 'mbbank',
    'ô tô': 'oto',
    'xe hơi': 'oto',
    'xe oto': 'oto',
    'xe máy': 'xe_may',
    'tphcm': 'tp_hcm',
    'tp hcm': 'tp_hcm',
    'hồ chí minh': 'tp_hcm',
    'sài gòn': 'tp_hcm',
    'hn': 'ha_noi',
    'hà nội': 'ha_noi',
    'đn': 'da_nang',
    'đà nẵng': 'da_nang',
    'gplx': 'bang_lai_xe',
    'bằng lái xe': 'bang_lai_xe',
    'bằng lái': 'bang_lai_xe',
    'giấy phép lái xe': 'bang_lai_xe',
    'bhyt': 'bao_hiem_y_te',
    'bảo hiểm y tế': 'bao_hiem_y_te',
    'bhtn': 'bao_hiem_that_nghiep',
    'bhxh': 'bao_hiem_xa_hoi',
    'tndsv': 'tnds',
    'trách nhiệm dân sự': 'tnds',
}

STOPWORDS = {
    'và', 'là', 'của', 'ở', 'tại', 'cho', 'với', 'trong', 'các', 'những',
    'được', 'có', 'ra', 'khi', 'về', 'này', 'đó', 'từ', 'theo', 'như',
    'để', 'lại', 'thì', 'người', 'cái', 'làm', 'hay', 'bao', 'nhiêu',
    'gì', 'sao', 'nao', 'nào', 'mấy', 'một', 'hai', 'ba', 'bốn', 'năm'
}

TELEX_FIXES = {
    'ddaaus': 'đấu',
    'ddieenj': 'điện',
    'ddoof': 'đồ',
    'ddoongf': 'đồng',
    'ngan hang': 'ngân hàng',
    'tiet kiem': 'tiết kiệm',
    'lai suat': 'lãi suất',
    'bien so': 'biển số',
    'bao hiem': 'bảo hiểm',
    'trả cứu': 'tra cứu',  # lỗi gõ dấu phổ biến của 'tra cứu'
    'o to': 'ô tô',
    'xe may': 'xe máy',
    # Student Hub: lỗi gõ & biến thể thiếu dấu
    'cao đăng': 'cao đẳng',
    'đai học': 'đại học',
    'điêm chuẩn': 'điểm chuẩn',
    'diem chuan': 'điểm chuẩn',
    'thi tôt nghiệp': 'thi tốt nghiệp',
    'phong trọ': 'phòng trọ',
    'phong tro': 'phòng trọ',
    'nha tro': 'nhà trọ',
    'hoc phi': 'học phí',
    'tuyen sinh': 'tuyển sinh',
    'sinh vien': 'sinh viên',
}

# ============================================================
# SHARED HELPERS & UNIFIED CLASSIFIER (SSOT cho toàn pipeline)
# Mọi script (sync_inventory_to_hubs, generate_content_plan,
# keyword_cluster_engine) BẮT BUỘC import từ đây để tránh drift.
# ============================================================

INTENT_WEIGHTS = {
    'Transactional': 2.0,
    'Tool/Calculator': 1.8,
    'Commercial': 1.5,
    'Informational': 1.0,
    'Navigational': 0.7
}

# Ngưỡng phân loại quadrant - nguồn duy nhất toàn pipeline
QUICK_WIN_MIN_VOLUME = 1500
STRATEGIC_PILLAR_MIN_VOLUME = 5000
COMMERCIAL_CONVERTER_MIN_VOLUME = 200

def clean_val(val):
    """Bóc tách công thức Excel '="val"' thành giá trị thực."""
    if not val:
        return ""
    val = val.strip()
    if val.startswith('="') and val.endswith('"'):
        return val[2:-1]
    return val

def normalize_text(text):
    """Chuẩn hóa keyword: lowercase, sửa lỗi gõ Telex/biến thể thiếu dấu, gộp khoảng trắng."""
    text = text.lower().strip()
    for err, fix in TELEX_FIXES.items():
        text = text.replace(err, fix)
    text = re.sub(r'\s+', ' ', text)
    return text

def calculate_opportunity_score(volume, cpc, competition, intent):
    """Opportunity Score = log10(V+1) x (1.2 - CompFactor) x IntentWeight x (1 + CPC Bonus)."""
    weight = INTENT_WEIGHTS.get(intent, 1.0)
    comp_val = competition.lower()
    comp_factor = 0.2
    if 'high' in comp_val:
        comp_factor = 0.8
    elif 'medium' in comp_val:
        comp_factor = 0.5
    elif 'low' in comp_val:
        comp_factor = 0.2

    vol_score = math.log10(volume + 1) if volume > 0 else 0
    cpc_bonus = min(cpc * 0.2, 0.5)

    score = vol_score * (1.2 - comp_factor) * weight * (1.0 + cpc_bonus)
    return round(score, 2)

def classify_quadrant(volume, competition, intent):
    """Phân loại 4 góc phần tư: Quick Win / Strategic Pillar / Commercial Converter / Long-tail.
    Head terms khổng lồ (>= 300k search) hoặc Informational Head (>= 50k search) là Strategic Pillar,
    không thể là Quick Win do độ khó SEO Organic thực tế rất cao.
    """
    comp_val = competition.lower()
    is_high_comp = 'high' in comp_val or 'medium' in comp_val
    is_head_volume = volume >= 300000
    is_info_head = (intent == 'Informational' and volume >= 50000)

    if volume >= STRATEGIC_PILLAR_MIN_VOLUME and (is_high_comp or is_head_volume or is_info_head):
        return 'Strategic Pillar'
    elif volume >= QUICK_WIN_MIN_VOLUME and not is_high_comp and not is_head_volume and not is_info_head:
        return 'Quick Win'
    elif volume >= COMMERCIAL_CONVERTER_MIN_VOLUME and intent in ['Commercial', 'Tool/Calculator', 'Transactional']:
        return 'Commercial Converter'
    else:
        return 'Long-tail / Supporting'

def classify_priority(volume, competition, intent):
    """Ưu tiên sản xuất P0/P1/P2 - suy trực tiếp từ quadrant để không lệch với SSOT."""
    quadrant = classify_quadrant(volume, competition, intent)
    if quadrant == 'Quick Win':
        return 'P0'
    if intent in ['Tool/Calculator', 'Transactional'] and volume >= 500:
        return 'P0'
    if quadrant in ['Strategic Pillar', 'Commercial Converter']:
        return 'P1'
    if volume >= 1000 or intent == 'Commercial':
        return 'P1'
    return 'P2'

# Tập từ điển nhiễu chéo ngành (Cross-domain Alien Collisions)
CROSS_DOMAIN_OUTLIERS = {
    'financial': [
        'giao hàng', 'gửi hàng', 'ghtk', 'ghn', 'shopee express', 'chuyển phát nhanh',
        'bưu điện', 'xe tải', 'game lậu', 'hack', 'mod', 'tín dụng đen', 'xã hội đen',
        'bốc bát họ', 'lừa đảo chiếm đoạt', 'cm88', 'cmanga', 'casino', 'nhà cái',
        'cá cược', 'đánh bạc', 'tài xỉu', 'bắn cá'
    ],
    'vehicle': [
        'gta', 'mod skin', 'mô hình', 'đồ chơi', 'diogo jota', 'fifa', 'pes',
        'tiết kiệm', 'lãi suất ngân hàng', 'chứng chỉ quỹ'
    ],
    'insurtech': [
        'lừa đảo chiếm đoạt', 'bảo hiểm giang hồ', 'game', 'hack'
    ],
    'cinema': [
        # Web phim lậu: thương hiệu bên thứ ba vi phạm bản quyền, không phải intent đặt vé MoMo
        'phimmoi', 'phim moi chill', 'phim mới chill', 'mọt phim', 'motphim', 'phim vn2', 'vn2',
        'phim moi net', 'phim mới net', 'động phim', 'dongphim',
        'phimbathu', 'bilutv', 'tvhay', 'phim88', 'xem phim lậu'
    ],
    'lottery': [
        'soi cầu lừa đảo', 'mua số trúng 100%', 'bán số đề'
    ],
    'hospital': [
        'chữa bệnh bằng bùa', 'thầy lang lừa đảo'
    ],
    'student': [
        'chợ tốt', 'vietnamworks', 'vietnamwork', 'topcv', 'vieclam24h', 'game', 'hack'
    ],
    'ota': [
        'phào chỉ', 'phào nhôm', 'gia phả dòng họ', 'cây gia phả', 'game', 'hack'
    ]
}

# Ma trận trọng số Intent nhiều tín hiệu (Multi-signal Weighted Intent Matrix)
INTENT_WEIGHT_SIGNALS = {
    'Transactional': {
        'keywords': [
            'mở sổ', 'đăng ký', 'đổi biển', 'nộp phạt', 'mua', 'nạp', 'thanh toán',
            'làm thẻ', 'vay ngay', 'tất toán', 'gia hạn', 'đặt vé', 'mở thẻ', 'kích hoạt'
        ],
        'weight': 3.5,
        'action_level': 'high'
    },
    'Tool/Calculator': {
        'keywords': [
            'tính', 'công cụ tính', 'tra cứu', 'kiểm tra', 'check', 'bao nhiêu tiền',
            'lãi bao nhiêu', 'cách tính', 'định giá', 'so sánh giá', 'bảng tính', 'máy tính'
        ],
        'weight': 3.0,
        'action_level': 'high'
    },
    'Commercial': {
        'keywords': [
            'nên', 'tốt nhất', 'so sánh', 'nào tốt', 'lãi suất', 'bảng giá',
            'giá bao nhiêu', 'chi phí', 'ưu đãi', 'đánh giá', 'review', 'kỳ hạn',
            'lãi cao nhất', 'ngân hàng nào', 'loại nào', 'báo giá'
        ],
        'weight': 2.2,
        'action_level': 'medium'
    },
    'Informational': {
        'keywords': [
            'an toàn', 'rủi ro', 'lừa đảo', 'bảo mật', 'có nên', 'kinh nghiệm',
            'hướng dẫn', 'thủ tục', 'quy định', 'hồ sơ', 'điều kiện', 'là gì',
            'ở đâu', 'khái niệm', 'thông tin', 'quy trình', 'ý nghĩa'
        ],
        'weight': 1.8,
        'action_level': 'low'
    },
    'Navigational': {
        'keywords': [
            'login', 'đăng nhập', 'app', 'chi nhánh', 'tổng đài', 'hotline',
            'website', 'vneid', 'dvc', 'cổng dịch vụ công', 'trang chủ'
        ],
        'weight': 2.5,
        'action_level': 'medium'
    }
}

class MultiSignalIntentClassifier:
    """
    Phân loại Search Intent bằng thuật toán tính điểm trọng số đa tín hiệu (Multi-Signal Scoring).
    Giải quyết triệt để xung đột khi từ khóa chứa nhiều từ báo hiệu khác nhau.
    """
    @staticmethod
    def classify(keyword: str) -> dict:
        kw = keyword.lower().strip()
        scores = defaultdict(float)
        matched_signals = defaultdict(list)
        
        # 1. Quét đối sánh đa tín hiệu
        for intent, config in INTENT_WEIGHT_SIGNALS.items():
            base_weight = config['weight']
            for signal in config['keywords']:
                if re.search(r'\b' + re.escape(signal) + r'\b', kw):
                    # Trọng số gia tăng nếu từ chỉ intent nằm ở đầu câu (vị trí chủ đạo của hành vi người dùng)
                    pos_bonus = 1.3 if kw.startswith(signal) else 1.0
                    score_gain = base_weight * pos_bonus
                    scores[intent] += score_gain
                    matched_signals[intent].append(signal)

        # 2. Xử lý xung đột intent đặc thù:
        # Trường hợp "cách tính...": "tính" (Tool) kết hợp "cách" (Info). Người dùng muốn tính cụ thể -> Ưu tiên Tool
        if 'tính' in kw and ('cách' in kw or 'hướng dẫn' in kw):
            scores['Tool/Calculator'] += 1.5

        # Trường hợp "lãi bao nhiêu": Tính lãi cụ thể -> Ưu tiên Tool/Calculator hơn Commercial thuần túy
        if 'lãi bao nhiêu' in kw or 'bao nhiêu tiền' in kw:
            scores['Tool/Calculator'] += 2.0

        # Nếu không có tín hiệu nào khớp rõ ràng -> Mặc định Informational
        if not scores:
            return {
                'intent': 'Informational',
                'confidence': 0.60,
                'scores': {'Informational': 1.0},
                'matched_signals': []
            }

        # Tìm intent có điểm cao nhất
        sorted_intents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_intent, top_score = sorted_intents[0]
        
        total_score = sum(scores.values())
        confidence = round(top_score / total_score, 2) if total_score > 0 else 0.5
        
        return {
            'intent': top_intent,
            'confidence': confidence,
            'scores': dict(scores),
            'matched_signals': matched_signals[top_intent]
        }


class SemanticDomainFilter:
    """
    Bộ lọc ranh giới ngữ nghĩa tự động (Dynamic Domain Boundary Filtering).
    Loại bỏ từ khóa ngoài ngành (Out-of-scope) mà không cần hardcode danh sách cho từng use case.
    """
    @staticmethod
    def is_outlier(keyword: str, sector: str, usecase_slug: str, domain_anchors: set = None) -> tuple:
        kw = keyword.lower().strip()
        sec_key = sector.lower()
        if sec_key not in CROSS_DOMAIN_OUTLIERS:
            sec_key = sec_key.replace('-hub', '')  # thư mục 'vehicle-hub' dùng bộ lọc 'vehicle'
        
        # 1. Kiểm tra đối chiếu với danh mục Alien Outliers của từng ngành
        alien_patterns = CROSS_DOMAIN_OUTLIERS.get(sec_key, [])
        for alien in alien_patterns:
            if alien in kw:
                return True, f"Cross-domain alien keyword: matches '{alien}' in sector '{sector}'"

        # 2. Kiểm tra nếu có domain_anchors truyền vào
        if domain_anchors and len(domain_anchors) > 0:
            kw_tokens = set([t for t in kw.split() if t not in STOPWORDS and len(t) > 1])
            # Nếu không có bất kỳ token nào giao thoa với anchor thực thể cốt lõi của use case
            overlap = kw_tokens.intersection(domain_anchors)
            if len(kw_tokens) >= 3 and len(overlap) == 0:
                return True, f"Zero domain overlap with anchors: {list(domain_anchors)[:4]}"

        # 3. Lọc các mẫu spam/lỗi ký tự đặc biệt
        if re.search(r'[<>{}@#$%^&*()_+=\[\]~`|\\]', kw):
            return True, "Contains illegal special characters/code injection"

        if len(kw) < 2 or len(kw) > 120:
            return True, "Invalid keyword length (<2 or >120 chars)"

        # 4. Lọc single-word noise tokens
        if kw in ['kiệm', 'nhiêu', 'thoại', 'khoản', 'toán', 'phẩm', 'vụ']:
            return True, "Single word noise fragment"

        # 5. Kiểm tra ngoại lệ đặc thù từng Theme
        if usecase_slug == 'vietlott':
            vietlott_tokens = ['vietlott', 'viet lott', 'mega 6 45', 'mega 6/45', 'mega645', 'power 6 55', 'power 6/55', 'power 655', 'keno', 'max 3d', 'max3d', 'max 3d+', 'bingo18', 'bingo 18', 'omg',
                               # đồng bộ BRAND_THEMES['vietlott'] (content_plan_config): sản phẩm con được định tuyến về /vietlott/
                               'power', 'mega', 'bingo', 'max 4d', 'max4d', '3d max', 'xổ số 3d', 'vé số 3d']
            if not any(token in kw for token in vietlott_tokens):
                return True, "Outlier: Vietlott theme only accepts Vietlott brand/product keywords"

        if usecase_slug == 'bao-hiem-nhan-tho' and any(term in kw for term in ['bảo hiểm y tế', 'bảo hiểm y tê', 'bhyt']):
            return True, "Outlier: BHYT keyword in life insurance theme"

        return False, "valid"


def calculate_kd(competition: str, volume: int = 0, cpc: float = 0.0) -> int:
    """
    Tính chỉ số Độ khó từ khóa (Keyword Difficulty - KD 0-100) chuẩn xác
    dựa trên PPC Competition từ kho CSV, Volume tìm kiếm và CPC thực tế.
    """
    comp = str(competition).strip().lower()
    if 'high' in comp or 'cao' in comp:
        base = 65
    elif 'med' in comp or 'trung' in comp:
        base = 40
    else:
        base = 18
    vol_bonus = min(15, math.log10(max(1, volume)) * 2.5) if volume > 10 else 0
    cpc_bonus = min(10, cpc * 3) if cpc > 0 else 0
    kd = round(base + vol_bonus + cpc_bonus)
    return max(5, min(95, kd))


class SERPCannibalizationShield:
    """
    Cơ chế phát hiện SERP Intent Overlap & Triệt tiêu Keyword Cannibalization.
    Tạo Fingerprint chuẩn hóa và gom các từ khóa có cùng kết quả SERP về 1 canonical entry.
    """
    @staticmethod
    def normalize_entities(text: str) -> str:
        text = text.lower().strip()
        for syn, target in SYNONYM_MAP.items():
            text = re.sub(r'\b' + re.escape(syn) + r'\b', target, text)
        return text

    @classmethod
    def generate_intent_fingerprint(cls, keyword: str, intent: str) -> str:
        """
        Tạo mã định danh dấu vân tay (Fingerprint) dựa trên Intent + Tập thực thể đã chuẩn hóa.
        Hai từ khóa có cùng Fingerprint chắc chắn phục vụ cùng 1 trang đích duy nhất.
        """
        norm_text = cls.normalize_entities(keyword)
        # Tách token, loại trừ stopwords, loại bỏ trùng lặp và sắp xếp theo bảng chữ cái
        tokens = sorted(list(set([t for t in norm_text.split() if t not in STOPWORDS and len(t) > 1])))
        token_hash = "_".join(tokens)
        return f"{intent}::{token_hash}"

    @classmethod
    def calculate_token_similarity(cls, kw1: str, kw2: str) -> float:
        """Tính Jaccard Similarity giữa hai tập token thực thể đã chuẩn hóa"""
        n1 = set([t for t in cls.normalize_entities(kw1).split() if t not in STOPWORDS and len(t) > 1])
        n2 = set([t for t in cls.normalize_entities(kw2).split() if t not in STOPWORDS and len(t) > 1])
        if not n1 or not n2:
            return 0.0
        intersection = len(n1.intersection(n2))
        union = len(n1.union(n2))
        return intersection / union if union > 0 else 0.0

    @classmethod
    def cluster_and_shield(cls, keyword_items: list, similarity_threshold: float = 0.70) -> tuple:
        """
        Gom cụm và triệt tiêu Cannibalization:
        - Nhóm các từ có cùng fingerprint hoặc độ tương đồng semantic token >= threshold.
        - Giữ từ khóa có volume lớn nhất làm Primary Keyword.
        - Gom các từ còn lại thành Secondary Synonyms.
        """
        # Sắp xếp danh sách giảm dần theo Volume để từ khóa có volume lớn nhất luôn làm Canonical Leader
        sorted_items = sorted(keyword_items, key=lambda x: x['volume'], reverse=True)
        
        canonical_clusters = []
        merge_log = []
        processed_fingerprints = {}
        token_to_leaders = defaultdict(set)

        for item in sorted_items:
            kw = item['keyword']
            intent = item['intent']
            norm_kw = cls.normalize_entities(kw)
            tokens = set([t for t in norm_kw.split() if t not in STOPWORDS and len(t) > 1])
            fp = f"{intent}::{'_'.join(sorted(tokens))}"

            # Trường hợp 1: Trùng Fingerprint hoàn toàn -> Chắc chắn cannibalized
            if fp in processed_fingerprints:
                leader_idx = processed_fingerprints[fp]
                leader = canonical_clusters[leader_idx]
                leader['secondary_keywords'].append(kw)
                leader['total_cluster_volume'] += item['volume']
                merge_log.append({
                    'merged_keyword': kw,
                    'canonical_primary': leader['keyword'],
                    'reason': f"Exact Intent Fingerprint: {fp}",
                    'volume_added': item['volume']
                })
                continue

            # Trường hợp 2: Kiểm tra Inverted Index - chỉ xét các Leader có chung ít nhất 1 token
            candidates = set()
            for t in tokens:
                if (intent, t) in token_to_leaders:
                    candidates.update(token_to_leaders[(intent, t)])

            merged = False
            for leader_idx in candidates:
                leader = canonical_clusters[leader_idx]
                l_tokens = leader['_tokens']
                union_len = len(tokens.union(l_tokens))
                sim = len(tokens.intersection(l_tokens)) / union_len if union_len > 0 else 0.0
                if sim >= similarity_threshold:
                    leader['secondary_keywords'].append(kw)
                    leader['total_cluster_volume'] += item['volume']
                    processed_fingerprints[fp] = leader_idx
                    merged = True
                    merge_log.append({
                        'merged_keyword': kw,
                        'canonical_primary': leader['keyword'],
                        'reason': f"High Semantic Token Similarity ({round(sim, 2)} >= {similarity_threshold})",
                        'volume_added': item['volume']
                    })
                    break

            if not merged:
                # Trở thành một Canonical Cluster Leader mới
                idx = len(canonical_clusters)
                new_cluster = {
                    'keyword': kw,
                    '_tokens': tokens,
                    'volume': item['volume'],
                    'cpc': item.get('cpc', 0.0),
                    'competition': item.get('competition', 'Low'),
                    'kd': item.get('kd', calculate_kd(item.get('competition', 'Low'), item['volume'], item.get('cpc', 0.0))),
                    'trending': item.get('trending', False),
                    'intent': intent,
                    'opportunity_score': item.get('opportunity_score', 0.0),
                    'quadrant': item.get('quadrant', 'Supporting'),
                    'total_cluster_volume': item['volume'],
                    'secondary_keywords': []
                }
                canonical_clusters.append(new_cluster)
                processed_fingerprints[fp] = idx
                for t in tokens:
                    token_to_leaders[(intent, t)].add(idx)

        # Xóa trường tạm _tokens trước khi return
        for c in canonical_clusters:
            c.pop('_tokens', None)

        return canonical_clusters, merge_log


class MoMoDomainSERPShield:
    """
    Cơ chế đối soát Domain SERP Cannibalization trực tiếp trên Google / Search Engine & MoMo Live Inventory:
    Kiểm tra xem tên miền momo.vn đã có bài viết/URL nào đang xếp hạng hoặc đã index cho Intent/Keyword này chưa.

    Ma trận Rủi ro 4 Cấp độ (Domain SERP Cannibalization Matrix):
    1. CRITICAL (Top 1-3 SERP): MoMo đã sở hữu thứ hạng tuyệt đối.
       -> Khuyến nghị: PROTECT_AND_LINK (Không tạo URL mới. Tránh tự ăn thịt PageRank).
    2. MODERATE (Top 4-20 SERP - Striking Distance): MoMo đã có URL xếp hạng tiềm năng.
       -> Khuyến nghị: REFRESH_EXISTING_URL (Không tạo URL mới. Tối ưu On-page URL cũ để đẩy vào Top 3).
    3. LOW (Không có trong Top 20 SERP, nhưng momo.vn đã có URL live / indexed phù hợp):
       -> Khuyến nghị: CONSOLIDATE_OR_EXPAND (Cập nhật hoặc gộp thực thể vào trang cũ thay vì tạo trang rời rạc).
    4. ZERO (Không có trong Top 20 SERP và chưa từng xuất hiện trên momo.vn):
       -> Khuyến nghị: SAFE_TO_ALLOCATE (Đèn xanh cấp phép phân bổ từ khóa tạo mới trên Web Platform).
    """
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    _live_urls_cache = None
    _gsc_matrix_cache = None

    @classmethod
    def _get_gsc_matrix(cls) -> dict:
        if cls._gsc_matrix_cache is not None:
            return cls._gsc_matrix_cache
        matrix_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "07_REPORTS", "data", "gsc_cannibalization_matrix.json"))
        if not os.path.exists(matrix_path):
            matrix_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "07_REPORTS", "data", "cache", "gsc_cannibalization_matrix.json"))
        if os.path.exists(matrix_path):
            try:
                with open(matrix_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    cls._gsc_matrix_cache = {item['query'].lower().strip(): item for item in data.get('top_cannibalized', [])}
                    return cls._gsc_matrix_cache
            except Exception:
                pass
        cls._gsc_matrix_cache = {}
        return cls._gsc_matrix_cache

    @classmethod
    def _get_live_urls(cls) -> list:
        if cls._live_urls_cache is not None:
            return cls._live_urls_cache
        
        # Thử nạp từ file SSOT nội bộ
        json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "07_REPORTS", "data", "momo_live_urls.json"))
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    cls._live_urls_cache = json.load(f).get('urls', [])
                    return cls._live_urls_cache
            except Exception:
                pass
        
        cls._live_urls_cache = []
        return cls._live_urls_cache

    @staticmethod
    def _remove_accents(text: str) -> str:
        import unicodedata
        text = unicodedata.normalize('NFD', text)
        text = re.sub(r'[\u0300-\u036f]', '', text)
        text = text.replace('đ', 'd').replace('Đ', 'D')
        return text

    @classmethod
    def find_sitemap_matches(cls, query: str, sector: str = None, threshold: float = 0.6) -> list:
        """Kiểm tra đối chiếu với toàn bộ URLs đã xuất bản chính thức trên momo.vn kèm lọc Cross-Sector"""
        live_urls = cls._get_live_urls()
        if not live_urls:
            return []

        clean_q = cls._remove_accents(query.lower()).strip()
        q_slug = re.sub(r'[^a-z0-9]+', '-', clean_q).strip('-')
        q_tokens = set([t for t in clean_q.split() if len(t) > 1 and t not in STOPWORDS])
        if not q_tokens:
            q_tokens = set(clean_q.split())

        # Khớp chính xác slug theo ranh giới từ để tránh lỗi dính từ (ví dụ scotty-giai-cuu dính ty-gia)
        slug_boundary_regex = re.compile(r'(^|[-/])' + re.escape(q_slug) + r'([-/]|$)')

        # Danh sách chặn tiền tố chéo Sector để triệt tiêu việc Cinema blog ăn vào Tài chính / Xổ số
        forbidden_prefixes = []
        if sector == 'Financial':
            forbidden_prefixes = ['/cinema/', '/xsmb', '/xsmn', '/xsmt', '/xo-so', '/ve-so', '/game-app', '/nap-the-game']
        elif sector == 'vehicle-hub':
            forbidden_prefixes = ['/cinema/', '/tai-chinh/', '/xsmb']
        elif sector == 'other':
            forbidden_prefixes = ['/cinema/', '/du-lich', 'du-lich-va-van-tai', '/bao-hiem', '/ve-may-bay']
        elif sector in ['Lottery', 'hospital', 'insurtech', 'telco', 'ota']:
            forbidden_prefixes = ['/cinema/']

        exact_matches = []
        token_matches = []

        for u in live_urls:
            path = u.replace('https://www.momo.vn/', '').lower()

            # Chặn chéo sector
            if any(fb in u for fb in forbidden_prefixes):
                continue

            # 1. Khớp chính xác slug theo ranh giới từ
            if slug_boundary_regex.search(path):
                exact_matches.append(u)
                continue

            path_tokens = set(re.findall(r'[a-z0-9]+', path))
            # Tránh nhầm lẫn từ đa nghĩa: nếu path là du-lich hoặc lich-su nhưng query không chứa du/su
            if 'du-lich' in path and 'du' not in q_tokens and 'lich' in q_tokens:
                path_tokens.discard('lich')
            if 'lich-su' in path and 'su' not in q_tokens and 'lich' in q_tokens:
                path_tokens.discard('lich')

            overlap = q_tokens.intersection(path_tokens)
            if not overlap:
                continue

            coverage = len(overlap) / len(q_tokens)
            jaccard = len(overlap) / len(q_tokens.union(path_tokens))

            # Yêu cầu độ tương đồng Jaccard hợp lý để tránh bài viết dài ngẫu nhiên chứa 2 từ đơn
            if coverage >= 0.65 and jaccard >= 0.20:
                score = coverage * 10.0 + jaccard * 10.0
                if sector == 'Financial' and ('tai-chinh' in path or 'ty-gia' in path or 'ngan-hang' in path):
                    score += 5.0
                token_matches.append((score, u))

        if exact_matches:
            return exact_matches[:3]
        token_matches.sort(key=lambda x: x[0], reverse=True)
        return [u for _, u in token_matches[:3]]

    @classmethod
    def check_live_serp_presence(cls, query: str, limit: int = 20) -> dict:
        """Kiểm tra sự hiện diện của momo.vn trên bảng xếp hạng tìm kiếm tự nhiên (Organic SERP)"""
        if not HAS_LXML:
            return {'error': 'lxml is not available', 'momo_rankings': []}

        headers = {
            'User-Agent': cls.USER_AGENT,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        data = urllib.parse.urlencode({'q': query, 'kl': 'vn-vi'}).encode('utf-8')
        req = urllib.request.Request('https://html.duckduckgo.com/html/', data=data, headers=headers)
        
        momo_rankings = []
        try:
            with urllib.request.urlopen(req, timeout=8, context=ssl_ctx) as resp:
                html_text = resp.read().decode('utf-8', errors='ignore')
                tree = lxml.html.fromstring(html_text)
                rank = 0
                for r in tree.xpath('//div[contains(@class, "result__body")]'):
                    a = r.xpath('.//a[contains(@class, "result__url")]')
                    title_el = r.xpath('.//h2[contains(@class, "result__title")]//a')
                    snippet_el = r.xpath('.//a[contains(@class, "result__snippet")]')
                    if a and title_el:
                        rank += 1
                        raw_url = a[0].get('href', '').strip()
                        if '/l/?kh=-1&uddg=' in raw_url:
                            parsed = urllib.parse.parse_qs(urllib.parse.urlparse(raw_url).query).get('uddg')
                            if parsed:
                                raw_url = parsed[0]
                        domain = urllib.parse.urlparse(raw_url).netloc.lower()
                        if 'momo.vn' in domain:
                            title = title_el[0].text_content().strip()
                            snippet = snippet_el[0].text_content().strip() if snippet_el else ""
                            momo_rankings.append({
                                'rank': rank,
                                'url': raw_url,
                                'title': title,
                                'snippet': snippet
                            })
                    if rank >= limit:
                        break
        except Exception as e:
            return {'error': str(e), 'momo_rankings': []}
            
        return {'momo_rankings': momo_rankings}

    @classmethod
    def evaluate_cannibalization_risk(cls, query: str, sector: str = None, check_live_serp: bool = True) -> dict:
        """Đánh giá toàn diện rủi ro Domain Cannibalization và trả về Ma trận Quyết định chuẩn xác"""
        # 1. Đối soát trước với dữ liệu thực tế từ Google Search Console (GSC Ground Truth)
        clean_q_key = query.lower().strip()
        gsc_match = cls._get_gsc_matrix().get(clean_q_key)
        if gsc_match:
            pages = gsc_match.get('competing_pages', [])
            # Lọc bỏ pages cross-sector bị rác nếu có
            if sector == 'Financial':
                pages = [p for p in pages if '/cinema/' not in p['url']]
            top_p = pages[0] if pages else None
            top_url = top_p['url'] if top_p else None
            best_rank = int(round(top_p['position'])) if top_p and top_p.get('position') else None
            risk_level = gsc_match.get('risk_level', 'CRITICAL')
            action = gsc_match.get('recommended_action', 'CANONICAL_OR_301_CONSOLIDATE')
            verdict = "BLOCK_NEW_URL" if risk_level == "CRITICAL" else "CONSOLIDATE"
            rationale = (
                f"Google Search Console xác nhận {len(pages)} URLs của momo.vn đang cạnh tranh trực tiếp truy vấn này "
                f"({gsc_match.get('total_impressions', 0):,} impressions, {gsc_match.get('total_clicks', 0):,} clicks). "
                f"URL nhận nhiều click nhất: {top_url} (Top ~{best_rank}). "
                f"Hành động tối ưu: Hợp nhất (Consolidate) nội dung hoặc cắm Canonical về URL chính để tránh tự ăn thịt thứ hạng."
            )
            return {
                'query': query,
                'risk_level': risk_level,
                'verdict': verdict,
                'action': action,
                'serp_rank': best_rank,
                'ranking_url': top_url,
                'ranking_title': None,
                'sitemap_matches': [p['url'] for p in pages],
                'top_live_url': top_url,
                'rationale': rationale,
                'competing_pages': pages,
                'live_rankings': []
            }

        momo_rankings = []
        if check_live_serp:
            serp_res = cls.check_live_serp_presence(query, limit=20)
            momo_rankings = serp_res.get('momo_rankings', [])
        
        best_rank = momo_rankings[0]['rank'] if momo_rankings else None
        top_url = momo_rankings[0]['url'] if momo_rankings else None
        top_title = momo_rankings[0]['title'] if momo_rankings else None

        # Đối soát với Sitemap SSOT nội bộ có bóc tách sector
        sitemap_hits = cls.find_sitemap_matches(query, sector=sector)

        # Phân loại theo Ma trận
        if best_rank is not None and best_rank <= 3:
            risk_level = "CRITICAL"
            verdict = "BLOCK_NEW_URL"
            action = "PROTECT_AND_LINK"
            rationale = (
                f"Tên miền momo.vn đang giữ vị trí Top {best_rank} ({top_url}) trên SERP. "
                f"Tuyệt đối KHÔNG tạo URL mới vì sẽ gây hiện tượng tự ăn thịt thứ hạng (Self-Cannibalization). "
                f"Hành động tối ưu: Giữ URL hiện tại, cắm widget tra cứu/chuyển đổi và tối ưu internal link."
            )
        elif best_rank is not None and 4 <= best_rank <= 20:
            risk_level = "MODERATE"
            verdict = "BLOCK_NEW_URL"
            action = "REFRESH_EXISTING_URL"
            rationale = (
                f"Tên miền momo.vn đã có URL xếp hạng Top {best_rank} ({top_url}) trong vùng Striking Distance (Top 4-20). "
                f"Tuyệt đối KHÔNG tạo trang mới để cạnh tranh. "
                f"Hành động tối ưu: Thực hiện Content Refresh & On-page Upgrade trên chính URL này để đưa bài viết vào Top 3."
            )
        elif sitemap_hits:
            risk_level = "LOW"
            verdict = "CONSOLIDATE"
            action = "UPDATE_OR_REDIRECT"
            first_idx = sitemap_hits[0]
            rationale = (
                f"momo.vn đã có URL chính thức xuất bản trên hệ thống: {first_idx}. "
                f"Hành động tối ưu: Cập nhật nội dung hoặc bổ sung Sub-intent vào URL này, tránh tạo URL mới trùng lặp."
            )
        else:
            risk_level = "ZERO"
            verdict = "SAFE_TO_ALLOCATE"
            action = "ALLOCATE_NEW"
            rationale = (
                f"Tên miền momo.vn chưa có bài viết nào trên SERP hoặc trong hệ thống cho chủ đề này. "
                f"Đèn xanh (Green Light): Cho phép phân bổ từ khóa và tạo mới trang trên Web Platform."
            )

        return {
            'query': query,
            'risk_level': risk_level,
            'verdict': verdict,
            'action': action,
            'serp_rank': best_rank,
            'ranking_url': top_url,
            'ranking_title': top_title,
            'sitemap_matches': sitemap_hits,
            'top_live_url': top_url or (sitemap_hits[0] if sitemap_hits else None),
            'rationale': rationale,
            'live_rankings': momo_rankings
        }


class StructuredSchemaGenerator:
    """
    Tự động sinh JSON-LD Structured Data Schema chuẩn Google Search Central:
    - FAQPage Schema cho các cụm câu hỏi và công cụ tra cứu.
    - BreadcrumbList Schema cho cấu trúc phân tầng Hub -> Sector -> Use Case.
    """
    @staticmethod
    def generate_faq_jsonld(usecase_name: str, qa_pairs: list) -> dict:
        entities = []
        for q, a in qa_pairs:
            entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })
        return {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "name": f"Hỏi đáp thường gặp về {usecase_name}",
            "mainEntity": entities
        }

    @staticmethod
    def generate_breadcrumb_jsonld(sector: str, usecase_name: str, usecase_slug: str, base_url: str = "https://momo.vn") -> dict:
        sector_slug = sector.lower().replace('_', '-').replace(' ', '-')
        return {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Trang chủ",
                    "item": base_url
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": sector.title(),
                    "item": f"{base_url}/{sector_slug}"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": usecase_name,
                    "item": f"{base_url}/{usecase_slug.strip('/')}"
                }
            ]
        }


class ContentBriefGenerator:
    """
    Tự động tạo Content Brief chi tiết cho từng bài viết:
    - Dự toán dung lượng bài viết (Word Count Target)
    - Dàn ý H2/H3 Entity Checklist bắt buộc
    - Hướng dẫn liên kết nội bộ và CTA Web-to-App
    """
    @staticmethod
    def estimate_word_count(format_type: str, intent: str, cluster_volume: int) -> dict:
        if 'Pillar' in format_type or cluster_volume >= 20000:
            return {'min_words': 2500, 'target_words': 3500, 'tier': 'Master Hub Pillar'}
        elif intent in ('Tool/Calculator', 'Transactional'):
            return {'min_words': 1500, 'target_words': 2200, 'tier': 'High Conversion Guide'}
        elif intent == 'Commercial':
            return {'min_words': 1800, 'target_words': 2500, 'tier': 'Comparison & Review'}
        else:
            return {'min_words': 1200, 'target_words': 1600, 'tier': 'Educational Spoke'}

    @classmethod
    def generate_outline_checklist(cls, page_plan: dict, usecase_name: str) -> list:
        kw = page_plan['primary_kw']
        intent = page_plan['intent']
        sec_kws = page_plan.get('secondary_kws', [])
        
        outline = [
            f"## H2 1: Tổng quan & Khái niệm cốt lõi về {kw}",
            f"## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất"
        ]
        
        if intent == 'Tool/Calculator':
            outline.extend([
                f"## H2 3: Hướng dẫn sử dụng công cụ tính toán / tra cứu trực tuyến trên Web",
                f"### H3 3.1: Các bước điền tham số và cách đọc kết quả",
                f"## H2 4: Công thức tính và ví dụ thực tế minh họa từng bước"
            ])
        elif intent == 'Commercial':
            outline.extend([
                f"## H2 3: So sánh chi tiết các lựa chọn hàng đầu trên thị trường hiện nay",
                f"### H3 3.1: Ưu và nhược điểm của từng đơn vị cung cấp",
                f"## H2 4: Lời khuyên nên chọn giải pháp nào tối ưu nhất theo nhu cầu"
            ])
        elif intent == 'Transactional':
            outline.extend([
                f"## H2 3: Hồ sơ và điều kiện cần chuẩn bị trước khi thực hiện",
                f"## H2 4: Quy trình 3 bước thực hiện giao dịch nhanh chóng trên điện thoại"
            ])
        else:
            outline.extend([
                f"## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi",
                f"## H2 4: Những sai lầm thường gặp và cách phòng tránh"
            ])

        # Đề mục FAQ chuẩn Schema
        outline.append(f"## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về {kw}")
        for idx, s in enumerate(sec_kws[:3], 1):
            outline.append(f"### H3 5.{idx}: {s.capitalize()}?")
            
        outline.append("## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo")
        return outline


class InternalLinkingTopologyEngine:
    """
    Xây dựng mạng lưới liên kết nội bộ phân tầng (Internal Linking & Silo Matrix):
    - Parent Hub: Liên kết ngược về Hub trụ cột của phân khối.
    - Peer In-Silo: 3-5 Use Cases cùng ngành có độ tương đồng ngữ nghĩa cao nhất.
    - Cross-Silo Bridges: Liên kết chéo ngành có tính chất bổ trợ chuyển đổi tự nhiên (Vehicle <-> Insurtech, Financial <-> Vehicle).
    """
    SECTOR_HUB_MAP = {
        'Financial': {'name': 'Tài Chính & Ngân Hàng', 'url': '/tai-chinh', 'anchor': 'Cổng dịch vụ Tài chính MoMo'},
        'vehicle-hub': {'name': 'Giao Thông & Tiện Ích Xe', 'url': '/xe', 'anchor': 'Trung tâm tiện ích Giao thông & Hồ sơ xe'},
        'insurtech': {'name': 'Bảo Hiểm Số', 'url': '/bao-hiem', 'anchor': 'Sàn giao dịch Bảo hiểm trực tuyến MoMo'},
        'ota': {'name': 'Du Lịch & Đi Lại', 'url': '/du-lich', 'anchor': 'Cổng đặt vé máy bay & Khách sạn MoMo Travel'},
        'Lottery': {'name': 'Xổ Số & Trúng Thưởng', 'url': '/xo-so', 'anchor': 'Tra cứu kết quả & Vé số Vietlott MoMo'},
        'hospital': {'name': 'Y Tế & Viện Phí', 'url': '/y-te', 'anchor': 'Thanh toán viện phí & Dịch vụ Y tế MoMo'},
        'telco': {'name': 'Viễn Thông & 4G/5G', 'url': '/vien-thong', 'anchor': 'Cổng Nạp điện thoại & Data 4G/5G'},
        'MDS': {'name': 'Dịch Vụ Đời Sống', 'url': '/dich-vu-doi-song', 'anchor': 'Thanh toán hóa đơn & Dịch vụ sinh hoạt'},
        'PS': {'name': 'Giải Trí & Mua Sắm', 'url': '/giai-tri', 'anchor': 'Đặt vé xem phim & Giải trí MoMo'},
        'trust': {'name': 'Xác Thực & Uy Tín', 'url': '/xac-thuc', 'anchor': 'Cổng bảo mật & Xác thực an toàn MoMo'},
        'other': {'name': 'Tiện Ích Nền Tảng', 'url': '/tien-ich', 'anchor': 'Hệ sinh thái tiện ích Web MoMo'},
    }

    CROSS_SECTOR_RULES = [
        ('vehicle-hub', 'insurtech', ['bảo hiểm', 'tnds', 'tai nạn', 'vật chất', 'xe máy', 'ô tô']),
        ('Financial', 'vehicle-hub', ['vay', 'mua xe', 'trả góp', 'định giá', 'thế chấp']),
        ('ota', 'insurtech', ['bảo hiểm', 'du lịch', 'chuyến bay', 'trễ chuyến']),
        ('hospital', 'insurtech', ['bảo hiểm', 'y tế', 'sức khỏe', 'viện phí']),
        ('telco', 'Financial', ['nạp tiền', 'thanh toán', 'ví trả sau', 'chiết khấu']),
        ('MDS', 'Financial', ['hóa đơn', 'ví trả sau', 'trả chậm', 'tiết kiệm']),
    ]

    @classmethod
    def extract_keywords_tokens(cls, usecase: dict) -> set:
        raw_text = f"{usecase.get('id', '')} {usecase.get('name', '')}"
        tokens = set(re.findall(r'\b\w{2,}\b', raw_text.lower()))
        for kw_item in usecase.get('top_opportunities', [])[:10]:
            kw_str = kw_item.get('keyword', '')
            tokens.update([t for t in kw_str.lower().split() if len(t) > 2 and t not in STOPWORDS])
        return tokens

    @classmethod
    def build_silo_matrix(cls, current_usecase: dict, all_usecases: list) -> dict:
        cur_id = current_usecase['id']
        cur_sec = current_usecase['sector']
        cur_tokens = cls.extract_keywords_tokens(current_usecase)
        parent_hub = cls.SECTOR_HUB_MAP.get(cur_sec, cls.SECTOR_HUB_MAP['other'])

        # 1. Tìm Peer In-Silo (Cùng phân khối)
        peer_candidates = []
        for u in all_usecases:
            if u['id'] == cur_id or u['sector'] != cur_sec:
                continue
            u_tokens = cls.extract_keywords_tokens(u)
            overlap = len(cur_tokens.intersection(u_tokens))
            sim = overlap / len(cur_tokens.union(u_tokens)) if cur_tokens.union(u_tokens) else 0.0
            
            # Gợi ý anchor text tối ưu từ pillar keyword hoặc top opportunity
            p_kw = u.get('pillar_keyword', {}).get('keyword') or u.get('name', '')
            peer_candidates.append({
                'target_id': u['id'],
                'target_name': u['name'],
                'target_url': f"/{u['id']}/",
                'suggested_anchor': p_kw,
                'similarity_score': round(sim, 3),
                'volume': u.get('total_volume', 0)
            })

        # Sắp xếp ưu tiên: similarity cao nhất, sau đó đến volume
        peer_candidates.sort(key=lambda x: (x['similarity_score'], x['volume']), reverse=True)
        peer_links = peer_candidates[:4]

        # 2. Tìm Cross-Silo Bridges (Cầu nối liên kết xuyên ngành)
        cross_bridges = []
        for u in all_usecases:
            if u['sector'] == cur_sec:
                continue
            target_sec = u['sector']
            
            # Kiểm tra xem có luật tương hỗ giữa 2 ngành không
            is_compatible = False
            for s1, s2, triggers in cls.CROSS_SECTOR_RULES:
                if (cur_sec == s1 and target_sec == s2) or (cur_sec == s2 and target_sec == s1):
                    # Kiểm tra xem có token trigger nào xuất hiện
                    u_tokens = cls.extract_keywords_tokens(u)
                    if any(tr in ' '.join(cur_tokens) or tr in ' '.join(u_tokens) for tr in triggers):
                        is_compatible = True
                        break
            
            if is_compatible:
                u_tokens = cls.extract_keywords_tokens(u)
                overlap = len(cur_tokens.intersection(u_tokens))
                p_kw = u.get('pillar_keyword', {}).get('keyword') or u.get('name', '')
                cross_bridges.append({
                    'target_id': u['id'],
                    'target_sector': target_sec,
                    'target_name': u['name'],
                    'target_url': f"/{u['id']}/",
                    'suggested_anchor': p_kw,
                    'overlap_tokens': overlap,
                    'volume': u.get('total_volume', 0)
                })

        cross_bridges.sort(key=lambda x: (x['overlap_tokens'], x['volume']), reverse=True)
        selected_bridges = cross_bridges[:2]

        return {
            'parent_hub': {
                'title': parent_hub['name'],
                'url': parent_hub['url'],
                'anchor': parent_hub['anchor']
            },
            'peer_in_silo': peer_links,
            'cross_silo_bridges': selected_bridges
        }


class GEODirectAnswerGenerator:
    """
    Sinh nội dung tối ưu cho Tìm kiếm Tạo sinh (Generative Engine Optimization - GEO):
    Phục vụ trích dẫn trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini.
    Được thiết kế theo cấu trúc Ontology đa tầng: Nhận diện Archetype thực thể nghiệp vụ
    đặc thù (Savings, Loan, Gold/FX, Securities, Fines, Motor Insurance, BHYT/BHXH, Cinema, Telco...)
    để cung cấp số liệu định lượng, căn cứ pháp lý và giá trị Information Gain cao nhất.
    """
    @staticmethod
    def _resolve_archetype(usecase_name: str, sector: str, usecase_slug: str = None) -> str:
        text = f"{usecase_slug or ''} {usecase_name} {sector}".lower()
        if any(k in text for k in ['gui-tiet-kiem', 'tiet-kiem', 'lai-suat', 'tich-luy', 'chung-chi-tien-gui', 'lai-kep']):
            return 'savings'
        if any(k in text for k in ['diem-tin-dung', 'no-xau', 'cic']):
            return 'credit_score_cic'
        if any(k in text for k in ['vay', 'tin-chap', 'the-chap', 'lai-vay', 'the-tin-dung', 'vi-tra-sau', 'thau-chi', 'tra-gop', 'du-no']):
            return 'loan_credit'
        if any(k in text for k in ['gia-vang', 'vang', 'bac', 'ty-gia', 'ngoai-te', 'doi-tien', 'kieu-hoi']):
            return 'gold_fx'
        if any(k in text for k in ['chung-khoan', 'co-phieu', 'trai-phieu', 'chung-chi-quy', 'quy-etf', 'phai-sinh', 'ma-chung-khoan', 'dau-tu', 'crypto']):
            return 'investment_securities'
        if any(k in text for k in ['thue-tncn', 'ma-so-thue', 'tinh-luong', 'giam-tru-gia-canh', 'thue']):
            return 'tax_salary'
        if any(k in text for k in ['phat-nguoi', 'loi-giao-thong', 'dang-kiem', 'giay-phep-lai-xe', 'thi-bang-lai-xe']):
            return 'traffic_fines'
        if any(k in text for k in ['bien-so', 'sang-ten-xe', 'thue-truoc-ba']):
            return 'vehicle_plate_reg'
        if any(k in text for k in ['gara', 'sua-xe', 'rua-xe', 'cuu-ho', 'bao-duong', 'dinh-gia-xe', 'gia-xe', 'gia-xang', 'gia-dau', 'tram-sac', 'doi-pin', 'vetc', 'epass']):
            return 'vehicle_maintenance'
        if any(k in text for k in ['bao-hiem-xe-may', 'bao-hiem-o-to', 'phi-bao-hiem']):
            return 'insurance_motor'
        if any(k in text for k in ['bhyt', 'bhxh', 'bao-hiem-nhan-tho', 'bao-hiem-tai-nan', 'bao-hiem-chay-no']):
            return 'insurance_health_social'
        if any(k in text for k in ['rap', 've-xem-phim', 'lich-phim', 'dat-phim', 'phim']):
            return 'cinema_tickets'
        if any(k in text for k in ['ve-may-bay', 've-tau', 've-xe', 've-cap-treo', 'tour-du-lich', 'du-lich', 'dat-resort', 'visa-du-lich']):
            return 'ota_travel'
        if any(k in text for k in ['data-4g', 'nap-tien-dien-thoai', 'sim', 'esim']):
            return 'telco_data'
        if any(k in text for k in ['benh-vien', 'dat-lich-kham', 'kham-benh', 'calo', 'bmi']):
            return 'hospital_health'
        if any(k in text for k in ['dai-hoc', 'cao-dang', 'trung-cap', 'diem-chuan', 'hoc-phi', 'tuyen-sinh', 'sinh-vien', 'nha-tro']):
            return 'student_education'
        if any(k in text for k in ['xo-so', 'vietlott', 've-so']):
            return 'lottery'
        return sector.lower()

    @staticmethod
    def generate_direct_answer_snippet(usecase_name: str, pillar_kw: str, intent: str, sector: str, usecase_slug: str = None) -> str:
        """Đoạn định nghĩa chuẩn xác 40-70 từ chứa Information Gain cao để công cụ tìm kiếm AI bốc làm Direct Answer"""
        arch = GEODirectAnswerGenerator._resolve_archetype(usecase_name, sector, usecase_slug)
        kw = pillar_kw.capitalize()

        if arch == 'savings':
            return (
                f"{kw} là giải pháp tài chính số cho phép người dùng cá nhân gửi tiền nhàn rỗi vào các ngân hàng thương mại "
                f"được Ngân hàng Nhà nước cấp phép nhằm sinh lời an toàn. Khoản tiền gửi được bảo hiểm theo quy định của BHTGVN "
                f"(hạn mức 125 triệu đồng), áp dụng đa dạng kỳ hạn từ 1 đến 36 tháng với lãi suất niêm yết minh bạch và hỗ trợ quản lý trực tuyến 24/7."
            )
        elif arch == 'loan_credit':
            return (
                f"{kw} là hình thức cấp tín dụng tiêu dùng số cho phép cá nhân tiếp cận nguồn vốn hợp pháp từ các tổ chức tín dụng "
                f"được Ngân hàng Nhà nước cấp phép mà không cần tài sản thế chấp. Hạn mức và lãi suất được duyệt tự động dựa trên điểm tín dụng cá nhân, "
                f"giải ngân tức thì với lịch trả góp minh bạch và công thức tính lãi theo dư nợ giảm dần."
            )
        elif arch == 'gold_fx':
            return (
                f"{kw} là tiện ích theo dõi biến động giá vàng miếng SJC, vàng nhẫn 9999 và tỷ giá ngoại tệ ngân hàng theo thời gian thực "
                f"từ các tổ chức kinh doanh vàng bạc và hệ thống ngân hàng được cấp phép. Dữ liệu đối chiếu trực tiếp với thị trường quốc tế, "
                f"giúp người dùng nắm bắt chênh lệch mua vào - bán ra và đưa ra quyết định giao dịch chính xác."
            )
        elif arch == 'investment_securities':
            return (
                f"{kw} là công cụ tài chính số giúp nhà đầu tư cá nhân tiếp cận các sản phẩm tích lũy và đầu tư được cấp phép bởi Ủy ban Chứng khoán "
                f"Nhà nước (UBCKNN). Nền tảng hỗ trợ tra cứu danh mục, theo dõi giá trị tài sản ròng (NAV), phân tích biểu đồ kỹ thuật và thực hiện "
                f"giao dịch thuận tiện với tính thanh khoản cao."
            )
        elif arch == 'credit_score_cic':
            return (
                f"{kw} là chỉ số phản ánh mức độ uy tín tài chính và lịch sử quan hệ tín dụng của cá nhân, được quản lý và ghi nhận bởi "
                f"Trung tâm Thông tin Tín dụng Quốc gia (CIC - NHNN). Việc theo dõi điểm tín dụng giúp người dùng chủ động kiểm soát hồ sơ nợ, "
                f"phòng ngừa rủi ro nợ xấu và tối ưu hóa điều kiện xét duyệt khi mở thẻ hoặc vay vốn ngân hàng."
            )
        elif arch == 'tax_salary':
            return (
                f"{kw} là công cụ tính toán và tra cứu nghĩa vụ thuế số hóa, hỗ trợ người lao động xác định chính xác số thuế TNCN phải nộp "
                f"theo biểu thuế lũy tiến từng phần, áp dụng đầy đủ mức giảm trừ gia cảnh (11 triệu đồng cho bản thân, 4.4 triệu đồng cho người phụ thuộc) "
                f"và các khoản đóng bảo hiểm bắt buộc theo đúng quy định hiện hành của Bộ Tài chính."
            )
        elif arch == 'traffic_fines':
            return (
                f"{kw} là hình thức xử phạt vi phạm hành chính trong lĩnh vực giao thông đường bộ được ghi nhận qua hệ thống camera giám sát của "
                f"Cục Cảnh sát Giao thông. Chủ phương tiện có thể tra cứu thông tin lỗi, thời gian, địa điểm và hình ảnh vi phạm trực tuyến, "
                f"từ đó chủ động nộp phạt trước khi phương tiện bị gửi cảnh báo sang hệ thống đăng kiểm sau 20 ngày."
            )
        elif arch == 'vehicle_plate_reg':
            return (
                f"{kw} là tiện ích hỗ trợ tra cứu mã vùng biển số xe 63 tỉnh thành, thông tin đấu giá biển số định danh theo Nghị quyết 73/2022/QH15 "
                f"và hướng dẫn thủ tục đăng ký, sang tên phương tiện theo Thông tư 24/2023/TT-BCA, giúp chủ xe hoàn thiện hồ sơ pháp lý minh bạch và nhanh chóng."
            )
        elif arch == 'vehicle_maintenance':
            return (
                f"{kw} là tiện ích toàn diện cho chủ phương tiện cơ giới, hỗ trợ tra cứu định giá xe, chi phí bảo dưỡng định kỳ, bảng giá xăng dầu "
                f"và mạng lưới trạm sạc, garage sửa chữa uy tín toàn quốc. Dữ liệu cập nhật liên tục giúp người dùng dự toán ngân sách vận hành và chăm sóc xe tối ưu."
            )
        elif arch == 'insurance_motor':
            return (
                f"{kw} là gói bảo hiểm bắt buộc theo Nghị định 67/2023/NĐ-CP nhằm bồi thường thiệt hại về người (tối đa 150 triệu đồng/vụ) và tài sản "
                f"cho bên thứ ba khi xảy ra tai nạn giao thông. Chủ xe có thể mua và nhận giấy chứng nhận bảo hiểm điện tử tích hợp mã QR hợp lệ trong 1 phút, "
                f"sử dụng thuận tiện khi xuất trình với lực lượng kiểm tra."
            )
        elif arch == 'insurance_health_social':
            return (
                f"{kw} là chính sách an sinh xã hội trụ cột do Bảo hiểm Xã hội Việt Nam quản lý, giúp người tham gia giảm thiểu gánh nặng tài chính "
                f"khi khám chữa bệnh (mức hưởng đến 100% đúng tuyến) hoặc nhận trợ cấp thai sản, ốm đau, hưu trí. Dịch vụ hỗ trợ tra cứu mã thẻ, "
                f"đóng tiếp hoặc gia hạn BHYT hộ gia đình trực tuyến nhanh chóng."
            )
        elif arch == 'cinema_tickets':
            return (
                f"{kw} là dịch vụ tổng hợp lịch chiếu, giá vé và sơ đồ ghế ngồi thời gian thực của toàn bộ các cụm rạp chiếu phim lớn trên cả nước "
                f"(CGV, Lotte, Galaxy, BHD, Beta). Người xem có thể dễ dàng so sánh suất chiếu gần nhất, áp dụng mã giảm giá độc quyền và đặt vé trực tuyến "
                f"nhận vé điện tử Smart Ticket vào thẳng phòng chiếu."
            )
        elif arch == 'ota_travel':
            return (
                f"{kw} là nền tảng so sánh giá vé máy bay, vé tàu xe, phòng nghỉ và tour du lịch từ các hãng vận chuyển và đối tác lữ hành uy tín. "
                f"Hệ thống hỗ trợ tìm kiếm hành trình tối ưu, xác nhận mã đặt chỗ (PNR) tức thì và quản lý lịch trình linh hoạt với nhiều chương trình khuyến mãi du lịch."
            )
        elif arch == 'telco_data':
            return (
                f"{kw} là tiện ích nạp tiền điện thoại, đăng ký gói cước data 4G/5G tốc độ cao và mua eSIM du lịch quốc tế kết nối trực tiếp với "
                f"các nhà mạng viễn thông hàng đầu (Viettel, VinaPhone, MobiFone). Dịch vụ xử lý kích hoạt tự động 24/7 với chiết khấu cạnh tranh và đa dạng gói cước."
            )
        elif arch == 'hospital_health':
            return (
                f"{kw} là giải pháp y tế số giúp người dân tra cứu thông tin chuyên khoa, lịch công tác của bác sĩ và chủ động đặt lịch khám bệnh trực tuyến "
                f"tại các bệnh viện tuyến đầu, hạn chế tình trạng xếp hàng lấy số và hỗ trợ quản lý hồ sơ tiếp đón bệnh án điện tử an toàn, tiện lợi."
            )
        elif arch == 'student_education':
            return (
                f"{kw} là chuyên trang thông tin giáo dục tổng hợp điểm chuẩn xét tuyển, đề án tuyển sinh, biểu phí đào tạo và các chính sách học bổng, "
                f"hỗ trợ vay vốn sinh viên cho các trường đại học, cao đẳng trên toàn quốc, giúp phụ huynh và học sinh lựa chọn ngành học phù hợp."
            )
        elif arch == 'lottery':
            return (
                f"{kw} là tiện ích theo dõi kết quả mở thưởng xổ số kiến thiết 3 miền và xổ số điện toán Vietlott theo thời gian thực từ các hội đồng "
                f"quay thưởng chính thức, cung cấp bảng thống kê giải thưởng minh bạch và hướng dẫn quy trình lĩnh thưởng hợp pháp theo quy định của Bộ Tài chính."
            )
        else:
            action_verb = "tra cứu và tính toán" if intent == 'Tool/Calculator' else ("so sánh và lựa chọn giải pháp" if intent == 'Commercial' else "thực hiện giao dịch trực tuyến")
            return (
                f"{kw} là tiện ích chuyên sâu thuộc lĩnh vực {sector.title()} trên Kênh Web MoMo, hỗ trợ người dùng {action_verb} "
                f"{usecase_name.lower()} một cách nhanh chóng, minh bạch và chính xác theo thời gian thực. Dịch vụ kết nối trực tiếp với các đơn vị "
                f"uy tín hàng đầu, đảm bảo tiêu chuẩn bảo mật dữ liệu và mang lại trải nghiệm liền mạch từ Web sang Ứng dụng."
            )

    @staticmethod
    def generate_entity_factsheet(usecase_name: str, sector: str, intent: str, usecase_slug: str = None) -> list:
        """Bảng dữ liệu thực thể nghiệp vụ (Entity Facts) đặc thù theo từng lĩnh vực phục vụ AI Knowledge Graph"""
        arch = GEODirectAnswerGenerator._resolve_archetype(usecase_name, sector, usecase_slug)

        if arch == 'savings':
            return [
                {"entity_field": "Cơ quan quản lý nhà nước", "value": "Ngân hàng Nhà nước Việt Nam (NHNN)"},
                {"entity_field": "Chính sách bảo hiểm tiền gửi", "value": "Hạn mức tối đa 125.000.000 VNĐ/cá nhân tại một tổ chức (BHTGVN)"},
                {"entity_field": "Kỳ hạn huy động áp dụng", "value": "Linh hoạt từ không kỳ hạn, 1, 3, 6, 9, 12 đến 36 tháng"},
                {"entity_field": "Phương thức chi trả lãi", "value": "Lĩnh lãi cuối kỳ, định kỳ hàng tháng/quý hoặc nhận lãi trước"},
                {"entity_field": "Hệ thống tổ chức huy động", "value": "Ngân hàng thương mại Nhà nước (Big 4) và NHTM Cổ phần được cấp phép"},
                {"entity_field": "Căn cứ pháp lý áp dụng", "value": "Luật Các tổ chức tín dụng & Thông tư quy định về tiền gửi tiết kiệm"}
            ]
        elif arch == 'loan_credit':
            return [
                {"entity_field": "Cơ quan cấp phép & giám sát", "value": "Ngân hàng Nhà nước Việt Nam (Cơ chế cấp phép tổ chức tín dụng)"},
                {"entity_field": "Phương thức tính lãi suất", "value": "Lãi suất danh nghĩa & lãi suất thực tế theo dư nợ giảm dần (APR)"},
                {"entity_field": "Thời hạn thanh toán khoản vay", "value": "Kỳ hạn linh hoạt từ 1 đến 36 tháng hoặc theo chu kỳ sao kê hàng tháng"},
                {"entity_field": "Tiêu chí thẩm định hạn mức", "value": "Thuật toán chấm điểm tín dụng tự động & dữ liệu lịch sử nợ từ CIC"},
                {"entity_field": "Chi phí phát sinh cần lưu ý", "value": "Phí tất toán trước hạn (1% - 5% dư nợ gốc) và phí phạt chậm trả"},
                {"entity_field": "Cơ chế bảo mật & ký kết", "value": "Định danh điện tử eKYC sinh trắc học và ký kết hợp đồng số theo luật"}
            ]
        elif arch == 'gold_fx':
            return [
                {"entity_field": "Thương hiệu niêm yết chính", "value": "SJC, DOJI, PNJ, Bảo Tín Minh Châu, Mi Hồng và hệ thống Ngân hàng"},
                {"entity_field": "Đơn vị đo lường giao dịch", "value": "Lượng (Cây = 10 chỉ = 37.5g), Chỉ vàng hoặc đơn vị ngoại tệ (USD, EUR...)"},
                {"entity_field": "Tần suất cập nhật dữ liệu", "value": "Thời gian thực (Real-time) theo diễn biến phiên giao dịch trong nước & quốc tế"},
                {"entity_field": "Cơ sở tham chiếu quốc tế", "value": "Biểu giá giao ngay thế giới (Kitco/LBMA) quy đổi theo tỷ giá liên ngân hàng"},
                {"entity_field": "Phân loại sản phẩm chính", "value": "Vàng miếng SJC 999.9, nhẫn tròn trơn 24K, vàng trang sức 18K/14K"},
                {"entity_field": "Cơ quan điều hành thị trường", "value": "Ngân hàng Nhà nước Việt Nam (Quản lý độc quyền sản xuất vàng miếng)"}
            ]
        elif arch == 'investment_securities':
            return [
                {"entity_field": "Cơ quan quản lý thị trường", "value": "Ủy ban Chứng khoán Nhà nước (UBCKNN) & Sở Giao dịch (HOSE/HNX)"},
                {"entity_field": "Phân loại tài sản tài chính", "value": "Cổ phiếu niêm yết, chứng chỉ quỹ mở/ETF, trái phiếu doanh nghiệp, phái sinh"},
                {"entity_field": "Chu kỳ thanh toán bù trừ", "value": "T+2 đối với giao dịch cổ phiếu và chứng chỉ quỹ theo quy định hiện hành"},
                {"entity_field": "Tổ chức phát hành & quản lý", "value": "Các công ty quản lý quỹ và công ty chứng khoán thành viên được cấp phép"},
                {"entity_field": "Phân tầng khẩu vị rủi ro", "value": "Đa dạng từ bảo toàn vốn (trái phiếu/quỹ nợ) đến tăng trưởng (cổ phiếu)"},
                {"entity_field": "Kênh công bố thông tin", "value": "Báo cáo tài chính kiểm toán, bản cáo bạch và hệ thống cổng thông tin UBCKNN"}
            ]
        elif arch == 'credit_score_cic':
            return [
                {"entity_field": "Đơn vị quản lý cơ sở dữ liệu", "value": "Trung tâm Thông tin Tín dụng Quốc gia Việt Nam (CIC - NHNN)"},
                {"entity_field": "Hệ thống phân loại nhóm nợ", "value": "5 nhóm (Nhóm 1: Tiêu chuẩn; Nhóm 2: Chú ý; Nhóm 3-5: Nợ xấu)"},
                {"entity_field": "Thời gian lưu vết nợ xấu", "value": "Lưu trữ lịch sử từ 3 đến 5 năm kể từ ngày tất toán xong toàn bộ dư nợ"},
                {"entity_field": "Ý nghĩa điểm số tín dụng", "value": "Quyết định trực tiếp tỷ lệ duyệt hồ sơ vay, hạn mức và lãi suất cấp vốn"},
                {"entity_field": "Chu kỳ cập nhật dữ liệu", "value": "Định kỳ hàng tháng từ báo cáo của 100% ngân hàng và công ty tài chính"},
                {"entity_field": "Quyền của chủ thể dữ liệu", "value": "Được tra cứu báo cáo tín dụng cá nhân và yêu cầu đính chính khi có sai sót"}
            ]
        elif arch == 'tax_salary':
            return [
                {"entity_field": "Cơ quan quản lý thuế", "value": "Tổng cục Thuế (Bộ Tài chính) & hệ thống Thuế các tỉnh, thành phố"},
                {"entity_field": "Mức giảm trừ gia cảnh", "value": "11.000.000 VNĐ/tháng (bản thân) và 4.400.000 VNĐ/tháng (mỗi người phụ thuộc)"},
                {"entity_field": "Biểu thuế suất áp dụng", "value": "Biểu thuế lũy tiến từng phần gồm 7 bậc từ 5% đến 35% cho thu nhập tiền lương"},
                {"entity_field": "Thời hạn quyết toán thuế năm", "value": "Chậm nhất ngày cuối cùng của tháng thứ 4 kể từ ngày kết thúc năm dương lịch"},
                {"entity_field": "Nền tảng số hóa ngành thuế", "value": "Ứng dụng eTax Mobile và Cổng dịch vụ công của Tổng cục Thuế"},
                {"entity_field": "Căn cứ pháp lý hiện hành", "value": "Luật Thuế thu nhập cá nhân & các Nghị quyết của Ủy ban Thường vụ Quốc hội"}
            ]
        elif arch == 'traffic_fines':
            return [
                {"entity_field": "Cơ quan phát hiện & xử phạt", "value": "Cục Cảnh sát Giao thông (Bộ Công an) & Phòng CSGT các địa phương"},
                {"entity_field": "Công nghệ giám sát vi phạm", "value": "Hệ thống camera AI giám sát thông minh và thiết bị đo tốc độ chuẩn hóa"},
                {"entity_field": "Thời hạn cảnh báo đăng kiểm", "value": "Tự động gửi thông tin cảnh báo sang Cục Đăng kiểm sau 20 ngày chưa nộp phạt"},
                {"entity_field": "Quy định cấp tem kiểm định", "value": "Cấp tem kiểm định thời hạn 15 ngày đối với xe chưa hoàn thành xử phạt phạt nguội"},
                {"entity_field": "Cổng tra cứu & nộp phạt", "value": "Cổng Dịch vụ công Quốc gia, cổng csgt.vn và nền tảng số MoMo"},
                {"entity_field": "Căn cứ pháp lý xử phạt", "value": "Nghị định 168/2024/NĐ-CP của Chính phủ về xử phạt vi phạm trật tự ATGT đường bộ"}
            ]
        elif arch == 'vehicle_plate_reg':
            return [
                {"entity_field": "Cơ quan thẩm quyền cấp biển", "value": "Phòng Cảnh sát Giao thông (Công an các tỉnh, thành phố trực thuộc)"},
                {"entity_field": "Cơ chế quản lý biển số", "value": "Cấp và quản lý theo mã định danh cá nhân của chủ sở hữu phương tiện"},
                {"entity_field": "Nền tảng đấu giá trực tuyến", "value": "Công ty Đấu giá Hợp danh Việt Nam (VPA) theo quy chế của Bộ Công an"},
                {"entity_field": "Quy định giữ biển khi chuyển nhượng", "value": "Cơ quan công an giữ lại biển số định danh trong kho dữ liệu 05 năm"},
                {"entity_field": "Thủ tục bắt buộc khi bán xe", "value": "Thu hồi chứng nhận đăng ký, biển số xe trước khi làm thủ tục sang tên"},
                {"entity_field": "Căn cứ pháp lý áp dụng", "value": "Thông tư 24/2023/TT-BCA & Nghị quyết 73/2022/QH15 của Quốc hội"}
            ]
        elif arch == 'vehicle_maintenance':
            return [
                {"entity_field": "Phân loại tiện ích phương tiện", "value": "Dịch vụ vận hành, bảo dưỡng & hạ tầng giao thông đường bộ"},
                {"entity_field": "Cơ chế cập nhật giá xăng dầu", "value": "Điều chỉnh theo kỳ điều hành của Liên Bộ Công Thương - Tài chính"},
                {"entity_field": "Hạ tầng trạm thu phí không dừng", "value": "Hệ thống tài khoản giao thông VETC và ePass liên thông toàn quốc"},
                {"entity_field": "Mạng lưới đối tác cung ứng", "value": "Hệ thống garage ô tô, xưởng dịch vụ ủy quyền và trạm xăng dầu chính hãng"},
                {"entity_field": "Quy chuẩn an toàn kỹ thuật", "value": "Kiểm định định kỳ theo quy định của Cục Đăng kiểm Việt Nam"},
                {"entity_field": "Phương thức quản lý chi phí", "value": "Lưu trữ lịch sử giao dịch và nhắc lịch bảo dưỡng, đăng kiểm tự động"}
            ]
        elif arch == 'insurance_motor':
            return [
                {"entity_field": "Phân loại sản phẩm bảo hiểm", "value": "Bảo hiểm trách nhiệm dân sự bắt buộc của chủ xe cơ giới & tự nguyện"},
                {"entity_field": "Căn cứ pháp lý ban hành", "value": "Nghị định số 67/2023/NĐ-CP của Chính phủ về bảo hiểm bắt buộc"},
                {"entity_field": "Mức bồi thường tối đa về người", "value": "150.000.000 VNĐ/người/vụ tai nạn đối với thiệt hại thân thể, tính mạng"},
                {"entity_field": "Mức bồi thường tối đa về tài sản", "value": "50.000.000 VNĐ/vụ (xe máy) hoặc 100.000.000 VNĐ/vụ (xe ô tô)"},
                {"entity_field": "Hình thức giấy chứng nhận", "value": "Giấy chứng nhận bảo hiểm điện tử có mã QR tra cứu tính pháp lý tức thì"},
                {"entity_field": "Chế tài xử phạt khi vi phạm", "value": "Phạt 100.000 - 200.000 VNĐ (xe máy) hoặc 400.000 - 600.000 VNĐ (ô tô)"}
            ]
        elif arch == 'insurance_health_social':
            return [
                {"entity_field": "Cơ quan thực hiện chính sách", "value": "Bảo hiểm Xã hội Việt Nam (BHXH) trực thuộc Chính phủ"},
                {"entity_field": "Mức hưởng khám chữa bệnh", "value": "Chi trả từ 80% đến 100% chi phí khám chữa bệnh đúng tuyến theo danh mục"},
                {"entity_field": "Cơ chế đóng BHYT hộ gia đình", "value": "Giảm trừ lũy tiến mức đóng cho thành viên thứ 2 (70%), thứ 3 (60%), thứ 4 (50%)"},
                {"entity_field": "Nền tảng số hóa thẻ BHYT", "value": "Sử dụng hình ảnh thẻ trên ứng dụng VssID hoặc tài khoản VNeID mức độ 2"},
                {"entity_field": "Chính sách tham gia 5 năm liên tục", "value": "Hưởng 100% chi phí khi số tiền cùng chi trả vượt 6 tháng lương cơ sở"},
                {"entity_field": "Căn cứ pháp lý trụ cột", "value": "Luật Bảo hiểm Y tế sửa đổi & Luật Bảo hiểm Xã hội hiện hành"}
            ]
        elif arch == 'cinema_tickets':
            return [
                {"entity_field": "Hệ thống chuỗi rạp liên kết", "value": "CGV Cinemas, Lotte Cinema, Galaxy, BHD Star, Beta Cinemas, Cinestar"},
                {"entity_field": "Khung phân loại độ tuổi khán giả", "value": "Nhãn P (Phổ biến), K (Dưới 13 tuổi có bảo trợ), T13, T16, T18 và C (Cấm)"},
                {"entity_field": "Cơ chế đồng bộ suất chiếu", "value": "Đồng bộ API thời gian thực với hệ thống bán vé của từng cụm rạp"},
                {"entity_field": "Hình thức vé vào phòng chiếu", "value": "Vé điện tử (Smart Ticket QR) quét mã vào thẳng rạp không cần in vé giấy"},
                {"entity_field": "Phụ thu định dạng trải nghiệm", "value": "Áp dụng định dạng 3D, IMAX, 4DX, ScreenX và các dòng ghế đôi Sweetbox/VIP"},
                {"entity_field": "Quy định pháp lý chuyên ngành", "value": "Luật Điện ảnh & Thông tư 05/2023/TT-BVHTTDL của Bộ Văn hóa, Thể thao và Du lịch"}
            ]
        elif arch == 'ota_travel':
            return [
                {"entity_field": "Hệ thống đối tác vận chuyển", "value": "Vietnam Airlines, Vietjet Air, Bamboo Airways và Tổng công ty Đường sắt (VNR)"},
                {"entity_field": "Cơ chế xác nhận mã đặt chỗ", "value": "Mã PNR đặt chỗ chính thức được gửi tức thì qua tin nhắn SMS và email"},
                {"entity_field": "Tiêu chuẩn hành lý áp dụng", "value": "Hành lý xách tay tiêu chuẩn 7-12kg và tùy chọn mua thêm hành lý ký gửi"},
                {"entity_field": "Chính sách thay đổi & hoàn hủy", "value": "Tuân thủ nghiêm ngặt điều kiện biểu giá vé của từng hãng vận chuyển"},
                {"entity_field": "Bảo hiểm chuyến đi tích hợp", "value": "Tùy chọn bảo hiểm trễ hủy chuyến bay và bảo hiểm tai nạn du lịch toàn diện"},
                {"entity_field": "Kênh làm thủ tục chuyến bay", "value": "Hỗ trợ check-in trực tuyến trước giờ khởi hành 24 giờ để chọn ghế ngồi"}
            ]
        elif arch == 'telco_data':
            return [
                {"entity_field": "Hạ tầng nhà mạng viễn thông", "value": "Viettel, VinaPhone, MobiFone, Vietnamobile, Wintel và iTel"},
                {"entity_field": "Cơ cấu gói cước data cung cấp", "value": "Gói ngày (1-3GB/ngày), gói chu kỳ ngắn tuần và gói tháng (30-180GB/tháng)"},
                {"entity_field": "Thời gian xử lý & kích hoạt", "value": "Kích hoạt nạp tiền và cộng dung lượng tự động trong 3 đến 10 giây"},
                {"entity_field": "Công nghệ eSIM du lịch số", "value": "Quét mã QR kích hoạt profile mạng quốc tế tức thì không cần tháo lắp SIM"},
                {"entity_field": "Chính sách ưu đãi chiết khấu", "value": "Chiết khấu trực tiếp trên mệnh giá nạp tiền điện thoại từ 3% đến 10%"},
                {"entity_field": "Phương thức kiểm tra số dư", "value": "Cú pháp tra cứu tin nhắn trực tiếp với tổng đài hoặc qua ứng dụng nhà mạng"}
            ]
        elif arch == 'hospital_health':
            return [
                {"entity_field": "Mạng lưới cơ sở y tế đối tác", "value": "Các bệnh viện đa khoa, chuyên khoa tuyến Trung ương và phòng khám chuẩn hóa"},
                {"entity_field": "Quy trình đăng ký khám bệnh", "value": "Đặt trước chuyên khoa, bác sĩ và khung giờ khám tối thiểu 24 giờ"},
                {"entity_field": "Thủ tục tiếp đón tại viện", "value": "Quét mã tiếp đón điện tử tại quầy ưu tiên, giảm 50-70% thời gian chờ đợi"},
                {"entity_field": "Chính sách thanh toán viện phí", "value": "Hỗ trợ đối soát quyền lợi BHYT nhà nước và bảo lãnh viện phí tư nhân"},
                {"entity_field": "Bảo mật hồ sơ bệnh án", "value": "Dữ liệu kết quả khám và đơn thuốc số hóa lưu trữ bảo mật đa tầng"},
                {"entity_field": "Căn cứ pháp lý y tế", "value": "Luật Khám bệnh, chữa bệnh & Đề án Chuyển đổi số Y tế của Bộ Y tế"}
            ]
        elif arch == 'student_education':
            return [
                {"entity_field": "Cơ quan chỉ đạo tuyển sinh", "value": "Bộ Giáo dục và Đào tạo (Bộ GD&ĐT) quản lý đề án tuyển sinh quốc gia"},
                {"entity_field": "Phương thức xét tuyển áp dụng", "value": "Điểm thi tốt nghiệp THPT, học bạ THPT, bài thi đánh giá năng lực & tư duy"},
                {"entity_field": "Khung học phí đào tạo", "value": "Quy định theo Nghị định 81/2021/NĐ-CP & Nghị định 97/2023/NĐ-CP của Chính phủ"},
                {"entity_field": "Chính sách tín dụng sinh viên", "value": "Chương trình vay vốn học tập lãi suất ưu đãi qua Ngân hàng CSXH (NHCSXH)"},
                {"entity_field": "Chính sách học bổng & hỗ trợ", "value": "Học bổng khuyến khích học tập, miễn giảm học phí diện chính sách xã hội"},
                {"entity_field": "Kênh tra cứu thông tin", "value": "Cổng thông tin tuyển sinh quốc gia và đề án tuyển sinh chính thức từng trường"}
            ]
        elif arch == 'lottery':
            return [
                {"entity_field": "Đơn vị phát hành chính thức", "value": "Công ty TNHH MTV Xổ số Kiến thiết 3 miền & Xổ số Điện toán Việt Nam (Vietlott)"},
                {"entity_field": "Cơ cấu giá trị giải thưởng", "value": "Giải Đặc biệt 2 tỷ đồng (XSKT truyền thống) hoặc Jackpot từ 12 đến 30 tỷ (Vietlott)"},
                {"entity_field": "Khung giờ quay số mở thưởng", "value": "16h15 (Miền Nam), 17h15 (Miền Trung), 18h15 (Miền Bắc) & 18h00 (Vietlott)"},
                {"entity_field": "Thời hạn lĩnh thưởng hợp lệ", "value": "Trong vòng 30 ngày kể từ ngày công bố kết quả mở thưởng chính thức"},
                {"entity_field": "Nghĩa vụ thuế khi trúng thưởng", "value": "Khấu trừ thuế TNCN 10% đối với phần tiền thưởng vượt trên 10.000.000 VNĐ"},
                {"entity_field": "Cơ chế giám sát quay số", "value": "Hội đồng Giám sát Xổ số theo quy định của Bộ Tài chính và cơ quan thanh tra"}
            ]
        else:
            return [
                {"entity_field": "Phân loại giải pháp", "value": f"Dịch vụ số hóa chuyên sâu ngành {sector.title()} - Kênh Web MoMo"},
                {"entity_field": "Đối tượng phục vụ", "value": "Người dùng cá nhân có nhu cầu tra cứu và thao tác trực tuyến trên toàn quốc"},
                {"entity_field": "Thời gian phản hồi nghiệp vụ", "value": "Xử lý tức thì (Real-time), dữ liệu đồng bộ liên tục 24/7"},
                {"entity_field": "Hạ tầng kết nối dịch vụ", "value": "Tích hợp API trực tiếp từ hệ thống dữ liệu đối tác uy tín đầu ngành"},
                {"entity_field": "Tiêu chuẩn an toàn thông tin", "value": "Mã hóa dữ liệu chuẩn quốc tế, bảo mật đa tầng PCI DSS Level 1"},
                {"entity_field": "Kênh chuyển tiếp thao tác", "value": "Trình duyệt Web (Desktop/Mobile) kết hợp điều hướng Web-to-App MoMo"}
            ]



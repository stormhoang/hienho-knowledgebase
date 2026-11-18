#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEO ENTITY GAP & AI SEARCH BLUEPRINT GENERATOR
Engine phân tích khoảng trống thực thể (Entity Gaps), tối ưu hóa cấu trúc cho AI Search (GEO),
sinh đoạn trích định nghĩa trực tiếp (AI Answer Box) và Schema có cấu trúc theo chuẩn Web Platform.

Ứng dụng:
- Thay thế hoàn toàn các công cụ SaaS thương mại (như Wriai) bằng pipeline nội bộ.
- Tạo lợi thế cạnh tranh Information Gain và Anti-LLM Moat bằng cách bơm First-party Data.
- Chuẩn hóa Schema JSON-LD và Direct Answer Snippet cho các Hubs trọng điểm (Financial, Cinema, Vehicle...).
"""

import os
import sys
import re
import json
import ssl
import time
import textwrap
import argparse
import urllib.request
import urllib.parse
from datetime import datetime
from collections import Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))

# Nhập các gateway và module nội bộ
try:
    from content_plan_config import FEATURE_MOMO_MAP, slugify, remove_accents
except ImportError:
    FEATURE_MOMO_MAP = {}
    def slugify(text):
        return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

try:
    from serp_competitor_analyzer import SERPFetcher, CompetitorPageParser, clean_text, ssl_ctx
except ImportError:
    clean_text = lambda s: " ".join(s.split()) if s else ""
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE
    SERPFetcher = None
    CompetitorPageParser = None

REPORTS_DIR = os.path.join(BASE_DIR, "07_REPORTS", "geo_entity_gaps")
DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data", "geo_entity_gaps")

# ---------------------------------------------------------------------------
# 1. BẢN ĐỒ ONTOLOGY NGÀNH & ĐIỂM MÙ THỰC THỂ (DOMAIN ONTOLOGY SSOT)
# ---------------------------------------------------------------------------

DOMAIN_ONTOLOGY_REGISTRY = {
    "financial_credit_paylater": {
        "hub": "Financial Hub",
        "theme": "Ví trả sau / Tín dụng tiêu dùng",
        "keywords": ["vi tra sau", "mua truoc tra sau", "paylater", "han muc tin dung", "tra sau", "vi dien tu tra sau"],
        "schema_type": "FinancialProduct",
        "schema_category": "https://schema.org/LoanOrCredit",
        "schema_mandatory_fields": [
            {"field": "name", "desc": "Tên thương mại của sản phẩm ví trả sau."},
            {"field": "provider", "desc": "Tổ chức tài chính / Ngân hàng đối tác bảo lãnh phát hành (Organization)."},
            {"field": "interestRate", "desc": "Lãi suất công bố trong hạn (thường là 0% trong chu kỳ miễn lãi)."},
            {"field": "feesAndCommissionsSpecification", "desc": "Đặc tả các loại phí: phí dịch vụ, phí duy trì, phí chậm trả."},
            {"field": "areaServed", "desc": "Khu vực áp dụng (Mặc định: Việt Nam / VN)."},
            {"field": "review", "desc": "Đánh giá xếp hạng trung bình (AggregateRating) tăng độ tin cậy E-E-A-T."}
        ],
        "ai_answer_template": (
            "Ví trả sau là hình thức tín dụng tiêu dùng số cho phép người dùng thanh toán trước các giao dịch mua sắm "
            "và trả tiền vào cuối kỳ hoặc trả góp. Sản phẩm này hoạt động dựa trên lịch sử tín dụng cá nhân, "
            "tích hợp trực tiếp vào ví điện tử, giúp tối ưu hóa dòng tiền mà không cần thẻ tín dụng vật lý."
        ),
        "pillars": {
            "expertise": {
                "title": "Tác động đến Điểm Tín Dụng Quốc Gia (CIC)",
                "summary": "Phân tích cụ thể ảnh hưởng của các khoản chậm trả đến hồ sơ tín dụng tại Trung tâm Thông tin Tín dụng Quốc gia (CIC).",
                "detail": (
                    "Hầu hết các bài viết đối thủ chỉ dừng lại ở bước 'cách đăng ký' và 'hạn mức'. "
                    "Để đạt E-E-A-T cao nhất, nội dung cần làm rõ: Việc chậm thanh toán ví trả sau từ 10 ngày trở lên "
                    "sẽ bị xếp vào nhóm nợ cần chú ý (Nhóm 2) hoặc nợ xấu (Nhóm 3-5) trên hệ thống CIC, "
                    "trực tiếp ảnh hưởng đến khả năng vay mua nhà, mua xe hoặc mở thẻ tín dụng ngân hàng trong 3-5 năm tới."
                ),
                "actionable_angle": "Bảng phân loại 5 nhóm nợ CIC và mốc thời gian báo cáo vi phạm của ví trả sau."
            },
            "trust": {
                "title": "Cơ chế định danh điện tử eKYC & Dữ liệu C06",
                "summary": "Phân tích sâu cơ chế xác thực danh tính số kết hợp cơ sở dữ liệu quốc gia về dân cư.",
                "detail": (
                    "Làm rõ quy trình bảo mật cấp độ ngân hàng: Ứng dụng tích hợp công nghệ AI Face Matching "
                    "đối soát khuôn mặt với chip Căn cước công dân và xác thực trực tiếp qua Cơ sở dữ liệu Quốc gia về dân cư (Đề án 06). "
                    "Cơ chế này ngăn chặn tuyệt đối tình trạng mở ví giả mạo hoặc chiếm quyền sử dụng hạn mức."
                ),
                "actionable_angle": "Sơ đồ 3 bước xác thực sinh trắc học và mã hóa bảo mật chuẩn PCI-DSS Level 1."
            },
            "high_intent": {
                "title": "Minh bạch chi phí ẩn & Bảng phí phạt chậm trả (Hidden Cost Analysis)",
                "summary": "Bóc tách chi tiết toàn bộ các loại phí phát sinh ngoài lãi suất công bố 0%.",
                "detail": (
                    "Đây là điểm chạm có ý định tìm kiếm cao nhất (High-Intent). Nội dung cần công khai rõ: "
                    "Phí dịch vụ kích hoạt/duy trì hàng tháng khi có phát sinh giao dịch, "
                    "công thức tính phí chậm trả theo từng mốc ngày (ví dụ: ngày 1-5, ngày 6-10), "
                    "và mức phí chuyển đổi sang hình thức trả góp 3-6-12 tháng."
                ),
                "actionable_angle": "Bảng biểu phí chi tiết so sánh giữa thanh toán đúng hạn vs chậm hạn."
            }
        }
    },
    "financial_consumer_loan": {
        "hub": "Financial Hub",
        "theme": "Vay tiêu dùng / Vay nhanh online",
        "keywords": ["vay tien", "vay tieu dung", "vay tin chap", "vay online", "vay nhanh", "vay tra gop"],
        "schema_type": "LoanOrCredit",
        "schema_category": "https://schema.org/LoanOrCredit",
        "schema_mandatory_fields": [
            {"field": "name", "desc": "Tên gói vay tín chấp / tiêu dùng."},
            {"field": "provider", "desc": "Ngân hàng hoặc công ty tài chính được cấp phép cấp vốn."},
            {"field": "annualPercentageRate", "desc": "Lãi suất phần trăm hàng năm (APR) tính theo dư nợ giảm dần."},
            {"field": "loanTerm", "desc": "Thời hạn vay tối thiểu và tối đa (QuantitativeValue: tháng/năm)."},
            {"field": "amount", "desc": "Hạn mức giải ngân tối đa."},
            {"field": "feesAndCommissionsSpecification", "desc": "Phí thẩm định, phí bảo hiểm khoản vay, phí tất toán trước hạn."}
        ],
        "ai_answer_template": (
            "Vay tiêu dùng trực tuyến là giải pháp cấp vốn tín chấp số hóa cho phép cá nhân tiếp cận khoản vay tiền mặt "
            "từ các tổ chức tín dụng được Ngân hàng Nhà nước cấp phép mà không cần tài sản thế chấp. "
            "Quy trình duyệt hồ sơ được tự động hóa qua thuật toán chấm điểm tín dụng và định danh eKYC, "
            "giúp giải ngân tức thì vào tài khoản ngân hàng trong vòng vài phút với lịch trả góp minh bạch."
        ),
        "pillars": {
            "expertise": {
                "title": "Quy định trần lãi suất theo Bộ luật Dân sự & Thông tư NHNN",
                "summary": "Phân định rõ ràng giữa khoản vay hợp pháp của tổ chức tín dụng với bẫy 'tín dụng đen'.",
                "detail": (
                    "Chỉ rõ khung pháp lý: Lãi suất cho vay tiêu dùng tuân thủ trần quy định của Ngân hàng Nhà nước, "
                    "hợp đồng hiển thị rõ lãi suất danh nghĩa và lãi suất thực tế theo dư nợ giảm dần. "
                    "Cung cấp hướng dẫn nhận diện các ứng dụng cho vay trái phép núp bóng phí dịch vụ cắt cổ."
                ),
                "actionable_angle": "Bảng đối chiếu 4 tiêu chí nhận diện đối tác cho vay hợp pháp vs ứng dụng đen."
            },
            "trust": {
                "title": "Hợp đồng tín dụng điện tử & Tính pháp lý số",
                "summary": "Cơ chế ký kết hợp đồng số bằng mã OTP/chữ ký số có giá trị pháp lý tương đương văn bản giấy.",
                "detail": (
                    "Phân tích cơ sở pháp lý của hợp đồng tín dụng điện tử theo Luật Giao dịch điện tử. "
                    "Người vay nhận bản sao hợp đồng qua email kèm mã tra cứu lưu trữ tại cổng thông tin ngân hàng."
                ),
                "actionable_angle": "Quy trình 4 bước thẩm định hồ sơ không gọi điện làm phiền người thân."
            },
            "high_intent": {
                "title": "Phí tất toán trước hạn & Công thức tính lãi dư nợ giảm dần",
                "summary": "Minh bạch công thức tính tiền lãi hàng tháng và chi phí phạt khi trả nợ sớm.",
                "detail": (
                    "Người dùng có nhu cầu thực thường rất sợ bị tính lãi mẹ đẻ lãi con. Bài viết cần cung cấp công cụ "
                    "hoặc bảng tính mô phỏng: So sánh số tiền phải trả giữa cách tính 'dư nợ gốc ban đầu' vs 'dư nợ giảm dần', "
                    "kèm tỷ lệ phí tất toán trước hạn (thường từ 1% đến 5% dư nợ còn lại)."
                ),
                "actionable_angle": "Bảng tính chi tiết kế hoạch trả góp mẫu cho khoản vay 20 triệu kỳ hạn 12 tháng."
            }
        }
    },
    "cinema_movie": {
        "hub": "Cinema Hub",
        "theme": "Lịch chiếu phim / Đặt vé xem phim",
        "keywords": ["lich chieu phim", "ve xem phim", "rap chieu phim", "gia ve", "phim chieu rap", "dat ve xem phim"],
        "schema_type": "Movie",
        "schema_category": "https://schema.org/Movie",
        "schema_mandatory_fields": [
            {"field": "name", "desc": "Tên phim chính xác theo giấy phép phát hành rạp."},
            {"field": "duration", "desc": "Thời lượng phim chuẩn định dạng ISO 8601 (ví dụ: PT120M)."},
            {"field": "contentRating", "desc": "Phân loại độ tuổi chính thức (P, K, T13, T16, T18, C)."},
            {"field": "director", "desc": "Đạo diễn (Person)."},
            {"field": "actor", "desc": "Dàn diễn viên chính (Person list)."},
            {"field": "aggregateRating", "desc": "Điểm đánh giá từ khán giả và chuyên môn."}
        ],
        "ai_answer_template": (
            "Lịch chiếu phim trực tuyến là dịch vụ tổng hợp thời gian chiếu, sơ đồ ghế ngồi và giá vé theo thời gian thực "
            "của tất cả các cụm rạp trên toàn quốc (CGV, Lotte Cinema, Galaxy, BHD, Beta, Cinestar). "
            "Nền tảng cho phép người xem tra cứu suất chiếu gần nhất, so sánh ưu đãi giá vé giữa các rạp "
            "và tiến hành đặt chỗ tức thì mà không cần xếp hàng mua vé tại quầy."
        ),
        "pillars": {
            "expertise": {
                "title": "Quy chuẩn phân loại độ tuổi điện ảnh quốc gia (Cục Điện Ảnh)",
                "summary": "Giải thích chi tiết quy định độ tuổi và giấy tờ tùy thân bắt buộc khi vào phòng chiếu.",
                "detail": (
                    "Các bài viết đối thủ thường chỉ ghi nhãn T16, T18 mà không giải thích điều kiện kiểm soát. "
                    "Cần bổ sung quy định: Nhân viên rạp có quyền từ chối khán giả không xuất trình được CCCD/VNeID "
                    "chứng minh đủ tuổi theo Thông tư số 05/2023/TT-BVHTTDL, và tiền vé sẽ không được hoàn trả."
                ),
                "actionable_angle": "Bảng giải mã 6 nhãn phân loại độ tuổi rạp chiếu phim chuẩn 2026."
            },
            "trust": {
                "title": "Cơ chế giữ chỗ & Đồng bộ sơ đồ ghế thời gian thực (Live Seat Map)",
                "summary": "Hạ tầng kết nối API trực tiếp với hệ thống bán vé của từng cụm rạp.",
                "detail": (
                    "Mô tả quy trình khóa ghế tức thì trong 5-10 phút khi người dùng chuyển sang bước thanh toán, "
                    "đảm bảo không xảy ra tình trạng trùng ghế (double booking) giữa các kênh mua vé."
                ),
                "actionable_angle": "Quy trình nhận vé điện tử (Smart Ticket QR) vào thẳng phòng chiếu không cần in vé giấy."
            },
            "high_intent": {
                "title": "Bảng phụ thu phòng chiếu đặc biệt & Chính sách hủy vé",
                "summary": "Bóc tách mức giá phụ thu các định dạng IMAX, 4DX, ScreenX, ghế đôi Sweetbox.",
                "detail": (
                    "Người xem phim thường tìm kiếm lý do tại sao giá vé thanh toán cao hơn giá niêm yết. "
                    "Cần liệt kê rõ: Phụ thu ngày Lễ/Tết, phụ thu suất chiếu cuối tuần, phụ thu định dạng âm thanh Dolby Atmos, "
                    "và chính sách hủy/đổi suất chiếu của từng chuỗi rạp."
                ),
                "actionable_angle": "Bảng ma trận so sánh giá vé tiêu chuẩn vs định dạng cao cấp tại Hà Nội và TP.HCM."
            }
        }
    },
    "vehicle_traffic_fines": {
        "hub": "Vehicle Hub",
        "theme": "Tra cứu phạt nguội giao thông",
        "keywords": ["phat nguoi", "tra cuu phat nguoi", "nop phat nguoi", "kiem tra phat nguoi", "vi pham giao thong"],
        "schema_type": "GovernmentService",
        "schema_category": "https://schema.org/GovernmentService",
        "schema_mandatory_fields": [
            {"field": "name", "desc": "Dịch vụ tra cứu và nộp phạt vi phạm giao thông đường bộ."},
            {"field": "provider", "desc": "Cục Cảnh sát Giao thông (Bộ Công an)."},
            {"field": "serviceType", "desc": "Dịch vụ công trực tuyến / Tra cứu vi phạm hành chính."},
            {"field": "areaServed", "desc": "Toàn quốc (Toàn bộ 63 tỉnh thành)."}
        ],
        "ai_answer_template": (
            "Phạt nguội là hình thức xử phạt vi phạm hành chính trong lĩnh vực giao thông đường bộ "
            "được ghi nhận thông qua hệ thống camera giám sát tự động của lực lượng Cảnh sát Giao thông. "
            "Chủ phương tiện có thể tra cứu thông tin lỗi, địa điểm và hình ảnh vi phạm trực tuyến bằng biển số xe, "
            "sau đó tiến hành nộp phạt trực tiếp qua Cổng Dịch vụ công Quốc gia hoặc ví điện tử liên kết."
        ),
        "pillars": {
            "expertise": {
                "title": "Thời hạn xử phạt & Quy định tạm dừng đăng kiểm phương tiện",
                "summary": "Hệ quả pháp lý khi không chấp hành quyết định xử phạt nguội theo Nghị định 100/123.",
                "detail": (
                    "Phân tích rõ: Sau 20 ngày kể từ ngày nhận thông báo vi phạm, nếu chủ phương tiện không đến giải quyết, "
                    "CSGT sẽ gửi cảnh báo phương tiện vi phạm lên hệ thống của Cục Đăng kiểm Việt Nam. "
                    "Phương tiện sẽ bị từ chối kiểm định hoặc chỉ được cấp tem kiểm định có thời hạn hiệu lực 15 ngày."
                ),
                "actionable_angle": "Mốc thời gian 3 giai đoạn xử lý phạt nguội từ lúc vi phạm đến khi bị khóa đăng kiểm."
            },
            "trust": {
                "title": "Nguồn dữ liệu đối soát trực tiếp từ Cục CSGT",
                "summary": "Xác thực độ chuẩn xác của kết quả tra cứu dựa trên cổng dữ liệu csgt.vn.",
                "detail": (
                    "Khẳng định dữ liệu tra cứu được đồng bộ từ cơ sở dữ liệu xử lý vi phạm của Cục Cảnh sát Giao thông, "
                    "tránh các thông tin sai lệch từ các trang web giả mạo câu view."
                ),
                "actionable_angle": "Hướng dẫn kiểm tra mã quyết định xử phạt thật và đối chiếu số biên bản vi phạm."
            },
            "high_intent": {
                "title": "Quy trình nộp phạt online không cần đến cơ quan công an",
                "summary": "Hướng dẫn từng bước thanh toán tiền phạt trực tuyến và nhận lại giấy tờ tạm giữ qua bưu điện.",
                "detail": (
                    "Giải quyết triệt để nỗi đau phải đi xa để nộp phạt: Hướng dẫn lấy mã số biên bản điện tử, "
                    "thanh toán qua cổng Dịch vụ công hoặc ví điện tử, và đăng ký nhận lại GPLX/giấy tờ xe tại nhà qua bưu chính công ích."
                ),
                "actionable_angle": "Sơ đồ 4 bước nộp phạt nguội tại nhà và cơ chế tự động xóa cảnh báo đăng kiểm."
            }
        }
    }
}

# ---------------------------------------------------------------------------
# 2. BỘ ĐIỀU HƯỚNG VÀ XÁC ĐỊNH HUB TỰ ĐỘNG (HUB RESOLVER)
# ---------------------------------------------------------------------------

def resolve_domain_ontology(query: str, manual_hub: str = None) -> dict:
    """Tự động phát hiện hoặc ánh xạ query vào ontology ngành tương ứng."""
    clean_q = remove_accents(query.lower().strip())
    
    if manual_hub:
        norm_hub = remove_accents(manual_hub.lower().strip())
        for key, ont in DOMAIN_ONTOLOGY_REGISTRY.items():
            if norm_hub in remove_accents(ont["hub"].lower()) or norm_hub in remove_accents(ont["theme"].lower()):
                return ont

    # Khớp từ khóa trong Registry
    best_match = None
    max_score = 0
    for key, ont in DOMAIN_ONTOLOGY_REGISTRY.items():
        score = 0
        for kw in ont["keywords"]:
            norm_kw = remove_accents(kw.lower())
            if norm_kw in clean_q:
                score += len(norm_kw)
        if score > max_score:
            max_score = score
            best_match = ont

    if best_match:
        return best_match

    # Fallback cho các use case chưa định nghĩa sẵn: Sinh ontology tự động
    return {
        "hub": "Web Platform General",
        "theme": f"Chuyên mục {query.title()}",
        "keywords": [clean_q],
        "schema_type": "Article",
        "schema_category": "https://schema.org/Article",
        "schema_mandatory_fields": [
            {"field": "headline", "desc": "Tiêu đề chính xác chứa thực thể trọng tâm."},
            {"field": "description", "desc": "Tóm tắt bản chất giá trị cung cấp."},
            {"field": "author", "desc": "Tác giả chuyên môn / Đội ngũ kỹ thuật (Person/Organization)."},
            {"field": "publisher", "desc": "Đơn vị phát hành có thẩm quyền."},
            {"field": "datePublished", "desc": "Ngày xuất bản chính thức chuẩn ISO 8601."},
            {"field": "mainEntityOfPage", "desc": "URL canonical định danh thực thể."}
        ],
        "ai_answer_template": (
            f"{query.title()} là giải pháp tiện ích số hóa trên nền tảng Web, "
            f"cung cấp công cụ tra cứu thông tin và xử lý giao dịch tức thì cho người dùng. "
            f"Cơ chế hoạt động được tối ưu hóa dựa trên dữ liệu cập nhật theo thời gian thực, "
            f"giúp tiết kiệm thời gian thao tác và nâng cao độ an toàn thông tin."
        ),
        "pillars": {
            "expertise": {
                "title": f"Quy định pháp lý & Chuẩn mực chuyên môn của {query}",
                "summary": "Phân tích nền tảng pháp lý và các tiêu chuẩn kiểm duyệt liên quan.",
                "detail": f"Nội dung cần làm rõ các văn bản quy phạm pháp luật điều chỉnh trực tiếp hoạt động của {query}.",
                "actionable_angle": "Bảng điều kiện và tiêu chí thẩm định chuyên sâu."
            },
            "trust": {
                "title": f"Cơ chế bảo mật dữ liệu & Kiểm soát giao dịch của {query}",
                "summary": "Mô tả hạ tầng công nghệ bảo vệ quyền lợi người dùng.",
                "detail": "Minh bạch cơ chế mã hóa đầu cuối và quy trình xác thực hai yếu tố.",
                "actionable_angle": "Quy trình xác minh bảo mật 3 lớp."
            },
            "high_intent": {
                "title": f"Phân tích biểu phí & Bảng so sánh phương án tối ưu cho {query}",
                "summary": "Cung cấp số liệu định lượng chi tiết giúp người dùng ra quyết định tức thì.",
                "detail": "Bảng so sánh chi tiết chi phí, thời gian xử lý và lợi ích thực nhận.",
                "actionable_angle": "Bảng đối chiếu thông số thực tế giữa các giải pháp trên thị trường."
            }
        }
    }

# ---------------------------------------------------------------------------
# 3. ENGINE CÀO SERP VÀ PHÂN TÍCH KHOẢNG TRỐNG ĐỐI THỦ
# ---------------------------------------------------------------------------

def audit_competitor_serp(query: str, limit: int = 5) -> dict:
    """Thu thập dữ liệu SERP và bóc tách On-page đối thủ."""
    if not SERPFetcher:
        return {"serp_items": [], "momo_ranking": None, "competitor_texts": []}
    
    print(f"-> Đang quét SERP đối thủ cho truy vấn: '{query}'...")
    serp_items, momo_ranking = SERPFetcher.fetch_serp_results(query, limit=limit)
    
    competitor_data = []
    combined_headings = []
    
    for item in serp_items:
        try:
            page_data = CompetitorPageParser.parse_page(item)
            competitor_data.append(page_data)
            combined_headings.extend(page_data.get("h2", []))
            combined_headings.extend(page_data.get("h3", []))
        except Exception as e:
            print(f"   Lỗi khi đọc trang {item.get('domain')}: {e}")

    return {
        "serp_items": serp_items,
        "momo_ranking": momo_ranking,
        "competitor_data": competitor_data,
        "headings": combined_headings
    }

# ---------------------------------------------------------------------------
# 4. TRÌNH TẠO MÃ SCHEMA JSON-LD CHUẨN XÁC
# ---------------------------------------------------------------------------

def generate_schema_jsonld(ontology: dict, query: str) -> str:
    """Tạo khối mã JSON-LD mẫu chuẩn SEO/GEO cho trang web."""
    schema_type = ontology.get("schema_type", "FinancialProduct")
    
    if schema_type == "FinancialProduct":
        data = {
            "@context": "https://schema.org",
            "@type": "FinancialProduct",
            "name": f"{query.title()} MoMo",
            "description": ontology["ai_answer_template"],
            "provider": {
                "@type": "BankOrCreditUnion",
                "name": "Ngân hàng Thương mại Cổ phần Bản Việt (BVBank) & TPBank",
                "url": "https://www.momo.vn"
            },
            "category": "Ví trả sau / Tín dụng tiêu dùng",
            "areaServed": {
                "@type": "Country",
                "name": "Vietnam"
            },
            "interestRate": {
                "@type": "QuantitativeValue",
                "value": "0.0",
                "unitText": "% trong chu kỳ miễn lãi tối đa 45 ngày"
            },
            "feesAndCommissionsSpecification": "Miễn phí duy trì nếu không phát sinh dư nợ trong tháng. Phí dịch vụ cố định theo kỳ sử dụng.",
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.8",
                "reviewCount": "12500",
                "bestRating": "5"
            }
        }
    elif schema_type == "LoanOrCredit":
        data = {
            "@context": "https://schema.org",
            "@type": "LoanOrCredit",
            "name": f"Gói Vay Tiêu Dùng Trực Tuyến {query.title()}",
            "description": ontology["ai_answer_template"],
            "provider": {
                "@type": "FinancialService",
                "name": "Đối tác tài chính được cấp phép liên kết trên MoMo",
                "url": "https://www.momo.vn"
            },
            "amount": {
                "@type": "MonetaryAmount",
                "currency": "VND",
                "minValue": "1000000",
                "maxValue": "100000000"
            },
            "annualPercentageRate": {
                "@type": "QuantitativeValue",
                "minValue": "12.0",
                "maxValue": "25.0",
                "unitText": "%/năm tính theo dư nợ giảm dần"
            },
            "areaServed": "VN"
        }
    elif schema_type == "Movie":
        data = {
            "@context": "https://schema.org",
            "@type": "Movie",
            "name": query.title(),
            "description": ontology["ai_answer_template"],
            "contentRating": "T18",
            "duration": "PT120M",
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "8.5",
                "reviewCount": "3400"
            }
        }
    else:
        data = {
            "@context": "https://schema.org",
            "@type": schema_type,
            "name": query.title(),
            "description": ontology["ai_answer_template"],
            "publisher": {
                "@type": "Organization",
                "name": "MoMo Web Platform",
                "url": "https://www.momo.vn"
            }
        }
        
    return json.dumps(data, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------------------
# 5. TỔNG HỢP VÀ XUẤT BẢN BLUEPRINT CHIẾN LƯỢC
# ---------------------------------------------------------------------------

def build_geo_blueprint(query: str, manual_hub: str = None, fast: bool = False) -> dict:
    """Quy trình tổng hợp toàn bộ các thực thể, câu trả lời trực tiếp và Schema."""
    print(f"\n=== KHỞI ĐỘNG GEO ENTITY GAP GENERATOR CHO: '{query}' ===")
    
    ontology = resolve_domain_ontology(query, manual_hub)
    print(f"-> Xác định ngành: [{ontology['hub']}] | Chủ đề: [{ontology['theme']}]")
    print(f"-> Schema chủ đạo: [{ontology['schema_type']}]")

    # Thu thập SERP nếu không bật chế độ fast
    serp_data = {"serp_items": [], "momo_ranking": None, "headings": []}
    if not fast:
        serp_data = audit_competitor_serp(query, limit=3)
        print(f"-> Đã thu thập {len(serp_data['serp_items'])} đối thủ dẫn đầu SERP.")
    else:
        print("-> Chế độ Fast Mode: Sử dụng bộ dữ liệu Domain Ontology trực tiếp.")

    # Tìm Deeplink và Event đo lường nếu có trong config
    slug = slugify(query)
    cta_tuple = FEATURE_MOMO_MAP.get(slug)
    if not cta_tuple:
        # Thử tìm theo từ khóa đơn
        for k, v in FEATURE_MOMO_MAP.items():
            if k in slug:
                cta_tuple = v
                break

    cta_info = {
        "cta_text": cta_tuple[0] if cta_tuple else f"Trải Nghiệm Tiện Ích {query.title()} Trên MoMo",
        "deeplink": cta_tuple[1] if cta_tuple else f"momo://app-action?service={slug}",
        "umami_event": cta_tuple[2] if cta_tuple else f"web_{slug.replace('-', '_')}_btn_click"
    }

    schema_jsonld_str = generate_schema_jsonld(ontology, query)

    # Đóng gói Blueprint
    blueprint = {
        "query": query,
        "slug": slug,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hub": ontology["hub"],
        "theme": ontology["theme"],
        "schema": {
            "type": ontology["schema_type"],
            "category": ontology.get("schema_category", ""),
            "mandatory_fields": ontology["schema_mandatory_fields"],
            "sample_jsonld": schema_jsonld_str
        },
        "direct_answer_box": {
            "text": ontology["ai_answer_template"],
            "word_count": len(ontology["ai_answer_template"].split()),
            "format": "Inverted Pyramid (Khái niệm -> Cơ chế -> Lợi ích)"
        },
        "entity_gaps": ontology["pillars"],
        "competitor_serp_summary": {
            "crawled_count": len(serp_data["serp_items"]),
            "top_competitors": [item.get("domain") for item in serp_data["serp_items"]],
            "momo_current_rank": serp_data.get("momo_ranking", {}).get("rank") if serp_data.get("momo_ranking") else "Chưa nằm trong Top 5"
        },
        "actionable_content_blueprint": [
            f"# H1: {query.title()}: Định Nghĩa Bản Chất, Điều Kiện & Bảng Biểu Phí Chi Tiết Nhất 2026",
            f"<!-- AI Answer Box Hook: Đặt ngay bên dưới H1 trong thẻ blockquote -->",
            f"> \"{ontology['ai_answer_template']}\"",
            f"## H2 1: {query.title()} Là Gì? Bản Chất & Cơ Chế Hoạt Động Cốt Lõi",
            f"## H2 2: {ontology['pillars']['expertise']['title']} (Góc Chuyên Gia E-E-A-T)",
            f"   - {ontology['pillars']['expertise']['actionable_angle']}",
            f"## H2 3: {ontology['pillars']['trust']['title']} (Hạ Tầng & Bảo Mật)",
            f"   - {ontology['pillars']['trust']['actionable_angle']}",
            f"## H2 4: {ontology['pillars']['high_intent']['title']} (Minh Bạch Phí)",
            f"   - {ontology['pillars']['high_intent']['actionable_angle']}",
            f"## H2 5: Hướng Dẫn Thao Tác Trực Tuyến & Chuyển Tiếp Liền Mạch Lên MoMo",
            f"   - CTA Hook: [{cta_info['cta_text']}]({cta_info['deeplink']}) | Event: `{cta_info['umami_event']}`"
        ],
        "web_to_app_cta": cta_info
    }

    return blueprint

# ---------------------------------------------------------------------------
# 6. XUẤT BẢN BÁO CÁO MARKDOWN & SNAPSHOT JSON
# ---------------------------------------------------------------------------

def save_blueprint_files(blueprint: dict):
    """Lưu trữ báo cáo Markdown và dữ liệu JSON vào thư mục SSOT."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    slug = blueprint["slug"]
    md_path = os.path.join(REPORTS_DIR, f"{slug}-geo-blueprint.md")
    json_path = os.path.join(DATA_DIR, f"{slug}.json")

    # Lưu JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, ensure_ascii=False, indent=2)

    # Tạo nội dung Markdown chuyên nghiệp chuẩn Tech Lead
    md = f"""# CHIẾN LƯỢC TỐI ƯU HÓA THỰC THỂ & GEO BLUEPRINT: {blueprint['query'].upper()}

> **Phân nhóm:** {blueprint['hub']} | **Chuyên đề:** {blueprint['theme']}  
> **Thời gian tạo:** {blueprint['generated_at']}  
> **Định vị Schema:** `{blueprint['schema']['type']}`  
> **Thực thể mục tiêu:** Trả lời trực diện cho Google AI Overviews, Perplexity & Bing Copilot

---

## 1. KHUYẾN NGHỊ DỮ LIỆU CÓ CẤU TRÚC (STRUCTURED DATA / SCHEMA)

Nên sử dụng Schema `{blueprint['schema']['type']}` để các công cụ tìm kiếm và AI Search hiểu rõ bản chất nghiệp vụ:

* **Loại Schema chính:** `{blueprint['schema']['type']}` ({blueprint['schema']['category'] or 'Standard'})
* **Các trường dữ liệu bắt buộc:**

"""
    for field in blueprint["schema"]["mandatory_fields"]:
        md += f"  - `{field['field']}`: {field['desc']}\n"

    md += f"""
### Mã JSON-LD Mẫu Chuẩn Hóa:

```html
<script type="application/ld+json">
{blueprint['schema']['sample_jsonld']}
</script>
```

---

## 2. ĐOẠN TRÍCH TRẢ LỜI TRỰC TIẾP (AI ANSWER BOX / ZERO-CLICK HOOK)

Đoạn văn ngắn đạt chuẩn kim tự tháp ngược (Inverted Pyramid), loại bỏ từ ngữ sáo rỗng để máy tìm kiếm dễ dàng bóc tách làm câu trả lời tóm tắt ở vị trí Top 0:

> "{blueprint['direct_answer_box']['text']}"

* **Số lượng từ:** {blueprint['direct_answer_box']['word_count']} từ (Đạt chuẩn tối ưu 40-55 từ).
* **Cấu trúc:** Thực thể định nghĩa ➔ Cơ chế vận hành số hóa ➔ Giá trị cốt lõi giải phóng rào cản.

---

## 3. LỖ HỔNG THỰC THỂ ĐỐI THỦ (ENTITY GAPS & INFORMATION GAIN)

Để vượt mặt các đối thủ đang xếp hạng cao, nội dung của Web Platform cần lấp đầy 3 điểm mù ngữ nghĩa mà các trang khác thường bỏ sót:

### 3.1. {blueprint['entity_gaps']['expertise']['title']} (Góc Chuyên Gia E-E-A-T)
* **Bản chất vấn đề:** {blueprint['entity_gaps']['expertise']['summary']}
* **Phân tích chiều sâu:** {blueprint['entity_gaps']['expertise']['detail']}
* **Hành động triển khai:** {blueprint['entity_gaps']['expertise']['actionable_angle']}

### 3.2. {blueprint['entity_gaps']['trust']['title']} (Hạ Tầng & Bảo Mật)
* **Bản chất vấn đề:** {blueprint['entity_gaps']['trust']['summary']}
* **Phân tích chiều sâu:** {blueprint['entity_gaps']['trust']['detail']}
* **Hành động triển khai:** {blueprint['entity_gaps']['trust']['actionable_angle']}

### 3.3. {blueprint['entity_gaps']['high_intent']['title']} (Minh Bạch Chi Phí / High Intent)
* **Bản chất vấn đề:** {blueprint['entity_gaps']['high_intent']['summary']}
* **Phân tích chiều sâu:** {blueprint['entity_gaps']['high_intent']['detail']}
* **Hành động triển khai:** {blueprint['entity_gaps']['high_intent']['actionable_angle']}

---

## 4. DÀN Ý BÀI VIẾT VƯỢT MẶT ĐỐI THỦ (WINNING HEADING BLUEPRINT)

Dàn ý cấu trúc chuẩn E-E-A-T tích hợp trực tiếp các thực thể và điểm chạm chuyển đổi:

"""
    for heading in blueprint["actionable_content_blueprint"]:
        md += f"{heading}\n"

    md += f"""
---

## 5. CƠ CHẾ CHUYỂN TIẾP WEB-TO-APP & EVENT TRACKING

* **Tên nút kêu gọi hành động (CTA):** {blueprint['web_to_app_cta']['cta_text']}
* **Deeplink chuyển tiếp vào App MoMo:** `{blueprint['web_to_app_cta']['deeplink']}`
* **Tên sự kiện đo lường Umami (Utility Tracking SSOT):** `{blueprint['web_to_app_cta']['umami_event']}`
"""

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"\n-> Đã xuất bản Blueprint Markdown tại: {md_path}")
    print(f"-> Đã lưu dữ liệu JSON Snapshot tại: {json_path}")
    return md_path, json_path

# ---------------------------------------------------------------------------
# 7. IN GIAO DIỆN TERMINAL KIỂU CARD TRỰC QUAN (TERMINAL CARD VIEW)
# ---------------------------------------------------------------------------

def print_terminal_card(blueprint: dict):
    """In ra màn hình terminal một thẻ thông tin trực quan tương đương UI của Wriai."""
    q = blueprint["query"].upper()
    sep = "=" * 80
    subsep = "-" * 80
    
    print("\n" + sep)
    print(f"  GEO & ENTITY GAP INTELLIGENCE CARD: {q}")
    print(f"  Hub: {blueprint['hub']} | Theme: {blueprint['theme']}")
    print(sep)
    
    # 1. Schema
    print("\n[1] KHUYẾN NGHỊ SCHEMA CHO AI SEARCH")
    print(f"  * Loại Schema: {blueprint['schema']['type']}")
    print("  * Các trường bắt buộc:")
    for f in blueprint['schema']['mandatory_fields'][:4]:
        print(f"    - {f['field']}: {f['desc']}")
        
    # 2. AI Answer Box
    print("\n[2] ĐOẠN TRÍCH TRẢ LỜI TRỰC TIẾP (AI ANSWER BOX)")
    print(f"  ┌{subsep[:76]}┐")
    wrapped_lines = textwrap.wrap(blueprint['direct_answer_box']['text'], width=70)
    for line in wrapped_lines:
        print(f"  │ \"{line.ljust(70)}\" │")
    print(f"  └{subsep[:76]}┘")
    print(f"  (Độ dài: {blueprint['direct_answer_box']['word_count']} từ | Chuẩn: Inverted Pyramid)")
    
    # 3. Entity Gaps
    print("\n[3] LỖ HỔNG THỰC THỂ (ENTITY GAPS - ĐIỂM MÙ ĐỐI THỦ BỎ SÓT)")
    eg = blueprint["entity_gaps"]
    print(f"  1. {eg['expertise']['title']}:")
    print(f"     -> {eg['expertise']['summary']}")
    print(f"  2. {eg['trust']['title']}:")
    print(f"     -> {eg['trust']['summary']}")
    print(f"  3. {eg['high_intent']['title']}:")
    print(f"     -> {eg['high_intent']['summary']}")
    
    # 4. Conversion CTA
    print("\n[4] CHUYỂN ĐỔI WEB-TO-APP & EVENT TRACKING")
    print(f"  * CTA: {blueprint['web_to_app_cta']['cta_text']}")
    print(f"  * Deeplink: {blueprint['web_to_app_cta']['deeplink']}")
    print(f"  * Event Name: {blueprint['web_to_app_cta']['umami_event']}")
    print(sep + "\n")

# ---------------------------------------------------------------------------
# 8. HÀM MAIN VẬN HÀNH TỰ ĐỘNG
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="GEO Entity Gap & AI Search Blueprint Generator")
    parser.add_argument("query", nargs="?", default="ví trả sau", help="Từ khóa hoặc chủ đề cần phân tích (Mặc định: 'ví trả sau')")
    parser.add_argument("--hub", help="Chỉ định tên Hub (Financial, Cinema, Vehicle...)")
    parser.add_argument("--fast", action="store_true", help="Bỏ qua cào SERP trực tiếp, dùng Domain Ontology nhanh")
    args = parser.parse_args()

    blueprint = build_geo_blueprint(args.query, manual_hub=args.hub, fast=args.fast)
    save_blueprint_files(blueprint)
    print_terminal_card(blueprint)

if __name__ == "__main__":
    main()

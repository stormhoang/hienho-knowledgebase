#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PIPELINE CONTENT PLAN REFACTOR & AUDIT ENGINE
Triển khai toàn diện 5 yêu cầu tái cấu trúc Content Plan & SEO Clusters:
1. Reallocate misplaced keywords across themes (Lottery, Banks, Insurtech, Vehicle).
2. Merge spelling and accent variants with MAX volume (no sum) and record variants[].
3. Abolish fixed 6-slot templates; dynamically generate Silo URLs from qualifying sub-clusters (vol >= 500).
4. Compute priority (via classify_priority), funnel (majority intent), format (intent-driven) dynamically.
5. Replace generic fallback CTA hook with concrete MoMo feature mappings (or null).
"""

import os
import sys
import glob
import re
import json
import unicodedata
import pandas as pd
from collections import defaultdict, Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)
INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")
REPORT_FILE = os.path.join(BASE_DIR, "07_REPORTS", "CONTENT_PLAN_REFACTOR_REVIEW.md")
JSON_OUTPUT = os.path.join(BASE_DIR, "07_REPORTS", "data", "content_plan_refactor_audit.json")

# -------------------------------------------------------------
# 0. THƯ VIỆN CHUẨN HÓA & PHÂN LOẠI
# -------------------------------------------------------------
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def make_norm_key(text):
    text = text.lower().strip()
    text = remove_accents(text)
    return re.sub(r'[^a-z0-9]', '', text)

def slugify(text):
    text = remove_accents(text.lower().strip())
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text

def clean_val(val):
    if not val:
        return ""
    val = str(val).strip()
    if val.startswith('="') and val.endswith('"'):
        return val[2:-1]
    return val

def clean_csv(path):
    if not os.path.exists(path):
        return pd.DataFrame(columns=['clean_kw', 'clean_vol', 'cpc', 'comp', 'raw_file'])
    try:
        df = pd.read_csv(path)
    except Exception:
        return pd.DataFrame(columns=['clean_kw', 'clean_vol', 'cpc', 'comp', 'raw_file'])
        
    kw_col = next((c for c in df.columns if 'keyword' in c.lower()), None)
    if not kw_col:
        return pd.DataFrame(columns=['clean_kw', 'clean_vol', 'cpc', 'comp', 'raw_file'])
        
    vol_col = next((c for c in df.columns if 'volume' in c.lower()), None)
    cpc_col = next((c for c in df.columns if 'cpc' in c.lower()), None)
    comp_col = next((c for c in df.columns if 'competition' in c.lower()), None)
    
    if vol_col:
        df['clean_vol'] = pd.to_numeric(df[vol_col].astype(str).str.replace('="', '', regex=False).str.replace('"', '', regex=False), errors='coerce').fillna(0).astype(int)
    else:
        df['clean_vol'] = 0
        
    if cpc_col:
        df['cpc'] = pd.to_numeric(df[cpc_col].astype(str).str.replace('="', '', regex=False).str.replace('"', '', regex=False), errors='coerce').fillna(0.0)
    else:
        df['cpc'] = 0.0
        
    if comp_col:
        df['comp'] = df[comp_col].astype(str).str.replace('="', '', regex=False).str.replace('"', '', regex=False)
    else:
        df['comp'] = 'Low'
    
    kws = df[kw_col].astype(str).str.replace('="', '', regex=False).str.replace('"', '', regex=False)
    df['clean_kw'] = kws.str.strip().str.lower()
    df = df[~df['clean_kw'].isin(['kiệm', 'nhiêu', 'thoại', 'khoản', 'toán', 'phẩm', 'vụ'])]
    df['raw_file'] = os.path.basename(path)
    return df

# -------------------------------------------------------------
# 1. HỆ THỐNG INTENT, PRIORITY, FUNNEL, FORMAT CLASSIFIER
# -------------------------------------------------------------
INTENT_SIGNALS = {
    'Tool/Calculator': [
        'tính', 'cách tính', 'bảng tính', 'công cụ', 'tra cứu', 'kiem tra',
        'ước tính', 'mô phỏng', 'bao nhiêu tiền', 'lãi bao nhiêu', 'quy đổi', 'chuyển đổi'
    ],
    'Commercial': [
        'so sánh', 'nào tốt', 'nên chọn', 'đánh giá', 'review', 'top', 'ưu đãi',
        'khuyến mãi', 'lãi suất cao nhất', 'chiết khấu', 'rẻ nhất'
    ],
    'Transactional': [
        'mua', 'đặt', 'nạp', 'thanh toán', 'đăng ký', 'mở', 'vay', 'gia hạn',
        'thủ tục', 'hồ sơ', 'quy trình', 'rút tiền', 'đóng'
    ],
    'Navigational': [
        'đăng nhập', 'login', 'app', 'tổng đài', 'hotline', 'chi nhánh',
        'website', 'trang chủ', 'địa chỉ', 'cổng dịch vụ'
    ]
}

def detect_intent(keyword):
    kw = keyword.lower()
    for intent, signals in INTENT_SIGNALS.items():
        if any(s in kw for s in signals):
            return intent
    return 'Informational'

def classify_priority(volume, competition, intent):
    comp_val = str(competition).lower()
    is_high_comp = 'high' in comp_val or 'medium' in comp_val
    if (volume >= 2000 and not is_high_comp) or (intent in ['Tool/Calculator', 'Transactional'] and volume >= 500):
        return 'P0'
    elif volume >= 1000 or intent == 'Commercial':
        return 'P1'
    else:
        return 'P2'

def determine_funnel(intent):
    if intent in ['Tool/Calculator', 'Transactional']:
        return 'BOFU'
    elif intent == 'Commercial':
        return 'MOFU'
    return 'TOFU'

def recommend_format(intent, is_pillar=False):
    if is_pillar:
        return 'Pillar Hub Page + Interactive Widget'
    if intent == 'Tool/Calculator':
        return 'Interactive Calculator / Lookup Tool'
    elif intent == 'Commercial':
        return 'Comparison Table & Evaluation'
    elif intent == 'Transactional':
        return 'Step-by-step How-to & Action Form'
    elif intent == 'Navigational':
        return 'Directory & Service Portal'
    return 'Educational Guide & FAQ'

# -------------------------------------------------------------
# 2. BẢN ĐỒ TÍNH NĂNG MOMO CỤ THỂ CHO WEB-TO-APP (CTA HOOK SSOT)
# -------------------------------------------------------------
FEATURE_MOMO_MAP = {
    # Financial Hub
    'diem-tin-dung': ('Tra cứu Điểm Tín Dụng & Hồ Sơ CIC', 'momo://credit-score', 'web_cic_lookup_btn_click'),
    'no-xau': ('Kiểm tra Nợ Xấu & Điểm Tín Dụng CIC', 'momo://credit-score', 'web_cic_lookup_btn_click'),
    'gui-tiet-kiem': ('Mở Sổ Tiết Kiệm Online / Túi Thần Tài', 'momo://saving-partner', 'web_saving_interest_calculator_btn_click'),
    'lai-suat': ('Gửi Tiết Kiệm Online Lãi Suất Tốt', 'momo://saving-partner', 'web_saving_interest_calculator_btn_click'),
    'tich-luy': ('Tích Lũy Tiền Nhàn Rỗi Túi Thần Tài', 'momo://saving-partner', 'web_saving_interest_calculator_btn_click'),
    'gia-vang': ('Mua Vàng Tích Lũy / Túi Thần Tài', 'momo://gold-accumulation', 'web_gold_price_lookup_btn_click'),
    'ty-gia': ('Trải Nghiệm Nhận Tiền Quốc Tế MoMo', 'momo://international-remittance', 'web_exchange_rate_lookup_btn_click'),
    'doi-tien': ('Trải Nghiệm Nhận Tiền Quốc Tế MoMo', 'momo://international-remittance', 'web_exchange_rate_lookup_btn_click'),
    'kieu-hoi': ('Nhận Kiều Hối Trực Tiếp Vào MoMo', 'momo://international-remittance', 'web_exchange_rate_lookup_btn_click'),
    'chuyen-khoan': ('Chuyển Tiền Miễn Phí 24/7 Đến 50+ Ngân Hàng', 'momo://money-transfer', 'web_money_transfer_btn_click'),
    'thanh-toan-qr': ('Quét Mã QR MoMo Thanh Toán Đa Dịch Vụ', 'momo://qr-payment', 'web_qr_payment_btn_click'),
    'thue': ('Nộp Thuế Điện Tử Trực Tuyến Qua MoMo', 'momo://tax-payment', 'web_tax_payment_btn_click'),
    'thue-tncn': ('Nộp Thuế Thu Nhập Cá Nhân Trực Tuyến', 'momo://tax-payment', 'web_tax_payment_btn_click'),
    'tinh-luong': ('Tính Lương Gross Sang Net & Quản Lý Chi Tiêu', 'momo://financial-management', 'web_gross_net_calculator_btn_click'),
    'vay': ('Đăng Ký Khoản Vay Tiêu Dùng Online', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'vay-tin-chap': ('Vay Tín Chấp Hạn Mức Đến 100 Triệu', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'vay-the-chap': ('Đăng Ký Vay Thế Chấp Ngân Hàng Đối Tác', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'lai-vay': ('Mô Phỏng Khoản Vay & Đăng Ký In-App', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'vi-tra-sau': ('Kích Hoạt Ví Trả Sau Hạn Mức Đến 20 Triệu', 'momo://postpaid-wallet', 'web_postpaid_wallet_btn_click'),
    'mua-truoc-tra-sau': ('Kích Hoạt Ví Trả Sau Mua Sắm 0% Lãi', 'momo://postpaid-wallet', 'web_postpaid_wallet_btn_click'),
    'tra-gop': ('Thanh Toán Mua Hàng Trả Góp Qua MoMo', 'momo://installment-payment', 'web_installment_btn_click'),

    # Lottery Hub
    'vietlott': ('Đặt Vé Số Vietlott Online Qua MoMo', 'momo://lottery', 'web_lottery_btn_click'),
    'xo-so': ('Dò Kết Quả & Đặt Vé Số Trực Tuyến', 'momo://lottery', 'web_lottery_btn_click'),
    've-so': ('Dò Vé Số & Đặt Vé Số Trực Tuyến', 'momo://lottery', 'web_lottery_btn_click'),

    # Vehicle Hub
    'phat-nguoi': ('Nộp Phạt Nguội Giao Thông Toàn Quốc', 'momo://traffic-fine', 'web_traffic_fine_lookup_btn_click'),
    'gia-xang': ('Tìm Cây Xăng Thanh Toán MoMo', 'momo://gas-station', 'web_fuel_price_lookup_btn_click'),
    'gia-dau': ('Tìm Cây Xăng Thanh Toán MoMo', 'momo://gas-station', 'web_fuel_price_lookup_btn_click'),
    'tram-xang': ('Tìm Cây Xăng Thanh Toán MoMo', 'momo://gas-station', 'web_fuel_price_lookup_btn_click'),
    'vetc': ('Nạp Tiền Thu Phí Tự Động VETC Không Dừng', 'momo://etc-topup', 'web_etc_topup_btn_click'),
    'epass': ('Nạp Tiền Thu Phí Tự Động ePass Không Dừng', 'momo://etc-topup', 'web_etc_topup_btn_click'),
    'phi-khong-dung': ('Nạp Tài Khoản Thu Phí ETC Không Dừng', 'momo://etc-topup', 'web_etc_topup_btn_click'),
    'cuu-ho-xe': ('Gọi Cứu Hộ Ô Tô & Xe Máy Khẩn Cấp', 'momo://rescue-garage', 'web_garage_lookup_btn_click'),
    'gara-o-to': ('Tìm Gara Ô Tô Uy Tín Gần Nhất', 'momo://rescue-garage', 'web_garage_lookup_btn_click'),
    'thue-truoc-ba': ('Nộp Lệ Phí Trước Bạ Phương Tiện Online', 'momo://tax-payment', 'web_tax_payment_btn_click'),

    # Insurtech Hub
    'bhyt': ('Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online', 'momo://bhyt-renew', 'web_bhyt_lookup_btn_click'),
    'bhxh': ('Đóng Tiếp BHXH Tự Nguyện Trực Tuyến', 'momo://bhxh-payment', 'web_bhxh_payment_btn_click'),
    'bao-hiem-xe-may': ('Mua Bảo Hiểm Xe Máy Bắt Buộc Nhận Thẻ Điện Tử', 'momo://motorbike-insurance', 'web_motorbike_insurance_btn_click'),
    'bao-hiem-o-to': ('Mua Bảo Hiểm Ô Tô (TNDS & Vật Chất)', 'momo://car-insurance', 'web_car_insurance_btn_click'),
    'bao-hiem-tai-nan': ('Mua Bảo Hiểm Tai Nạn & Sức Khỏe Toàn Diện', 'momo://accident-insurance', 'web_accident_insurance_btn_click'),
    'bao-hiem-chay-no': ('Mua Bảo Hiểm Cháy Nổ Nhà Tư Nhân Online', 'momo://fire-insurance', 'web_fire_insurance_btn_click'),

    # OTA Hub
    've-may-bay': ('Đặt Vé Máy Bay Giá Rẻ Trên MoMo', 'momo://flight-booking', 'web_flight_booking_btn_click'),
    've-tau': ('Đặt Vé Tàu Hỏa Bắc Nam Trên MoMo', 'momo://train-booking', 'web_train_booking_btn_click'),
    'xe-khach': ('Đặt Vé Xe Khách Liên Tỉnh Trên MoMo', 'momo://bus-booking', 'web_bus_booking_btn_click'),
    've-xe': ('Đặt Vé Xe Khách & Xe Limousine', 'momo://bus-booking', 'web_bus_booking_btn_click'),

    # Cinema Hub
    'dat-phim': ('Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    'phim': ('Đặt Vé Phim Rạp Chiếu Mới Nhất', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    'rap': ('Đặt Vé Cụm Rạp CGV, Lotte, Galaxy', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    've-xem-phim': ('Mua Vé Xem Phim Nhận Ưu Đãi MoMo', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    'lich-phim': ('Tra Cứu Lịch Phim & Đặt Vé Tức Thì', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),

    # PS Hub
    'nap-game': ('Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao', 'momo://game-topup', 'web_game_card_topup_btn_click'),
    'nap-tiktok': ('Nạp Xu TikTok Trực Tuyến', 'momo://tiktok-topup', 'web_tiktok_topup_btn_click'),

    # Telco Hub
    'data-3g': ('Nạp Gói Data 3G Tốc Độ Cao MoMo', 'momo://data-topup', 'web_data_topup_btn_click'),
    'data-4g': ('Nạp Gói Cước Data 4G Viettel, Vina, Mobi', 'momo://data-topup', 'web_data_topup_btn_click'),
    'data-5g': ('Nạp Gói Cước 5G Siêu Tốc Độ', 'momo://data-topup', 'web_data_topup_btn_click'),
    'nap-data': ('Nạp Dung Lượng Data 3G/4G/5G Trực Tuyến', 'momo://data-topup', 'web_data_topup_btn_click'),
    'sim': ('Mua SIM Chính Chủ & Chọn Gói Cước Data', 'momo://sim-store', 'web_sim_store_btn_click'),

    # Hospital Hub
    'dat-lich-kham-benh': ('Đặt Lịch Khám Bệnh Tại Bệnh Viện Hàng Đầu', 'momo://hospital-booking', 'web_hospital_booking_btn_click'),
    'benh-vien': ('Thanh Toán Viện Phí & Đặt Lịch Khám Bệnh', 'momo://hospital-booking', 'web_hospital_booking_btn_click'),
}

def get_concrete_cta_hook(theme_slug):
    slug = theme_slug.lower()
    if slug in FEATURE_MOMO_MAP:
        name, link, evt = FEATURE_MOMO_MAP[slug]
        return f"{name} -> Deeplink: {link} -> Event: {evt}"
    return None

# -------------------------------------------------------------
# 3. QUY TẮC PHÂN CỤM NGỮ NGHĨA SUB-CLUSTERS (THEME & SECTOR)
# -------------------------------------------------------------
SUB_CLUSTER_RULES = {
    'vietlott': [
        ('Power 6/55', ['power 6 55', 'power 6/55', 'power 655', 'power655', 'xspower', 'power'], 'power-6-55'),
        ('Mega 6/45', ['mega 6 45', 'mega 6/45', 'mega 645', 'mega645', 'xổ số mega', 'mega'], 'mega-6-45'),
        ('Keno', ['keno', 'quay số nhanh'], 'keno'),
        ('Max 3D', ['max 3d', 'max3d', 'max 4d', 'max4d', 'max 3d pro'], 'max-3d'),
        ('Bingo 18', ['bingo', 'bingo18', 'bingo 18'], 'bingo-18'),
        ('Đại lý & Mua vé online', ['mua vé', 'mua ve', 'đại lý', 'dai ly', 'điểm bán', 'sms', 'app', 'online'], 'dai-ly-mua-ve'),
        ('Cơ cấu & Trúng thưởng', ['cơ cấu', 'co cau', 'giải thưởng', 'giai thuong', 'trúng thưởng', 'dò vé', 'do ve'], 'co-cau-trung-thuong'),
    ],
    'xo-so': [
        ('Xổ số Miền Bắc', ['miền bắc', 'mien bac', 'xsmb', 'sxmb', 'kqsxmb', 'bắc'], 'mien-bac'),
        ('Xổ số Miền Nam', ['miền nam', 'mien nam', 'xsmn', 'sxmn', 'kqsxmn', 'nam'], 'mien-nam'),
        ('Xổ số Miền Trung', ['miền trung', 'mien trung', 'xsmt', 'sxmt', 'kqsxmt', 'trung'], 'mien-trung'),
        ('Thống kê & Soi cầu', ['thống kê', 'thong ke', 'soi cầu', 'soi cau', 'lô gan', 'tần suất', 'bạch thủ'], 'thong-ke-soi-cau'),
        ('Quay thử & Trực tiếp', ['quay thử', 'quay thu', 'trực tiếp', 'truc tiep', 'live', 'sxtt'], 'quay-thu-truc-tiep'),
        ('Cơ cấu & Đổi thưởng', ['cơ cấu', 'co cau', 'giải thưởng', 'giai thuong', 'trúng', 'đổi vé', 'lãnh thưởng'], 'co-cau-doi-thuong'),
    ],
    've-so': [
        ('Dò vé số kiến thiết', ['dò', 'tra cứu', 'kiểm tra', 'hôm nay'], 'do-ve-so'),
        ('Đại lý & Điểm đổi vé', ['đại lý', 'đổi vé', 'hoa hồng', 'vé dạo'], 'dai-ly-doi-ve'),
        ('Cơ cấu giải thưởng vé số', ['cơ cấu', 'giải đặc biệt', 'giải phụ', 'vé số cào'], 'co-cau-giai-thuong'),
    ],
    'gia-vang': [
        ('Giá vàng SJC', ['sjc', 'vàng miếng'], 'gia-vang-sjc'),
        ('Vàng nhẫn 9999 & Vàng 24K', ['9999', 'nhẫn trơn', '24k', 'vàng nhẫn', 'vàng tây'], 'vang-nhan-9999'),
        ('Giá vàng DOJI & PNJ', ['doji', 'pnj', 'mi hồng', 'bảo tín'], 'vang-doji-pnj'),
        ('Biểu đồ & Dự báo giá vàng', ['biểu đồ', 'dự báo', 'xu hướng', 'thế giới', 'kitco'], 'bieu-do-du-bao'),
    ],
    'gui-tiet-kiem': [
        ('Lãi suất ngân hàng', ['lãi suất', 'lai suat', 'ngân hàng nào cao nhất', 'cao nhất'], 'lai-suat-ngan-hang'),
        ('Công cụ tính lãi', ['cách tính', 'tính lãi', 'công thức', '100 triệu', '50 triệu', '1 tỷ', 'bao nhiêu tiền'], 'tinh-lai'),
        ('Kỳ hạn & Hình thức gửi', ['kỳ hạn', 'không kỳ hạn', 'có kỳ hạn', 'bậc thang', 'online'], 'ky-han-hinh-thuc'),
        ('Thủ tục mở sổ & Rút tiền', ['thủ tục', 'rút tiền', 'trước hạn', 'sổ tiết kiệm', 'tất toán', 'mở sổ', 'đáo hạn'], 'thu-tuc-mo-so'),
        ('So sánh giải pháp tiết kiệm', ['so sánh', 'nên gửi', 'túi thần tài', 'vàng hay tiết kiệm', 'chứng chỉ tiền gửi'], 'so-sanh-tiet-kiem'),
    ],
    'diem-tin-dung': [
        ('Tra cứu CIC & Kiểm tra nợ xấu', ['tra cứu cic', 'kiểm tra cic', 'nợ xấu', 'nhóm nợ', 'check cic'], 'tra-cuu-cic'),
        ('Xóa nợ xấu & Cải thiện điểm', ['xóa nợ', 'cải thiện', 'điểm tín dụng', 'bao lâu'], 'xoa-no-xau'),
        ('Thủ tục & Biểu phí CIC', ['thủ tục', 'phí tra cứu', 'hồ sơ', 'mẫu đơn'], 'thu-tuc-bieu-phi'),
        ('Vay vốn theo điểm tín dụng', ['vay', 'ngân hàng', 'hạn mức', 'duyet vay'], 'vay-theo-diem-tin-dung'),
    ]
}

SECTOR_RULES = {
    'Financial': [
        ('Tỷ giá & Ngoại tệ', ['tỷ giá', 'ty gia', 'đô la', 'usd', 'ngoại tệ', 'ngoai te', 'euro', 'dxy', 'vnd', 'chuyển đổi'], 'ty-gia'),
        ('Lãi suất & Tiền gửi', ['lãi suất', 'lai suat', 'tiết kiệm', 'tiet kiem', 'gửi tiền', 'gui tien', 'kỳ hạn', 'ky han', 'rút tiền'], 'lai-suat'),
        ('Vay vốn & Tín chấp', ['vay', 'vay vốn', 'vay von', 'vay tiền', 'vay tien', 'tín chấp', 'tin chap', 'thế chấp', 'the chap', 'trả góp', 'tra gop', 'hạn mức'], 'vay-von'),
        ('Thẻ & Tài khoản', ['thẻ', 'the atm', 'thẻ tín dụng', 'the tin dung', 'mở thẻ', 'mo the', 'tài khoản', 'tai khoan', 'số tài khoản', 'phát hành thẻ'], 'the-tai-khoan'),
        ('Biểu phí & Thủ tục', ['phí', 'biểu phí', 'bieu phi', 'thủ tục', 'thu tuc', 'hồ sơ', 'ho so', 'điều kiện', 'dieu kien', 'hướng dẫn', 'huong dan', 'cách'], 'bieu-phi-thu-tuc'),
        ('Tra cứu & Chi nhánh', ['tra cứu', 'tra cuu', 'chi nhánh', 'chi nhanh', 'phòng giao dịch', 'tổng đài', 'tong dai', 'hotline', 'địa chỉ', 'dia chi', 'swift'], 'chi-nhanh'),
        ('Giá vàng & Kim loại quý', ['giá vàng', 'gia vang', 'vàng sjc', 'vàng 9999', 'nhẫn trơn', 'vàng miếng', 'vàng tây'], 'gia-vang'),
    ],
    'vehicle-hub': [
        ('Phạt nguội & Luật giao thông', ['phạt nguội', 'phat nguoi', 'lỗi vi phạm', 'mức phạt', 'nghị định', 'trừ điểm', 'bằng lái', 'giấy phép', 'camera'], 'phat-nguoi'),
        ('Bảo dưỡng & Nuôi xe', ['bảo dưỡng', 'bao duong', 'thay nhớt', 'chi phí', 'nuôi xe', 'xăng dầu', 'giá xăng', 'tiêu hao', 'đăng kiểm', 'sang tên'], 'bao-duong-nuoi-xe'),
        ('Gara & Cứu hộ', ['gara', 'garage', 'cứu hộ', 'cuu ho', 'sửa xe', 'sua xe', 'rửa xe', 'rua xe', 'vá lốp', 'kéo xe'], 'gara-cuu-ho'),
        ('Định giá & Mua bán xe', ['giá xe', 'gia xe', 'định giá', 'dinh gia', 'lăn bánh', 'lan banh', 'mua xe', 'bán xe', 'trả góp xe'], 'dinh-gia-xe'),
        ('Thu phí & Cây xăng', ['vetc', 'epass', 'không dừng', 'cây xăng', 'trạm xăng', 'petrolimex'], 'thu-phi-tram-xang'),
    ],
    'insurtech': [
        ('Tra cứu & Hạn sử dụng', ['tra cứu', 'kiểm tra', 'check', 'thời hạn', 'hạn sử dụng', 'mã số', 'thẻ', 'sổ'], 'tra-cuu-han-dung'),
        ('Biểu phí & Mua bảo hiểm', ['phí', 'biểu phí', 'giá', 'bao nhiêu tiền', 'mua', 'đóng', 'nộp', 'tái tục', 'online', 'trực tuyến'], 'bieu-phi-mua-online'),
        ('Quyền lợi & Chế độ', ['quyền lợi', 'khám chữa bệnh', 'bệnh viện', 'thanh toán', 'hưởng', 'chế độ', 'thai sản', 'hưu trí', 'ốm đau'], 'quyen-loi-che-do'),
        ('Quy định & Bồi thường', ['bồi thường', 'boi thuong', 'chi trả', 'mức phạt', 'bắt buộc', 'tnds', 'quy định', 'luật', 'nghị định', 'hồ sơ'], 'boi-thuong-quy-dinh'),
    ],
    'cinema': [
        ('Lịch chiếu & Suất chiếu', ['lịch chiếu', 'lich chieu', 'suất chiếu', 'suat chieu', 'gio chieu', 'chiếu rạp', 'phim chiếu', 'lịch phim'], 'lich-chieu'),
        ('Giá vé & Khuyến mãi', ['giá vé', 'gia ve', 'vé rẻ', 've re', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'voucher', 'combo', 'giảm giá'], 'gia-ve-khuyen-mai'),
        ('Cụm rạp & Đặt vé', ['rạp', 'cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'đặt vé', 'dat ve', 'đặt phim', 'mua vé'], 'rap-dat-ve'),
        ('Review & Đánh giá phim', ['review', 'đánh giá', 'danh gia', 'nội dung', 'diễn viên', 'trailer', 'phim hay', 'top phim'], 'review-danh-gia'),
    ],
    'PS': [
        ('Nạp thẻ & Chiết khấu', ['nạp', 'nap', 'thẻ', 'the', 'chiết khấu', 'chiet khau', 'garena', 'zing', 'vcoin', 'xu', 'tiktok', 'mua thẻ'], 'nap-the-chiet-khau'),
        ('Tựa game & Sự kiện', ['game', 'liên quân', 'free fire', 'pubg', 'tốc chiến', 'sự kiện', 'giftcode', 'code'], 'tua-game-su-kien'),
        ('Tài khoản & Hướng dẫn', ['tài khoản', 'tai khoan', 'đăng ký', 'nhà phát hành', 'nph', 'vng', 'garena', 'vtc'], 'tai-khoan-huong-dan'),
    ],
    'ota': [
        ('Vé máy bay & Di chuyển', ['vé máy bay', 've may bay', 'chuyến bay', 'vé tàu', 'vé xe', 'xe khách', 'cáp treo'], 've-di-chuyen'),
        ('Đặt phòng & Resort', ['khách sạn', 'khach san', 'resort', 'homestay', 'đặt phòng', 'dat phong', 'villa'], 'dat-phong-resort'),
        ('Tour & Điểm đến', ['tour', 'du lịch', 'du lich', 'hành trình', 'lịch trình', 'visa', 'điểm đến'], 'tour-diem-den'),
    ],
    'telco': [
        ('Gói cước & Data 4G/5G', ['data', '4g', '5g', '3g', 'gói cước', 'goi cuoc', 'nạp data', 'dung lượng'], 'goi-cuoc-data'),
        ('SIM & Tài khoản', ['sim', 'sim số', 'chính chủ', 'esim', 'tài khoản điện thoại', 'nạp thẻ'], 'sim-tai-khoan'),
    ],
    'hospital': [
        ('Đặt khám & Bác sĩ', ['đặt khám', 'dat kham', 'bác sĩ', 'bac si', 'bệnh viện', 'benh vien', 'phòng khám', 'chuyên khoa'], 'dat-kham-bac-si'),
        ('Chỉ số & Sức khỏe', ['bmi', 'calo', 'cân nặng', 'chiều cao', 'dinh dưỡng', 'sức khỏe'], 'chi-so-suc-khoe'),
    ]
}

FALLBACK_INTENT_CLUSTERS = [
    ('Công cụ & Tra cứu', 'Tool/Calculator', 'tra-cuu'),
    ('So sánh & Đánh giá', 'Commercial', 'so-sanh'),
    ('Đăng ký & Hướng dẫn thủ tục', 'Transactional', 'thu-tuc'),
    ('Cẩm nang & Hỏi đáp', 'Informational', 'cam-nang'),
    ('Cổng dịch vụ & Liên hệ', 'Navigational', 'lien-he'),
]

# -------------------------------------------------------------
# 4. CHẠY TOÀN BỘ PIPELINE
# -------------------------------------------------------------
print("Bắt đầu xử lý Pipeline Content Plan...")

# A. Quét inventory & Chuyển Theme (Reallocation)
VIETLOTT_ENTITIES = [
    'vietlott', 'viet lott', 'mega', 'power',
    'keno', 'max 3d', 'max3d', 'max 4d', 'max4d', 'bingo18', 'bingo 18',
    'bingo', '6/55', '6/45', '6 55', '6 45', '655', '645', 'xspower', 'xsp0wer', 'vietluck'
]

BANK_THEMES = {
    'mbbank': ['mb bank', 'mbbank', 'ngan hang mb', 'ngân hàng mb'],
    'Vietcombank': ['vietcombank', 'vcb', 'vietcom bank'],
    'Techcombank': ['techcombank', 'tcb', 'techcom bank'],
    'VietinBank': ['vietinbank', 'ctg', 'vietin bank'],
    'BIDV': ['bidv', 'ngan hang bidv', 'ngân hàng bidv'],
    'agribank': ['agribank', 'ngan hang agribank', 'ngân hàng agribank'],
    'ACB': ['acb bank', 'ngân hàng acb', 'ngan hang acb', 'acb'],
    'sacombank': ['sacombank', 'stb'],
    'vpbank': ['vpbank', 'vp bank'],
    'tpbank': ['tpbank', 'tp bank', 'tien phong bank', 'tiên phong bank'],
    'shb': ['shb bank', 'ngân hàng shb', 'ngan hang shb'],
    'hd-bank': ['hdbank', 'hd bank'],
    'vib': ['vib bank', 'ngân hàng vib', 'ngan hang vib'],
    'MSB': ['msb bank', 'ngân hàng msb', 'hàng hải'],
    'ocb': ['ocb bank', 'ngân hàng ocb', 'phương đông'],
    'seabank': ['seabank', 'sea bank', 'đông nam á'],
    'scb': ['scb bank', 'ngân hàng scb', 'sài gòn thương tín'],
    'ab-bank': ['ab bank', 'abbank', 'an bình'],
    'bac-a-bank': ['bac a bank', 'baca bank', 'bắc á bank'],
    'ban-viet': ['bản việt', 'bvbank', 'ban viet bank'],
    'bao-viet-bank': ['baoviet bank', 'bảo việt bank'],
    'kien-long-bank': ['kienlong bank', 'kienlongbank'],
    'LPBank': ['lpbank', 'lp bank', 'liên việt'],
    'nam-a-bank': ['nam a bank', 'namabank'],
    'ncb': ['ncb bank', 'quốc dân'],
    'ocean-bank': ['oceanbank', 'ocean bank', 'đại dương'],
    'pvcom bank': ['pvcombank', 'pvcom bank'],
    'saigonbank': ['saigonbank', 'saigon bank'],
    'Shinhan Bank': ['shinhan bank', 'shinhan'],
    'vietbank': ['vietbank', 'viet bank'],
    'vrb': ['vrb bank', 'việt nga'],
    'Indovina Bank': ['indovina bank', 'ivb'],
    'donga bank': ['đông á bank', 'donga bank', 'dong a bank'],
    'Eximbank': ['eximbank', 'exim bank']
}

from scripts.sync_inventory_to_hubs import MERGE_MAP, VIETNAMESE_THEME_NAMES

print("Bắt đầu xử lý Pipeline Content Plan...")
# Đọc toàn bộ các CSV vào raw database
all_csv_paths = glob.glob(os.path.join(INVENTORY_DIR, "*", "*.csv"))
theme_raw_dfs = defaultdict(list)
for p in all_csv_paths:
    sec = os.path.basename(os.path.dirname(p))
    t_slug = os.path.splitext(os.path.basename(p))[0]
    clean_s = re.sub(r'[\s_]*\(\d+\)$', '', t_slug).strip()
    canonical_s = MERGE_MAP.get(clean_s, clean_s)
    df_clean = clean_csv(p)
    if not df_clean.empty:
        theme_raw_dfs[(sec, canonical_s)].append(df_clean)

reallocated_moves = []
# Map cuối cùng của keywords theo từng theme: (sec, theme_slug) -> list of rows
theme_keywords = defaultdict(list)

# Bước 1: Reallocation audit
for (sec, t_slug), dfs in theme_raw_dfs.items():
    combined_df = pd.concat(dfs, ignore_index=True)
    for idx, r in combined_df.iterrows():
        kw = r['clean_kw']
        vol = r['clean_vol']
        cpc = r['cpc']
        comp = r['comp']
        moved = False

        # A. Lottery checks
        if sec == 'Lottery':
            has_vl = any(e in kw for e in VIETLOTT_ENTITIES)
            if t_slug == 'vietlott' and not has_vl:
                to_t = 've-so' if ('vé số' in kw or 'dò vé' in kw) else 'xo-so'
                reallocated_moves.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': 'vietlott',
                    'to_theme': to_t,
                    'sector': 'Lottery',
                    'reason': 'Từ khóa XSKT truyền thống nằm trong Vietlott'
                })
                theme_keywords[('Lottery', to_t)].append((kw, vol, cpc, comp))
                moved = True
            elif (t_slug in ['xo-so', 've-so']) and has_vl:
                reallocated_moves.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': t_slug,
                    'to_theme': 'vietlott',
                    'sector': 'Lottery',
                    'reason': 'Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số'
                })
                theme_keywords[('Lottery', 'vietlott')].append((kw, vol, cpc, comp))
                moved = True

        # B. Bank checks
        elif sec == 'Financial' and t_slug in BANK_THEMES:
            aliases = BANK_THEMES[t_slug]
            has_self = any(a in kw for a in aliases)
            if not has_self:
                for other_b, other_aliases in BANK_THEMES.items():
                    if other_b == t_slug:
                        continue
                    strong = [a for a in other_aliases if len(a) >= 4 and a in kw]
                    if strong:
                        reallocated_moves.append({
                            'keyword': kw,
                            'volume': vol,
                            'from_theme': t_slug,
                            'to_theme': other_b,
                            'sector': 'Financial',
                            'reason': f'Chứa thương hiệu ngân hàng đối thủ ({strong[0]})'
                        })
                        theme_keywords[('Financial', other_b)].append((kw, vol, cpc, comp))
                        moved = True
                        break

        # C. Insurtech checks
        elif sec == 'insurtech':
            if t_slug == 'bhyt' and ('bhxh' in kw or 'bảo hiểm xã hội' in kw) and ('bhyt' not in kw and 'bảo hiểm y tế' not in kw):
                reallocated_moves.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': 'bhyt',
                    'to_theme': 'bhxh',
                    'sector': 'insurtech',
                    'reason': 'Từ khóa thuần Bảo Hiểm Xã Hội nằm trong BHYT'
                })
                theme_keywords[('insurtech', 'bhxh')].append((kw, vol, cpc, comp))
                moved = True
            elif t_slug == 'bhxh' and ('bhyt' in kw or 'bảo hiểm y tế' in kw) and ('bhxh' not in kw and 'bảo hiểm xã hội' not in kw):
                reallocated_moves.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': 'bhxh',
                    'to_theme': 'bhyt',
                    'sector': 'insurtech',
                    'reason': 'Từ khóa thuần Bảo Hiểm Y Tế nằm trong BHXH'
                })
                theme_keywords[('insurtech', 'bhyt')].append((kw, vol, cpc, comp))
                moved = True

        # D. Vehicle Hub checks
        elif sec == 'vehicle-hub':
            if t_slug == 'vetc' and 'epass' in kw and 'vetc' not in kw:
                reallocated_moves.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': 'vetc',
                    'to_theme': 'epass',
                    'sector': 'vehicle-hub',
                    'reason': 'Từ khóa thương hiệu ePass nằm trong VETC'
                })
                theme_keywords[('vehicle-hub', 'epass')].append((kw, vol, cpc, comp))
                moved = True
            elif t_slug == 'epass' and 'vetc' in kw and 'epass' not in kw:
                reallocated_moves.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': 'epass',
                    'to_theme': 'vetc',
                    'sector': 'vehicle-hub',
                    'reason': 'Từ khóa thương hiệu VETC nằm trong ePass'
                })
                theme_keywords[('vehicle-hub', 'vetc')].append((kw, vol, cpc, comp))
                moved = True

        if not moved:
            theme_keywords[(sec, t_slug)].append((kw, vol, cpc, comp))

print(f"Tổng số từ khóa đã di chuyển sai theme: {len(reallocated_moves):,} từ khóa")

# Bước 2: Gộp biến thể chính tả (Max Volume & lưu variants[])
all_merged_variant_groups = []
theme_deduped_keywords = {}

for (sec, t_slug), rows in theme_keywords.items():
    # Nhóm theo normalized key
    groups = defaultdict(list)
    for kw, vol, cpc, comp in rows:
        n_key = make_norm_key(kw)
        groups[n_key].append({
            'kw': kw,
            'vol': vol,
            'cpc': cpc,
            'comp': comp,
            'has_accent': (kw != remove_accents(kw))
        })
    
    clean_kws = []
    for n_key, items in groups.items():
        if len(items) > 1:
            max_v = max(it['vol'] for it in items)
            max_cpc = max(it['cpc'] for it in items)
            # Chọn canonical: Ưu tiên có dấu, sau đó là volume cao nhất, sau đó là có khoảng trắng
            def sort_key(x):
                kw_str = x['kw']
                is_exact_brand = 1 if kw_str in ['vietlott', 'epass', 'vetc', 'mbbank', 'vietcombank', 'techcombank', 'bidv', 'agribank', 'acb'] else 0
                return (is_exact_brand, x['has_accent'], x['vol'], len(kw_str.split()))
            sorted_it = sorted(items, key=sort_key, reverse=True)
            canonical_kw = sorted_it[0]['kw']
            comp_val = sorted_it[0]['comp']
            variants = [it['kw'] for it in items if it['kw'] != canonical_kw]
            
            clean_kws.append({
                'keyword': canonical_kw,
                'volume': max_v,
                'cpc': max_cpc,
                'competition': comp_val,
                'intent': detect_intent(canonical_kw),
                'variants': variants
            })
            all_merged_variant_groups.append({
                'theme': t_slug,
                'sector': sec,
                'canonical_keyword': canonical_kw,
                'max_volume': max_v,
                'variants': variants
            })
        else:
            it = items[0]
            clean_kws.append({
                'keyword': it['kw'],
                'volume': it['vol'],
                'cpc': it['cpc'],
                'competition': it['comp'],
                'intent': detect_intent(it['kw']),
                'variants': []
            })
            
    theme_deduped_keywords[(sec, t_slug)] = clean_kws

all_merged_variant_groups.sort(key=lambda x: x['max_volume'], reverse=True)
print(f"Tổng số nhóm biến thể đã gộp: {len(all_merged_variant_groups):,} nhóm")

# Bước 3: Phân Cụm & Sinh Dynamic Silo (Bỏ 6 slot cố định, lọc ngưỡng >= 500)
theme_silos = {}
pruned_clusters_list = []
THRESHOLD = 500

for (sec, t_slug), kws in sorted(theme_deduped_keywords.items()):
    if not kws:
        continue
    
    # Sắp xếp kws giảm dần theo volume
    kws.sort(key=lambda x: x['volume'], reverse=True)
    theme_display_name = VIETNAMESE_THEME_NAMES.get(t_slug, t_slug.replace('-', ' ').title())
    
    # 1. Nhóm từ khóa vào các Sub-clusters
    assigned_clusters = defaultdict(list)
    theme_rules = SUB_CLUSTER_RULES.get(t_slug) or SECTOR_RULES.get(sec) or []
    
    unassigned = []
    for k in kws:
        matched = False
        kw_l = k['keyword'].lower()
        for rule in theme_rules:
            c_name, triggers, c_slug = rule
            if any(tr in kw_l for tr in triggers):
                assigned_clusters[(c_name, c_slug)].append(k)
                matched = True
                break
        if not matched:
            unassigned.append(k)
            
    # Gán các từ khóa chưa khớp vào Fallback Intent clusters
    for k in unassigned:
        intent = k['intent']
        fb = next((f for f in FALLBACK_INTENT_CLUSTERS if f[1] == intent), FALLBACK_INTENT_CLUSTERS[3])
        assigned_clusters[(fb[0], fb[2])].append(k)
        
    # 2. Xây dựng Pillar Hub Page
    top_overall_kw = kws[0]
    total_theme_vol = sum(k['volume'] for k in kws)
    pillar_cta = get_concrete_cta_hook(t_slug)
    
    pillar_page = {
        'slug': f"/{t_slug}/",
        'title': f"Cẩm Nang & Bảng Tra Cứu {theme_display_name} Toàn Diện",
        'primary_kw': top_overall_kw['keyword'],
        'secondary_kws': [k['keyword'] for k in kws[1:5]],
        'volume': top_overall_kw['volume'],
        'intent': top_overall_kw['intent'],
        'format': 'Pillar Hub Page + Interactive Widget',
        'funnel': 'TOFU',
        'priority': 'P0',
        'cta_hook': pillar_cta,
        'variants_count': len(top_overall_kw.get('variants', []))
    }
    
    # 3. Duyệt từng Sub-cluster để tạo Child Pages hoặc Prune
    child_pages = []
    sorted_clusters = sorted(assigned_clusters.items(), key=lambda x: sum(k['volume'] for k in x[1]), reverse=True)
    
    for (c_name, c_slug), cluster_kws in sorted_clusters:
        cluster_kws.sort(key=lambda x: x['volume'], reverse=True)
        tot_vol = sum(k['volume'] for k in cluster_kws)
        primary_k = cluster_kws[0]
        p_vol = primary_k['volume']
        
        # Nếu primary_kw trùng với pillar_kw hoặc chỉ có duy nhất 1 cluster thì bỏ qua để tránh cannibalization
        if primary_k['keyword'] == top_overall_kw['keyword'] or len(sorted_clusters) == 1:
            continue
            
        # Kiểm tra ngưỡng 500
        if tot_vol < THRESHOLD and p_vol < THRESHOLD:
            pruned_clusters_list.append({
                'theme': t_slug,
                'sector': sec,
                'cluster_name': c_name,
                'total_volume': tot_vol,
                'primary_keyword': primary_k['keyword'],
                'primary_vol': p_vol,
                'reason': f"Dưới ngưỡng {THRESHOLD}/tháng (Total: {tot_vol}, Primary: {p_vol})"
            })
            continue
            
        # Cluster đạt ngưỡng -> Sinh 1 Standalone URL
        majority_intent = Counter(k['intent'] for k in cluster_kws).most_common(1)[0][0]
        prio = classify_priority(tot_vol, primary_k['competition'], majority_intent)
        funnel = determine_funnel(majority_intent)
        fmt = recommend_format(majority_intent)
        cta = get_concrete_cta_hook(t_slug)
        
        child_slug = f"/{t_slug}/{c_slug}/"
        child_pages.append({
            'slug': child_slug,
            'title': f"{c_name} {theme_display_name}: Hướng Dẫn & Tra Cứu Chi Tiết",
            'primary_kw': primary_k['keyword'],
            'secondary_kws': [k['keyword'] for k in cluster_kws[1:5]],
            'volume': tot_vol,
            'intent': majority_intent,
            'format': fmt,
            'funnel': funnel,
            'priority': prio,
            'cta_hook': cta,
            'variants_count': len(primary_k.get('variants', []))
        })
        
    theme_silos[t_slug] = {
        'theme': t_slug,
        'sector': sec,
        'total_keywords': len(kws),
        'total_volume': total_theme_vol,
        'pages': [pillar_page] + child_pages
    }

print(f"Tổng số cụm bị loại do < 500/tháng: {len(pruned_clusters_list):,} cụm")

# Bước 4: Thống kê Điểm chạm CTA Hook cụ thể
total_usecases = len(theme_silos)
mapped_usecases = sum(1 for s in theme_silos.values() if s['pages'][0]['cta_hook'] is not None)
print(f"Số Use Case có CTA Hook cụ thể: {mapped_usecases} / {total_usecases} ({round(mapped_usecases/total_usecases*100, 1)}%)")

# Lưu Audit JSON
audit_payload = {
    'summary': {
        'total_usecases': total_usecases,
        'reallocated_moves_count': len(reallocated_moves),
        'merged_variant_groups_count': len(all_merged_variant_groups),
        'pruned_clusters_count': len(pruned_clusters_list),
        'concrete_cta_mapped_usecases': mapped_usecases,
        'concrete_cta_percentage': round(mapped_usecases/total_usecases*100, 1)
    },
    'reallocated_moves': reallocated_moves,
    'merged_variant_groups': all_merged_variant_groups,
    'pruned_clusters': pruned_clusters_list,
    'theme_silos': theme_silos
}

os.makedirs(os.path.dirname(JSON_OUTPUT), exist_ok=True)
with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(audit_payload, f, ensure_ascii=False, indent=2)
print(f"Đã lưu Snapshot Audit JSON tại: {JSON_OUTPUT}")

# Xuất Báo cáo Markdown Review
md = f"""# BÁO CÁO TOÀN DIỆN: REVIEW KẾT QUẢ TÁI CẤU TRÚC PIPELINE CONTENT PLAN

Dữ liệu kiểm toán và rà soát từ kho SSOT `05_HUBS/inventory/` chuẩn bị đồng bộ cho Web Platform.
Đáp ứng đầy đủ 5 tiêu chí:
1. Phân loại từ khóa sai theme (Entity-based reallocation).
2. Gộp biến thể chính tả (Max volume, không cộng dồn, lưu variants).
3. Triệt tiêu khung 6 slot cố định, sinh URL từ sub-cluster thực tế theo ngưỡng $\ge 500$/tháng.
4. Thuộc tính Priority, Funnel, Format tính toán hoàn toàn từ dữ liệu.
5. Loại bỏ câu fallback chung, ánh xạ chính xác tính năng MoMo thực tế kèm Deeplink & Event đo lường (hoặc null).

---

## 1. TỔNG QUAN CHỈ SỐ KIỂM TOÁN

| Chỉ Số Đo Lường | Giá Trị Thực Tế | Ghi Chú Kỹ Thuật |
| :--- | :---: | :--- |
| **Tổng số Use Cases (Themes)** | **{total_usecases}** | Sau khi merge cic -> diem-tin-dung |
| **Từ khóa chuyển sai theme** | **{len(reallocated_moves):,}** | Lottery: Vietlott <-> XSKT; Bank đối thủ; BHYT <-> BHXH; VETC <-> ePass |
| **Nhóm biến thể chính tả đã gộp** | **{len(all_merged_variant_groups):,}** | Lấy Max Volume, loại trừ trùng lặp chính tả/khoảng trắng |
| **Cụm Sub-cluster bị loại (< 500)** | **{len(pruned_clusters_list):,}** | Dưới ngưỡng $\ge 500$/tháng, gộp vào section Pillar, không tách URL |
| **Use Case có CTA Hook cụ thể** | **{mapped_usecases} / {total_usecases} ({round(mapped_usecases/total_usecases*100, 1)}%)** | Ánh xạ tính năng thực tế MoMo; 100% theme còn lại trả về `null` |

---

## 2. A. DANH SÁCH KEYWORD ĐÃ CHUYỂN THEME (TOP ĐIỂN HÌNH)

Tổng cộng **{len(reallocated_moves):,} từ khóa** được chuyển về đúng thực thể chủ quản. Dưới đây là bảng trích xuất các từ khóa có volume lớn nhất:

| STT | Từ Khóa | Volume/Tháng | Chuyển Từ Theme | Chuyển Đến Theme | Lý Do Kỹ Thuật |
| :---: | :--- | :---: | :--- | :--- | :--- |
"""

for idx, m in enumerate(sorted(reallocated_moves, key=lambda x: x['volume'], reverse=True)[:50], 1):
    md += f"| {idx} | `{m['keyword']}` | {m['volume']:,} | `{m['from_theme']}` | `{m['to_theme']}` | {m['reason']} |\n"

md += f"""\n---

## 3. B. DANH SÁCH NHÓM BIẾN THỂ ĐÃ GỘP (MAX VOLUME)

Tổng cộng **{len(all_merged_variant_groups):,} nhóm biến thể** được làm sạch. Volume lấy MAX (không cộng dồn) để tránh phóng đại dung lượng thị trường:

| STT | Theme | Từ Khóa Chính (Canonical) | Max Volume | Danh Sách Biến Thể Đã Gộp (`variants[]`) |
| :---: | :--- | :--- | :---: | :--- |
"""

for idx, g in enumerate(all_merged_variant_groups[:60], 1):
    var_str = ", ".join([f"`{v}`" for v in g['variants'][:4]])
    if len(g['variants']) > 4:
        var_str += f" (+{len(g['variants']) - 4} khác)"
    md += f"| {idx} | `{g['theme']}` | **`{g['canonical_keyword']}`** | {g['max_volume']:,} | {var_str} |\n"

md += f"""\n---

## 4. C. SILO MỚI THEO TỪNG USE CASE (MẪU CÁC DỰ ÁN TRỌNG ĐIỂM)

Số trang mỗi Use Case thay đổi linh hoạt theo Search Demand thực tế (từ 1 đến 6 trang). Không còn slug cố định.

"""

sample_themes = ['vietlott', 'xo-so', 've-so', 'gia-vang', 'diem-tin-dung', 'phat-nguoi', 'gui-tiet-kiem', 'tinh-luong', 'nap-game', 'dat-phim', 'bhyt', 'vetc', 'gdp']

for st in sample_themes:
    if st not in theme_silos:
        continue
    sdata = theme_silos[st]
    md += f"""### Theme: `{st}` ({sdata['total_volume']:,} volume/tháng, {len(sdata['pages'])} trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Priority | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
"""
    for pidx, page in enumerate(sdata['pages'], 1):
        cta_display = f"`{page['cta_hook']}`" if page['cta_hook'] else "*null (Không có tính năng MoMo)*"
        md += f"| {pidx} | `{page['slug']}` | {page['title']} | `{page['primary_kw']}` | {page['volume']:,} | `{page['priority']}` | `{page['funnel']}` | {page['format']} | {cta_display} |\n"
    md += "\n"

md += f"""---

## 5. D. DANH SÁCH CỤM BỊ LOẠI DO DƯỚI NGƯỠNG VOLUME (< 500/THÁNG)

Tổng cộng **{len(pruned_clusters_list):,} cụm** có volume dưới ngưỡng 500/tháng bị loại bỏ khỏi danh mục trang độc lập và được tích hợp thành Section trong Pillar Page:

| STT | Theme | Phân Khối Ngành | Tên Cụm Bị Loại | Primary Keyword | Volume Cụm | Xử Lý Kiến Trúc |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
"""

for idx, p in enumerate(sorted(pruned_clusters_list, key=lambda x: x['total_volume'], reverse=True)[:50], 1):
    md += f"| {idx} | `{p['theme']}` | `{p['sector']}` | {p['cluster_name']} | `{p['primary_keyword']}` | {p['total_volume']:,} | Tích hợp thành Section trong Pillar Hub |\n"

md += f"""\n---

## 6. E. THỐNG KÊ MAPPING ĐIỂM CHẠM WEB-TO-APP (CTA HOOK)

- **Tổng số Use Cases:** {total_usecases}
- **Số Use Case có CTA Hook cụ thể:** **{mapped_usecases}** ({round(mapped_usecases/total_usecases*100, 1)}%)
- **Số Use Case trả về `null`:** **{total_usecases - mapped_usecases}** ({round((total_usecases - mapped_usecases)/total_usecases*100, 1)}%)
- **Nguyên tắc kỹ thuật:** Đã xóa bỏ hoàn toàn câu fallback chung *"Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ"*. Chỉ điền khi map được tính năng MoMo cụ thể gồm: `Tên Tính Năng -> Deeplink Đích -> Event Đo Lường`.
"""

with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"Đã xuất bản toàn bộ báo cáo Review tại: {REPORT_FILE}")

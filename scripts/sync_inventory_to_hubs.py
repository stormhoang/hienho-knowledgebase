#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC INVENTORY TO HUBS-MOMO PIPELINE
Tự động quét toàn bộ kho từ khóa Use Cases (05_HUBS/inventory/),
áp dụng động cơ Keyword Intelligence (Multi-signal Intent Classifier,
Semantic Domain Filter, SERP Cannibalization Shield)
và đồng bộ trực tiếp sang hubs-momo (react-web-momo) phục vụ giao diện & nội dung.
"""

import sys
import os
import glob
import csv
import re
import json
import math
import unicodedata
from datetime import datetime
from collections import defaultdict, Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"

# Thêm scripts vào path để import thư viện lib
sys.path.insert(0, BASE_DIR)
from scripts.lib.keyword_intelligence import (
    MultiSignalIntentClassifier,
    SemanticDomainFilter,
    SERPCannibalizationShield,
    MoMoDomainSERPShield,
    InternalLinkingTopologyEngine,
    GEODirectAnswerGenerator,
    clean_val,
    normalize_text,
    calculate_opportunity_score,
    classify_quadrant,
    calculate_kd
)

MERGE_MAP = {
    # Financial - Bank Consolidation -> ngan-hang
    'ACB': 'ngan-hang',
    'acb': 'ngan-hang',
    'BIDV': 'ngan-hang',
    'bidv': 'ngan-hang',
    'Eximbank': 'ngan-hang',
    'eximbank': 'ngan-hang',
    'Indovina Bank': 'ngan-hang',
    'Indovina-Bank': 'ngan-hang',
    'LPBank': 'ngan-hang',
    'LPBank ': 'ngan-hang',
    'MSB': 'ngan-hang',
    'Shinhan Bank': 'ngan-hang',
    'Shinhan-Bank': 'ngan-hang',
    'Techcombank': 'ngan-hang',
    'Vietcombank': 'ngan-hang',
    'vietcombank': 'ngan-hang',
    'VietinBank': 'ngan-hang',
    'viettinbank': 'ngan-hang',
    'ab-bank': 'ngan-hang',
    'agribank': 'ngan-hang',
    'bac-a-bank': 'ngan-hang',
    'ban-viet': 'ngan-hang',
    'bao-viet-bank': 'ngan-hang',
    'donga bank': 'ngan-hang',
    'donga-bank': 'ngan-hang',
    'hd-bank': 'ngan-hang',
    'kien-long-bank': 'ngan-hang',
    'mbbank': 'ngan-hang',
    'nam-a-bank': 'ngan-hang',
    'ncb': 'ngan-hang',
    'ocb': 'ngan-hang',
    'ocean-bank': 'ngan-hang',
    'pvcom bank': 'ngan-hang',
    'pvcom-bank': 'ngan-hang',
    'sacombank': 'ngan-hang',
    'saigonbank': 'ngan-hang',
    'scb': 'ngan-hang',
    'seabank': 'ngan-hang',
    'shb': 'ngan-hang',
    'tpbank': 'ngan-hang',
    'uob': 'ngan-hang',
    'vcb': 'ngan-hang',
    'vib': 'ngan-hang',
    'viet-bank': 'ngan-hang',
    'vpbank': 'ngan-hang',
    'vrb': 'ngan-hang',
    # Financial - Cannibalization & Intent Merges
    'vang': 'gia-vang',
    'tiet-kiem': 'gui-tiet-kiem',
    'chia-co-tuc': 'co-tuc',
    'mua-truoc-tra-sau': 'vi-tra-sau',
    'tien-ao': 'crypto',
    'tien-dien-tu': 'crypto',
    'tien-so': 'crypto',
    'no': 'no-xau',
    'thu-nhap': 'thue-tncn',
    'cic': 'diem-tin-dung',
    # Lottery
    'xskt': 'xo-so',
    # Insurtech
    'bao-hiem-y-te': 'bhyt',
    'bao-hiem-xe': 'bao-hiem-xe-may',
    'bao-hiem-than-vo': 'bao-hiem-o-to',
    'bao-hiem-vat-chat': 'bao-hiem-o-to',
    'dong-bao-hiem': 'bhxh',
    'bao-hiem': 'bhxh',
    'bao-hiem-benh': 'bao-hiem-tai-nan',
    # PS
    'nap-xu-tiktok': 'nap-tiktok',
    'nap-the-game': 'nap-game',
    # Cinema
    'mua-ve-phim': 'dat-phim',
    # OTA
    'du-lich-my': 'visa-du-lich',
    'xe-khach': 've-xe',
    # Vehicle Hub
    'bien-so': 'bien-so-xe',
    'garage-o-to': 'gara-o-to',
    'cuu-ho-o-to': 'cuu-ho-xe',
    'trạm-sac': 'tram-sac',
    'cay-xang': 'tram-xang',
    # Hospital
    'tinh-bmi': 'bmi',
    # Student
    'truong-dai-hoc': 'dai-hoc',
    # Other
    'lich-van-nien': 'lich-am',
    'voucher': 'ma-giam-gia',
    # Telco
    'Data-3g': 'data-4g',
    'data-3g': 'data-4g',
    'data-5g': 'data-4g',
    'nap-data': 'data-4g',
    'mang-4g': 'data-4g',
    'mang-5g': 'data-4g',
    'nap-card': 'nap-tien-dien-thoai',
    'sim-so-dep': 'sim',
}

VIETNAMESE_THEME_NAMES = {
    # === Financial (101) ===
    'ACB': 'Ngân Hàng ACB',
    'BIDV': 'Ngân Hàng BIDV',
    'Eximbank': 'Ngân Hàng Eximbank',
    'Indovina Bank': 'Ngân Hàng Indovina Bank',
    'LPBank': 'Ngân Hàng LPBank',
    'MSB': 'Ngân Hàng MSB',
    'Shinhan Bank': 'Ngân Hàng Shinhan Bank',
    'Techcombank': 'Ngân Hàng Techcombank',
    'Vietcombank': 'Ngân Hàng Vietcombank',
    'VietinBank': 'Ngân Hàng VietinBank',
    'ab-bank': 'Ngân Hàng ABBank',
    'agribank': 'Ngân Hàng Agribank',
    'bac': 'Bạc & Kim Loại Quý',
    'bac-a-bank': 'Ngân Hàng Bac A Bank',
    'ban-viet': 'Ngân Hàng Bản Việt (BVBank)',
    'bao-viet-bank': 'Ngân Hàng BaoViet Bank',
    'chia-co-tuc': 'Chia Cổ Tức',
    'chung-chi-quy': 'Chứng Chỉ Quỹ',
    'chung-chi-tien-gui': 'Chứng Chỉ Tiền Gửi',
    'chung-khoan': 'Chứng Khoán',
    'chuyen-khoan': 'Chuyển Khoản & Chuyển Tiền',
    'co-phieu': 'Cổ Phiếu',
    'co-tuc': 'Cổ Tức',
    'crypto': 'Tiền Điện Tử (Crypto)',
    'dau-tu': 'Đầu Tư Tài Chính',
    'diem-tin-dung': 'Điểm Tín Dụng & Tra Cứu CIC',
    'doi-tien': 'Đổi Ngoại Tệ',
    'dong-tien': 'Quản Lý Dòng Tiền',
    'donga bank': 'Ngân Hàng Đông Á',
    'du-no': 'Dư Nợ Tín Dụng',
    'gdp': 'Tổng Sản Phẩm Quốc Nội (GDP)',
    'gia-vang': 'Giá Vàng',
    'giam-phat': 'Giảm Phát',
    'giam-tru-gia-canh': 'Giảm Trừ Gia Cảnh',
    'gui-tiet-kiem': 'Gửi Tiết Kiệm',
    'hd-bank': 'Ngân Hàng HDBank',
    'internet-banking': 'Ngân Hàng Trực Tuyến (Internet Banking)',
    'ke-hoach-tai-chinh': 'Kế Hoạch Tài Chính',
    'kien-long-bank': 'Ngân Hàng KienlongBank',
    'kieu-hoi': 'Kiều Hối',
    'ky-quy': 'Ký Quỹ',
    'lai-kep': 'Lãi Kép & Công Thức Tính',
    'lai-suat': 'Lãi Suất Ngân Hàng',
    'lai-vay': 'Lãi Vay',
    'lam-phat': 'Lạm Phát',
    'ma-chung-khoan': 'Mã Cổ Phiếu & Chứng Khoán',
    'masteer-card': 'Thẻ Mastercard',
    'mbbank': 'Ngân Hàng MBBank',
    'mua-truoc-tra-sau': 'Mua Trước Trả Sau (BNPL)',
    'nam-a-bank': 'Ngân Hàng Nam A Bank',
    'napas': 'Cổng Thanh Toán NAPAS',
    'ncb': 'Ngân Hàng NCB',
    'ngan-hang': 'Hệ Thống Ngân Hàng',
    'ngoai-te': 'Tỷ Giá Ngoại Tệ',
    'no-xau': 'Nợ Xấu & CIC',
    'ocb': 'Ngân Hàng OCB',
    'ocean-bank': 'Ngân Hàng OceanBank',
    'phai-sinh': 'Chứng Khoán Phái Sinh',
    'pvcom bank': 'Ngân Hàng PVcomBank',
    'quy-du-phong': 'Quỹ Dự Phòng Khẩn Cấp',
    'quy-etf': 'Quỹ ETF',
    'quy-huu-tri': 'Quỹ Hưu Trí Tự Nguyện',
    'quy-mo': 'Quỹ Mở',
    'sacombank': 'Ngân Hàng Sacombank',
    'saigonbank': 'Ngân Hàng Saigonbank',
    'scb': 'Ngân Hàng SCB',
    'seabank': 'Ngân Hàng SeABank',
    'shb': 'Ngân Hàng SHB',
    'tai-san': 'Quản Trị Tài Sản',
    'thanh-toan-qr': 'Thanh Toán Mã QR',
    'thau-chi': 'Thấu Chi Tài Khoản',
    'the-ghi-no': 'Thẻ Ghi Nợ (Debit Card)',
    'the-tin-dung': 'Thẻ Tín Dụng',
    'the-tra-truoc': 'Thẻ Trả Trước',
    'the-visa': 'Thẻ Quốc Tế Visa',
    'thue': 'Tra Cứu & Nộp Thuế',
    'thue-tncn': 'Thuế Thu Nhập Cá Nhân (TNCN)',
    'tich-luy': 'Tích Lũy Tiền',
    'tien-ao': 'Tiền Ảo & Tài Sản Số',
    'tien-dien-tu': 'Tiền Điện Tử & Ví Điện Tử',
    'tien-so': 'Tiền Kỹ Thuật Số',
    'tieu-san': 'Tài Sản & Tiêu Sản',
    'tin-dung': 'Tín Dụng Cá Nhân',
    'tinh-luong': 'Tính Lương Gross Sang Net',
    'tpbank': 'Ngân Hàng TPBank',
    'tra-gop': 'Mua Hàng Trả Góp',
    'trai-phieu': 'Trái Phiếu Doanh Nghiệp',
    'tu-do-tai-chinh': 'Tự Do Tài Chính (FIRE)',
    'ty-gia': 'Tỷ Giá Ngoại Tệ',
    'uy-thac': 'Ủy Thác Đầu Tư',
    'vay': 'Vay Tiền Nhanh',
    'vay-the-chap': 'Vay Thế Chấp',
    'vay-tin-chap': 'Vay Tín Chấp',
    'vi-dien-tu': 'Ví Điện Tử',
    'vi-tra-sau': 'Ví Trả Sau',
    'vib': 'Ngân Hàng VIB',
    'vietbank': 'Ngân Hàng Vietbank',
    'von-luu-dong': 'Vốn Lưu Động',
    'vpbank': 'Ngân Hàng VPBank',
    'vrb': 'Ngân Hàng Việt Nga (VRB)',

    # === Lottery (3) ===
    've-so': 'Dò Vé Số Trực Tuyến',
    'vietlott': 'Vietlott Mega & Power',
    'xo-so': 'Xổ Số Kiến Thiết 3 Miền',

    # === PS (4) ===
    'game-app': 'Ứng Dụng Game',
    'nap-game': 'Nạp Thẻ Game',
    'nap-the-game': 'Nạp Thẻ Game',
    'nap-tiktok': 'Nạp Xu TikTok',
    'nph-game': 'Nhà Phát Hành Game',

    # === cinema (5) ===
    'dat-phim': 'Đặt Vé Phim Online',
    'lich-phim': 'Lịch Chiếu Phim Rạp',
    'phim': 'Phim Chiếu Rạp Mới Nhất',
    'rap': 'Rạp Chiếu Phim & Cụm Rạp',
    've-xem-phim': 'Giá Vé Xem Phim & Khuyến Mãi',

    # === hospital (4) ===
    'benh-vien': 'Bệnh Viện & Phòng Khám',
    'bmi': 'Chỉ Số & Tính Toán BMI Chuẩn',
    'dat-lich-kham-benh': 'Đặt Lịch Khám Bệnh',
    'tinh-calo': 'Tính Calo & Dinh Dưỡng',

    # === insurtech (8) ===
    'bao-hiem-chay-no': 'Bảo Hiểm Cháy Nổ',
    'bao-hiem-nhan-tho': 'Bảo Hiểm Nhân Thọ',
    'bao-hiem-o-to': 'Bảo Hiểm Ô Tô (TNDS & Vật Chất)',
    'bao-hiem-tai-nan': 'Bảo Hiểm Tai Nạn & Sức Khỏe',
    'bao-hiem-xe-may': 'Bảo Hiểm Xe Máy Bắt Buộc',
    'bhxh': 'Bảo Hiểm Xã Hội (BHXH)',
    'bhyt': 'Bảo Hiểm Y Tế (BHYT)',
    'phi-bao-hiem': 'Biểu Phí Bảo Hiểm',

    # === ota (19) ===
    'dat-resort': 'Đặt Resort Nghỉ Dưỡng',
    'du-lich': 'Cẩm Nang Du Lịch',
    'du-lich-an-do': 'Du Lịch Ấn Độ',
    'du-lich-dai-loan': 'Du Lịch Đài Loan',
    'du-lich-han-quoc': 'Du Lịch Hàn Quốc',
    'du-lich-hongkong': 'Du Lịch Hồng Kông',
    'du-lich-nhat': 'Du Lịch Nhật Bản',
    'du-lich-singapore': 'Du Lịch Singapore',
    'du-lich-thai-lan': 'Du Lịch Thái Lan',
    'du-lich-trung-quoc': 'Du Lịch Trung Quốc',
    'du-lich-viet-nam': 'Du Lịch Việt Nam',
    'gia-pha': 'Giá Vé Phà & Tuyến Phà',
    'tour-du-lich': 'Tour Du Lịch Trọn Gói',
    've-cap-treo': 'Vé Cáp Treo',
    've-may-bay': 'Vé Máy Bay Giá Rẻ',
    've-tau': 'Vé Tàu Hỏa Bắc Nam',
    've-xe': 'Vé Xe Khách',
    'visa-du-lich': 'Thủ Tục Visa Du Lịch',
    'xe-khach': 'Đặt Vé Xe Khách',

    # === other (3) ===
    'lich-am': 'Lịch Âm & Lịch Vạn Niên',
    'ma-giam-gia': 'Mã Giảm Giá & Voucher Khuyến Mãi',
    'ma-so-thue': 'Tra Cứu Mã Số Thuế',
    'tu-vi': 'Tử Vi Hàng Ngày & Trọn Đời',

    # === telco (8) ===
    'data-4g': 'Gói Cước & Nạp Data 4G/5G',
    'nap-tien-dien-thoai': 'Nạp Tiền Điện Thoại & Thẻ Cào',
    'sim': 'SIM Số Đẹp & eSIM',
    'sim-trung-quoc': 'SIM Trung Quốc',
    'sim-thai-lan': 'SIM Thái Lan',
    'sim-du-lich': 'SIM Du Lịch Quốc Tế',
    'esim-du-lich': 'eSIM Du Lịch',
    'sim-nhat-ban': 'SIM Nhật Bản',

    # === trust (2) ===
    'bao-cao-lua-dao': 'Báo Cáo Gian Lận & Lừa Đảo',
    'lua-dao': 'Cảnh Báo Thủ Đoạn Lừa Đảo',

    # === vehicle-hub (35) ===
    'bai-do-xe': 'Bãi Đỗ Xe & Bãi Giữ Xe',
    'bai-giu-xe': 'Bãi Giữ Xe Ô Tô & Xe Máy',
    'bao-duong-xe': 'Bảo Dưỡng Xe Định Kỳ',
    'bien-so-dep': 'Đấu Giá Biển Số Đẹp',
    'bien-so-xe': 'Tra Cứu Biển Số Xe Toàn Quốc',
    'chi-duong': 'Chỉ Đường & Bản Đồ Giao Thông',
    'cuu-ho-xe': 'Cứu Hộ Ô Tô & Xe Máy',
    'dang-kiem': 'Tra Cứu & Đặt Hẹn Đăng Kiểm Xe',
    'dinh-gia-xe': 'Định Giá Xe Ô Tô & Xe Máy',
    'doi-pin': 'Trạm Đổi Pin Xe Điện',
    'epass': 'Thu Phí Tự Động ePass',
    'gara-o-to': 'Gara Ô Tô Uy Tín',
    'garage-keywords-for-search-volume': 'Tra Cứu Hệ Thống Garage',
    'garage-keywords-list': 'Gara Ô Tô (Tổng Hợp)',
    'gia-dau': 'Giá Dầu Hôm Nay',
    'gia-xang': 'Giá Xăng Hôm Nay',
    'gia-xe': 'Bảng Giá Xe Ô Tô & Xe Máy',
    'giay-phep-lai-xe': 'Tra Cứu Giấy Phép Lái Xe',
    'loi-giao-thong': 'Tra Cứu Lỗi Vi Phạm Giao Thông',
    'ly-thuyet-lai-xe': 'Học Lý Thuyết Lái Xe A1, B1, B2',
    'metro': 'Tuyến Metro Bến Thành - Suối Tiên',
    'partner-garages': 'Danh Sách Đối Tác Garage',
    'phan-mem-mo-phong': 'Phần Mềm Mô Phỏng 120 Tình Huống',
    'phat-nguoi': 'Tra Cứu Phạt Nguội Toàn Quốc',
    'phi-duong-bo': 'Biểu Phí Sử Dụng Đường Bộ',
    'phi-khong-dung': 'Thu Phí Không Dừng (ETC)',
    'rua-xe': 'Dịch Vụ Rửa Xe Chuyên Nghiệp',
    'sang-ten-xe': 'Thủ Tục Sang Tên Đổi Chủ Xe',
    'sua-xe': 'Dịch Vụ Sửa Xe Lưu Động',
    'thi-bang-lai-xe': 'Thi Bằng Lái Xe Máy & Ô Tô',
    'thue-truoc-ba': 'Tính Thuế Trước Bạ Xe',
    'tram-sac': 'Trạm Sạc Xe Điện Toàn Quốc',
    'tram-xang': 'Trạm Xăng Gần Nhất',
    'tuyen-xe-buyt': 'Tra Cứu Tuyến Xe Buýt',
    'vetc': 'Thu Phí Tự Động VETC',

    # === student (9) ===
    'cao-dang': 'Cao Đẳng & Tuyển Sinh Cao Đẳng',
    'dai-hoc': 'Đại Học & Trường Đại Học',
    'diem-chuan': 'Điểm Chuẩn & Thi Tốt Nghiệp THPT',
    'hoc-phi': 'Học Phí Đại Học & Học Bổng',
    'nha-tro': 'Nhà Trọ & Phòng Trọ Sinh Viên',
    'sinh-vien': 'Sinh Viên & Cổng Thông Tin Đào Tạo',
    'truong-trung-cap': 'Trường Trung Cấp & Trung Cấp Nghề',
    'tuyen-sinh': 'Tuyển Sinh & Xét Tuyển Đại Học',
    'viec-lam-sinh-vien': 'Việc Làm Sinh Viên & Bán Thời Gian',
}

SECTOR_SPECIFIC_RULES = {
    'Financial': [
        ('Tỷ giá & Ngoại tệ', ['tỷ giá', 'ty gia', 'đô la', 'usd', 'ngoại tệ', 'ngoai te', 'euro', 'dxy', 'vnd', 'chuyển đổi']),
        ('Giá vàng & Kim loại quý', ['giá vàng', 'gia vang', 'vàng sjc', 'vàng 9999', 'nhẫn trơn', 'vàng miếng', 'vàng tây']),
        ('Lãi suất & Tiền gửi', ['lãi suất', 'lai suat', 'tiết kiệm', 'tiet kiem', 'gửi tiền', 'gui tien', 'kỳ hạn', 'ky han', 'rút tiền']),
        ('Vay vốn & Tín chấp', ['vay', 'vay vốn', 'vay von', 'vay tiền', 'vay tien', 'tín chấp', 'tin chap', 'thế chấp', 'the chap', 'trả góp', 'tra gop', 'hạn mức']),
        ('Thẻ & Tài khoản', ['thẻ', 'the atm', 'thẻ tín dụng', 'the tin dung', 'mở thẻ', 'mo the', 'tài khoản', 'tai khoan', 'số tài khoản', 'phát hành thẻ']),
        ('Biểu phí & Thủ tục', ['phí', 'biểu phí', 'bieu phi', 'thủ tục', 'thu tuc', 'hồ sơ', 'ho so', 'điều kiện', 'dieu kien', 'hướng dẫn', 'huong dan', 'cách']),
        ('Tra cứu & Chi nhánh', ['tra cứu', 'tra cuu', 'chi nhánh', 'chi nhanh', 'phòng giao dịch', 'tổng đài', 'tong dai', 'hotline', 'địa chỉ', 'dia chi', 'swift']),
    ],
    'vehicle-hub': [
        ('Phạt nguội & Luật giao thông', ['phạt nguội', 'phat nguoi', 'lỗi vi phạm', 'mức phạt', 'nghị định', 'trừ điểm', 'bằng lái', 'giấy phép', 'camera']),
        ('Bảo dưỡng & Nuôi xe', ['bảo dưỡng', 'bao duong', 'thay nhớt', 'chi phí', 'nuôi xe', 'xăng dầu', 'giá xăng', 'tiêu hao', 'đăng kiểm', 'sang tên']),
        ('Gara & Cứu hộ', ['gara', 'garage', 'cứu hộ', 'cuu ho', 'sửa xe', 'sua xe', 'rửa xe', 'rua xe', 'vá lốp', 'kéo xe']),
        ('Định giá & Mua bán xe', ['giá xe', 'gia xe', 'định giá', 'dinh gia', 'lăn bánh', 'lan banh', 'mua xe', 'bán xe', 'trả góp xe']),
    ],
    'insurtech': [
        ('Quy định & Mức bồi thường', ['bồi thường', 'boi thuong', 'chi trả', 'mức phạt', 'bắt buộc', 'tnds', 'quy định', 'luật', 'nghị định', 'hồ sơ']),
        ('Biểu phí & Mua bảo hiểm', ['phí', 'biểu phí', 'giá', 'bao nhiêu tiền', 'mua', 'đóng', 'nộp', 'tái tục', 'online', 'trực tuyến']),
        ('Tra cứu & Hạn sử dụng', ['tra cứu', 'kiểm tra', 'check', 'thời hạn', 'hạn sử dụng', 'mã số', 'thẻ', 'sổ']),
        ('Quyền lợi & Chế độ', ['quyền lợi', 'khám chữa bệnh', 'bệnh viện', 'thanh toán', 'hưởng', 'chế độ', 'thai sản', 'hưu trí', 'ốm đau']),
    ],
    'Lottery': [
        ('Kết quả xổ số', ['kết quả', 'ket qua', 'xsmb', 'xsmn', 'xsmt', 'sxtt', 'trực tiếp', 'truc tiep', 'kqsx', 'sxmb', 'sxmn', 'sxmt', 'xo so', 'xổ số', 'xô số', 'xô sô', 'xo số', 'xskt', 'kiến thiết', 'kien thiet', 'hôm nay', 'hom nay', 'miền bắc', 'miền nam', 'miền trung', 'minh ngọc', 'minhngoc']),
        ('Thống kê & Soi cầu', ['thống kê', 'thong ke', 'soi cầu', 'soi cau', 'lô gan', 'chu kỳ', 'tần suất', 'đầu đuôi', 'bạch thủ']),
        ('Cơ cấu & Đổi thưởng', ['giải thưởng', 'giai thuong', 'trúng thưởng', 'đổi vé', 'lãnh thưởng', 'thời hạn', 'cơ cấu', 'co cau', 'vé số', 've so']),
    ],
    'cinema': [
        ('Lịch chiếu & Suất chiếu', ['lịch chiếu', 'lich chieu', 'suất chiếu', 'suat chieu', 'gio chieu', 'chiếu rạp', 'phim chiếu', 'lịch phim']),
        ('Giá vé & Khuyến mãi', ['giá vé', 'gia ve', 'vé rẻ', 've re', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'voucher', 'combo', 'giảm giá']),
        ('Cụm rạp & Đặt vé', ['rạp', 'cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'đặt vé', 'dat ve', 'đặt phim', 'mua vé']),
        ('Review & Đánh giá phim', ['review', 'đánh giá', 'danh gia', 'nội dung', 'diễn viên', 'trailer', 'phim hay', 'top phim']),
    ],
}

# Per-use-case rules (overrides SECTOR_SPECIFIC_RULES when slug matches)
USECASE_SPECIFIC_RULES = {
    # === CINEMA (5) ===
    've-xem-phim': [
        ('Giá Vé & Khuyến Mãi Đặt Vé', ['giá vé', 'gia ve', 'vé rẻ', 've re', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'voucher', 'combo', 'giảm giá', 'bao nhiêu tiền', 'momo', 'học sinh', 'sinh viên', 'thứ 3', 'thứ 4']),
        ('Mua Vé Rạp & Ứng Dụng Online', ['mua vé', 'mua ve', 'đặt vé', 'dat ve', 'đặt phim', 'cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'beta', 'rạp', 'rap']),
        ('Cẩm Nang Hướng Dẫn Mua Vé', ['cách mua', 'hướng dẫn', 'kinh nghiệm', 'lưu ý', 'chọn ghế', 'đổi vé', 'hoàn vé', 'thanh toán']),
        ('Vé Xem Phim Chiếu Rạp Mới', ['vé xem phim', 've xem phim', 'phim chiếu rạp', 'bom tấn', 'phim hay', 'review', 'trailer', 'chiếu rạp', 'phim']),
    ],
    'lich-phim': [
        ('Lịch Chiếu Phim Hôm Nay & Cuối Tuần', ['hôm nay', 'hom nay', 'ngày mai', 'cuối tuần', 'suất chiếu', 'suat chieu', 'giờ chiếu', 'gio chieu', 'chiếu sớm', 'sneak']),
        ('Lịch Phim Theo Cụm Rạp Toàn Quốc', ['cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'beta', 'quốc gia', 'chieuphimquocgia', 'vincom', 'aeon', 'starlight', 'mega gs', 'dcine', 'rạp', 'rap']),
        ('Tra Cứu Lịch Phim Sắp & Đang Chiếu', ['đang chiếu', 'dang chieu', 'sắp chiếu', 'sap chieu', 'tuần này', 'tháng này', 'bom tấn', 'phim mới', 'phim chiếu']),
        ('Thông Tin Suất Chiếu & Lịch Rạp', ['lịch chiếu', 'lich chieu', 'lịch phim', 'lich phim', 'tra cứu', 'tìm lịch', 'xem lịch', 'phim', 'chiếu', 'lịch']),
    ],
    'rap': [
        ('Hệ Thống Rạp CGV Cinemas', ['cgv', 'cgv hà nội', 'cgv tp hcm', 'cgv vincom', 'cgv aeon', 'cgv quận']),
        ('Hệ Thống Rạp Lotte, Galaxy & BHD', ['lotte', 'galaxy', 'bhd', 'beta', 'cinestar', 'quốc gia', 'mega gs', 'dcine', 'starlight']),
        ('Rạp Chiếu Phim Gần Đây & Phòng Chiếu', ['gần đây', 'gan day', 'gần nhất', 'địa chỉ', 'chi nhánh', 'phòng chiếu', 'imax', '4dx', 'gold class', 'lamour', 'ghế đôi', 'sweetbox']),
        ('Bảng Giá & Dịch Vụ Bỏng Nước Tại Rạp', ['giá vé', 'gia ve', 'vé rẻ', 'bắp', 'bỏng', 'nước', 'combo', 'menu', 'dịch vụ', 'đặt vé', 'mua vé', 'rạp chiếu phim', 'rap chieu phim', 'phim chiếu rạp', 'rạp phim', 'cụm rạp', 'rạp', 'rap']),
    ],
    'dat-phim': [
        ('Đặt Vé CGV & Lotte Cinema', ['cgv', 'lotte', 'lotte cinema']),
        ('Đặt Vé Galaxy, Cinestar & Beta', ['galaxy', 'cinestar', 'beta', 'quốc gia', 'metiz', 'bhd', 'mega gs']),
        ('Đặt Vé Phim Online Qua App', ['app', 'online', 'momo', 'trực tuyến', 'đặt trước', 'chọn ghế']),
        ('Hướng Dẫn Đặt Vé & Thanh Toán', ['hướng dẫn', 'cách đặt', 'thanh toán', 'đổi vé', 'hoàn vé', 'đặt vé', 'dat ve', 'đặt phim', 'dat phim']),
    ],
    'phim': [
        ('Phim Chiếu Rạp Mới Nhất', ['chiếu rạp', 'chieu rap', 'phim rạp', 'phim mới', 'phim moi', 'sắp chiếu', 'bom tấn']),
        ('Top Phim Hay & Đánh Giá Phim', ['phim hay', 'top phim', 'review', 'đánh giá', 'trailer', 'thuyết minh', 'vietsub']),
        ('Phim Hoạt Hình & Anime Hot', ['hoạt hình', 'anime', '3d', 'hoat hinh', 'manga']),
        ('Thể Loại Phim & Tuyển Tập', ['hành động', 'kinh dị', 'tình cảm', 'hài', 'khoa học viễn tưởng', 'phim lẻ', 'phim bộ', 'phim']),
    ],

    # === FINANCIAL (4) ===
    'gui-tiet-kiem': [
        ('Lãi Suất Tiết Kiệm Vietcombank & Big 4', ['vietcombank', 'vcb', 'agribank', 'bidv', 'vietinbank']),
        ('Lãi Suất Tiết Kiệm Techcombank, MB & TMCP', ['techcombank', 'tcb', 'mbbank', 'mb bank', 'mb', 'sacombank', 'vpbank', 'acb', 'tpbank', 'hdbank', 'shb', 'vib', 'ocb', 'msb']),
        ('Công Cụ Tính Lãi Suất Tiết Kiệm', ['cách tính', 'tính lãi', 'công thức', '100 triệu', '50 triệu', '200 triệu', '500 triệu', '1 tỷ', 'bao nhiêu tiền', 'mỗi tháng']),
        ('Gửi Tiết Kiệm Online & An Toàn', ['online', 'trực tuyến', 'an toàn', 'app', 'mở sổ', 'kỳ hạn', 'không kỳ hạn', 'rút trước hạn', 'đáo hạn', 'sổ tiết kiệm']),
    ],
    'vay': [
        ('Vay Tiền Online Chuyển Khoản Nhanh', ['chuyển khoản', 'online', 'duyệt nhanh', 'cấp tốc', 'ngay', 'trong ngày', 'app vay', 'h5', 'cmnd', 'cccd', 'không thế chấp']),
        ('Vay Tín Chấp & Vay Tiêu Dùng Ngân Hàng', ['tín chấp', 'tin chap', 'tiêu dùng', 'ngân hàng', 'shb finance', 'fe credit', 'home credit', 'mcredit', 'lotte finance', 'shinhan']),
        ('Vay Theo Hạn Mức (Dưới 10tr - 50tr)', ['1 triệu', '2 triệu', '5 triệu', '10 triệu', '20 triệu', '30 triệu', '50 triệu', '100 triệu', 'hạn mức', 'khoản vay', 'sinh viên', 'nợ xấu']),
        ('Lãi Suất Vay & Công Cụ Tính Trả Góp', ['lãi suất', 'lai suat', 'trả góp', 'tra gop', 'cách tính', 'bảng tính', 'điều kiện', 'thủ tục', 'hồ sơ', 'vay']),
    ],
    'vay-nhanh': [
        ('Vay Tiền Online Chuyển Khoản Nhanh', ['chuyển khoản', 'online', 'duyệt nhanh', 'cấp tốc', 'ngay', 'trong ngày', 'app vay', 'h5', 'cmnd', 'cccd', 'không thế chấp']),
        ('Vay Tín Chấp & Vay Tiêu Dùng Ngân Hàng', ['tín chấp', 'tin chap', 'tiêu dùng', 'ngân hàng', 'shb finance', 'fe credit', 'home credit', 'mcredit', 'lotte finance', 'shinhan']),
        ('Vay Theo Hạn Mức (Dưới 10tr - 50tr)', ['1 triệu', '2 triệu', '5 triệu', '10 triệu', '20 triệu', '30 triệu', '50 triệu', '100 triệu', 'hạn mức', 'khoản vay', 'sinh viên', 'nợ xấu']),
        ('Lãi Suất Vay & Công Cụ Tính Trả Góp', ['lãi suất', 'lai suat', 'trả góp', 'tra gop', 'cách tính', 'bảng tính', 'điều kiện', 'thủ tục', 'hồ sơ', 'vay']),
    ],
    'vay-tin-chap': [
        ('Vay Tín Chấp Theo Lương & Hợp Đồng', ['theo lương', 'hợp đồng', 'sao kê', 'bảo hiểm nhân thọ', 'hóa đơn', 'tín chấp']),
        ('Vay Tín Chấp Ngân Hàng Lãi Suất Thấp', ['vietcombank', 'bidv', 'agribank', 'mbbank', 'vpbank', 'tpbank', 'shinhan', 'ngân hàng']),
        ('Điều Kiện & Thủ Tục Vay Tín Chấp', ['điều kiện', 'thủ tục', 'hồ sơ', 'duyệt vay', 'hạn mức', 'nợ xấu']),
        ('Bảng Tính Trả Góp & Lãi Suất Tín Chấp', ['lãi suất', 'trả góp', 'cách tính', 'bảng tính', 'dư nợ giảm dần', 'vay']),
    ],
    'diem-tin-dung': [
        ('Tra Cứu Điểm Tín Dụng & Check CIC', ['tra cứu', 'tra cuu', 'kiểm tra', 'kiem tra', 'check', 'xem điểm', 'cách kiểm tra', 'online', 'cá nhân', 'miễn phí']),
        ('Xóa Nợ Xấu & Xếp Hạng CIC', ['nợ xấu', 'no xau', 'nhóm nợ', 'hạng 5', 'hạng 6', 'hạng 7', 'hạng 8', 'xóa nợ', 'bao lâu', 'lịch sử nợ']),
        ('Điều Kiện Vay Theo Điểm Tín Dụng', ['có vay được không', 'vay được không', 'vay ngân hàng', 'duyệt vay', 'hạn mức', 'thẻ tín dụng', 'điều kiện']),
        ('Thủ Tục, Biểu Phí & Báo Cáo CIC', ['thủ tục', 'biểu phí', 'chi phí', 'bao nhiêu tiền', 'báo cáo', 'trung tâm cic', 'ngân hàng nhà nước', 'điểm tín dụng', 'cic']),
    ],
    'gia-vang': [
        ('Giá Vàng SJC & Vàng Miếng Hôm Nay', ['sjc', 'vàng miếng', 'vang mieng', 'hôm nay', 'hom nay', 'trong nước', 'hiện tại']),
        ('Giá Vàng DOJI, PNJ & Mi Hồng', ['doji', 'pnj', 'mi hồng', 'mi hong', 'bảo tín', 'bao tin', 'phú quý', 'huy thanh']),
        ('Giá Vàng Nhẫn 9999 & Vàng 24K, 18K', ['9999', 'nhẫn trơn', 'vàng nhẫn', '24k', '18k', 'vàng tây', 'vàng ta', 'vàng 10k']),
        ('Biểu Đồ Giá Vàng & Thị Trường Thế Giới', ['thế giới', 'the gioi', 'kitco', 'biểu đồ', 'dự báo', 'xu hướng', 'trực tuyến', 'giá vàng', 'gia vang']),
    ],

    # === INSURTECH (4) ===
    'bao-hiem-xe-may': [
        ('Bảo Hiểm Xe Máy Bắt Buộc (TNDS)', ['tnds', 'bắt buộc', 'bat buoc', 'trách nhiệm dân sự', 'trach nhiem dan su', 'quy định', 'luật', 'mức phạt', 'công an', 'bị phạt']),
        ('Bảo Hiểm Tự Nguyện & Cháy Nổ Xe Máy', ['tự nguyện', 'tu nguyen', 'cháy nổ', 'mất cắp', 'tai nạn', 'người ngồi trên xe', 'vật chất']),
        ('Biểu Phí & Mua Bảo Hiểm Xe Máy Online', ['mua', 'đặt', 'online', 'trực tuyến', 'giá', 'biểu phí', 'bao nhiêu tiền', '66k', '86k', 'app', 'momo', 'giao tận nơi']),
        ('Tra Cứu Hạn Dùng & Bồi Thường Xe Máy', ['tra cứu', 'kiểm tra', 'check', 'thời hạn', 'hạn dùng', 'điện tử', 'bồi thường', 'hồ sơ', 'thủ tục', 'bảo hiểm xe máy', 'bảo hiểm xe']),
    ],
    'bao-hiem-o-to': [
        ('Bảo Hiểm TNDS Bắt Buộc Ô Tô', ['tnds', 'bắt buộc', 'bat buoc', 'trách nhiệm dân sự', 'dân sự', 'đăng kiểm', 'mức phạt', 'nghị định']),
        ('Bảo Hiểm Thân Vỏ & Vật Chất Xe Ô Tô', ['thân vỏ', 'than vo', 'vật chất', 'vat chat', 'thủy kích', 'ngập nước', 'mất cắp', 'tai nạn', 'xước', 'sơn']),
        ('Báo Giá & Mua Bảo Hiểm Ô Tô Online', ['báo giá', 'giá', 'biểu phí', 'bao nhiêu tiền', 'mua online', 'bảo việt', 'pvi', 'pti', 'mic', 'bảo minh', 'liberty']),
        ('Quy Trình Giám Định & Bồi Thường Ô Tô', ['bồi thường', 'giám định', 'gara', 'sửa chữa', 'hồ sơ', 'thủ tục', 'miễn thường', 'bảo hiểm ô tô', 'bảo hiểm xe ô tô', 'bảo hiểm oto']),
    ],
    'bhyt': [
        ('Quyền Lợi & Mức Hưởng Khám BHYT', ['quyền lợi', 'mức hưởng', 'khám chữa bệnh', 'bệnh viện', 'trái tuyến', 'đúng tuyến', '100%', '80%', 'chi trả', 'thuốc']),
        ('Đóng Tiếp & Gia Hạn BHYT Hộ Gia Đình', ['hộ gia đình', 'đóng', 'gia hạn', 'tái tục', 'online', 'mua mới', 'mua ở đâu', 'bao nhiêu tiền', 'giá', 'dịch vụ công']),
        ('Tra Cứu Thẻ & Mã Số BHYT Điện Tử', ['tra cứu', 'kiểm tra', 'check', 'mã số', 'số thẻ', 'hạn sử dụng', 'giá trị', 'điện tử', 'vssid', 'vneid']),
        ('Thủ Tục Cấp Lại & Đổi Thẻ BHYT', ['cấp lại', 'đổi thẻ', 'mất thẻ', 'sai thông tin', 'thủ tục', 'hồ sơ', 'bảo hiểm y tế', 'bhyt']),
    ],
    'bhxh': [
        ('Rút BHXH 1 Lần & Điều Kiện Chi Trả', ['1 lần', 'một lần', 'rút', 'lãnh', 'cách tính', 'hồ sơ', 'điều kiện', 'thủ tục', 'bao lâu']),
        ('Chế Độ Thai Sản, Ốm Đau & Hưu Trí', ['thai sản', 'ốm đau', 'hưu trí', 'lương hưu', 'nghỉ việc', 'dưỡng sức', 'chế độ', 'tuổi nghỉ hưu', 'thất nghiệp']),
        ('Tra Cứu Sổ BHXH & Quá Trình Đóng', ['tra cứu', 'sổ bhxh', 'quá trình đóng', 'kiểm tra', 'mã số', 'vssid', 'cổng dịch vụ công', 'dvc']),
        ('Đóng BHXH Tự Nguyện & Doanh Nghiệp', ['tự nguyện', 'bắt buộc', 'mức đóng', 'phương thức đóng', 'doanh nghiệp', 'nộp tiền', 'bảo hiểm xã hội', 'bhxh']),
    ],

    # === VEHICLE (3) ===
    'phat-nguoi': [
        ('Tra Cứu Phạt Nguội Toàn Quốc & Cục CSGT', ['tra cứu', 'kiểm tra', 'check', 'cục csgt', 'cảnh sát giao thông', 'toàn quốc', 'app', 'website', 'chính xác', 'hôm nay']),
        ('Phạt Nguội Xe Ô Tô & Thủ Tục Đăng Kiểm', ['ô tô', 'oto', 'xe ô tô', 'đăng kiểm', 'từ chối đăng kiểm', 'cảnh báo đăng kiểm']),
        ('Phạt Nguội Xe Máy & Lỗi Vi Phạm', ['xe máy', 'xe may', 'mô tô', 'lỗi vi phạm', 'tốc độ', 'vượt đèn đỏ', 'sai làn', 'nguội xe máy']),
        ('Nộp Phạt Nguội Online & Quy Trình Xử Lý', ['nộp phạt', 'nop phat', 'đóng phạt', 'dịch vụ công', 'kho bạc', 'thời hạn', 'quy trình', 'xử lý', 'ở đâu', 'phạt nguội']),
    ],
    'bien-so': [
        ('Tra Cứu Biển Số Xe 63 Tỉnh Thành', ['tỉnh', 'tỉnh nào', 'tỉnh thành', 'toàn quốc', 'tra cứu', 'bảng tra', 'danh sách', 'ký hiệu', 'mã vùng']),
        ('Đấu Giá Biển Số Xe Đẹp & Định Danh', ['đấu giá', 'dau gia', 'định danh', 'dinh danh', 'biển số định danh', 'quy chế', 'tiền đặt trước']),
        ('Ý Nghĩa Biển Số Đẹp & Phong Thủy', ['phong thủy', 'ý nghĩa', 'ngũ quý', 'tứ quý', 'thần tài', 'lộc phát', 'số đẹp', 'hợp mệnh', 'dịch biển']),
        ('Thủ Tục Cấp, Đổi Biển & Sang Tên Xe', ['sang tên', 'đổi biển', 'cấp lại', 'thủ tục', 'hồ sơ', 'thu hồi', 'đăng ký xe', 'làm biển', 'biển số']),
    ],
    'bien-so-xe': [
        ('Tra Cứu Biển Số Xe 63 Tỉnh Thành', ['tỉnh', 'tỉnh nào', 'tỉnh thành', 'toàn quốc', 'tra cứu', 'bảng tra', 'danh sách', 'ký hiệu', 'mã vùng']),
        ('Đấu Giá Biển Số Xe Đẹp & Định Danh', ['đấu giá', 'dau gia', 'định danh', 'dinh danh', 'biển số định danh', 'quy chế', 'tiền đặt trước']),
        ('Ý Nghĩa Biển Số Đẹp & Phong Thủy', ['phong thủy', 'ý nghĩa', 'ngũ quý', 'tứ quý', 'thần tài', 'lộc phát', 'số đẹp', 'hợp mệnh', 'dịch biển']),
        ('Thủ Tục Cấp, Đổi Biển & Sang Tên Xe', ['sang tên', 'đổi biển', 'cấp lại', 'thủ tục', 'hồ sơ', 'thu hồi', 'đăng ký xe', 'làm biển', 'biển số']),
    ],
    'bien-so-dep': [
        ('Đấu Giá Biển Số Xe Đẹp Trực Tuyến', ['đấu giá', 'dau gia', 'trực tuyến', 'biển số đẹp', 'vpa', 'tiền cọc']),
        ('Biển Số Ngũ Quý, Tứ Quý & Thần Tài', ['ngũ quý', 'tứ quý', 'thần tài', 'lộc phát', 'tam hoa', 'sảnh tiến', 'phát lộc']),
        ('Định Danh Biển Số Đẹp Theo Luật', ['định danh', 'dinh danh', 'thu hồi', 'sang tên', 'chuyển nhượng', 'quy định']),
        ('Ý Nghĩa Phong Thủy Biển Số Xe', ['phong thủy', 'ý nghĩa', 'dịch biển', 'hợp tuổi', 'hợp mệnh', 'biển số']),
    ],

    # === TELCO (2) ===
    'data-4g': [
        ('Gói Cước Data Viettel', ['viettel', 'viettel 4g', 'viettel 5g', 'viettel 3g', 'gói viettel', 'st90', 'v90', 'sd135', 'đăng ký viettel', 'nạp 3g viettel']),
        ('Gói Cước Data MobiFone', ['mobi', 'mobifone', 'mobi 4g', 'mobi 5g', 'mobi 3g', 'gói mobi', 'c90', 'kc90', 'đăng ký mobi', 'đăng ky 3g mobi', 'nạp data mobifone']),
        ('Gói Cước Data VinaPhone', ['vina', 'vinaphone', 'vina 4g', 'vina 5g', 'vina 3g', 'gói vina', 'vd149', 'd89y', 'đăng ký vina', 'nạp data vinaphone']),
        ('Nạp Data & Cú Pháp Đăng Ký', ['nạp data', 'nap data', 'cách nạp', 'cú pháp', 'hủy gói', 'kiểm tra dung lượng', 'gia hạn', 'mua thêm', 'gói cước']),
    ],
    'nap-tien-dien-thoai': [
        ('Nạp Tiền Viettel & Thẻ Cào Viettel', ['viettel', 'thẻ viettel', 'cào viettel', 'nạp thẻ viettel', 'cạc viettel', 'card viettel']),
        ('Nạp Tiền MobiFone & Thẻ Mobi', ['mobi', 'mobifone', 'thẻ mobi', 'nạp thẻ mobi', 'cào mobi', 'card mobi']),
        ('Nạp Tiền VinaPhone & Thẻ Vina', ['vina', 'vinaphone', 'thẻ vina', 'nạp thẻ vina', 'cào vina', 'card vina']),
        ('Cú Pháp Nạp Tiền & Khuyến Mãi', ['cú pháp', 'cách nạp', 'hướng dẫn', 'nạp cho người khác', 'bắn tiền', 'chuyển tiền điện thoại', 'chiết khấu', 'khuyến mãi', '20%', '50%', 'ngày vàng', 'hoàn tiền']),
    ],

    # === LOTTERY (3) ===
    'vietlott': [
        ('Xổ Số Power 6/55 & Mega 6/45', ['power 6 55', 'power 6/55', 'power 655', 'power655', 'xspower', 'power', 'mega 6 45', 'mega 6/45', 'mega 645', 'mega645', 'xổ số mega', 'mega']),
        ('Quay Số Keno & Bingo 18', ['keno', 'quay số nhanh', 'bingo', 'bingo18', 'bingo 18', 'max 3d', 'max3d', 'max 4d']),
        ('Mua Vé Vietlott Online & Điểm Bán', ['mua vé', 'mua ve', 'đại lý', 'dai ly', 'điểm bán', 'sms', 'app', 'online', 'momo']),
        ('Cơ Cấu Giải Thưởng & Dò Vé Vietlott', ['cơ cấu', 'co cau', 'giải thưởng', 'giai thuong', 'trúng thưởng', 'dò vé', 'do ve', 'kết quả']),
    ],
    'xo-so': [
        ('Xổ Số Kiến Thiết Miền Bắc (XSMB)', ['miền bắc', 'mien bac', 'xsmb', 'sxmb', 'kqsxmb', 'bắc']),
        ('Xổ Số Kiến Thiết Miền Nam (XSMN)', ['miền nam', 'mien nam', 'xsmn', 'sxmn', 'kqsxmn', 'nam']),
        ('Xổ Số Kiến Thiết Miền Trung (XSMT)', ['miền trung', 'mien trung', 'xsmt', 'sxmt', 'kqsxmt', 'trung']),
        ('Thống Kê, Soi Cầu & Quay Thử XS', ['thống kê', 'thong ke', 'soi cầu', 'soi cau', 'lô gan', 'tần suất', 'bạch thủ', 'quay thử', 'trực tiếp', 'live', 'sxtt', 'cơ cấu', 'đổi thưởng', 'kết quả']),
    ],
    've-so': [
        ('Dò Kết Quả Vé Số Kiến Thiết', ['dò', 'tra cứu', 'kiểm tra', 'hôm nay', 'kết quả', 'trúng số']),
        ('Đại Lý Vé Số & Điểm Đổi Thưởng', ['đại lý', 'đổi vé', 'hoa hồng', 'vé dạo', 'điểm đổi', 'lãnh thưởng']),
        ('Cơ Cấu Giải Thưởng & Quy Định Vé Số', ['cơ cấu', 'giải đặc biệt', 'giải phụ', 'vé số cào', 'thời hạn', 'quy định', 'thuế trúng thưởng', 'vé số']),
        ('Mua Vé Số Online & Ứng Dụng Tiện Ích', ['mua', 'online', 'app', 'tiện ích', 'đặt mua', 'trực tuyến']),
    ],
}

SECTOR_SPECIFIC_RULES['Entertainment'] = [
    ('Nạp thẻ & Nạp game', ['nạp', 'nap', 'thẻ', 'the', 'chiết khấu', 'chiet khau', 'garena', 'zing', 'vcoin', 'xu', 'tiktok', 'mua thẻ']),
    ('Tựa game & Sự kiện', ['game', 'liên quân', 'free fire', 'pubg', 'tốc chiến', 'sự kiện', 'giftcode', 'code']),
    ('Tài khoản & Nhà phát hành', ['tài khoản', 'tai khoan', 'đăng ký', 'nhà phát hành', 'nph', 'vng', 'garena', 'vtc']),
]
SECTOR_SPECIFIC_RULES['hospital'] = [
    ('Đặt khám & Bác sĩ', ['đặt khám', 'dat kham', 'bác sĩ', 'bac si', 'bệnh viện', 'benh vien', 'phòng khám', 'chuyên khoa']),
    ('Chỉ số & Sức khỏe', ['bmi', 'calo', 'cân nặng', 'chiều cao', 'dinh dưỡng', 'sức khỏe']),
]
SECTOR_SPECIFIC_RULES['ota'] = [
    ('Đặt phòng & Resort', ['khách sạn', 'khach san', 'resort', 'homestay', 'đặt phòng', 'dat phong', 'villa']),
    ('Vé máy bay & Di chuyển', ['vé máy bay', 've may bay', 'chuyến bay', 'vé tàu', 'vé xe', 'xe khách', 'cáp treo']),
    ('Tour & Điểm đến', ['tour', 'du lịch', 'du lich', 'hành trình', 'lịch trình', 'visa', 'điểm đến']),
]
SECTOR_SPECIFIC_RULES['telco'] = [
    ('Gói cước & Data 4G/5G', ['data', '4g', '5g', '3g', 'gói cước', 'goi cuoc', 'nạp data', 'dung lượng']),
    ('SIM & Tài khoản', ['sim', 'sim số', 'chính chủ', 'esim', 'tài khoản điện thoại', 'nạp thẻ']),
]
SECTOR_SPECIFIC_RULES['student'] = [
    ('Tuyển sinh & Xét tuyển', ['tuyển sinh', 'xét tuyển', 'điểm chuẩn', 'thi tốt nghiệp', 'thi thpt', 'nguyện vọng', 'học bạ', 'tổ hợp môn']),
    ('Trường & Ngành học', ['trường', 'đại học', 'cao đẳng', 'trung cấp', 'học viện', 'ngành học', 'chuyên ngành', 'mã trường']),
    ('Học phí & Học bổng', ['học phí', 'học bổng', 'miễn giảm', 'lệ phí', 'tín chỉ']),
    ('Nhà trọ & Ký túc xá', ['nhà trọ', 'phòng trọ', 'ký túc xá', 'thuê trọ', 'tìm trọ', 'chỗ ở']),
    ('Sinh viên & Cổng thông tin', ['sinh viên', 'cổng thông tin', 'đăng nhập', 'tài khoản', 'email', 'thẻ sinh viên']),
    ('Việc làm & Kỹ năng', ['việc làm', 'part-time', 'bán thời gian', 'thực tập', 'tuyển dụng', 'kỹ năng']),
]

# Đầu ra dữ liệu
LOCAL_DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data")
LOCAL_OUTPUT_PATH = os.path.join(LOCAL_DATA_DIR, "inventory_clusters_summary.json")
LOCAL_MD_PATH = os.path.join(BASE_DIR, "07_REPORTS", "KEYWORD_INVENTORY_MASTER.md")

HUBS_DASHBOARD_DATA = os.path.join(HUBS_REPO, "lib", "dashboard", "seo-inventory-clusters.json")
HUBS_PUBLIC_DATA = os.path.join(HUBS_REPO, "data", "seo-clusters-summary.json")

# clean_val / normalize_text / calculate_opportunity_score / classify_quadrant
# da duoc chuan hoa ve scripts/lib/keyword_intelligence.py (SSOT) - import o dau file.

# ---------------------------------------------------------------------------
# PILLAR SELECTION - Chọn từ khóa Pillar ĐẠI DIỆN CHO USE CASE
# Nguyên tắc: Pillar phải là chính Use Case (Theme), không phải sub-query có volume
# lớn nhất (các truy vấn điều hướng/tra cứu như "tổng đài mobiphone" không đại diện
# cho Theme). Cơ chế: neo ngữ nghĩa với Slug + Tên Theme, ưu tiên head-term ngắn,
# ưu tiên Intent thương mại/giao dịch, phạt Intent điều hướng và lỗi chính tả.
# ---------------------------------------------------------------------------
GENERIC_PILLAR_TOKENS = {
    'goi', 'cach', 'cua', 'va', 'cho', 'cac', 'nhat', 'moi', 'cai', 'co', 'khong',
    'la', 'gi', 'nhu', 'nao', 'hay', 'nen', 'khi', 'den', 'lam', 'sao', 'xem',
    'chi', 'tiet', 'thong', 'tong', 'hop', 'danh', 'sach', 'huong', 'dan',
}

PILLAR_INTENT_WEIGHT = {
    'Transactional': 1.0,
    'Commercial': 1.0,
    'Tool/Calculator': 1.0,
    'Informational': 0.9,
    'Navigational': 0.25,
}


def _raw_tokens(text):
    """Tách token giữ nguyên dấu tiếng Việt (chuẩn hóa NFC trước để tránh lỗi combining marks)."""
    text = unicodedata.normalize('NFC', (text or '').lower())
    out = []
    for w in text.split():
        w = w.strip('.,;:!?()[]{}"\'/\\-\u2013\u2014“”‘’…&+*')
        if w:
            out.append(w)
    return out


def _strip_diacritics(text):
    t = unicodedata.normalize('NFD', text)
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return unicodedata.normalize('NFC', t).replace('đ', 'd')


def _pillar_tokens(text):
    """Token đã bỏ dấu, dùng để so khớp ngữ nghĩa accent-insensitive."""
    return set(_strip_diacritics(w) for w in _raw_tokens(text) if _strip_diacritics(w))


def _slug_tokens(slug):
    """Token hóa slug (phân tách theo gạch ngang/gạch dưới) - tránh sinh token rác kiểu 'gia-ve-xem-phim'."""
    return set(_strip_diacritics(t) for t in re.split(r'[-_\s]+', (slug or '').lower()) if t.strip())


_ALL_THEME_TOKENS = None


def _get_all_theme_tokens():
    """
    Token set của toàn bộ Theme trong kho Inventory (Slug + Tên hiển thị).
    Dùng để phát hiện ứng viên Pillar đang "mượn" ngữ nghĩa của Theme khác
    (VD: "vay nhanh" trùng token với Theme "Vay Tiền Nhanh" nên không được làm
    Pillar cho Theme "Vay Tín Chấp").
    """
    global _ALL_THEME_TOKENS
    if _ALL_THEME_TOKENS is not None:
        return _ALL_THEME_TOKENS
    result = {}
    if os.path.isdir(INVENTORY_DIR):
        for sector in os.listdir(INVENTORY_DIR):
            sdir = os.path.join(INVENTORY_DIR, sector)
            if not os.path.isdir(sdir):
                continue
            for f in glob.glob(os.path.join(sdir, '*.csv')):
                slug = os.path.splitext(os.path.basename(f))[0]
                name = VIETNAMESE_THEME_NAMES.get(slug, slug.replace('-', ' '))
                result[slug] = (_slug_tokens(slug) | _pillar_tokens(name)) - GENERIC_PILLAR_TOKENS
    _ALL_THEME_TOKENS = result
    return result


def _cross_theme_penalty(kw_tokens, own_slug, own_tokens):
    """Phạt ứng viên khớp trọn token với Theme khác nhưng không khớp trọn Theme hiện tại."""
    if not kw_tokens or kw_tokens <= own_tokens:
        return 1.0
    for slug, toks in _get_all_theme_tokens().items():
        if slug == own_slug or not toks:
            continue
        if MERGE_MAP.get(slug, slug) == own_slug:
            continue
        if kw_tokens <= toks:
            return 0.55
    return 1.0


_THEME_TOKEN_IDF = None


def _get_theme_token_idf():
    """
    Trọng số IDF cho từng token của Theme, tính trên toàn bộ kho Inventory.
    - Token từ Slug ('s', token): so khớp accent-insensitive (slug viết không dấu).
    - Token từ Tên hiển thị ('n', token): so khớp giữ nguyên dấu, tránh bắt nhầm
      từ khác nghĩa khi bỏ dấu (VD: "Cẩm Nang" -> 'nang' không được khớp "thung nắng").
    Token xuất hiện ở nhiều Theme (vay, ngân, hàng...) bị giảm trọng số để tránh
    việc Theme này mượn Pillar của Theme khác.
    """
    global _THEME_TOKEN_IDF
    if _THEME_TOKEN_IDF is not None:
        return _THEME_TOKEN_IDF
    df = Counter()
    if os.path.isdir(INVENTORY_DIR):
        for sector in os.listdir(INVENTORY_DIR):
            sdir = os.path.join(INVENTORY_DIR, sector)
            if not os.path.isdir(sdir):
                continue
            for f in glob.glob(os.path.join(sdir, '*.csv')):
                slug = os.path.splitext(os.path.basename(f))[0]
                for t in _slug_tokens(slug):
                    df[('s', t)] += 1
                name = VIETNAMESE_THEME_NAMES.get(slug)
                if name:
                    for t in set(_raw_tokens(name)):
                        df[('n', t)] += 1
    _THEME_TOKEN_IDF = {k: 1.0 / math.sqrt(c) for k, c in df.items()}
    return _THEME_TOKEN_IDF


def _theme_token_entries(usecase_slug, usecase_name):
    """Tập token neo của Theme, kèm nguồn gốc ('s' = Slug, 'n' = Tên hiển thị)."""
    entries = set()
    for t in _slug_tokens(usecase_slug):
        if t and t not in GENERIC_PILLAR_TOKENS:
            entries.add(('s', t))
    for t in set(_raw_tokens(usecase_name)):
        if _strip_diacritics(t) not in GENERIC_PILLAR_TOKENS:
            entries.add(('n', t))
    return entries


def _kw_token_index(keyword):
    """(token giữ dấu, token bỏ dấu) của từ khóa để so khớp với token neo."""
    full = set(_raw_tokens(keyword))
    return full, {_strip_diacritics(w) for w in full}


def _entry_match(entry, kw_full, kw_stripped):
    kind, tok = entry
    return tok in (kw_stripped if kind == 's' else kw_full)


def _build_spelling_dominance(raw_keywords):
    """
    Bảng thống kê biến thể chính tả theo tần suất xuất hiện (số từ khóa khác nhau
    dùng biến thể đó). Biến thể chuẩn (đúng dấu) thường xuất hiện trong nhiều từ khóa
    hơn biến thể lỗi gõ, dù volume từng biến thể có thể cao hơn.
    """
    dominance = defaultdict(Counter)
    for item in raw_keywords:
        for w in _raw_tokens(item['keyword']):
            dominance[_strip_diacritics(w)][w] += 1
    return dominance


def _spelling_quality(keyword, dominance):
    """Hệ số chất lượng chính tả trong [0,1] - càng gần 1 càng đúng chính tả."""
    if not dominance:
        return 1.0
    ws = _raw_tokens(keyword)
    if not ws:
        return 1.0
    total = 0.0
    for w in ws:
        variants = dominance.get(_strip_diacritics(w))
        if not variants:
            continue
        total += variants.get(w, 0) / max(1, sum(variants.values()))
    return total / len(ws)


def select_pillar_keyword(canonical_clusters, usecase_slug, usecase_name, raw_keywords=None):
    """
    Chọn từ khóa Pillar đại diện cho Use Case.

    Cơ chế: xếp hạng toàn bộ cụm theo
        Volume (log) x [w_coverage x Độ phủ token Use Case + w_brevity x Độ ngắn gọn
                        + w_intent x Trọng số Intent] x Chất lượng chính tả
    trong đó:
    - Độ phủ token (đã bão hòa): tỷ lệ token của Slug + Tên Theme xuất hiện trong từ khóa.
      Đây là yếu tố neo vào chính Use Case, giúp các truy vấn điều hướng/tra cứu (không
      chứa token của Use Case) không chiếm vị trí Pillar. Hàm bão hòa giữ cho Volume vẫn
      là tín hiệu quyết định giữa các ứng viên cùng on-topic (VD: "agribank" 368k phải
      thắng "ngân hàng agribank" 63k).
    - Độ ngắn gọn: ưu tiên head-term thay vì long-tail.
    - Intent: ưu tiên Commercial/Transactional/Tool, phạt nặng Navigational.
    - Chất lượng chính tả: phạt biến thể lỗi gõ (tần suất xuất hiện thấp hơn biến thể chuẩn).
    Volume vẫn giữ vai trò quyết định để không đánh mất các từ khóa lớn hợp lệ.
    """
    if not canonical_clusters:
        return None

    theme_entries = _theme_token_entries(usecase_slug, usecase_name)
    theme_tokens = {_strip_diacritics(t) for _, t in theme_entries}
    dominance = _build_spelling_dominance(raw_keywords) if raw_keywords else {}
    idf = _get_theme_token_idf()

    # Điều kiện bắt buộc: Pillar phải chứa ít nhất 1 token ĐẶC TRƯNG của Theme
    # (token ít xuất hiện ở các Theme khác). Ngăn Theme mượn Pillar của Theme khác
    # hoặc các truy vấn ngoài Use Case (VD: "tổng đài mobiphone" cho theme data-4g).
    # Token từ Tên hiển thị so khớp giữ nguyên dấu để tránh bắt nhầm từ khác nghĩa
    # (VD: "Cẩm Nang" -> 'nang' không khớp "thung nắng").
    distinctive = {e for e in theme_entries if idf.get(e, 1.0) >= 0.35} or theme_entries
    eligible = []
    if distinctive:
        for c in canonical_clusters:
            kw_full, kw_stripped = _kw_token_index(c['keyword'])
            if any(_entry_match(e, kw_full, kw_stripped) for e in distinctive):
                eligible.append(c)
    if not eligible:
        eligible = list(canonical_clusters)

    best_item, best_score = None, -1.0

    for c in eligible:
        kw_full, kw_stripped = _kw_token_index(c['keyword'])
        if theme_entries:
            total_w = sum(idf.get(e, 1.0) for e in theme_entries)
            overlap_w = sum(idf.get(e, 1.0) for e in theme_entries if _entry_match(e, kw_full, kw_stripped))
            raw_coverage = overlap_w / total_w if total_w else 0.0
        else:
            raw_coverage = 0.0
        # Bão hòa coverage: 2x/(1+2x) - neo mạnh nhưng không lấn át hoàn toàn Volume
        coverage = 2 * raw_coverage / (1 + 2 * raw_coverage) if raw_coverage else 0.0

        n = max(1, len(kw_full))
        brevity = 1.0 if n <= 3 else 0.85 if n == 4 else 0.7 if n == 5 else 0.55
        intent_w = PILLAR_INTENT_WEIGHT.get(c['intent'], 0.8)
        spelling = 0.85 + 0.3 * _spelling_quality(c['keyword'], dominance)
        volume_signal = math.log10(c['total_cluster_volume'] + 10)
        cross_penalty = _cross_theme_penalty(kw_stripped, usecase_slug, theme_tokens)

        score = volume_signal * (0.45 * coverage + 0.25 * brevity + 0.35 * intent_w) * spelling * cross_penalty

        if score > best_score:
            best_score, best_item = score, c

    return best_item


def build_adaptive_clusters(canonical_clusters, sector=None, usecase_slug=None, usecase_name=None, top_n_clusters=5):
    """Gom cụm thích ứng 3 tầng (Adaptive Clustering v2): Intent -> Entity -> Residual.

    Tự động bóc tách thực thể thương hiệu, triệt tiêu lỗi đổ rác vào rules[-1].
    """
    rules = USECASE_SPECIFIC_RULES.get(usecase_slug) or SECTOR_SPECIFIC_RULES.get(sector, [])
    from scripts.lib.adaptive_clustering import build_adaptive_clusters_v2
    return build_adaptive_clusters_v2(
        canonical_clusters,
        sector=sector,
        usecase_slug=usecase_slug,
        usecase_name=usecase_name,
        rules=rules,
        top_n_clusters=top_n_clusters
    )

def process_csv_paths(csv_paths, sector, canonical_slug):
    usecase_slug = canonical_slug
    usecase_name = VIETNAMESE_THEME_NAMES.get(usecase_slug, usecase_slug.replace('-', ' ').replace('_', ' ').title())
    
    raw_keywords_map = {}
    outliers_filtered = 0
    total_raw_rows = 0

    for csv_path in csv_paths:
        with open(csv_path, 'r', encoding='utf-8-sig', errors='replace') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_raw_rows += 1
                kw_raw = row.get('Keyword', '')
                if not kw_raw:
                    continue
                kw = normalize_text(clean_val(kw_raw))
                if kw in raw_keywords_map:
                    continue

                # 1. Dynamic Domain Outlier Filtering
                is_out, _ = SemanticDomainFilter.is_outlier(kw, sector, usecase_slug)
                if is_out:
                    outliers_filtered += 1
                    continue

                try:
                    vol = int(clean_val(row.get('Volume', '0')) or 0)
                except ValueError:
                    vol = 0
                try:
                    cpc = float(clean_val(row.get('CPC', '0')) or 0.0)
                except ValueError:
                    cpc = 0.0
                comp = clean_val(row.get('PPC Competition', 'Low'))
                trending = clean_val(row.get('Trending', 'false')).lower() == 'true'
                kd = calculate_kd(comp, vol, cpc)

                # 2. Multi-Signal Weighted Intent Classifier
                intent_res = MultiSignalIntentClassifier.classify(kw)
                intent = intent_res['intent']
                opp_score = calculate_opportunity_score(vol, cpc, comp, intent)
                quadrant = classify_quadrant(vol, comp, intent)

                raw_keywords_map[kw] = {
                    'keyword': kw,
                    'volume': vol,
                    'cpc': cpc,
                    'competition': comp,
                    'kd': kd,
                    'trending': trending,
                    'intent': intent,
                    'intent_confidence': intent_res['confidence'],
                    'opportunity_score': opp_score,
                    'quadrant': quadrant
                }

    raw_keywords = list(raw_keywords_map.values())
    if not raw_keywords:
        return None

    # 3. SERP Intent Fingerprinting & Cannibalization Shield
    canonical_clusters, merge_log = SERPCannibalizationShield.cluster_and_shield(raw_keywords)

    total_volume = sum(k['volume'] for k in raw_keywords)

    intent_counts = Counter(k['intent'] for k in canonical_clusters)
    quadrant_counts = Counter(k['quadrant'] for k in canonical_clusters)

    top_opportunities = sorted(canonical_clusters, key=lambda x: (x['opportunity_score'], x['volume']), reverse=True)[:10]
    # Pillar = từ khóa đại diện chính Use Case (không phải sub-query volume lớn nhất)
    pillar_item = select_pillar_keyword(canonical_clusters, usecase_slug, usecase_name, raw_keywords)

    sub_clusters = build_adaptive_clusters(canonical_clusters, sector=sector, usecase_slug=usecase_slug, usecase_name=usecase_name)

    # 4. Domain SERP Cannibalization Shield
    shield_eval = MoMoDomainSERPShield.evaluate_cannibalization_risk(pillar_item['keyword'], sector=sector, check_live_serp=False)
    if not shield_eval.get('top_live_url'):
        for opp in top_opportunities:
            sub_eval = MoMoDomainSERPShield.evaluate_cannibalization_risk(opp['keyword'], sector=sector, check_live_serp=False)
            if sub_eval.get('top_live_url'):
                shield_eval['top_live_url'] = sub_eval['top_live_url']
                shield_eval['risk_level'] = sub_eval['risk_level']
                shield_eval['verdict'] = sub_eval['verdict']
                shield_eval['action'] = sub_eval['action']
                shield_eval['rationale'] = f"Kế thừa live URL từ truy vấn nhánh: {opp['keyword']}"
                break

    cannibalization_shield = {
        'risk_level': shield_eval['risk_level'],
        'verdict': shield_eval['verdict'],
        'action': shield_eval['action'],
        'serp_rank': shield_eval.get('serp_rank'),
        'top_live_url': shield_eval.get('top_live_url'),
        'rationale': shield_eval['rationale']
    }

    return {
        'id': usecase_slug,
        'name': usecase_name,
        'display_name': usecase_name,
        'sector': sector,
        'file_name': ", ".join([os.path.basename(p) for p in csv_paths]),
        'total_raw_keywords': total_raw_rows,
        'clean_keywords_count': len(raw_keywords),
        'outliers_filtered_count': outliers_filtered,
        'canonical_topics_count': len(canonical_clusters),
        'cannibalization_merged_count': len(merge_log),
        'total_volume': total_volume,
        'cannibalization_shield': cannibalization_shield,
        'pillar_keyword': {
            'keyword': pillar_item['keyword'],
            'volume': pillar_item['volume'],
            'cluster_volume': pillar_item['total_cluster_volume'],
            'intent': pillar_item['intent'],
            'secondary_synonyms': pillar_item.get('secondary_keywords', [])[:5]
        },
        'intent_breakdown': dict(intent_counts),
        'quadrant_breakdown': dict(quadrant_counts),
        'top_opportunities': [
            {
                'keyword': k['keyword'],
                'volume': k['volume'],
                'cluster_volume': k['total_cluster_volume'],
                'cpc': k.get('cpc', 0.0),
                'competition': k.get('competition', 'Low'),
                'kd': k.get('kd', calculate_kd(k.get('competition', 'Low'), k['volume'], k.get('cpc', 0.0))),
                'trending': k.get('trending', False),
                'intent': k['intent'],
                'score': k['opportunity_score'],
                'quadrant': k['quadrant'],
                'secondary_synonyms': k.get('secondary_keywords', [])[:3]
            } for k in top_opportunities
        ],
        'keywords': [
            {
                'keyword': k['keyword'],
                'volume': k['volume'],
                'cluster_volume': k['total_cluster_volume'],
                'cpc': k.get('cpc', 0.0),
                'competition': k.get('competition', 'Low'),
                'kd': k.get('kd', calculate_kd(k.get('competition', 'Low'), k['volume'], k.get('cpc', 0.0))),
                'trending': k.get('trending', False),
                'intent': k['intent'],
                'score': k['opportunity_score'],
                'quadrant': k.get('quadrant', 'Supporting'),
                'secondary_synonyms': k.get('secondary_keywords', [])[:3]
            } for k in sorted(canonical_clusters, key=lambda x: (x['opportunity_score'], x['volume']), reverse=True)[:150]
        ],
        'sub_clusters': sub_clusters
    }

def main():
    target_sector = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ['--hub', '--sector'] and i + 1 < len(args):
            target_sector = args[i+1].strip()
            i += 2
        elif arg.startswith('--hub='):
            target_sector = arg.split('=', 1)[1].strip()
            i += 1
        elif arg.startswith('--sector='):
            target_sector = arg.split('=', 1)[1].strip()
            i += 1
        elif not arg.startswith('-'):
            target_sector = arg.strip()
            i += 1
        else:
            i += 1

    print(f"Bắt đầu quét và đồng bộ kho Inventory từ: {INVENTORY_DIR}")
    if not os.path.exists(INVENTORY_DIR):
        print(f"Lỗi: Không tìm thấy thư mục {INVENTORY_DIR}")
        sys.exit(1)
        
    all_sectors = sorted([d for d in os.listdir(INVENTORY_DIR) if os.path.isdir(os.path.join(INVENTORY_DIR, d)) and not d.startswith('.')])
    
    if target_sector:
        matched = [s for s in all_sectors if s.lower() == target_sector.lower()]
        if not matched:
            print(f"Lỗi: Không tìm thấy Hub/Sector '{target_sector}'. Các Hub hiện có: {', '.join(all_sectors)}")
            sys.exit(1)
        sectors = matched
        print(f"-> Chế độ chạy mục tiêu Hub: {matched[0]}")
    else:
        sectors = all_sectors
    
    all_usecases = []
    sector_summary = {}
    total_kws_all = 0
    total_vol_all = 0
    total_cannibalized_all = 0
    total_outliers_all = 0
    
    for s in sectors:
        s_dir = os.path.join(INVENTORY_DIR, s)
        csv_files = sorted(glob.glob(os.path.join(s_dir, '*.csv')))

        slug_groups = defaultdict(list)
        for fpath in csv_files:
            raw_slug = os.path.splitext(os.path.basename(fpath))[0]
            # Tự động loại bỏ hậu tố nhân bản như (1), (2), _copy...
            clean_slug = re.sub(r'[\s_]*\(\d+\)$', '', raw_slug).strip()
            canonical_slug = MERGE_MAP.get(clean_slug, MERGE_MAP.get(clean_slug.lower(), clean_slug))
            slug_groups[canonical_slug].append(fpath)

        s_usecases = []
        s_kws = 0
        s_vol = 0
        s_cannibalized = 0
        s_outliers = 0
        
        for canonical_slug, paths in slug_groups.items():
            # Ưu tiên tệp có thời gian sửa đổi (mtime) mới nhất
            paths.sort(key=lambda p: os.path.getmtime(p), reverse=True)
            res = process_csv_paths(paths, s, canonical_slug)
            if res:
                s_usecases.append(res)
                all_usecases.append(res)
                s_kws += res['clean_keywords_count']
                s_vol += res['total_volume']
                s_cannibalized += res['cannibalization_merged_count']
                s_outliers += res['outliers_filtered_count']
                
        sector_summary[s] = {
            'usecase_count': len(s_usecases),
            'total_keywords': s_kws,
            'total_volume': s_vol,
            'cannibalized_merged': s_cannibalized,
            'outliers_filtered': s_outliers
        }
        total_kws_all += s_kws
        total_vol_all += s_vol
        total_cannibalized_all += s_cannibalized
        total_outliers_all += s_outliers
        print(f"- Hub {s:15s}: {len(s_usecases):3d} themes | {s_kws:7,d} kws | {s_cannibalized:5,d} cannibalized merged | {s_vol:12,d} vol")

    if target_sector and os.path.exists(LOCAL_OUTPUT_PATH):
        try:
            with open(LOCAL_OUTPUT_PATH, 'r', encoding='utf-8') as f:
                cached_data = json.load(f)
            cached_usecases = [uc for uc in cached_data.get('usecases', []) if uc.get('sector', '').lower() != target_sector.lower()]
            cached_summary = cached_data.get('sector_summary', {})
            cached_summary.update(sector_summary)
            sector_summary = cached_summary
            all_usecases = cached_usecases + all_usecases
            total_kws_all = sum(s['total_keywords'] for s in sector_summary.values())
            total_vol_all = sum(s['total_volume'] for s in sector_summary.values())
            total_cannibalized_all = sum(s['cannibalized_merged'] for s in sector_summary.values())
            total_outliers_all = sum(s['outliers_filtered'] for s in sector_summary.values())
            sectors = sorted(list(sector_summary.keys()))
        except Exception as e:
            print(f"Cảnh báo khi nạp snapshot cũ: {e}")
        
    print(f"\nTổng kết: {len(all_usecases)} themes | {total_kws_all:,} từ khóa sạch | {total_cannibalized_all:,} từ khóa được gom chống ăn thịt | {total_outliers_all:,} từ khóa nhiễu bị chặn.")
    
    # 0. Làm giàu dữ liệu: Tính toán Mạng lưới Liên kết nội bộ (Silo Topology), GEO Direct Answers & Mùa vụ SSOT
    print("Đang tính toán mạng lưới liên kết nội bộ (Internal Linking Topology), GEO Direct Answers & Mùa vụ SSOT...")
    
    # Nạp dữ liệu Mùa vụ SSOT (5-year Google Trends)
    seasonality_path = os.path.join(BASE_DIR, "07_REPORTS", "data", "theme_seasonality.json")
    seasonality_lookup = {}
    if os.path.exists(seasonality_path):
        try:
            with open(seasonality_path, 'r', encoding='utf-8') as sf:
                sdata = json.load(sf)
                for st in sdata.get('themes', []):
                    if 'theme_id' in st and 'monthly' in st:
                        seasonality_lookup[st['theme_id']] = st['monthly']
            print(f"Đã nạp {len(seasonality_lookup)} theme seasonality curves từ SSOT.")
        except Exception as se:
            print(f"Cảnh báo nạp seasonality: {se}")

    for uc in all_usecases:
        # A. Internal Linking Matrix
        silo = InternalLinkingTopologyEngine.build_silo_matrix(uc, all_usecases)
        uc['internal_links'] = silo
        
        # B. GEO Optimization Block
        p_kw = uc['pillar_keyword']['keyword']
        p_intent = uc['pillar_keyword']['intent']
        uc['geo_optimization'] = {
            'direct_answer_snippet': GEODirectAnswerGenerator.generate_direct_answer_snippet(uc['name'], p_kw, p_intent, uc['sector'], usecase_slug=uc['id']),
            'entity_facts': GEODirectAnswerGenerator.generate_entity_factsheet(uc['name'], uc['sector'], p_intent, usecase_slug=uc['id'])
        }
        
        # C. 5-Year Google Trends Seasonality Curve
        uc['seasonality'] = seasonality_lookup.get(uc['id'])

    # 1. Đóng gói Snapshot Master & SSOT Local
    data_payload = {
        'version': '3.1-enterprise',
        'generated_at': datetime.now().strftime('%Y-%m-%d'),
        'stats': {
            'total_usecases': len(all_usecases),
            'total_keywords': total_kws_all,
            'total_volume': total_vol_all,
            'total_cannibalized_shielded': total_cannibalized_all,
            'total_outliers_pruned': total_outliers_all,
            'total_sectors': len(sectors)
        },
        'sector_summary': sector_summary,
        'usecases': all_usecases
    }
    
    os.makedirs(LOCAL_DATA_DIR, exist_ok=True)
    with open(LOCAL_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data_payload, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu Snapshot SSOT tại: {LOCAL_OUTPUT_PATH}")
    
    # 2. Tổng hợp Danh mục Quick Wins Toàn Nền Tảng (Cross-Hub Quick Wins Portfolio)
    all_quick_wins = []
    for uc in all_usecases:
        for opp in uc['top_opportunities']:
            if opp['quadrant'] == 'Quick Win':
                all_quick_wins.append({
                    'keyword': opp['keyword'],
                    'volume': opp['volume'],
                    'cluster_volume': opp['cluster_volume'],
                    'intent': opp['intent'],
                    'score': opp['score'],
                    'usecase': uc['name'],
                    'usecase_id': uc['id'],
                    'sector': uc['sector'],
                    'synonyms': opp.get('secondary_synonyms', [])
                })
    all_quick_wins.sort(key=lambda x: (x['score'], x['volume']), reverse=True)
    
    # Xuất Báo cáo Quick Wins Markdown
    qw_md_path = os.path.join(BASE_DIR, "07_REPORTS", "QUICK_WINS_PORTFOLIO.md")
    qw_md = f"""# DANH MỤC TỪ KHÓA QUICK WINS TOÀN WEB PLATFORM (HIGH ROI OPPORTUNITIES)

Tập hợp các từ khóa có **Search Volume cao ($\\\\ge 1.500$) và Mức độ Cạnh tranh Thấp (Low PPC Competition)** trên toàn bộ {len(all_usecases)} Use Cases của Web Platform. Đây là các chủ đề ưu tiên hàng đầu mang lại lưu lượng truy cập nhanh nhất với chi phí nội dung tối thiểu.

- **Tổng số từ khóa Quick Wins phát hiện:** {len(all_quick_wins):,} từ khóa
- **Tổng dung lượng tìm kiếm Quick Wins:** {sum(x['volume'] for x in all_quick_wins):,} lượt/tháng

---

## TOP 50 TỪ KHÓA QUICK WINS ƯU TIÊN SẢN XUẤT HÀNG ĐẦU

| STT | Từ Khóa Quick Win | Search Volume | Search Intent | Điểm Cơ Hội | Use Case | Khối Ngành | Biến Thể Đồng Nghĩa Đã Gom Cụm |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
"""
    for idx, qw in enumerate(all_quick_wins[:50], 1):
        syn_str = ", ".join(qw['synonyms'][:2]) if qw['synonyms'] else "Độc lập"
        qw_md += f"| {idx} | `{qw['keyword']}` | {qw['volume']:,} | `{qw['intent']}` | {qw['score']} | {qw['usecase']} | {qw['sector']} | {syn_str} |\n"

    with open(qw_md_path, 'w', encoding='utf-8') as f:
        f.write(qw_md)
    print(f"Đã xuất bản Danh mục Quick Wins tại: {qw_md_path}")

    # 3. Tạo Báo cáo Master Markdown
    md_content = f"""# TỔNG QUAN TÀI NGUYÊN TỪ KHÓA & TOPIC CLUSTERS WEB PLATFORM (SSOT INVENTORY V2)

Dữ liệu được trích xuất, lọc nhiễu tự động và bảo vệ chống ăn thịt từ khóa (Cannibalization Shield) từ kho `05_HUBS/inventory/`.
- **Tổng số Themes:** {len(all_usecases)}
- **Tổng số từ khóa theo dõi:** {total_kws_all:,}
- **Tổng số từ khóa trùng Intent được gom cụm (Shielded):** {total_cannibalized_all:,}
- **Tổng số từ khóa nhiễu bị loại bỏ:** {total_outliers_all:,}
- **Tổng dung lượng tìm kiếm thị trường:** {total_vol_all:,} lượt/tháng

---

## 1. TỔNG HỢP THEO HUBS

| Hub | Số Lượng Themes | Từ Khóa Sạch | Từ Khóa Gom Chống Cannibalization | Dung Lượng Tìm Kiếm (Volume/Tháng) |
| :--- | :---: | :---: | :---: | :---: |
"""
    for sec, stats in sorted(sector_summary.items(), key=lambda x: x[1]['total_volume'], reverse=True):
        md_content += f"| {sec} | {stats['usecase_count']:,} | {stats['total_keywords']:,} | {stats['cannibalized_merged']:,} | {stats['total_volume']:,} |\n"

    md_content += """\n---\n\n## 2. TOP THEMES CÓ QUY MÔ LỚN NHẤT\n\n| STT | Theme | Hub | Số Từ Khóa | Gom Cannibalized | Search Volume | Từ Khóa Cột Trụ (Pillar KW) | Top Quick Win |\n| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- |\n"""

    top_usecases = sorted(all_usecases, key=lambda x: x['total_volume'], reverse=True)[:25]
    for idx, uc in enumerate(top_usecases, 1):
        pkw = uc['pillar_keyword']['keyword']
        pvol = uc['pillar_keyword']['cluster_volume']
        qwin = next((k['keyword'] for k in uc['top_opportunities'] if k['quadrant'] == 'Quick Win'), 'N/A')
        md_content += f"| {idx} | {uc['name']} | {uc['sector']} | {uc['clean_keywords_count']:,} | {uc['cannibalization_merged_count']:,} | {uc['total_volume']:,} | {pkw} ({pvol:,}) | {qwin} |\n"

    with open(LOCAL_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Đã cập nhật tài liệu báo cáo tại: {LOCAL_MD_PATH}")

    # 4. Xuất Modular Chunks & Đẩy trực tiếp sang hubs-momo
    if os.path.exists(HUBS_REPO):
        # A. Cập nhật Dashboard Payload siêu nhẹ
        os.makedirs(os.path.dirname(HUBS_DASHBOARD_DATA), exist_ok=True)
        dashboard_payload = {
            'stats': data_payload['stats'],
            'sector_summary': sector_summary,
            'top_usecases': sorted(all_usecases, key=lambda x: x['total_volume'], reverse=True)[:35],
            'recent_sync': data_payload['generated_at']
        }
        with open(HUBS_DASHBOARD_DATA, 'w', encoding='utf-8') as f:
            json.dump(dashboard_payload, f, ensure_ascii=False, indent=2)
        print(f"Đã push sang hubs-momo (Dashboard): {HUBS_DASHBOARD_DATA}")
        
        # B. Cập nhật File Tổng tương thích ngược
        os.makedirs(os.path.dirname(HUBS_PUBLIC_DATA), exist_ok=True)
        with open(HUBS_PUBLIC_DATA, 'w', encoding='utf-8') as f:
            json.dump(data_payload, f, ensure_ascii=False, indent=2)
        print(f"Đã push sang hubs-momo (Data layer master): {HUBS_PUBLIC_DATA}")

        # C. TRIỂN KHAI MODULAR CHUNKING: data/seo-clusters/index.json + chunks từng use case
        modular_dir = os.path.join(HUBS_REPO, "data", "seo-clusters")
        os.makedirs(modular_dir, exist_ok=True)

        # Index siêu nhẹ (~45 KB)
        sector_filter = target_sector.lower() if target_sector else None
        target_usecases = [
            uc for uc in all_usecases
            if not sector_filter or uc.get('sector', '').lower() == sector_filter
        ]
        current_sector_usecases = [
            {
                'id': uc['id'],
                'name': uc['name'],
                'display_name': uc.get('display_name', uc['name']),
                'sector': uc['sector'],
                'total_volume': uc['total_volume'],
                'clean_keywords_count': uc['clean_keywords_count'],
                'pillar_keyword': uc['pillar_keyword']['keyword'],
                'pillar_volume': uc['pillar_keyword']['cluster_volume'],
                'pillar_intent': uc['pillar_keyword']['intent'],
                'quick_wins_count': len([k for k in uc['top_opportunities'] if k['quadrant'] == 'Quick Win']),
                'chunk_url': f"/data/seo-clusters/{uc['sector']}/{uc['id']}.json"
            } for uc in target_usecases
        ]

        index_file = os.path.join(modular_dir, "index.json")
        final_usecases = current_sector_usecases
        final_sector_summary = sector_summary

        if target_sector and os.path.exists(index_file):
            try:
                with open(index_file, 'r', encoding='utf-8') as f:
                    old_index = json.load(f)
                other_usecases = [u for u in old_index.get('usecases', []) if u.get('sector', '').lower() != target_sector.lower()]
                final_usecases = other_usecases + current_sector_usecases
                final_sector_summary = old_index.get('sector_summary', {})
                final_sector_summary.update(sector_summary)
            except Exception as e:
                print(f"Không thể kế thừa index cũ: {e}")

        # Cơ chế phòng thủ kép: Dedupe tuyệt đối theo 'id' và sắp xếp theo total_volume giảm dần
        seen_ids = set()
        deduped_usecases = []
        for u in final_usecases:
            if u['id'] not in seen_ids:
                seen_ids.add(u['id'])
                deduped_usecases.append(u)
        final_usecases = sorted(deduped_usecases, key=lambda x: x['total_volume'], reverse=True)

        index_payload = {
            'version': '3.0-modular',
            'generated_at': data_payload['generated_at'],
            'stats': data_payload['stats'],
            'sector_summary': final_sector_summary,
            'quick_wins_count': len(all_quick_wins),
            'usecases': final_usecases
        }
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index_payload, f, ensure_ascii=False, indent=2)
        print(f"Đã tạo Modular Index siêu nhẹ tại: {index_file} ({round(os.path.getsize(index_file)/1024, 1)} KB)")

        # Xuất file Quick Wins độc lập
        qw_file = os.path.join(modular_dir, "quick-wins.json")
        with open(qw_file, 'w', encoding='utf-8') as f:
            json.dump({'quick_wins': all_quick_wins[:100]}, f, ensure_ascii=False, indent=2)
        print(f"Đã tạo Quick Wins JSON tại: {qw_file}")

        # Xuất từng Chunk Use Case độc lập
        chunks_to_write = [uc for uc in all_usecases if uc['sector'].lower() == target_sector.lower()] if target_sector else all_usecases
        chunk_count = 0
        for uc in chunks_to_write:
            sec_dir = os.path.join(modular_dir, uc['sector'])
            os.makedirs(sec_dir, exist_ok=True)
            uc_file = os.path.join(sec_dir, f"{uc['id']}.json")
            with open(uc_file, 'w', encoding='utf-8') as f:
                json.dump(uc, f, ensure_ascii=False, indent=2)
            chunk_count += 1
        
        # Xóa các chunk cũ đã bị merge trong các sector được xử lý
        clean_sectors = [target_sector] if target_sector else [s for s in sectors]
        for sec in clean_sectors:
            sec_dir = os.path.join(modular_dir, sec)
            if not os.path.exists(sec_dir):
                for actual_dir in glob.glob(os.path.join(modular_dir, '*')):
                    if os.path.basename(actual_dir).lower() == sec.lower():
                        sec_dir = actual_dir
                        break
            if os.path.exists(sec_dir):
                active_files = {f"{uc['id']}.json" for uc in all_usecases if uc['sector'].lower() == sec.lower()}
                for existing_f in glob.glob(os.path.join(sec_dir, '*.json')):
                    if os.path.basename(existing_f) not in active_files:
                        os.remove(existing_f)
                        print(f"Đã xóa chunk thừa: {existing_f}")

        # Tự động dọn dẹp các thư mục ngành mồ côi (không còn trong danh sách sectors) khi Full Sync
        if not target_sector:
            import shutil
            valid_sector_names = {s.lower() for s in sectors}
            for item in os.listdir(modular_dir):
                item_path = os.path.join(modular_dir, item)
                if os.path.isdir(item_path) and item.lower() not in valid_sector_names:
                    shutil.rmtree(item_path)
                    print(f"Đã tự động xóa thư mục ngành mồ côi không còn trong inventory: {item_path}")

        print(f"Đã bóc tách chi tiết và xuất bản thành công {chunk_count} Modular Chunks tại {modular_dir}/<sector>/<id>.json!")
    else:
        print(f"Cảnh báo: Không tìm thấy hubs-momo tại {HUBS_REPO}")

if __name__ == '__main__':
    main()

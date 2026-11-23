# -*- coding: utf-8 -*-
"""
CONTENT PLAN & SUB-CLUSTER CONFIGURATION (SSOT)
Chứa các quy tắc phân cụm ngữ nghĩa thực tế (Demand-driven Sub-clusters),
Bản đồ tính năng MoMo Web-to-App (CTA Hook cụ thể) và các hàm chuẩn hóa.
"""

import re
import unicodedata

THRESHOLD = 500

# Theme tổng (head term của cả Hub): nhường mọi từ khóa đã có trong CSV của theme con cùng Hub
# để tránh hai URL cạnh tranh cùng một từ khóa (pillar tổng vs pillar con).
# Theme thường cũng nhường từ khóa cho theme chuyên biệt hơn, xem generate_content_plan.keyword_owner.
UMBRELLA_THEMES = {'bao-hiem'}

# Theme mang tên thương hiệu/sản phẩm: từ khóa chứa tên thương hiệu (hoặc sản phẩm con) thuộc theme này,
# kể cả khi tên theme ngành chung có nhiều token khớp hơn. Vd 'xổ số vietlott', 'xổ số mega' thuộc /vietlott/,
# không thuộc /xo-so/. Khớp nguyên cụm từ trên dạng không dấu; chỉ áp dụng trong Hub có theme đó.
BRAND_THEMES = {
    'vietlott': ['vietlott', 'power 6 55', 'power 655', 'power', 'mega 6 45', 'mega 645', 'mega',
                 'keno', 'max 3d', 'max3d', 'max 4d', 'max4d', '3d max', 'xo so 3d', 've so 3d', 'bingo', 'bingo18', 'bingo 18'],
}

# Cụm đồng nghĩa (không dấu) quy về một dạng khi xác định biến thể của head term pillar.
# Ví dụ 'bảo hiểm xe ô tô', 'bảo hiểm xe hơi', 'bảo hiểm oto' đều là biến thể của 'bảo hiểm ô tô'.
HEAD_SYNONYM_PHRASES = [
    ('xe o to', 'o to'),
    ('xe oto', 'o to'),
    ('xe hoi', 'o to'),
    ('oto', 'o to'),
    ('bhxh', 'bao hiem xa hoi'),
    ('bhyt', 'bao hiem y te'),
    ('xo so vietlott', 'vietlott'),
    ('xs vietlott', 'vietlott'),
]

def remove_accents(input_str):
    # "đ/Đ" không tách được bằng NFKD nên phải thay tay, nếu không slug sẽ mất chữ (điểm -> iem)
    input_str = input_str.replace('đ', 'd').replace('Đ', 'D')
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

# Bản đồ ánh xạ tính năng MoMo thực tế kèm Deeplink & Event đo lường chuẩn Umami
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
    'data-4g': ('Nạp Gói Cước Data 4G/5G Tốc Độ Cao MoMo', 'momo://data-topup', 'web_data_topup_btn_click'),
    'nap-tien-dien-thoai': ('Nạp Tiền Điện Thoại Chiết Khấu Đến 5% MoMo', 'momo://topup', 'web_mobile_topup_btn_click'),
    'sim': ('Mua SIM Chính Chủ & Chọn Gói Cước Data', 'momo://sim-store', 'web_sim_store_btn_click'),

    # Hospital Hub
    'dat-lich-kham-benh': ('Đặt Lịch Khám Bệnh Tại Bệnh Viện Hàng Đầu', 'momo://hospital-booking', 'web_hospital_booking_btn_click'),
    'benh-vien': ('Thanh Toán Viện Phí & Đặt Lịch Khám Bệnh', 'momo://hospital-booking', 'web_hospital_booking_btn_click'),

    # Other Hub
    'ma-giam-gia': ('Săn Voucher Khuyến Mãi & Mã Giảm Giá MoMo', 'momo://voucher-hub', 'web_voucher_claim_btn_click'),
    'tu-vi': ('Xem Tử Vi & Quẻ Đầu Năm Cùng MoMo', 'momo://horoscope', 'web_horoscope_btn_click'),
}

def get_concrete_cta_hook(theme_slug):
    slug = theme_slug.lower()
    if slug in FEATURE_MOMO_MAP:
        name, link, evt = FEATURE_MOMO_MAP[slug]
        return f"{name} -> Deeplink: {link} -> Event: {evt}"
    return None

# Quy tắc gom cụm Sub-clusters theo Demand thực tế.
# Trigger khớp nguyên cụm từ (không khớp chuỗi con). Không đặt head term của theme (vd 'bảo hiểm y tế') làm trigger:
# nó gom mọi từ khóa chung vào một cụm chuyên biệt, làm primary của cụm lệch nghĩa. Từ khóa không khớp cụm nào
# đi về cụm fallback theo intent (FALLBACK_INTENT_CLUSTERS).
SUB_CLUSTER_RULES = {
    'vietlott': [
        ('Power 6/55', ['power 6 55', 'power 6/55', 'power 655', 'power655', 'xspower', 'power'], 'power-6-55'),
        ('Mega 6/45', ['mega 6 45', 'mega 6/45', 'mega 645', 'mega645', 'xổ số mega', 'mega'], 'mega-6-45'),
        ('Keno', ['keno', 'quay số nhanh'], 'keno'),
        ('Max 3D', ['max 3d', 'max3d', 'max 4d', 'max4d', 'max 3d pro', '3d max', 'xổ số 3d', 'vé số 3d'], 'max-3d'),
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
        ('Giá Vàng SJC & Vàng Miếng Hôm Nay', ['sjc', 'vàng miếng', 'vang mieng', 'hôm nay', 'hom nay', 'trong nước', 'hiện tại'], 'gia-vang-sjc'),
        ('Giá Vàng DOJI, PNJ & Mi Hồng', ['doji', 'pnj', 'mi hồng', 'mi hong', 'bảo tín', 'bao tin', 'phú quý', 'huy thanh'], 'vang-doji-pnj'),
        ('Giá Vàng Nhẫn 9999 & Vàng 24K, 18K', ['9999', 'nhẫn trơn', 'vàng nhẫn', '24k', '18k', 'vàng tây', 'vàng ta', 'vàng 10k'], 'vang-nhan-9999'),
        ('Biểu Đồ Giá Vàng & Thị Trường Thế Giới', ['thế giới', 'the gioi', 'kitco', 'biểu đồ', 'dự báo', 'xu hướng', 'trực tuyến', 'giá vàng', 'gia vang'], 'bieu-do-du-bao'),
    ],
    'gui-tiet-kiem': [
        ('Lãi Suất Tiết Kiệm Vietcombank & Big 4', ['vietcombank', 'vcb', 'agribank', 'bidv', 'vietinbank'], 'lai-suat-vietcombank-big4'),
        ('Lãi Suất Tiết Kiệm Techcombank, MB & TMCP', ['techcombank', 'tcb', 'mbbank', 'mb bank', 'mb', 'sacombank', 'vpbank', 'acb', 'tpbank', 'hdbank', 'shb', 'vib', 'ocb', 'msb'], 'lai-suat-techcombank-tmcp'),
        ('Công Cụ Tính Lãi Suất Tiết Kiệm', ['cách tính', 'tính lãi', 'công thức', '100 triệu', '50 triệu', '200 triệu', '500 triệu', '1 tỷ', 'bao nhiêu tiền', 'mỗi tháng'], 'cong-cu-tinh-lai-suat'),
        ('Gửi Tiết Kiệm Online & An Toàn', ['online', 'trực tuyến', 'an toàn', 'app', 'mở sổ', 'kỳ hạn', 'không kỳ hạn', 'rút trước hạn', 'đáo hạn', 'sổ tiết kiệm'], 'gui-tiet-kiem-online-an-toan'),
    ],
    'diem-tin-dung': [
        ('Tra Cứu Điểm Tín Dụng & Check CIC', ['tra cứu', 'tra cuu', 'kiểm tra', 'kiem tra', 'check', 'xem điểm', 'cách kiểm tra', 'online', 'cá nhân', 'miễn phí'], 'tra-cuu-diem-tin-dung-cic'),
        ('Xóa Nợ Xấu & Xếp Hạng CIC', ['nợ xấu', 'no xau', 'nhóm nợ', 'hạng 5', 'hạng 6', 'hạng 7', 'hạng 8', 'xóa nợ', 'bao lâu', 'lịch sử nợ'], 'xoa-no-xau-xep-hang-cic'),
        ('Điều Kiện Vay Theo Điểm Tín Dụng', ['có vay được không', 'vay được không', 'vay ngân hàng', 'duyệt vay', 'hạn mức', 'thẻ tín dụng', 'điều kiện'], 'dieu-kien-vay-theo-diem'),
        ('Thủ Tục, Biểu Phí & Báo Cáo CIC', ['thủ tục', 'biểu phí', 'chi phí', 'bao nhiêu tiền', 'báo cáo', 'trung tâm cic', 'ngân hàng nhà nước', 'điểm tín dụng', 'cic'], 'thu-tuc-bieu-phi-bao-cao-cic'),
    ],
    'bmi': [
        ('Công cụ tính chỉ số BMI', ['tính bmi', 'tinh bmi', 'cách tính', 'máy tính', 'calculator', 'online', 'công thức', 'phần mềm'], 'cong-cu-tinh-bmi'),
        ('Bảng BMI chuẩn Nam & Nữ', ['nam', 'nữ', 'người lớn', 'chuẩn', 'bảng', 'châu á', 'who', 'tiêu chuẩn'], 'bang-bmi-nam-nu'),
        ('Chỉ số BMI trẻ em', ['trẻ em', 'tuổi', 'bé', 'học sinh', 'mầm non'], 'bmi-tre-em'),
        ('Đánh giá thể trạng & Thừa cân', ['béo phì', 'gầy', 'thừa cân', 'suy dinh dưỡng', 'giảm cân', 'tăng cân'], 'the-trang-suc-khoe'),
    ],
    'lich-am': [
        ('Lịch Vạn Niên & Ngày Hoàng Đạo', ['vạn niên', 'van nien', 'ngày tốt', 'ngày hoàng đạo', 'giờ hoàng đạo', 'ngày xấu', 'hắc đạo', 'xuất hành', 'vạn sự'], 'lich-van-nien'),
        ('Đổi Ngày Âm Dương & Hôm Nay', ['đổi ngày', 'doi ngay', 'âm sang dương', 'dương sang âm', 'hôm nay', 'tra cứu', 'lịch âm dương', 'âm lịch hôm nay'], 'doi-ngay-am-duong'),
        ('Lịch Tết & Ngày Lễ Âm Lịch', ['tết', 'tet', 'nguyên đán', 'rằm', 'mùng 1', 'tháng giêng', 'ông công ông táo', 'vu lan', 'trung thu'], 'lich-tet-ngay-le'),
        ('Lịch Âm Các Năm', ['2025', '2026', '2027', 'năm nay', 'năm sau'], 'lich-am-cac-nam'),
    ],
    'ma-giam-gia': [
        ('Mã Giảm Giá Sàn TMĐT & Freeship', ['shopee', 'lazada', 'tiktok', 'tiki', 'freeship', 'chợ', '0đ', 'mã freeship', 'voucher shopee'], 'ma-giam-gia-tmdt'),
        ('Voucher Ăn Uống & Cafe', ['highland', 'highlands', 'phúc long', 'phuc long', 'cgv', 'haidilao', 'jollibee', 'kfc', 'lotteria', 'ăn uống', 'cafe', 'voucher highland'], 'voucher-an-uong-cafe'),
        ('Voucher Du Lịch & Di Chuyển', ['klook', 'traveloka', 'grab', 'grabfood', 'be', 'agoda', 'booking', 'vé máy bay', 'voucher klook'], 'voucher-du-lich-dich-vu'),
        ('Mã Giảm Giá & Voucher MoMo', ['momo', 'ví momo', 'thanh toán', 'chiết khấu', 'hoàn tiền', 'voucher momo', 'ưu đãi momo'], 'voucher-momo-uu-dai'),
    ],
    'data-4g': [
        ('Gói Cước Data Viettel', ['viettel', 'viettel 4g', 'viettel 5g', 'viettel 3g', 'gói viettel', 'st90', 'v90', 'sd135', 'đăng ký viettel', 'nạp 3g viettel'], 'goi-cuoc-viettel'),
        ('Gói Cước Data MobiFone', ['mobi', 'mobifone', 'mobi 4g', 'mobi 5g', 'mobi 3g', 'gói mobi', 'c90', 'kc90', 'đăng ký mobi', 'đăng ky 3g mobi', 'nạp data mobifone'], 'goi-cuoc-mobifone'),
        ('Gói Cước Data VinaPhone', ['vina', 'vinaphone', 'vina 4g', 'vina 5g', 'vina 3g', 'gói vina', 'vd149', 'd89y', 'đăng ký vina', 'nạp data vinaphone'], 'goi-cuoc-vinaphone'),
        ('Nạp Data & Cú Pháp Đăng Ký', ['nạp data', 'nap data', 'cách nạp', 'cú pháp', 'hủy gói', 'kiểm tra dung lượng', 'gia hạn', 'mua thêm', 'gói cước'], 'nap-data-cu-phap'),
        ('SIM Data & 5G Tốc Độ Cao', ['sim data', '5g', 'sim 5g', 'không giới hạn', 'tốc độ cao', 'phát wifi', 'sim 4g'], 'sim-data-5g'),
    ],
    'nap-tien-dien-thoai': [
        ('Nạp Tiền Viettel & Thẻ Cào Viettel', ['viettel', 'thẻ viettel', 'cào viettel', 'nạp thẻ viettel', 'cạc viettel', 'card viettel'], 'nap-the-viettel'),
        ('Nạp Tiền MobiFone & Thẻ Mobi', ['mobi', 'mobifone', 'thẻ mobi', 'nạp thẻ mobi', 'cào mobi', 'card mobi'], 'nap-the-mobifone'),
        ('Nạp Tiền VinaPhone & Thẻ Vina', ['vina', 'vinaphone', 'thẻ vina', 'nạp thẻ vina', 'cào vina', 'card vina'], 'nap-the-vinaphone'),
        ('Cú Pháp Nạp Tiền & Hướng Dẫn', ['cú pháp', 'cách nạp', 'hướng dẫn', 'nạp cho người khác', 'bắn tiền', 'chuyển tiền điện thoại'], 'cu-phap-huong-dan-nap'),
        ('Chiết Khấu & Khuyến Mãi Nạp Tiền', ['chiết khấu', 'khuyến mãi', '20%', '50%', 'ngày vàng', 'hoàn tiền'], 'chiet-khau-khuyen-mai'),
    ],
    # Cinema: per-use-case rules để tránh overlap tên sub-cluster
    've-xem-phim': [
        ('Giá Vé & Khuyến Mãi Đặt Vé', ['giá vé', 'gia ve', 'vé rẻ', 've re', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'voucher', 'combo', 'giảm giá', 'bao nhiêu tiền', 'momo', 'học sinh', 'sinh viên', 'thứ 3', 'thứ 4'], 'gia-ve-khuyen-mai'),
        ('Mua Vé Rạp & Ứng Dụng Online', ['mua vé', 'mua ve', 'đặt vé', 'dat ve', 'đặt phim', 'cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'beta', 'rạp', 'rap'], 'mua-ve-rap-app'),
        ('Cẩm Nang Hướng Dẫn Mua Vé', ['cách mua', 'hướng dẫn', 'kinh nghiệm', 'lưu ý', 'chọn ghế', 'đổi vé', 'hoàn vé', 'thanh toán'], 'cam-nang-mua-ve'),
        ('Vé Xem Phim Chiếu Rạp Mới', ['vé xem phim', 've xem phim', 'phim chiếu rạp', 'bom tấn', 'phim hay', 'review', 'trailer', 'chiếu rạp', 'phim'], 've-phim-chieu-rap-moi'),
    ],
    'lich-phim': [
        ('Lịch Chiếu Phim Hôm Nay & Cuối Tuần', ['hôm nay', 'hom nay', 'ngày mai', 'cuối tuần', 'suất chiếu', 'suat chieu', 'giờ chiếu', 'gio chieu', 'chiếu sớm', 'sneak'], 'lich-chieu-hom-nay-cuoi-tuan'),
        ('Lịch Phim Theo Cụm Rạp Toàn Quốc', ['cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'beta', 'quốc gia', 'chieuphimquocgia', 'vincom', 'aeon', 'starlight', 'mega gs', 'dcine', 'rạp', 'rap'], 'lich-phim-theo-cum-rap'),
        ('Tra Cứu Lịch Phim Sắp & Đang Chiếu', ['đang chiếu', 'dang chieu', 'sắp chiếu', 'sap chieu', 'tuần này', 'tháng này', 'bom tấn', 'phim mới', 'phim chiếu'], 'lich-phim-dang-chieu-sap-chieu'),
        ('Thông Tin Suất Chiếu & Lịch Rạp', ['lịch chiếu', 'lich chieu', 'lịch phim', 'lich phim', 'tra cứu', 'tìm lịch', 'xem lịch', 'phim', 'chiếu', 'lịch'], 'thong-tin-suat-chieu-lich-rap'),
    ],
    'rap': [
        ('Hệ Thống Rạp CGV Cinemas', ['cgv', 'cgv hà nội', 'cgv tp hcm', 'cgv vincom', 'cgv aeon', 'cgv quận'], 'he-thong-rap-cgv'),
        ('Hệ Thống Rạp Lotte, Galaxy & BHD', ['lotte', 'galaxy', 'bhd', 'beta', 'cinestar', 'quốc gia', 'mega gs', 'dcine', 'starlight'], 'he-thong-rap-lotte-galaxy-bhd'),
        ('Rạp Chiếu Phim Gần Đây & Phòng Chiếu', ['gần đây', 'gan day', 'gần nhất', 'địa chỉ', 'chi nhánh', 'phòng chiếu', 'imax', '4dx', 'gold class', 'lamour', 'ghế đôi', 'sweetbox'], 'rap-chieu-phim-gan-day'),
        ('Bảng Giá & Dịch Vụ Bỏng Nước Tại Rạp', ['giá vé', 'gia ve', 'vé rẻ', 'bắp', 'bỏng', 'nước', 'combo', 'menu', 'dịch vụ'], 'bang-gia-dich-vu-bong-nuoc'),
    ],
    'dat-phim': [
        ('Đặt Vé CGV & Lotte Cinema', ['cgv', 'lotte', 'lotte cinema'], 'dat-ve-cgv-lotte'),
        ('Đặt Vé Galaxy, Cinestar & Beta', ['galaxy', 'cinestar', 'beta', 'quốc gia', 'metiz', 'bhd', 'mega gs'], 'dat-ve-galaxy-cinestar-beta'),
        ('Đặt Vé Phim Online Qua App', ['app', 'online', 'momo', 'trực tuyến', 'đặt trước', 'chọn ghế'], 'dat-ve-phim-app-online'),
        ('Hướng Dẫn Đặt Vé & Thanh Toán', ['hướng dẫn', 'cách đặt', 'thanh toán', 'đổi vé', 'hoàn vé', 'đặt vé', 'dat ve', 'đặt phim', 'dat phim'], 'huong-dan-dat-ve-thanh-toan'),
    ],
    'phim': [
        ('Phim Chiếu Rạp Mới Nhất', ['chiếu rạp', 'chieu rap', 'phim rạp', 'phim mới', 'phim moi', 'sắp chiếu', 'bom tấn'], 'phim-chieu-rap-moi-nhat'),
        ('Top Phim Hay & Đánh Giá Phim', ['phim hay', 'top phim', 'review', 'đánh giá', 'trailer', 'thuyết minh', 'vietsub'], 'top-phim-hay-danh-gia'),
        ('Phim Hoạt Hình & Anime Hot', ['hoạt hình', 'anime', '3d', 'hoat hinh', 'manga'], 'phim-hoat-hinh-anime'),
        ('Thể Loại Phim & Tuyển Tập', ['hành động', 'kinh dị', 'tình cảm', 'hài', 'khoa học viễn tưởng', 'phim lẻ', 'phim bộ'], 'the-loai-phim-tuyen-tap'),
    ],
    'vay': [
        ('Vay Tiền Online Chuyển Khoản Nhanh', ['chuyển khoản', 'online', 'duyệt nhanh', 'cấp tốc', 'ngay', 'trong ngày', 'app vay', 'h5', 'cmnd', 'cccd', 'không thế chấp'], 'vay-online-chuyen-khoan'),
        ('Vay Tín Chấp & Vay Tiêu Dùng Ngân Hàng', ['tín chấp', 'tin chap', 'tiêu dùng', 'ngân hàng', 'shb finance', 'fe credit', 'home credit', 'mcredit', 'lotte finance', 'shinhan'], 'vay-tin-chap-tieu-dung'),
        ('Vay Theo Hạn Mức (Dưới 10tr - 50tr)', ['1 triệu', '2 triệu', '5 triệu', '10 triệu', '20 triệu', '30 triệu', '50 triệu', '100 triệu', 'hạn mức', 'khoản vay', 'sinh viên', 'nợ xấu'], 'vay-theo-han-muc'),
        ('Lãi Suất Vay & Công Cụ Tính Trả Góp', ['lãi suất', 'lai suat', 'trả góp', 'tra gop', 'cách tính', 'bảng tính', 'điều kiện', 'thủ tục', 'hồ sơ', 'vay'], 'lai-suat-tinh-tra-gop'),
    ],
    'vay-nhanh': [
        ('Vay Tiền Online Chuyển Khoản Nhanh', ['chuyển khoản', 'online', 'duyệt nhanh', 'cấp tốc', 'ngay', 'trong ngày', 'app vay', 'h5', 'cmnd', 'cccd', 'không thế chấp'], 'vay-online-chuyen-khoan'),
        ('Vay Tín Chấp & Vay Tiêu Dùng Ngân Hàng', ['tín chấp', 'tin chap', 'tiêu dùng', 'ngân hàng', 'shb finance', 'fe credit', 'home credit', 'mcredit', 'lotte finance', 'shinhan'], 'vay-tin-chap-tieu-dung'),
        ('Vay Theo Hạn Mức (Dưới 10tr - 50tr)', ['1 triệu', '2 triệu', '5 triệu', '10 triệu', '20 triệu', '30 triệu', '50 triệu', '100 triệu', 'hạn mức', 'khoản vay', 'sinh viên', 'nợ xấu'], 'vay-theo-han-muc'),
        ('Lãi Suất Vay & Công Cụ Tính Trả Góp', ['lãi suất', 'lai suat', 'trả góp', 'tra gop', 'cách tính', 'bảng tính', 'điều kiện', 'thủ tục', 'hồ sơ', 'vay'], 'lai-suat-tinh-tra-gop'),
    ],
    'vay-tin-chap': [
        ('Vay Tín Chấp Theo Lương & Hợp Đồng', ['theo lương', 'hợp đồng', 'sao kê', 'bảo hiểm nhân thọ', 'hóa đơn', 'tín chấp'], 'vay-tin-chap-theo-luong'),
        ('Vay Tín Chấp Ngân Hàng Lãi Suất Thấp', ['vietcombank', 'bidv', 'agribank', 'mbbank', 'vpbank', 'tpbank', 'shinhan', 'ngân hàng'], 'vay-tin-chap-ngan-hang'),
        ('Điều Kiện & Thủ Tục Vay Tín Chấp', ['điều kiện', 'thủ tục', 'hồ sơ', 'duyệt vay', 'hạn mức', 'nợ xấu'], 'dieu-kien-thu-tuc-vay-tin-chap'),
        ('Bảng Tính Trả Góp & Lãi Suất Tín Chấp', ['lãi suất', 'trả góp', 'cách tính', 'bảng tính', 'dư nợ giảm dần', 'vay'], 'bang-tinh-tra-gop-tin-chap'),
    ],
    'bao-hiem-xe-may': [
        ('Bảo Hiểm Xe Máy Bắt Buộc (TNDS)', ['tnds', 'bắt buộc', 'bat buoc', 'trách nhiệm dân sự', 'trach nhiem dan su', 'quy định', 'luật', 'mức phạt', 'công an', 'bị phạt'], 'tnds-bat-buoc-xe-may'),
        ('Bảo Hiểm Tự Nguyện & Cháy Nổ Xe Máy', ['tự nguyện', 'tu nguyen', 'cháy nổ', 'mất cắp', 'tai nạn', 'người ngồi trên xe', 'vật chất'], 'bao-hiem-tu-nguyen-xe-may'),
        ('Biểu Phí & Mua Bảo Hiểm Xe Máy Online', ['mua', 'đặt', 'online', 'trực tuyến', 'giá', 'biểu phí', 'bao nhiêu tiền', '66k', '86k', 'app', 'momo', 'giao tận nơi'], 'bieu-phi-mua-online-xe-may'),
        ('Tra Cứu Hạn Dùng & Bồi Thường Xe Máy', ['tra cứu', 'kiểm tra', 'check', 'thời hạn', 'hạn dùng', 'điện tử', 'bồi thường', 'hồ sơ', 'thủ tục'], 'tra-cuu-boi-thuong-xe-may'),
    ],
    'bao-hiem-o-to': [
        ('Bảo Hiểm TNDS Bắt Buộc Ô Tô', ['tnds', 'bắt buộc', 'bat buoc', 'trách nhiệm dân sự', 'dân sự', 'đăng kiểm', 'mức phạt', 'nghị định'], 'tnds-bat-buoc-o-to'),
        ('Bảo Hiểm Thân Vỏ & Vật Chất Xe Ô Tô', ['thân vỏ', 'than vo', 'vật chất', 'vat chat', 'thủy kích', 'ngập nước', 'mất cắp', 'tai nạn', 'xước', 'sơn'], 'bao-hiem-than-vo-o-to'),
        ('Báo Giá & Mua Bảo Hiểm Ô Tô Online', ['báo giá', 'giá', 'biểu phí', 'bao nhiêu tiền', 'mua online', 'bảo việt', 'pvi', 'pti', 'mic', 'bảo minh', 'liberty'], 'bao-gia-mua-online-o-to'),
        ('Quy Trình Giám Định & Bồi Thường Ô Tô', ['bồi thường', 'giám định', 'gara', 'sửa chữa', 'hồ sơ', 'thủ tục', 'miễn thường'], 'quy-trinh-boi-thuong-o-to'),
    ],
    'bhyt': [
        ('Quyền Lợi & Mức Hưởng Khám BHYT', ['quyền lợi', 'mức hưởng', 'khám chữa bệnh', 'bệnh viện', 'trái tuyến', 'đúng tuyến', '100%', '80%', 'chi trả', 'thuốc'], 'quyen-loi-muc-huong-bhyt'),
        ('Đóng Tiếp & Gia Hạn BHYT Hộ Gia Đình', ['hộ gia đình', 'đóng', 'gia hạn', 'tái tục', 'online', 'mua mới', 'mua ở đâu', 'bao nhiêu tiền', 'giá', 'dịch vụ công'], 'dong-tiep-gia-han-bhyt'),
        ('Tra Cứu Thẻ & Mã Số BHYT Điện Tử', ['tra cứu', 'kiểm tra', 'check', 'mã số', 'số thẻ', 'hạn sử dụng', 'giá trị', 'điện tử', 'vssid', 'vneid'], 'tra-cuu-the-bhyt-dien-tu'),
        ('Thủ Tục Cấp Lại & Đổi Thẻ BHYT', ['cấp lại', 'đổi thẻ', 'mất thẻ', 'sai thông tin', 'thủ tục', 'hồ sơ'], 'thu-tuc-doi-the-bhyt'),
    ],
    'bhxh': [
        ('Rút BHXH 1 Lần & Điều Kiện Chi Trả', ['1 lần', 'một lần', 'rút', 'lãnh', 'cách tính', 'hồ sơ', 'điều kiện', 'thủ tục', 'bao lâu'], 'rut-bhxh-1-lan'),
        ('Chế Độ Thai Sản, Ốm Đau & Hưu Trí', ['thai sản', 'ốm đau', 'hưu trí', 'lương hưu', 'nghỉ việc', 'dưỡng sức', 'chế độ', 'tuổi nghỉ hưu', 'thất nghiệp'], 'che-do-thai-san-huu-tri'),
        ('Tra Cứu Sổ BHXH & Quá Trình Đóng', ['tra cứu', 'sổ bhxh', 'quá trình đóng', 'kiểm tra', 'mã số', 'vssid', 'cổng dịch vụ công', 'dvc'], 'tra-cuu-so-bhxh-qua-trinh'),
        ('Đóng BHXH Tự Nguyện & Doanh Nghiệp', ['tự nguyện', 'bắt buộc', 'mức đóng', 'phương thức đóng', 'doanh nghiệp', 'nộp tiền'], 'dong-bhxh-tu-nguyen'),
    ],
    'phat-nguoi': [
        ('Tra Cứu Phạt Nguội Toàn Quốc & Cục CSGT', ['tra cứu', 'kiểm tra', 'check', 'cục csgt', 'cảnh sát giao thông', 'toàn quốc', 'app', 'website', 'chính xác', 'hôm nay'], 'tra-cuu-phat-nguoi-csgt'),
        ('Phạt Nguội Xe Ô Tô & Thủ Tục Đăng Kiểm', ['ô tô', 'oto', 'xe ô tô', 'đăng kiểm', 'từ chối đăng kiểm', 'cảnh báo đăng kiểm'], 'phat-nguoi-o-to-dang-kiem'),
        ('Phạt Nguội Xe Máy & Lỗi Vi Phạm', ['xe máy', 'xe may', 'mô tô', 'lỗi vi phạm', 'tốc độ', 'vượt đèn đỏ', 'sai làn', 'nguội xe máy'], 'phat-nguoi-xe-may-loi-vi-pham'),
        ('Nộp Phạt Nguội Online & Quy Trình Xử Lý', ['nộp phạt', 'nop phat', 'đóng phạt', 'dịch vụ công', 'kho bạc', 'thời hạn', 'quy trình', 'xử lý', 'ở đâu', 'phạt nguội'], 'nop-phat-nguoi-online'),
    ],
    'bien-so': [
        ('Tra Cứu Biển Số Xe 63 Tỉnh Thành', ['tỉnh', 'tỉnh nào', 'tỉnh thành', 'toàn quốc', 'tra cứu', 'bảng tra', 'danh sách', 'ký hiệu', 'mã vùng'], 'tra-cuu-bien-so-63-tinh'),
        ('Đấu Giá Biển Số Xe Đẹp & Định Danh', ['đấu giá', 'dau gia', 'định danh', 'dinh danh', 'biển số định danh', 'quy chế', 'tiền đặt trước'], 'dau-gia-bien-so-dinh-danh'),
        ('Ý Nghĩa Biển Số Đẹp & Phong Thủy', ['phong thủy', 'ý nghĩa', 'ngũ quý', 'tứ quý', 'thần tài', 'lộc phát', 'số đẹp', 'hợp mệnh', 'dịch biển'], 'y-nghia-bien-so-phong-thuy'),
        ('Thủ Tục Cấp, Đổi Biển & Sang Tên Xe', ['sang tên', 'đổi biển', 'cấp lại', 'thủ tục', 'hồ sơ', 'thu hồi', 'đăng ký xe', 'làm biển'], 'thu-tuc-cap-doi-bien-so'),
    ],
    'bien-so-xe': [
        ('Tra Cứu Biển Số Xe 63 Tỉnh Thành', ['tỉnh', 'tỉnh nào', 'tỉnh thành', 'toàn quốc', 'tra cứu', 'bảng tra', 'danh sách', 'ký hiệu', 'mã vùng'], 'tra-cuu-bien-so-63-tinh'),
        ('Đấu Giá Biển Số Xe Đẹp & Định Danh', ['đấu giá', 'dau gia', 'định danh', 'dinh danh', 'biển số định danh', 'quy chế', 'tiền đặt trước'], 'dau-gia-bien-so-dinh-danh'),
        ('Ý Nghĩa Biển Số Đẹp & Phong Thủy', ['phong thủy', 'ý nghĩa', 'ngũ quý', 'tứ quý', 'thần tài', 'lộc phát', 'số đẹp', 'hợp mệnh', 'dịch biển'], 'y-nghia-bien-so-phong-thuy'),
        ('Thủ Tục Cấp, Đổi Biển & Sang Tên Xe', ['sang tên', 'đổi biển', 'cấp lại', 'thủ tục', 'hồ sơ', 'thu hồi', 'đăng ký xe', 'làm biển'], 'thu-tuc-cap-doi-bien-so'),
    ],
    'bien-so-dep': [
        ('Đấu Giá Biển Số Xe Đẹp Trực Tuyến', ['đấu giá', 'dau gia', 'trực tuyến', 'biển số đẹp', 'vpa', 'tiền cọc'], 'dau-gia-bien-so-truc-tuyen'),
        ('Biển Số Ngũ Quý, Tứ Quý & Thần Tài', ['ngũ quý', 'tứ quý', 'thần tài', 'lộc phát', 'tam hoa', 'sảnh tiến', 'phát lộc'], 'bien-so-ngu-quy-than-tai'),
        ('Định Danh Biển Số Đẹp Theo Luật', ['định danh', 'dinh danh', 'thu hồi', 'sang tên', 'chuyển nhượng', 'quy định'], 'dinh-danh-bien-so-dep'),
        ('Ý Nghĩa Phong Thủy Biển Số Xe', ['phong thủy', 'ý nghĩa', 'dịch biển', 'hợp tuổi', 'hợp mệnh'], 'y-nghia-phong-thuy-bien-so'),
    ],
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
    ],
    'student': [
        ('Tuyển sinh & Xét tuyển', ['tuyển sinh', 'xét tuyển', 'điểm chuẩn', 'thi tốt nghiệp', 'thi thpt', 'nguyện vọng', 'học bạ', 'tổ hợp môn'], 'tuyen-sinh'),
        ('Trường & Ngành học', ['trường', 'đại học', 'cao đẳng', 'trung cấp', 'học viện', 'ngành học', 'chuyên ngành', 'mã trường'], 'truong-nganh-hoc'),
        ('Học phí & Học bổng', ['học phí', 'học bổng', 'miễn giảm', 'lệ phí', 'tín chỉ'], 'hoc-phi-hoc-bong'),
        ('Nhà trọ & Ký túc xá', ['nhà trọ', 'phòng trọ', 'ký túc xá', 'thuê trọ', 'tìm trọ', 'chỗ ở'], 'nha-tro-ktx'),
        ('Sinh viên & Cổng thông tin', ['sinh viên', 'cổng thông tin', 'đăng nhập', 'tài khoản', 'email', 'thẻ sinh viên'], 'sinh-vien-cong-thong-tin'),
        ('Việc làm & Kỹ năng', ['việc làm', 'part-time', 'bán thời gian', 'thực tập', 'tuyển dụng', 'kỹ năng'], 'viec-lam-ky-nang'),
    ]
}

FALLBACK_INTENT_CLUSTERS = [
    ('Công cụ & Tra cứu', 'Tool/Calculator', 'tra-cuu'),
    ('So sánh & Đánh giá', 'Commercial', 'so-sanh'),
    ('Đăng ký & Hướng dẫn thủ tục', 'Transactional', 'thu-tuc'),
    ('Cẩm nang & Hỏi đáp', 'Informational', 'cam-nang'),
    ('Cổng dịch vụ & Liên hệ', 'Navigational', 'lien-he'),
]

VIETLOTT_ENTITIES = [
    'vietlott', 'viet lott', 'việt lott', 'mega 6 45', 'mega 6/45', 'mega645',
    'power 6 55', 'power 6/55', 'power 655', 'power655', 'keno', 'max 3d', 'max3d',
    'max 3d pro', 'bingo18', 'bingo 18', 'vietlott sms', 'mua vietlott', 'vé số vietlott'
]

BANK_THEMES = {
    'Vietcombank': ['vietcombank', 'vcb', 'vietcom bank', 'việt com bank', 'ngoại thương'],
    'Techcombank': ['techcombank', 'techcom bank', 'kỹ thương'],
    'BIDV': ['bidv', 'đầu tư và phát triển'],
    'VietinBank': ['vietinbank', 'vietin bank', 'việt tin', 'công thương'],
    'agribank': ['agribank', 'agri bank', 'nông nghiệp'],
    'mbbank': ['mbbank', 'mb bank', 'quân đội', 'ngân hàng mb'],
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

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('05_HUBS/game-hub-roadmap.xlsx')

# Remove Provider Subpages sheet if already exists
if 'Provider Subpages' in wb.sheetnames:
    del wb['Provider Subpages']

ws = wb.create_sheet('Provider Subpages')

# -------------------------------------------------------------------------
# Styles
# -------------------------------------------------------------------------
font_title = Font(name='Calibri', size=13, bold=True, color='0F172A')
font_subtitle = Font(name='Calibri', size=10, italic=True, color='475569')
font_sec_hdr = Font(name='Calibri', size=11, bold=True, color='0369A1')
font_tbl_hdr = Font(name='Calibri', size=10, bold=True, color='0F172A')
font_data_bold = Font(name='Calibri', size=9, bold=True, color='0F172A')
font_data = Font(name='Calibri', size=9, color='334155')
font_code = Font(name='Consolas', size=9, color='0369A1')

fill_sec = PatternFill(start_color='E0F2FE', end_color='E0F2FE', fill_type='solid')
fill_hdr = PatternFill(start_color='F1F5F9', end_color='F1F5F9', fill_type='solid')
fill_sub_hdr = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid')

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

align_left_wrap = Alignment(horizontal='left', vertical='top', wrap_text=True)
align_left_top = Alignment(horizontal='left', vertical='top')
align_center_top = Alignment(horizontal='center', vertical='top')
align_left_nowrap = Alignment(horizontal='left', vertical='center')

# Title rows
ws.cell(1, 1, 'QUY CHUẨN CẤU TRÚC & NỘI DUNG SUBPAGE NHÀ PHÁT HÀNH (PROVIDER SUBPAGE SPECIFICATION)')
ws.cell(1, 1).font = font_title
ws.cell(2, 1, 'Đặc tả cấu trúc On-Page chuẩn SEO & Bộ nội dung copywriting mẫu chuẩn Brand Guideline MoMo cho từng Nhà Phát Hành (URL: /nap-the-game/{tên-nph})')
ws.cell(2, 1).font = font_subtitle

# =========================================================================
# SECTION 1: CẤU TRÚC 7 MODULES SUBPAGE NPH CHUẨN BRAND GUIDELINE
# =========================================================================
row = 4
ws.cell(row, 1, 'PHẦN 1: BẢNG QUY CHUẨN KHUNG CẤU TRÚC ON-PAGE SUBPAGE NPH CHUẨN BRAND GUIDELINE (7 MODULES KHUNG SƯỜN)')
ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=7)
for c in range(1, 8):
    cell = ws.cell(row, c)
    cell.font = font_sec_hdr
    cell.fill = fill_sec
    cell.border = thin_border
ws.row_dimensions[row].height = 24

row += 1
headers_sec1 = [
    'STT', 
    'Thứ Tự Module', 
    'Tên Thành Phần UI', 
    'Vị Trí & Tỷ Lệ', 
    'Mô Tả Thành Phần & Wireframe', 
    'Quy Chuẩn Nội Dung & Copywriting Chuẩn Brand MoMo', 
    'Yêu Cầu UX / Kỹ Thuật & Schema'
]
for col_idx, h in enumerate(headers_sec1, start=1):
    cell = ws.cell(row, col_idx, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_hdr
    cell.border = thin_border
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws.row_dimensions[row].height = 28

modules_data = [
    (
        '1.1',
        'Module 1',
        'Hero Banner & Entity Header',
        'Above-the-fold (100% màn hình đầu)',
        'Khối đầu trang gồm: Tiêu đề H1 rõ ràng tên NPH và loại thẻ, Badge xác thực đối tác phân phối chính hãng, đoạn giới thiệu ngắn về NPH và hệ sinh thái game, kèm 3 cam kết thương hiệu (Trust Badges).',
        'Brand Guideline: Tôn trọng thương hiệu NPH, định vị MoMo là cổng thông tin & phân phối mã thẻ Softpin chính ngạch. Copywriting trực diện, trung thực, không giật gân, không dùng từ sáo rỗng. Nêu bật 3 cam kết vàng: 100% mã sạch từ NPH, Chiết khấu trực tiếp minh bạch, Nhận mã trong 30 giây.',
        'Component Hero Banner từ MoBase UI Kit; Breadcrumb: Trang chủ > Nạp thẻ game > {Tên NPH}; Schema: Organization & Brand Entity.'
    ),
    (
        '1.2',
        'Module 2',
        'Bảng Niêm Yết Mệnh Giá & Tỷ Giá Quy Đổi',
        'Above-the-fold (Ngay dưới Hero)',
        'Bảng ma trận hiển thị 6 - 8 mốc mệnh giá tiêu chuẩn (20.000đ đến 2.000.000đ). Mỗi dòng gồm: Mệnh giá thẻ, Mức chiết khấu %, Giá bán tại NaptheNgay, Tỷ lệ tiền tệ quy đổi ingame (KNB, Kim Cương, Vàng), và Nút CTA mua thẻ tương ứng.',
        'Brand Guideline: Minh bạch 100% về giá bán và tỷ lệ quy đổi. Nêu rõ giá thực trả sau chiết khấu. Nút CTA ghi rõ hành động và mệnh giá (Ví dụ: [ Mua Thẻ 100k Trên NaptheNgay ]). Không dùng từ "rẻ nhất quả đất" hay "siêu sale sốc".',
        'Component Table tương tác responsive trên Mobile; Nút CTA gắn dynamic URL link out sang NaptheNgay.vn kèm tham số query; Schema: Product & Offer.'
    ),
    (
        '1.3',
        'Module 3',
        'Master CTA Sang NaptheNgay.vn & Hướng Dẫn Luồng',
        'Sticky Header / Hero (Mobile & Desktop)',
        'Nút Master CTA nổi bật: [ MUA THẺ {TÊN THẺ} CHIẾT KHẤU CAO TẠI NAPTHENGAY.VN ]. Đính kèm ghi chú luồng 3 bước chuyển tiếp: Chọn thẻ trên Web MoMo -> Tự động chuyển và chọn sẵn trên NaptheNgay -> Thanh toán nhận mã PIN nạp vào cổng NPH.',
        'Brand Guideline: Nêu rõ bản chất luồng để người dùng an tâm khi chuyển tab. Nhấn mạnh phương thức thanh toán an toàn tiện lợi bằng mã QR Ví MoMo tại NaptheNgay.vn. Thể hiện sự phối hợp đối tác uy tín giữa MoMo và NaptheNgay.',
        'Target URL: https://napthengay.vn/?partner=momo&card={code}&amount={amount}; Thuộc tính bắt buộc: target="_blank" rel="noopener noreferrer nofollow"; Event tracking: click_buy_napthengay.'
    ),
    (
        '1.4',
        'Module 4',
        'Hệ Sinh Thái Tựa Game Thuộc NPH',
        'Mid-page (Giữa trang)',
        'Lưới thẻ (Game Card Grid) hiển thị 6 - 15 tựa game tiêu biểu của NPH sử dụng chung loại thẻ cào này. Mỗi thẻ game gồm: Tên game, Thể loại, Ảnh artwork, Đơn vị tiền tệ ingame, Nút [Xem Bảng Giá Nạp] (link nội bộ) và Nút [Mua Thẻ Ngay] (link NaptheNgay).',
        'Brand Guideline: Phân loại game chính xác theo thông tin đăng ký NPH, không đưa thông tin sai lệch về game. Nhắc nhở người chơi mua đúng loại thẻ để nạp cho đúng tựa game, tránh mua nhầm thẻ.',
        'Component Card Grid responsive 2 cột (Mobile) / 4 cột (Desktop); Schema: ItemList kết hợp SoftwareApplication.'
    ),
    (
        '1.5',
        'Module 5',
        'Bảng So Sánh Chi Phí Nạp (Web vs In-App Store)',
        'Mid-page (Sau danh mục game)',
        'Bảng so sánh 5 tiêu chí: Thuế & phí dịch vụ, Số tiền thực trả gói 500k, Lượng tiền tệ ingame nhận được, Quyền lợi sự kiện nạp đầu/nạp tích lũy, Phương thức thanh toán giữa: Mua thẻ qua MoMo/NaptheNgay (0% thuế, chiết khấu 3-5%) vs Nạp trực tiếp In-App Apple/Google (chịu 30% thuế phí).',
        'Brand Guideline: Giáo dục người dùng về bài toán kinh tế một cách văn minh, khách quan. Không công kích Store mà nêu rõ cơ chế phí nền tảng 30% của Store quốc tế. Khẳng định quyền lợi nạp thẻ qua Web được hưởng 100% mốc sự kiện NPH.',
        'Component Markdown Comparison Table; Highlight trực quan số tiền tiết kiệm và lượng KNB chênh lệch.'
    ),
    (
        '1.6',
        'Module 6',
        'Cẩm Nang 3 Bước Nạp Thẻ Vào Cổng NPH',
        'Near-bottom (Gần chân trang)',
        'Quy trình 3 bước cụ thể có ảnh minh họa: Bước 1: Mua mã thẻ trên NaptheNgay qua Web MoMo và sao chép mã PIN -> Bước 2: Truy cập cổng nạp chính thức của NPH (nap.{nph}.vn), đăng nhập tài khoản và chọn nhân vật/server -> Bước 3: Chọn nạp bằng thẻ Softpin, dán Serial + PIN và xác nhận.',
        'Brand Guideline: Cung cấp chính xác đường dẫn cổng nạp chính thức của từng NPH, cảnh báo người dùng không truy cập các trang nạp giả mạo để phòng chống lừa đảo. Thể hiện trách nhiệm bảo vệ khách hàng của MoMo.',
        'Visual Step Cards (1, 2, 3); Nút link out an toàn sang cổng NPH; Schema: HowTo Step Schema.'
    ),
    (
        '1.7',
        'Module 7',
        'Hỏi Đáp (FAQ), Hỗ Trợ Kỹ Thuật & Entity SEO',
        'Bottom (Chân trang)',
        'Khối FAQ Accordion giải đáp 5 câu hỏi thường gặp: Thẻ có nạp được cho mọi game của NPH không, Hạn sử dụng thẻ, Thanh toán bằng Ví Trả Sau, Xử lý khi mã thẻ bị lỗi, Chính sách hoàn hủy. Kèm số Hotline CSKH MoMo (1900 5454 41) và thông tin pháp lý.',
        'Brand Guideline: Trả lời ngắn gọn, minh bạch, có trách nhiệm. Cung cấp hotline CSKH chính thức, không trốn tránh trách nhiệm giải quyết khiếu nại. Tuân thủ chuẩn E-E-A-T và quy chuẩn YMYL nội dung tài chính.',
        'Component Accordion UI; Schema: FAQPage (hỗ trợ Rich Snippets Google) & BreadcrumbList.'
    )
]

for item in modules_data:
    row += 1
    ws.row_dimensions[row].height = 42
    ws.cell(row, 1, item[0]).alignment = align_center_top
    ws.cell(row, 2, item[1]).alignment = align_left_top
    ws.cell(row, 2, item[1]).font = font_data_bold
    ws.cell(row, 3, item[2]).alignment = align_left_top
    ws.cell(row, 3, item[2]).font = font_data_bold
    ws.cell(row, 4, item[3]).alignment = align_left_top
    ws.cell(row, 5, item[4]).alignment = align_left_wrap
    ws.cell(row, 6, item[5]).alignment = align_left_wrap
    ws.cell(row, 7, item[6]).alignment = align_left_wrap
    
    for c in range(1, 8):
        cell = ws.cell(row, c)
        if c != 2 and c != 3:
            cell.font = font_data
        cell.border = thin_border

# =========================================================================
# SECTION 2: BẢNG DANH MỤC SUBPAGE TỪNG PROVIDER & NỘI DUNG MẪU
# =========================================================================
row += 2
sec2_start = row
ws.cell(row, 1, 'PHẦN 2: BẢNG DANH MỤC SUBPAGE TỪNG PROVIDER & BỘ NỘI DUNG VIẾT SẴN CHUẨN BRAND GUIDELINE (18 NHÀ PHÁT HÀNH TRỌNG ĐIỂM)')
ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=14)
for c in range(1, 15):
    cell = ws.cell(row, c)
    cell.font = font_sec_hdr
    cell.fill = fill_sec
    cell.border = thin_border
ws.row_dimensions[row].height = 24

row += 1
headers_sec2 = [
    'STT',
    'Nhà Phát Hành (Provider)',
    'Phân Loại Đối Tác',
    'Đường Dẫn URL Chuẩn Hóa',
    'Loại Mã Thẻ & Mã Card Code',
    'Cổng Nạp Chính Thức Của NPH',
    'Tiêu Đề H1 Chuẩn SEO & Brand',
    'Meta Title & Description',
    'Hero Copywriting & 3 Cam Kết Vàng MoMo',
    'Tựa Game Nổi Bật & Tiền Tệ Ingame',
    'Bảng Mệnh Giá & Tỷ Giá Quy Đổi Mẫu',
    'Cấu Trúc URL CTA Sang NaptheNgay',
    'Cẩm Nang 3 Bước Nạp Thẻ Vào Cổng NPH',
    'Hỏi Đáp Thường Gặp (FAQ Chuẩn E-E-A-T)'
]
for col_idx, h in enumerate(headers_sec2, start=1):
    cell = ws.cell(row, col_idx, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_hdr
    cell.border = thin_border
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws.row_dimensions[row].height = 32

providers_data = [
    (
        1,
        'Funtap (Funtek Software)',
        'Tier 1 (Đại NPH)',
        '/nap-the-game/funtap',
        'Thẻ Funcard (code: funcard)',
        'https://nap.funtap.vn',
        'Cổng Mua Mã Thẻ Nạp Game Funtap (Funcard) - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Funcard Nạp Game Funtap Chiết Khấu 5% | MoMo\nDesc: Mua mã thẻ Funcard nạp game Funtap (Tiểu Yêu Tầm Đạo, Đấu La Đại Lục) nhận mã PIN tức thì trong 30 giây. Chiết khấu cao, an toàn 100%.',
        'Funtap là nhà phát hành game mobile hàng đầu tại Việt Nam với hơn 20 tựa game nhập vai, chiến thuật thịnh hành. MoMo hợp tác phân phối mã thẻ Funcard chính hãng, giao mã tức thì qua Web với mức chiết khấu tốt nhất.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã sạch xuất trực tiếp từ NPH Funtap.\n2. Giao mã PIN và Serial trong 30 giây sau khi thanh toán.\n3. Tiết kiệm 10% - 30% chi phí so với nạp trực tiếp qua App Store.',
        'Tiểu Yêu Tầm Đạo (Tiên Ngọc), Đấu La Đại Lục (Kim Cương), Kiếm Vũ Thiên Hành Ca (KNB), Tình Kiếm 3D (Tiên Ngọc), Ragnarok X (Kim Cương), MU Vượt Thời Đại (KNB).',
        'Mệnh giá: 20k (19.4k -> 200 KNB) | 50k (48.2k -> 500 KNB) | 100k (96k -> 1.050 KNB) | 200k (191k -> 2.150 KNB) | 500k (475k -> 5.500 KNB) | 1Tr (950k -> 11.200 KNB) | 2Tr (1.900k -> 23.000 KNB). Chiết khấu từ 3.0% đến 5.0%.',
        'https://napthengay.vn/?partner=momo&card=funcard&amount=100000',
        'Bước 1: Chọn mệnh giá thẻ Funcard trên Web MoMo và bấm [Mua Thẻ Ngay] để mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Truy cập cổng nạp nap.funtap.vn, đăng nhập tài khoản Funtap, chọn Game, Server và Nhân vật cần nạp.\nBước 3: Chọn phương thức "Thẻ Funcard", dán Serial và PIN đã nhận để nhận ngay Tiên Ngọc/KNB trong game.',
        'Q1: Thẻ Funcard nạp được những game nào?\n-> Nạp được 100% game do Funtap phát hành tại VN.\nQ2: Thẻ mua trên MoMo có hạn dùng bao lâu?\n-> Hạn sử dụng tối thiểu 24 tháng kể từ ngày giao dịch.\nQ3: Có dùng được Ví Trả Sau MoMo không?\n-> Có, hỗ trợ thanh toán qua Ví Trả Sau 0% lãi suất.'
    ),
    (
        2,
        'SohaGame (VCCorp)',
        'Tier 1 (Đại NPH)',
        '/nap-the-game/sohagame',
        'Thẻ Sohacoin (code: sohacoin)',
        'https://nap.soha.vn',
        'Cổng Mua Mã Thẻ Nạp Game SohaGame (Sohacoin) - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Sohacoin Nạp Game SohaGame Chiết Khấu Cao | MoMo\nDesc: Mua mã thẻ Sohacoin nạp game SohaGame (Thục Sơn Kỳ Hiệp, Loạn Chiến Mobile, Tam Quốc Ca Ca) nhận mã tức thì. Chiết khấu đến 5%, thanh toán QR tiện lợi.',
        'SohaGame thuộc VCCorp, chuyên phát hành các dòng game kiếm hiệp, tiên hiệp và chiến thuật thẻ tướng đông đảo người chơi. Mua thẻ Sohacoin qua MoMo giúp game thủ nạp nhanh vào toàn bộ hệ sinh thái SohaGame với chiết khấu tốt.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã Sohacoin chính hãng từ VCCorp.\n2. Giao mã Serial và PIN trong 30 giây trên màn hình.\n3. Nhận trọn vẹn 100% mốc sự kiện nạp đầu và quà NPH.',
        'Thục Sơn Kỳ Hiệp Mobile (Kim Phiếu), Loạn Chiến Mobile (Kim Cương), Tam Quốc Ca Ca (KNB), Thần Ma Đại Lục (Linh Thạch), Tuyệt Kiếm Cổ Phong (Ngọc).',
        'Mệnh giá: 20k (19.4k -> 20 Sohacoin) | 50k (48.2k -> 50 Sohacoin) | 100k (96k -> 105 Sohacoin) | 200k (191k -> 215 Sohacoin) | 500k (475k -> 550 Sohacoin) | 1Tr (950k -> 1.150 Sohacoin) | 2Tr (1.900k -> 2.350 Sohacoin). Chiết khấu từ 3.0% đến 5.0%.',
        'https://napthengay.vn/?partner=momo&card=sohacoin&amount=100000',
        'Bước 1: Chọn mệnh giá thẻ Sohacoin trên Web MoMo, bấm chuyển sang NaptheNgay.vn và quét QR MoMo thanh toán.\nBước 2: Mở website nap.soha.vn, đăng nhập tài khoản SohaGame, chọn đúng tựa game và nhân vật.\nBước 3: Chọn phương thức "Thẻ Sohacoin", nhập Serial và Mã PIN để nhận tiền tệ ingame tức thì.',
        'Q1: Sohacoin quy đổi thành tiền ingame như thế nào?\n-> 1 Sohacoin = 1.000đ giá trị nạp, khi đổi sang ingame sẽ được áp dụng tỷ giá từng game kèm khuyến mãi.\nQ2: Nạp thẻ có được tích điểm VIP Soha không?\n-> Có, nạp bằng Sohacoin được tích lũy 100% điểm VIP SohaGame.\nQ3: Xử lý thế nào nếu gặp lỗi nạp?\n-> Liên hệ hotline MoMo 1900 5454 41 hoặc CSKH SohaGame để được kiểm tra đổi mã trong 5 phút.'
    ),
    (
        3,
        'Gamota (Appota Corporation)',
        'Tier 1 (Đại NPH)',
        '/nap-the-game/gamota',
        'Thẻ Appotacard (code: appota)',
        'https://nap.gamota.com',
        'Cổng Mua Mã Thẻ Nạp Game Gamota (Appotacard) - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Appotacard Nạp Game Gamota Chiết Khấu 5% | MoMo\nDesc: Mua thẻ Appota nạp game Gamota (Zenless Zone Zero, Lords Mobile, Tru Tiên 3D) nhận mã nhanh trong 30 giây. An toàn tuyệt đối, thanh toán QR tiện lợi.',
        'Gamota là nhà phát hành hàng đầu với các siêu phẩm nhập vai MMORPG và hợp tác phát hành các tựa game bom tấn toàn cầu như Zenless Zone Zero, Lords Mobile. Thẻ Appotacard là phương thức nạp tiết kiệm nhất cho hệ sinh thái Gamota.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã Appota sạch từ Appota Corporation.\n2. Tiết kiệm 10% - 30% so với nạp qua Apple In-App Purchase.\n3. Hỗ trợ đa dạng nguồn tiền MoMo, Túi Thần Tài và Ví Trả Sau.',
        'Zenless Zone Zero (Film / Polychrome), Tru Tiên 3D (Vàng), Lords Mobile (Gems), Rise of Kingdoms (Rubs), Tân Ỷ Thiên Đồ Long Ký (KNB), Beast Lord (Gems).',
        'Mệnh giá: 20k (19.4k -> 20 Vàng Appota) | 50k (48.2k -> 50 Vàng Appota) | 100k (96k -> 105 Vàng) | 200k (191k -> 215 Vàng) | 500k (475k -> 550 Vàng) | 1Tr (950k -> 1.150 Vàng) | 2Tr (1.900k -> 2.350 Vàng). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=appota&amount=100000',
        'Bước 1: Chọn mệnh giá thẻ Appota trên Web MoMo, bấm mở NaptheNgay.vn để thanh toán qua QR MoMo.\nBước 2: Truy cập nap.gamota.com, đăng nhập tài khoản Gamota, chọn Game và Server.\nBước 3: Chọn phương thức "Thẻ Appota", điền số Serial và Mã nạp để hoàn tất cộng vật phẩm.',
        'Q1: Game Zenless Zone Zero có nạp bằng Appotacard được không?\n-> Có, phiên bản ZZZ do Gamota đồng phát hành tại VN hỗ trợ nạp thẻ Appota trên cổng chính thức.\nQ2: Thẻ Appota có nạp được cho ứng dụng khác không?\n-> Thẻ nạp được cho toàn bộ game và tiện ích thuộc hệ sinh thái Appota/Gamota.\nQ3: Tôi có thể xem lại lịch sử mã thẻ đã mua ở đâu?\n-> Xem lại trực tiếp trong Lịch sử giao dịch App MoMo hoặc Email nhận hóa đơn.'
    ),
    (
        4,
        'VTC Game (VTC Intecom)',
        'Tier 1 (Đại NPH)',
        '/nap-the-game/vtc-game',
        'Thẻ Vcoin (code: vcoin)',
        'https://vtcpay.vn / https://napthe.vtcgame.vn',
        'Cổng Mua Mã Thẻ Nạp Game VTC (Vcoin) - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Vcoin Nạp Game Đột Kích, Audition Chiết Khấu 5% | MoMo\nDesc: Mua mã thẻ Vcoin chính hãng nạp Đột Kích (Crossfire), Audition, Laplace M nhận mã trong 30 giây. Chiết khấu cao, giao dịch an toàn 100%.',
        'VTC Game thuộc Tổng công ty Truyền thông Đa phương tiện VTC, gắn liền với các tựa game tượng đài eSports như Đột Kích (Crossfire) và Audition. Thẻ Vcoin là đồng tiền chung nạp cho toàn bộ game VTC và các game đối tác liên kết.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Thẻ Vcoin chính hãng từ VTC Intecom.\n2. Mã Serial và PIN hiển thị tức thì, hỗ trợ sao chép 1-chạm.\n3. Hỗ trợ kỹ thuật 24/7, cam kết đổi mã nếu phát sinh lỗi từ hệ thống.',
        'Đột Kích - Crossfire (Go-Coin / Vcoin), Audition (Vcoin), Laplace M (Ốc Vàng), Phục Kích Mobile (Kim Cương), Tập Kích (Kim Cương).',
        'Mệnh giá: 20k (19.4k -> 20 Vcoin) | 50k (48.2k -> 50 Vcoin) | 100k (96k -> 100 Vcoin) | 200k (191k -> 200 Vcoin) | 500k (475k -> 500 Vcoin) | 1Tr (950k -> 1.000 Vcoin) | 2Tr (1.900k -> 2.000 Vcoin). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=vcoin&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Vcoin trên Web MoMo, bấm mở NaptheNgay.vn và quét QR MoMo thanh toán.\nBước 2: Mở website napthe.vtcgame.vn, đăng nhập tài khoản VTC ID, chọn Game và Dịch vụ cần nạp.\nBước 3: Nhập Mã thẻ và Số Serial để hoàn tất nạp Vcoin vào tài khoản game.',
        'Q1: Thẻ Vcoin nạp Đột Kích có được hưởng sự kiện nạp thẻ không?\n-> Có, hưởng trọn vẹn 100% sự kiện tặng báu vật và nhân đôi Vcoin của VTC Game.\nQ2: Thẻ Vcoin có nạp được cho game ngoài VTC không?\n-> Rất nhiều game mobile và webgame đối tác tại VN chấp nhận thanh toán bằng Thẻ Vcoin.\nQ3: Mua nhầm mệnh giá có được đổi trả không?\n-> Theo quy định bảo mật, thẻ đã xuất mã không thể đổi trả. Quý khách vui lòng kiểm tra kỹ mệnh giá trước khi bấm thanh toán.'
    ),
    (
        5,
        'Gosu Online',
        'Tier 2 (NPH Tầm Trung)',
        '/nap-the-game/gosu',
        'Thẻ Gosu (code: gosu)',
        'https://pay.gosu.vn',
        'Cổng Mua Mã Thẻ Nạp Game Gosu - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Gosu Nạp Cửu Âm Chân Kinh Chiết Khấu Cao | MoMo\nDesc: Mua mã thẻ Gosu nạp Cửu Âm Chân Kinh, Ngạo Kiếm Vô Song, Hải Tặc Đại Chiến nhận mã PIN sau 30 giây. Chiết khấu cao, thanh toán tiện lợi qua MoMo.',
        'Gosu Online là nhà phát hành có cộng đồng game thủ kiếm hiệp và anime trung thành bậc nhất với các tựa game huyền thoại như Cửu Âm Chân Kinh, Ngạo Kiếm Vô Song. Mua Thẻ Gosu qua MoMo giúp người chơi nhận chiết khấu tốt nhất thị trường.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã thẻ Gosu chính hãng từ Gosu Online.\n2. Tỷ lệ quy đổi GOSU coin nguyên gốc, không cắt xén phế.\n3. Thanh toán siêu tốc qua mã QR MoMo hoặc Ví Trả Sau 0% lãi.',
        'Cửu Âm Chân Kinh (Vàng / Xu), Ngạo Kiếm Vô Song (Vàng), Hải Tặc Đại Chiến (Kim Cương), Lục Giới AFK (Tiên Ngọc), Thần Vương Nhất Thế (KNB).',
        'Mệnh giá: 20k (19.4k -> 200 Gosu) | 50k (48.2k -> 500 Gosu) | 100k (96k -> 1.050 Gosu) | 200k (191k -> 2.150 Gosu) | 500k (475k -> 5.500 Gosu) | 1Tr (950k -> 11.200 Gosu). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gosu&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gosu trên Web MoMo và bấm mở NaptheNgay.vn để thanh toán qua QR MoMo.\nBước 2: Truy cập pay.gosu.vn, đăng nhập tài khoản Gosu, chọn Game và Server nhân vật.\nBước 3: Chọn hình thức nạp bằng "Thẻ Gosu", điền Serial và Mã PIN để nhận GOSU coin ngay tức khắc.',
        'Q1: Nạp thẻ Gosu có được cộng dồn điểm VIP không?\n-> Có, toàn bộ mệnh giá nạp đều được tích lũy vào cấp VIP tài khoản Gosu.\nQ2: Thẻ Gosu có thời hạn sử dụng bao lâu?\n-> Mã thẻ có hạn dùng 24 tháng kể từ thời điểm giao dịch thành công.\nQ3: Tôi có thể mua nhiều thẻ Gosu cùng lúc không?\n-> Được, bạn có thể chọn số lượng lên đến 10 thẻ trong 1 lần giao dịch trên NaptheNgay.'
    ),
    (
        6,
        'VGP (VGPlay)',
        'Tier 1 (Đại NPH)',
        '/nap-the-game/vgp',
        'Thẻ VGPlay (code: vgplay)',
        'https://nap.vgp.vn',
        'Cổng Mua Mã Thẻ Nạp Game VGP (VGPlay) - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ VGPlay Nạp Game VGP Chiết Khấu Cao | MoMo\nDesc: Mua mã thẻ VGPlay nạp Kỳ Vương, Thiên Vũ Thần Vương, Ngự Long Kiếm 3D nhận mã sau 30 giây. Chiết khấu cao, giao dịch an toàn tuyệt đối.',
        'VGP là nhà phát hành nổi tiếng với các tựa game tiên kiếm hiệp và cờ tướng trực tuyến hàng đầu Việt Nam như Kỳ Vương, Ngự Long Kiếm 3D. Thẻ VGPlay cung cấp tỷ lệ quy đổi Vxu cao nhất cho cộng đồng game thủ VGP.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã VGPlay chính hãng từ VGP.\n2. Giao mã nhanh trong 30 giây, hiển thị đầy đủ Serial & PIN.\n3. Tiết kiệm 15% - 25% so với nạp trực tiếp trong ứng dụng di động.',
        'Kỳ Vương (Vàng), Thiên Vũ Thần Vương (KNB), Ngự Long Kiếm 3D (Tiên Ngọc), Thanh Vân Kiếm 3D (KNB), Tứ Hoàng Mobile (Kim Cương).',
        'Mệnh giá: 20k (19.4k -> 20 Vxu) | 50k (48.2k -> 50 Vxu) | 100k (96k -> 105 Vxu) | 200k (191k -> 215 Vxu) | 500k (475k -> 550 Vxu) | 1Tr (950k -> 1.150 Vxu). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=vgplay&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ VGPlay trên Web MoMo, bấm mở NaptheNgay.vn để quét QR MoMo thanh toán.\nBước 2: Mở website nap.vgp.vn, đăng nhập tài khoản VGP, chọn tựa game cần nạp.\nBước 3: Chọn phương thức "Thẻ VGPlay", nhập Mã nạp và Serial để nhận Vxu trong 1 phút.',
        'Q1: Vxu dùng để làm gì trong game VGP?\n-> Vxu dùng để quy đổi sang Kim Cương, KNB hoặc kích hoạt các gói thẻ tháng, thẻ tuần ingame.\nQ2: Thẻ VGPlay có an toàn không?\n-> Thẻ được phân phối chính ngạch từ VGP, cam kết không bao giờ bị lỗi khóa nick.\nQ3: Thanh toán qua MoMo có tốn phí dịch vụ không?\n-> Hoàn toàn 0% phí dịch vụ, người dùng còn được giảm giá chiết khấu trực tiếp.'
    ),
    (
        7,
        'VPlay (VTVLive / Truyền Hình Tương Tác VN)',
        'Tier 2 (NPH Đa Nền Tảng)',
        '/nap-the-game/vplay',
        'Thẻ VPlay / Thẻ Gate (code: vplay)',
        'https://nap.vplay.vn',
        'Cổng Mua Mã Thẻ Nạp Game VPlay - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ VPlay Nạp Game VPlay Chiết Khấu Cao | MoMo\nDesc: Mua mã thẻ VPlay nạp Khởi Nguyên Mobile, Phong Ma Đạo Sỹ, Đấu Thần Tuyệt Thế nhận mã tức thì. Chiết khấu hấp dẫn, thanh toán an toàn.',
        'VPlay là nhà phát hành trực thuộc VTVLive với các tựa game nhập vai thế giới mở và tiên hiệp đa nền tảng ấn tượng. Nạp thẻ VPlay qua MoMo giúp người chơi nhận được tỷ lệ quy đổi Vcoin VPlay tối ưu nhất.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã thẻ chuẩn từ VPlay / VTVLive.\n2. Giao mã tức thì, hỗ trợ lưu trữ mã thẻ bảo mật trong ví.\n3. Hưởng đầy đủ khuyến mại sự kiện nạp x2 của nhà phát hành.',
        'Khởi Nguyên Mobile (KNB), Phong Ma Đạo Sỹ (Linh Phù), Đấu Thần Tuyệt Thế (Tiên Ngọc), Chiến Giới 4D (Kim Cương).',
        'Mệnh giá: 20k (19.4k -> 200 VPlay) | 50k (48.2k -> 500 VPlay) | 100k (96k -> 1.050 VPlay) | 200k (191k -> 2.150 VPlay) | 500k (475k -> 5.500 VPlay) | 1Tr (950k -> 11.200 VPlay). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=vplay&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ VPlay trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Mở website nap.vplay.vn, đăng nhập tài khoản, chọn Game và Nhân vật.\nBước 3: Chọn phương thức "Thẻ VPlay" hoặc "Thẻ Gate", nhập Serial và PIN để nhận tiền tệ.',
        'Q1: Game VPlay ngoài thẻ VPlay còn nạp được thẻ gì?\n-> Hầu hết game VPlay hỗ trợ song song Thẻ VPlay và Thẻ Gate.\nQ2: Nạp thẻ qua Web có rẻ hơn trong game không?\n-> Rẻ hơn 20% - 30% so với nạp qua Apple App Store.\nQ3: Hỗ trợ CSKH khi gặp sự cố thế nào?\n-> Hỗ trợ 24/7 qua tổng đài MoMo 1900 5454 41.'
    ),
    (
        8,
        'ADNX Mobile',
        'Tier 2 (Game Kiếm Hiệp/MU)',
        '/nap-the-game/adnx',
        'Thẻ ADNX / Thẻ Gate (code: adnx)',
        'https://nap.adnx.vn',
        'Cổng Mua Mã Thẻ Nạp Game ADNX - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ ADNX Nạp Kiếm Thế ADNX, Lục Địa Loren | MoMo\nDesc: Mua mã thẻ ADNX nạp Kiếm Thế ADNX Mobile, Lục Địa Loren, Tam Quốc ADNX nhận mã sau 30 giây. Chiết khấu cao, giao dịch an toàn 100%.',
        'ADNX nổi tiếng với việc hồi sinh các tựa game huyền thoại tuổi thơ như Kiếm Thế ADNX Mobile và Lục Địa Loren (MU Mobile). Sử dụng thẻ ADNX giúp game thủ nâng cấp trang bị với chi phí tối ưu.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã thẻ chính thức từ ADNX.\n2. Bảo mật tuyệt đối thông tin, không yêu cầu mật khẩu game.\n3. Tiết kiệm chi phí với chiết khấu trực tiếp trừ vào giá mua.',
        'Kiếm Thế ADNX Mobile (Đồng), Lục Địa Loren (Zen / Kim Cương), Tam Quốc ADNX (KNB).',
        'Mệnh giá: 50k (48.2k -> 500 Xu ADNX) | 100k (96k -> 1.050 Xu) | 200k (191k -> 2.150 Xu) | 500k (475k -> 5.500 Xu) | 1Tr (950k -> 11.200 Xu). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=adnx&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ ADNX trên Web MoMo, bấm mở NaptheNgay.vn để quét QR thanh toán.\nBước 2: Mở website nap.adnx.vn, đăng nhập tài khoản ADNX ID, chọn Game và Server.\nBước 3: Chọn phương thức nạp thẻ, dán Serial và PIN để hoàn tất giao dịch.',
        'Q1: Có thể nạp thẻ Gate cho game ADNX được không?\n-> Có, cổng nap.adnx.vn hỗ trợ nạp cả thẻ ADNX và thẻ Gate.\nQ2: Nạp thẻ ADNX có tích lũy mốc nạp đầu không?\n-> Có, kích hoạt 100% gói quà nạp đầu và quà hoàn trả server mới.\nQ3: Quét QR bằng ứng dụng ngân hàng khác được không?\n-> Được, mã QR hỗ trợ chuẩn thanh toán đa năng qua MoMo và ứng dụng ngân hàng.'
    ),
    (
        9,
        'Efun Corp',
        'Tier 2 (Game Võ Lâm)',
        '/nap-the-game/efun',
        'Thẻ Efun / Thẻ Gate (code: efun)',
        'https://nap.efun.vn',
        'Cổng Mua Mã Thẻ Nạp Game Efun - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Efun Nạp JX1 Huyền Thoại Võ Lâm | MoMo\nDesc: Mua mã thẻ Efun nạp JX1 Huyền Thoại Võ Lâm, Chinh Đồ Origin nhận mã trong 30 giây. Chiết khấu cao, nạp thẻ chính hãng an toàn.',
        'Efun Corp là nhà phát hành chuyên sâu các dòng game kiếm hiệp hoài niệm, tiêu biểu là JX1 Huyền Thoại Võ Lâm. Thẻ Efun là công cụ nạp tiền tệ chính yếu giúp game thủ xưng bá giang hồ.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã thẻ sạch xuất từ Efun Corp.\n2. Giao mã tức thì, hỗ trợ sao chép tiện lợi.\n3. Nhận đủ 100% KNB và quà mốc nạp từ NPH.',
        'JX1 - Huyền Thoại Võ Lâm (Kim Nguyên Bảo), Chinh Đồ Origin (Vàng), Võ Lâm Miễn Phí Mobile (KNB).',
        'Mệnh giá: 50k (48.2k -> 50 Xu Efun) | 100k (96k -> 105 Xu) | 200k (191k -> 215 Xu) | 500k (475k -> 550 Xu) | 1Tr (950k -> 1.150 Xu) | 2Tr (1.900k -> 2.350 Xu). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=efun&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Efun trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng MoMo.\nBước 2: Mở website nap.efun.vn, đăng nhập tài khoản Efun, chọn đúng nhân vật môn phái.\nBước 3: Chọn nạp bằng "Thẻ Efun", dán Serial và PIN để nhận KNB trong túi đồ.',
        'Q1: Nạp thẻ Efun có kích hoạt Phi Phong không?\n-> Có, giá trị nạp được tính đầy đủ vào điểm tích lũy kích hoạt Phi Phong.\nQ2: Thẻ Efun có nạp được cho Chinh Đồ Origin không?\n-> Có, thẻ dùng chung cho toàn bộ sản phẩm của Efun.\nQ3: Tôi nhận mã thẻ qua đâu?\n-> Mã hiển thị trực tiếp trên màn hình và gửi về Email dự phòng của bạn.'
    ),
    (
        10,
        'ACE Game',
        'Tier 2 (Game Anime/Nhẫn Giả)',
        '/nap-the-game/ace-game',
        'Thẻ Gate / Thẻ Zing (code: gate)',
        'https://nap.acegame.vn',
        'Cổng Mua Mã Thẻ Nạp Game ACE Game - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Nạp Game ACE Game (Làng Nhẫn Giả, Ngọc Rồng) | MoMo\nDesc: Mua mã thẻ nạp game ACE Game chiết khấu cao, giao mã tức thì. Hỗ trợ nạp Làng Nhẫn Giả, Ngọc Rồng Huyền Thoại an toàn 100%.',
        'ACE Game là nhà phát hành nổi danh trong cộng đồng yêu thích truyện tranh Anime/Manga với các tựa game như Làng Nhẫn Giả, Ngọc Rồng Huyền Thoại. Mua thẻ qua MoMo giúp game thủ chiêu mộ tướng yêu thích với giá tốt nhất.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. Phân phối mã thẻ cào đối tác chính thức.\n2. Chiết khấu trực tiếp, rẻ hơn 20% so với nạp In-App.\n3. Hỗ trợ giao dịch nhanh chóng và an toàn 100%.',
        'Làng Nhẫn Giả (Ryo / Vàng), Ngọc Rồng Huyền Thoại (Ngọc), Ninja Siêu Cấp (Vàng), Huyền Thoại Làng Lá (Kim Cương).',
        'Mệnh giá: 20k (19.4k -> 20k Ingame) | 50k (48.2k -> 50k Ingame) | 100k (96k -> 100k Ingame) | 200k (191k -> 200k Ingame) | 500k (475k -> 500k Ingame). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gate&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gate trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Mở website nap.acegame.vn, đăng nhập tài khoản ACE Game, chọn Server và Nhân vật.\nBước 3: Chọn phương thức nạp thẻ cào, nhập mã và số serial để nhận quà.',
        'Q1: Game ACE Game nạp bằng thẻ nào tốt nhất?\n-> Cổng ACE Game hỗ trợ tốt nhất qua Thẻ Gate và Thẻ Zing.\nQ2: Nạp thẻ có được x2 lần đầu không?\n-> Các mốc nạp đầu trên web đều được hưởng ưu đãi x2 theo quy định NPH.\nQ3: Tôi có cần cung cấp mật khẩu game không?\n-> Tuyệt đối không, bạn chỉ cần nhập mã PIN nạp vào cổng chính thức.'
    ),
    (
        11,
        'VMGE (Visual Mobile Game)',
        'Tier 2 (Game Anime/Manga)',
        '/nap-the-game/vmge',
        'Thẻ Gate / Thẻ Vcoin (code: gate)',
        'https://pay.vmge.vn',
        'Cổng Mua Mã Thẻ Nạp Game VMGE - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Nạp Game VMGE (Siêu Đại Chiến, OP Đại Chiến) | MoMo\nDesc: Mua mã thẻ nạp game VMGE chiết khấu cao, giao mã tức thì trong 30 giây. Hỗ trợ nạp Siêu Đại Chiến, Hơi Thở Mặt Trời an toàn tuyệt đối.',
        'VMGE chuyên phát hành các dòng game mobile Anime/Manga ăn khách như Siêu Đại Chiến, Hơi Thở Mặt Trời. Mua thẻ nạp VMGE trên Web MoMo giúp game thủ tiết kiệm chi phí tối đa.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã thẻ sạch từ đối tác phân phối chính ngạch.\n2. Giao mã PIN và Serial trong 30 giây.\n3. Tiết kiệm 20% - 30% so với nạp qua Apple In-App Store.',
        'Siêu Đại Chiến (Kim Cương), Kho Báu Đại Chiến (Beli / Kim Cương), Hơi Thở Mặt Trời (Ngọc), OP Đại Chiến (Kim Cương).',
        'Mệnh giá: 50k (48.2k -> 500 Kim Cương) | 100k (96k -> 1.050 Kim Cương) | 200k (191k -> 2.150 Kim Cương) | 500k (475k -> 5.500 Kim Cương). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gate&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gate trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng MoMo.\nBước 2: Mở pay.vmge.vn, đăng nhập tài khoản VMGE, chọn Game và Tên nhân vật.\nBước 3: Chọn nạp thẻ cào Gate, nhập thông tin thẻ để nhận Kim Cương ngay lập tức.',
        'Q1: Nạp thẻ qua Web có nhanh hơn nạp trong app không?\n-> Nạp qua Web nhận mã trong 30s và nạp thẳng vào tài khoản mà không bị lỗi trừ tiền treo nạp của App Store.\nQ2: Thẻ Gate có nạp được cho mọi game VMGE không?\n-> Có, 100% game VMGE chấp nhận Thẻ Gate.\nQ3: Tôi thanh toán bằng hình thức nào trên MoMo?\n-> Hỗ trợ Ví MoMo, Thẻ ngân hàng liên kết, Túi Thần Tài và Ví Trả Sau.'
    ),
    (
        12,
        'Thiên Thượng Hỏa',
        'Tier 2 (NPH Tầm Trung)',
        '/nap-the-game/thien-thuong-hoa',
        'Thẻ Gate / Thẻ Zing (code: gate)',
        'https://pay.thienthuonghoa.vn',
        'Cổng Mua Mã Thẻ Nạp Game Thiên Thượng Hỏa - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Nạp Game Thiên Thượng Hỏa Chiết Khấu Cao | MoMo\nDesc: Mua mã thẻ nạp Tree of Savior: Neverland, Nấm Lùn Tiến Lên, Ta Là Quan Lão Gia nhận mã tức thì. Chiết khấu cao, giao dịch an toàn 100%.',
        'Thiên Thượng Hỏa phát hành nhiều tựa game casual và nhập vai đình đám như Nấm Lùn Tiến Lên, Tree of Savior: Neverland. Nạp thẻ qua MoMo là lựa chọn thông thái giúp game thủ tiết kiệm chi phí chơi game.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. Mã thẻ cào chuẩn hóa đối tác.\n2. Chiết khấu trực tiếp minh bạch.\n3. Hỗ trợ giao dịch bảo mật và an toàn 100%.',
        'Tree of Savior: Neverland (Lá Vàng), Nấm Lùn Tiến Lên (Kim Cương), Ta Là Quan Lão Gia (Nguyên Bảo), Tam Quốc Chí - Chiến Lược (Ngọc Bích).',
        'Mệnh giá: 50k (48.2k -> 500 Ngọc) | 100k (96k -> 1.050 Ngọc) | 200k (191k -> 2.150 Ngọc) | 500k (475k -> 5.500 Ngọc) | 1Tr (950k -> 11.200 Ngọc). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gate&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gate trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Mở website nạp chính thức của game, đăng nhập ID tài khoản và chọn nhân vật.\nBước 3: Chọn phương thức Thẻ Gate, điền Serial và PIN để nhận tài nguyên ingame.',
        'Q1: Nấm Lùn Tiến Lên nạp bằng thẻ gì rẻ nhất?\n-> Nạp bằng Thẻ Gate qua Web MoMo giúp tiết kiệm 20-30% so với nạp trong game.\nQ2: Mua thẻ lúc nửa đêm có nhận mã được không?\n-> Hệ thống xuất mã tự động 24/7 trong 30 giây bất kể ngày đêm.\nQ3: Tôi có thể xuất hóa đơn VAT không?\n-> Có, hỗ trợ yêu cầu xuất hóa đơn điện tử hợp lệ.'
    ),
    (
        13,
        'Travellet',
        'Tier 2 (NPH Tầm Trung)',
        '/nap-the-game/travellet',
        'Thẻ Gate / Thẻ Zing (code: gate)',
        'https://nap.travellet.vn',
        'Cổng Mua Mã Thẻ Nạp Game Travellet - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Nạp Game Travellet (Hành Trình AFK, Warpath) | MoMo\nDesc: Mua mã thẻ nạp Hành Trình AFK, Warpath: Huân Chương Chiến Hỏa nhận mã trong 30 giây. Chiết khấu cao, nạp game an toàn chính ngạch.',
        'Travellet là đối tác phát hành các tựa game chiến thuật và nhập vai thế giới nổi tiếng tại Việt Nam như Hành Trình AFK, Warpath. Mua mã thẻ nạp qua MoMo mang lại trải nghiệm tiện lợi và chiết khấu cao.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã thẻ chính hãng an toàn cho tài khoản.\n2. Giao mã nhanh, giao dịch tiện lợi qua QR Code.\n3. Nhận đầy đủ mốc thưởng nạp từ NPH.',
        'Hành Trình AFK (Kim Cương Long), Warpath (Vàng Chiến Lược), Dislyte (Nexus Crystals), Lithas (Kim Cương).',
        'Mệnh giá: 50k (48.2k -> 500 Kim Cương) | 100k (96k -> 1.050 Kim Cương) | 200k (191k -> 2.150 Kim Cương) | 500k (475k -> 5.500 Kim Cương). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gate&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gate trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng MoMo.\nBước 2: Mở cổng nạp chính thức của game Travellet, đăng nhập tài khoản và chọn Server.\nBước 3: Chọn nạp thẻ cào, dán mã thẻ để nhận tài nguyên trong game.',
        'Q1: Hành Trình AFK nạp qua web có bị mất quyền lợi nạp đầu không?\n-> Không, nạp qua web vẫn kích hoạt đầy đủ tướng tặng và gói quà nạp đầu.\nQ2: Mã thẻ mua xong chưa dùng có hết hạn ngay không?\n-> Thẻ có hạn dùng 2 năm kể từ ngày mua.\nQ3: Nếu nhập sai mã thẻ 3 lần thì sao?\n-> Hệ thống tạm khóa 5 phút để bảo vệ, bạn vui lòng kiểm tra lại chính xác Serial và PIN đã lưu trong email/MoMo.'
    ),
    (
        14,
        'FTech (Công Nghệ Gia Đình)',
        'Tier 3 (Game Studio)',
        '/nap-the-game/ftech',
        'Thẻ Gate (code: gate)',
        'https://nap.ftech.vn',
        'Cổng Mua Mã Thẻ Nạp Game FTech - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Nạp Game FTech (3Q Triệu Hoán Sư, Đùn Đùn) | MoMo\nDesc: Mua mã thẻ Gate nạp game FTech chiết khấu cao, giao mã tức thì trong 30 giây. Hỗ trợ nạp 3Q Triệu Hoán Sư, Biệt Đội Đùn Đùn an toàn.',
        'FTech chuyên phát hành các dòng game giải trí vui nhộn và chiến thuật nhẹ nhàng như Biệt Đội Đùn Đùn, 3Q Triệu Hoán Sư. Nạp thẻ qua MoMo giúp người chơi tối ưu chi phí trải nghiệm game.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. Mã thẻ phân phối chính thức.\n2. Giao mã tức thì, chiết khấu trực tiếp.\n3. Hỗ trợ khách hàng chu đáo 24/7.',
        '3Q Triệu Hoán Sư (Kim Cương), Biệt Đội Đùn Đùn (Kim Cương), Loạn Chiến Mobile (Vàng).',
        'Mệnh giá: 20k (19.4k -> 200 KC) | 50k (48.2k -> 500 KC) | 100k (96k -> 1.050 KC) | 200k (191k -> 2.150 KC) | 500k (475k -> 5.500 KC). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gate&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gate trên Web MoMo, mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Mở website nạp game FTech, đăng nhập tài khoản và chọn nhân vật.\nBước 3: Chọn nạp bằng Thẻ Gate, nhập Serial và PIN để nhận tiền tệ.',
        'Q1: Biệt Đội Đùn Đùn nạp bằng thẻ gì?\n-> Nạp bằng Thẻ Gate trên cổng nạp chính thức của FTech.\nQ2: Thẻ Gate mua trên MoMo có đảm bảo sạch không?\n-> Cam kết 100% mã thẻ sạch xuất từ kho thẻ chính thức.\nQ3: Tôi có thể kiểm tra thẻ đã dùng chưa ở đâu?\n-> Kiểm tra trực tiếp trên cổng kiểm tra mã thẻ của NPH hoặc liên hệ CSKH MoMo.'
    ),
    (
        15,
        '3T Online',
        'Tier 3 (Game Studio)',
        '/nap-the-game/3t',
        'Thẻ Gate / Thẻ Vcoin (code: gate)',
        'https://nap.3t.vn',
        'Cổng Mua Mã Thẻ Nạp Game 3T - Chiết Khấu Đến 5%',
        'Title: Mua Thẻ Nạp Game 3T Online Chiết Khấu Cao | MoMo\nDesc: Mua mã thẻ nạp game 3T (Con Đường Sao Băng, Hỗn Độn Đại Lục) nhận mã tức thì trong 30 giây. Chiết khấu cao, giao dịch an toàn tuyệt đối.',
        '3T Online phát hành các tựa game MMORPG fantasy và khoa học viễn tưởng đặc sắc. Mua mã thẻ nạp qua MoMo giúp người chơi tiết kiệm tối đa ngân sách nạp game.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Thẻ chính hãng từ đối tác phát hành.\n2. Giao mã tức thì, sao chép tiện lợi.\n3. Bảo đảm an toàn tuyệt đối cho tài khoản game.',
        'Con Đường Sao Băng (Kim Cương), Hỗn Độn Đại Lục (KNB), Binh Đoàn Z (Vàng).',
        'Mệnh giá: 50k (48.2k -> 500 KC) | 100k (96k -> 1.050 KC) | 200k (191k -> 2.150 KC) | 500k (475k -> 5.500 KC). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=gate&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Gate trên Web MoMo, mở NaptheNgay.vn thanh toán qua MoMo.\nBước 2: Truy cập cổng nạp game 3T, đăng nhập tài khoản và chọn nhân vật.\nBước 3: Chọn nạp thẻ cào, nhập thông tin để hoàn tất.',
        'Q1: Game 3T hỗ trợ những loại thẻ nào?\n-> Hỗ trợ nạp qua Thẻ Gate và Thẻ Vcoin.\nQ2: Có giới hạn số lần nạp trong ngày không?\n-> Không giới hạn số lần nạp.\nQ3: Nếu lỡ tắt tab mua thẻ thì lấy lại mã ở đâu?\n-> Mã thẻ luôn được lưu trong Lịch sử giao dịch App MoMo và gửi qua Email xác nhận.'
    ),
    (
        16,
        'Divine Shop',
        'Đại Lý Thẻ (Aggregator)',
        '/nap-the-game/divine-shop',
        'Thẻ Steam / Thẻ Roblox (code: steam)',
        'https://divineshop.vn',
        'Cổng Mua Thẻ Steam Wallet, Roblox Gift Card - Nhận Mã Sau 30 Giây',
        'Title: Mua Thẻ Steam Wallet, Roblox Gift Card Giá Rẻ | MoMo\nDesc: Mua thẻ Steam Wallet Code, Roblox Gift Card nạp Robux uy tín nhận mã trong 30 giây. Không cần thẻ tín dụng quốc tế, thanh toán MoMo tiện lợi.',
        'Divine Shop là đơn vị phân phối bản quyền game PC và thẻ game quốc tế uy tín hàng đầu tại Việt Nam. MoMo hợp tác mang đến giải pháp thanh toán thẻ Steam Wallet và Robux tiện lợi mà không cần thẻ Visa/Mastercard.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Key và mã thẻ quốc tế chính hãng từ Valve/Roblox.\n2. Giao mã Key 15 ký tự tức thì trên màn hình.\n3. Hỗ trợ kích hoạt và bảo hành đổi trả nếu mã lỗi.',
        'Game PC Steam (Dota 2, CS2, Black Myth: Wukong), Thế giới ảo Roblox (Robux), Discord Nitro.',
        'Mệnh giá Steam: 5 USD (~135k) | 10 USD (~265k) | 20 USD (~525k) | 50 USD (~1.300k). Mệnh giá Robux: 100k (400 Robux) | 200k (800 Robux) | 500k (2.000 Robux).',
        'https://napthengay.vn/?partner=momo&card=steam&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Steam/Roblox trên Web MoMo, mở NaptheNgay.vn thanh toán qua QR MoMo.\nBước 2: Nhận mã Key kích hoạt 15 ký tự trên màn hình hoặc qua Email.\nBước 3: Mở phần mềm Steam (vào Games -> Activate a Product on Steam) hoặc roblox.com/redeem, dán mã Key để nhận số dư ví.',
        'Q1: Mua thẻ Steam có cần tài khoản ngân hàng quốc tế không?\n-> Không cần, bạn có thể thanh toán trực tiếp bằng nguồn tiền MoMo hoặc Ví Trả Sau.\nQ2: Mã Steam Wallet có nạp được cho Store Việt Nam không?\n-> Có, mã tự động quy đổi sang tiền VND theo tỷ giá niêm yết chính thức của Steam.\nQ3: Mua Robux qua MoMo có sợ bị ban nick không?\n-> Tuyệt đối an toàn vì đây là mã Gift Card chính thức từ Roblox Corporation.'
    ),
    (
        17,
        'Garena (Sea Group)',
        'Master Brand (Đại NPH Quốc Dân)',
        '/nap-the-game/garena',
        'Thẻ Garena / Sò (code: garena)',
        'https://napthe.vn',
        'Cổng Mua Mã Thẻ Garena (Sò) - Chiết Khấu Đến 5% Giao Mã 30 Giây',
        'Title: Mua Thẻ Garena Nạp Quân Huy Liên Quân, Kim Cương FF | MoMo\nDesc: Mua mã thẻ Garena chiết khấu cao, nạp Sò, Quân Huy Liên Quân Mobile, Kim Cương Free Fire, FC Online nhận mã trong 30 giây. An toàn 100%.',
        'Garena là nhà phát hành game số 1 Đông Nam Á với các tựa game eSports quốc dân như Liên Quân Mobile, Free Fire, FC Online. Mua thẻ Garena trên Web MoMo là giải pháp nạp thẻ thông thái giúp game thủ tiết kiệm chi phí tối đa.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã Thẻ Garena sạch xuất trực tiếp từ Sea Group.\n2. Nhận ngay Serial và PIN trong 30 giây, nạp thẳng trên napthe.vn.\n3. Tiết kiệm 10% - 30% chi phí so với nạp trực tiếp qua App Store / Google Play.',
        'Liên Quân Mobile (Quân Huy), Free Fire (Kim Cương), FC Online - FO4 (FC / MC), Garena Sò.',
        'Mệnh giá: 20k (19.4k -> 40 Sò / 40 Quân Huy) | 50k (48.2k -> 100 Sò / 105 Quân Huy) | 100k (96k -> 200 Sò / 210 Quân Huy) | 200k (191k -> 400 Sò / 425 Quân Huy) | 500k (475k -> 1.000 Sò / 1.070 Quân Huy). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=garena&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Garena trên Web MoMo, bấm mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Truy cập cổng nạp chính thức napthe.vn, đăng nhập tài khoản Garena hoặc OpenID game (Liên Quân, Free Fire).\nBước 3: Chọn phương thức "Thẻ Garena", dán Mã PIN vừa mua để nhận Quân Huy/Kim Cương tức thì.',
        'Q1: Nạp thẻ Garena qua MoMo có được cộng dồn huy hiệu VIP Liên Quân không?\n-> Có, nạp trên napthe.vn được tính 100% điểm sự kiện và mốc nạp VIP.\nQ2: Tại sao mua thẻ Garena trên Web MoMo rẻ hơn nạp trong game trên iPhone?\n-> Vì nạp qua Web né được 30% thuế phí trung gian của Apple App Store.\nQ3: Tôi có thể dùng Ví Trả Sau để mua thẻ Garena nạp đua TOP không?\n-> Có, MoMo hỗ trợ nguồn tiền Ví Trả Sau 0% lãi suất giúp bạn nạp thẻ ngay hôm nay và trả tiền sau.'
    ),
    (
        18,
        'VNG Corporation (Zing)',
        'Master Brand (Đại NPH Quốc Dân)',
        '/nap-the-game/zing',
        'Thẻ Zing / Zing Xu (code: zing)',
        'https://pay.zing.vn',
        'Cổng Mua Mã Thẻ Zing Xu (VNG) - Chiết Khấu Đến 5% Giao Mã 30 Giây',
        'Title: Mua Thẻ Zing Xu Nạp Võ Lâm, Tốc Chiến, Valorant | MoMo\nDesc: Mua mã thẻ Zing chiết khấu cao nạp Võ Lâm Truyền Kỳ, Tốc Chiến, Gunny, Valorant nhận mã sau 30 giây. Thanh toán tiện lợi, an toàn 100%.',
        'VNG Corporation là tập đoàn công nghệ và nhà phát hành game hàng đầu Việt Nam với các thương hiệu đình đám như Võ Lâm Truyền Kỳ, LMHT Tốc Chiến, Valorant. Thẻ Zing Xu là phương thức nạp truyền thống tiện lợi và an toàn nhất cho toàn bộ game VNG.\n\n3 Cam Kết Thương Hiệu MoMo:\n1. 100% Mã Thẻ Zing chính ngạch từ VNG.\n2. Giao mã PIN và Serial trong 30 giây sau khi quét QR.\n3. Hưởng đầy đủ khuyến mại sự kiện nạp x2 và quà VIP của VNG.',
        'Võ Lâm Truyền Kỳ Mobile (Nguyên Bảo), Tốc Chiến (Wild Cores), Valorant (VP), Gunny Origin (Xu), Thiên Long Bát Bộ (KNB).',
        'Mệnh giá: 20k (19.4k -> 200 Zing Xu) | 50k (48.2k -> 500 Zing Xu) | 100k (96k -> 1.050 Zing Xu) | 200k (191k -> 2.150 Zing Xu) | 500k (475k -> 5.500 Zing Xu) | 1Tr (950k -> 11.200 Zing Xu). Chiết khấu 3.0% - 5.0%.',
        'https://napthengay.vn/?partner=momo&card=zing&amount=100000',
        'Bước 1: Chọn mệnh giá Thẻ Zing trên Web MoMo, mở NaptheNgay.vn thanh toán bằng QR MoMo.\nBước 2: Mở website pay.zing.vn, đăng nhập tài khoản Zing ID / Role ID nhân vật.\nBước 3: Chọn phương thức thanh toán "Thẻ Zing", nhập Serial và Mật mã thẻ để hoàn tất nhận tiền tệ ingame.',
        'Q1: Thẻ Zing có nạp được cho Valorant không?\n-> Có, trên cổng pay.zing.vn, bạn chọn game Valorant và nạp bằng Thẻ Zing để đổi sang VP.\nQ2: Thẻ Zing mua trên MoMo có bị trừ chiết khấu khi nạp không?\n-> Không, bạn mua giá rẻ hơn tại MoMo nhưng khi nạp vào VNG vẫn nhận đủ 100% giá trị mệnh giá gốc.\nQ3: Nếu gặp lỗi nạp thì liên hệ ai?\n-> Bạn liên hệ Hotline MoMo 1900 5454 41 hoặc hỗ trợ VNG (hotro.zing.vn) để được tra soát mã thẻ tức thì.'
    )
]

for p in providers_data:
    row += 1
    ws.row_dimensions[row].height = 68
    ws.cell(row, 1, p[0]).alignment = align_center_top
    ws.cell(row, 2, p[1]).alignment = align_left_top
    ws.cell(row, 2, p[1]).font = font_data_bold
    ws.cell(row, 3, p[2]).alignment = align_left_top
    ws.cell(row, 4, p[3]).alignment = align_left_top
    ws.cell(row, 4, p[3]).font = font_code
    ws.cell(row, 5, p[4]).alignment = align_left_top
    ws.cell(row, 6, p[5]).alignment = align_left_top
    ws.cell(row, 7, p[6]).alignment = align_left_wrap
    ws.cell(row, 7, p[6]).font = font_data_bold
    ws.cell(row, 8, p[7]).alignment = align_left_wrap
    ws.cell(row, 9, p[8]).alignment = align_left_wrap
    ws.cell(row, 10, p[9]).alignment = align_left_wrap
    ws.cell(row, 11, p[10]).alignment = align_left_wrap
    ws.cell(row, 12, p[11]).alignment = align_left_wrap
    ws.cell(row, 12, p[11]).font = font_code
    ws.cell(row, 13, p[12]).alignment = align_left_wrap
    ws.cell(row, 14, p[13]).alignment = align_left_wrap
    
    for c in range(1, 15):
        cell = ws.cell(row, c)
        if c != 2 and c != 7 and c != 4 and c != 12:
            cell.font = font_data
        cell.border = thin_border

# Set column widths
col_widths = {
    1: 6,    # STT
    2: 24,   # Provider Name
    3: 16,   # Tier
    4: 24,   # URL
    5: 22,   # Card code
    6: 25,   # Official URL
    7: 35,   # H1
    8: 38,   # Meta Title & Desc
    9: 45,   # Hero Copy
    10: 32,  # Games
    11: 38,  # Denominations
    12: 38,  # Target CTA URL
    13: 40,  # 3-Step Guide
    14: 38   # FAQs
}
for col_idx, width in col_widths.items():
    col_letter = get_column_letter(col_idx)
    ws.column_dimensions[col_letter].width = width

# -------------------------------------------------------------------------
# UPDATE README SHEET
# -------------------------------------------------------------------------
ws_readme = wb['Readme']

# Update row 48 to remove "sàn" -> "toàn Website"
r48_val = ws_readme.cell(48, 2).value
if r48_val and 'toàn bộ Search Volume sàn' in r48_val:
    ws_readme.cell(48, 2).value = r48_val.replace('toàn bộ Search Volume sàn', 'toàn bộ Search Volume trên toàn Website')
    print('Fixed "sàn" in Readme row 48!')

# Check if Provider Subpages is mentioned in Project Management Docs (rows 10-20)
found_doc = False
insert_row = 16
for r in range(11, 21):
    val = ws_readme.cell(r, 1).value
    if val and 'Provider' in str(val):
        found_doc = True
        break
    if val and 'Kiến Trúc Điều Hướng' in str(val):
        insert_row = r + 1

if not found_doc:
    # Insert new row in Project Management Docs
    ws_readme.insert_rows(insert_row)
    ws_readme.cell(insert_row, 1, 'Quy Chuẩn Subpage Từng Provider (Structure & Content)')
    ws_readme.cell(insert_row, 1).font = Font(name='Calibri', size=9, bold=True, color='0F172A')
    ws_readme.cell(insert_row, 2, 'Sheet [Provider Subpages]: Đặc tả cấu trúc 7 Modules On-Page và bộ nội dung mẫu chuẩn Brand Guideline cho 18 NPH trọng điểm')
    ws_readme.cell(insert_row, 2).font = Font(name='Calibri', size=9, color='334155')
    print(f'Added Provider Subpages entry to Readme at row {insert_row}!')

# Save workbook
wb.save('05_HUBS/game-hub-roadmap.xlsx')
print('SUCCESS: Added "Provider Subpages" sheet and updated Readme in 05_HUBS/game-hub-roadmap.xlsx!')

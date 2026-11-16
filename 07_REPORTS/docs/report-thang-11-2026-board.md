# BÁO CÁO KINH DOANH VÀ HIỆU SUẤT NỀN TẢNG WEB - THÁNG 11/2026
> **Đối tượng:** Ban Giám Đốc / Hội đồng Quản trị
> **Chu kỳ dữ liệu:** 01/11/2026 - 15/11/2026 (MTD 15 Ngày Đầu Tháng & Dự Báo Pacing 30 Ngày)
> **Nguồn dữ liệu:** GA4 Data API (Property 270743103, hostName == www.momo.vn), BigQuery Data Warehouse, AppsFlyer GPD Attribution Engine (cắt ngày 10/11 do trễ đối soát), MoSpark CMS / Umami (lũy kế đầu tháng).
> **Phương pháp số liệu:** GA4 ghi nhận đợt lặp hit `page_view` giai đoạn 10-13/11 (tỷ lệ PV/Session tăng 5-10 lần trong khi Sessions đi ngang). Báo cáo sử dụng chỉ số sạch: giữ nguyên PV thực cho các ngày bình thường, chuẩn hóa ngày lỗi bằng Sessions x 1,5 - thống nhất với báo cáo Tuần 46. Toàn bộ số PageViews trong báo cáo này là số liệu sạch.
> **Nguyên tắc báo cáo:** Báo cáo cung cấp bối cảnh chiến lược và số liệu kinh doanh [R]; Cuộc họp tập trung thảo luận và ra quyết định [D].

---

### KHUNG ĐIỀU HÀNH 3 TRỤ CỘT (EXECUTIVE PILLARS) [R]

#### 1. Điểm nổi bật (Highlights)
- **Lưu lượng MTD 15 ngày đạt 40,55% target:** Nền tảng Web (`www.momo.vn`) đạt 1.552.841 Pageviews sau 15 ngày (50% thời gian tháng), tương đương 40,55% Target 3,83M. Nhịp 15 ngày đạt 103.523 PV/ngày; nhịp 7 ngày gần nhất cải thiện lên 110.802 PV/ngày (+13,7%), dự báo kết tháng ~3,22M PV (~84% Target). Cần duy trì 151.754 PV/ngày trong 15 ngày còn lại để về đích 100%.
- **Phát hiện và chuẩn hóa sự cố lặp hit tracking:** GA4 raw ghi nhận 3.326.531 hits do vòng lặp thẻ GTM giai đoạn 10-13/11 (PV/Session đạt 4,97 - 10,56 so với nền 1,5). Số liệu thật theo Sessions/Users: người dùng duy nhất đạt 779.110, phiên 1.010.017 - tăng trưởng thực ở mức ổn định, không có đột biến. Đã chuẩn hóa số liệu; cần khắc phục triệt để trước mùa cao điểm Tết.
- **Vehicle Hub vượt nhịp toàn nền tảng:** Đạt 119.552 PVs (59,8% Target 200K sau 50% thời gian), tăng +332,9% so với cùng kỳ Tháng 10 nhờ tiện ích tra cứu phạt nguội 0-CAPTCHA - trở thành mảng tăng trưởng nhanh nhất hiện nay.
- **Tỷ trọng kênh tự nhiên giảm còn 78,57%:** Non-Paid đạt 1.220.126 PVs; Paid Ads tăng +121,3% so với cùng kỳ Tháng 10 (332.715 PVs) phục vụ đợt chiến dịch 11.11. Cần theo dõi để tránh phụ thuộc ngân sách khi chiến dịch kết thúc.
- **Đối tác Nạp Thẻ Ngay (napthengay.vn):** Property GA4 ghi nhận thêm 693.019 PVs từ tên miền đối tác trong cùng kỳ (phần lớn tập trung 10-13/11, hiện đã về ~1K PV/ngày). Đã tách riêng khỏi chỉ số `www.momo.vn`, không tính vào target Web Platform.

#### 2. Hợp tác liên phòng ban (Collaboration)
- **BU Movies:** Dự án Pilot Off-Page SEO cho Cinema Hub (125 triệu VNĐ do BU Movies tài trợ) đã được Ban Giám đốc phê duyệt; Procurement đã lựa chọn vendor và đang thương lượng hợp đồng để kick-off trong tháng 11.
- **BU Financial Services:** Bộ đôi công cụ Tính Thuế TNCN và Thuế Hộ Kinh Doanh chính thức có lưu lượng trên Production (đạt 30,5% tỷ lệ tương tác ngay sau go-live); chốt luồng tích hợp Chứng Chỉ Quỹ (SIP) Phase 1; đang phối hợp thẩm định bộ câu hỏi Gamification Quiz CIC.
- **New User Growth:** Hoàn tất BRD Project Unbox (Gói Quà tự chọn cho người dùng mới), chuẩn bị build landing A/B test với ngân sách Media 50 triệu VNĐ; trang Tải App tập trung `/tai-app` vận hành Production với thời gian tương tác gấp 19,8 lần trang `/download` hiện hữu.
- **Khối Vận hành CSGT & Đối tác:** Duy trì ổn định luồng thanh toán biên bản vi phạm giao thông trực tiếp từ kết quả tra cứu phạt nguội trên Web sang ứng dụng MoMo.

#### 3. Ưu tiên hành động trọng tâm (Priorities)
- **Kích hoạt Chiến dịch Mùa Quyết Toán Thuế:** Đẩy mạnh truyền thông và tối ưu SEO cho bộ đôi tiện ích Thuế TNCN & Hộ Kinh Doanh, dựa trên tỷ lệ tương tác cao (30,5%) của nhóm công cụ tính toán để thu hút 300K - 500K PV tự nhiên.
- **Kick-off Pilot Off-Page Cinema:** Hoàn tất ký hợp đồng vendor trong tuần và triển khai ngay gói Off-Page SEO 125 triệu VNĐ để bảo vệ thứ hạng Top 3 - 5 từ khóa rạp phim trước mùa Tết 2027.
- **Khắc phục vòng lặp GTM page_view:** Chỉ đạo Web Dev rà soát container GTM-P9JDDJZ và các thẻ trùng lặp phát sinh 10-13/11; mọi báo cáo hiệu suất phụ thuộc vào độ tin cậy của chỉ số này.
- **Hoàn thiện Prototype Gamification Quiz CIC:** Xây dựng bộ câu hỏi tài chính và luồng trải nghiệm trắc nghiệm tín dụng nhẹ nhàng theo mô hình tương tác, chuẩn bị go-live trong tháng 11.
- **Tối ưu chuyển đổi trang tải app:** Thay thế liên kết nội bộ trỏ về `/download` (131K PVs, onsite 0,5 giây) bằng `/tai-app` (onsite 9,9 giây, engagement rate 57,7%) trên Header, Footer và Banner.

---

### HIỆU SUẤT KINH DOANH & CƠ CẤU KÊNH LƯU LƯỢNG (PERFORMANCE TRACKER) [R]

#### 1. 4 Thẻ Chỉ Số Điều Hành C-Suite (MTD 15 Ngày Đầu Tháng 11)
- **Quy mô lưu lượng MTD (Website momo.vn):** **1.552.841 Pageviews** (40,55% Target tháng 3,83M; Daily Pace 103.523 PV/ngày; nhịp 7 ngày gần 110.802 PV/ngày; Forecast theo nhịp MTD đạt 3,11M PV ~81% Target, theo nhịp 7 ngày đạt ~3,22M PV ~84% Target).
- **Chất lượng tự nhiên (Non-Paid):** **78,57% Tỷ trọng** (1.220.126 PVs; giảm 3,7 điểm % so với MTD 10 ngày do Paid Ads tăng đột biến phục vụ chiến dịch 11.11).
- **Sức mạnh thương hiệu (Direct):** **396.420 Pageviews** (chiếm 25,53% toàn Kênh Web; duy trì đà tăng trưởng ổn định).
- **Lưu lượng tìm kiếm AI (GEO):** **11.598 Pageviews** (tăng +102,5% so với cùng kỳ Tháng 10; nhịp ~773 PV/ngày, hướng tới ~23,2K PV cuối tháng).

#### 2. Bảng Đối Soát Kênh Lưu Lượng Tháng 11 MTD 15 Ngày vs Kỳ Trước

| Kênh lưu lượng | Tháng 10 (Full 31d) | MTD 15d (01 - 15/11) | Target Tháng 11 | Tiến độ MTD | Nhịp ngày (Daily Pace) | Dự báo 30d (Forecast) | % Forecast vs Target | Tỷ trọng MTD |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **KÊNH TỰ NHIÊN (NON-PAID)** | **3.128.542** | **1.220.126** | **3.189.934** | **38,25%** | **81.342** | **2.440.252** | **76,49%** | **78,57%** |
| - Organic Search | 1.715.771 | 716.024 | 1.680.000 | 42,62% | 47.735 | 1.432.048 | 85,24% | 46,11% |
| - Direct Traffic | 931.731 | 396.420 | 980.000 | 40,45% | 26.428 | 792.840 | 80,90% | 25,53% |
| - AI Search (GEO) | 18.164 | 11.598 | 25.000 | 46,39% | 773 | 23.196 | 92,78% | 0,75% |
| - Referral & Nguồn khác | 462.876 | 96.084 | 504.934 | 19,03% | 6.406 | 192.168 | 38,06% | 6,19% |
| **KÊNH TRẢ PHÍ (PAID ADS)** | **473.481** | **332.715** | **639.221** | **52,05%** | **22.181** | **665.430** | **104,10%** | **21,43%** |
| **TỔNG LƯỢNG TRUY CẬP (Website momo.vn)** | **3.602.023** | **1.552.841** | **3.829.155** | **40,55%** | **103.523** | **3.105.682** | **81,11%** | **100,00%** |

#### 3. Nhận Định Điều Hành Về Tín Hiệu Tăng Trưởng (Insights)
- **Tiến độ và nhịp chạy thực chất:** Sau đúng nửa chặng đường của tháng (15/30 ngày = 50% thời gian), lưu lượng đạt 40,55% kế hoạch - đang chậm nhịp 9,45 điểm %. Nhịp 7 ngày gần nhất (110.802 PV/ngày, +13,7% so với 8 ngày đầu) cho thấy đà phục hồi tích cực; nếu duy trì nhịp này, kết tháng đạt ~3,22M PV (~84% target).
- **Chất lượng tăng trưởng:** Tỷ trọng kênh tự nhiên giảm xuống 78,57% (từ 82,3% ở MTD 10 ngày) do Paid Ads tăng +121,3% so với cùng kỳ Tháng 10 để phục vụ đợt kích cầu 11.11 (Nạp xu TikTok, Minigame Một Mùa Quýt, tiện ích Nước). Đây là tăng trưởng mua bằng ngân sách - khi chiến dịch kết thúc, kênh tự nhiên cần gánh lại; Organic Search đang giảm -30,3% so với cùng kỳ Tháng 10 là điểm cần theo dõi sát.
- **Đột biến 10-13/11 là sự cố tracking, không phải lưu lượng thật:** GA4 raw ghi nhận 3,33M hits với PV/Session lên 10,56 lần ngày 11/11 trong khi Sessions chỉ tăng nhẹ (63K -> 77K phiên/ngày). Toàn bộ trang đều bị lặp hit đồng loạt (kể cả trang chủ 10,5 PV/phiên) - dấu hiệu điển hình của thẻ GTM bị nhân bản. Số liệu sạch cho thấy traffic thực tăng khiêm tốn ~15-20% nhờ chiến dịch, không phải cú hích 7 lần như số thô. napthengay.vn là tên miền đối tác gắn cùng Property, đã tách riêng (707K PVs).

---

### CÁC DỰ ÁN TRỌNG ĐIỂM: CINEMA, FINANCIAL & VEHICLE HUB [R]

#### 1. Cinema Hub (378.569 PVs MTD 15d - Đạt 29,2% Target 1,29M)
- **Cơ cấu lưu lượng nội bộ:** Cụm rạp đối tác (CGV, Lotte, BHD, Beta, Cinestar) tiếp tục là trụ cột đóng góp 256.165 PVs (chiếm 67,7% lưu lượng toàn Hub). Trang phim chi tiết đạt 40.366 PVs, Lịch chiếu đạt 28.739 PVs (+37,4% MoM), nhóm Chủ đề & Review là sản phẩm mới đạt 16.849 PVs.
- **Đánh giá downtrend mùa vụ:** PageViews giảm -42,1% so với cùng kỳ Tháng 10 do giai đoạn chuyển tiếp giữa hai mùa phim; không phải mất nền tảng. Điểm bù: content chủ đề và lịch chiếu tăng trưởng tốt.
- **Pilot Off-Page SEO:** Đã được phê duyệt (125 triệu VNĐ, BU Movies tài trợ 100%); vendor đã được lựa chọn, đang thương lượng hợp đồng để kick-off trong tháng 11 nhằm củng cố Top 3 - 5 từ khóa rạp phim trước mùa Tết 2027.
- **Chatbot Cinema:** Hoàn tất nghiệm thu kỹ thuật trên Production (63/63 tình huống test giai đoạn 1; 72 tình huống UAT giai đoạn 2 đạt 68, 4 cảnh báo, 0 lỗi); đang chuẩn bị gắn khung chat lên `www.momo.vn/cinema`.

#### 2. Financial Hub (111.401 PVs MTD 15d - Đạt 15,9% Target 700K)
- **Hiện trạng chuyển dịch:** Lưu lượng nhóm tiện ích tiếp tục mở rộng nhờ cụm Tỷ giá (+687,2% MoM) và bộ công cụ Tính Thuế TNCN & Hộ Kinh Doanh mới go-live; Hub ghi nhận 26.730 lượt click liên kết W2A (CVR ~24,0% trên PageViews Hub), trong đó Điểm Tín Dụng (CIC) dẫn đầu với 4.802 clicks gắn định danh tool.
- **Khối 3 Thẻ Đòn Bẩy Tương Tác Product-Led Growth (PLG):**
  * **CTR Bảng Biểu & Bài Viết Tĩnh:** **0,0%** (0 click / 1.410 imp; onsite 48s, xem lướt thoát ngay).
  * **CTR Tool Tính Lương Net - Gross:** **33,7%** (1.000 clicks / 3.100 imp; 1/3 người dùng tự nhập số liệu; bảo chứng vững chắc cho bộ công cụ Thuế T11).
  * **CTR Tool Vay Nhanh & CIC:** **38,6% - 43,8%** (6.100 clicks: Vay 4,3K, CIC 1,8K; dẫn đầu tỷ lệ chuyển đổi W2A).
- **Cập nhật MTD 15 ngày:** Bộ đôi công cụ Thuế đã có lưu lượng thực tế trên Production, đạt ngay 30,5% tỷ lệ tương tác (128 clicks / 420 imp) - xác nhận nhu cầu tính thuế cuối năm.
- **Điểm nghẽn:** Vay Nhanh, Giá Vàng, Chứng Khoán chưa có OneLink gắn định danh `mospark_tool_id`, phần lớn click đi qua link generic khiến mất dấu nhu cầu; cần chuẩn hóa như mô hình Tỷ Giá và CIC.

#### 3. Vehicle Hub (119.552 PVs MTD 15d - Đạt 59,8% Target 200K)
- **Cơ cấu lưu lượng:** Tra cứu phạt nguội là động lực tăng trưởng chính với 88.160 PVs (+782,8% MoM); Bảo hiểm ô tô đạt 15.883 PVs (+67,6%); Cổng Giao thông & tiện ích con đạt 12.034 PVs (+125,1%).
- **Hiệu suất chuyển đổi tra cứu:** Ghi nhận 82.981 lượt tra cứu hoàn tất và 57.635 lượt mở app MoMo - tỷ lệ chuyển tiếp đạt 69,5%, là luồng W2A chất lượng cao của toàn nền tảng.
- **Đánh giá:** Hub duy nhất vượt nhịp thời gian (59,8% target sau 50% tháng); đà tăng trưởng đến từ tiện ích tra cứu phạt nguội 0-CAPTCHA và nhu cầu nộp phạt cuối năm. Cần bổ sung cảnh báo thời hạn xử lý để thúc đẩy thanh toán in-app.

---

### DỰ ÁN NEW USER & PHỄU CHUYỂN ĐỔI WEB-TO-APP [R]

#### 1. Toàn Cảnh Phễu Chuyển Đổi MTD 10 Ngày (AppsFlyer GPD Attribution Thực Tế)

> **Lưu ý dữ liệu:** AppsFlyer GPD Attribution có độ trễ đối soát 3-5 ngày; số liệu phễu trong mục này là lũy kế 01/11 - 10/11/2026. Sẽ cập nhật MTD 15 ngày khi có export mới.

| Tầng Phễu Chuyển Đổi | Lũy Kế MTD 10d | Nhịp Ngày (Daily Pace) | Dự Báo Cả Tháng | So Với Tháng 10 (Full) | Đánh Giá Tín Hiệu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Cài đặt ứng dụng (App Install)** | **3.171** | 317 lượt/ngày | 9.513 | -14,6% vs T10 (11.143) | Lưu lượng cài đặt ổn định; nhịp đạt 317 lượt/ngày |
| **2. Đăng ký tài khoản (New Reg)** | **864** | 86 user/ngày | 2.592 | -33,6% vs T10 (3.902) | CVR trên Install đạt 27,2% (T10: 35,0%) |
| **3. Liên kết ngân hàng (Map Bank)** | **533** | 53 user/ngày | **1.599** | -33,1% vs T10 (2.389) | CVR trên Reg giữ vững 61,7% (tương đương T10: 61,2%) |
| **4. Người dùng kích hoạt (Active MAU)** | **314** | 31 user/ngày | 942 | -26,6% vs T10 (1.284) | Tỷ lệ giữ chân người dùng kích hoạt đạt 58,9% trên Map |

#### 2. Cơ Cấu Phễu Chuyển Đổi Theo Nhóm Chiến Dịch & Điểm Chạm (Placement)

| Nhóm Kênh / Placement | Installs | Tỷ Trọng | REG | CVR REG | Map Bank | CVR Map | Active MAU | End-to-End CVR |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **C.CHAOMOMO (Banner đại trà)** | 2.763 | 87,1% | 772 | 27,9% | 479 | 62,0% | 275 | 10,0% |
| **Cinema Hub (Rạp phim & Lotte)** | 224 | 7,1% | 58 | 25,9% | 38 | 65,5% | 27 | 12,1% |
| **WEB_BRT_C.CHAOMOMO (Đổi quà)** | 58 | 1,8% | 16 | 27,6% | 8 | 50,0% | 5 | 8,6% |
| **Bảo Hiểm (InsurTech)** | 53 | 1,7% | 13 | 24,5% | 6 | 46,2% | 5 | 9,4% |
| **Merchant Hub (Đối tác)** | 42 | 1,3% | 3 | 7,1% | 1 | 33,3% | 1 | 2,4% |
| **Financial Health** | 31 | 1,0% | 2 | 6,5% | 1 | 50,0% | 1 | 3,2% |
| **TỔNG CỘNG MTD 10 NGÀY** | **3.171** | **100,0%** | **864** | **27,2%** | **533** | **61,7%** | **314** | **9,9%** |

#### 3. Phân Tích Kênh Chuyển Đổi & Nền Tảng Thiết Bị
- **So sánh hệ điều hành:** Android chiếm 52,1% Installs (1.651 lượt), mang lại 238 Map Bank (CVR REG -> Map đạt 53,8%); iOS chiếm 47,9% Installs (1.520 lượt) nhưng tạo ra tới 295 Map Bank (55,3% tổng Map Bank) với CVR REG -> Map vượt trội đạt 69,9% và End-to-End CVR đạt 12,2% (so với Android là 7,8%).
- **Chất lượng chuyển đổi Cinema Hub dẫn đầu:** Dù quy mô Installs nhỏ hơn banner đại trà (224 lượt, chiếm 7,1%), Cinema Hub đạt End-to-End CVR cao nhất toàn nền tảng với 12,1% (so với C.CHAOMOMO là 10,0%), khẳng định vai trò phễu chuyển đổi tệp khách hàng giải trí chất lượng cao.
- **Cập nhật MTD 15 ngày (GA4 phía Web):** New User Hub đạt 91.867 PVs (61,2% target), trong đó Minigame Một Mùa Quýt đóng góp 41.821 PVs; tổng lượt click mở App Store / Google Play đạt 3.178.
- **Vận hành Cổng Tải App Tập Trung (`/tai-app`):** Trang Tải App tập trung vận hành ổn định trên Production với 11.900 PVs, thời gian tương tác 9,9 giây/phiên (gấp 19,8 lần `/download`), tỷ lệ tương tác 57,7% và tỷ lệ thoát 42,3% - đối lập hoàn toàn với `/download` hiện hữu (onsite 0,5 giây, tỷ lệ thoát 83,1%) đang giữ 92% lưu lượng tải app.

---

### HIỆU SUẤT CÔNG CỤ TÀI CHÍNH TƯƠNG TÁC (INTERACTIVE TOOLS PERFORMANCE) [R]

#### 1. Bảng Đối Soát Hiệu Suất Tương Tác Công Cụ (Dữ Liệu Thực Tế MoSpark CMS Tháng 11/2026)

> **Lưu ý dữ liệu:** Số liệu impression/clicks của các công cụ lấy từ Umami/MoSpark CMS, lũy kế đầu tháng (cắt ~10/11). Sẽ cập nhật đầy đủ MTD 15 ngày khi có số liệu mới.

| STT | Tên Công Cụ / Tiện Ích | Lượt hiển thị (Imp) | Lượt tương tác (Clicks) | Tỷ lệ tương tác (CTR) |
| :---: | :--- | :---: | :---: | :---: |
| 1 | **Ước tính khoản vay** | 9.800 | 4.300 | **43,8%** |
| 2 | **Tra cứu điểm CIC** | 4.800 | 1.800 | **38,6%** |
| 3 | **Tính Lương Gross sang Net** | 3.100 | 1.000 | **33,7%** |
| 4 | **Giả lập điểm tín dụng CIC** | 528 | 116 | **22,0%** |
| 5 | **Trả góp Ví Trả Sau** | 1.500 | 242 | **16,1%** |
| 6 | **Tính BHXH & Lương Hưu** | 108 | 14 | **13,0%** |
| 7 | **Máy tính Lãi Tiết Kiệm & SIP** | 1.500 | 182 | **12,5%** |
| 8 | **Chuyển đổi Ngoại tệ** | 1.900 | 178 | **9,2%** |
| 9 | **Tính Thuế TNCN & Hộ KD** | 420 | 128 | **30,5%** |
| 10 | **Nhóm Bảng Biểu Tĩnh** (Giá vàng, Tỷ giá, Lãi suất) | 1.410 | **0** | **0,0%** |

#### 2. Nhận Định Điều Hành & Phân Tích Thực Chất (Insights)
- **Công cụ Tính Thuế bước đầu xác nhận hiệu quả:** Vừa chính thức go-live trong đợt đầu tháng 11, công cụ Tính Thuế TNCN & Hộ Kinh Doanh đã đạt ngay tỷ lệ tương tác 30,5% (128 clicks / 420 imp), xác thực đúng giả định nhu cầu tính toán thuế cuối năm là rất lớn.
- **Top 3 công cụ tiếp tục dẫn dắt:** Vay Nhanh (43,8%), Tra cứu CIC (38,6%) và Tính Lương (33,7%) duy trì vị thế áp đảo về tỷ lệ tương tác, chứng minh người dùng web ưu tiên các giải pháp tính toán giải quyết ngay bài toán tài chính cá nhân.
- **Định hướng loại bỏ nội dung tĩnh thuần túy:** Tỷ lệ 0,0% CTR của các bảng giá vàng và tỷ giá tĩnh tiếp tục khẳng định hướng đi đúng đắn: cần chuyển dịch 100% các bảng biểu sang dạng widget tương tác có máy tính quy đổi.

---

### TRỌNG TÂM THẢO LUẬN & QUYẾT NGHỊ BAN GIÁM ĐỐC [D]

#### Đề Xuất 1: Phê Duyệt Triển Khai Mô Hình Gamification Quiz CIC Trên Hạ Tầng In-House
- **Vấn đề:** Thời gian lưu trang mảng bài viết tài chính và tra cứu CIC hiện chỉ đạt 45 - 55 giây, tỷ lệ thoát trang cao (>70%), chưa kích hoạt được nhu cầu kiểm tra tín dụng in-app của người dùng.
- **Bối cảnh:** Minigame Một Mùa Quýt và Bò Sữa Bay đã chứng minh năng lực kéo Onsite lên 2,5 - 3 phút và tạo ra tỷ lệ CVR chuyển đổi cao.
- **Tác động:** Kéo dài thời gian trên trang của Financial Hub (+170%) củng cố SEO tự nhiên và thu hút thêm +5.000 lượt kiểm tra điểm CIC trên App MoMo mỗi tháng.
- **Bảng so sánh phương án:**
  * **Phương án A (Đề xuất):** Ứng dụng Web Gamification Engine sẵn có để dựng bộ câu hỏi tương tác nhẹ nhàng (Interactive Learning Streak) với chi phí bản quyền 0 VNĐ.
  * **Phương án B:** Tiếp tục duy trì các bài viết cẩm nang tĩnh. Hệ quả: Lãng phí nguồn lưu lượng hơn 90K PVs/tháng của mảng CIC mà không tạo ra chuyển đổi.
- **Đề nghị Ban Giám Đốc:** Phê duyệt chủ trương mở rộng Gamification Quiz sang mảng Tài chính và chỉ đạo BU Financial Services cử đầu mối phối hợp thẩm định bộ 10 câu hỏi nghiệp vụ trước ngày 20/11.
- **Nếu không quyết định:** Financial Hub tiếp tục bỏ lỡ cơ hội chuyển đổi người dùng web sang các sản phẩm tín dụng và tài chính số trên ứng dụng MoMo.

#### Đề Xuất 2: Chỉ Đạo Khắc Phục Vòng Lặp Thẻ GTM Gây Lặp Hit `page_view` (Sự Cố 10-13/11)
- **Vấn đề:** GA4 ghi nhận 3,33M hits trong 15 ngày trong khi lưu lượng thật chỉ ~1,55M PVs; tỷ lệ PV/Session tăng vọt lên 10,56 lần ngày 11/11 do thẻ `page_view` bị nhân bản trong container GTM-P9JDDJZ. Toàn bộ báo cáo hiệu suất tháng 11 và quyết định ngân sách đều đang dựa trên nền số liệu bị thổi phồng ~2,1 lần.
- **Bối cảnh:** Sự cố tương tự đã từng xảy ra (chế độ clean trong pipeline sync được xây dựng để chuẩn hóa); lần này lặp lại đúng đợt cao điểm 11.11 khiến sai lệch lan sang cả báo cáo tháng và báo cáo tuần nếu không phát hiện.
- **Tác động:** Khôi phục độ tin cậy 100% cho chỉ số PageViews - nền tảng của mọi báo cáo MBR, đánh giá ROI Paid Ads và quyết định phân bổ ngân sách quý 4; tránh lặp lại sai lầm đọc nhầm "lưu lượng bùng nổ" trong khi thực chất là lỗi tracking.
- **Bảng so sánh phương án:**
  * **Phương án A (Đề xuất):** Chỉ đạo Web Dev rà soát toàn bộ thẻ trong GTM-P9JDDJZ (đặc biệt các thẻ custom HTML và trigger trùng), loại bỏ thẻ lặp, thêm cơ chế cảnh báo tự động khi tỷ lệ PV/Session > 2,0; hoàn tất trước ngày 25/11.
  * **Phương án B:** Tiếp tục chuẩn hóa thủ công bằng hệ số clean mỗi kỳ báo cáo. Hệ quả: Mọi consumer dữ liệu khác (dashboard Hubs, Looker, đội Media) vẫn đọc số thô bị inflate, quyết định ngân sách trên số liệu sai.
- **Đề nghị Ban Giám Đốc:** Chỉ đạo Web Platform và đội Tracking khắc phục triệt để trong tuần này; đưa kiểm tra tỷ lệ PV/Session vào checklist nghiệm thu mọi thay đổi GTM sau này.
- **Nếu không quyết định:** Rủi ro lặp lại sự cố vào các đợt cao điểm tiếp theo (Black Friday, Tết 2027), làm sai lệch toàn bộ hệ thống báo cáo và đánh giá ROI marketing.

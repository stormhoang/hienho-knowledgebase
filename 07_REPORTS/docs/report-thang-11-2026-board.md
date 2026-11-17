# BÁO CÁO KINH DOANH VÀ HIỆU SUẤT NỀN TẢNG WEB - THÁNG 11/2026
> **Chu kỳ dữ liệu:** 01/11/2026 - 16/11/2026 (MTD 16 ngày, 53% thời gian tháng) và dự báo pacing 30 ngày
> **Nguồn dữ liệu:** File `monthly_11_2026_mtd_16d.json` đọc lúc 17/11/2026 13:06 (chuẩn hóa BigQuery DWH SSOT `WEB_L4_EVENT_PAGE_MASTER` & GA4 Data API Property 270743103); AppsFlyer GPD Attribution (cắt 10/11); MoSpark CMS / Umami (lũy kế đến 10/11); `web_performance_tracking.xlsx`.
> **Phương pháp số liệu:** Số PV lấy từ JSON 13:06 ngày 17/11 (2.861.286 PV, khử trùng lặp `event_id`, loại domain đối tác napthengay.vn). Số này thay thế 1.696.417 của lần kéo GA4 www.momo.vn trước đó. Chênh lệch chủ yếu do đổi phạm vi đo, không phải tăng trưởng thực; cần Web Dev xác nhận trước khi công bố.
> **Nguyên tắc báo cáo:** Báo cáo cung cấp bối cảnh chiến lược và số liệu kinh doanh [R]; Cuộc họp tập trung thảo luận và ra quyết định [D].

---

## 1. ĐIỂM NỔI BẬT & ƯU TIÊN TRỌNG TÂM [R]

### 1.1. Điểm nổi bật (Highlights)
- **Lưu lượng MTD 16 ngày đạt 74,7% target:** 2.861.286 Pageviews so với target 3,83M. Nhịp trung bình 178.830 PV/ngày; dự báo kết tháng ~5,36M PV (~140% target). Cần 69.134 PV/ngày trong 14 ngày còn lại, thấp hơn nhịp hiện tại 61%.
- **Vehicle Hub vượt target:** 225.172 PVs, đạt 112,6% target 200K sau 53% thời gian tháng, nhờ tra cứu phạt nguội 0-CAPTCHA (xem Mục 3.3 về target).
- **Cinema Hub đạt 53,5% target:** 693.106 PVs, trong đó cụm trang rạp phim chiếm 67,6% lưu lượng Hub.
- **AI Traffic (GEO) đạt 21.151 PVs,** tiến độ 84,6% target 25K; chiếm 0,74% tổng lưu lượng.

### 1.2. Hợp tác liên phòng ban (Collaboration)
- **BU Movies:** Pilot Off-Page SEO Cinema (125 triệu VNĐ, đã duyệt) đang triển khai với vendor đã chọn; kick-off trong tháng 11.
- **BU Financial Services & Pháp chế:** Đang thẩm định bộ câu hỏi nghiệp vụ cho Quiz CIC, hạn trả kết luận 20/11.
- **Media Team:** Ngân sách 50 triệu VNĐ cho Project Unbox (Gói Quà tự chọn người dùng mới) đã duyệt, chờ Web Platform build landing thử nghiệm A/B.

### 1.3. Ưu tiên hành động trọng tâm (Priorities)
- **Quiz CIC:** Trình Ban Giám Đốc phê duyệt chủ trương trong tuần này để kịp build đón mùa quyết toán thuế cuối năm (Mục 6.2).
- **Cinema Hub:** Kick-off Off-Page SEO trong tháng 11; triển khai cụm trang Lịch chiếu theo tỉnh thành; gắn Chatbot Cinema lên `/cinema`.
- **Vehicle Hub:** Bổ sung cảnh báo thời hạn nộp phạt để thúc đẩy thanh toán in-app sau khi người dùng tra cứu xong.

---

## 2. HIỆU SUẤT NỀN TẢNG & KÊNH LƯU LƯỢNG [R]

### 2.1. 4 Thẻ Chỉ Số Điều Hành
- **Quy mô lưu lượng:** **2.861.286 Pageviews** (74,7% Target tháng 3,83M; nhịp 178.830 PV/ngày; cần 69.134 PV/ngày cho 14 ngày còn lại).
- **Chất lượng tự nhiên (Non-Paid):** **78,51% tỷ trọng** (2.246.310 PVs). Organic Search 1.307.096 PVs (45,68%) là kênh lớn nhất.
- **Kênh trả phí (Paid Ads):** **614.976 PVs** (21,49% tổng).
- **Lưu lượng tìm kiếm AI (GEO):** **21.151 PVs** (0,74% tổng), tiến độ 84,6% target 25K.

### 2.2. Bảng Pageviews Đa Tháng (T7 - T11, nguồn: web_performance_tracking.xlsx)

| Chỉ số | T7/2026 (Full) | T8/2026 (Full) | T9/2026 (Full) | T10/2026 (Full) | T11/2026 (MTD 16d) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| **Total Pageviews** | 3.167.821 | 3.465.363 | 3.950.763 | 3.602.023 | 2.861.286 |
| **Non-Paid** | 2.669.863 | 2.820.824 | 2.753.670 | 3.128.542 | 2.246.310 |
| **Paid** | 497.958 | 644.539 | 1.197.093 | 473.481 | 614.976 |
| **MoM (Pageviews)** | -7,1% vs T6 | +9,4% vs T7 | +14,0% vs T8 | -8,8% vs T9 | - |
| **Target** | - | - | 3.509.044 | 3.665.607 | 3.829.155 |
| **% Target** | - | - | **112,6%** | **98,3%** | **74,7%** |

### 2.3. Phân Tích Nguyên Nhân Gốc & Yếu Tố Mùa Vụ
- **Nhịp hiện tại đủ để về đích:** Lưu lượng đạt 74,7% target sau 53% thời gian tháng. Cần 69.134 PV/ngày trong 14 ngày còn lại, thấp hơn nhịp hiện tại 178.830 PV/ngày. Kết luận này phụ thuộc phạm vi đo mới, cần xác nhận trước khi công bố.
- **Paid tăng mạnh so với lần kéo cũ:** 364.885 → 614.976 PVs. Theo báo cáo, phần tăng gắn với chiến dịch 11.11 và không phải tín hiệu nhu cầu mới [cần xác nhận]. Tiến độ theo target từng nhóm chưa có trong JSON mới, nên chưa so sánh được Non-Paid với Paid.
- **Referral và nguồn khác:** 206.823 PVs (Referral 130.973 + Khác 75.850). Target nhóm này chưa có trong JSON mới; cần kiểm tra tracking trước khi đánh giá tiến độ.
- **So sánh cùng kỳ tháng 10 chưa thực hiện:** Báo cáo tháng 10 chỉ có số 15 ngày, không cùng mốc 16 ngày. Mục này sẽ bổ sung khi có số cùng kỳ 16 ngày.

---

## 3. HIỆU SUẤT CÁC HUB TRỌNG ĐIỂM [R]

### 3.1. Cinema Hub (693.106 PVs - Đạt 53,5% Target 1,29M)
- **Đóng góp quy mô:** Trang rạp phim đóng góp 468.528 PVs (67,6% lưu lượng Hub). Trang phim chi tiết đạt 150.609 PVs (21,7%). Trang chủ và Blog Cinema cộng thêm 71.108 PVs (10,3%).
- **Chất lượng chuyển đổi Web-to-App:** End-to-End CVR 12,1% (số 10 ngày từ AppsFlyer), cao nhất các nguồn Web-to-App.
- **Trang review tương tác và trang diễn viên (GSC 01-15/11 so với 17-31/10):** 4 phim ưu tiên đạt 5.145 click, +671% (Sử Thi Ramayana +2.233%, Ngày Con Còn Mẹ +1.725%, Bò Sữa Bay +478%, Godzilla Trừ Không +398%). Trang /person đạt 399 click, +17,7%. Nguồn báo cáo ghi trang review có traffic gấp 48 lần review thường, chưa kiểm chứng lại.
- **Hành động tiếp theo:** Kick-off Pilot Off-Page SEO 125 triệu VNĐ trong tháng 11; triển khai cụm trang Lịch chiếu theo tỉnh thành; gắn Chatbot Cinema lên `/cinema`; xử lý sự cố API lịch chiếu bị rớt.

### 3.2. Financial Hub (297.482 PVs - Đạt 42,5% Target 700K [cần xác nhận])
- **Số PV: 297.482 (16 ngày, JSON 17/11 13:06).** Cao hơn 68,5% so với mốc 176.529 đã thống nhất trước đó (GA4 www.momo.vn), nên cần chốt lại trước khi công bố. W46 (121.938) và báo cáo 14 ngày (151.548) dùng phạm vi cũ, không dùng cho báo cáo tháng.
- **Tỷ giá (GSC 01-15/11 so với 17-31/10):** 24 trang tỷ giá đạt 2.192 click (+101%), hiển thị 1.416.535 (+84,8%). Ngoại tệ sang VND: JPY +490%, THB +150%, CNY +91%, KRW +46%. Báo cáo 14 ngày ghi 151.548 PV và 23.130 click OneLink về app, không dùng cho báo cáo tháng; số PV tháng là 297.482 (16 ngày, xem trên).
- **Công cụ tương tác:** Bộ đôi Thuế TNCN và Hộ KD đạt 30,5% tỷ lệ tương tác sau go-live. CIC dẫn đầu lượt click OneLink toàn Hub (số 15 ngày).
- **Hành động tiếp theo:** Trình phê duyệt Quiz CIC (Mục 6.2); xác nhận target tháng 11 và định nghĩa Hub; chuẩn hóa OneLink cho Vay Nhanh, Giá vàng, Chứng khoán.

### 3.3. Vehicle Hub (225.172 PVs - Đạt 112,6% Target 200K [cần xác nhận])
- **Target:** JSON 17/11 ghi 100K (tương đương 225,2%); báo cáo dùng 200K theo chốt target T11. Cần thống nhất trước khi công bố.
- **Động lực tăng trưởng:** Tra cứu phạt nguội 0-CAPTCHA là điểm sáng chính. Ở báo cáo 15 ngày ghi nhận 88.160 PVs, 82.981 lượt tra cứu hoàn tất và 57.635 lượt mở app (69,5%).
- **Hành động tiếp theo:** Bổ sung cảnh báo thời hạn nộp phạt để thúc đẩy thanh toán in-app.

### 3.4. New User Hub (167.037 PVs - Đạt 55,7% Target 300K)
- **Minigame & chiến dịch:** Một Mùa Quýt là nội dung chính; Project Unbox (Gói Quà tự chọn) đã hoàn tất tài liệu nghiệp vụ, chờ build thử nghiệm A/B với ngân sách Media 50 triệu VNĐ.
- **Mục target:** Chốt target 300K (thay mốc khoảng 150K ở báo cáo 15 ngày); tiến độ 55,7% sau 53% thời gian tháng, cần 9.497 PV/ngày trong 14 ngày còn lại.

---

## 4. PHỄU CHUYỂN ĐỔI WEB-TO-APP (APPSFLYER GPD) [R]

### 4.1. Toàn Cảnh Phễu Chuyển Đổi Đa Tháng

| Kỳ dữ liệu | Lượt cài app | Đăng ký mới | Liên kết ngân hàng | Người dùng hoạt động | Tỷ lệ đầu-cuối |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Tháng 7 (Full) | 5.242 | 1.682 | 948 | 536 | 10,2% |
| Tháng 8 (Full) | 10.058 | 3.229 | 1.818 | 1.029 | 10,2% |
| Tháng 9 (Full) | 10.501 | 3.569 | 2.276 | 1.328 | 12,6% |
| Tháng 10 (Full) | 11.143 | 3.902 | 2.389 | 1.284 | 11,5% |
| Tháng 11 (lũy kế 10 ngày, cắt 10/11) | 3.171 | 864 | 533 | 314 | 9,9% |

### 4.2. Phễu 10 Ngày & Điểm Nghẽn
- **Chuỗi chuyển đổi:** 3.171 lượt cài -> 864 đăng ký (CVR 27,2%) -> 533 liên kết ngân hàng (CVR 61,7%) -> 314 người dùng hoạt động (CVR 58,9%).
- **Điểm nghẽn Install -> Reg:** CVR 27,2% thấp hơn tháng 10 (35,0%). Cần chẩn đoán chất lượng nguồn cài và luồng ngay sau khi cài app.
- **Theo nguồn chiến dịch:** Cinema Hub dẫn đầu End-to-End CVR 12,1% nhưng chỉ chiếm 7,1% số cài; C.CHAOMOMO chiếm 87,1% số cài với CVR 10,0%. Merchant Hub (2,4%) và Financial Health (3,2%) có chất lượng chuyển đổi thấp nhất.
- **Theo hệ điều hành:** iOS vượt Android về End-to-End CVR, 12,2% so với 7,8%.
- **Cần thống nhất:** Workbook ghi 4.868 cài cho 15 ngày; báo cáo này dùng lũy kế 10 ngày (cắt 10/11). Phải chốt một nguồn trước khi công bố.

---

## 5. HIỆU SUẤT CÔNG CỤ TÀI CHÍNH TƯƠNG TÁC [R]

### 5.1. Bảng Đối Soát Hiệu Suất Công Cụ (Dữ liệu MoSpark CMS, lũy kế đến 10/11)

| STT | Tên Công Cụ / Tiện Ích | Lượt hiển thị | Lượt tương tác | Tỷ lệ tương tác |
| :---: | :--- | :---: | :---: | :---: |
| 1 | Ước tính khoản vay | 9.800 | 4.300 | **43,9%** |
| 2 | Tra cứu điểm CIC | 4.800 | 1.800 | **37,5%** |
| 3 | Tính Lương Gross sang Net | 3.100 | 1.000 | **32,3%** |
| 4 | Giả lập điểm tín dụng CIC | 528 | 116 | **22,0%** |
| 5 | Trả góp Ví Trả Sau | 1.500 | 242 | **16,1%** |
| 6 | Tính BHXH & Lương Hưu | 108 | 14 | **13,0%** |
| 7 | Máy tính Lãi Tiết Kiệm | 1.500 | 182 | **12,1%** |
| 8 | Chuyển đổi Ngoại tệ | 1.900 | 178 | **9,4%** |
| 9 | Tính Thuế TNCN & Hộ KD | 420 | 128 | **30,5%** |
| 10 | Nhóm Bảng Biểu Tĩnh (Giá vàng, Tỷ giá, Lãi suất) | 1.410 | **0** | **0,0%** |

### 5.2. Nhận Định Điều Hành
- **Đối lập rõ giữa bảng tĩnh (0% tương tác) và công cụ tương tác (32,3% - 43,9%):** Người dùng chỉ tương tác khi được cung cấp công cụ tự nhập số liệu.
- **Cơ sở cho Quiz CIC:** Tỷ lệ 37,5% của Tra cứu CIC và 32,3% của Tính lương cho thấy nhu cầu công cụ tài chính tương tác lớn.
- **Việc cần làm:** Thay dần bảng biểu tĩnh bằng widget tương tác; cập nhật số công cụ theo lũy kế 16 ngày khi có export mới.

---

## 6. THEO DÕI ACTION KỲ TRƯỚC & CHỦ ĐỀ THẢO LUẬN BAN GIÁM ĐỐC [R][D]

### 6.1. Chủ đề thảo luận và đề xuất cần Ban Giám Đốc quyết định

**Chủ đề 1: Web Platform Direction 2027** `[D]`

- **Vấn đề:** 2026 mới có 3 Hub live (Cinema, Vehicle, Financial); mục tiêu 2027 là 5+ Hub. SE Team 9 người chỉ đủ cho dedicated build có điều kiện. Web-attributed MAU 1.029/tháng (T8), Organic 50% lưu lượng.
- **Đề xuất:** Dedicated Build cho 2-3 Hub ưu tiên (Cinema, Financial, Vehicle); các Hub còn lại tư vấn SEO/GEO (phương án A). Phương án B: Base Case, chỉ tư vấn, khó đạt mục tiêu install và MAU. Phương án C: dedicated build đồng thời nhiều Hub, SE Team quá tải.
- **Tác động:** Mục tiêu 2027: install 20-30K/tháng, MAU web 5-10K, Organic từ 60%, 5.000+ AI citations, 5+ Hub live.
- **Đề nghị Ban Giám Đốc:** Thống nhất 4 trụ cột 2027 và tiêu chí Scale/Stop cho từng Hub. BU đủ điều kiện (cam kết KPI, ngân sách, RACI) được cấp Growth Case.
- **Hạn:** [cần xác nhận]
- **Nếu không quyết định:** Mặc định Base Case; mục tiêu install và MAU 2027 khó đạt.

**Chủ đề 2: Quiz CIC, cho phép Log in và Legal Policy theo User Flow của Course** `[D]`

- **Vấn đề:** Bảng xếp hạng tháng và lưu tiến độ cần định danh người chơi; concept hiện chưa có bước đăng nhập. Thời gian lưu trang mảng tài chính và tra cứu CIC chỉ 45-55 giây, thoát trang trên 70%.
- **Đề xuất:** Chơi thử không cần đăng nhập; đăng nhập tài khoản MoMo để lưu tiến độ và xếp hạng (phương án A). Phương án B: chơi ẩn danh, không xếp hạng, không đo được chuyển đổi. Phương án C: bắt buộc đăng nhập trước khi chơi, rào cản vào cao.
- **Legal Policy đề xuất:** Điều khoản mô phỏng, không phải đề nghị vay; không dùng dữ liệu CIC thật; CIC và Legal duyệt nội dung nhóm nợ và lãi quá hạn trước khi build. User flow của Course chưa có trong bộ tài liệu, cần đối chiếu [cần verify].
- **Tác động:** Đo được chuyển đổi người chơi sang app. Mục tiêu kéo dài thời gian trên Financial Hub +170% và thu hút ~5.000 lượt kiểm tra CIC mỗi tháng; hai con số này chưa có căn cứ [cần verify].
- **Đề nghị Ban Giám Đốc:** Phê duyệt phương án A và giao Legal, CIC duyệt policy trước **20/11** để kịp build đón mùa quyết toán thuế cuối năm.
- **Nếu không quyết định:** Build bị trễ, không có xếp hạng để đón mùa quyết toán; Financial Hub tiếp tục bỏ lỡ cơ hội chuyển người dùng web sang sản phẩm tín dụng trên app.

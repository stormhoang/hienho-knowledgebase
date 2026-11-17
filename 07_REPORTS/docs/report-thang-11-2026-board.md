# BÁO CÁO KINH DOANH VÀ HIỆU SUẤT NỀN TẢNG WEB - THÁNG 11/2026
> **Chu kỳ dữ liệu:** 01/11/2026 - 16/11/2026 (MTD 16 ngày, 53% thời gian tháng) và dự báo pacing 30 ngày
> **Nguồn dữ liệu:** GA4 Data API (Property 270743103, hostName == www.momo.vn) kéo ngày 17/11/2026 lúc 07:43; AppsFlyer GPD Attribution (cắt 10/11); MoSpark CMS / Umami (lũy kế đến 10/11); `web_performance_tracking.xlsx`.
> **Phương pháp số liệu:** Số PV trong báo cáo lấy từ lần kéo GA4 ngày 17/11 (PV/Session 1,55, không thấy lặp hit trong kỳ này). Lần kéo trước đó (ngày 16/11, 15 ngày đầu tháng) ghi 3.326.531 hits do lặp thẻ GTM giai đoạn 10-13/11, nên không dùng làm số chính. Web Dev cần xác nhận đã gỡ thẻ trùng.
> **Nguyên tắc báo cáo:** Báo cáo cung cấp bối cảnh chiến lược và số liệu kinh doanh [R]; Cuộc họp tập trung thảo luận và ra quyết định [D].

---

## 1. ĐIỂM NỔI BẬT & ƯU TIÊN TRỌNG TÂM [R]

### 1.1. Điểm nổi bật (Highlights)
- **Lưu lượng MTD 16 ngày đạt 44,3% target:** 1.696.417 Pageviews so với target 3,83M. Nhịp trung bình 106.026 PV/ngày; dự báo kết tháng ~3,18M PV (~83% target). Cần 152.338 PV/ngày trong 14 ngày còn lại (cao hơn nhịp hiện tại 44%).
- **Vehicle Hub tăng mạnh:** 133.623 PVs, tăng so với 119.552 PVs ở báo cáo 15 ngày, nhờ tra cứu phạt nguội 0-CAPTCHA. Target Vehicle trong file là 100K, khác mốc 200K của báo cáo cũ [cần xác nhận].
- **Cinema Hub đạt 31,8% target:** 411.350 PVs, trong đó cụm trang rạp phim chiếm 67,6% lưu lượng Hub.
- **AI Traffic (GEO) đạt 12.550 PVs,** tiến độ 50,2% target 25K; chiếm 0,74% tổng lưu lượng.

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
- **Quy mô lưu lượng:** **1.696.417 Pageviews** (44,3% Target tháng 3,83M; nhịp 106.026 PV/ngày; cần 152.338 PV/ngày cho 14 ngày còn lại).
- **Chất lượng tự nhiên (Non-Paid):** **78,49% tỷ trọng** (1.331.532 PVs, tiến độ 41,74% target Non-Paid). Organic Search 775.481 PVs là kênh lớn nhất, đạt 46,16% target.
- **Kênh trả phí (Paid Ads):** **364.885 PVs** (21,51% tổng), tiến độ 57,09% target Paid; dự báo kết tháng 107% target Paid.
- **Lưu lượng tìm kiếm AI (GEO):** **12.550 PVs** (0,74% tổng), tiến độ 50,2% target 25K. Phần lớn đến từ ChatGPT.

### 2.2. Bảng Pageviews Đa Tháng (T7 - T11, nguồn: web_performance_tracking.xlsx)

| Chỉ số | T7/2026 (Full) | T8/2026 (Full) | T9/2026 (Full) | T10/2026 (Full) | T11/2026 (MTD 16d) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| **Total Pageviews** | 3.167.821 | 3.465.363 | 3.950.763 | 3.602.023 | 1.696.417 |
| **Non-Paid** | 2.669.863 | 2.820.824 | 2.753.670 | 3.128.542 | 1.331.532 |
| **Paid** | 497.958 | 644.539 | 1.197.093 | 473.481 | 364.885 |
| **MoM (Pageviews)** | -7,1% vs T6 | +9,4% vs T7 | +14,0% vs T8 | -8,8% vs T9 | - |
| **Target** | - | - | 3.509.044 | 3.665.607 | 3.829.155 |
| **% Target** | - | - | **112,6%** | **98,3%** | **44,3%** |

### 2.3. Phân Tích Nguyên Nhân Gốc & Yếu Tố Mùa Vụ
- **Khoảng cách nằm ở nhịp:** Lưu lượng đạt 44,3% target sau 53% thời gian tháng. Để về đích, nhịp phải tăng từ 106.026 lên 152.338 PV/ngày (+44%).
- **Kênh tự nhiên đang chậm hơn Paid:** Non-Paid đạt 41,74% tiến độ, Paid đạt 57,09%. Phần thiếu chủ yếu nằm ở Non-Paid. Paid tăng để phục vụ chiến dịch 11.11 và không phải tín hiệu nhu cầu mới.
- **Referral và nguồn khác chậm nhất:** 121.597 PVs, đạt 24,08% tiến độ target nhóm này. Cần kiểm tra là lỗi tracking hay mất nguồn trước khi kết luận.
- **So sánh cùng kỳ tháng 10 chưa thực hiện:** Báo cáo tháng 10 chỉ có số 15 ngày, không cùng mốc 16 ngày. Mục này sẽ bổ sung khi có số cùng kỳ 16 ngày.

---

## 3. HIỆU SUẤT CÁC HUB TRỌNG ĐIỂM [R]

### 3.1. Cinema Hub (411.350 PVs - Đạt 31,8% Target 1,29M)
- **Đóng góp quy mô:** Trang rạp phim đóng góp 278.017 PVs (67,6% lưu lượng Hub). Trang phim chi tiết đạt 89.505 PVs (21,8%). Trang chủ và Blog Cinema cộng thêm 42.130 PVs.
- **Chất lượng chuyển đổi Web-to-App:** End-to-End CVR 12,1% (số 10 ngày từ AppsFlyer), cao nhất các nguồn Web-to-App.
- **Trang review tương tác và trang diễn viên (GSC 01-15/11 so với 17-31/10):** 4 phim ưu tiên đạt 5.145 click, +671% (Sử Thi Ramayana +2.233%, Ngày Con Còn Mẹ +1.725%, Bò Sữa Bay +478%, Godzilla Trừ Không +398%). Trang /person đạt 399 click, +17,7%. Nguồn báo cáo ghi trang review có traffic gấp 48 lần review thường, chưa kiểm chứng lại.
- **Hành động tiếp theo:** Kick-off Pilot Off-Page SEO 125 triệu VNĐ trong tháng 11; triển khai cụm trang Lịch chiếu theo tỉnh thành; gắn Chatbot Cinema lên `/cinema`; xử lý sự cố API lịch chiếu bị rớt.

### 3.2. Financial Hub (176.529 PVs - Đạt 25,2% Target 700K [cần xác nhận])
- **Lưu lượng tăng so với số 15 ngày cũ (111.401 PVs):** +58,5%. Mức tăng này lớn bất thường, cần kiểm tra định nghĩa Hub trước khi công bố.
- **Tỷ giá (GSC 01-15/11 so với 17-31/10):** 24 trang tỷ giá đạt 2.192 click (+101%), hiển thị 1.416.535 (+84,8%). Ngoại tệ sang VND: JPY +490%, THB +150%, CNY +91%, KRW +46%. Báo cáo 14 ngày ghi 151.548 PV và 23.130 click OneLink về app, khác mốc và số trong file 16 ngày; cần thống nhất trước khi công bố.
- **Công cụ tương tác:** Bộ đôi Thuế TNCN và Hộ KD đạt 30,5% tỷ lệ tương tác sau go-live. CIC dẫn đầu lượt click OneLink toàn Hub (số 15 ngày).
- **Hành động tiếp theo:** Trình phê duyệt Quiz CIC (Mục 6.2); xác nhận target tháng 11 và định nghĩa Hub; chuẩn hóa OneLink cho Vay Nhanh, Giá vàng, Chứng khoán.

### 3.3. Vehicle Hub (133.623 PVs - Đạt 133,6% Target 100K [cần xác nhận])
- **Động lực tăng trưởng:** Tra cứu phạt nguội 0-CAPTCHA là điểm sáng chính. Ở báo cáo 15 ngày ghi nhận 88.160 PVs, 82.981 lượt tra cứu hoàn tất và 57.635 lượt mở app (69,5%).
- **Hành động tiếp theo:** Bổ sung cảnh báo thời hạn nộp phạt để thúc đẩy thanh toán in-app.

### 3.4. New User Hub (99.143 PVs - Đạt 33,1% Target 300K [cần xác nhận])
- **Minigame & chiến dịch:** Một Mùa Quýt là nội dung chính; Project Unbox (Gói Quà tự chọn) đã hoàn tất tài liệu nghiệp vụ, chờ build thử nghiệm A/B với ngân sách Media 50 triệu VNĐ.
- **Mục target:** Target 300K trong file khác với mốc khoảng 150K ở báo cáo 15 ngày. Cần thống nhất trước khi công bố.

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
| 1 | Ước tính khoản vay | 9.800 | 4.300 | **43,8%** |
| 2 | Tra cứu điểm CIC | 4.800 | 1.800 | **38,6%** |
| 3 | Tính Lương Gross sang Net | 3.100 | 1.000 | **33,7%** |
| 4 | Giả lập điểm tín dụng CIC | 528 | 116 | **22,0%** |
| 5 | Trả góp Ví Trả Sau | 1.500 | 242 | **16,1%** |
| 6 | Tính BHXH & Lương Hưu | 108 | 14 | **13,0%** |
| 7 | Máy tính Lãi Tiết Kiệm & SIP | 1.500 | 182 | **12,5%** |
| 8 | Chuyển đổi Ngoại tệ | 1.900 | 178 | **9,2%** |
| 9 | Tính Thuế TNCN & Hộ KD | 420 | 128 | **30,5%** |
| 10 | Nhóm Bảng Biểu Tĩnh (Giá vàng, Tỷ giá, Lãi suất) | 1.410 | **0** | **0,0%** |

### 5.2. Nhận Định Điều Hành
- **Đối lập rõ giữa bảng tĩnh (0% tương tác) và công cụ tương tác (33,7% - 43,8%):** Người dùng chỉ tương tác khi được cung cấp công cụ tự nhập số liệu.
- **Cơ sở cho Quiz CIC:** Tỷ lệ 38,6% của Tra cứu CIC và 33,7% của Tính lương cho thấy nhu cầu công cụ tài chính tương tác lớn.
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

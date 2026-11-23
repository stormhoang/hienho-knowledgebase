# -*- coding: utf-8 -*-
from pathlib import Path

content = """# BÁO CÁO TIẾN ĐỘ TUẦN - WEB PLATFORM
> **Kỳ báo cáo:** Tuần 44 (26/10 - 01/11/2026) | **Cập nhật:** 02/11/2026
> **Đội ngũ thực hiện:** Kỹ thuật & Sản phẩm Web Platform (Chủ trì: Văn Hiến)
> **Nguồn số liệu:** GA4 Data API (Property 270743103), AppsFlyer Web-to-App, Excel SSOT `web_performance_tracking.xlsx`.

---

## I. TỔNG QUAN HIỆU SUẤT THÁNG 10/2026

### 1. Bảng Số Liệu Chốt Cả Tháng 10 (Full 31 Ngày)

| Kênh Lưu Lượng / Chỉ Số | T9/2026 (Full) | T10/2026 (Target) | T10/2026 (Thực Đạt) | % Đạt Target | % MoM vs. T9 | Tỷ Trọng T10 | Ghi Chú Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **TỔNG LƯU LƯỢNG (PAGEVIEWS)** | **3.952.859** | **3.665.607** | **3.602.023** | **98.3%** | **-8.9%** | **100.0%** | Thiếu 63.584 PV so với kế hoạch (chủ yếu do cắt giảm mạnh Paid Ads) |
| **Kênh Tự Nhiên (Non-Paid)** | **2.755.766** | 3.176.343* | **3.128.542** | **98.5%*** | **+13.5%** | **86.9%** | Tăng thêm 372.776 PV (+13,5% MoM), bù được 52% lượng view giảm từ Ads |
| - Tìm kiếm tự nhiên (Organic Search) | 1.623.796 | - | 1.715.771 | - | +5.7% | 47.6% | Đóng góp gần một nửa tổng view toàn trang |
| - Truy cập trực tiếp (Direct) | 755.896 | - | 931.731 | - | +23.3% | 25.9% | Người dùng vào thẳng các trang tiện ích quen thuộc |
| - Giới thiệu & Khác (Referral / Others) | 376.074 | - | 481.040 | - | +27.9% | 13.4% | Lượng truy cập từ các trang đối tác và backlink |
| *- Trong đó: Nguồn AI (GEO / AI Search)* | *13.596* | *-* | *18.547* | *-* | **+36.4%** | *0.5%* | ChatGPT chiếm 17.739 PV (95,6%), Perplexity 284 PV |
| **Kênh Trả Phí (Paid Traffic)** | **1.197.093** | 489.264 | **473.481** | **96.8%** | **-60.4%** | **13.1%** | Giảm 723.612 PV sau khi dừng các chiến dịch quảng cáo kém hiệu quả |

### 2. Tóm Tắt Điểm Đáng Chú Ý Tháng 10
- **Lượng truy cập tự nhiên (Non-Paid) bù được một nửa lượng view bị hụt do cắt Ads:** Non-Paid tháng 10 đạt 3,12 triệu PV (+13,5% so với tháng 9), chiếm 86,9% tổng view toàn trang. Khi cắt 723K view quảng cáo, lượng view tự nhiên tăng thêm đã bù lại được 52% phần hụt này.
- **Khách vào web trực tiếp (Direct) tăng khá (+23,3% MoM, đạt 931K PV):** Người dùng có thói quen vào thẳng các trang tiện ích như xem lịch chiếu phim, tra cứu phạt nguội, xem tỷ giá ngoại tệ, giá vàng và giá xăng.
- **Tình hình 2 hub trọng điểm:**
  - *Cinema Hub:* Đạt 1,19 triệu PV (vượt chỉ tiêu 1,11 triệu, đạt 107,3%). Traffic tự nhiên tăng 21,7% giúp bù đủ phần view giảm do cắt quảng cáo trang phim lẻ.
  - *Financial Hub:* Đạt 273K PV (tăng +9,6% so với 249K của tháng 9, đạt 60,8% chỉ tiêu 450K). Lượng view từ nhóm trang Trung tâm Tài chính (+442%) và Ví Trả Sau (+38%) tăng tốt, giúp bù phần giảm của Vay Nhanh khi dừng chạy ads.
- **Phễu tải app sang liên kết ngân hàng (AppsFlyer cả tháng 10):** Đạt **11.143 lượt cài đặt** ➔ **3.902 đăng ký tài khoản** (35%) ➔ **2.389 người liên kết ngân hàng (Map Bank)** (tăng +5% so với tháng 9, đạt mức cao nhất từ trước đến nay) ➔ **1.284 MAU**. Điểm rơi rụng lớn nhất vẫn là khâu cài app xong nhưng chưa đăng ký tài khoản (chiếm 65%).
- **Việc cần làm trên Google tuần tới:** Tối ưu tỷ lệ click (CTR) cho cụm từ khóa Tỷ giá (vừa có thêm 440K lượt hiển thị) và kéo lại thứ hạng trang rạp CGV về lại top 5 sau khi bị tụt nhẹ.

### 3. Lưu Lượng Từ Các Công Cụ AI (GEO - Generative Engine Optimization)

| Nền tảng AI (sessionSource GA4) | T9/2026 (Full) | T10/2026 (Full 31d) | Tăng/Giảm vs. T9 | % MoM | Tỷ trọng GEO (%) | Ghi Chú |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **ChatGPT (chatgpt.com)** | 12.589 | 17.739 | **+5.150** | **+40.9%** | **95.6%** | Nguồn chính kéo người dùng về web khi hỏi về tài chính và rạp phim |
| **Google Gemini (gemini.google.com)** | 704 | 467 | **-237** | **-33.7%** | **2.5%** | Giảm do Gemini trả lời ngay trên kết quả tìm kiếm, người dùng ít click sang web |
| **Perplexity (perplexity.ai)** | 239 | 284 | **+45** | **+18.8%** | **1.5%** | Lượng dùng tăng nhẹ từ nhóm tìm kiếm thông tin chuyên sâu |
| **Khác (Claude, Copilot, Meta AI)** | 64 | 57 | **-7** | **-10.9%** | **0.4%** | Quy mô nhỏ, chiếm tỷ trọng không đáng kể |
| **TỔNG LƯU LƯỢNG GEO (AI SEARCH)** | **13.596** | **18.547** | **+4.951** | **+36.4%** | **100.0%** | Chiếm **0.5%** toàn web; khách ở lại xem trung bình 1.6 trang mỗi lượt vào |

- **Các nhóm trang nhận được nhiều lượt vào từ AI nhất:**
  1. *Tài chính (Vay, Thẻ, Ví):* Chiếm 17,3% lượt vào (trang `/vay-nhanh` 757 phiên, `/vi-tra-sau` 155 phiên).
  2. *Hỏi đáp (FAQ):* Chiếm 14,1% lượt vào (trang `/hoi-dap` 517 phiên; tỷ lệ tương tác đạt 95,2%).
  3. *Trang chủ & Giới thiệu:* Chiếm 11,4% lượt vào (Trang chủ 667 phiên, `/merchant` 279 phiên).
  4. *Cinema Hub:* Chiếm 10,3% lượt vào (tăng từ 460 lên 1.210 phiên, chủ yếu từ cụm rạp CGV và các phim mới ra rạp).
- **Thực tế về click từ AI:** Các bài viết được AI trích dẫn nhiều nhất (như tra cứu BHYT ~44K trích dẫn, review phim ~35K trích dẫn) lại có rất ít người click sang web, vì câu trả lời đã hiển thị đầy đủ ngay trên màn hình AI. Muốn người dùng bấm vào web, trang đích cần có **công cụ tính toán hoặc tra cứu tương tác** (như tính thuế, xem lịch chiếu rạp) thay vì chỉ là bài viết thông tin đơn thuần.

---

## II. TIẾN ĐỘ CÁC DỰ ÁN CHIẾN LƯỢC (USE CASES)

### 1. Cinema Hub: Minigame Bò Sữa Bay Tại Rạp, Bổ Sung Trang Diễn Viên & Giữ Thứ Hạng Tìm Kiếm

- **Đội ngũ phụ trách:** Frontend Engineering & SEO Content Studio (Chủ trì: Hoan, Anh Hùng | Hợp tác BU Movies: Bình, Thức)
- **Mục tiêu tuần qua:** Giữ lượng view khi dừng chạy ads; chuẩn bị minigame cho phim *Bò Sữa Bay*, mở trang diễn viên và cập nhật giao diện các cụm rạp đối tác (Rio, Touch, Metiz).

#### A. Khung Ưu Tiên Công Việc (Initiative Priority)
- **[P0 - Ưu tiên hàng đầu]:**
  - **Minigame Bò Sữa Bay quét QR tại rạp (`/cinema/bo-sua-bay-25058`):** Sau khi kiểm tra tải và đối soát quy định của rạp, team chuyển sang dạng trả lời câu hỏi trắc nghiệm (Quiz) nhận voucher giảm giá vé xem phim. Đã kiểm thử chịu tải sẵn sàng cho khách tại rạp quét mã từ màn hình TVC rạp (Rio, Touch, Metiz).
    - ![Màn hình mở đầu minigame Bò Sữa Bay](https://homepage.momocdn.net/img/bosuabay-1-261102170040.jpg)
  - **Lưu cache tĩnh cho lịch chiếu rạp (Static Cache):** Lưu cache cục bộ dữ liệu lịch chiếu từ các rạp để trang tải nhanh (P95 < 1.5s), không bị lỗi trang khi hệ thống API bên rạp bị chậm hoặc rớt mạng.
- **[P1 - Mở rộng nội dung & SEO]:**
  - **Mở trang thông tin Diễn viên (`/cinema/dien-vien/...`):** Đã lên Production các trang hồ sơ diễn viên gắn liền với phim họ đóng, chuẩn bị đón lượng tìm kiếm tăng cao vào dịp trao giải và mùa phim Tết.
  - **Kéo lại thứ hạng trang rạp CGV:** Bổ sung lại Schema lịch chiếu và dùng AI Qwen tóm tắt nhanh đánh giá của khán giả từ Google Maps để làm dày nội dung trang, kéo CGV về lại top 5.
  - **Cập nhật giao diện rạp đối tác:** Giữ vị trí Top 5 Google cho các trang phim chiếu rạp; đưa từ khóa thương hiệu rạp đối tác `metiz cinema` lên **Top 3 SERP**; hoàn thành cập nhật UI cho Starlight Cinema và Cinemax; viết thêm 3 bài blog mới.
  - **Thử nghiệm SEO Off-Page 3 tháng (ngân sách 125 triệu):** Đặt mục tiêu đưa các cụm trang rạp lên top 5 Google và tăng xuất hiện trong câu trả lời của AI.

#### B. Phối Hợp Giữa Web Platform Và BU Movies
*(Theo bảng kế hoạch chung tại Google Sheets `[WP] Web Cinema | Roadmap` - ID `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`)*

| Hạng mục Phối hợp | Việc của Web Platform (Anh Hùng, Hoan) | Việc của BU Movies (Bình, Thức) | Cách phối hợp & Thời hạn |
| :--- | :--- | :--- | :--- |
| **Game Bò Sữa Bay (quét QR tại rạp)** | Lập trình luồng Quiz, tối ưu hiển thị điện thoại, kiểm tra chịu tải luồng quét mã QR từ TVC rạp. | Cung cấp số lượng voucher vé xem phim, viết thể lệ (TnC), liên hệ rạp duyệt phát TVC tại sảnh (Rio, Touch, Metiz). | BU Movies chốt kịch bản TVC và cấp mã voucher trước 31/10; gửi link bài đăng trước giờ chiếu tối thiểu 60 phút. |
| **Viết bài & Review Phim** | Dùng AI hỗ trợ viết 80% số lượng bài blog/review phim hot; tối ưu SEO onpage và gắn Schema. | Cung cấp thông tin phim, ảnh và video bản quyền từ nhà phát hành, kiểm tra nội dung (QC) trước khi duyệt. | Web Team cấp tài khoản CMS; BU Movies gửi góp ý outline trong vòng 24 giờ. |
| **Trang Cụm Rạp Đối Tác** | Chỉnh sửa giao diện, gắn bản đồ chỉ đường, lưu cache lịch chiếu cho rạp (Touch, Metiz, Starlight, Rio). | Cung cấp thông tin kết nối và hình ảnh rạp đúng chuẩn thương hiệu. | Hai bên kiểm tra lại chất lượng hiển thị lịch chiếu định kỳ hàng tuần. |

- **Điểm nghẽn cần tháo gỡ:** BU Movies cần chốt sớm cơ chế cấp voucher vé xem phim và duyệt kịch bản phát sóng TVC minigame tại rạp trước ngày 31/10.

| Phân loại Trang / Tiện ích | T9/2026 (Full) | T10/2026 (Target) | T10/2026 (Thực đạt) | % Đạt Target | % MoM vs. T9 | Đánh Giá Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Cinema Hub** | **1.220.075** | **1.117.378** | **1.198.507** | **107.3%** | **-1.8%** | **Vượt 107.3% chỉ tiêu** (+81K view); traffic tự nhiên (+21,7%) bù đủ phần cắt giảm Ads |
| **Trang Rạp phim (Cinema_Cineplex)** | 501.574 | - | 735.008 | - | **+46.5%** | Tăng mạnh (+233K view) nhờ tối ưu giao diện các rạp đối tác (Rio, Touch, Metiz) |
| **Trang phim chi tiết (Cinema_Page)** | 645.998 | - | 400.952 | - | **-37.9%** | Giảm do chủ động dừng chạy Ads (tháng 9 chạy 333K view, tháng 10 còn 7K view) |
| **Trang chủ Cinema (Cinema_Home)** | 29.066 | - | 36.361 | - | **+25.1%** | Tăng tự nhiên (+7.3K view) từ lượng khách vào tìm rạp và xem lịch chiếu |
| **Blog Phim (Cinema_Blog)** | 41.166 | - | 20.115 | - | **-51.1%** | Giảm sau khi tập trung nội dung vào trang chi tiết phim |
| **Trang Chiến dịch (Cinema_LP)** | 80 | - | 3.493 | - | **+4266.2%** | Tăng nhờ có minigame Quiz Bò Sữa Bay và các trang sự kiện rạp |
| **Tin tức (Cinema_News)** | 2.191 | - | 2.578 | - | **+17.7%** | Lượng đọc duy trì đều đặn |

---

### 2. Financial Hub: Ra Mắt 2 Công Cụ Tính Thuế, Chuẩn Bị Đưa Chứng Chỉ Quỹ Lên Web & Ý Tưởng Game CIC

- **Đội ngũ phụ trách:** Financial Web Team & UX Design Studio (Chủ trì: nhat.bui1, Hoan)
- **Mục tiêu tuần qua:** Chuyển trọng tâm sang xây dựng các công cụ tính toán tài chính thiết thực cho người dùng (tính thuế, tỷ giá, quỹ đầu tư), thay vì chỉ viết bài lý thuyết; thu hút tệp hộ kinh doanh và người làm việc tự do (Freelancers).
- **Công việc đã làm & Kết quả:**
  - **Lên Production 7 trang tra cứu Tỷ Giá ngoại tệ:** Cả 7 trang đều đã vào `top 10 Google`; viết thêm 9 bài blog tài chính; đang phối hợp mở tiếp các trang tỷ giá đảo `VND sang [Ngoại tệ]`.
  - **Hoàn thành 2 công cụ tính thuế mới:**
    - Công cụ Tính Thuế TNCN (`/tai-chinh/thue-tncn`): Hỗ trợ tính thuế theo tháng (từ lương Gross sang Net) và ước tính quyết toán thuế cả năm.
      - ![Tính Thuế TNCN hàng tháng: quy đổi lương Gross sang Net](https://homepage.momocdn.net/img/thue-tncn-261102170227.jpg)
      - ![Quyết toán Thuế TNCN cả năm: dự toán số thuế còn phải nộp hoặc được hoàn](https://homepage.momocdn.net/img/thue-tncn2-261102170226.jpg)
    - Công cụ Tính Thuế Hộ Kinh Doanh (`/tai-chinh/thue-ho-kinh-doanh`): Dành cho hộ kinh doanh cá thể, người bán hàng online theo Thông tư 40 với ngưỡng doanh thu mới 200 triệu đồng.
    - Đã xong công thức tính, giao diện hiển thị và thanh menu chuyển đổi giữa các tiện ích thuế.
  - **Chốt phương án đưa Chứng Chỉ Quỹ (SIP) lên Web:** Trong lúc chờ kết nối API dữ liệu giá chứng chỉ quỹ (NAV) từ các quỹ đối tác, team thống nhất làm trước Phase 1 dùng dữ liệu cập nhật định kỳ (giới thiệu lợi nhuận quá khứ, giải thích cách tích lũy từ 10.000 đồng) để dẫn người dùng vào mở tài khoản trong app.
    - ![Công cụ mô phỏng tích lũy Chứng Chỉ Quỹ: chọn mức góp hàng tháng, thời điểm bắt đầu, loại quỹ và so sánh với gửi tiết kiệm](https://homepage.momocdn.net/img/ccq-261102165842.png)
  - **Lên ý tưởng game Điểm Tín Dụng CIC:** Thiết kế các bài học tình huống ngắn gọn (kiểu Duolingo), học mỗi ngày để nhận voucher quà tặng, giúp người dùng hiểu cách giữ điểm tín dụng tốt một cách nhẹ nhàng.
  - **Duy trì công cụ Quỹ Nhóm Phase 1 (`/tai-chinh/quy`):** Giúp người dùng mô phỏng cách chia tiền quỹ nhóm minh bạch và dẫn vào tính năng trong app.
- **Điểm nghẽn cần tháo gỡ:** Chờ BU Ngân hàng duyệt giao diện trang Bank Detail trước 30/10; Finhub BU kiểm tra trang Chứng Chỉ Quỹ Phase 1 và chốt lịch nối API NAV chính thức.

| Phân loại Dịch vụ / Tiện ích | T9/2026 (Full) | T10/2026 (Full 31d) | Tăng/Giảm vs. T9 | % MoM | Đánh Giá Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Financial Hub** | **249.823** | **254.077** | **+4.254** | **+1.7%** | Tăng nhẹ +1,7%; Trung tâm tài chính & Ví Trả Sau tăng giúp bù cho Vay Nhanh |
| **Điểm Tín Dụng** | 79.092 | 79.987 | **+895** | **+1.1%** | Giữ đều quanh mức 80K view, chuẩn bị mở rộng sang bài trắc nghiệm CIC |
| **Ví Trả Sau** | 42.174 | 59.537 | **+17.363** | **+41.2%** | Tăng tốt (+41,2%) nhờ người dùng tìm kiếm tự nhiên và đọc cẩm nang |
| **Vay Nhanh** | 109.955 | 57.512 | **-52.443** | **-47.7%** | Giảm mạnh do cắt quảng cáo, cần kéo lại bằng bài viết SEO và tiện ích thuế |
| **Trung Tâm Tài Chính** | 8.025 | 38.013 | **+29.988** | **+373.7%** | Tăng mạnh (+373,7%) nhờ đưa 7 trang Tỷ Giá mới lên trang web |
| **Quản Lý Chi Tiêu** | 1.000 | 4.829 | **+3.829** | **+382.9%** | Tăng nhờ có thêm loạt bài viết hướng dẫn quản lý tài chính cá nhân |
| **Mở Thẻ Tín Dụng** | 1.464 | 3.397 | **+1.933** | **+132.0%** | Tăng nhờ có bảng so sánh quyền lợi các loại thẻ tín dụng |
| **Túi Thần Tài** | 2.077 | 2.135 | **+58** | **+2.8%** | Lượng người xem duy trì ổn định |

---

### 3. Vehicle Hub: Mở Trang Nộp Phạt CSGT Trên Web & Hoàn Thiện Dữ Liệu 41 Hãng Xe

- **Đội ngũ phụ trách:** Transport & Public Services Engineering
- **Mục tiêu tuần qua:** Mở rộng từ trang tra cứu phạt nguội sang hỗ trợ người dùng nộp phạt online và tìm kiếm thông tin xe cộ.
- **Công việc đã làm & Kết quả:**
  - **Mở trang Nộp Phạt CSGT trên Production:** Nối luồng từ trang tra cứu phạt nguội ([`/phat-nguoi`](https://www.momo.vn/phat-nguoi)) sang trang hướng dẫn nộp phạt trên web, sau đó dẫn vào app thanh toán.
  - **Rà soát dữ liệu 41 hãng xe và gara toàn quốc:** Cùng team VTTI hoàn thành kiểm tra danh sách hệ thống gara và đại lý chính hãng trước 31/10 để sẵn sàng hiển thị trên web.
  - **Hoàn thành menu tiện ích giao thông:** Gắn thanh menu `/tien-ich-giao-thong`, đưa công cụ tính khấu hao xe cũ lên Staging và theo dõi tải hệ thống tra cứu cuối tháng.
- **Điểm nghẽn cần tháo gỡ:** Chờ VTTI BU duyệt nội dung trang Nộp Phạt và gửi danh sách địa chỉ các Trụ sở Công an để làm tính năng tìm điểm nộp phạt gần nhất.

| Phân loại Tiện ích / Dịch vụ | T9/2026 (Full) | T10/2026 (Full 31d) | Tăng/Giảm vs. T9 | % MoM | Đánh Giá Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Vehicle Hub** | **66.808** | **61.969** | **-4.839** | **-7.2%** | Tiện ích giao thông tăng tốt giúp bù phần nào lượng sụt giảm của Phạt nguội |
| **Bảo Hiểm Ô Tô** | 19.022 | 22.332 | **+3.310** | **+17.4%** | Tăng +17,4% sau khi chuyển sang MoSpark và làm lại widget báo giá |
| **Phạt Nguội** | 39.382 | 22.255 | **-17.127** | **-43.5%** | Giảm do mùa vụ và cạnh tranh thứ hạng tìm kiếm, cần tối ưu lại SEO on-page |
| **Tiện Ích Giao Thông** | 1.179 | 11.895 | **+10.716** | **+908.9%** | Tăng mạnh nhờ trang Giá xăng và bảng tra cứu thông tin xe |
| **Bảo Hiểm Xe Máy** | 6.178 | 4.482 | **-1.696** | **-27.5%** | Giảm theo xu hướng chung của nhóm bảo hiểm xe máy |
| **Phí Không Dừng** | 1.047 | 1.005 | **-42** | **-4.0%** | Duy trì ổn định quanh mức 1.000 view/tháng |

---

### 4. Insurtech Hub: Thiết Kế Lại Trang Chủ Bảo Hiểm & Làm Tính Năng Lưu Form Báo Giá Dở Dang

- **Đội ngũ phụ trách:** Insurtech Web Engineering
- **Mục tiêu tuần qua:** Tối ưu lại giao diện để khách dễ tìm sản phẩm bảo hiểm và giảm tỷ lệ bỏ dở khi đang nhập thông tin báo giá.
- **Công việc đã làm & Kết quả:**
  - **Sắp xếp lại trang chủ Bảo hiểm (`/bao-hiem`):** Gom 9 loại bảo hiểm theo từng nhóm rõ ràng, dễ nhìn hơn trên điện thoại và đơn giản hóa biểu mẫu lấy báo giá nhanh.
  - **Đưa widget bảo hiểm lên bản chính thức:** Đã đưa widget Bảo hiểm ô tô lên Production; kiểm thử xong widget tra cứu thẻ BHYT.
  - **Lưu thông tin form báo giá dở dang:** Khi khách từng vào xem báo giá quay lại web, hệ thống tự điền lại các thông tin đã nhập trước đó để họ không phải gõ lại từ đầu, giảm tỷ lệ bỏ dở form.
- **Điểm nghẽn cần tháo gỡ:** Chờ team Insurtech duyệt phát hành trang chủ bảo hiểm mới và widget tra cứu BHYT lên Production.

---

### 5. New User Hub: Kiểm Thử Trang Tải App `/tai-app` & Kết Quả Các Kênh Quảng Cáo Hút Người Dùng Mới

- **Đội ngũ phụ trách:** User Acquisition & Growth Engineering
- **Mục tiêu:** Chuẩn bị trang tải app tập trung trên web và theo dõi hiệu quả chuyển đổi thành người dùng app có liên kết ngân hàng.
- **Công việc đã làm & Kết quả:**
  - **Kiểm thử trang tải app (`/tai-app`):** Đã test xong cơ chế tự nhận diện máy (trên điện thoại thì mở thẳng App Store / Google Play, trên máy tính thì hiển thị mã QR to rõ).
  - **Phễu người dùng mới cả tháng 10:** Mang về **11.143 lượt cài app** ➔ **3.902 đăng ký** (35%) ➔ **2.389 người liên kết ngân hàng (Map Bank)** (tăng +5% so với tháng 9, đạt mức cao nhất từ trước đến nay) ➔ **1.284 MAU**.
  - **Hiệu quả cụm quảng cáo tương tác tài chính (Điểm Tín Dụng + Game Một Mùa Quýt):**
    - Khi gộp 2 trang tương tác này lại, tổng lượt truy cập từ quảng cáo đạt **65.219 phiên** (chiếm **22,4%** toàn bộ quảng cáo web, đứng thứ 2 sau trang nạp TikTok).
    - *Điểm Tín Dụng (`/diem-tin-dung`):* 35.541 phiên, có 33.496 lượt bấm mở app kiểm tra CIC (tỷ lệ bấm đạt 94,25%).
    - *Game Một Mùa Quýt (`/game/mot-mua-quyt`):* 29.678 phiên, có 7.097 người chơi hết game (ở lại trang trung bình 65,2 giây) và 3.454 lượt bấm cài/mở app (1.230 khách duy nhất).
    - *Chiến dịch AppsFlyer (`261012_C.Financial-Health`):* Đóng góp 68 lượt cài app và 3 người liên kết ngân hàng đầu tiên.
    - *Đánh giá:* Dùng câu hỏi trắc nghiệm tài chính vui và công cụ tra cứu thực tế giúp giữ chân khách lâu hơn hẳn các trang quảng cáo khuyến mãi thông thường.
- **Điểm nghẽn cần tháo gỡ:** Team Growth cần thống nhất nội dung và hình ảnh để thử nghiệm A/B trên trang `/tai-app` trước khi đổ traffic lớn.

---

### 6. Lottery Hub: Đảm Bảo Web Chạy Ổn Định Giờ Mở Thưởng Vietlott & Chuẩn Bị Công Cụ Sửa Nội Dung

- **Đội ngũ phụ trách:** Utility Web Engineering (Chủ trì: duy.tran2)
- **Công việc đã làm & Kết quả:**
  - **Ổn định giao diện hiển thị:** Giữ cấu trúc 8 trò chơi Vietlott dạng thẻ gọn gàng trên mobile, rút Keno/Bingo18 về 20 bóng và bảng kết quả 27 giải XSKT 3 miền không bị cuộn ngang trên điện thoại.
  - **Lưu cache giờ cao điểm:** Lưu cache cục bộ dữ liệu kết quả để trang web tải dưới 1,5 giây trong khung giờ 18h00 - 18h30 hàng ngày, không làm quá tải hệ thống máy chủ.
  - **Chuẩn bị công cụ MoSpark trên Staging:** Sẵn sàng công cụ để PO vé số tự thay đổi nội dung chữ và banner trên trang mà không cần nhờ lập trình viên sửa code.
- **Kế hoạch tiếp theo:** Tiếp tục theo dõi tốc độ tải trang trong khung giờ mở thưởng 18h00 hàng ngày và hướng dẫn PO vé số dùng công cụ.

---

### 7. Dịch Vụ Mới & Nạp Game: Ra Mắt Trang Giới Thiệu ChatGPT & Tối Ưu Nạp Game Mobile

- **Đội ngũ phụ trách:** Commerce Web Engineering
- **Công việc đã làm & Kết quả:**
  - **Lên trang giới thiệu tài khoản ChatGPT:** Hoàn thành trang giới thiệu gói dịch vụ ChatGPT kèm bảng giá rõ ràng, sẵn sàng mở cổng thanh toán qua MoMo.
  - **Đơn giản hóa nạp thẻ game trên điện thoại:** Giảm bớt các bước chọn mệnh giá và nhà phát hành trên mobile, giúp khách thao tác nhanh hơn khi mua thẻ của 4 nhà mạng lớn.
- **Kế hoạch tiếp theo:** Theo dõi tỷ lệ nạp thẻ thành công và đánh giá lượng người quan tâm trên trang giới thiệu ChatGPT.

---

## III. TIẾN ĐỘ CÁC NỀN TẢNG KỸ THUẬT (ENABLERS)

### 1. MoSpark CMS: Cải Tiến Màn Hình Viết Bài Cho Biên Tập Viên

- **Đội ngũ phụ trách:** CMS Frontend Engineering (Chủ trì: duy.tran2, hieu.nguyen8)
- **Tiến độ & Kết quả:**
  - **Làm mới giao diện soạn thảo (Blog Editor):** Tinh gọn khung viết bài, mở rộng khoảng trống gõ chữ, xếp lại nút chèn ảnh, chỉnh thẻ SEO và tóm tắt ý chính để biên tập viên đỡ phải cuộn trang lên xuống nhiều lần.
  - **Tính năng xem trước thời gian thực (Live Preview):** Cho phép xem trước bài viết hiển thị ra sao trên cả điện thoại lẫn máy tính ngay trong lúc đang gõ.
  - **Bảng quản lý bài viết:** Nối số view từ GA4 vào để biên tập viên biết bài nào đang có người đọc theo từng cụm chủ đề.
- **Kế hoạch tiếp theo:** Hoàn thiện giao diện mới và mời đội Content Studio dùng thử trên môi trường Staging.

---

### 2. MoSpark AI Core: Quản Trị Tài Liệu Tri Thức & Tích Hợp LLM Gateway

- **Đội ngũ phụ trách:** AI Platform Engineering (Chủ trì: duy.tran2, hieu.nguyen8)
- **Tiến độ & Kết quả:**
  - **Màn hình quản lý tri thức AI (Project Center):** Xây dựng bảng theo dõi tập trung để biết mỗi chatbot AI đã nạp bao nhiêu tài liệu, tài liệu nào đã đồng bộ xong và tài liệu nào còn thiếu.
  - **Tự động quét link từ Sitemap:** Tự động đọc sitemap web, so khớp với kho tài liệu hiện có để phát hiện ngay các bài viết mới chưa được nạp cho AI học.
  - **Bộ lọc bài viết hợp lệ:** Chỉ nạp những bài viết đã xuất bản chính thức, có nội dung chữ rõ ràng; tự động lọc bỏ các banner quảng cáo, nút bấm trang trí để AI không học nhầm rác.
  - **Đồng bộ trực tiếp từ cây danh mục web:** Cho phép bấm 1 nút để đồng bộ nhanh tài liệu theo từng nhánh chuyên mục hoặc theo link tùy chọn.
  - **Đóng gói thư viện Company LLM Gateway SDK:** Hoàn thành bộ thư viện kết nối mô hình Qwen 3.5 an toàn bằng token bảo mật, phục vụ cho 3 sản phẩm dùng AI trên web (gợi ý nội dung MoMo AI, dashboard MoSpark và Content Studio).
- **Kế hoạch tiếp theo:** Nối dữ liệu báo cáo GA4/GSC vào mô hình AI để tự động sinh nhận định phân tích hàng tuần.

---

### 3. Hệ Thống Thiết Kế MoBase: Mở Rộng Menu 2 Tầng & Đóng Gói Thành Phần Chuẩn

- **Đội ngũ phụ trách:** Design System Engineering
- **Tiến độ & Kết quả:**
  - **Mở rộng thanh menu 2 tầng (Header Advance):** Đưa cấu trúc menu 2 tầng từ Financial Hub sang Cinema Hub và Vehicle Hub để giao diện toàn web đồng nhất.
  - **Đóng gói thành phần dùng chung:** Đóng gói component Bảng giá chuẩn và chuẩn bị tài liệu kỹ thuật để bàn giao bản MoBase v2.1 cho các team khác.
- **Kế hoạch tiếp theo:** Kiểm tra độ tương thích của MoBase v2.1 trên các dòng điện thoại khác nhau và xuất bản gói thư viện nội bộ.

---

### 4. Web-in-App & Admin Panel BMC: Chuẩn Bị Build Prod Phase 2

- **Đội ngũ phụ trách:** Web-in-App Engineering (Chủ trì: duy.tran2, hieu.nguyen8)
- **Tiến độ & Kết quả:**
  - **Hoàn thành trang All-in-One Editor:** Hợp nhất công cụ chỉnh sửa cấu hình trang web nhúng trong app, cho phép chỉnh sửa nội dung, banner và xem trước hiển thị ngay trên cùng một màn hình.
  - **Chuẩn bị triển khai Production:** Đồng bộ các nhánh tính năng với team BMC, chạy kiểm thử tự động (Unit Test) và rà soát các quyền truy cập để chuẩn bị đưa lên Production vào ngày 02/11/2026.
- **Kế hoạch tiếp theo:** Phối hợp team BMC đưa bản cập nhật lên Production an toàn vào ngày 02/11.

---

### 5. Cổng Tìm Kiếm (`/tim-kiem`): Đưa Thẻ Chuyển Tiền & Banner Bạn Mới Lên Production

- **Đội ngũ phụ trách:** Search & Portal Engineering
- **Tiến độ & Kết quả:**
  - **Lên Production thẻ Chuyển tiền qua SĐT:** Khi người dùng gõ số điện thoại vào ô tìm kiếm, web tự hiện thẻ chuyển tiền nhanh dẫn vào app.
  - **Hiển thị banner cho người dùng mới:** Gắn banner hướng dẫn nhận quà và tải app cho khách mới vào trang tìm kiếm.
  - **Chuẩn bị Phase 2:** Thiết kế khung hiển thị các dịch vụ gợi ý thông minh dựa trên lịch sử tìm kiếm phổ biến.
- **Kế hoạch tiếp theo:** Đo lường tỷ lệ người dùng bấm vào thẻ chuyển tiền nhanh và banner bạn mới trong tuần đầu ra mắt.

---

### 6. Danh Mục URL (URL Catalog) & Bảo Mật Hạ Tầng API

- **Đội ngũ phụ trách:** Backend & Data Architecture
- **Tiến độ & Kết quả:**
  - **Khởi tạo bảng danh mục URL (`tblWebsiteUrlCatalog`):** Đã chạy kịch bản tạo bảng trên Staging, sẵn sàng kết nối dữ liệu từ CMS để quản lý tập trung toàn bộ link web.
  - **Bảo mật API Public:** Bật cơ chế giới hạn tần suất gọi API (Rate Limiting) và kiểm soát nguồn gọi (CORS) trên 100% các API công khai của Web Platform để chống cào dữ liệu.
  - **Xử lý luồng dữ liệu Merchant:** Đang chuyển các cuộc gọi API phía trình duyệt sang chạy qua máy chủ (Server-side Proxy) để không lộ thông tin đối tác ra ngoài.
- **Kế hoạch tiếp theo:** Chạy thử luồng đồng bộ danh mục URL trên Staging và hoàn thành chuyển đổi Server-side Proxy cho luồng Merchant trước 05/11.

---

## IV. ĐIỂM NGHẼN & VIỆC CẦN PHỐI HỢP LIÊN PHÒNG BAN

### 1. Phối Hợp Với Các Cell Teams
- **BU Movies (Cinema):** Cung cấp voucher vé xem phim và duyệt kịch bản phát TVC minigame Bò Sữa Bay tại rạp (Rio, Touch, Metiz) trước ngày 31/10; gửi ảnh/video bản quyền từ nhà rạp để làm truyền thông.
- **BU Dịch Vụ Tài Chính & Ngân Hàng:** BU Ngân hàng duyệt giao diện trang Bank Detail trước 30/10; Finhub BU kiểm tra trang Chứng Chỉ Quỹ Phase 1 và chốt lịch nối API NAV chính thức.
- **BU Giao Thông (VTTI):** Chốt danh sách 41 hãng xe và gara trước 31/10; duyệt nội dung trang Nộp Phạt CSGT và gửi địa chỉ Trụ sở Công an để làm tính năng tìm điểm nộp phạt.
- **Team Bảo Hiểm (Insurtech):** Duyệt phát hành trang chủ bảo hiểm mới (`/bao-hiem`) và widget tra cứu BHYT lên bản chính thức trước ngày 02/11.
- **PO Vé Số:** Dùng thử công cụ MoSpark trên Staging để sau này tự thay đổi nội dung chữ và banner trên trang.

### 2. Phối Hợp Với Các Functional Teams
- **Security & DevOps:** Hỗ trợ kiểm tra bảo mật, chuyển đổi luồng dữ liệu Merchant sang Server-side Proxy trước ngày 05/11.
- **Growth Team:** Phối hợp lịch đăng bài truyền thông game Bò Sữa Bay; chốt thông điệp để làm thử nghiệm A/B trên trang tải app `/tai-app`.
- **Design Studio:** Hoàn thiện bản vẽ thiết kế cho game Điểm Tín Dụng CIC; chốt giao diện màn hình viết bài mới trên MoSpark CMS.
- **Pháp Lý (Legal):** Rà soát câu chữ trên 2 trang Tính Thuế (TNCN, Hộ kinh doanh) trước khi mở công khai cho người dùng tính toán.

---

## V. KẾ HOẠCH CÔNG VIỆC TRỌNG TÂM TUẦN TỚI

### 1. Các Dự Án Sử Dụng (Strategic Projects)
- **Cinema Hub:**
  - [P0] Đưa game Quiz Bò Sữa Bay lên web, sẵn sàng đón luồng quét mã QR từ TVC tại rạp đối tác.
  - [P0] Đăng bài truyền thông và chia sẻ thông tin game Bò Sữa Bay trên các nhóm cộng đồng phim.
  - [P1] Tối ưu lại Schema và nội dung trang rạp CGV để kéo lại thứ hạng top 3–5 Google.
  - [P1] Mở trang thông tin Diễn viên (`/cinema/dien-vien/...`) trên Production.
- **Financial Hub:**
  - [P0] Đưa 2 trang Tính Thuế TNCN (`/tai-chinh/thue-tncn`) và Thuế Hộ Kinh Doanh (`/tai-chinh/thue-ho-kinh-doanh`) lên Production.
  - [P0] Hoàn tất kiểm thử và phát hành trang Chứng Chỉ Quỹ (Phase 1 dùng dữ liệu định kỳ).
  - [P1] Làm tiếp các trang tỷ giá đảo `VND sang [Ngoại tệ]` và viết thêm bài blog tài chính.
  - [P1] Cùng Design Studio hoàn thiện bản vẽ giao diện game Điểm Tín Dụng CIC.
- **Vehicle Hub:**
  - [P0] Phát hành chính thức trang Nộp Phạt CSGT trên Production, nối từ trang tra cứu phạt nguội.
  - [P0] Hoàn thành tích hợp dữ liệu 41 hãng xe và gara cùng team VTTI.
  - [P1] Hoàn thiện menu tiện ích giao thông `/tien-ich-giao-thong` và đưa công cụ tính khấu hao xe lên Staging.
- **Insurtech & New User:**
  - [P1] Đưa trang chủ Bảo hiểm mới (`/bao-hiem`) lên Production sau khi team duyệt.
  - [P1] Theo dõi số lượt cài app thực tế từ trang `/tai-app` để bám sát mục tiêu 30.000 lượt tải/tháng.
- **Lottery Hub:**
  - [P1] Hướng dẫn PO vé số dùng công cụ MoSpark trên Staging để tự sửa nội dung.

### 2. Các Nền Tảng Kỹ Thuật (Platform Projects)
- **CMS & Admin Panel:**
  - [P0] Build Production Phase 2 cho Admin Panel cùng nhánh BMC vào ngày 02/11/2026.
  - [P0] Lập trình giao diện viết bài mới trên MoSpark CMS, hỗ trợ xem trước trên điện thoại và máy tính.
- **Bảo Mật & Hạ Tầng:**
  - [P0] Hoàn thành chuyển đổi luồng dữ liệu Merchant sang Server-side Proxy trước ngày 05/11.
  - [P0] Bật giới hạn tần suất gọi API (Rate Limiting) trên toàn bộ các API công khai của Web Platform.
- **Tìm Kiếm & Dữ Liệu:**
  - [P0] Chạy thử bảng danh mục URL (`tblWebsiteUrlCatalog`) trên Staging và kết nối thử luồng đồng bộ từ CMS.
  - [P1] Đo lường hiệu quả của thẻ chuyển tiền nhanh và banner bạn mới trên trang tìm kiếm `/tim-kiem`.
- **AI & Design System:**
  - [P1] Nối dữ liệu báo cáo GA4/GSC vào mô hình AI để tự động tạo báo cáo phân tích hàng tuần.
  - [P1] Mở rộng thanh menu 2 tầng sang Cinema Hub và Vehicle Hub; phát hành tài liệu MoBase v2.1.
"""

# Write to local file
with open("07_REPORTS/docs/weekly-report-2026-10-26-11-01.md", "w") as f:
    f.write(content.strip() + "\n")

# Copy to Hubs repo
hubs_path = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md")
with open(hubs_path, "w") as f:
    f.write(content.strip() + "\n")

print("Generated clean human report in both locations successfully.")

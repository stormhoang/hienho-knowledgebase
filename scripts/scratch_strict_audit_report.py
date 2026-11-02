# -*- coding: utf-8 -*-
from pathlib import Path

content = """# BÁO CÁO TIẾN ĐỘ TUẦN - WEB PLATFORM
> **Kỳ báo cáo:** Tuần 44 (26/10 - 01/11/2026) | **Cập nhật:** 02/11/2026
> **Đội ngũ thực hiện:** Kỹ thuật & Sản phẩm Web Platform (Chủ trì: Văn Hiến)
> **Nguồn tổng hợp:** 6 báo cáo trực tiếp từ đội ngũ kỹ sư trên Google Drive (`duy.tran2`, `hieu.nguyen8`, `hung.nguyen9`, `nhat.bui1`, `Hoan.md`, `2026-W44_thuanvo.md`) kèm số liệu GA4, AppsFlyer và Excel SSOT.

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
- **Lưu lượng tự nhiên (Non-Paid) bù được một nửa lượng view bị hụt do cắt Ads:** Non-Paid tháng 10 đạt 3,12 triệu PV (+13,5% so với tháng 9), chiếm 86,9% tổng view toàn trang. Khi cắt 723K view quảng cáo, lượng view tự nhiên tăng thêm đã bù lại được 52% phần hụt này.
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

---

## II. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN CHIẾN LƯỢC (USE CASES)
*(Tổng hợp trực tiếp từ báo cáo của Hoan, hung.nguyen9, nhat.bui1, thuanvo)*

### 1. Cinema Hub: Lên Prod Trang Diễn Viên, Suất Chiếu Cinetour & Tối Ưu Minigame Bò Sữa Bay
- **Kỹ sư & Đầu mối thực hiện:** Hoan, hung.nguyen9, thuanvo (Phối hợp BU Movies: Bình, Thức)
- **Công việc thực tế đã làm trong tuần:**
  - **Lên Production trang danh sách diễn viên tổng (`/cinema/person`):**
    - Link chạy thật: [momo.vn/cinema/person](https://www.momo.vn/cinema/person) *(hung.nguyen9)*.
    - Xây dựng trang danh mục tập trung toàn bộ kho nghệ sĩ/diễn viên; có khối **Diễn viên nổi bật (Featured Artists)**, bộ lọc tìm kiếm nhanh theo tên, phân trang mượt mà và liên kết điều hướng 2 chiều sang từng phim diễn viên tham gia để tăng sức mạnh SEO.
  - **Tích hợp hiển thị suất chiếu Cinetour (API mới):**
    - Kết nối API Suất chiếu mới từ Backend, bóc tách riêng các suất chiếu có đoàn làm phim/nghệ sĩ giao lưu trực tiếp tại rạp *(hung.nguyen9)*.
    - Gắn nhãn **Badge Cinetour highlight nổi bật** (nhận diện suất giao lưu, thời gian, rạp chiếu) và tích hợp nút đặt vé nhanh.
  - **Tối ưu thứ hạng phim rạp & cụm rạp đối tác:**
    - Các trang phim chiếu rạp (*Bò Sữa Bay*, *Chị Chị Em Em 3*, *Godzilla Trừ Không*) giữ vững vị trí Top 5 Google *(Hoan)*.
    - Từ khóa thương hiệu rạp đối tác `metiz cinema` lên **Top 3 SERP**; hoàn thành cập nhật UI cho Starlight Cinema và Cinemax; viết bổ sung 3 bài blog mới *(Hoan)*.
    - Sửa lỗi rớt hạng trang rạp CGV: Cập nhật lại Schema lịch chiếu và dùng mô hình AI Qwen (API free) tóm tắt nhanh đánh giá của khán giả từ Google Maps để bổ sung nội dung trang, kéo CGV về lại top 5 *(Hoan)*.
  - **Xử lý Minigame Bò Sữa Bay (`/cinema/bo-sua-bay-25058`):**
    - Phim khởi chiếu ngày 06/11. Game gắn trên trang phim, phát cùng video tại các cụm rạp kèm mã QR để khán giả quét chơi *(thuanvo)*.
    - Game cũ bị vướng quy định đối tác rạp chiếu nên team chuyển sang format Quiz tương tác trả về mã ưu đãi vé xem phim cho New/Current User; hiện game đang hoàn thiện và chờ Legal duyệt *(Hoan, thuanvo)*.
- **Điểm nghẽn:** Chờ Legal phê duyệt luật chơi và BU Movies duyệt kịch bản TVC minigame tại rạp.

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

### 2. Financial Hub: Hoàn Thành Trang Chứng Chỉ Quỹ SIP, Tool Thuế TNCN & Thuế Hộ Kinh Doanh
- **Kỹ sư & Đầu mối thực hiện:** nhat.bui1, Hoan
- **Công việc thực tế đã làm trong tuần:**
  - **Trang Chứng Chỉ Quỹ SIP (`/tai-chinh/chung-chi-quy` - Staging):**
    - Link Staging: [momo-stg.mservice.io/tai-chinh/chung-chi-quy](https://momo-stg.mservice.io/tai-chinh/chung-chi-quy) *(nhat.bui1)*.
    - Cập nhật UI/UX tool tích sản định kỳ từ 10.000đ theo góp ý của BU; chốt Phase 1 dùng dữ liệu định kỳ (danh mục quỹ, tỷ suất sinh lời quá khứ) dẫn phễu mở tài khoản in-app trong lúc chờ API NAV realtime từ các quỹ đối tác. Trạng thái: Đã hoàn thành chỉnh sửa, chờ BU duyệt nội dung để lên prod.
  - **Tool & Trang Tính Thuế / Quyết Toán Thuế TNCN (`/tai-chinh/thue-thu-nhap-ca-nhan` - Demo):**
    - Link Demo: [momovn-dev.mservice.io/tai-chinh/thue-thu-nhap-ca-nhan](https://momovn-dev.mservice.io/tai-chinh/thue-thu-nhap-ca-nhan) *(nhat.bui1)*.
    - Xây dựng tool quyết toán thuế TNCN đa nguồn (lương công ty, vãng lai 10%, freelance), áp dụng biểu thuế lũy tiến hiện hành và dự thảo luật mới; hoàn thiện bài viết hướng dẫn và gắn menu liên kết `TaxHubNav`.
  - **Tool & Trang Tính Thuế Hộ Kinh Doanh (`/tai-chinh/thue-ho-kinh-doanh` - Demo):**
    - Link Demo: [momovn-dev.mservice.io/tai-chinh/thue-ho-kinh-doanh](https://momovn-dev.mservice.io/tai-chinh/thue-ho-kinh-doanh) *(nhat.bui1)*.
    - Xây dựng tool tính thuế cho hộ kinh doanh cá thể, bán hàng online TMĐT (Shopee, TikTok Shop) và cho thuê tài sản theo Thông tư 40 với ngưỡng doanh thu mới 200 triệu; liên kết chéo qua `TaxHubNav`.
  - **Mở rộng trang Tỷ Giá & Blog:**
    - Đưa lên Production 7 trang Tỷ Giá mới, toàn bộ đều lọt vào `~Top 10 Google`; viết bổ sung 9 bài blog tài chính *(Hoan)*.
- **Kế hoạch tuần tới của nhat.bui1:**
  - Nghiên cứu và dựng tiếp công cụ **Chia hóa đơn & Quỹ nhóm** (`/tai-chinh/cong-cu/chia-tien-du-lich`): giải quyết bài toán tính tiền, bù trừ công nợ sau chuyến đi và tạo thói quen dùng tính năng Quỹ nhóm in-app.
  - Nghiên cứu trang danh mục công cụ tập trung **`/cong-cu`** (Tool Directory) gom toàn bộ tiện ích tài chính của MoMo.
  - Làm tiếp các trang tỷ giá đảo `VND sang [ngoại tệ]` *(Hoan)*.
- **Điểm nghẽn:** Chờ BU Tài chính duyệt trang Chứng Chỉ Quỹ SIP và review 2 trang tính thuế.

| Phân loại Dịch vụ / Tiện ích | T9/2026 (Full) | T10/2026 (Full 31d) | Tăng/Giảm vs. T9 | % MoM | Đánh Giá Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Financial Hub** | **249.823** | **254.077** | **+4.254** | **+1.7%** | Tăng nhẹ +1,7%; Trung tâm tài chính & Ví Trả Sau tăng giúp bù cho Vay Nhanh |
| **Điểm Tín Dụng** | 79.092 | 79.987 | **+895** | **+1.1%** | Giữ đều quanh mức 80K view, đang thử nghiệm đưa Quiz vào blog |
| **Ví Trả Sau** | 42.174 | 59.537 | **+17.363** | **+41.2%** | Tăng tốt (+41,2%) nhờ người dùng tìm kiếm tự nhiên và đọc cẩm nang |
| **Vay Nhanh** | 109.955 | 57.512 | **-52.443** | **-47.7%** | Giảm mạnh do cắt quảng cáo, cần kéo lại bằng bài viết SEO và tiện ích thuế |
| **Trung Tâm Tài Chính** | 8.025 | 38.013 | **+29.988** | **+373.7%** | Tăng mạnh (+373,7%) nhờ đưa 7 trang Tỷ Giá mới lên trang web |
| **Quản Lý Chi Tiêu** | 1.000 | 4.829 | **+3.829** | **+382.9%** | Tăng nhờ có thêm loạt bài viết hướng dẫn quản lý tài chính cá nhân |
| **Mở Thẻ Tín Dụng** | 1.464 | 3.397 | **+1.933** | **+132.0%** | Tăng nhờ có bảng so sánh quyền lợi các loại thẻ tín dụng |
| **Túi Thần Tài** | 2.077 | 2.135 | **+58** | **+2.8%** | Lượng người xem duy trì ổn định |

---

### 3. Vehicle Hub: Danh Sách Gara Mới, Tool Maps & Menu Bảo Hiểm Xe Máy
- **Kỹ sư thực hiện:** thuanvo
- **Công việc thực tế đã làm trong tuần:**
  - **Danh sách gara mới (`/tien-ich-giao-thong/garage`):** Thẻ gọn không ảnh, bố cục 3 cột, hiển thị 9 gara mỗi lượt kèm nhãn đối tác bảo hiểm liên kết; người dùng đã cấp quyền vị trí sẽ thấy ngay gara gần nhất (xong phần code, chờ gỡ nút thử nghiệm để phát hành).
  - **Công cụ danh sách gara theo đối tác:** Danh sách khóa sẵn đối tác và lọc hãng xe có bản đồ; code xong, chờ gắn vào luồng mua bảo hiểm.
  - **Chạy hàng loạt tìm gara trên Google Maps (Admin):** Chạy đủ 100 gara một lượt để bổ sung ảnh, giờ mở cửa, đánh giá từ Google Maps làm sạch dữ liệu. Đã xử lý xong lỗi tìm kiếm theo tên hiển thị.
  - **Menu trang bảo hiểm xe máy (`/bao-hiem-xe-may`):** Đã lên trang thật ngày 02/11.
  - **Trang bãi đỗ xe:** Đang lập phương án thiết kế.
  - **Báo cáo nhu cầu tìm kiếm:** Đã hoàn thành và dùng được.
- **Điểm nghẽn & Việc tiếp theo:** Gỡ nút thử nghiệm để phát hành trang Gara; chạy lại 28 gara đối tác báo lỗi và rà soát 10 nhóm gara trùng để trình BU phương án gộp.

| Phân loại Tiện ích / Dịch vụ | T9/2026 (Full) | T10/2026 (Full 31d) | Tăng/Giảm vs. T9 | % MoM | Đánh Giá Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Vehicle Hub** | **66.808** | **61.969** | **-4.839** | **-7.2%** | Tiện ích giao thông tăng tốt giúp bù phần nào lượng sụt giảm của Phạt nguội |
| **Bảo Hiểm Ô Tô** | 19.022 | 22.332 | **+3.310** | **+17.4%** | Tăng +17,4% sau khi chuyển sang MoSpark và làm lại widget báo giá |
| **Phạt Nguội** | 39.382 | 22.255 | **-17.127** | **-43.5%** | Giảm do mùa vụ và cạnh tranh thứ hạng tìm kiếm, cần tối ưu lại SEO on-page |
| **Tiện Ích Giao Thông** | 1.179 | 11.895 | **+10.716** | **+908.9%** | Tăng mạnh nhờ trang Giá xăng và bảng tra cứu thông tin xe |
| **Bảo Hiểm Xe Máy** | 6.178 | 4.482 | **-1.696** | **-27.5%** | Giảm theo xu hướng chung của nhóm bảo hiểm xe máy |
| **Phí Không Dừng** | 1.047 | 1.005 | **-42** | **-4.0%** | Duy trì ổn định quanh mức 1.000 view/tháng |

---

### 4. Insurtech Hub: Lên Trang Thật `/bao-hiem` & Hoàn Thành Công Cụ Mức Khấu Trừ
- **Kỹ sư thực hiện:** thuanvo
- **Công việc thực tế đã làm trong tuần:**
  - **Trang chủ Bảo hiểm (`/bao-hiem`):** Đã lên trang thật ngày 30/10 tại [momo.vn/bao-hiem](https://www.momo.vn/bao-hiem). Gom 9 nhóm sản phẩm bảo hiểm, hiển thị khối tra cứu BHYT, tính BHXH và báo giá ô tô; hiện còn phần nội dung text đang chờ BU duyệt.
  - **Công cụ mức khấu trừ bảo hiểm ô tô:** Mô phỏng 4 mức khấu trừ theo ví dụ xe mới 800 triệu, phí gốc 8 triệu/năm để người dùng biết chọn mức khấu trừ cao thì phí giảm bao nhiêu; code xong, chờ phát hành lên trang `/bao-hiem-o-to/vat-chat-xe`.
- **Điểm nghẽn:** Chờ BU Bảo hiểm duyệt nội dung trang `/bao-hiem` và xếp lịch phát hành công cụ khấu trừ.

---

### 5. New User Hub: Trang Tải App `/tai-app` Đã Lên Trang Thật & Kết Quả Chốt Tháng
- **Kỹ sư thực hiện:** thuanvo
- **Công việc thực tế đã làm trong tuần:**
  - **Trang tải app chính thức (`/tai-app`):** Đã lên trang thật ngày 30/10 tại [momo.vn/tai-app](https://www.momo.vn/tai-app). Tự động nhận diện thiết bị (trên mobile mở App Store / Google Play, trên desktop hiện mã QR rõ nét). Hiện đang làm tiếp khối hiển thị đánh giá của người dùng.
  - **Số liệu New User Full Month (AppsFlyer):** Đạt 11.143 Installs, 3.902 REG (35%) và 2.389 người liên kết ngân hàng (tăng +5% so với tháng 9, đạt đỉnh mới).
  - **Cụm Paid Ads tương tác tài chính (Điểm Tín Dụng + Quýt):** Đạt 65.219 phiên quảng cáo (chiếm 22,4% toàn web), mang về 36.950 lượt bấm OneLink mở app.
- **Kế hoạch tiếp theo:** Hoàn thành khối đánh giá người dùng và phối hợp Growth Team theo dõi số lượt tải app thực tế.

---

### 6. Lottery Hub: Sẵn Sàng Công Cụ MoSpark Trên Staging
- **Kỹ sư thực hiện:** duy.tran2
- **Công việc thực tế đã làm trong tuần:**
  - Đã chuẩn bị sẵn công cụ MoSpark trên môi trường Staging, sẵn sàng hướng dẫn PO vé số vào tự thay đổi nội dung chữ và banner trên trang.
  - Giữ hiển thị 8 trò chơi Vietlott và bảng kết quả XSKT 3 miền ổn định trên điện thoại, tải dưới 1,5 giây giờ cao điểm 18h00 - 18h30.
- **Kế hoạch tiếp theo:** Hướng dẫn PO vé số thao tác trên Staging khi PO bắt đầu làm quen.

---

## III. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN NỀN TẢNG (PLATFORM PROJECTS)
*(Trích xuất trực tiếp từ báo cáo của duy.tran2, hieu.nguyen8, hung.nguyen9, thuanvo)*

### 1. Chatbot AI & Hệ Thống Cơ Sở Tri Thức (Knowledge Base)
- **Kỹ sư chủ trì:** duy.tran2
- **Công việc thực tế đã làm trong tuần:**
  - **Project Center:** Bảng điều khiển trung tâm theo dõi số lượng tài liệu đã đồng bộ, số cụm chủ đề, trạng thái đồng bộ và thời gian cập nhật gần nhất cho từng dự án Chatbot.
  - **Sitemap & Link Scanner:** Tự động đọc `sitemap.xml`, so khớp với kho tài liệu tri thức, phân loại tài liệu thiếu (*Missing*) vs đã đồng bộ (*Synced*), tính tỷ lệ bao phủ tri thức (% Coverage).
  - **Eligibility Validation:** Tự động kiểm tra chất lượng bài viết trước khi nạp vào AI (chỉ nhận bài blog đã xuất bản chính thức; trang web phải có ít nhất 1 khối văn bản dài hoặc khối FAQ thực tế; gắn nhãn cảnh báo lý do không đủ điều kiện).
  - **Web Pages Tree:** Đồng bộ tri thức trực tiếp từ cây danh mục trang web (1-chạm hoặc theo link tùy chọn).
  - **Chuẩn hóa trích xuất:** Lọc bỏ banner, nút bấm trang trí; chỉ lấy phần chữ giàu tri thức (tiêu đề, tóm tắt, từ khóa, H2, nội dung chi tiết, FAQ) cho LLM.
- **Kế hoạch tuần sau:** Hoàn thiện bộ tiêu chí đánh giá chất lượng câu trả lời của Chatbot và theo dõi tỷ lệ bao phủ tri thức trên các trang dịch vụ trọng điểm.

---

### 2. Admin Panel: All-in-One Editor & Khối Nội Dung In-App (Build Prod Phase 2)
- **Kỹ sư chủ trì:** hieu.nguyen8 (phối hợp duy.tran2)
- **Công việc thực tế đã làm trong tuần:**
  - **All-in-One Editor:** Hợp nhất công cụ soạn thảo cho các trang chuyên biệt, gom chỉnh sửa nội dung, danh sách bài, banner và xem trước lên cùng 1 màn hình.
  - **Phân quyền tài khoản:** Tách bạch rõ quyền giữa người tạo bài viết và người duyệt bài; bổ sung nút chuyển nhanh sang danh sách bài chờ duyệt.
  - **Đóng gói khối nội dung In-App nâng cao:**
    - *Khối Voucher:* Nhập tiêu đề, quyền lợi, mã voucher, hạn dùng; tự sinh thẻ ưu đãi chuẩn MoMo kèm nút sao chép mã.
    - *Khối Hướng dẫn từng bước:* Thêm/sắp xếp các bước có ảnh minh họa, tiêu đề, mô tả; tự sinh khối trình chiếu mô phỏng điện thoại.
    - *Live Mobile Preview:* Khung xem trước trực tiếp ngay trong màn hình chỉnh sửa in-app.
  - **Chuẩn bị hoàn tất nghiệm thu Phase 2:** Kiểm thử tự động (Unit Test), làm sạch mã nguồn, chốt ngày build production Phase 2 vào ngày **02/11/2026** cùng nhánh BMC.
- **Kế hoạch tuần sau:** Theo dõi vận hành sau đợt build prod ngày 02/11 và hỗ trợ các Cell Teams dùng các khối nội dung mới.

---

### 3. Cổng Tìm Kiếm Website (`/tim-kiem`) & Hồ Danh Mục URL Toàn Website (URL Catalog)
- **Kỹ sư chủ trì:** hieu.nguyen8
- **Công việc thực tế đã làm trong tuần:**
  - **Thẻ chuyển tiền nhanh qua số điện thoại:** Nhập số điện thoại hợp lệ vào ô tìm kiếm thì web tự hiện thẻ chuyển tiền dẫn vào app MoMo (nhận diện số điện thoại hoàn toàn phía trình duyệt, không gửi lên server để bảo mật).
  - **Banner người dùng mới:** Gắn banner hướng dẫn nhận quà và tải app cho khách lần đầu vào trang tìm kiếm.
  - **Hồ danh mục URL toàn website (URL Catalog):**
    - Chốt 4 quyết định thiết kế: Định danh rút gọn theo dự án để sinh Sitemap riêng; lọc theo dự án con; đồng bộ tự động trước mắt cho Bài viết, Blog và Trang dịch vụ.
    - Lộ trình 4 giai đoạn: (1) Tạo bảng nạp 51 trang tìm kiếm ưu tiên; (2) Lớp đọc dữ liệu có cache; (3) Chuyển Tìm kiếm sang đọc từ Hồ danh mục; (4) Đồng bộ tự động từ CMS/MoSpark và sinh Sitemap theo dự án.
- **Kế hoạch tuần sau:** Theo dõi số liệu thẻ chuyển tiền và banner bạn mới trên bản thật; bắt đầu tạo bảng dữ liệu trên môi trường phát triển và nạp 51 trang tìm kiếm ban đầu.

---

### 4. Bảo Mật Dữ Liệu Web & Hạ Tầng MoMo API
- **Kỹ sư thực hiện:** thuanvo, hieu.nguyen8
- **Công việc thực tế đã làm trong tuần:**
  - **Bảo mật dữ liệu web (thuanvo):** Khóa quyền đọc trực tiếp dữ liệu từ bên ngoài (Anonymous read), chuyển luồng dữ liệu quảng cáo, giá xăng và địa điểm của 19 trang web sang gọi qua máy chủ `momo.vn` (Server-side Proxy / Public RPC API).
  - **Vận hành API (hieu.nguyen8):** Mở kết nối môi trường dev nội bộ gọi tới API test và API chính; cập nhật thư viện dùng chung; bổ sung cấu hình kết nối trung tâm dữ liệu ổn định sau khi triển khai.
- **Kế hoạch tuần sau:** Tiếp tục theo dõi độ ổn định của API và hỗ trợ triển khai lớp máy chủ trung gian cho dữ liệu Merchant.

---

### 5. MoBase Design System: Header Advance (Navigation 2 Tầng)
- **Kỹ sư thực hiện:** hung.nguyen9
- **Công việc thực tế đã làm trong tuần:**
  - Đưa component **Header Advance (Navigation 2 tầng)** lên môi trường Staging trang chủ ([momo-stg.mservice.io](https://momo-stg.mservice.io/)), cho phép cấu hình linh hoạt menu chính, menu phụ, icon và nút CTA từ MoSpark CMS; kiểm tra responsive trên mobile, tablet và desktop.
- **Kế hoạch tuần sau:** Kiểm tra tương thích và chuẩn bị đưa Header Advance lên trang chủ bản chính thức.

---

### 6. Web Performance GA4 · GSC (Admin MoSpark) & Quiz Blog
- **Kỹ sư thực hiện:** thuanvo
- **Công việc thực tế đã làm trong tuần:**
  - **Web Performance GA4 · GSC:** Dự án chuyển kết nối Google Search Console và GA4 sang máy chủ riêng để mở rộng cho PM/BU xem số liệu an toàn trong MoSpark Admin (Analytics › Web Performance); hiện code xong, đang chờ DevOps dựng máy chủ riêng.
  - **Quiz trong bài blog:** Đang làm thử nghiệm gắn quiz tương tác điểm tín dụng vào bài blog (`/tai-chinh/blog/co-nen-mo-the-tin-dung-5138`).
- **Kế hoạch tuần sau:** DevOps mở quyền truy cập máy chủ để kết nối bảng số liệu; tiếp tục chạy thử quiz trên trình duyệt thật.

---

## IV. ĐIỂM NGHẼN & VIỆC CẦN PHỐI HỢP LIÊN PHÒNG BAN
*(Trích xuất đúng theo các vướng mắc thực tế được kỹ sư nêu trong báo cáo)*

1. **Phối hợp BU Movies:** Duyệt kịch bản TVC phát tại rạp (Rio, Touch, Metiz) và cấp mã ưu đãi vé xem phim cho minigame Bò Sữa Bay trước ngày chiếu 06/11 *(Hoan, thuanvo)*.
2. **Phối hợp Legal:** Phê duyệt điều khoản và thể lệ minigame Bò Sữa Bay *(thuanvo)*.
3. **Phối hợp BU Dịch Vụ Tài Chính:** BU duyệt nội dung trang Chứng Chỉ Quỹ SIP (`/tai-chinh/chung-chi-quy`) trên Staging để lên Production; review 2 công cụ tính thuế TNCN và Hộ kinh doanh *(nhat.bui1)*.
4. **Phối hợp BU Bảo Hiểm (Insurtech):** Duyệt nội dung text cho trang chủ Bảo hiểm mới (`/bao-hiem`) đã lên trang thật; xếp lịch phát hành công cụ khấu trừ bảo hiểm ô tô *(thuanvo)*.
5. **Phối hợp BU Giao Thông (VTTI):** Rà soát lại 28 gara lỗi và 10 nhóm gara trùng lặp để gộp dữ liệu sạch *(thuanvo)*.
6. **Phối hợp DevOps Team:** Dựng máy chủ riêng cho bảng Web Performance GA4/GSC trong MoSpark Admin để mở quyền truy cập an toàn *(thuanvo)*.
7. **Phối hợp BMC Team:** Chốt lịch build Production Phase 2 Admin Panel vào ngày 02/11/2026 *(hieu.nguyen8, duy.tran2)*.

---

## V. KẾ HOẠCH CÔNG VIỆC TRỌNG TÂM TUẦN TỚI
*(Tổng hợp đúng theo kế hoạch tuần sau của từng kỹ sư)*

### 1. Nhóm Dự Án Sử Dụng (Strategic Projects)
- **Cinema Hub:**
  - [P0] Hoàn thiện minigame Quiz Bò Sữa Bay và chờ Legal duyệt trước ngày chiếu 06/11 *(thuanvo, Hoan)*.
  - [P1] Tối ưu lại Schema và review Google Maps qua AI Qwen để kéo thứ hạng trang rạp CGV về top 5 *(Hoan)*.
  - [P1] Kiểm tra độ tương thích và chuẩn bị đưa Header Advance lên trang chủ *(hung.nguyen9)*.
- **Financial Hub:**
  - [P0] Đưa trang Chứng Chỉ Quỹ SIP (`/tai-chinh/chung-chi-quy`) lên Production sau khi BU duyệt *(nhat.bui1)*.
  - [P0] Hoàn tất review 2 trang Tính Thuế TNCN và Thuế Hộ Kinh Doanh để sẵn sàng lên bản thật *(nhat.bui1)*.
  - [P1] Nghiên cứu và dựng tiếp công cụ Chia hóa đơn & Quỹ nhóm (`/tai-chinh/cong-cu/chia-tien-du-lich`) *(nhat.bui1)*.
  - [P1] Nghiên cứu trang danh mục công cụ tập trung `/cong-cu` (Tool Directory) *(nhat.bui1)*.
  - [P1] Làm tiếp các trang tỷ giá đảo `VND sang [ngoại tệ]` *(Hoan)*.
- **Vehicle Hub:**
  - [P0] Gỡ nút thử nghiệm để phát hành trang Gara mới (`/tien-ich-giao-thong/garage`) *(thuanvo)*.
  - [P0] Chạy lại 28 gara lỗi và rà soát 10 nhóm gara trùng trình BU phương án gộp *(thuanvo)*.
  - [P1] Tiếp tục lập phương án trang bãi đỗ xe *(thuanvo)*.
- **Insurtech & New User:**
  - [P1] Chờ BU duyệt nội dung trang `/bao-hiem` và xếp lịch phát hành công cụ mức khấu trừ *(thuanvo)*.
  - [P1] Hoàn thành khối đánh giá người dùng trên trang `/tai-app` *(thuanvo)*.

### 2. Nhóm Nền Tảng Kỹ Thuật (Platform Projects)
- **Admin Panel & Web-in-App (hieu.nguyen8 & duy.tran2):**
  - [P0] Build Production Phase 2 Admin Panel cùng nhánh BMC vào ngày 02/11/2026.
  - [P0] Theo dõi vận hành và hỗ trợ Cell Teams sử dụng các khối nội dung mới (Voucher, Hướng dẫn từng bước, Mobile Preview).
- **Cổng Tìm Kiếm & URL Catalog (hieu.nguyen8):**
  - [P0] Bắt đầu triển khai giai đoạn 1 Hồ danh mục URL: tạo bảng dữ liệu trên môi trường phát triển và nạp 51 trang tìm kiếm ban đầu.
  - [P1] Đo lường tỷ lệ dùng thẻ chuyển tiền qua SĐT và banner bạn mới trên trang tìm kiếm.
- **Chatbot AI & Knowledge Base (duy.tran2):**
  - [P1] Hoàn thiện bộ tiêu chí đánh giá chất lượng câu trả lời của Chatbot và theo dõi tỷ lệ bao phủ tri thức trên các trang dịch vụ trọng điểm.
- **Bảo Mật & Hạ Tầng API (thuanvo, hieu.nguyen8):**
  - [P0] Tiếp tục theo dõi độ ổn định của API và hỗ trợ triển khai lớp máy chủ trung gian (Server-side Proxy) cho dữ liệu Merchant.
  - [P1] Phối hợp DevOps dựng máy chủ riêng cho bảng Web Performance GA4/GSC trong MoSpark Admin.
- **Vé Số MoSpark (duy.tran2):**
  - [P1] Hướng dẫn PO vé số cấu hình nội dung tĩnh trên Staging.
"""

report_path = Path("07_REPORTS/docs/weekly-report-2026-10-26-11-01.md")
with open(report_path, "w") as f:
    f.write(content.strip() + "\n")

hubs_path = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md")
with open(hubs_path, "w") as f:
    f.write(content.strip() + "\n")

print("Strict audit report written successfully to both files.")

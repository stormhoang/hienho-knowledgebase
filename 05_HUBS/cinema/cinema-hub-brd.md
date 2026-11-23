# Cinema Hub

> - **Dự án:** Cinema
> - **Khối phụ trách:** Marketing Distribution Services (MDS) / Web Platform
> - **Owner:** Web Platform Team x BU Movies
> - **Phiên bản:** v4.0 - Tháng 9/2026
> - **Trạng thái:** Active & Production Pilot Ready (`momo.vn/cinema`)

## I. Executive Summary

### 1.1 Core Problems & Objectives
* **Vấn đề thực tế (Problem Statement):** Khách hàng khi có nhu cầu xem phim sẽ chủ động tìm kiếm lịch chiếu/suất chiếu trên Google. Tuy nhiên, MoMo chưa tối ưu hóa chuyên sâu về kỹ thuật và trải nghiệm Web trong các chu kỳ trước, dẫn đến việc chưa khai thác triệt để tệp từ khóa ngành (tổng quy mô nhu cầu tìm kiếm đạt **20.850.490 search volume/tháng** với 12.067 từ khóa, riêng head-term "phim chiếu rạp" đạt ~309.8K search volume/tháng). Đồng thời, việc thiếu cổng thanh toán trực tiếp trên Web (Non-App payment barrier) khiến tỷ lệ chuyển đổi Web-to-App (W2A CR) giảm mạnh từ 12.10% xuống 4.37%, gây lãng phí lượng lớn cơ hội giao dịch.
* **Mục tiêu định lượng H2/2026:** Uplift **100% mọi chỉ số** so với H1/2026:
  * **Organic Traffic:** Đạt **>4.020.000 visits/H2** (so với 2.01M H1).
  * **Total Traffic:** Đạt **>8.070.000 visits/H2** (so với 4.03M H1).
  * **Booking Clicks:** Đạt **>1.740.000 clicks/H2** (so với 870K H1).
  * **Tickets Sold (Số vé bán):** Đạt **>214.292 vé/H2** (so với 107K H1).
  * **Web Purchase Conversion:** Đặt mục tiêu tăng tỷ lệ hoàn tất đơn hàng trên Web lên **≥ 4.50%** nhờ triển khai luồng Native Web Payment.
  * **W2A Conversion:** Theo dõi riêng tỷ lệ người dùng Web nhấp và mở App; chỉ áp dụng cho các luồng chuyển tiếp sang App.
* **Triết lý cốt lõi:** **"Một bộ phim - Trọn vẹn hành trình điện ảnh"**, biến Web `momo.vn/cinema` thành trung tâm kết nối tự động:
  1. **Tìm kiếm 0-Click, giữ chỗ realtime:** Search Google  ➔  Thấy ngay lịch chiếu rạp gần nhất trên Web MoMo mà không cần chuyển app hay nhập lại địa điểm.
  2. **Thanh toán liền mạch Native Web Payment:** Người dùng Non-App có thể hoàn tất mua vé và thanh toán trực tiếp trên Web hoặc chuyển tiếp sang App 1-click.
  3. **Vòng đời nội dung tự động (Lifecycle Automation):** Phim đang chiếu  ➔  Phim hết suất chiếu rạp tự động chuyển hướng sang các nền tảng xem phim OTT đối tác, đảm bảo không lãng phí bất kỳ lượt Traffic nào.

### 1.2 Situation - Complication - Resolution
* **Situation (Bối cảnh & Vị thế):** Cinema là Use Case trưởng thành và có tiềm năng giao dịch lớn nhất của Khối Web Platform (~1M organic/3 tháng Q1/2026, chiếm giữ Top 1 SERP cho từ khóa "vé xem phim"). Website đóng vai trò là **"cửa ngõ đón nhận nhu cầu và cổng dẫn dắt chuyển đổi"** cho hệ sinh thái vé xem phim MoMo.
* **Complication (Khó khăn & Thách thức):** Tỷ lệ chuyển đổi suy giảm do 4 vấn đề cốt lõi:
  1. *Drop-off ở luồng thanh toán:* Khách hàng Non-App bị chặn lại do bắt buộc tải App mới mua được vé.
  2. *Keyword Gap lớn:* Chưa phủ sóng hết tệp từ khóa ngành với tổng quy mô nhu cầu tìm kiếm **20.850.490 search volume/tháng** trên 12.067 từ khóa (bao gồm head-terms lớn như "phimmoi" 1M, "phim" 1M, "cgv" 450K, "phim chiếu rạp" 301K, "lotte cinema" 165K...).
  3. *Rủi ro từ Google AI Overview (AIO):* Thiếu cấu trúc dữ liệu chuẩn Schema khiến Google AI trả về kết quả trực tiếp làm người dùng không click vào Web.
  4. *Nội dung lỗi thời do vận hành thủ công:* Phim hết suất chiếu rạp nhưng Web vẫn hiển thị "Đang chiếu", gây trải nghiệm tệ và lãng phí traffic.
* **Resolution (Giải pháp H2/2026):** Tái cấu trúc toàn diện và chuyển dịch hạ tầng sang nền tảng **MoSpark**, xây dựng **Cinema Hub** theo mô hình Product-Led Growth (PLG) & Hub-and-Spoke. Triển khai **Native Web Payment**, ứng dụng **GenAI Content** tự động hóa vòng đời phim và điều hướng sang các dịch vụ xem phim OTT.

### 1.3 Product-Led Growth (PLG) Drivers
Cơ chế PLG của Cinema Hub dựa trên 5 Điểm Chạm Kích Hoạt (Acquisition & Engagement Hooks) giải quyết tức thời nhu cầu tìm kiếm trên Open Web:

1. **Phễu Tra Cứu Lịch Chiếu Realtime (Acquisition Gate):** Đón nhận nhu cầu tìm "lịch chiếu phim [tên phim] [tỉnh thành]"  ➔  Hiển thị suất chiếu của 13 chuỗi rạp đối tác (CGV, Lotte Cinema, Galaxy Cinema, BHD Star, Beta Cinemas, Cinestar, Mega GS, Cinemax, DCINE, Starlight, Rio Cinemas, Trung Tâm Chiếu Phim Quốc Gia, AEON Beta) theo vị trí GPS realtime.
2. **Phễu Báo Giá & Ưu Đãi Cụm Rạp (Retention Magnet):** Tra cứu bảng giá vé, chương trình khuyến mãi theo từng rạp  ➔  Gợi ý Combo Bỏng Nước & Thẻ quà tặng ưu đãi độc quyền MoMo.
3. **Phễu Bách Khoa Toàn Thư Điện Ảnh & Review (Topical Authority Hook):** Đón đầu nhu cầu tìm trailer, diễn viên, đạo diễn, điểm IMDb/Rotten Tomatoes  ➔  Kích hoạt tính năng đánh giá/review từ cộng đồng người xem MoMo.
4. **Phễu Native Web Payment (Conversion Hook):** Cho phép đặt ghế và thanh toán trực tiếp trên Web không cần mở App đối với khách hàng mới/Non-App.
5. **Phễu Chuyển Đổi Vòng Đời Phim sang OTT (Lifecycle Reminder Hook):** Tự động phát hiện phim đã hết suất chiếu rạp  ➔  Gợi ý link xem trực tuyến trên các nền tảng OTT đối tác (Netflix, VieON, Galaxy Play, FPT Play).

### 1.4 Key Metrics & Targets

#### Dual North Star Metrics



| Platform Layer | North Star Metric | Definition | Target H2/2026 | Strategic Role |
| :--- | :--- | :--- | :--- | :--- |
| **Web Platform** *(Primary Goal)* | **Total Organic Web Traffic** | Tổng số lượt truy cập tự nhiên từ Google Search và AI Search vào Cinema Hub trên Kênh Web mỗi tháng. | **>4.020.082 Visits/H2** *(Uplift 100%)* | Mục tiêu cốt lõi: Đón nhận trọn vẹn nhu cầu tìm kiếm điện ảnh ngoài Open Web, mở rộng tệp Acquisition. |
| **In-App & Web Booking** *(Secondary Layer)* | **Total Tickets Sold** | Tổng số lượng vé xem phim được xuất bản thành công qua luồng Web & Web-to-App. | **>214.292 Vé/H2** *(Uplift 100%)* | Đo lường hiệu quả chuyển đổi kinh doanh trực tiếp cho BU Movies và các chuỗi rạp đối tác. |



#### Web Platform Metric Tree (Chi tiết H2/2026)



| Metric | 2025 Full Year | Q1/2026 (Baseline) | H1/2026 (Actual) | **H2/2026 (Target)** |
| :--- | :--- | :--- | :--- | :--- |
| Organic Traffic | 6,387,700 | 1,066,000 | 2,010,041 | **4,020,082** |
| Total Traffic | 12,425,040 | 2,980,000 | 4,035,028 | **8,070,056** |
| Booking Clicks | 266,258 | 81,517 | 870,467 | **1,740,934** |
| Traffic to App (W2A Users) | 78,735 | 9,866 | 38,079 | **76,158** |
| Transactions (via App/Web) | 52,311 | 9,212 | 48,830 | **97,660** |
| Tickets Sold (Số vé bán) | N/A | N/A | 107,146 | **214,292** |
| **% W2A (Conversion Rate)** | **29.57%** | **12.10%** | **4.37%** | **≥ 4.50%+** |
| W2A MAU (Web in App) | 93,758 | 25,012 | 43,262 | **>60,000** |
| W2A MEU (Web in App) | 264,178 | 71,692 | 123,581 | **>180,000** |
| **GMV Quy Đổi Web-to-App (MAU x 205.000đ)** | **19.22 tỷ đ** | **5.13 tỷ đ** | **8.87 tỷ đ** | **>12.30 tỷ đ** |
| GMV Theo Giao Dịch Thực Thu (Txn x 205.000đ) | 10.72 tỷ đ | 1.89 tỷ đ | 10.01 tỷ đ | **>20.00 tỷ đ** |

#### Web Traffic Performance Theo Tháng (GA4 PageViews, 2026)

Bảng theo dõi lưu lượng Web Cinema Hub hàng tháng, nguồn GA4 Data API (`05_HUBS/cinema/data/cinema_monthly_pv_ga4.json`). Tháng 9 ghi nhận đợt Paid Ads lớn (349.388 PVs, chiến dịch phim mùa cao điểm); tháng 11 là MTD số liệu sạch.

| Tháng | Tổng PageViews | Organic Search | Direct | Paid | Non-Paid | MoM |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Tháng 1 | 582.290 | 512.423 | 40.334 | 3.744 | 578.546 | - |
| Tháng 2 | 1.045.262 | 946.975 | 64.449 | 1.502 | 1.043.760 | **+79.5%** |
| Tháng 3 | 760.092 | 680.941 | 52.489 | 863 | 759.229 | -27.3% |
| Tháng 4 | 852.829 | 629.235 | 93.421 | 2.507 | 850.322 | +12.2% |
| Tháng 5 | 975.266 | 709.388 | 215.513 | 1.427 | 973.839 | +14.4% |
| Tháng 6 | 869.342 | 742.132 | 66.427 | 24.603 | 844.739 | -10.9% |
| Tháng 7 | 808.140 | 715.262 | 61.876 | 6.228 | 801.912 | -7.0% |
| Tháng 8 | 821.166 | 702.545 | 52.741 | 37.232 | 783.934 | +1.6% |
| Tháng 9 | 1.210.599 | 776.998 | 49.213 | 349.388 | 861.211 | **+47.4%** |
| Tháng 10 | 1.097.315 | 918.815 | 70.979 | 26.750 | 1.070.565 | -9.4% |
| **Lũy kế 10 tháng** | **9.022.301** | **7.334.714** | **767.442** | **454.244** | **8.568.057** | - |
| Tháng 11 (MTD 9 ngày sạch, 01-09/11) | 234.277 | - | - | 1.261 | 233.016 | MTD |

*Ghi chú: Tháng 11 mới có dữ liệu lũy kế 9 ngày sạch (đã loại trừ nhiễu vòng lặp GTM ngày 10-11/11); số liệu MTD 15 ngày chuẩn hóa theo báo cáo W46/board report và cơ cấu sub-page chi tiết tại Mục 1.5.D. Direct tháng 5 cao bất thường (215.513) phản ánh đợt chiến dịch/offline activation, cần đối chiếu lại nguồn.*

### 1.5 Phễu Chuyển Đổi Web-to-App & Báo Cáo Quy Đổi Doanh Thu GMV (Chuỗi 2025 - 2026 MTD 10T, cập nhật MTD 11T tại mục D)

Căn cứ dữ liệu đối soát chính thức tiếp nhận từ BU Movies và số liệu giao dịch in-app thực tế từ hệ thống Dashboard vận hành bán vé, hiệu suất chuyển đổi từ Kênh Web sang ứng dụng MoMo (Web-to-App) và doanh thu được xác lập theo hai công thức chuẩn hóa:
* **GMV Thực Thu (Actual GMV - Tiêu chuẩn tài chính SSOT):**
  $$\text{GMV Thực Thu} = \text{Success Transactions} \times \text{AoV (205,000 VND)}$$
* **GMV Tiềm Năng Quy Đổi (Potential Reach GMV):**
  $$\text{GMV Tiềm Năng} = \text{W2A MAU} \times \text{AoV (205,000 VND)}$$
*(Quy chuẩn AoV: 205,000 đồng/đơn hàng, trung bình 2.13 vé/giao dịch, tương đương ~96,000 đồng/vé).*

#### A. Bảng Theo Dõi GMV Web-to-App 10 Tháng Năm 2026 So Với Cùng Kỳ 2025



| Tháng | 2026 W2A MAU | 2026 W2A MEU | GMV W2A 2026 | 2025 W2A MAU | GMV W2A 2025 | Tăng Trưởng YoY GMV |
| :--- | :---: | :---: | ---: | :---: | ---: | :---: |
| Tháng 1 | 5,362 | 20,258 | 1,099,210,000 đ | 2,687 | 550,835,000 đ | +99.6% |
| Tháng 2 | 10,922 | 27,595 | 2,239,010,000 đ | 9,090 | 1,863,450,000 đ | +20.2% |
| Tháng 3 | 8,728 | 23,839 | 1,789,240,000 đ | 4,963 | 1,017,415,000 đ | +75.9% |
| Tháng 4 | 7,300 | 20,020 | 1,496,500,000 đ | 8,855 | 1,815,275,000 đ | -17.6% |
| Tháng 5 | 5,141 | 15,823 | 1,053,905,000 đ | 5,285 | 1,083,425,000 đ | -2.7% |
| Tháng 6 | 5,809 | 16,046 | 1,190,845,000 đ | 2,667 | 546,735,000 đ | +117.8% |
| Tháng 7 | 2,263 | 7,806 | 463,915,000 đ | 4,880 | 1,000,400,000 đ | -53.6% |
| Tháng 8 | 3,757 | 12,962 | 770,185,000 đ | 16,541 | 3,390,905,000 đ | -77.3% |
| Tháng 9 | 8,927 | 26,698 | 1,830,035,000 đ | 14,952 | 3,065,160,000 đ | -40.3% |
| Tháng 10 | 11,457 | 30,470 | 2,348,685,000 đ | 6,092 | 1,248,860,000 đ | **+88.1%** |
| **Lũy kế 10 Tháng** | **69,666** | **201,517** | **14,281,530,000 đ** | **76,012** | **15,582,460,000 đ** | **-8.3%** |



#### B. Báo Cáo Giao Dịch Thực Thu 10 Tháng Năm 2026 (Realtime In-App Dashboard)

Dữ liệu ghi nhận từ hệ thống vận hành bán vé in-app (`SUCCESS IN-APP TRANSACTIONS`) phản ánh số lượng đơn hàng chốt thành công và doanh thu thực tế từ Kênh Web-to-App:



| Kỳ Báo Cáo | MAU | MEU | Đơn | Vé | GMV Thực Thu | Tăng Trưởng MoM | Vé / Đơn |
| :--- | :---: | :---: | :---: | :---: | ---: | :---: | :---: |
| Năm 2025 | 93,758 | 264,178 | 52,311 | 111,422 | 10,723,755,000 đ | - | 2.13 |
| Tháng 1/2026 | 5,362 | 20,258 | 5,889 | 12,643 | 1,207,245,000 đ | -47.4% | 2.15 |
| Tháng 2/2026 | 10,922 | 27,595 | 12,432 | 28,379 | 2,548,560,000 đ | +182.5% | 2.28 |
| Tháng 3/2026 | 8,728 | 23,839 | 9,881 | 20,600 | 2,025,605,000 đ | -23.0% | 2.08 |
| Tháng 4/2026 | 7,300 | 20,020 | 8,221 | 18,730 | 1,685,305,000 đ | -11.7% | 2.28 |
| Tháng 5/2026 | 5,141 | 15,823 | 5,777 | 12,561 | 1,184,285,000 đ | -30.9% | 2.17 |
| Tháng 6/2026 | 7,871 | 16,046 | 9,055 | 19,444 | 1,856,275,000 đ | +56.7% | 2.15 |
| Tháng 7/2026 | 2,263 | 7,806 | 2,425 | 5,211 | 497,125,000 đ | -64.6% | 2.15 |
| Tháng 8/2026 | 3,757 | 12,962 | 4,016 | 8,754 | 823,280,000 đ | - | 2.18 |
| Tháng 9/2026 | 8,927 | 26,698 | 9,807 | 20,983 | 2,010,435,000 đ | +144.2% | 2.14 |
| Tháng 10/2026 | 11,457 | 30,470 | 12,547 | 26,789 | 2,572,135,000 đ | +20.1% | 2.13 |
| **Tổng 9 tháng trực tiếp Dashboard** | **67,971** | **188,555** | **76,034** | **165,340** | **15,586,970,000 đ** | **-** | **2.17** |
| Cộng dồn 10 dòng tháng (tham chiếu) | 71,728 | 201,517 | 80,050 | 174,094 | 16,410,250,000 đ | - | 2.17 |
| **Toàn bộ 10 tháng năm 2026 (Dashboard In-App, chính thức)** | **60,378** | **201,517** | **77,625** | **168,884** | **15,913,125,000 đ** | **-** | **2.18** |



* **Đánh giá tăng trưởng thực tế:** Toàn bộ 10 tháng năm 2026 đã được xác thực chính thức từ dữ liệu vận hành bán vé in-app. Theo Dashboard In-App range T1-T10 (chốt 18/11/2026), kênh Web-to-App đã mang về tổng cộng **77,625 đơn hàng thành công**, bán ra **168,884 vé xem phim** và đóng góp **15.91 tỷ đồng GMV thực thu** cho BU Movies, từ **60,378 người dùng giao dịch** không trùng lặp (vượt toàn bộ năm 2025 **+48.4% về số đơn hàng**, **+51.6% về số vé bán ra** và **+48.4% về GMV thực thu**). Cộng dồn các dòng tháng ra 80,050 đơn / 174,094 vé, cao hơn Dashboard đúng bằng dòng Tháng 7; đang đối soát, SSOT tại `CINEMA_W2A_GMV_PERFORMANCE_2026.md`.

#### C. Phễu Chuyển Đổi Web-to-App Toàn Diện & Phân Tích Điểm Nghẽn OneLink (Cinema Growth Funnel)

Hành trình chuyển đổi từ tìm kiếm tự nhiên ngoài Open Web vào App và tạo ra doanh thu thực tế được chuẩn hóa qua mô hình Phễu Chuyển Đổi Toàn Diện 6 tầng (End-to-End Cinema Growth Funnel):

##### 1. Sơ Đồ Dòng Chảy Phễu Cinema Hub (Flowchart TD)

```mermaid
flowchart TD
    subgraph T1 ["TẦNG 1: SEARCH ENGINE & KHÁM PHÁ (AWARENESS)"]
        A1["Google SERP Impressions<br/>282.9M lượt hiển thị/năm<br/>(Lịch chiếu, Cụm rạp, Review, Giá vé)"]
    end

    subgraph T2 ["TẦNG 2: THU HÚT & DUYỆT THÔNG TIN TRÊN WEB (ACQUISITION)"]
        B1["Tổng Lưu Lượng Web MoMo Cinema<br/>12.4M Pageviews/năm (~1.1M PV/tháng)"]
        B2["Trang Cụm Rạp & Lịch Chiếu: 61.3% PV<br/>(CGV, Lotte, BHD, Galaxy, Beta, NCC)"]
        B3["Trang Chi Tiết Phim & Trailer: 33.5% PV<br/>(Nội dung phim, Diễn viên, Suất chiếu)"]
        B4["Review Hub, Box Office & Blog: 5.2% PV<br/>(Đánh giá phim, BXH Doanh thu, Cẩm nang)"]
        B5["Trợ Lý AI Phòng Vé & Minigame Tương Tác<br/>(Giải tỏa băn khoăn & Thẻ gợi ý 1-chạm)"]
    end

    subgraph T3 ["TẦNG 3: KÍCH HOẠT Ý ĐỊNH ĐẶT VÉ (CONSIDERATION & INTENT)"]
        C1["Nhấp Nút Đặt Vé / Giữ Chỗ (Booking Clicks)<br/>266,258 Clicks/năm (CTR: 2.14% trên PV)"]
    end

    subgraph T4 ["TẦNG 4: CẦU NỐI CHUYỂN TIẾP WEB-TO-APP (ONELINK & BRIDGE)"]
        D1["Hệ Thống Cầu Nối Chuyển Tiếp Web-to-App<br/>(Contextual OneLink + Dynamic QR Desktop)"]
        D2["Điểm Nghẽn Rò Rỉ Kỹ Thuật (Rơi rớt 70.4%)<br/>(Trình duyệt chặn mở App, Desktop thiếu QR)"]
        D3["Mở App MoMo Thành Công (Tỷ lệ W2A: 29.57%)<br/>78,735 lượt vào App / 93.8K W2A MAU"]
    end

    subgraph T5 ["TẦNG 5: THANH TOÁN & DOANH THU GMV TRÊN APP (CONVERSION & REVENUE)"]
        E1["Chốt Đơn Bán Vé In-App Thành Công (CR: 66.44%)<br/>77,625 đơn hàng / 168,884 vé (Lũy kế 10T 2026)<br/>(52,311 đơn cả năm 2025)"]
        E2["Doanh Thu Thực Thu Kênh Web-to-App<br/>15.91 tỷ đồng GMV (Lũy kế 10T 2026)<br/>(Đóng góp 10.72 tỷ đồng năm 2025)"]
        E3["Bàn Giao Khách Hàng Mới Cho BU Movies<br/>(Chuyển tiếp vào phễu Loyalty & Nuôi dưỡng của BU)"]
    end

    A1 -->|"SERP CTR: 4.39%"| B1
    B1 --> B2 & B3 & B4
    B2 & B3 & B4 -.->|"Tư vấn ngữ cảnh"| B5
    B2 & B3 & B4 -->|"Nhấp Đặt Vé trên trang"| C1
    B5 -->|"Chạm thẻ gợi ý 1-chạm"| C1
    C1 -->|"Kích hoạt OneLink điều hướng"| D1
    D1 -.->|"Rò rỉ chuyển giao (70.43%)"| D2
    D1 -->|"Chuyển tiếp thành công (29.57%)"| D3
    D3 -->|"Chọn ghế & Thanh toán In-App"| E1
    E1 --> E2
    E1 --> E3
```

##### 2. Bảng Bóc Tách Chỉ Số Theo Từng Tầng Phễu Web-to-App (Funnel Metrics Table)

| Tầng Phễu | Chỉ số chính | Giá trị chuẩn (Benchmark 2025) | Giá trị 8 Tháng 2026 | Tỷ lệ chuyển đổi tầng (%CR) | Điểm nghẽn chính | Giải pháp tối ưu hóa |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tầng 1: Search Demand** | Google Search Impressions | 282,940,000 | ~190,000,000 | 4.39% (SERP CTR) | Thứ hạng từ khóa chưa đều ở top 1-3 | Mở rộng SEO cụm rạp địa phương và lịch chiếu |
| **Tầng 2: Web Acquisition** | Total Web Traffic (PV) | 12,425,040 | ~9,200,000 | 100% | Trang tĩnh, thiếu tương tác tư vấn | Tích hợp Cinema Chatbot và Minigame giữ chân |
| **Tầng 3: Intent Activation** | Booking Clicks | 266,258 | ~185,000 | 2.14% (CTR trên PV) | Nút CTA đặt vé chưa nổi bật, thiếu preview rạp | Bổ sung Floating CTA và bảng chọn suất chiếu nhanh |
| **Tầng 4: Web-to-App Bridge** | Traffic inApp (W2A MAU) | 78,735 (93,758 MAU) | 49,282 MAU | **29.57% (%W2A)** | **Rơi rớt 70.4% ở bước OneLink** | Smart Bridge Page, Dynamic QR trên Desktop |
| **Tầng 5: Purchase & GMV** | Transactions / GMV | 52,311 đơn / 10.72 tỷ đ thực thu | 12,547 đơn / 2.57 tỷ đ (T10) | **66.44% (In-App CR)** | Thời gian giữ ghế ngắn, hết suất đẹp | Giữ nguyên ngữ cảnh rạp/suất chiếu từ Web sang App |

* **Phân định ranh giới đo lường (Measurement & Ownership Boundary):** Phễu chuyển đổi Web-to-App kết thúc tại **Tầng 5** khi đơn hàng và doanh thu GMV được ghi nhận thành công trên App MoMo. Toàn bộ các chỉ số về tỷ lệ quay lại mua vé sau đó (In-App MAU Retention 17% - 47%) thuộc hệ thống đo lường hành vi người dùng trong ứng dụng do **BU Movies** độc lập quản trị, Web Platform không đo lường và không nhận sở hữu chỉ số này để tránh gây hiểu nhầm về phạm vi dữ liệu.

##### Bảng Full Funnel Hàng Tháng T1-T10/2026 (GA4 + AppsFlyer Proxy + BU Movies)

Dữ liệu tổng hợp 3 nguồn: **GA4** (event `engage_product_funnel` với `funnel_step`, `funnel_start`, `funnel_complete`, `click_to_app`/`click_outbound_link` lọc `pagePath` chứa `/cinema`), **AppsFlyer proxy** (click link `momoapp.onelink.me` trên `/cinema`), và **BU Movies in-app dashboard** (W2A MAU/MEU/GMV thực thu). File SSOT: `07_REPORTS/data/analytics/cinema_product_funnel_jan_oct_2026.json`, `cinema_app_open_clicks_jan_oct_2026.json`, `05_HUBS/cinema/data/movies_app_w2a_performance.json`.

**Bảng A - Phễu Web (GA4, unique users):**

| Tháng | Pageviews | Users | Sessions | 1. Funnel Start | 2. Seat | 3. Popcorn & Drink | 4. Book Ticket (+QR) | Complete (Web txn) | CR Start → Complete |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| T1 | 582.291 | 199.461 | 325.631 | 36.024 | 9.903 | 8.160 | 6.007 | 6.006 | 16.7% |
| T2 | 1.045.263 | 301.602 | 507.104 | 89.652 | 23.201 | 19.204 | 15.332 | 15.249 | 17.0% |
| T3 | 760.095 | 248.209 | 430.011 | 53.475 | 16.152 | 13.518 | 10.389 | 10.365 | 19.4% |
| T4 | 852.833 | 341.479 | 524.298 | 48.661 | 13.755 | 11.750 | 8.451 | 8.328 | 17.1% |
| T5 | 975.269 | 439.354 | 627.127 | 58.683 | 13.590 | 11.299 | 8.077 | 7.996 | 13.6% |
| T6 | 869.372 | 296.562 | 474.187 | 52.843 | 14.497 | 12.066 | 8.767 | 8.590 | 16.3% |
| T7 | 808.140 | 331.927 | 493.143 | 56.944 | 13.523 | 10.852 | 7.971 | 7.729 | 13.6% |
| T8 | 821.166 | 287.392 | 470.988 | 56.988 | 15.828 | 12.867 | 9.700 | 9.441 | 16.6% |
| T9 | 1.210.595 | 534.011 | 779.655 | 68.039 | 20.434 | 17.074 | 13.171 | 13.164 | 19.4% |
| T10 | 1.097.332 | 388.524 | 640.160 | 85.117 | 29.439 | 24.280 | 19.147 | 19.144 | **22.5%** |

**Bảng B - Cầu nối Web-to-App và chuyển đổi In-App (AppsFlyer proxy + BU Movies):**

| Tháng | OneLink Click Users (proxy) | W2A MAU | W2A MEU* | Transactions | Tickets | GMV Thực Thu (tỷ đ) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| T1 | 0** | 5.362 | 20.258 | 5.889 | 12.643 | 1.21 |
| T2 | 0** | 10.922 | 27.595 | 12.432 | 28.379 | 2.55 |
| T3 | 0** | 8.728 | 23.839 | 9.881 | 20.600 | 2.03 |
| T4 | 145.635** | 7.300 | 20.020 | 8.221 | 18.730 | 1.69 |
| T5 | 2.516 | 5.141 | 15.823 | 5.777 | 12.561 | 1.18 |
| T6 | 4.593 | 5.809 | 16.046 | 9.055 | 19.444 | 1.86 |
| T7 | 5.259 | 2.263 | 7.806 | 2.425 | 5.211 | 0.50 |
| T8 | 5.354 | 3.757 | 12.962 | 4.016 | 8.754 | 0.82 |
| T9 | 5.828 | 8.927 | 26.698 | 9.807 | 20.983 | 2.01 |
| T10 | 7.889 | 11.457 | 30.470 | 12.547 | 26.789 | 2.57 |
| **Lũy kế 10T** | - | **69.666** | **201.517** | **77.625*** | **168.884*** | **14.28** |

\*\*\* Đơn và vé lũy kế lấy theo Dashboard In-App range T1-T10 (chốt 18/11/2026); cộng dồn các dòng tháng ra 80.050 / 174.094, chênh đúng bằng dòng T7, đang đối soát.

\* W2A MEU trong bảng này là **số lượt tương tác in-app** do BU Movies dashboard ghi nhận (hệ số ~2.5-3.8 lượt/MAU), không phải unique engaged users và không phải số lần mở app.

\*\* Cảnh báo chất lượng dữ liệu tracking: (a) T1-T3 = 0 do param OneLink trên `click_to_app`/`click_outbound_link` của `/cinema` chưa được bắn, cần xác nhận với Web Platform; (b) T4 spike 145.635 users OneLink click là bất thường (nghi chiến dịch `/cinema/trai-buon-nguoi-24991/tang-3000-ve` hoặc tag bắn trùng), không dùng T4 làm baseline; (c) click OneLink chỉ là proxy cho "mở app", số mở app/install thật phải lấy từ AppsFlyer.

**Nhận định nhanh từ funnel T1-T10:**

* **Điểm nghẽn cố định ở bước 1 → 2 (Xem suất chiếu → Chọn ghế):** CR chỉ 23-30% quanh năm, T5 và T7 thấp nhất (~23%). Một khi user vào được màn chọn ghế, tỷ lệ đi đến Book Ticket ~72-79% và Complete ~97-100%, tức checkout web gần như không rò rỉ.
* **CR Start → Complete cải thiện rõ ở T10:** đạt 22.5%, cao nhất 10 tháng, tương ứng Complete users 19.144 và W2A MAU in-app 11.457.
* **T10 là tháng đỉnh:** Complete users +45% MoM so với T9 trong khi paid traffic giảm mạnh (349K PVs T9 chủ yếu organic/paid campaign, T10 paid chỉ ~27K), cho thấy chất lượng traffic và intent cải thiện.
* **Bài toán tăng trưởng nằm ở tầng Consideration, không phải checkout:** tối ưu Show Time → Seat (relevance suất chiếu, rạp gần, giá vé, CTA nổi bật) sẽ có đòn bẩy lớn hơn sửa lỗi thanh toán.

##### 3. Phân Tích Hai Nút Thắt Quan Trọng Nhất Của Phễu Web-to-App

* **Nút thắt 1: Rò rỉ lớn nhất ở bước chuyển Web sang App (Tầng 3 sang Tầng 4)**
  * **Hiện tượng:** Có 266,258 người dùng nhấp vào nút "Đặt vé" trên Web, nhưng chỉ có 78,735 lượt vào được App MoMo. Tỷ lệ rơi rớt lên tới 70.43%.
  * **Nguyên nhân cốt lõi:** Trình duyệt Safari chặn deeplink tự động; người dùng truy cập bằng máy tính (Desktop) không có cơ chế chuyển giao tức thì; trang đệm (Bridge Page) tải chậm.
  * **Đòn bẩy kinh tế:** Cải thiện tỷ lệ này từ 29.57% lên 45.0% giúp mang về thêm **+10.03 tỷ đồng GMV/năm** cho BU Movies.

* **Nút thắt 2: Tỷ lệ kích hoạt ý định mua vé trên Web còn thấp (Tầng 2 sang Tầng 3)**
  * **Hiện tượng:** Tỷ lệ nhấp đặt vé mới đạt 2.14% trên tổng lưu lượng 12.4 triệu lượt xem trang.
  * **Nguyên nhân cốt lõi:** Người dùng vào đọc tin tức, review hoặc xem thông tin diễn viên rồi rời đi mà không thấy đường dẫn đặt vé phù hợp với nhu cầu.
  * **Giải pháp:** Chatbot AI đóng vai trò "Trợ lý phòng vé", chủ động gợi ý suất chiếu đẹp và đưa ra thẻ lựa chọn 1-chạm kết nối thẳng vào App MoMo.

* **Cơ Chế Bàn Giao Khách Hàng Cho BU Movies (Post-Conversion Handoff):** Sau khi hoàn tất mua vé tại Tầng 5, khách hàng được bàn giao trọn vẹn cho BU Movies để tiếp tục kích hoạt các chương trình chăm sóc khách hàng in-app (chương trình Loyalty, Tiệm Sưu Tầm, ưu đãi độc quyền) nhằm tối ưu tỷ lệ mua lại cho các bom tấn tiếp theo.

* **Định lượng cơ hội tổng thể (Opportunity Sizing):** Nếu nâng tỷ lệ chuyển tiếp %W2A từ 29.57% lên **45.0%** thông qua Smart Bridge Page và QR động, doanh thu GMV quy đổi sẽ tăng từ 19.22 tỷ đồng lên **29.25 tỷ đồng/năm** (tăng thêm **+10.03 tỷ đồng GMV/năm** cho BU Movies mà không tốn thêm chi phí kéo traffic).

#### D. Cập Nhật Hiệu Suất MTD Tháng 11/2026 (Web Traffic & Phễu Web-to-App)

Số liệu mới nhất tính đến ngày 16/11/2026. Lưu lượng Web là **số liệu sạch** theo cơ chế chuẩn hóa của báo cáo tuần W46 và board report MTD 15d: giữ nguyên PageViews thực cho các ngày bình thường, chuẩn hóa các ngày 10-13/11 (sự cố lặp hit `page_view` trong GTM-P9JDDJZ) bằng Sessions x 1.5. Phễu cài đặt app nguồn AppsFlyer GPD.

**1. Lưu lượng Web Cinema Hub - Lũy kế MTD 15 ngày (01/11 - 15/11/2026)**

| Chỉ số | Giá trị MTD 15d | Target Tháng 11 | Tiến độ |
| :--- | :---: | :---: | :---: |
| **Tổng PageViews Cinema Hub (số sạch)** | **378.569 PVs** | 1.294.630 | **29.2%** (sau 50% thời gian tháng) |
| So với cùng kỳ Tháng 10 (15 ngày đầu) | 654.194 PVs | - | **-42.1% MoM** (downtrend mùa vụ) |

Cơ cấu lưu lượng theo nhóm trang (chuẩn tracking mới):

| Nhóm Trang | PageViews MTD 15d | Tỷ trọng | MoM vs T10 cùng kỳ |
| :--- | :---: | :---: | :---: |
| Cụm rạp đối tác (`Cinema_Cineplex`: CGV, Lotte, BHD, Beta, Cinestar, NCC) | 256.165 | 67.7% | -48.1% |
| Trang phim chi tiết (`Cinema_Page`) | 40.366 | 10.7% | -30.8% |
| Lịch chiếu | 28.739 | 7.6% | **+37.4%** |
| Trang chủ (`Cinema_Home Page`) | 23.759 | 6.3% | +0.8% |
| Chủ đề & Review (sản phẩm mới) | 16.849 | 4.4% | Mới |
| Blog Phim (`Cinema_Blog`) | 10.319 | 2.7% | -22.3% |
| Landing Page & khuyến mãi | 1.031 | 0.3% | -97.6% |
| Khác | 1.341 | 0.4% | -11.5% |

Nhận định: Sụt giảm -42.1% mang tính chu kỳ mùa vụ giữa hai đợt bom tấn, không phải mất nền tảng. T10 hưởng trọn chiến dịch Landing Page đặt vé/khuyến mãi (42,6K PVs, kết thúc T11); T11 là giai đoạn chuyển tiếp trước mùa phim Tết 2027. Điểm bù tích cực: Lịch chiếu +37.4% và nhóm Chủ đề & Review (16,8K PVs, sản phẩm mới) cho thấy content chủ đề đang giảm phụ thuộc vào sóng phim ngắn hạn. Chatbot Cinema (MoSpark Production) đã nghiệm thu kỹ thuật và đang trong lộ trình gắn khung chat lên `www.momo.vn/cinema`.

**2. Phễu Web-to-App theo placement - AppsFlyer MTD 10 ngày (01/11 - 10/11/2026)**

| Tầng phễu | Cinema Hub (placement rạp phim) | CVR tầng | Toàn nền tảng Web (tham chiếu) |
| :--- | :---: | :---: | :---: |
| Cài đặt ứng dụng (App Installs) | 224 | - | 3.171 |
| Đăng ký tài khoản (New Reg) | 58 | 25.9% | 864 (27.2%) |
| Liên kết ngân hàng (Map Bank) | 38 | 65.5% | 533 (61.7%) |
| Người dùng kích hoạt (Active MAU) | 27 | 58.9% | 314 (58.9%) |
| **End-to-End CVR (MAU / Install)** | **12.1%** | - | **9.9%** |

Cinema Hub ghi nhận End-to-End CVR cao nhất toàn Web (12.1% so với mặt bằng chung 9.9%), khẳng định placement rạp phim kéo về tệp khách hàng giải trí chất lượng cao. Đây là phễu đo lường theo campaign placement của AppsFlyer GPD, khác với phễu giao dịch vé in-app (W2A MAU/GMV) tại mục A và B.

**Lưu ý dữ liệu:** Số liệu đơn hàng bán vé in-app và GMV thực thu của Tháng 11/2026 chưa có bản đối soát chính thức từ BU Movies (series hiện tại chốt sổ tới T10/2026: 80.050 đơn, 174.094 vé, 16.41 tỷ đồng). Sẽ cập nhật bổ sung khi dữ liệu đối soát được xác nhận.

## II. Market Context & Strategy

### 2.1 Market Sizing & Opportunity
* **Quy mô thị trường rạp chiếu phim Việt Nam:** Doanh thu thị trường rạp chiếu phim Việt Nam tăng trưởng mạnh mẽ với hơn 45 triệu lượt vé bán ra hàng năm.
* **Mạng lưới đối tác:** MoMo kết nối trực tiếp với 13 chuỗi rạp chiếu phim lớn nhất Việt Nam: **CGV, Lotte Cinema, Galaxy Cinema, BHD Star, Beta Cinemas, Cinestar, Mega GS, Cinemax, DCINE, Starlight, Rio Cinemas, Trung Tâm Chiếu Phim Quốc Gia, AEON Beta**.
* **Xu hướng AI Search & Open Web:** Hơn 85% người xem phim thực hiện tìm kiếm "lịch chiếu phim", "review phim" trên Google trước khi quyết định ra rạp. Việc đón đầu Google AI Overview (AIO) giúp MoMo chiếm lĩnh vị thế Top-of-Mind.

### 2.2 Collaboration Model & Cross-BU Synergy

Dự án được vận hành dưới mô hình đối tác chiến lược giữa **BU Movies** và **Khối Web Platform**:

#### 1. BU Movies (Business Owner)
* **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (P&L, Doanh thu, New Users, MAU, Transactions, Số vé bán).
* **Domain Strategy & Merchant Ecosystem:** Hoạch định chiến lược kinh doanh, đàm phán thương lượng thương mại và định hướng khai thác hệ sinh thái đối tác (13 chuỗi Rạp & Nền tảng OTT).
* **Luồng Gửi Vé & Fulfillment (E-ticket Delivery Ownership):** Chịu trách nhiệm toàn bộ đối với luồng gửi vé điện tử đa kênh sau khi giao dịch hoàn tất (gửi tin nhắn Zalo ZNS, gửi Email xác nhận vé, nhắn SMS mã check-in và gửi thông báo push nhắc giờ xem phim). Quản lý ngân sách và hạ tầng phát hành vé.
* **Kênh Push Marketing Nội Bộ In-App (MDS-Movies Social Post Feed):** Vận hành kênh tin tức In-App Social Post (Feed MoMo) để đăng tải các bài viết truyền thông, tin hot bom tấn và deal ưu đãi, biến đây thành **Kênh Push Marketing Nội Bổ In-App** kéo lượt truy cập (driven-traffic) trực tiếp về Mini App và phối hợp đồng bộ traffic với Web Cinema Hub.
* **Media & Off-Page Investment:** Chủ động đầu tư ngân sách và triển khai các hoạt động Media, Truyền thông PR, Social Marketing và Xây dựng liên kết Off-Page (Backlink Authority) để thúc đẩy độ phủ thương hiệu và sức mạnh SEO của Cinema Hub trên Open Web.

#### 2. Web Platform (Product & Tech Partner)
* **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Trải nghiệm Sản phẩm (Web Product), Tỷ lệ Chuyển đổi (CR) và Tăng trưởng Organic Traffic.
* **Trọng tâm thực thi H2/2026:**
  * **Product-Led Growth (PLG):** Chuyển hóa luồng Booking thành hệ thống thu hút và giữ chân người dùng tự nhiên.
  * **MoSpark Migration:** Hiện đại hóa hạ tầng công nghệ, nâng cao khả năng chịu tải và tốc độ phát triển.
  * **GenAI Content:** Ứng dụng AI tự động hóa sản xuất nội dung theo Content Plan của BU Movies.

### 2.3 Search Demand & Keyword Research

Bộ dữ liệu Keyword Research chuẩn mới nhất của Cinema Hub gồm **12.067 từ khóa hợp pháp độc lập** với tổng quy mô nhu cầu tìm kiếm đạt **20.850.490 lượt/tháng** trên Open Web tại Việt Nam (đã chuẩn hóa và loại bỏ các từ khóa rác).

Dưới đây là Bảng phân tích nhu cầu tìm kiếm theo 7 Cụm Chủ Đề (Themes) và các Cụm Chi Tiết (Sub-Clusters):



| Mã Cụm | Cụm Chủ Đề (Theme Content Plan) | Cụm Chi Tiết (Sub-Cluster Editorial) | Search Volume / Tháng | Tỷ Lệ % | Ý Nghĩa Nhu Cầu Tìm Kiếm (Search Intent) |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **1** | **THƯƠNG HIỆU RẠP & CỤM RẠP ĐỊA PHƯƠNG** | **Tổng Cụm Rạp & Địa Điểm** | **4.633.370** | **22.22%** | **Nhu cầu tìm thương hiệu rạp và rạp gần vị trí người dùng** |
| 1.1 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp CGV Cinema | 1.626.460 | 7.80% | Intent tìm rạp CGV gần nhất, tra cứu lịch chiếu rạp CGV & giá vé CGV. |
| 1.2 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp Galaxy Cinema | 876.400 | 4.20% | Intent tìm lịch chiếu rạp Galaxy và cụm rạp Galaxy gần nhà. |
| 1.3 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp Lotte Cinema | 668.700 | 3.21% | Intent tra cứu rạp Lotte Cinema và vị trí rạp tại các trung tâm thương mại. |
| 1.4 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp Cinestar Cinema | 300.620 | 1.44% | Intent tìm rạp Cinestar, vé xem phim giá rẻ & vé học sinh sinh viên. |
| 1.5 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp Beta Cinemas & AEON Beta | 221.210 | 1.06% | Intent tra cứu rạp Beta Cinemas, suất chiếu & cụm rạp Beta local. |
| 1.6 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Trung Tâm Chiếu Phim Quốc Gia (NCC) | 182.080 | 0.87% | Intent tìm lịch chiếu & giá vé tại Trung Tâm Chiếu Phim Quốc Gia Hà Nội. |
| 1.7 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp Starlight Cinema | 163.090 | 0.78% | Intent tìm rạp Starlight Cinema tại các tỉnh miền Trung & Tây Nguyên. |
| 1.8 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Rạp BHD Star Cinema | 98.180 | 0.47% | Intent tra cứu cụm rạp BHD Star Cineplex tại TPHCM & Hà Nội. |
| 1.9 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Tra Cứu Rạp Theo Tỉnh / Thành (GEO) | 459.530 | 2.20% | Intent tìm địa điểm rạp chiếu phim gần vị trí hiện tại theo Tỉnh/Thành/Quận/Huyện. |
| 1.10 | Thương Hiệu Rạp & Cụm Rạp Địa Phương | Các Chuỗi Rạp Khác (DCINE, Rio, Touch, Mega GS...) | 37.100 | 0.18% | Intent tra cứu thông tin suất chiếu & vị trí các rạp đối tác khác. |
| **2** | **KHÁM PHÁ & GỢI Ý PHIM CHIẾU RẠP** | **Tổng Cụm Gợi Ý & Thể Loại Phim** | **646.650** | **3.10%** | **Nhu cầu khám phá phim rạp mới và tìm gợi ý phim hay** |
| 2.1 | Khám Phá & Gợi Ý Phim Chiếu Rạp | Phim Đang Chiếu Rạp Mới Nhất | 43.020 | 0.21% | Intent khám phá các bộ phim mới công chiếu tại rạp hôm nay. |
| 2.2 | Khám Phá & Gợi Ý Phim Chiếu Rạp | Top Phim Rạp Hay & Phim Hot Tuần Này | 22.540 | 0.11% | Intent tìm kiếm danh sách phim hay, phim được đánh giá cao tuần này. |
| 2.3 | Khám Phá & Gợi Ý Phim Chiếu Rạp | Phim Theo Thể Loại & Quốc Gia (Hành Động, Kinh Dị...) | 581.090 | 2.79% | Intent tìm phim chiếu rạp theo thể loại (hành động, kinh dị, tình cảm, Việt Nam...). |
| **3** | **THÔNG TIN PHIM, VŨ TRỤ PHIM & NHÂN VẬT** | **Tổng Cụm Phim, Vũ Trụ Phim & Diễn Viên** | **13.022.970** | **62.46%** | **Nhu cầu tra cứu tác phẩm cụ thể, phim bộ, diễn viên và đạo diễn** |
| 3.1 | Thông Tin Phim, Vũ Trụ Phim & Nhân Vật | Phim Hoạt Hình & Vũ Trụ Anime | 1.515.560 | 7.27% | Intent tìm kiếm các thương hiệu Anime/Hoạt hình nổi tiếng (Doraemon, Conan, One Piece). |
| 3.2 | Thông Tin Phim, Vũ Trụ Phim & Nhân Vật | Điện Ảnh Việt Nam Bom Tấn | 558.710 | 2.68% | Intent tra cứu thông tin, lịch chiếu phim điện ảnh Việt Nam bom tấn. |
| 3.3 | Thông Tin Phim, Vũ Trụ Phim & Nhân Vật | Bom Tấn Hollywood & Quốc Tế | 43.150 | 0.21% | Intent tìm kiếm phim bom tấn Hollywood và các thương hiệu điện ảnh lớn. |
| 3.4 | Thông Tin Phim, Vũ Trụ Phim & Nhân Vật | Đạo Diễn, Diễn Viên & Nhân Vật Nổi Tiếng | 2.887.650 | 13.85% | Intent tra cứu tiểu sử, sự nghiệp & danh sách phim của đạo diễn, diễn viên. |
| 3.5 | Thông Tin Phim, Vũ Trụ Phim & Nhân Vật | Chi Tiết Phim & Thứ Tự Xem Phim (Watch Order) | 8.017.900 | 38.45% | Intent tra cứu thông tin chi tiết từng tác phẩm điện ảnh cụ thể. |
| **4** | **LỊCH CHIẾU, VÉ RẠP & TRẢI NGHIỆM PHÒNG CHIẾU** | **Tổng Cụm Suất Chiếu & Đặt Vé Rạp** | **1.119.290** | **5.37%** | **Nhu cầu giao dịch trực tiếp, tra cứu suất chiếu và đặt vé rạp** |
| 4.1 | Lịch Chiếu, Vé Rạp & Trải Nghiệm Phòng Chiếu | Tra Cứu Lịch Chiếu & Suất Chiếu Rạp | 810.530 | 3.89% | Intent tìm khung giờ chiếu, suất chiếu cụ thể tại từng rạp. |
| 4.2 | Lịch Chiếu, Vé Rạp & Trải Nghiệm Phòng Chiếu | Trải Nghiệm Phòng Chiếu Đặc Biệt (IMAX, 3D, 4DX) | 303.410 | 1.46% | Intent tìm phim chiếu định dạng đặc biệt (IMAX, 3D, 4DX). |
| 4.3 | Lịch Chiếu, Vé Rạp & Trải Nghiệm Phòng Chiếu | Bảng Giá Vé Rạp & Ưu Đãi Khuyến Mãi | 3.000 | 0.01% | Intent so sánh bảng giá vé rạp và tìm mã giảm giá vé phim. |
| 4.4 | Lịch Chiếu, Vé Rạp & Trải Nghiệm Phòng Chiếu | Đặt Vé Xem Phim Trực Tuyến | 2.350 | 0.01% | Intent mua vé xem phim trực tuyến và chọn giữ ghế nhanh trên web. |
| **5** | **REVIEW PHIM & PHÂN TÍCH NỘI DUNG** | **Tổng Cụm Review & Đánh Giá Phim** | **159.040** | **0.76%** | **Nhu cầu tham khảo nhận xét, điểm số và bài viết phân tích phim** |
| 5.1 | Review Phim & Phân Tích Nội Dung | Review Phim & Nhận Xét Chi Tiết | 158.810 | 0.76% | Intent đọc nhận xét, bài đánh giá phim trước khi mua vé ra rạp. |
| 5.2 | Review Phim & Phân Tích Nội Dung | Giải Thích Kết Phim, Spoilers & Chấm Điểm IMDb | 230 | 0.00% | Intent tìm bài phân tích kết phim, giải thích tình tiết và điểm số IMDb. |
| **6** | **PHIM BỘ TRỰC TUYẾN & GÓI CƯỚC OTT** | **Tổng Cụm Phim Bộ & Gói OTT** | **1.261.740** | **6.05%** | **Nhu cầu xem phim bộ, TV Series trực tuyến tại nhà trên nền tảng OTT** |
| 6.1 | Phim Bộ Trực Tuyến & Gói Cước OTT | Phim Nổi Bật Trên Netflix & OTT | 16.210 | 0.08% | Intent tìm kiếm các bộ phim phát sóng trên nền tảng Netflix. |
| 6.2 | Phim Bộ Trực Tuyến & Gói Cước OTT | Gói Cước Xem Phim VieON, FPT Play, Galaxy Play | 270 | 0.00% | Intent mua gói cước & xem phim trên nền tảng đối tác Việt Nam. |
| 6.3 | Phim Bộ Trực Tuyến & Gói Cước OTT | Phim Bộ & TV Series Trực Tuyến | 1.245.260 | 5.97% | Intent tìm phim bộ, Kdrama, Anime xem trực tuyến tại nhà. |
| **7** | **TIN TỨC PHIM SẮP CHIẾU & TRAILER** | **Tổng Cụm Phim Sắp Chiếu & Trailer** | **7.430** | **0.04%** | **Nhu cầu đón đầu thông tin phim bom tấn chuẩn bị công chiếu** |
| 7.1 | Tin Tức Phim Sắp Chiếu & Trailer | Lịch Khởi Chiếu Phim Sắp Ra Mắt | 3.100 | 0.01% | Intent theo dõi lịch công chiếu các phim bom tấn chuẩn bị ra rạp. |
| 7.2 | Tin Tức Phim Sắp Chiếu & Trailer | Trailer Official & Tin Tức Hậu Trường | 4.330 | 0.02% | Intent xem trailer chính thức và video xem trước của phim. |



### 2.4 Competitive Landscape, Gap Analysis & MoMo Strategic Advantage

#### 2.4.1 Ma Trận Phân Loại Đối Thủ Thị Trường (Market Competitor Mapping)

Thị trường thông tin và đặt vé xem phim điện ảnh trực tuyến tại Việt Nam hiện được chia thành 3 nhóm đối thủ chính:

1. **Nhóm Website Chuỗi Rạp Đơn Lẻ (CGV.vn, Lottecinema.com.vn, Galaxycine.vn, Betacinemas.vn):**
   * **Thế mạnh:** Dữ liệu suất chiếu gốc trực tiếp, chương trình thành viên rạp (Loyalty) và thương hiệu mạnh.
   * **Hạn chế:** Giới hạn rạp độc quyền (không thể so sánh suất chiếu giữa các chuỗi rạp), trải nghiệm Web SEO hạn chế ngoài từ khóa tên phim gốc, thiếu sự linh hoạt trong các giải pháp thanh toán tài chính.
2. **Nhóm Trang Trang Aggregator & Tổng Hợp Điện Ảnh (Moveek.com, Rapchieuphim.com):**
   * **Thế mạnh:** Lượng truy cập tự nhiên (Organic Traffic) lớn từ từ khóa long-tail, kho nội dung bài viết tin tức và review phong phú.
   * **Hạn chế:** Luồng thanh toán đứt gãy (phải chuyển hướng hoặc phụ thuộc công cụ bên thứ ba), hạ tầng công nghệ cũ kỹ, không có hệ sinh thái thanh toán bù trừ tài chính.
3. **Nhóm Nền Tảng Siêu Ứng Dụng (ZaloPay, Shopee, Traveloka, VinID):**
   * **Thế mạnh:** Tệp người dùng ứng dụng có sẵn, khả năng bán chéo dịch vụ In-App.
   * **Hạn chế:** Không có năng lực hiển thị và chiếm lĩnh thứ hạng trên Open Web (phụ thuộc 95%+ vào quảng cáo In-App và Banner), trải nghiệm trang Web Landing Page mờ nhạt.

#### 2.4.2 Bảng Phân Tích Khoảng Trống Thị Trường (Gap Analysis Matrix)



| Tiêu Chí Phân Tích | Chuỗi Rạp Đơn Lẻ (CGV, Galaxy, Lotte) | Trang Aggregator Truyền Thống (Moveek, Rapchieuphim) | Ứng Dụng Khác (ZaloPay, Shopee) | **MoMo Cinema Hub (momo.vn/cinema)** | **Khoảng Trống Thị Trường & Lợi Thế MoMo** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Khả Năng Phủ 13 Chuỗi Rạp Trên 1 Giao Diện** | Không (Chỉ hiển thị rạp thuộc chuỗi) | Có (Hiển thị nhiều rạp nhưng đứt gãy thanh toán) | Yếu (Không có Web Hub Open Web) | **Có (Tra cứu & mua vé 13 chuỗi rạp trên 1 giao diện duy nhất)** | **MoMo là Hub duy nhất cho phép so sánh suất chiếu & giá vé 13 chuỗi rạp trên 1 bản đồ.** |
| **2. Luồng Thanh Toán Native Web Payment** | Nhập thẻ ngân hàng / quét QR lâu | Chuyển hướng bên thứ ba, đứt gãy luồng | Chỉ thanh toán In-App | **Thanh toán Web Native 1-Click (Ví MoMo, Ví Trả Sau, Thẻ Ngân Hàng)** | **Triệt tiêu đứt gãy checkout, tỷ lệ chuyển đổi đơn hàng cao hơn 30%-40% đối thủ Web.** |
| **3. Giải Pháp Tài Chính & Hỗ Trợ Dòng Tiền** | Không có Ví Trả Sau | Không có | Hạn chế | **Ví Trả Sau (BNPL 0% lãi suất), Hoàn tiền MoMo Rewards** | **Độc quyền Ví Trả Sau MoMo thúc đẩy mua sắm vé xem phim & combo bắp nước giá trị cao.** |
| **4. Open Web SEO & Phủ Từ Khóa Long-Tail** | Yếu (Chỉ xếp hạng từ khóa tên nhà) | Mạnh (Hạ tầng cũ, tốc độ load chậm) | Rất yếu (Gần như không có dữ liệu Web) | **Rất mạnh (Hạ tầng MoSpark, pSEO 120+ chi nhánh rạp, 12.067 KWs - 20,85M volume)** | **Chiếm lĩnh vị trí Top 1-3 Google Search cho tệp từ khóa Rạp Local, Review & Lịch chiếu.** |
| **5. Vòng Đời Dịch Vụ Điện Ảnh Khép Kín (End-to-End)** | Chỉ dừng ở vé chiếu rạp | Chỉ dừng ở bài viết tin tức | Chỉ dừng ở giao dịch mua vé | **Rạp Chiếu + OTT (VieON/Netflix) + Combo Bắp Nước + Voucher Ăn Uống** | **Tự động chuyển đổi người dùng từ Phim Rạp sang Phim OTT khi hết đợt chiếu.** |



#### 2.4.3 Các Nhóm Năng Lực Cần Xác Nhận & Định Hướng Khai Thác (Capability Alignment)

1. **Năng Lực Thanh Toán Native Web Payment:** Đánh giá khả năng tích hợp luồng thanh toán trực tiếp trên Web (Ví MoMo, Ví Trả Sau, Thẻ Ngân Hàng) để tối ưu tỷ lệ chuyển đổi đơn hàng mà không bắt buộc người dùng chuyển tiếp ứng dụng.
2. **Năng Lực Kết Nối API 13 Chuỗi Rạp & Nền Tảng OTT:** Đánh giá mức độ sẵn sàng và độ trễ của hệ thống API kết nối giữ ghế realtime với 13 chuỗi rạp đối tác và dịch vụ bán gói cước OTT.
3. **Hạ Tầng Công Nghệ Web Platform:** Đánh giá năng lực hạ tầng Web trong việc đáp ứng tốc độ tải trang, tối ưu hóa các chỉ số kỹ thuật Core Web Vitals và khả năng mở rộng trang địa điểm rạp (pSEO).
4. **Hệ Sinh Thái Phương Thức Thanh Toán:** Khai thác các phương thức thanh toán linh hoạt hiện có như Ví Trả Sau và chương trình ưu đãi MoMo Rewards để hỗ trợ kích cầu giao dịch.

## III. System Design & Product Solution

### 3.1 Multi-sided Value Proposition
* **Cho Người Xem Phim (Consumers):** Tìm kiếm suất chiếu của tất cả các rạp xung quanh trên 1 bản đồ duy nhất, đặt vé không cần tải app, nhận ưu đãi độc quyền combo bỏng nước.
* **Cho 13 Chuỗi Rạp Đối Tác (Cinema Merchants):** Tiếp cận tệp khách hàng mua vé dồi dào từ Open Web (Open Web Traffic Acquisition), tối ưu tỷ lệ lấp đầy ghế trống các suất chiếu.
* **Cho MoMo Platform:** Biến Web thành kênh thu hút người dùng mới (Acquisition Engine), tăng trưởng lượng giao dịch (Transactions) và tối ưu hóa LTV người dùng.

### 3.2 Web Onboarding & Booking Flow

```mermaid
graph LR
    A["1. Tìm Phim (Google Search)"] --> B["2. Định Vị Rạp & Suất Chiếu"]
    B --> C["3. Chọn Suất Chiếu (Showtime)"]
    C --> D["4. Chọn Ghế (Seats) + Inline F&B Popup"]
    D --> E["5. Xem Đơn Hàng & Checkout"]
    E --> F["6. Thanh Toán Web / App MoMo"]
    F --> G["7. Nhận Vé QR Check-in"]
```

#### Bảng Phân Tích Chi Tiết Các Bước (Step Breakdown Table)



| Bước | Tên Giai Đoạn | Trải Nghiệm Người Dùng (UX) | Hạ Tầng / Cơ Chế Kỹ Thuật | Nền Tảng |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Khởi Tạo Nhu Cầu (Search Trigger)** | Người dùng tìm kiếm từ khóa lịch chiếu, tên phim hoặc cụm rạp trên Google Search. | Google Indexing & SEO Metadata Schema.org (ScreeningEvent, Movie). | Open Web (Google SERP) |
| **2** | **Truy Cập & Định Vị GEO (Onboarding)** | Chuyển hướng về momo.vn/cinema, tự động xác định vị trí GPS để gợi ý suất chiếu rạp gần nhất. | GeoIP Lookup API & Browser HTML5 Geolocation API. | MoSpark Web Platform |
| **3** | **Chọn Suất Chiếu (Showtime Selection)** | Chọn ngày xem, cụm rạp phù hợp và khung giờ suất chiếu mong muốn (ví dụ: 14:00). | Showtime Inventory API sync realtime với 13 chuỗi rạp đối tác. | MoSpark Web & Partner APIs |
| **4** | **Chọn Ghế & Modal Bắp Nước (Seat & F&B Modal)** | Chọn ghế trên sơ đồ phòng chiếu ➔ Nhấp "Tiếp tục" ➔ Bật Popup Modal / Bottom Sheet chọn combo bắp nước ➔ Sang Checkout. | Realtime Seat Map Lock API + Dynamic Modal Component (Client State). | MoSpark Web Platform |
| **5** | **Xem Đơn Hàng & Checkout (Review & Info)** | Xem lại chi tiết đơn hàng (vé + bắp nước chọn từ modal + voucher), nhập Email/SĐT nhận vé điện tử. | Order Calculation Engine & Guest Profile Session. | MoSpark Web Platform |
| **6** | **Thanh Toán & Fallback (Native Payment)** | Thanh toán qua Ví MoMo hoặc All-in-One QR Code. Nếu sự cố API rạp sau khi nhận tiền, kích hoạt Fallback Queue retry hoặc Instant Refund 100% trong 5 phút. | Gateway Payment API, All-in-One QR Engine, Instant Refund Fallback Service. | MoMo Payment Gateway |
| **7** | **Hiển Thị Vé & Gửi Vé (Fulfillment)** | Web Platform hiển thị mã QR vé điện tử trực tiếp trên màn hình web. Luồng gửi vé đa kênh (Zalo ZNS, Email, SMS) do BU Movies vận hành. | Web QR Display Engine, Payment Webhook Trigger ➔ BU Movies Fulfillment System. | Web Platform (UI) & BU Movies (Delivery) |



### 3.3 Kick-off Alignment Rules & Web Compliance
1. **Chuyển đổi trạng thái phim tự động (Lifecycle Automation):** Phim khi hết suất chiếu rạp phải tự động chuyển trạng thái sang *"Đang chiếu Online"* và gợi ý link xem trên OTT đối tác, tuyệt đối không để trang trống hoặc báo lỗi 404.
2. **Đồng bộ sơ đồ ghế Realtime (Realtime Seat Map Sync):** Đảm bảo giữ ghế chính xác với API của 13 chuỗi rạp đối tác, không xảy ra tình trạng trùng ghế khi thanh toán qua Web.
3. **Web Payment Security Compliance:** Tuân thủ chuẩn bảo mật thanh toán PCI-DSS đối với luồng Native Web Payment, xác thực OTP SMS/Biometric khi thanh toán qua Ví MoMo/Thẻ ngân hàng.

### 3.4 Core Use Cases & KPIs Matrix

Bảng chuẩn hóa các Nhóm Trải Nghiệm Sản Phẩm Cốt Lõi (Product Use Cases) và Chỉ Số Cam Kết Kinh Doanh:



| # | Nhóm Trải Nghiệm Cốt Lõi (Core Product Use Case) | Luồng Trải Nghiệm & Tính Năng Sản Phẩm | Mục Tiêu Nhu Cầu Gốc | Chỉ Số Cam Kết (KPIs H2/2026) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Phễu Tra Cứu Lịch Chiếu & Đặt Vé Rạp** | Tra cứu suất chiếu realtime 13 chuỗi rạp, sơ đồ giữ ghế, mua combo bắp nước & thanh toán Native Web Checkout. | Tra cứu suất chiếu & mua vé rạp gần bạn nhất. | **>214.292 Vé bán ra**; Tỷ lệ chuyển đổi **CR ≥ 4.50%**; **GMV Web-to-App >15.0 tỷ đ/H2**. |
| **2** | **Phễu Khám Phá Phim & Trang Chi Tiết Phim** | Trang thông tin phim chiếu rạp, trailer HD, thông tin đạo diễn/diễn viên & gợi ý rạp chiếu theo GPS. | Tìm hiểu nội dung phim, suất chiếu & lịch công chiếu. | **>2.0M Organic Traffic/H2**; Top 1-3 SERP phim hot; **CTR vào Booking >35%**. |
| **3** | **Phễu Khám Phá Rạp Chi Tiết & Local GEO** | Trang thông tin 13 chuỗi rạp đối tác (CGV, Galaxy, Lotte...) và pSEO 120+ chi nhánh rạp local kèm chỉ đường Google Maps. | Tìm vị trí rạp gần nhà, bảng giá vé & ưu đãi rạp. | **Bao phủ tệp từ khóa Rạp Local (4.63M volume)**; phủ 120+ chi nhánh rạp. |
| **4** | **Phễu Đọc Review & Đánh Giá Phim** | Bài viết nhận xét chi tiết, tổng hợp điểm IMDb/Rotten Tomatoes, giải thích kết phim & nhận xét từ cộng đồng MoMo. | Đánh giá chất lượng phim trước & sau khi ra rạp. | **>50k lượt đánh giá mới**; hiển thị trích dẫn Google AI Overview (AIO). |
| **5** | **Phễu Thanh Toán Gói Cước Xem Phim OTT** | Trang chi tiết TV Series/Phim bộ trực tuyến (Kdrama, Anime, Netflix), mua gói cước & Voucher OTT trực tiếp qua Ví MoMo. | Tìm phim xem tại nhà & thanh toán gói cước OTT. | **Tăng trưởng doanh thu gói cước OTT** trực tiếp trên MoMo. |
| **6** | **Phễu Săn Deal & Khuyến Mãi Vé Phim** | Chuyên mục tổng hợp mã giảm giá rạp, chương trình hoàn tiền Ví MoMo, ưu đãi Ví Trả Sau & vé giá rẻ Học sinh - Sinh viên. | Săn mã ưu đãi & vé xem phim tiết kiệm. | **Tỷ lệ đính kèm Combo Bắp nước >20%**; thu hút tệp khách hàng trẻ. |



### 3.5 Định Hướng Trợ Lý AI Phòng Vé: Mô Hình Chuyển Hóa Ý Định Người Dùng (MoMo Cinema AI Concierge)

Nhằm khắc phục triệt để điểm nghẽn tại Tầng 2 sang Tầng 3 của phễu chuyển đổi (người dùng đọc bài đánh giá, tra cứu thông tin nhưng thoát trang do lười tìm rạp hoặc chưa chọn được phim phù hợp), Cinema Hub đưa vào hoạt động **Trợ Lý AI Phòng Vé (MoMo Cinema AI Concierge)** trực tiếp trên nền tảng Web với định hướng chuyển hóa trọn vẹn ý định của khách hàng thành hành động mua vé.

#### 3.5.1 Ý Định Sản Phẩm & Định Vị Trải Nghiệm (Product Intent & Mission)
* **Từ Tra Cứu Thụ Động Sang Dẫn Dắt Tương Tác:** Thay vì để khách hàng phải tự bơi giữa hàng chục danh sách phim và cụm rạp, Trợ lý AI đóng vai trò như một **Tiếp Tân Phòng Vé Thông Minh** 24/7, chủ động lắng nghe, thấu cảm và đưa ra gợi ý chuẩn xác theo từng ngữ cảnh cá nhân.
* **Rút Ngắn Khoảng Cách Đến Quyết Định Mua Vé:** Thấu hiểu những băn khoăn thường gặp của khán giả để đưa ra câu trả lời trực diện, loại bỏ sự do dự và dẫn dắt người dùng đến bước đặt vé trên App MoMo chỉ sau một chạm.

#### 3.5.2 4 Nhóm Ý Định Người Dùng Trọng Tâm (4 Core User Intents)

```mermaid
graph TD
    User["Khách Hàng Truy Cập Web Cinema"] --> Intake["Tiếp Nhận Ý Định Khách Hàng"]
    
    Intake --> I1["1. Ý Định Khám Phá & Gợi Ý<br/>('Chưa biết xem gì, cần tư vấn theo gu')"]
    Intake --> I2["2. Ý Định Khớp Lịch & Địa Điểm<br/>('Tìm suất chiếu gần nhất, giờ đẹp tối nay')"]
    Intake --> I3["3. Ý Định Tối Ưu Chi Phí<br/>('Tìm ưu đãi, mã giảm giá vé & combo bắp nước')"]
    Intake --> I4["4. Ý Định Xác Thực Thông Tin<br/>('Hỏi nhanh độ tuổi, after-credit, review')"]
    
    I1 --> Sol1["Gợi ý 1-2 phim xuất sắc nhất kèm lý do phù hợp"]
    I2 --> Sol2["Tổng hợp suất chiếu đẹp tại rạp gần nhất"]
    I3 --> Sol3["Cung cấp quyền lợi hoàn tiền & mã giảm giá MoMo"]
    I4 --> Sol4["Giải đáp súc tích, gỡ bỏ hoàn toàn phân vân"]
    
    Sol1 & Sol2 & Sol3 & Sol4 --> Bridge["Cung Cấp Thẻ Lựa Chọn Trực Quan 1-Chạm"]
    Bridge --> Action["Chuyển Tiếp Thẳng Vào Luồng Chọn Ghế Trên App MoMo"]
```

* **1. Ý Định Khám Phá & Gợi Ý Phim (Discovery & Recommendation Intent - "Chưa biết xem gì"):**
  * *Tâm lý & Rào cản:* Khách hàng có nhu cầu giải trí cuối tuần hoặc xả stress nhưng bị choáng ngợp trước quá nhiều tựa phim đang chiếu; chưa rõ phim nào thực sự đáng tiền, phim nào hợp sở thích.
  * *Ý định đáp ứng của Trợ lý:* Lắng nghe tâm trạng, thể loại ưa thích hoặc đối tượng đi cùng (hẹn hò lãng mạn, gia đình có con nhỏ, nhóm bạn đi chơi) để đề xuất 1-2 phương án tối ưu nhất kèm tóm tắt sức hút của phim, giúp người dùng ra quyết định nhanh chóng mà không cần đọc quá nhiều bài viết dài.
* **2. Ý Định Khớp Lịch Chiếu & Rạp Tiện Lợi (Convenience & Logistics Intent - "Xem ở đâu, khi nào thuận tiện nhất"):**
  * *Tâm lý & Rào cản:* Khách hàng đã chọn được phim nhưng ngần ngại việc phải mở từng trang web của 13 chuỗi rạp để dò tìm khung giờ và địa điểm phù hợp.
  * *Ý định đáp ứng của Trợ lý:* Tiếp nhận nhu cầu về thời gian (sau giờ làm, tối muộn) và khu vực sinh sống, tự động tổng hợp những suất chiếu đẹp nhất tại các cụm rạp gần nhất để khách hàng lựa chọn ngay trong tích tắc.
* **3. Ý Định Tối Ưu Chi Phí & Săn Ưu Đãi (Value & Promotion Intent - "Làm sao mua vé tiết kiệm nhất"):**
  * *Tâm lý & Rào cản:* Khán giả trẻ, học sinh sinh viên luôn tìm kiếm các mã giảm giá, chương trình hoàn tiền hoặc combo bắp nước giá tốt trước khi quyết định chi tiền.
  * *Ý định đáp ứng của Trợ lý:* Chủ động giới thiệu các đặc quyền thanh toán trên MoMo (ưu đãi khi thanh toán qua Ví Trả Sau, quyền lợi tích điểm, quà tặng độc quyền theo từng bom tấn), khơi gợi sự hào hứng và cung cấp nút nhận ưu đãi dẫn thẳng vào ứng dụng.
* **4. Ý Định Xác Thực Thông Tin Nhanh (Validation & Assurance Intent - "Hỏi nhanh để an tâm chốt"):**
  * *Tâm lý & Rào cản:* Cần kiểm chứng gấp các chi tiết quan trọng trước khi mua: Phim có phù hợp với trẻ em không? Phim có đoạn phim bổ sung sau phần kết (after-credit) không? Rạp có phòng chiếu đặc biệt hay ghế đôi không?
  * *Ý định đáp ứng của Trợ lý:* Giải đáp ngắn gọn, trọng tâm từng băn khoăn cụ thể để người dùng hoàn toàn tự tin chuyển sang bước đặt vé.

#### 3.5.3 Hành Trình Chuyển Hóa Ý Định Thành Hành Động (Intent-to-Action Experience)
* **Bước 1: Tiếp Nhận Ý Định Tự Nhiên:** Khách hàng trò chuyện bằng câu từ tự nhiên hoặc nhấp chọn các câu hỏi gợi ý sẵn có trên giao diện web.
* **Bước 2: Giải Tỏa Băn Khoăn & Đề Xuất Trực Quan:** Trợ lý phản hồi đúng trọng tâm, hiển thị thẻ thông tin súc tích gồm tên phim, rạp chiếu, khung giờ phù hợp và quyền lợi ưu đãi đi kèm.
* **Bước 3: Chuyển Tiếp Liền Mạch Lên Ứng Dụng:** Khách hàng chỉ cần chạm nhẹ vào thẻ đề xuất là được đưa thẳng tới màn hình chọn ghế và thanh toán trên App MoMo mà không phải thao tác tìm kiếm lại từ đầu.

#### 3.5.4 Kết Quả Kinh Doanh & Trải Nghiệm Hướng Tới
* **Gia Tăng Mức Độ Tương Tác:** Biến người đọc bài thụ động thành người dùng chủ động tương tác, nâng tỷ lệ người dùng tham gia tư vấn.
* **Thúc Đẩy Chuyển Đổi Thực Chất:** Chuyển hóa lưu lượng truy cập tìm kiếm tự nhiên trên Web thành đơn đặt vé và doanh thu giao dịch thực tế trên App MoMo.
* **Xây Dựng Thói Quen Nhận Diện:** Định vị Web Cinema MoMo không chỉ là nơi xem giờ chiếu, mà là người bạn đồng hành tin cậy mỗi khi có ý định ra rạp thưởng thức điện ảnh.

### 3.6 Out of Scope
* Không tự vận hành cụm rạp chiếu phim vật lý.
* Không tự sản xuất phim điện ảnh thương mại.
* Không ôm kho vé cứng (chỉ kết nối API giữ vé realtime với các hệ thống Rạp đối tác).

## IV. Target Personas & JTBD

### 4.1 Target Personas
* **Persona 1: Gen Z / Bạn trẻ nghiện phim (Movie Buffs):** Thường xuyên tìm kiếm phim hot, xem review trước khi ra rạp, thích đặt vé nhanh không muốn tải thêm app rườm rà.
* **Persona 2: Cặp đôi & Gia đình đi xem phim cuối tuần:** Nhu cầu tìm rạp gần nhà, tiện đường đi ăn uống, chọn rạp có ghế đôi (Sweetbox) hoặc phòng chiếu trẻ em.
* **Persona 3: Người dùng tìm xem phim Online / Phim bộ:** Tìm kiếm các bộ phim đã rời rạp để xem lại trên các ứng dụng OTT tại nhà.

### 4.2 Consumer Journey (4 Stages)
1. **Trigger:** Thấy bài PR/Trailer phim mới trên Facebook/TikTok hoặc có nhu cầu đi chơi cuối tuần.
2. **Search & Discovery:** Search Google *"lịch chiếu phim [tên phim]"*  ➔  Truy cập `momo.vn/cinema` hiển thị rạp gần nhất theo vị trí GPS.
3. **Booking & Payment:** Chọn rạp  ➔  Chọn suất chiếu & ghế đẹp  ➔  Thanh toán trực tiếp trên Web bằng Native Web Payment (hoặc mở App MoMo).
4. **Experience & Retention:** Nhận vé điện tử có mã QR check-in tại rạp  ➔  Nhận thông báo đánh giá phim sau khi xem  ➔  Gợi ý các phim cùng thể loại sắp ra mắt.

### 4.3 Multi-sided JTBD Matrix



| Đối tượng | Job-To-Be-Done chính (Job Statement) | Pain Points cần giải quyết | Thay đổi sau khi dùng Cinema Hub |
| :--- | :--- | :--- | :--- |
| **Người xem phim (Consumers)** | *"Giúp tôi tìm suất chiếu phim phù hợp nhất tại các rạp gần tôi và đặt vé nhanh chóng mà không cần tải nhiều app từng chuỗi rạp."* | - Phải tải app của từng rạp riêng lẻ (CGV app, Lotte app...).**- Bị đứt gãy luồng mua vé khi dùng Web do bắt tải App.**- Thông tin lịch chiếu rạp không cập nhật đúng realtime. | - Tất cả 13 chuỗi rạp đối tác trên 1 giao diện duy nhất.**- Mua vé & thanh toán mượt mà trên Native Web.**- Lịch chiếu tự động cập nhật chuẩn xác. |
| **Chuỗi Rạp Đối Tác (Cinemas)** | *"Giúp rạp của tôi tiếp cận lượng lớn khách hàng tìm kiếm tự nhiên trên Google để lấp đầy các suất chiếu còn trống."* | - Phụ thuộc vào kênh traffic tự có của app rạp.**- Chi phí quảng cáo tìm khách hàng mới trên Open Web đắt đỏ.**- Tỷ lệ hủy vé cao nếu luồng đặt vé rườm rà. | - Thu hút hàng triệu lượt tìm kiếm tự nhiên từ MoMo Web.**- Đồng bộ ghế và bán vé tự động 24/7.**- Đẩy mạnh bán kèm Combo Bỏng nước tăng ARPU. |
| **Nền tảng (MoMo Platform)** | *"Giúp MoMo biến Web Cinema thành kênh thu hút người dùng mới, khôi phục CR và tối đa hóa số lượng vé bán ra."* | - CR luồng W2A suy giảm xuống 4.37% do rào cản ứng dụng.**- Chưa phủ trọn tệp từ khóa ngành ~20,85M search volume/tháng.**- Phim hết rạp không mang lại giá trị gia tăng. | - Tăng trưởng Traffic H2 đạt >8.07M.**- Khôi phục CR ≥ 4.50% nhờ Native Web Payment.**- Tận dụng traffic phim hết rạp để monetization qua OTT. |



## V. Site Structure & SEO/GEO

### 5.1 Site Structure Blueprint

#### 5.1.1 Cấu Trúc Website Hiện Tại (Current Site Structure)
Bảng tổng hợp các trang và tuyến đường dẫn sản phẩm đang vận hành hiện tại trên `momo.vn/cinema`:



| Tên Trang (Page Name) | Cấu Trúc Đường Dẫn (Current URL Structure) | Chức Năng Cốt Lõi |
| :--- | :--- | :--- |
| **Trang Chủ Cinema Hub** | /cinema | Trang chủ tổng hợp: Định vị rạp gần nhất, banner phim hot, widget tìm kiếm & giá vé rạp. |
| **Lịch Chiếu Phim** | /cinema/lich-chieu-phim | Tra cứu lịch chiếu và suất chiếu rạp theo vị trí địa lý hoặc Tỉnh/Thành. |
| **Phim Chiếu Rạp** | /cinema/phim-chieu | Danh mục tổng hợp phim đang chiếu tại rạp. |
| **Phim Sắp Chiếu Rạp** | /cinema/phim-sap-chieu | Danh mục tổng hợp phim chuẩn bị công chiếu & nhận thông báo mở bán vé (Notify Me). |
| **Chi Tiết Phim** | /cinema/{movie-slug}-{movie-id} | Trang thông tin chi tiết bộ phim tích hợp Widget Tra Cứu Suất Chiếu & Chọn Ghế Realtime. |
| **Săn Deal & Khuyến Mãi Vé Phim** | /cinema/khuyen-mai | Hub tổng hợp mã giảm giá rạp, ưu đãi bắp nước & vé giá rẻ Học sinh - Sinh viên. |
| **Danh Sách Chuỗi Rạp (Tầng 1)** | /cinema/rap | Trang tổng hợp 13 thương hiệu chuỗi rạp đối tác (CGV, Lotte, Galaxy, BHD...). |
| **Chuỗi Rạp Chi Tiết (Tầng 2)** | /cinema/rap/{ten-rap} | Trang thông tin từng thương hiệu chuỗi rạp (Ví dụ: /cinema/rap/cgv, /cinema/rap/galaxy-cinema). |
| **Rạp Chi Tiết (Tầng 3)** | /cinema/rap/{ten-rap}/{ten-chi-nhanh} | Trang địa điểm rạp cụ thể (Ví dụ: /cinema/rap/cgv/cgv-crescent-mall - bản đồ, bảng giá, suất chiếu). |
| **Top Phim & Danh Sách Chọn Lọc** | /cinema/top-phim | Danh mục bài viết tổng hợp, xếp hạng top phim hay theo chủ đề và mùa giải. |
| **Danh Mục Review Phim (Master Hub)** | /cinema/review | Chuyên mục tổng hợp tất cả các bài viết nhận xét và đánh giá phim. |
| **Bài Review Phim Chi Tiết** | /cinema/{film-detail-ID}/review | Trang bài viết phân tích, đánh giá chuyên sâu cho một bộ phim cụ thể (Ví dụ: /cinema/ho-linh-trang-si-10452/review). Tích hợp điểm MoMo Rating & Widget Đặt Vé 1-Click. |
| **Blog Điện Ảnh** | /cinema/blog | Tin tức, sự kiện và bài viết blog cập nhật xu hướng điện ảnh. |
| **Vũ Trụ Phim & Phim Bộ (Blog)** | /cinema/blog/phim-bo-vu-tru-phim | Master Topic tổng hợp bài viết thứ tự xem phim (Watch Order), Anime IPs & TV Series. |
| **Doanh Thu Phòng Vé (Box Office)** | /cinema/doanh-thu-phong-ve***(Alias: /doanh-thu-phong-ve)* | Bảng xếp hạng doanh thu phim chiếu rạp theo thời gian thực (Box Office Vietnam Live Feed), CLB Phim Trăm Tỷ & nút Mua Vé Trực Tiếp. |
| **Thanh Toán Vé - Chọn Suất Chiếu** | /cinema/dat-ve/suat-chieu/{movie-slug} | Giao diện chọn cụm rạp, ngày chiếu và khung giờ suất chiếu realtime. |
| **Thanh Toán Vé - Chọn Ghế & Modal F&B** | /cinema/dat-ve/chon-ghe/{booking-id} | Sơ đồ giữ ghế realtime tích hợp Modal Popup / Bottom Sheet chọn bắp nước ưu đãi inline. |
| **Thanh Toán Vé - Checkout** | /cinema/dat-ve/checkout/{booking-id} | Trang nhập thông tin khách hàng, xem lại tổng đơn hàng (vé + combo bắp nước) và chọn phương thức thanh toán. |
| **Thanh Toán Vé - Xác Thực** | /cinema/dat-ve/thanh-toan/{booking-id} | Trang xác thực thanh toán Native Web / QR Code Payment. |
| **Thanh Toán Vé - Vé Điện Tử** | /cinema/dat-ve/ve-dien-tu/{booking-id} | Trang hiển thị mã QR vé điện tử check-in rạp và thông tin suất chiếu. |



#### 5.1.2 Đề Xuất Mở Rộng Cấu Trúc Website H2/2026 (Suggested Site Structure Extensions - Lean & Anti-Spam Control)

Để tránh lạm dụng pSEO sinh ra hàng ngàn URL tĩnh mỏng (Thin Pages), Cinema Hub áp dụng chiến lược mở rộng **Tinh gọn & Có Quality Gate kiểm soát chỉ mục**:



| Tên Trang Đề Xuất (Suggested Page) | Cấu Trúc Đường Dẫn Mới (Proposed URL) | Tiêu Chẩn Quality Gate & Cơ Chế Index Control |
| :--- | :--- | :--- |
| **Phim Chiếu Rạp Theo Thể Loại Big 3** | /cinema/phim-chieu/{the-loai} | Chỉ mở URL tĩnh indexable cho Top 3 thể loại siêu lớn (Anime, Kinh Dị, Việt Nam). Các thể loại còn lại dùng Client-side Filter Parameter (?genre=...) và Canonical về Master Hub. |
| **Master Hub TV Series & OTT** | /cinema/tv-series | Gom 100% phim hết chiếu rạp và phim bộ OTT vào 1 Master Hub duy nhất. Tuyệt đối không tự động sinh hàng ngàn trang phim bộ rác. |
| **Bách Khoa Diễn Viên / Đạo Diễn (Production URL)** | /cinema/person/{tên-diễn-viên} | Trang Profile Diễn viên chuẩn Production (hiện vận hành chính thức 55 trang hồ sơ chất lượng cao). Chỉ cho phép Index khi trang qua Quality Gate: ≥3 bộ phim tham gia + Có điểm MoMo Rating + Có Widget phim đang chiếu. Hồ sơ mỏng tự động cắm thẻ noindex, follow. |
| **Bảng Xếp Hạng Doanh Thu Phòng Vé** | /cinema/doanh-thu-phong-ve***(Short link: /doanh-thu-phong-ve)* | Data-driven Hub kết nối Box Office Vietnam (cập nhật Ngày/Tuần/Tích lũy). Đính kèm Schema Dataset & ItemList phục vụ trích dẫn số liệu tự động cho Google AI Overview và báo chí, đính kèm nút Mua vé 1-click. |



#### 5.1.3 Đề Xuất Tối Ưu Cấu Trúc Website & Giải Pháp Chống Duplicate / Thin Content

Dựa trên phản biện chuyên sâu về Kỹ thuật SEO (Technical SEO), việc lạm dụng pSEO tạo hàng loạt URL con tĩnh (Location Pages / Format Pages) sẽ dẫn tới rủi ro nghiêm trọng về **Duplicate Content, Thin Content và Lãng phí Crawl Budget**. 

Do đó, Cinema Hub áp dụng **3 Cơ Chế Kiểm Soát Kỹ Thuật Nghiêm Ngặt** để vừa thu hút lưu lượng vừa bảo vệ chất lượng chỉ mục Google:

#### 1. Luồng Lịch Chiếu Local GEO: Dynamic Client-Side Filter & Canonical Consolidation
* **Vấn đề:** Các trang `/cinema/lich-chieu-phim/tphcm/quan-1` hay `/cinema/lich-chieu-phim/lam-dong/da-lat` nếu tạo URL tĩnh riêng lẻ sẽ bị trùng lặp 90% nội dung danh sách phim với trang lịch chiếu chung.
* **Giải pháp Kỹ thuật:**
  * **Master Page:** Giữ nguyên trang chủ Lịch chiếu `/cinema/lich-chieu-phim` làm URL gốc duy nhất được Google Index.
  * **Dynamic URL Parameters:** Nhu cầu lọc rạp theo Tỉnh/Thành/Quận/Huyện vận hành bằng URL Parameter (`/cinema/lich-chieu-phim?city=ha-noi&district=quan-1`) hoặc Client-side State.
  * **Canonical Tag Consolidation:** Toàn bộ các URL parameter lọc địa phương đều khai báo `rel="canonical"` trỏ ngược về Master Page `/cinema/lich-chieu-phim` (hoặc đặt `<meta name="robots" content="noindex, follow">` cho các bộ lọc cấp Quận/Huyện) ➔ Triệt tiêu 100% nguy cơ Duplicate Content và bảo toàn Crawl Budget.
  * **Ngoại lệ Index (Top 5 Tỉnh/Thành lớn):** Chỉ khởi tạo URL tĩnh indexable cho Top 5 Tỉnh/Thành có volume tìm kiếm khổng lồ (Hà Nội, TP.HCM, Đà Nẵng, Hải Phòng, Cần Thơ) KHI VÀ CHỈ KHI trang đó được bổ sung nội dung độc bản (Unique Content) như: Hướng dẫn cụm rạp hot nhất khu vực, Bảng giá vé trung bình địa phương & Voucher bắp nước độc quyền.

#### 2. Vũ Trụ Phim & Franchise IPs: Gom Nhóm 100% Vào 1 Chuyên Mục Blog Master Duy Nhất (`/cinema/blog/phim-bo-vu-tru-phim`)
* **Vấn đề:** Việc xé lẻ tạo thêm hàng chục Category chi tiết cho từng Franchise (`/cinema/blog/doraemon`, `/cinema/blog/conan`, `/cinema/blog/marvel`...) sẽ gây phình to cấu trúc Blog Taxonomy, lãng phí PageRank và dễ phát sinh các Category mỏng (Thin Categories).
* **Giải pháp Kỹ thuật Chuẩn hóa Cốt lõi:**
  * **1 Master Topic Category duy nhất:** Toàn bộ nội dung về Vũ trụ điện ảnh, Series hoạt hình & Franchise IPs được **gom gọn 100% vào 1 Chuyên Mục Blog Master duy nhất**: `/cinema/blog/phim-bo-vu-tru-phim` (hoặc `/cinema/blog/chuoi-phim`).
  * **Quản lý bằng Article Tags (#Tag):** Các thương hiệu chi tiết (`Doraemon`, `Conan`, `Marvel`, `Anime`...) được phân loại hoàn toàn bằng **Hệ thống Tags trong bài viết** (`#doraemon`, `#conan`, `#marvel`, `#anime`), TUYỆT ĐỐI KHÔNG sinh thêm Category URL tĩnh mới.
  * **Ưu điểm Architecture:**
    1. Giữ Blog Taxonomy tối giản nhất (chỉ gồm 3 Chuyên mục Master: `/cinema/blog/review`, `/cinema/blog/tin-tuc`, `/cinema/blog/phim-bo-vu-tru-phim`).
    2. Tập trung tối đa Authority & PageRank vào 1 Chuyên mục Topic lớn thay vì phân tán sức mạnh SEO.
    3. Triệt tiêu 100% rủi ro Thin Category hay Duplicate Category.

#### 3. Chống Trang Rác & Tự Động Hóa Quản Lý Index (Thin Content Defense Matrix)
* **Dynamic Noindex Rule:** Đối với bất kỳ trang địa điểm hay chuyên mục nào có số lượng suất chiếu rạp active **< 2 phim** hoặc không có thông tin suất chiếu realtime, hệ thống tự động chèn `<meta name="robots" content="noindex, follow">`.
* **Crawl Budget Protection:** Đảm bảo Googlebot chỉ dành năng lực thu thập dữ liệu cho các trang chất lượng cao (`/cinema/{movie-slug}` và `/cinema/rap/{ten-rap}`), loại bỏ hoàn toàn các trang rác / trang trống dữ liệu.

#### Phân Tích Khoảng Trống & Lộ Trình Nâng Cấp (Gap Analysis: As-Is vs To-Be Architecture)

Dựa trên cấu trúc 4 khối hiện trạng (`Tiêu đề`, `Nội dung review`, `Block User Rating Review`, `Block Đặt vé nếu phim còn chiếu`), Web Platform triển khai lộ trình nâng cấp lên Cấu trúc 8 Khu Vực để bứt phá tỷ lệ chuyển đổi:



| Khối Chức Năng | Hiện Trạng (As-Is Current State) | Đề Xuất Nâng Cấp (To-Be Target H2/2026) | Tác Động Sản Phẩm & Metric Tăng Trưởng |
| :--- | :--- | :--- | :--- |
| **Tiêu Đề & Header** | Tiêu đề bài viết thô. | Tiêu đề H1 chuẩn SEO + Metadata + **MoMo Rating Badge (8.8/10 ⭐)**. | Gây ấn tượng thị giác mạnh & khẳng định uy tín nội dung biên tập. |
| **Tóm Tắt 1 Phút** | Chưa có (User phải cuộn đọc hết bài). | Bổ sung **Verdict Box (Pros/Cons/Verdict)** + Nút CTA Đặt Vé 79K Nhanh. | Giữ chân & chốt đơn ngẫu hứng cho 40% người đọc lười. |
| **Block Đặt Vé Phim** | Nằm cố định ở cuối bài viết (đáy trang). | Đẩy lên vị trí **Inline ngay dưới Verdict Box** + **Sticky Bar chân màn hình Mobile**. | Tối ưu vị trí mắt nhìn, nâng W2A CTR từ baseline 1% lên ≥4.5% - 8%. |
| **Phim Hết Chiếu Rạp** | Ẩn Block hoặc để khoảng trống. | Tự động đổi thành **Block Xem Online trên OTT** (VieON, FPT Play, Netflix). | Triệt tiêu lỗi 404 & thương mại hóa danh mục phim hết rạp. |
| **User Rating Review** | Block đánh giá cơ bản. | Hệ thống 10 sao đính kèm Badge **"Đã Mua Vé Trên MoMo"** + Filter spoiler + Upvote. | Tạo nguồn UGC thật & hiển thị điểm sao vàng Schema trên Google SERP. |



### 5.2 Chiến Lược Tối Ưu SEO & GEO (Generative Engine Optimization & Local GEO Targeting)

#### 1. Chiến Lược GEO (Generative Engine Optimization - Phủ Sóng Công Cụ Tìm Kiếm AI)
Chiến lược GEO tối ưu hóa cấu trúc dữ liệu để các công cụ tìm kiếm AI (Google AI Overview, ChatGPT Search, Perplexity) ưu tiên trích dẫn MoMo Cinema Hub làm nguồn dữ liệu trả lời chính xác cho người dùng:
* **Cấu Trúc Dữ Liệu Schema.org Nâng Cao:** Khai báo mã liên kết JSON-LD đa tầng cho các thực thể: `Movie` ➔ `ScreeningEvent` ➔ `MovieTheater` ➔ `Person` (Actor/Director) ➔ `AggregateRating` & `FAQPage`. Giúp các mô hình AI đọc hiểu chính xác suất chiếu và thông tin tác phẩm mà không bị ảo giác thông tin (Hallucination).
* **Trích Xuất Thông Tin Nhanh (Fact Density & Direct Answer Block):** Xây dựng khối thông tin tóm tắt cô đọng (bullet points về nội dung, thời lượng, độ tuổi, điểm IMDb, lịch công chiếu) ngay đầu trang phim, giúp Google AI Overview dễ dàng trích dẫn làm câu trả lời nổi bật (Featured Snippets).
* **Tích Hợp Đánh Giá Người Dùng Thật (Original UGC & Community Reviews):** Khai báo cấu trúc Schema `Review` từ các nhận xét của cộng đồng người dùng MoMo, giúp các công cụ AI ưu tiên hiển thị trích dẫn nguồn đánh giá người dùng thực tế.

#### 2. Chiến Lược Local GEO Search (Tối Ưu Tìm Kiếm Theo Vị Trí Địa Lý / Tỉnh Thành / Quận Huyện)
Chiến lược Local GEO tối ưu hóa cho các từ khóa tìm kiếm rạp theo vị trí địa lý gần người dùng (`rạp chiếu phim gần đây`, `rạp cgv quận 1`, `lịch chiếu phim đà lạt`):
* **Tự Động Nhận Diện Vị Trí GPS (Auto Location Detection):** Kích hoạt GeoIP Lookup API và Browser Geolocation API để ưu tiên hiển thị rạp chiếu và suất chiếu trong bán kính 5km gần nhất ngay khi người dùng truy cập `/cinema/lich-chieu-phim`.
* **Cấu Trúc Trang pSEO Rạp Local (120+ Chi Nhánh Rạp):** Xây dựng các trang chi tiết địa điểm rạp chuẩn hóa (`/cinema/rap/{ten-rap}/{ten-chi-nhanh}`), nhúng bản đồ vị trí Google Maps, địa chỉ chính xác, hướng dẫn gửi xe, bảng giá vé và thông tin suất chiếu realtime.
* **Cơ Chế Canonical Consolidation:** Khai báo thẻ `rel="canonical"` trỏ về Master Page `/cinema/lich-chieu-phim` cho các bộ lọc tham số địa phương động (`?city=ha-noi&district=quan-1`) để bảo tồn Crawl Budget và triệt tiêu Duplicate Content.

#### 3. Tối Ưu Hạ Tầng Kỹ Thuật (Technical SEO trên MoSpark Platform)
* **Kiến Trúc Hybrid Rendering (SSR / SSG):** Render trước thông tin phim tĩnh và hydrate dữ liệu suất chiếu realtime, đảm bảo tốc độ phản hồi máy chủ TTFB < 200ms và chỉ số LCP < 1.2s.
* **Tối Ưu Chỉ Số Core Web Vitals:** Đạt chỉ số xanh 100/100 Mobile PageSpeed, triệt tiêu hoàn toàn độ trễ layout (CLS = 0) khi tải sơ đồ giữ ghế.
* **Cấu Trúc Mạng Lưới Liên Kết Nội Bộ (Hub-and-Spoke Internal Link Building):** Tạo luồng liên kết tự nhiên từ Trang Danh Mục ➔ Trang Chi Tiết Phim ➔ Trang Diễn Viên/Đạo Diễn ➔ Trang Địa Điểm Rạp.

#### 4. Đầu Tư Truyền Thông & Sức Mạnh Liên Kết Off-Page (Media & Authority Building)
* **Chiến Lược Off-Page Investment của BU Movies:** Thực hiện chiến dịch PR báo chí chính thống (VnExpress, Tuổi Trẻ, Thanh Niên, Kenh14) về các sự kiện công chiếu phim bom tấn, đính kèm liên kết uy tín về https://momo.vn/cinema.
* **Xác Thực Thực Thể Thương Hiệu (Entity Verification):** Khai báo thực thể thương hiệu MoMo Cinema trên IMDb, Wikipedia và Google Knowledge Panel.

## VI. Gamification, User Engagement & Retention Tactics

Để khắc phục tình trạng người dùng chỉ xem lịch chiếu rồi thoát trang (Bounce rate cao), Cinema Hub triển khai **6 Chiến thuật Tăng trưởng Tương tác (Product-Led Engagement Tactics)** nhằm tăng Time-on-Site (từ 45s ➔ 3-5 phút), tăng số trang xem (Pages/Session từ 1.2 ➔ 3.5+) và tỷ lệ quay lại web:

### 6.1 6 Tactics Tối Ưu Engagement Kênh Web Cinema Hub

1. **Interactive Quiz "Hôm Nay Xem Gì?" (Personalized Movie Matcher):**
   * *Cơ chế:* Bộ trắc nghiệm 3 câu hỏi siêu nhanh (Cảm xúc hiện tại? Xem với ai? Thể loại yêu thích?).
   * *Output:* Trả kết quả *"Match 99% 1 Phim Chiếu Rạp Tối Nay"* kèm Widget chọn suất chiếu rạp gần nhất 1-Click. Tăng time-on-site +40%.
2. **Dự Đoán Doanh Thu Phòng Vé nhận Voucher (Box Office Predictor & Mini Poll):**
   * *Cơ chế:* Nhúng Widget bình chọn dự đoán trên trang Doanh Thu Phòng Vé (`/doanh-thu-phong-ve`) & Trang Phim: *"Dự đoán phim [Hộ Linh Tráng Sĩ] đạt mốc 100 tỷ trong bao nhiêu ngày?"* hoặc *"Top 1 Doanh thu Cuối tuần này"*.
   * *Phần thưởng:* Dự đoán đúng nhận Voucher Combo Bắp Nước 0đ hoặc Mã giảm 20k vé phim. Giữ chân người dùng quay lại hàng tuần.
3. **MoMo Verified User Rating & Spoiler-Free Community Reviews:**
   * *Cơ chế:* Hệ thống chấm điểm 10 sao đính kèm Badge *"Đã Mua Vé Trên MoMo"*. Bộ lọc review thông minh: *"Nhanh 1 Phút (Nên Xem/Không)"*, *"Phân Tích Chi Tiết (Không Spoiler)"*, *"Thấu Thị Cổ Trại (Có Spoiler)"*.
   * *Tác động:* Tính năng Upvote/Thả tim nhận xét hay giúp kéo dài Session Duration và tăng độ uy tín SEO (UGC Content).
4. **Sơ Đồ Tương Tác Vũ Trụ Phim & Thứ Tự Xem (Interactive Franchise Flowchart):**
   * *Cơ chế:* Ứng dụng cho các Theme Vũ trụ phim & Franchise IPs (Marvel, DC, Anime IPs, Doraemon, Conan). Sơ đồ Flowchart click tương tác từng phần phim + Thanh tiến trình *"Đã xem X/15 phim"*.
   * *Tác động:* Tăng số trang xem (Pages/Session) từ 1.2 lên 4.0+ trang.
5. **Countdown & Early Bird Ticket Alert (Rèm Phim Bom Tấn & Nhắc Vé Sớm):**
   * *Cơ chế:* Đồng hồ đếm ngược (Live Countdown Timer) tại trang Phim Sắp Chiếu (`/cinema/phim-sap-chieu`) + Nút *"Nhận Thông Báo Mở Bán Vé Sớm (Notify Me)"*.
   * *Tác động:* Thu thập Data Seed (Email/SĐT) và tự động kích hoạt thông báo khi rạp mở bán vé.
6. **Vòng Quay May Mắn & Đố Vui Điện Ảnh 0đ (Daily Movie Trivia & Spin Wheel):**
   * *Cơ chế:* Đố vui điện ảnh 1 câu mỗi ngày hoặc Vòng quay vé 0đ cho người dùng hoàn tất đặt vé. Trả thưởng Voucher F&B và mã giảm giá vé phim. Tăng tỷ lệ quay lại web hàng ngày (Daily Retention Rate).

### 6.2 Chiến Lược Phục Vụ Người Dùng "Lười Khám Phá" (Zero-Friction Discovery Framework)

Khi tâm lý người dùng ngày càng thụ động và ngại gõ tìm kiếm/lướt trang (Decision Paralysis & Choice Overload), Cinema Hub chuyển từ mô hình *"Search & Browse"* (Chờ user tự đi tìm) sang mô hình **"Zero-Friction Push" (Tự động đẩy nội dung đút tận miệng)** thông qua 4 trụ cột UX:

1. **Short Video Trailers & Vertical Reels Carousel:** Thay bài viết dài bằng chuỗi Short Trailer / Highlights 15s lướt dọc/ngang trên Hero Banner. Nhúng lớp phủ (Overlay) nút *"Đặt Vé Suất Gần Bạn"* trực tiếp trên clip.
2. **Contextual Micro-Pills (Nút Ngữ Cảnh 1-Chạm):** Đưa sẵn các nút lọc 1-touch dựa trên ngữ cảnh thực tế: `[🔥 Phim Đang Hot Tối Nay]`, `[🍿 Rạp Gần Bạn Còn Ghế Đẹp]`, `[💑 Phim Cặp Đôi Mua Nhiều Nhất]`.
3. **Zero-Click GeoIP Hero Card:** Vừa vào web, hệ thống tự đọc GPS/GeoIP đút sẵn **1 Hero Card duy nhất**: *"Rạp CGV Crescent Mall (cách 1.2km) có 2 suất phim hot tối nay 19:30 & 20:15"*, triệt tiêu 100% bước lọc tỉnh/thành/rạp.
4. **Contextual Trigger Notifications:** Bắn thông báo Zalo ZNS / App Push vào khung giờ vàng (17h thứ 6 / 11h30 thứ 7): *"Tối nay đi xem Hộ Linh Tráng Sĩ? Rạp gần bạn còn 4 ghế đẹp. Đặt vé giảm 20k!"* ➔ 1-Click mở thẳng Sơ đồ chọn ghế.

### 6.3 Chiến Dịch Gamification O2O: Săn Mã Số May Mắn (Search & Check-in Lucky Draw)

Đây là **Ý tưởng Tăng trưởng Đột phá (Growth Hacking Campaign)** giúp tăng vọt Organic CTR trên Google SERP, định danh khách hàng Web và kích hoạt luồng Vòng lặp O2O (Online-to-Offline-to-Online):

```mermaid
graph LR
    A["1. Đăng Nhập Gmail (Google OAuth)"] --> B["2. Google Search 'Tên Phim + MoMo'"]
    B --> C["3. Nhấp Link momo.vn ➔ Nhận Mã Số May Mắn #1"]
    C --> D["4. Xem Phim Rạp ➔ Chụp Ảnh Check-in / Review"]
    D --> E["5. Nhận Mã Số May Mắn #2 ➔ Quay Số Trúng Vé 0đ / Voucher"]
```

#### Phân Tích Cơ Chế & Tác Động Sản Phẩm:
1. **Bước 1 - Single Sign-On (Google OAuth Login):** Người dùng đăng nhập nhanh bằng Gmail trên Web Cinema Hub ➔ Định danh nhanh khách hàng Non-App, thu thập Data Seed (Email) cho chiến dịch Retargeting.
2. **Bước 2 - SEO Traffic Húc Rank Google (Search Trigger):** 
   * Người dùng nhận hướng dẫn tìm kiếm từ khóa dạng `"tên phim + momo"` (Ví dụ: `phim hộ linh tráng sĩ momo`, `review nghỉ hè sợ nghỉ hưu momo`) trên Google Search và nhấp vào kết quả `momo.vn`.
   * *Tác động SEO:* Gửi tín hiệu **High Organic CTR & Branded Search Frequency** cực mạnh lên thuật toán Google RankBrain ➔ Đẩy từ khóa `momo.vn` lên **Top 1 Google SERP** với tốc độ kỷ lục!
   * *Xác minh kỹ thuật:* Hệ thống kiểm tra `document.referrer` chứa `google.com` ➔ Tự động cấp **Mã Số May Mắn Ngẫu Nhiên #1**.
3. **Bước 3 - Vòng Lặp O2O & Review Check-in Rạp (Social Proof Trigger):**
   * Sau khi xem phim tại rạp, người dùng tải ảnh chụp check-in tại rạp / viết review trên trang phim (`/cinema/{film-detail-ID}/review`).
   * *Tác động:* Tạo nguồn dữ liệu **UGC Content Thật 100%** (User-Generated Content có hình ảnh tại CGV/Lotte/Galaxy), giúp nâng cao uy tín thương hiệu Cinema Hub và điểm SEO Schema `Review`.
   * *Xác minh kỹ thuật:* Hệ thống xác minh ảnh check-in / vé rạp ➔ Tự động cấp **Mã Số May Mắn Ngẫu Nhiên #2** (Tỷ lệ trúng thưởng cao gấp 3 lần).
4. **Bước 4 - Quay Số Trúng Thưởng (Lucky Draw / Spin Wheel):**
   * Tổ chức Quay số trực tiếp hàng tuần (Live Stream / Auto-draw) hoặc Vòng quay may mắn trúng ngay: Vé xem phim 0đ, Voucher F&B 100k, Combo Bắp Nước 0đ hoặc Vé xem phim 1 năm miễn phí.

### 6.4 Báo Cáo Kết Quả Thực Tế Đợt Testing Minigame Cào Vé (Testing Performance Audit)

Cập nhật kết quả đo lường dữ liệu thực tế từ hệ thống Tracking Analytics cho đợt Testing Minigame Cào Vé trên Cinema Web:

#### 1. Bảng Tổng Hợp Event Tracking & Phễu Chuyển Đổi Đợt Testing:
* **`cinema_traffic_google_detected` (Traffic Google đầu phễu):** **304 lượt**
* **`cinema_game_click_start` (Kích hoạt cào vé):** **130 lượt** *(CVR từ Traffic: 42.76%)*
* **`cinema_game_scratch_completed` (Cào hoàn tất):** **97 lượt** *(CVR từ Start: **74.61%**)*
* **`cinema_game_click_copy_code` (Sao chép code):** **115 lượt**
* **`cinema_game_click_to_app` (Nhấp Mở App MoMo):** **104 lượt** *(CVR từ Cào Done: 107.2%)*
* **`cinema_game_click_download_app` (Nhấp Tải App):** **4 lượt**
* **User chơi game trong App HỢP LỆ (Valid In-App Users):** **70 users** *(CVR từ Cào Done: **72.16%** | End-to-End CVR: **23.03%**)*

#### 2. Đánh Giá Hiệu Năng & Phương Án Tối Ưu Cho Production:
* **Điểm Sáng:** Tỷ lệ cào hoàn tất trên Web đạt **74.61%** và tỷ lệ user thực sự chơi game hợp lệ trong App đạt **72.16%** (End-to-End CVR đạt **23.03%**, gấp 5 lần trung bình ngành).
* **Khắc Phục Đứt Gãy Đầu Phễu (57.24% Drop-off):** Tự động bật Sticky Floating Banner 1-touch ngay khi detect `cinema_traffic_google_detected = true` để kéo user vào game.
* **Tối Ưu Kỹ Thuật Deep Link Handoff (Bảo Mật OS Compliant):** Thay thế cơ chế dán clipboard (vi phạm chính sách OS iOS/Android) bằng phương án truyền mã đính kèm trong tham số đường dẫn Deep Link `momo://cinema/claim?code=MOMO79K`. Khi App MoMo mở ra, Native App Handler tự động đọc URL Params và **Pre-fill mã Code vào ô nhập** hoàn toàn hợp lệ.

## VII. Compliance & Risk Governance

### 7.1 Compliance & Security Rules
* **Tuân thủ Bảo vệ Dữ liệu Cá nhân (PDPD - NĐ 13/2023/NĐ-CP):** Bảo mật thông tin giao dịch, SĐT và Email của khách hàng mua vé trên Web.
* **Cơ Chế Payment Settlement & Fallback (MoMo & All-in-One QR):** 
  * Xử lý giao dịch thanh toán trực tiếp qua Ví MoMo hoặc All-in-One QR Code.
  * Trường hợp thanh toán thành công nhưng xảy ra sự cố API hệ thống rạp nghẽn hoặc đứt gãy giữ ghế: Hệ thống Web Platform tự động đưa đơn hàng vào **Pending Retry Queue (5 phút)**. Nếu quá thời gian retry không xuất được vé, hệ thống tự động hoàn tiền 100% (Instant Refund) về tài khoản thanh toán của khách hàng và gửi voucher đền bù.
* **Phân Định Trách Nhiệm Luồng Gửi Vé (Fulfillment Ownership):** Khối Web Platform chịu trách nhiệm hiển thị mã vé QR điện tử trực tiếp trên giao diện màn hình xác nhận web (`/cinema/dat-ve/ve-dien-tu/{booking-id}`). Toàn bộ luồng gửi vé qua các kênh hạ tầng bên ngoài (Zalo ZNS, Email xác nhận, nhắn tin SMS mã vé) do **BU Movies** chịu trách nhiệm vận hành và quản lý ngân sách.

### 7.2 Risk Management Matrix



| Rủi ro tiềm tàng | Mức độ | Phương án xử lý | Đơn vị chịu trách nhiệm |
| :--- | :---: | :--- | :--- |
| **API Chuỗi Rạp bị nghẽn** vào khung giờ cao điểm mở bán phim bom tấn. | Cao | Triển khai cơ chế Caching lịch chiếu MoSpark & Queue giữ chỗ tạm thời trong 5 phút. | Technical Team (Lead Eng: Hùng) |
| **Người dùng hủy vé / Muốn đổi suất chiếu** sau khi thanh toán trên Web. | Trung bình | Hiển thị rõ quy định hủy vé của từng chuỗi rạp trước khi nhấp thanh toán. | Product Team & Operations |
| **Phim bị hoãn/hủy công chiếu** từ phía nhà phát hành. | Thấp | Tự động quét cập nhật trạng thái phim từ hệ thống rạp và thông báo hoàn tiền tự động. | Operations Team & BU Movies |



## VIII. Growth Roadmap & Changelog

### 8.1 Lộ Trình Phát Triển Sản Phẩm & Kế Hoạch Trọng Tâm Q4/2026 (Roadmap & Deliverables)

Kế hoạch phát triển sản phẩm Cinema Hub được phân bổ theo các giai đoạn thực tế và tiến độ thực thi:

* **Giai Đoạn Nền Tảng & Triển Khai (Tháng 8 - Tháng 9/2026 - Hoàn Thành):**
  * **Revamp Film Detail UI/UX:** Thiết kế lại toàn bộ giao diện Trang Chi Tiết Phim (`/cinema/{film-detail-ID}`) và Trang Review Phim (`/cinema/{film-detail-ID}/review`), nhúng Widget Tra cứu suất chiếu rạp realtime 13 chuỗi rạp.
  * **Minigame Platform cho Cinema:** Xây dựng Nền tảng Minigame Platform (Google OAuth 1-tap, Thẻ Cào Scratch Card, Săn Mã Số May Mắn) thúc đẩy Organic Search CTR từ từ khóa *'Tên Phim + MoMo'* trên Google SERP, kết nối In-App Social Feed Comment với đội MDS-Movies.
  * **Blog Migration sang MoSpark CMS:** Chuyển dịch toàn bộ kho bài viết Blog, Review phim và Cẩm nang điện ảnh cũ sang hạ tầng MoSpark CMS mới.
  * **Data-Driven Box Office Leaderboard:** Ra mắt trang Doanh Thu Phòng Vé (`/cinema/doanh-thu-phong-ve` và alias `/doanh-thu-phong-ve`) kết nối Box Office Vietnam Live Feed + Schema `Dataset` & `ItemList` cho Google AI Overview.
  * **Trợ Lý Tư Vấn Phòng Vé AI:** Xây dựng kịch bản trợ lý ảo tư vấn phim, tra cứu lịch chiếu và kết nối luồng đặt vé nhanh 1-chạm sang App MoMo.

* **Giai Đoạn Tối Ưu Hóa & Tăng Trưởng Bền Vững (Tháng 10/2026 - Đã Chốt Sổ Thành Công):**
  * **Duy Trì Vị Thế Dẫn Đầu Lưu Lượng:** Đạt 1.13M PVs (101.4% Target Tháng 10), lượng tìm kiếm tự nhiên tăng +21.7% MoM bù đắp -92.9% cắt giảm ngân sách Paid Ads.
  * **Chốt Đơn Bán Vé In-App Kỷ Lục:** Đạt 12,547 đơn hàng và 2.57 tỷ đồng GMV thực thu in-app (+20.1% MoM).
  * **Thử Nghiệm Giao Diện Cụm Rạp Mới (NCC Pilot):** Đã Go-live thử nghiệm tại Trung Tâm Chiếu Phim Quốc Gia (NCC) bảo toàn chất lượng trước khi mở rộng.

* **Giai Đoạn Trọng Tâm Q4/2026 (Tháng 11 - Tháng 12/2026 - Đang Triển Khai):**
  * **1. Hạ Tầng Lịch Chiếu Theo Tỉnh Thành Sau Sáp Nhập (Local GEO Screening Architecture):**
    * *Mục tiêu:* Phục vụ nhu cầu tìm kiếm lịch chiếu địa phương sau khi sáp nhập các đơn vị hành chính tỉnh thành, tránh đứt gãy luồng tra cứu của người dùng.
    * *Kiến trúc URL Chuyên biệt:* Triển khai các URL độc lập dạng `/cinema/{film-slug}-{id}/lich-chieu-{tinh-thanh}` (ví dụ: `/cinema/ngay-con-con-me-25093/lich-chieu-tp-ho-chi-minh`).
    * *Chuẩn Hóa Schema ScreeningEvent Độc Lập:* Tích hợp bộ Schema chuẩn hóa kết hợp `ScreeningEvent`, `Movie`, `MovieTheater`, `Offer` cho từng suất chiếu cụ thể nhằm tối ưu hiển thị Rich Results và Google AI Overview.
    * *Cơ chế Crawl Budget & Anti-Spam Control:* Áp dụng Dynamic Noindex cho các tỉnh thành có ít hơn 2 rạp hoạt động để bảo vệ chất lượng chỉ mục Google.
  * **2. Chiến Dịch Hợp Tác Bom Tấn Cuối Năm: Avengers: Doomsday (Disney x MoMo x CGV):**
    * *Mục tiêu:* Khai thác tối đa sự kiện điện ảnh lớn nhất năm 2026 để bứt phá lưu lượng tìm kiếm tự nhiên ngoài web (Organic Web Traffic) và đạt mốc doanh số bán vé kỷ lục.
    * *Pillar Page Doomsday:* Xây dựng Website phim đặc biệt với visual hiệu ứng Marvel, đếm ngược ngày chiếu và widget giữ ghế 1-click.
    * *Cụm Nội Dung Tri Thức & Topic Cluster:* Trang Chủ đề 3 Phase Marvel, Timeline *"Xem gì trước Doomsday"* (kết nối Secret Wars 2027), Wiki thẻ nhân vật *"X là ai"* đón đầu câu trả lời trực tiếp của Google AI Overview và AI Search.
    * *Gamification & Engagement Hook:* Interactive Quiz *"Bạn là Avenger nào?"* lồng ghép Easter Egg, tặng voucher vé / combo bắp nước và cơ hội nhận Mặt nạ Dr. Doom (10 mặt nạ từ Disney).
    * *Khai Thác Merchandise Độc Quyền MoMo:* Triển khai cơ chế tích điểm/tích vé đổi **40 Avengers Backpacks** (độc quyền Disney dành riêng cho khách hàng MoMo, không cung cấp cho bất kỳ đơn vị rạp hay bán vé nào khác).
    * *Suất Chiếu Fan Screening Độc Quyền CGV x MoMo:* Mở các suất chiếu đặc biệt chỉ bán duy nhất trên MoMo Web/App (phối hợp CGV lock suất chiếu).
    * *Chuỗi Trải Nghiệm O2O & Sự Kiện Premiere:* Đồng hành khu trải nghiệm Avengers: Doomsday tại Royal City (Hà Nội, 14-27/12/2026 - Premiere 15/12) và Landmark 81 (TP.HCM, 14-17/12/2026 - Premiere 16/12).
    * *Brand Takeover:* Khoác giao diện theme Doomsday lên toàn bộ trang chủ `momo.vn/cinema` trước và trong tuần công chiếu.
  * **3. Trợ Lý AI Phòng Vé (MoMo Cinema AI Concierge):**
    * *Mục tiêu:* Đưa vào hoạt động trợ lý thông minh lắng nghe và chuyển hóa trọn vẹn 4 nhóm ý định của người dùng (Khám phá phim, Khớp lịch chiếu/vị trí gần nhất, Tối ưu ưu đãi chi phí, Xác thực thông tin nhanh) thành quyết định mua vé tức thì.
    * *Trải Nghiệm Dẫn Dắt:* Chuyển đổi từ trải nghiệm tra cứu tĩnh sang tương tác tự nhiên, phản hồi đúng trọng tâm và cung cấp thẻ lựa chọn 1-chạm kết nối thẳng vào màn hình giữ chỗ trên App MoMo.
    * *Thử Nghiệm & Đánh Giá:* Triển khai thử nghiệm giao diện tư vấn tại Trang Chi Tiết Phim và Trang Cụm Rạp trong Tháng 12/2026, đo lường mức độ tương tác và tỷ lệ chuyển đổi mua vé thực tế.

### 8.2 Quy Trình Phối Hợp & Đề Xuất (Proposal Standard)
* Mọi đề xuất tính năng PO bắt buộc phải chuẩn bị slide gồm 4 phần: Vấn đề/Thách thức  ➔  Giải pháp đề xuất  ➔  Tác động kinh doanh dự kiến  ➔  UI Mockup phác thảo.
* Cập nhật báo cáo định kỳ cho Ban Giám Đốc (VP/CEO) về tiến độ thực thi và điều chỉnh kế hoạch vận hành.

### 8.3 Change Log



| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
| :--- | :--- | :--- | :--- |
| **v3.7** | 2026-11-18 | Web Product Lead | **Chốt lại lũy kế Cinema W2A T1-T10 theo Dashboard In-App:** 60,378 người dùng giao dịch, 77,625 đơn, 168,884 vé, 15.91 tỷ đồng GMV thực thu (148.4% cả năm 2025), thay cho số cộng dồn bảng tháng 80,050 đơn / 174,094 vé / 16.41 tỷ. Phần chênh bằng đúng Tháng 7, đang đối soát. |
| **v3.6** | 2026-11-16 | Web Product Lead | **Bổ sung Cập nhật Hiệu suất MTD Tháng 11/2026 (Mục 1.5.D):** Lưu lượng Web Cinema Hub MTD 15 ngày đạt 378.569 PVs số liệu sạch (29.2% Target 1.294.630, -42.1% MoM do mùa vụ), cơ cấu 8 nhóm trang theo chuẩn tracking mới, và phễu Web-to-App AppsFlyer MTD 10 ngày ghi nhận End-to-End CVR 12.1% cao nhất toàn Web. Ghi chú rõ số liệu đơn hàng/GMV in-app T11 chờ đối soát BU Movies. Đồng thời bổ sung Bảng Web Traffic Performance theo tháng (GA4 PageViews T1-T10/2026 + MTD T11) tại Mục 1.4 và chuyển toàn bộ bảng HTML inline sang Markdown table. |
| **v3.5** | 2026-11-11 | Web Product Lead | **Bổ sung Định hướng Trợ Lý AI Phòng Vé (MoMo Cinema AI Concierge):** Mô tả toàn diện 4 nhóm ý định cốt lõi của người dùng (Khám phá phim, Khớp lịch chiếu/vị trí tiện lợi, Tối ưu ưu đãi chi phí, Xác thực thông tin nhanh) và hành trình chuyển hóa ý định thành hành động đặt vé mượt mà sang App MoMo tại Mục 3.5. |
| **v3.4** | 2026-11-11 | Web Product Lead | **Rà soát toàn diện BRD Cinema Hub:** Chuẩn hóa phân cấp tiêu đề (Section III, 5.1.3, 5.1.4, Section VI), loại bỏ các liên kết tệp phân mảnh để tối ưu tính độc lập sạch gọn, hợp nhất Kiến trúc Phễu Chuyển Đổi 6 tầng, cập nhật số liệu vận hành chốt sổ Tháng 10/2026 (16.41 tỷ GMV in-app, 174K vé), bổ sung kiến trúc Schema Lịch chiếu Tỉnh thành và kế hoạch Chiến dịch Bom tấn Disney - Avengers: Doomsday Q4/2026. |
| **v3.3** | 2026-11-02 | Web Product Lead | **Cập nhật Báo cáo Hiệu suất Chốt sổ Tháng 10/2026:** Xác nhận số liệu 10 tháng chính thức từ in-app Dashboard (80,050 đơn hàng, 174,094 vé, 16.41 tỷ GMV thực thu), đánh giá chuyển dịch bền vững sang Organic Traffic (+21.7% MoM) khi cắt giảm 92.9% Paid Ads. |
| **v3.2** | 2026-10-02 | Web Product Lead | **Cập nhật Báo cáo Hiệu suất Chốt sổ Tháng 9/2026:** Đạt kỷ lục 1.22M PVs (vượt +26.5% Target), bóc tách lưu lượng theo từng Sub-page và đánh giá thử nghiệm giao diện rạp mới NCC. |
| **v3.1** | 2026-08-05 | Web Product Lead | **Cập nhật Kế hoạch Hoạt động Trọng tâm Tháng 8/2026:** Bổ sung phân loại hoạt động theo 2 trụ cột Software Engineering & Out-App Traffic Strategy, quy định chuẩn slide Proposal và chuyển đổi MoSpark. |
| **v3.0** | 2026-07-30 | Web Product Lead | **Chuyển đổi sang Cinema Hub Master BRD:** Tái cấu trúc toàn diện tài liệu theo quy chuẩn kiến trúc Hub độc lập. Bổ sung 5 Phễu PLG, Native Web Payment Flow, Hub-and-Spoke Sitemap, Schema.org Matrix và Lộ trình phát triển H2/2026. |
| **v2.6** | 2026-07-22 | Web Product Lead x BU Movies | Thống nhất Kế hoạch H2/2026: Cam kết Uplift 100% các chỉ số (Organic Traffic 4.02M, Total Traffic 8.07M, Tickets Sold 214K vé), phân định Collaboration Model giữa BU Movies & Web Platform. |



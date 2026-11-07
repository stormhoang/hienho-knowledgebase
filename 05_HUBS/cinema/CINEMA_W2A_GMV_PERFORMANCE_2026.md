# BÁO CÁO HIỆU SUẤT CHUYỂN ĐỔI WEB-TO-APP & QUY ĐỔI DOANH THU GMV (2025 - 2026)
**Dự án:** Cinema Hub (Web Platform x BU Movies)  
**Tài liệu tham chiếu:** [`MOVIES DATA SUMMARY.xlsx`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/cinema/data/MOVIES_DATA_SUMMARY.xlsx)  
**Dữ liệu snapshot JSON:** [`movies_app_w2a_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/cinema/data/movies_app_w2a_performance.json)  
**File Excel SSOT:** [`cinema_hub_roadmap_drive_sync.xlsx`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/cinema/cinema_hub_roadmap_drive_sync.xlsx) (Sheet: `W2A & GMV 2026`)  
**Công thức chuẩn hóa doanh thu:**
* **GMV Thực Thu (Actual GMV - Tiêu chuẩn tài chính SSOT):**
  $$\text{GMV Thực Thu} = \text{Success Transactions} \times \text{AoV (205,000 VND)}$$
* **GMV Tiềm Năng Quy Đổi (Potential Reach GMV):**
  $$\text{GMV Tiềm Năng} = \text{W2A MAU} \times \text{AoV (205,000 VND)}$$
*(Quy chuẩn AoV: 205,000 đồng/đơn hàng, trung bình 2.13 vé/giao dịch, tương đương ~96,000 đồng/vé).*

---

## 1. TỔNG QUAN HIỆU SUẤT 8 THÁNG ĐẦU NĂM 2026

Trong 8 tháng đầu năm 2026, kênh Web-to-App (người dùng từ Website MoMo chuyển tiếp sang ứng dụng hoặc quét mã QR thanh toán trên Web) đã đóng góp:
* **Tổng số người dùng hoạt động (W2A MAU):** **49,282 MAU** (so với 54,968 MAU cùng kỳ 2025, giảm -10.3%).
* **Tổng lượt tương tác chuyển đổi (W2A MEU):** **144,349 MEU** (so với 151,560 MEU cùng kỳ 2025, giảm -4.8%).
* **Tổng giá trị giao dịch quy đổi (GMV Web-to-App):** **10,102,810,000 đồng (10.10 tỷ đồng)**, mang lại nguồn doanh số bán vé tự nhiên (Inbound) ổn định cho BU Movies.

### Bảng hiệu suất chi tiết 8 tháng đầu năm 2026 so với cùng kỳ 2025

| Tháng | 2026 W2A MAU | 2026 W2A MEU | GMV W2A 2026 (VND) | 2025 W2A MAU | 2025 W2A MEU | GMV W2A 2025 (VND) | Tăng trưởng YoY GMV (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tháng 1** | 5,362 | 20,258 | 1,099,210,000 đ | 2,687 | 6,304 | 550,835,000 đ | +99.6% |
| **Tháng 2 (Tết)** | 10,922 | 27,595 | 2,239,010,000 đ | 9,090 | 20,202 | 1,863,450,000 đ | +20.2% |
| **Tháng 3** | 8,728 | 23,839 | 1,789,240,000 đ | 4,963 | 12,580 | 1,017,415,000 đ | +75.9% |
| **Tháng 4** | 7,300 | 20,020 | 1,496,500,000 đ | 8,855 | 33,232 | 1,815,275,000 đ | -17.6% |
| **Tháng 5** | 5,141 | 15,823 | 1,053,905,000 đ | 5,285 | 13,856 | 1,083,425,000 đ | -2.7% |
| **Tháng 6** | 5,809 | 16,046 | 1,190,845,000 đ | 2,667 | 6,502 | 546,735,000 đ | +117.8% |
| **Tháng 7** | 2,263 | 7,806 | 463,915,000 đ | 4,880 | 13,632 | 1,000,400,000 đ | -53.6% |
| **Tháng 8** | 3,757 | 12,962 | 770,185,000 đ | 16,541 | 45,252 | 3,390,905,000 đ | -77.3% |
| **Lũy kế 8 Tháng** | **49,282** | **144,349** | **10,102,810,000 đ** | **54,968** | **151,560** | **11,268,440,000 đ** | **-10.3%** |

---

## 2. BÁO CÁO GIAO DỊCH THỰC THU (SUCCESS IN-APP TRANSACTIONS) - CẬP NHẬT THÁNG 10 VÀ QUÝ 4/2026

Dữ liệu ghi nhận từ hệ thống Dashboard vận hành bán vé in-app (`SUCCESS IN-APP TRANSACTIONS`) phản ánh số liệu giao dịch chốt đơn thực tế của người dùng từ Web chuyển sang App:

### A. Kết quả thực tế Tháng 10/2026 (Realtime Dashboard)
* **Số giao dịch thành công (Transactions):** **12,547 đơn** (Tăng trưởng **+20.1%** so với tháng 9).
* **Số người dùng giao dịch thành công (Transacting Users):** **11,457 người** (Tăng trưởng **+20.7%** so với tháng 9).
* **Số lượng vé bán ra (Tickets):** **26,789 vé** (Tăng trưởng **+18.8%** so với tháng 9).
* **Doanh thu GMV thực thu:** **2,572,135,000 đồng (2.57 tỷ đồng)** (dựa trên AoV chuẩn 205,000 đồng/đơn).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Tần suất mua hàng:** 12,547 / 11,457 = **1.095 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 26,789 / 12,547 = **2.135 vé/đơn** (hành vi đi xem phim theo cặp đôi hoặc bạn bè).
  * **Giá vé bình quân thực tế:** 2,572,135,000 / 26,789 = **96,014 đồng/vé** (khớp sát với mặt bằng giá vé rạp phim hiện tại).

### B. Dữ liệu suy luận Tháng 9/2026 (Truy ngược từ tăng trưởng MoM Tháng 10)
Từ tỷ lệ tăng trưởng so với tháng trước của Tháng 10, chỉ số Tháng 9/2026 được xác định:
* **Transactions Tháng 9:** 12,547 / 1.201 = **10,447 đơn hàng**.
* **Transacting Users Tháng 9:** 11,457 / 1.207 = **9,492 người dùng**.
* **Tickets Tháng 9:** 26,789 / 1.188 = **22,550 vé**.
* **GMV thực thu Tháng 9:** 10,447 * 205,000 = **2,141,635,000 đồng (~2.14 tỷ đồng)**.
* **Tổng doanh thu thực thu 2 tháng Q4 (Tháng 9 và Tháng 10):** Đạt **22,994 đơn hàng**, tương ứng **4.71 tỷ đồng GMV**.

### C. Bảng đối soát Giao dịch Thực thu và Doanh thu Lũy kế 10 Tháng 2026

| Kỳ Báo Cáo | Transacting Users | Transactions (Đơn) | Tickets (Vé) | GMV Thực Thu (VND) | Tăng trưởng MoM | Vé / Đơn | Ghi Chú Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Năm 2025 (Cả năm)** | 93,758 (MAU) | 52,311 | 111,422 | 10,723,755,000 đ | - | 2.13 | Sheet REPORT 2025 (Inbound) |
| **8 Tháng đầu 2026 (Ước tính)** | 49,282 (MAU) | 27,494 | 58,562 | 5,636,270,000 đ | - | 2.13 | Áp dụng tỷ lệ CR 55.79% trên MAU |
| **Tháng 9/2026** | 9,492 | 10,447 | 22,550 | 2,141,635,000 đ | - | 2.16 | Truy ngược từ tăng trưởng MoM |
| **Tháng 10/2026 (Thực tế)** | 11,457 | 12,547 | 26,789 | 2,572,135,000 đ | +20.1% | 2.13 | Dashboard In-App |
| **Lũy kế 10 Tháng 2026** | **70,231** | **50,488** | **107,901** | **10,350,040,000 đ** | - | **2.14** | **Tổng hợp 8T ước tính + T9 + T10 thực tế** |

* **Đánh giá hiệu quả kinh doanh:** Chỉ trong 10 tháng năm 2026, lượng giao dịch Web-to-App đã đạt **50,488 đơn** (~10.35 tỷ đồng GMV thực thu), tương đương **96.5% tổng doanh thu cả năm 2025** (52,311 đơn, 10.72 tỷ đồng). Riêng Tháng 10 đạt 12,547 đơn (gấp gần 3 lần mức trung bình 4,359 đơn/tháng của năm 2025), khẳng định kênh Web-to-App đang tăng trưởng vượt bậc trong quý 4/2026.

---

## 3. DỮ LIỆU ĐỐI CHỨNG NĂM 2025 (BENCHMARK TOÀN DIỆN)

Trong năm 2025, Kênh Web-to-App đã chứng minh là một kênh phân phối doanh thu lớn với tổng GMV vượt **19.22 tỷ đồng**, chiếm tỷ trọng trung bình **1.57% tổng doanh thu bán vé** toàn ứng dụng MoMo:

| Tháng | W2A MAU | GMV W2A (VND) | Native App MAU | Tổng GMV Cinema App (VND) | Tỷ trọng W2A (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tháng 1** | 2,687 | 550,835,000 đ | 314,058 | 64,381,890,000 đ | 0.86% |
| **Tháng 2** | 9,090 | 1,863,450,000 đ | 855,966 | 175,473,030,000 đ | 1.06% |
| **Tháng 3** | 4,963 | 1,017,415,000 đ | 434,516 | 89,075,780,000 đ | 1.14% |
| **Tháng 4** | 8,855 | 1,815,275,000 đ | 453,568 | 92,981,440,000 đ | 1.95% |
| **Tháng 5** | 5,285 | 1,083,425,000 đ | 561,569 | 115,121,645,000 đ | 0.94% |
| **Tháng 6** | 2,667 | 546,735,000 đ | 287,509 | 58,939,345,000 đ | 0.93% |
| **Tháng 7** | 4,880 | 1,000,400,000 đ | 379,264 | 77,749,120,000 đ | 1.29% |
| **Tháng 8 (Kỷ lục)**| **16,541** | **3,390,905,000 đ** | **725,956** | **148,820,980,000 đ** | **2.28%** |
| **Tháng 9** | 14,952 | 3,065,160,000 đ | 676,630 | 138,709,150,000 đ | 2.21% |
| **Tháng 10** | 6,092 | 1,248,860,000 đ | 348,812 | 71,506,460,000 đ | 1.75% |
| **Tháng 11** | 7,314 | 1,499,370,000 đ | 414,509 | 84,974,345,000 đ | 1.76% |
| **Tháng 12** | 10,432 | 2,138,560,000 đ | 519,192 | 106,434,360,000 đ | 2.01% |
| **Tổng cả năm 2025** | **93,758** | **19,220,390,000 đ** | **5,971,549** | **1,224,167,545,000 đ** | **1.57%** |

---

## 4. PHỄU CHUYỂN ĐỔI INBOUND & ĐIỂM NGHẼN RÒ RỈ LƯU LƯỢNG

Phễu chuyển đổi 4 tầng từ Kênh Inbound (Google Search -> Web MoMo Cinema -> App MoMo -> Đơn hàng) cho thấy hai đặc điểm đối lập:

```
[Google SERP Impressions] (282.9M)
          |
          v
[Web Traffic Pageviews] (12.4M PV)
          |
          v
[Booking Clicks trên Web] (266,258 clicks) --- (CTR: 2.14%)
          |
          v  <--- ĐIỂM GÃY LỚN NHẤT: Rơi rớt 70.4% ở bước OneLink!
[Traffic vào App thực tế] (78,735 lượt) ------ (W2A CVR: 29.57%)
          |
          v  <--- CHẤT LƯỢNG CHUYỂN ĐỔI CỰC CAO: 66.4% chốt đơn!
[Đơn hàng mua vé hoàn tất] (52,311 đơn) ------- (In-App CVR: 66.44%)
```

* **Điểm sáng:** Khách hàng từ Web vào App có tỷ lệ mua vé thành công cực kỳ cao (66.44%). Cứ 3 người vào App từ Web thì có 2 người mua vé thành công.
* **Điểm nghẽn nghiêm trọng:** Cứ 100 người nhấp nút đặt vé trên Web, có tới **70 người bị rơi rớt dọc đường**, chỉ có gần 30 người mở được App thành công.

---

## 5. MÔ HÌNH ĐỊNH LƯỢNG CƠ HỘI DOANH THU (OPPORTUNITY SIZING)

Nếu Web Platform phối hợp cùng BU Movies xử lý triệt để nút thắt OneLink và Bridge UX, doanh số GMV mang về cho BU Movies sẽ tăng trưởng đột phá mà không cần tăng ngân sách kéo traffic:

| Kịch bản | Tỷ lệ mở App (%W2A) | Lượt vào App (In-App) | Ước tính W2A MAU | Ước tính GMV (VND) | Doanh thu tăng thêm (VND) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hiện trạng cơ sở (Baseline)** | 29.57% | 78,735 | 93,758 | 19,220,390,000 đ | 0 đ (Mốc quy chiếu) |
| **Tối ưu OneLink & Bridge UX** | 40.00% | 106,503 | 126,832 | 26,000,560,000 đ | **+6.78 tỷ đồng** |
| **Tối ưu Cao cấp + Chatbot Deeplink** | 45.00% | 119,816 | 142,686 | 29,250,630,000 đ | **+10.03 tỷ đồng** |
| **Đột phá Toàn diện (Web + Mini App)**| 50.00% | 133,129 | 158,540 | 32,500,700,000 đ | **+13.28 tỷ đồng** |

---

## 6. KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI

1. **Đối soát số liệu Tháng 9 và Tháng 10/2026 với BU Movies:**
   * Gửi đề nghị BU Movies trích xuất bổ sung W2A MAU/MEU của Tháng 9 và Tháng 10/2026 để khớp với mốc 1.2M PV/tháng trên hệ thống Web Tracking.
2. **Triển khai Bridge Page & QR Động:**
   * Thay thế link tĩnh bằng cầu nối thông minh: Với mobile mở thẳng App; với desktop hiển thị mã QR động chứa thông tin rạp và suất chiếu đã chọn để quét thanh toán tức thì.
3. **Kích hoạt Cinema Chatbot theo PRD:**
   * Đưa nút CTA đặt vé gắn Deeplink trực tiếp vào các câu trả lời tư vấn suất chiếu, rạp gần nhất và giá vé, tận dụng tỷ lệ chốt đơn 66.4% của tệp người dùng Inbound.

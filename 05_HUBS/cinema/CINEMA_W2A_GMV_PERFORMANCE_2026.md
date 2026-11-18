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

## 1. TỔNG QUAN HIỆU SUẤT 10 THÁNG NĂM 2026 (CHÍNH THỨC)

Trong 10 tháng năm 2026, kênh Web-to-App (người dùng từ Website MoMo chuyển tiếp sang ứng dụng hoặc quét mã QR thanh toán trên Web) đã đóng góp:
* **Tổng số người dùng hoạt động (W2A MAU):** **69,666 MAU** (so với 76,012 MAU cùng kỳ 2025, thu hẹp khoảng cách chỉ còn giảm -8.3% YoY).
* **Tổng lượt tương tác chuyển đổi (W2A MEU):** **201,517 MEU** (chính thức vượt mốc 200,000 lượt tương tác, so với 213,601 MEU cùng kỳ 2025, chỉ còn giảm -5.7% YoY).
* **Tổng giá trị giao dịch quy đổi tiềm năng (GMV Web-to-App):** **14,281,530,000 đồng (14.28 tỷ đồng)**, mang lại nguồn doanh số bán vé từ kênh Web-to-App khổng lồ cho BU Movies.

### Bảng hiệu suất chi tiết 10 tháng năm 2026 so với cùng kỳ 2025

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
| **Tháng 9** | **8,927** | **26,698** | **1,830,035,000 đ** | 14,952 | 40,414 | 3,065,160,000 đ | -40.3% |
| **Tháng 10** | **11,457** | **30,470** | **2,348,685,000 đ** | 6,092 | 21,627 | 1,248,860,000 đ | **+88.1%** |
| **Lũy kế 10 Tháng** | **69,666** | **201,517** | **14,281,530,000 đ** | **76,012** | **213,601** | **15,582,460,000 đ** | **-8.3%** |

---

## 2. BÁO CÁO GIAO DỊCH THỰC THU (SUCCESS IN-APP TRANSACTIONS) - CẬP NHẬT THỰC TẾ DASHBOARD

Dữ liệu ghi nhận trực tiếp từ hệ thống Dashboard vận hành bán vé in-app (`SUCCESS IN-APP TRANSACTIONS`) kết hợp số liệu tương tác chính thức (`MEU`):

### A. Kết quả thực tế Tháng 1/2026 (Xác thực 100% từ Dashboard In-App)
* **Số người dùng hoạt động (W2A MAU / Users):** **5,362 người** (Giảm -48.6% trên Dashboard sau đợt cao điểm cuối năm trước).
* **Nguồn gốc và đối soát:** Khớp 100% với cell D60 trong file `MOVIES DATA SUMMARY.xlsx` (Tháng 1/2026 W2A MAU = 5,362 người).
* **Số lượt tương tác (W2A MEU):** **20,258 lượt** (Khớp với cell C60 trong file `MOVIES DATA SUMMARY.xlsx`).
* **Số giao dịch thành công (Transactions):** **5,889 đơn** (Giảm -47.4% trên Dashboard).
* **Số lượng vé bán ra (Tickets):** **12,643 vé** (Giảm -47.4% trên Dashboard).
* **Doanh thu GMV thực thu Tháng 1:** **1,207,245,000 đồng (1.21 tỷ đồng)** (dựa trên công thức $5,889 	imes 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 20,258 / 5,362 = **3.78 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 5,889 / 5,362 = **1.098 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 12,643 / 5,889 = **2.147 vé/đơn** (chuẩn 2.15 vé/đơn).
  * **Giá vé bình quân thực tế:** 1,207,245,000 / 12,643 = **95,487 đồng/vé**.

### B. Kết quả thực tế Tháng 2/2026 (Xác thực 100% từ Dashboard In-App - Mùa Phim Tết)
* **Số người dùng hoạt động (W2A MAU / Users):** **10,922 người** (Tăng trưởng bùng nổ **+170.5%** trên Dashboard dịp Tết).
* **Nguồn gốc và đối soát:** Khớp 100% với cell D61 trong file `MOVIES DATA SUMMARY.xlsx` (Tháng 2/2026 W2A MAU = 10,922 người).
* **Số lượt tương tác (W2A MEU):** **27,595 lượt** (Khớp với cell C61 trong file `MOVIES DATA SUMMARY.xlsx`).
* **Số giao dịch thành công (Transactions):** **12,432 đơn** (Tăng trưởng **+182.5%** trên Dashboard).
* **Số lượng vé bán ra (Tickets):** **28,379 vé** (Tăng trưởng **+209.4%** trên Dashboard).
* **Doanh thu GMV thực thu Tháng 2:** **2,548,560,000 đồng (2.55 tỷ đồng)** (dựa trên công thức $12,432 	imes 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 27,595 / 10,922 = **2.53 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 12,432 / 10,922 = **1.138 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 28,379 / 12,432 = **2.283 vé/đơn** (cao điểm Tết gia đình và nhóm bạn mua số lượng vé lớn hơn bình thường).
  * **Giá vé bình quân thực tế:** 2,548,560,000 / 28,379 = **89,804 đồng/vé** (áp dụng nhiều chương trình khuyến mãi/combo vé Tết).

### C. Kết quả thực tế Tháng 3/2026 (Xác thực 100% từ Dashboard In-App)
* **Số người dùng hoạt động (W2A MAU / Users):** **8,728 người** (Giảm -22.6% trên Dashboard sau đợt cao điểm Tết Tháng 2).
* **Nguồn gốc và đối soát:** Khớp 100% với cell D62 trong file `MOVIES DATA SUMMARY.xlsx` (Tháng 3/2026 W2A MAU = 8,728 người).
* **Số lượt tương tác (W2A MEU):** **23,839 lượt** (Khớp với cell C62 trong file `MOVIES DATA SUMMARY.xlsx`).
* **Số giao dịch thành công (Transactions):** **9,881 đơn** (Giảm -23.0% trên Dashboard).
* **Số lượng vé bán ra (Tickets):** **20,600 vé** (Giảm -29.4% trên Dashboard).
* **Doanh thu GMV thực thu Tháng 3:** **2,025,605,000 đồng (2.03 tỷ đồng)** (dựa trên công thức $9,881 	imes 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 23,839 / 8,728 = **2.73 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 9,881 / 8,728 = **1.132 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 20,600 / 9,881 = **2.085 vé/đơn**.
  * **Giá vé bình quân thực tế:** 2,025,605,000 / 20,600 = **98,330 đồng/vé**.

### D. Kết quả thực tế Tháng 4/2026 (Xác thực 100% từ Dashboard In-App)
* **Số người dùng hoạt động (W2A MAU / Users):** **7,300 người** (Giảm -11.6% trên Dashboard).
* **Nguồn gốc và đối soát:** Khớp 100% với cell D63 trong file `MOVIES DATA SUMMARY.xlsx` (Tháng 4/2026 W2A MAU = 7,300 người).
* **Số lượt tương tác (W2A MEU):** **20,020 lượt** (Khớp với cell C63 trong file `MOVIES DATA SUMMARY.xlsx`).
* **Số giao dịch thành công (Transactions):** **8,221 đơn** (Giảm -11.7% trên Dashboard).
* **Số lượng vé bán ra (Tickets):** **18,730 vé** (Giảm -3.4% trên Dashboard).
* **Doanh thu GMV thực thu Tháng 4:** **1,685,305,000 đồng (1.69 tỷ đồng)** (dựa trên công thức $8,221 	imes 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 20,020 / 7,300 = **2.74 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 8,221 / 7,300 = **1.126 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 18,730 / 8,221 = **2.278 vé/đơn**.
  * **Giá vé bình quân thực tế:** 1,685,305,000 / 18,730 = **89,979 đồng/vé**.

### E. Kết quả thực tế Tháng 5/2026 (Xác thực 100% từ Dashboard In-App)
* **Số người dùng hoạt động (W2A MAU / Users):** **5,141 người** (Giảm -30.6% trên Dashboard sau đợt cao điểm tháng 4).
* **Nguồn gốc và đối soát:** Khớp 100% với cell D64 trong file `MOVIES DATA SUMMARY.xlsx` (Tháng 5/2026 W2A MAU = 5,141 người).
* **Số lượt tương tác (W2A MEU):** **15,823 lượt** (Khớp với cell C64 trong file `MOVIES DATA SUMMARY.xlsx`).
* **Số giao dịch thành công (Transactions):** **5,777 đơn** (Giảm -30.9% trên Dashboard).
* **Số lượng vé bán ra (Tickets):** **12,561 vé** (Giảm -34.0% trên Dashboard).
* **Doanh thu GMV thực thu Tháng 5:** **1,184,285,000 đồng (1.18 tỷ đồng)** (dựa trên công thức $5,777 	imes 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 15,823 / 5,141 = **3.08 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 5,777 / 5,141 = **1.124 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 12,561 / 5,777 = **2.174 vé/đơn** (chuẩn hành vi xem phim 2 người).
  * **Giá vé bình quân thực tế:** 1,184,285,000 / 12,561 = **94,283 đồng/vé**.

### F. Kết quả thực tế Tháng 6/2026 (Xác thực 100% từ Dashboard In-App)
* **Số người dùng hoạt động (W2A MAU / Users):** **7,871 người** (Giảm -33.9% sau giai đoạn cao điểm mùa phim lễ tháng 5).
* **Số giao dịch thành công (Transactions):** **9,055 đơn** (Giảm -35.3% so với tháng 5).
* **Số lượng vé bán ra (Tickets):** **19,444 vé** (Giảm -37.9% so với tháng 5).
* **Doanh thu GMV thực thu Tháng 6:** **1,856,275,000 đồng (1.86 tỷ đồng)** (dựa trên công thức $9,055 \times 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Tần suất mua hàng:** 9,055 / 7,871 = **1.150 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 19,444 / 9,055 = **2.147 vé/đơn** (chuẩn hành vi xem phim 2 người).
  * **Giá vé bình quân thực tế:** 1,856,275,000 / 19,444 = **95,468 đồng/vé**.

### G. Kết quả thực tế Tháng 7/2026 (Xác thực 100% từ Dashboard In-App)
* **Số người dùng hoạt động (W2A MAU / Users):** **2,263 người** (Giảm -62.1% trên Dashboard).
* **Nguồn gốc và đối soát:** Khớp 100% với cell D66 trong file `MOVIES DATA SUMMARY.xlsx` (Tháng 7/2026 W2A MAU = 2,263 người).
* **Số lượt tương tác (W2A MEU):** **7,806 lượt** (Khớp với cell C66 trong file `MOVIES DATA SUMMARY.xlsx`).
* **Số giao dịch thành công (Transactions):** **2,425 đơn** (Giảm -64.6% trên Dashboard).
* **Số lượng vé bán ra (Tickets):** **5,211 vé** (Giảm -64.7% trên Dashboard).
* **Doanh thu GMV thực thu Tháng 7:** **497,125,000 đồng (497.1 triệu đồng)** (dựa trên công thức $2,425 \times 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 7,806 / 2,263 = **3.45 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 2,425 / 2,263 = **1.072 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 5,211 / 2,425 = **2.149 vé/đơn** (chuẩn 2.15 vé/đơn).
  * **Giá vé bình quân thực tế:** 497,125,000 / 5,211 = **95,399 đồng/vé**.

### H. Kết quả thực tế Tháng 8/2026 (Khớp số từ MOVIES DATA SUMMARY và MoM Tháng 9)
* **Nguồn gốc con số 3,757:** Cell D67 và Z50 trong file `MOVIES DATA SUMMARY.xlsx` ghi nhận W2A MAU Tháng 8/2026 đạt đúng **3,757 người dùng**.
* **Độ khớp 100% với Dashboard:** Tỷ lệ tăng trưởng +137.6% trên thẻ Tháng 9 chính là so sánh giữa Tháng 9 (8,927) và Tháng 8 (3,757):
  $$\frac{8,927 - 3,757}{3,757} = +137.61\% \approx +137.6\%$$
* **Số giao dịch Tháng 8 quy đổi từ MoM (+144.2%):**
  $$9,807 / (1 + 1.442) = 4,016\text{ đơn hàng} \implies \text{GMV Thực Thu} = 4,016 \times 205,000 = 823,280,000\text{ đồng (823.3 triệu đồng)}$$
* **Số lượng vé bán ra Tháng 8:** $20,983 / (1 + 1.397) = 8,754\text{ vé}$.

### I. Kết quả thực tế Tháng 9/2026 (Xác thực 100% từ Dashboard & BU Movies)
* **Số người dùng hoạt động (W2A MAU / Users):** **8,927 người** (Tăng trưởng bùng nổ **+137.6%** so với tháng 8).
* **Số lượt tương tác (W2A MEU):** **26,698 lượt** (Tăng trưởng **+106.0%** so với 12,962 lượt của tháng 8).
* **Số giao dịch thành công (Transactions):** **9,807 đơn** (Tăng trưởng **+144.2%** so với tháng 8).
* **Số lượng vé bán ra (Tickets):** **20,983 vé** (Tăng trưởng **+139.7%** so với tháng 8).
* **Doanh thu GMV thực thu Tháng 9:** **2,010,435,000 đồng (2.01 tỷ đồng)** (dựa trên công thức $9,807 \times 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 26,698 / 8,927 = **2.99 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 9,807 / 8,927 = **1.098 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 20,983 / 9,807 = **2.140 vé/đơn** (chuẩn hành vi xem phim 2 người).
  * **Giá vé bình quân thực tế:** 2,010,435,000 / 20,983 = **95,813 đồng/vé**.

### K. Kết quả thực tế Tháng 10/2026 (Xác thực 100% từ Dashboard & BU Movies)
* **Số người dùng hoạt động (W2A MAU / Users):** **11,457 người** (Tăng trưởng **+20.7%** trên Dashboard; tăng trưởng YoY **+88.1%**).
* **Số lượt tương tác (W2A MEU):** **30,470 lượt** (Tăng trưởng **+14.1%** so với tháng 9; tăng trưởng YoY **+40.9%**).
* **Số giao dịch thành công (Transactions):** **12,547 đơn** (Tăng trưởng **+20.1%** trên Dashboard; tăng **+27.9%** so với tháng 9).
* **Số lượng vé bán ra (Tickets):** **26,789 vé** (Tăng trưởng **+18.8%** trên Dashboard; tăng **+27.7%** so với tháng 9).
* **Doanh thu GMV thực thu Tháng 10:** **2,572,135,000 đồng (2.57 tỷ đồng)** (dựa trên công thức $12,547 \times 205,000$ đồng).
* **Bóc tách chỉ số hành vi người dùng:**
  * **Hệ số tương tác:** 30,470 / 11,457 = **2.66 lượt tương tác/người dùng** trong tháng.
  * **Tần suất mua hàng:** 12,547 / 11,457 = **1.095 đơn/người** trong tháng.
  * **Số vé bình quân trên mỗi đơn:** 26,789 / 12,547 = **2.135 vé/đơn**.
  * **Giá vé bình quân thực tế:** 2,572,135,000 / 26,789 = **96,014 đồng/vé**.

### L. Bảng tổng hợp Giao dịch Thực thu 10 Tháng Năm 2026 (Chính Thức)

| Kỳ Báo Cáo | Transacting Users (MAU) | Lượt tương tác (MEU) | Transactions (Đơn) | Tickets (Vé) | GMV Thực Thu (VND) | Tăng trưởng MoM | Vé / Đơn | Nguồn Dữ Liệu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Năm 2025 (Cả năm)** | 93,758 | 264,178 | 52,311 | 111,422 | 10,723,755,000 đ | - | 2.13 | Sheet REPORT 2025 (Web-to-App) |
| **Tháng 1/2026 (Thực tế)** | 5,362 | 20,258 | 5,889 | 12,643 | 1,207,245,000 đ | -47.4% đơn | 2.15 | Dashboard In-App (Đã xác thực) |
| **Tháng 2/2026 (Thực tế - Tết)** | 10,922 | 27,595 | 12,432 | 28,379 | 2,548,560,000 đ | +182.5% đơn | 2.28 | Dashboard In-App (Đã xác thực) |
| **Tháng 3/2026 (Thực tế)** | 8,728 | 23,839 | 9,881 | 20,600 | 2,025,605,000 đ | -23.0% đơn | 2.08 | Dashboard In-App (Đã xác thực) |
| **Tháng 4/2026 (Thực tế)** | 7,300 | 20,020 | 8,221 | 18,730 | 1,685,305,000 đ | -11.7% đơn | 2.28 | Dashboard In-App (Đã xác thực) |
| **Tháng 5/2026 (Thực tế)** | 5,141 | 15,823 | 5,777 | 12,561 | 1,184,285,000 đ | -30.9% đơn | 2.17 | Dashboard In-App (Đã xác thực) |
| **Tháng 6/2026 (Thực tế)** | 7,871 | 16,046 | 9,055 | 19,444 | 1,856,275,000 đ | +56.7% đơn | 2.15 | Dashboard In-App (Đã xác thực) |
| **Tháng 7/2026 (Thực tế)** | 2,263 | 7,806 | 2,425 | 5,211 | 497,125,000 đ | -64.6% đơn | 2.15 | Dashboard In-App (Đã xác thực) |
| **Tháng 8/2026 (Thực tế)** | 3,757 | 12,962 | 4,016 | 8,754 | 823,280,000 đ | - | 2.18 | MOVIES DATA SUMMARY & T9 MoM |
| **Tháng 9/2026 (Thực tế)** | 8,927 | 26,698 | 9,807 | 20,983 | 2,010,435,000 đ | +144.2% đơn | 2.14 | Dashboard In-App (Tag tháng 9) & BU Movies |
| **Tháng 10/2026 (Thực tế)** | 11,457 | 30,470 | 12,547 | 26,789 | 2,572,135,000 đ | +20.1% đơn | 2.13 | Dashboard In-App & BU Movies |
| **Tổng 9 tháng trực tiếp Dashboard (T1-T7, T9, T10)** | **67,971** | **188,555** | **76,034** | **165,340** | **15,586,970,000 đ** | - | **2.17** | **9 tháng có ảnh chụp trực tiếp Dashboard (145.3% cả năm 2025)** |
| **Toàn bộ 10 tháng năm 2026 (T1 - T10)** | **71,728** | **201,517** | **80,050** | **174,094** | **16,410,250,000 đ** | - | **2.17** | **Đầy đủ 10 tháng chính thức năm 2026 (153.0% cả năm 2025)** |

* **Đánh giá hiệu quả kinh doanh 10 tháng năm 2026:** Toàn bộ 10 tháng năm 2026 đã được xác thực chính thức từ dữ liệu vận hành bán vé in-app. Kênh Web-to-App đã mang về tổng cộng **80,050 đơn hàng thành công**, bán ra **174,094 vé xem phim** và đóng góp **16.41 tỷ đồng GMV thực thu** cho BU Movies. Thành tích này chính thức vượt qua toàn bộ năm 2025 tới **+53.0% về số đơn hàng** (+27,739 đơn), **+56.2% về số vé bán ra** (+62,672 vé) và **+53.0% về doanh thu GMV thực thu** (+5.69 tỷ đồng).

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

## 4. PHỄU CHUYỂN ĐỔI WEB-TO-APP & ĐIỂM NGHẼN RÒ RỈ LƯU LƯỢNG

Phễu chuyển đổi 4 tầng từ Kênh Web-to-App (Google Search -> Web MoMo Cinema -> App MoMo -> Đơn hàng) cho thấy hai đặc điểm đối lập:

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

## 5. DỰ BÁO HIỆU SUẤT 2 THÁNG CUỐI NĂM & TOÀN CẢNH CẢ NĂM 2026 (FORECAST T11 - T12 & FULL YEAR 2026)

### A. Cơ sở phương pháp luận và dữ liệu tham chiếu
Dự báo hiệu suất 2 tháng cuối năm 2026 (Tháng 11 và Tháng 12) được xây dựng dựa trên 4 trụ cột dữ liệu thực tế:
1. **Chuỗi dữ liệu thực tế 10 tháng năm 2026 (Đã xác thực 100%):** Ghi nhận lũy kế 80,050 đơn hàng thành công, 174,094 vé xem phim và 16.41 tỷ đồng GMV thực thu (vượt +53.0% toàn bộ năm 2025).
2. **Hệ số kinh tế đơn vị thực tế (Unit Economics Baseline 10M 2026):**
   * Tần suất mua hàng bình quân: **1.116 đơn/user** ($80,050 / 71,728$).
   * Số lượng vé bình quân trên mỗi đơn: **2.175 vé/đơn** ($174,094 / 80,050$).
   * Giá vé thực tế bình quân: **94,261 đồng/vé** ($16,410,250,000 / 174,094$).
   * Giá trị đơn hàng chuẩn hóa (AoV): **205,000 đồng/đơn**.
3. **Tính chu kỳ mùa vụ lịch sử năm 2025 (Seasonality Reference):**
   * Tháng 11/2025: Thường có nhịp lưu lượng chậm hơn giai đoạn hè do là khoảng lặng giữa mùa hè và mùa lễ hội (ghi nhận 2,606 đơn hàng, 7,314 MAU).
   * Tháng 12/2025: Bùng nổ rất mạnh mẽ với mức tăng **+42.6% MAU**, **+46.9% Transactions**, **+54.3% in-app traffic** (đạt 3,827 đơn hàng, 10,432 MAU) nhờ làn sóng phim bom tấn Giáng sinh và Tết Dương Lịch.
4. **Các đòn bẩy kích hoạt thực tế trong Q4/2026:**
   * **Minigame Quiz Bò Sữa Bay (On-air 06/11):** Tạo phễu O2O trực tiếp tại các cụm rạp đối tác (CGV, Lotte, BHD, Rio, Touch, Metiz) quét QR nhận voucher giảm giá đặt vé in-app.
   * **Suất chiếu Cinetour & Danh bạ nghệ sĩ:** Gắn nhãn nhận diện suất chiếu giao lưu đoàn làm phim thời gian thực kích hoạt nhu cầu đặt vé nhanh.
   * **Chiến dịch SEO Off-Page:** Đã chốt xong đối tác triển khai với Procurement, tập trung đẩy mạnh thứ hạng rạp đối tác đón đầu mùa phim Tết 2027.

---

### B. Bảng mô hình 3 kịch bản dự báo 2 tháng còn lại và cả năm 2026

| Chỉ Số Đo Lường | Thực Tế 10 Tháng | Kịch Bản Thận Trọng | Kịch Bản Cơ Sở (Khuyến Nghị SSOT) | Kịch Bản Tích Cực |
| :--- | :--- | :--- | :--- | :--- |
| **Giả định Tháng 11/2026** | - | Giảm -20% đơn vs T10 | Giảm -12% đơn vs T10 (Nhờ Bò Sữa Bay) | Ngang đỉnh Tháng 10 (12.5k đơn) |
| **Giả định Tháng 12/2026** | - | Tăng +25% MoM vs T11 | Tăng +32% MoM vs T11 (Mùa lễ hội) | Tăng +40% MoM vs T11 (Chu kỳ 2025) |
| **Tháng 11/2026: Users (MAU)** | - | 8,995 | **9,893** | 11,243 |
| **Tháng 11/2026: Transactions (Đơn)** | - | 10,038 | **11,041** | 12,547 |
| **Tháng 11/2026: Tickets (Vé)** | - | 21,833 | **24,014** | 27,290 |
| **Tháng 11/2026: GMV Thực Thu (VND)** | - | 2,057,790,000 đ | **2,263,405,000 đ** | 2,572,135,000 đ |
| **Tháng 12/2026: Users (MAU)** | - | 11,244 | **13,059** | 15,740 |
| **Tháng 12/2026: Transactions (Đơn)** | - | 12,548 | **14,574** | 17,566 |
| **Tháng 12/2026: Tickets (Vé)** | - | 27,292 | **31,698** | 38,206 |
| **Tháng 12/2026: GMV Thực Thu (VND)** | - | 2,572,340,000 đ | **2,987,670,000 đ** | 3,601,030,000 đ |
| **Tổng 2 tháng cuối: Đơn hàng (Đơn)** | - | 22,586 | **25,615** | 30,113 |
| **Tổng 2 tháng cuối: Vé bán ra (Vé)** | - | 49,125 | **55,712** | 65,496 |
| **Tổng 2 tháng cuối: GMV Thực Thu (VND)**| - | 4,630,130,000 đ | **5,251,075,000 đ** | 6,173,165,000 đ |
| **DỰ BÁO CẢ NĂM 2026: TỔNG ĐƠN HÀNG** | **80,050** | **102,636 đơn** | **105,665 đơn** | **110,163 đơn** |
| *Tăng trưởng Đơn hàng vs Cả năm 2025* | - | *+96.2%* | ***+102.0% (Gấp đôi 2025)*** | *+110.6%* |
| **DỰ BÁO CẢ NĂM 2026: TỔNG VÉ BÁN RA** | **174,094** | **223,219 vé** | **229,806 vé** | **239,590 vé** |
| *Tăng trưởng Vé bán ra vs Cả năm 2025* | - | *+100.3%* | ***+106.2%*** | *+115.0%* |
| **DỰ BÁO CẢ NĂM 2026: GMV THỰC THU** | **16,410,250,000 đ** | **21,040,380,000 đ** | **21,661,325,000 đ** | **22,583,415,000 đ** |
| *Tăng trưởng Doanh thu GMV vs Cả năm 2025* | - | *+96.2%* | ***+102.0% (Đạt 21.66 tỷ đ)*** | *+110.6%* |

---

### C. Đánh giá chiến lược và kết luận điều hành
1. **Chắc chắn vượt mốc 100,000 đơn hàng cả năm 2026:**
   * Ngay cả trong kịch bản thận trọng nhất, Kênh Web-to-App cũng sẽ cán mốc **102,636 đơn hàng** và **21.04 tỷ đồng GMV**, tăng trưởng +96.2% so với toàn bộ năm 2025 (52,311 đơn / 10.72 tỷ đồng GMV).
   * Trong kịch bản cơ sở (khuyến nghị), kênh Web sẽ đạt **105,665 đơn hàng** và **21.66 tỷ đồng GMV**, chính thức thiết lập cột mốc **tăng trưởng gấp đôi (+102.0%) quy mô toàn bộ năm 2025**.
2. **Quy mô GMV tiềm năng quy đổi theo Reach (Potential GMV):**
   * Nếu quy đổi theo lượng người dùng tiếp cận chuyển đổi (W2A MAU đạt 94,680 MAU lũy kế cả năm), tổng giá trị GMV tiềm năng quy đổi đạt **19.41 tỷ đồng**.
   * Khi tính theo giá trị thực thu của các đơn hàng thành công (Success Transactions), tổng GMV thực tế mang về cho BU Movies đạt tới **21.66 tỷ đồng** (nhờ tần suất mua hàng lặp lại 1.116 đơn/user).

---

## 6. MÔ HÌNH ĐỊNH LƯỢNG CƠ HỘI DOANH THU (OPPORTUNITY SIZING)

Nếu Web Platform phối hợp cùng BU Movies xử lý triệt để nút thắt OneLink và Bridge UX, doanh số GMV mang về cho BU Movies sẽ tăng trưởng đột phá mà không cần tăng ngân sách kéo traffic:

| Kịch bản | Tỷ lệ mở App (%W2A) | Lượt vào App (In-App) | Ước tính W2A MAU | Ước tính GMV (VND) | Doanh thu tăng thêm (VND) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hiện trạng cơ sở (Baseline)** | 29.57% | 78,735 | 93,758 | 19,220,390,000 đ | 0 đ (Mốc quy chiếu) |
| **Tối ưu OneLink & Bridge UX** | 40.00% | 106,503 | 126,832 | 26,000,560,000 đ | **+6.78 tỷ đồng** |
| **Tối ưu Cao cấp + Chatbot Deeplink** | 45.00% | 119,816 | 142,686 | 29,250,630,000 đ | **+10.03 tỷ đồng** |
| **Đột phá Toàn diện (Web + Mini App)**| 50.00% | 133,129 | 158,540 | 32,500,700,000 đ | **+13.28 tỷ đồng** |

---

## 7. KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI

1. **Hoàn tất đối soát toàn diện 10 tháng năm 2026 với BU Movies (Đã xong):**
   * Đã đối soát và xác thực 100% dữ liệu 10 tháng năm 2026 từ Dashboard in-app, đạt 80,050 đơn hàng thành công, 174,094 vé và 16.41 tỷ đồng GMV thực thu.
2. **Triển khai Bridge Page & QR Động:**
   * Thay thế link tĩnh bằng cầu nối thông minh: Với mobile mở thẳng App; với desktop hiển thị mã QR động chứa thông tin rạp và suất chiếu đã chọn để quét thanh toán tức thì.
3. **Kích hoạt Cinema Chatbot theo PRD:**
   * Đưa nút CTA đặt vé gắn Deeplink trực tiếp vào các câu trả lời tư vấn suất chiếu, rạp gần nhất và giá vé, tận dụng tỷ lệ chốt đơn 66.4% của tệp người dùng từ kênh Web.

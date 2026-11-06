import os

path = '07_REPORTS/docs/weekly-report-2026-10-26-11-01.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

s1_marker = '## I. TỔNG QUAN HIỆU SUẤT THÁNG 10/2026'
s2_marker = '## II. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN CHIẾN LƯỢC (USE CASES)'

p1 = text.find(s1_marker)
p2 = text.find(s2_marker)
assert p1 != -1 and p2 != -1, 'Markers not found'

new_s1 = """## I. TỔNG QUAN HIỆU SUẤT THÁNG 10/2026

### 1. Tóm Tắt Điểm Đáng Chú Ý Nhất Tháng 10
> **Lượng truy cập tự nhiên (Non-Paid) tăng +13.5% so với tháng trước (đạt 3.13 triệu view, chiếm 86.9% toàn web), bù lại được 52% lượng view bị hụt do chủ động cắt giảm 60.4% tiền chạy quảng cáo (Ads).** Đồng thời, số người cài app và liên kết ngân hàng thành công đạt mức cao nhất từ trước đến nay với **2.389 người (Map Bank, tăng +5% MoM)**, cho thấy người dùng vào web vì có nhu cầu dùng tiện ích thực tế hàng ngày.

### 2. Chi Tiết Diễn Biến Số Liệu Tháng 10

#### a. Traffic tự nhiên tăng đều giúp bù đắp phần cắt giảm quảng cáo
- **Lượng view tự nhiên tăng tốt:** Kênh tự nhiên (Non-Paid) đạt **3.128.542 view** (tăng thêm +372.776 view so với tháng 9). Trong đó, người tìm kiếm trên Google (SEO) đóng góp gần một nửa (**1.715.771 view**, +5.7%); lượng người vào trực tiếp (Direct) tăng mạnh (**931.731 view**, +23.3%) do quen dùng các trang tiện ích.
- **Chủ động cắt giảm quảng cáo kém hiệu quả:** View từ quảng cáo giảm từ 1.197.093 view xuống còn **473.481 view (-60.4%)** để tiết kiệm chi phí, toàn sàn vẫn đạt **3.602.023 view (đạt 98.3% kế hoạch tháng)**.

| Kênh Truy Cập / Chỉ Số | Tháng 9 (Full) | Kế Hoạch T10 | Thực Đạt T10 | % Đạt Kế Hoạch | So Với Tháng 9 | Đánh Giá Tình Hình |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **TỔNG LƯỢNG TRUY CẬP (PAGEVIEWS)** | **3.952.859** | **3.665.607** | **3.602.023** | **98.3%** | **-8.9%** | Thiếu 63K view so với kế hoạch (chủ yếu do cắt quảng cáo) |
| **Kênh Tự Nhiên (Non-Paid)** | **2.755.766** | 3.176.343* | **3.128.542** | **98.5%*** | **+13.5%** | Tăng thêm 372K view, bù được 52% lượng hụt từ quảng cáo |
| - Tìm kiếm Google (Organic Search) | 1.623.796 | - | 1.715.771 | - | +5.7% | Kênh kéo traffic chính của toàn trang web |
| - Vào trực tiếp (Direct) | 755.896 | - | 931.731 | - | +23.3% | Người dùng vào thẳng xem: Lịch chiếu phim, Phạt nguội, Giá xăng, Tỷ giá |
| - Nguồn giới thiệu & đối tác (Referral) | 376.074 | - | 481.040 | - | +27.9% | Tăng từ các trang đối tác và liên kết ngoài |
| *- Trong đó: Nguồn từ AI (ChatGPT, Perplexity)* | *13.596* | *-* | *18.547* | *-* | **+36.4%** | ChatGPT chiếm 17.739 view (95.6%), Perplexity 284 view |
| **Kênh Trả Phí (Paid Ads)** | **1.197.093** | 489.264 | **473.481** | **96.8%** | **-60.4%** | Dừng các chiến dịch quảng cáo tốn kém, kém hiệu quả |

#### b. Các trang công cụ tiện ích kéo traffic tốt cho các Hub
- **Cinema Hub (1.132.721 view, vượt 101.4% kế hoạch):** Lượng truy cập tự nhiên tăng +21.7% giúp hub vẫn vượt chỉ tiêu dù đã cắt 98% quảng cáo phim lẻ; cụm trang rạp đối tác (Rio, Touch, Metiz) tăng mạnh +46.5% (+233K view).
- **Financial Hub (254.077 view, +1.7% so với tháng 9):** Nhóm trang Trung tâm Tài chính tăng vọt **+373.7%** (nhờ đưa 7 trang Tỷ Giá mới lên Top Google) và Ví Trả Sau tăng **+41.2%**, bù lại lượng giảm của Vay Nhanh khi dừng chạy ads.
- **Vehicle Hub (61.969 view):** Nhóm tiện ích giao thông tăng mạnh **+908.9%** (11.895 view) nhờ trang tra cứu Giá xăng và thông tin xe, giúp giữ nhịp khi trang Phạt nguội hạ nhiệt theo mùa vụ.

#### c. Phễu chuyển đổi từ Web sang cài App và liên kết ngân hàng
- **Kết quả cả tháng 10 (theo AppsFlyer):** Toàn sàn ghi nhận **11.143 lượt cài app** ➔ **3.902 người đăng ký tài khoản (35%)** ➔ **2.389 người liên kết ngân hàng (Map Bank - tăng +5% MoM, cao nhất từ trước đến nay)** ➔ **1.284 người dùng tích cực (MAU)**.
- **Nguồn người dùng & Điểm rơi rụng:** Lượng cài đặt hiện tại chủ yếu đến từ các landing page quảng cáo tài chính (Điểm Tín Dụng, Quýt kéo về 36.950 lượt bấm OneLink mở app), chưa phải từ trang tải app tự nhiên (`/tai-app` mới đưa lên Production ngày 30/10). Điểm rơi rụng lớn nhất là **65% người đã cài app từ quảng cáo nhưng chưa hoàn tất đăng ký tài khoản**.

### 3. Tình Hình Người Dùng Vào Từ Các Công Cụ AI (GEO)

| Công Cụ AI (sessionSource GA4) | Tháng 9 | Tháng 10 | Tăng/Giảm | % So Tháng 9 | Tỷ Trọng (%) | Nhận Xét Thực Tế |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **ChatGPT (chatgpt.com)** | 12.589 | 17.739 | **+5.150** | **+40.9%** | **95.6%** | Nguồn chính dẫn khách về web khi hỏi về tài chính và phim rạp |
| **Google Gemini (gemini.google.com)** | 704 | 467 | **-237** | **-33.7%** | **2.5%** | Giảm do Gemini trả lời sẵn nội dung ngay trên trang tìm kiếm |
| **Perplexity (perplexity.ai)** | 239 | 284 | **+45** | **+18.8%** | **1.5%** | Tăng nhẹ từ nhóm người dùng tra cứu thông tin chuyên sâu |
| **Khác (Claude, Copilot, Meta AI)** | 64 | 57 | **-7** | **-10.9%** | **0.4%** | Số lượng nhỏ, không đáng kể |
| **TỔNG VIEW TỪ AI** | **13.596** | **18.547** | **+4.951** | **+36.4%** | **100.0%** | Chiếm **0.5%** toàn web; khách xem trung bình 1.6 trang mỗi lượt |

- **4 nhóm nội dung được AI dẫn link về nhiều nhất:**
  1. *Tài chính (Vay Nhanh, Ví Trả Sau, Mở Thẻ):* Chiếm 17.3% lượt vào (trang [momo.vn/vay-nhanh](https://www.momo.vn/vay-nhanh) 757 phiên, [momo.vn/vi-tra-sau](https://www.momo.vn/vi-tra-sau) 155 phiên).
  2. *Hỏi đáp (FAQ):* Chiếm 14.1% lượt vào (trang [momo.vn/hoi-dap](https://www.momo.vn/hoi-dap) 517 phiên).
  3. *Trang chủ & Doanh nghiệp:* Chiếm 11.4% lượt vào (Trang chủ [momo.vn](https://www.momo.vn) 667 phiên, [momo.vn/merchant](https://www.momo.vn/merchant) 279 phiên).
  4. *Rạp phim (Cinema):* Chiếm 10.3% lượt vào (tăng từ 460 lên 1.210 phiên, chủ yếu từ cụm rạp CGV và các phim mới).

---

"""

clean_text = text[:p1] + new_s1 + text[p2:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(clean_text)

print('Rewritten Section I in simple, natural Vietnamese successfully!')

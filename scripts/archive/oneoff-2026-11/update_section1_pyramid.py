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

### 1. Thông Điệp Trọng Tâm (Executive Takeaway)
> **Lưu lượng tự nhiên (Non-Paid) bứt phá +13.5% MoM (đạt 3.13 triệu PV, chiếm 86.9% toàn sàn), bù đắp trọn vẹn 52% lượng hụt khi chủ động cắt giảm 60.4% ngân sách Ads.** Chuyển đổi Web-to-App lập đỉnh mới với **2.389 người liên kết ngân hàng (Map Bank, +5% MoM)**, chứng minh mô hình tăng trưởng bền vững dựa trên công cụ tiện ích (Utilities-Led Growth).

### 2. Ba Trụ Cột Luận Cứ & Bằng Chứng Số Liệu (Supporting Pillars)

#### a. Trụ Cột 1: Động Cơ Tự Nhiên Tăng Trưởng Bền Vững Bù Đắp Cắt Giảm Ads
- **Cơ cấu kênh chuyển dịch lành mạnh:** Non-Paid đạt **3.128.542 PV** (tăng thêm +372.776 PV, đạt 98.5% target tự nhiên). Trong đó, Tìm kiếm tự nhiên (SEO) đóng góp gần một nửa (**1.715.771 PV**, +5.7% MoM); Truy cập trực tiếp (Direct) bứt phá mạnh (**931.731 PV**, +23.3% MoM) nhờ thói quen vào thẳng các công cụ tiện ích.
- **Paid Ads được cắt giảm có chọn lọc:** Lưu lượng trả phí giảm từ 1.197.093 PV xuống còn **473.481 PV (-60.4% MoM)** do dừng các chiến dịch quảng cáo kém hiệu quả, giúp tiết kiệm chi phí mà toàn sàn vẫn đạt **3.602.023 PV (98.3% target)**.

| Kênh Lưu Lượng / Chỉ Số | T9/2026 (Full) | T10/2026 (Target) | T10/2026 (Thực Đạt) | % Đạt Target | % MoM vs. T9 | Đánh Giá Vận Hành |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **TỔNG LƯU LƯỢNG (PAGEVIEWS)** | **3.952.859** | **3.665.607** | **3.602.023** | **98.3%** | **-8.9%** | Thiếu 63.584 PV so với kế hoạch (chủ yếu do chủ động cắt Ads) |
| **Kênh Tự Nhiên (Non-Paid)** | **2.755.766** | 3.176.343* | **3.128.542** | **98.5%*** | **+13.5%** | Tăng ròng +372.776 PV, bù đắp 52% lượng giảm từ Ads |
| - Tìm kiếm tự nhiên (Organic Search) | 1.623.796 | - | 1.715.771 | - | +5.7% | Giữ vững vị thế kênh kéo traffic chủ lực toàn sàn |
| - Truy cập trực tiếp (Direct) | 755.896 | - | 931.731 | - | +23.3% | Khách vào thẳng các tiện ích: Lịch phim, Phạt nguội, Giá xăng, Tỷ giá |
| - Giới thiệu & Khác (Referral / Others) | 376.074 | - | 481.040 | - | +27.9% | Tăng trưởng từ mạng lưới đối tác và backlink |
| *- Trong đó: Nguồn AI (GEO / AI Search)* | *13.596* | *-* | *18.547* | *-* | **+36.4%** | ChatGPT chiếm 17.739 PV (95.6%), Perplexity 284 PV |
| **Kênh Trả Phí (Paid Traffic)** | **1.197.093** | 489.264 | **473.481** | **96.8%** | **-60.4%** | Dừng các chiến dịch ads kém hiệu quả, tối ưu chi phí |

#### b. Trụ Cột 2: Tiện Ích Thiết Yếu (Utilities) Là Đầu Tàu Tăng Trưởng Của Các Hub
- **Cinema Hub đạt 1.132.721 PV (vượt 101.4% target):** Traffic tự nhiên tăng +21.7% giúp hub giữ vững đà tăng trưởng dù cắt giảm 98% ads phim lẻ; cụm rạp đối tác (Rio, Touch, Metiz) tăng mạnh +46.5% (+233K view).
- **Financial Hub đạt 254.077 PV (+1.7% MoM):** Nhóm trang Trung tâm Tài chính tăng vọt **+373.7%** (nhờ đưa 7 trang Tỷ Giá mới lên Top Google) và Ví Trả Sau tăng **+41.2%**, bù đắp trọn vẹn phần giảm của Vay Nhanh khi dừng ngân sách ads.
- **Vehicle Hub đạt 61.969 PV:** Tiện ích giao thông tăng trưởng đột biến **+908.9%** (11.895 PV) nhờ bảng tra cứu Giá xăng và thông tin xe, giữ nhịp cho hub khi Phạt nguội vào chu kỳ hạ nhiệt.

#### c. Trụ Cột 3: Phễu Chuyển Đổi Web-to-App Lập Đỉnh Mới & Điểm Nghẽn Kích Hoạt
- **Hiệu quả chuyển đổi người dùng mới (AppsFlyer Full Month):** Toàn sàn ghi nhận **11.143 lượt cài đặt (Install)** ➔ **3.902 đăng ký tài khoản (REG, 35%)** ➔ **2.389 liên kết ngân hàng (Map Bank - tăng +5% MoM, mức cao nhất lịch sử)** ➔ **1.284 MAU**.
- **Bản chất luồng cài đặt & Điểm rơi rụng:** Lượng Install hiện tại đa phần đến từ các chiến dịch Paid Ads (cụm trang tương tác Điểm Tín Dụng, Quýt... mang về 36.950 lượt bấm OneLink mở app), chưa phải từ trang tải app tự nhiên (`/tai-app` mới On Production ngày 30/10 để bắt đầu hứng SEO). Điểm rơi rụng lớn nhất là **65% người cài app từ luồng ads chưa hoàn tất đăng ký tài khoản (REG)**.

### 3. Phân Tích Chuyên Đề: Lưu Lượng Từ Nguồn AI (GEO - Generative Engine Optimization)

| Nền tảng AI (sessionSource GA4) | T9/2026 (Full) | T10/2026 (Full 31d) | Tăng/Giảm vs. T9 | % MoM | Tỷ trọng GEO (%) | Nhận Định & Hành Động Kỹ Thuật |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **ChatGPT (chatgpt.com)** | 12.589 | 17.739 | **+5.150** | **+40.9%** | **95.6%** | Nguồn chính dẫn người dùng về web khi hỏi về tài chính và lịch phim rạp |
| **Google Gemini (gemini.google.com)** | 704 | 467 | **-237** | **-33.7%** | **2.5%** | Giảm do Gemini trả lời trực tiếp trên kết quả tìm kiếm (Zero-click) |
| **Perplexity (perplexity.ai)** | 239 | 284 | **+45** | **+18.8%** | **1.5%** | Tăng trưởng ổn định từ tệp người dùng tra cứu thông tin chuyên sâu |
| **Khác (Claude, Copilot, Meta AI)** | 64 | 57 | **-7** | **-10.9%** | **0.4%** | Quy mô nhỏ, chiếm tỷ trọng không đáng kể |
| **TỔNG LƯU LƯỢNG GEO (AI SEARCH)** | **13.596** | **18.547** | **+4.951** | **+36.4%** | **100.0%** | Chiếm **0.5%** toàn web; khách ở lại xem trung bình 1.6 trang mỗi lượt vào |

- **Top 4 nhóm trang được các mô hình AI trích dẫn nhiều nhất:**
  1. *Tài chính (Vay Nhanh, Ví Trả Sau, Mở Thẻ):* Chiếm 17.3% lượt vào (trang [momo.vn/vay-nhanh](https://www.momo.vn/vay-nhanh) 757 phiên, [momo.vn/vi-tra-sau](https://www.momo.vn/vi-tra-sau) 155 phiên).
  2. *Hỏi đáp (FAQ):* Chiếm 14.1% lượt vào (trang [momo.vn/hoi-dap](https://www.momo.vn/hoi-dap) 517 phiên; tỷ lệ tương tác đạt 95.2%).
  3. *Trang chủ & Doanh nghiệp:* Chiếm 11.4% lượt vào (Trang chủ [momo.vn](https://www.momo.vn) 667 phiên, [momo.vn/merchant](https://www.momo.vn/merchant) 279 phiên).
  4. *Cinema Hub:* Chiếm 10.3% lượt vào (tăng từ 460 lên 1.210 phiên, chủ yếu từ cụm rạp CGV và các phim mới ra rạp).

---

"""

clean_text = text[:p1] + new_s1 + text[p2:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(clean_text)

print('Updated Section I to Pyramid Principle successfully!')

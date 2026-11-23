---
date: 2026-11-01
source: Global & VN Search Intelligence (Search Engine Land, Search Engine Roundtable, Google Search Central, Reddit r/TechSEO, r/SEO, X/Twitter)
source_url: https://searchengineland.com/
category: tech_ai_seo
hubs_impacted: Web Overview | Financial Hub | Tech AI Hub
priority: P0_Urgent
tags: [seo, geo, aeo, ai_opt_out_trap, google_goto_serp, gemini_utm_drop, attribution_direct_traffic]
---

# BÁO CÁO TỔNG HỢP TIN TỨC SEO, GEO & THUẬT TOÁN GOOGLE [01/11/2026]

---

### Tóm Tắt Bản Tin (Executive Summary)
- Thử nghiệm opt-out khỏi các tính năng AI của Google ghi nhận sự sụt giảm bất ngờ của cả các lượt nhấp tự nhiên truyền thống (The AI Opt-Out Trap); việc hiện diện trong AI Overviews tạo ra hiệu ứng củng cố uy tín thương hiệu (Brand Halo Effect), rút lui khỏi AI Search khiến thương hiệu mất thị phần click tổng thể.
- Google bắt đầu bọc từ 54,8% đến 84,7% liên kết tự nhiên sang định dạng trung gian `google.com/goto?url=<token>` tại 8 quốc gia lớn và áp dụng cơ chế bóp nghẹt giải mã (throttling), khiến hàng loạt công cụ theo dõi thứ hạng báo cáo sai lệch về việc rớt hạng diện rộng.
- Nối tiếp ChatGPT, Google Gemini chính thức loại bỏ các tham số UTM khi trích dẫn URL nguồn trong câu trả lời tổng hợp, tiếp tục đẩy lượng lớn lưu lượng AI Referral vào kênh Direct trong GA4.

---

## PHẦN 1: CÁC CẬP NHẬT MỚI NHẤT LIÊN QUAN ĐẾN SEO / GEO / AEO

### 1. Cú Sốc Sụt Giảm Click Truyền Thống Khi Opt-Out Khỏi Google AI (The AI Opt-Out Trap)
- **Nguồn & Trích dẫn:** [Search Engine Land: Google AI opt-out test finds unexpected drop in organic clicks](https://searchengineland.com/google-ai-opt-out-test-organic-clicks-drop-499898) & [Search Engine Roundtable](https://www.seroundtable.com/google-ai-mode-ads-earn-less-42417.html).
- **Chi tiết bản tin:**
  - Thử nghiệm trên website khi chủ động sử dụng các thẻ chặn AI hiển thị: Lượt hiển thị (Impressions) trên AI Overviews giảm ngay về 0, nhưng lượng click tự nhiên ở 10 liên kết xanh truyền thống bên dưới cũng sụt giảm theo.
  - **Cơ chế tâm lý:** Dù CTR trực tiếp của AI Overviews chỉ khoảng 0,9%, nhưng việc xuất hiện trong khối AI đóng vai trò như một chứng thực xã hội (Social Proof). Người dùng đọc tóm tắt AI, ghi nhận thương hiệu và sau đó cuộn xuống nhấp vào chính website đó ở kết quả tự nhiên. Khi opt-out, thương hiệu mất đi sự bảo chứng này và mất luôn click bên dưới.
  - **Khuyến nghị:** Tuyệt đối không cấu hình opt-out khỏi AI Overviews đối với các trang thông tin và sản phẩm công khai.

### 2. Google Gemini Dừng Gắn Tham Số UTM Vào Liên Kết Trích Dẫn
- **Nguồn & Trích dẫn:** [Search Engine Roundtable: Google Gemini Stopped Attaching UTM Parameters To Cited URLs](https://www.seroundtable.com/).
- **Phân tích số liệu:**
  - Sau sự cố của ChatGPT, Gemini cũng chính thức ngừng gắn UTM parameters vào các liên kết nguồn.
  - **Hệ quả GA4:** Lưu lượng thực tế từ Gemini bị gộp vào kênh Direct hoặc Unassigned. Cần xây dựng mô hình Lift Analysis đối chiếu mức tăng Direct Traffic trên các trang nhận nhiều trích dẫn AI.

---

## PHẦN 2: THUẬT TOÁN & BIẾN ĐỘNG GOOGLE SEARCH

### 1. Đợt Bọc Liên Kết `google.com/goto` Gây Xáo Trộn Dữ Liệu Rank Tracking
- **Nguồn & Phân tích:** [Reddit r/TechSEO: google.com/goto in my DataForSEO data](https://www.reddit.com/r/TechSEO/comments/1xk4ktz/googlecomgoto_in_my_dataforseo_data_0_of_71531/).
- **Bản chất vấn đề:**
  - Google bọc 54,8% đến 84,7% liên kết tự nhiên thành URL trung gian `https://google.com/goto?url=...` (trường domain trả về `"google.com"`).
  - Áp dụng cơ chế điều tiết (throttling): trễ từ 40s đến 120s đối với các công cụ quét liên tiếp.
  - Thứ hạng người dùng thực không đổi, nhưng các công cụ theo dõi đối soát qua URL bị lỗi và báo cáo rớt hạng ảo.
  - **Giải pháp:** Trong 94,9% trường hợp, tên miền thực tế vẫn hiển thị nguyên vẹn ở trường `breadcrumb` trong cấu trúc DOM.

---

## PHẦN 3: CÁC KỸ THUẬT, TACTICS, TRICKS & TIPS THỰC CHIẾN (SEO / GEO / AEO)

### 1. Giữ Vững Hiện Diện AI Để Kích Hoạt Brand Halo Effect
- Không đặt các thẻ `nosnippet`, `max-snippet:0` hay cấm AI crawler trên các landing page chủ lực. Tận dụng AI Overviews làm phễu lọc intent và tăng nhận diện thương hiệu để thu hút click tự nhiên ở danh sách liên kết bên dưới.

### 2. Hiệu Chỉnh Logic Trích Xuất SERP API Nội Bộ
- Cập nhật bộ parser dữ liệu API (DataForSEO, Serper): đọc giá trị tên miền từ trường `breadcrumb` thay vì đọc trường `url` hoặc `domain` để khử lỗi rớt hạng ảo do `google.com/goto`.

---

## PHẦN 4: ĐỀ XUẤT HÀNH ĐỘNG CHO WEB PLATFORM (ACTIONABLE CHECKLIST)

1. **Duy trì chính sách mở cho AI Search:** Không cấu hình opt-out khỏi AI Overviews nhằm bảo vệ lưu lượng click tự nhiên tổng thể.
2. **Cập nhật hệ thống rank tracker nội bộ:** Trích xuất domain từ trường breadcrumb trong SERP API.
3. **Mô hình hóa đo lường Direct Traffic:** Phân tích độ tăng tương quan của lưu lượng Direct trên các trang nhận trích dẫn AI để bù trừ việc mất UTM từ Gemini và ChatGPT.
4. **Đối soát Search Console:** Lấy Google Search Console làm nguồn dữ liệu chuẩn duy nhất khi đánh giá thứ hạng.

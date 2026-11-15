---
name: web-platform-reporting
description: Quy chuẩn và công cụ tạo báo cáo định kỳ (Weekly cho anh Công, Monthly cho anh Tường) cho các dự án Web Platform. Áp dụng quy chuẩn trình bày cấp công ty tại 03_SKILLS/momo-reporting-guidelines.md, cộng phần đặc thù Web Platform về cấu trúc khối, thuật ngữ và định vị kênh.
---

# WEB PLATFORM REPORTING SKILL

## 1. MỤC TIÊU & ĐỊNH VỊ SKILL

Skill này cung cấp bộ khung chuẩn hóa, phương pháp luận bóc tách số liệu, công thức hành văn (copywriting/texting) và các biểu mẫu báo cáo chuẩn cho **Web Platform**:
- **Báo cáo Tuần (Weekly Report) gửi Executive Leadership (anh Công):** Tập trung vào tiến độ thực thi 7 ngày, hiệu quả vận hành tự phục vụ (Self-service), tháo gỡ điểm nghẽn kỹ thuật và A/B testing.
- **Báo cáo Tháng (Monthly Report) gửi Ban Giám Đốc / Board (anh Tường, anh Công):** Tập trung vào sức khỏe động cơ tăng trưởng (Growth Engine Health), phân tích Cohort (M0-M11), phân bổ 5 dự án chiến lược theo Khung 4 Zone và mục tiêu Web Destination (4M-5M-6M).

---

## 2. QUY TẮC BẮT BUỘC TUÂN THỦ (NON-NEGOTIABLES)

**Quy chuẩn gốc:** Trước khi dựng bất kỳ báo cáo nào, đọc [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md). Đó là quy chuẩn cấp công ty, hiệu lực cao hơn skill này. Các quy tắc dưới đây là phần đặc thù của Web Platform, đặt trên nền quy chuẩn đó.

0. **Sáu nguyên tắc của guidelines áp dụng cho mọi slide:** dòng `Mục đích` đầu slide; action title viết sentence case; tối đa 3 ý chính; tag `[R]`/`[D]`/`[F]`; mỗi số liệu có so sánh và việc tiếp theo; Discussion Topics đứng đầu deck.
1. **Tuyệt đối không sử dụng Emoji / Icon** trong tiêu đề, bảng biểu và danh sách của bài báo cáo.
2. **Quy tắc thuật ngữ (Terminology Rule):** TUYỆT ĐỐI KHÔNG dùng từ "sàn Web". Bắt buộc chỉ sử dụng **"nền tảng Web"**, **"Kênh Web"**, **"Web Platform"** hoặc **"Web"**.
3. **Không đề cập tên riêng cá nhân / PIC** (như Hiến, Bảo, Trọng, Thuận...). Bắt buộc thay thế bằng tên đội ngũ chuyên môn (`Web Dev`, `Backend Team`, `Content Team`, `SEO Vendor`, `Media Team`, `Risk Team`, `AI/ML Team`, `CX Team`, `BU Movies`, `VTTI BU`, `FS Team`...).
4. **Agenda Báo Cáo Tháng (Monthly Business Review Agenda):** Thứ tự chuẩn cho Web Platform, Discussion Topics đứng đầu:
   - `[D]` **Discussion Topics:** Bảng tổng một dòng mỗi chủ đề (3-5 chủ đề), kèm slide deep-dive riêng cho từng chủ đề theo cấu trúc Problem Statement -> Bối cảnh -> Tác động -> Phương án -> Đề nghị với BOM -> Nếu không quyết định.
   - `[R]` **Follow-up:** Bảng action từ meeting minutes kỳ trước (Action | Owner | Hạn | Trạng thái | Cập nhật). Bắt buộc có.
   - `[R]` **Executive Summary:** Hai khối `Điểm nổi bật` và `Vấn đề cần cải thiện`. Khối thứ hai bắt buộc có nội dung.
   - `[R]` **Product & Business Performance:** Bảng Target vs. Actual chuẩn 6 dòng chỉ số; áp dụng nguyên tắc "So What?" (tuyệt đối không đọc lại số liệu, chỉ tập trung phân tích bản chất dịch chuyển, nguyên nhân gốc rễ và định hướng hành động).
   - `[R]` **Key Projects (Cinema / Financial Hub):** Chi tiết hiệu suất 2 dự án trọng điểm, điểm nổi bật, việc trọng tâm tháng tới, việc cần hỗ trợ.
   - `[R]` **New User:** Mô tả luồng Ads (Paid Search, Ads Campaigns) và phễu Web-to-App (Installs, New Reg, Mapbank, MAU theo AppsFlyer GPD).
5. **Quy tắc gắn nhãn slide (Tagging):** Mọi slide/mục bắt buộc gắn mã `[R]` (Reporting - pre-read), `[D]` (Discussion - trọng tâm cuộc họp) hoặc `[F]` (FYI - tham khảo, không thảo luận).
6. **Quy định nội dung:** 
   - Tuyệt đối không đưa CX, không đưa CWV/P90, không đưa Ticket tồn đọng. Không tính New User vào nhóm Hubs. 
   - Tuyệt đối không liệt kê lại các con số đã có trên bảng.
   - **Định vị kênh:** Organic là kênh chủ lực của Web Platform. Tuyệt đối không tô điểm cho Paid. Paid tăng mà Organic giảm là cảnh báo rủi ro về chất lượng tăng trưởng.
   - **Phân loại Traffic Source (Non-Paid vs Paid):** BẮT BUỘC cơ cấu thành 2 nhóm lớn rõ rệt: **Kênh Tự Nhiên (Non-Paid)** chỉ gồm đúng 4 kênh con (Organic, Direct, AI Traffic (GEO), Referral) và **Kênh Trả Phí (Paid Ads)**. Khi trình bày bảng hoặc danh sách, gom rõ 2 dòng lớn Non-Paid vs Paid, 4 kênh con đặt thụt dòng dưới Non-Paid, tuyệt đối không tách thêm dòng Others rời rạc và không để Paid xen kẽ ngang hàng.
   - **Chỉ số lưu lượng chuẩn (PageViews):** Bắt buộc dùng `PageViews`, tuyệt đối không dùng từ `lượt xem` trong báo cáo, bảng biểu hoặc phân tích số liệu.
   - **Thuật ngữ kiểm tra chất lượng (Quality Assurance):** Bắt buộc dùng `Nghiệm thu kỹ thuật`, `Đánh giá chất lượng`, `UAT`, hoặc giữ nguyên thuật ngữ quốc tế `test`, `test cases`. Tuyệt đối không dùng cách dịch trường phái cũ (k.i.e.m t.h.u) trong báo cáo C-Suite.
   - **Gói quà người dùng mới:** Bắt buộc dùng `Gói Quà tự chọn cho người dùng mới` hoặc `Gói quà CHAOMOMO`. Tuyệt đối không dùng từ lóng game (q.u.a t.a.n t.h.u).
   - **Quy chuẩn ký tự & ưu tiên:** Tuyệt đối không dùng ký tự En Dash (mã U+2013) hoặc Em Dash (mã U+2014) (chỉ dùng Hyphen -); tuyệt đối không gắn nhãn mức độ ưu tiên (như chữ P kèm số từ 0 đến 3).
   - **Bullet Lead-ins:** Viết tiếng Việt ngắn gọn (`Vượt target:`, `Lưu lượng trực tiếp & sức mạnh thương hiệu:`, `Chuyển dịch SEO sang GEO:`, `Điểm nổi bật:`, `Việc tiếp theo:`). Chỉ giữ tiếng Anh cho thuật ngữ chỉ số: Target, Budget, Actual, MAU, MEU, CVR, Map Bank, OneLink, Installs, New Reg, PageViews. Toàn bộ báo cáo dùng một ngôn ngữ.
7. **Mật độ thông điệp & bảng biểu:** Tối đa 3 ý chính dưới mỗi tiêu đề, tốt nhất 1-2. Nhiều hơn thì tách slide. Tối đa 2-3 bảng/biểu đồ, không copy dashboard thô.
8. **Trực quan hóa:**
   - Luồng người dùng / Conversion Funnel: Dùng sơ đồ Mermaid (`graph TD` hoặc `graph LR`) + Bảng phân tích chi tiết các bước (Step Breakdown Table).
   - Lộ trình: Dùng Bảng Markdown (`Table`).

---

## 3. TIÊU CHUẨN BÁO CÁO TUẦN ĐIỀU HÀNH WEB PLATFORM (INSURTECH WEEKLY ARCHITECTURE)

Áp dụng nguyên mẫu kiến trúc từ `[InsurTech] Web 2026 Performance.pptx` kết hợp cẩm nang `03_SKILLS/executive-presentation-playbook.md` và các bài học chuẩn hóa thực tế (đúc kết từ Báo Cáo Tuần 46) cho toàn bộ Báo cáo Tuần (Weekly Report) gửi Executive Leadership (anh Công):

### 3.1. Cấu trúc Mục I: Tổng Quan Hiệu Suất Tuần
1. **Bốn chỉ số trọng tâm duy nhất (Section I.1 Overview):** Giới hạn đúng 4 đầu dòng then chốt, không đưa số liệu phân mảng lạc hậu hoặc số liệu suy đoán:
   - **Tổng lưu lượng so với mục tiêu (Total PageViews vs. Target):** Số PageViews MTD, % hoàn thành kế hoạch tháng, nhịp bình quân ngày (PageViews/ngày), tốc độ 7 ngày gần nhất (+/- % WoW) và nhịp cần thiết để về đích.
   - **Lưu lượng tự nhiên (Non-Paid Traffic):** Số PageViews và tỷ trọng % toàn Website, bóc tách Organic Search và Direct Traffic.
   - **Tìm kiếm AI (AI Traffic / GEO):** Số PageViews từ ChatGPT, Perplexity, Gemini; nhịp ngày và đánh giá tối ưu hóa Schema/GEO.
   - **Phễu chuyển đổi Web-to-App trọn vẹn (Install -> MAU):** Số lượng 4 tầng phễu AppsFlyer (Installs -> New Reg -> Map Bank -> Active MAU) và tỷ lệ chuyển đổi cuối phễu (End-to-End CVR).
2. **Cơ cấu kênh lưu lượng qua các tháng (Section I.2 Multi-Month Traffic Sources):** Bảng so sánh 5 tháng liên tiếp phân định rõ Non-Paid (4 kênh con) vs Paid Ads.
3. **Tiến độ mục tiêu các Hub (Section I.3 Realistic Hub Calibration):** Bảng đối soát Target tháng vs MTD Actual và % tiến độ; hiệu chỉnh mục tiêu các Hub (như Vehicle Hub, New User Hub) sát thực tế vận hành và run-rate MTD.
4. **Tiến trình chuyển đổi đa tháng (Section I.4 Historical Progression):** Bảng theo dõi số lượng và tỷ lệ chuyển đổi qua các tháng (từ Tháng 7 đến MTD hiện tại) để chứng minh chất lượng tệp người dùng và đà tăng trưởng bền vững.

### 3.2. Cấu trúc Mục II: Tiến Độ Dự Án Chiến Lược (Hubs Deep-Dive)
1. **Tiêu đề hành động THUẦN SỐ LIỆU, KHÔNG MENTION TÍNH NĂNG (Numbers-Only Action Titles):**
   - Tiêu đề mục các dự án/Hubs bắt buộc là câu kết luận trực diện gồm số liệu lưu lượng, chuyển đổi và tỷ lệ CVR.
   - **Tuyệt đối KHÔNG đưa tên tính năng, công cụ hay công nghệ vào tiêu đề** (Không ghi "Tool Tính Thuế", "Chatbot", "0-CAPTCHA", "Dynamic QR" trên heading). Tên tính năng và chi tiết kỹ thuật chỉ được trình bày trong phần thân bài.
   - Mẫu tiêu đề chuẩn:
     * `1. Cinema Hub [R]: Web mang về 348.428 PageViews, kéo về 224 lượt cài app mới và đạt tỷ lệ chuyển đổi sang MAU 12,1%`
     * `2. Financial Hub [R]: Web mang về 151.548 PageViews và kích hoạt 20.804 lượt chuyển đổi về app (Điểm Tín Dụng dẫn đầu 8.769 clicks)`
     * `3. Vehicle Hub [R]: Đạt 108.379 PageViews (54,2% target), phễu tra cứu ghi nhận 82.862 lượt tra cứu và 47.292 lượt mở app in-app`
     * `4. Dự án New User [R]: Web mang về 3.171 lượt cài app mới, tạo ra 864 tài khoản đăng ký và 533 người dùng liên kết ngân hàng`
2. **Thân bài đồng nhất chuẩn 3 khối bắt buộc (Standard 3-Block Body Structure):**
   - **`#### a. Key Highlights & Business Impact`:**
     - Phễu chuyển đổi 4 bước định lượng: Bước 1 (Traffic) -> Bước 2 (Tương tác / Tra cứu) -> Bước 3 (Chuyển tiếp W2A clicks) -> Bước 4 (Chuyển đổi App: Installs, Đăng ký, Đơn hàng, MAU).
     - Mốc kỹ thuật và sản phẩm đã nghiệm thu trên Production (tên công cụ, tính năng, số lượng trang/cụm rạp).
     - Radical Candor (Lowlights / Điểm nghẽn trung thực): Nêu thẳng điểm nghẽn, tỷ lệ rơi rớt, rủi ro cạnh tranh và nguyên nhân gốc rễ (không tô hồng).
   - **`#### b. Phối hợp liên đội ngũ (Cross-team Collaboration)`:**
     - Nêu đích danh các BU và phòng ban đối tác (`BU Movies`, `BU Financial Services`, `BU Bank`, `Khối CSGT/VTTI`, `Media Team`, `Procurement`...).
     - Nêu cụ thể ngân sách đầu tư và tiến độ phê duyệt (Ví dụ: Gói Pilot Off-Page Cinema 125 triệu VNĐ do BU Movies tài trợ; Gói Media New User 50 triệu VNĐ).
   - **`#### c. Kế hoạch hành động 7 ngày tới`:**
     - Danh sách việc cần làm cụ thể, thực thi ngay, sắp xếp theo logic tự nhiên.
     - **Tuyệt đối KHÔNG gắn nhãn mức độ ưu tiên (như chữ P kèm số từ 0 đến 3).**

### 3.3. Bảo Chứng Dữ Liệu & Nguyên Tắc Chống Hallucination (Strict Data Integrity)
1. **Dữ liệu chuyển đổi Financial Hub:** Khi trích dẫn lượt click và chuyển tiếp OneLink của Financial Hub, bắt buộc lấy từ dữ liệu kiểm toán chính thức tại `05_HUBS/financial/financial-hub-brd.md` Mục 3.6 (20.804 clicks, CIC 8.769, TTTC 4.950, VTS 3.953, Vay Nhanh 2.202, CVR 13,7%). Tuyệt đối không suy đoán hoặc nhân tỷ lệ từ các công cụ khác.
2. **Ưu tiên kỹ thuật Financial Hub:** Luôn có hạng mục phối hợp cùng BU Bank nghiệm thu kỹ thuật (UAT) 15 trang chi tiết ngân hàng.
3. **Dự án New User:** Luôn bóc tách so sánh `/tai-app` vs `/download`, tỷ lệ quét Dynamic QR trên Desktop, tối ưu từ khóa tải APK, và kế hoạch triển khai "Gói Quà tự chọn cho người dùng mới" với ngân sách 50 triệu VNĐ.

### 3.4. Cấu trúc Mục III: Bảng Kết Luận & Kế Hoạch Toàn Kênh (Action Matrix)
Thay thế danh sách gạch đầu dòng bằng Bảng 3 cột quan hệ nhân quả khép kín:
**BÀI HỌC (Insight thực tế) | BẰNG CHỨNG (Data Proof đối soát sạch) | KẾ HOẠCH HÀNH ĐỘNG 7 NGÀY TỚI**.
Cuối báo cáo có ghi chú nguồn số liệu (kỳ chốt GA4, trễ đối soát AppsFlyer) và ngân sách Media rõ ràng.

---

## 4. TIÊU CHUẨN BÁO CÁO THÁNG ĐIỀU HÀNH WEB PLATFORM (EXECUTIVE 6 STREAMS ARCHITECTURE)

Đây là chuẩn mực báo cáo tháng chính thức (Monthly Executive Standard) được thống nhất cho Kênh Web MoMo, bảo đảm tính nhất quán 100% giữa văn bản Board Markdown (`report-thang-XX-YYYY-board.md`), Web Dashboard Hubs (`MonthlyReportApp.tsx`, `MonthlySlideDeck.tsx`) và Bộ Slide Trình Chiếu PowerPoint (`Web_Platform_Thang_XX_YYYY_Pyramid.pptx`):

### 6 Luồng Điều Hành Bắt Buộc (6 Executive Streams)

1. **Stream 1: Khung Điều Hành 3 Trụ Cột (Pillars) [R]:**
   - Phân bổ thành 3 khối chiến lược: Điểm nổi bật (Highlights), Hợp tác liên phòng ban (Collaboration), và Ưu tiên hành động (Priorities).
   - Tóm tắt cô đọng tình hình chuyển dịch tăng trưởng tự nhiên của Kênh Web.

2. **Stream 2: Hiệu Suất Kinh Doanh & Quan Sát Chiến Lược [R]:**
   - Bảng tổng thể Full Month 31 ngày kèm so sánh Target và MoM.
   - Bóc tách rõ ràng cơ cấu Non-Paid Traffic vs Paid Traffic.
   - 3 nhận định điều hành "So What?": Bản chất chuyển dịch, động lực tăng trưởng cốt lõi và cảnh báo rủi ro.

3. **Stream 3: Hai Dự Án Trọng Điểm: Cinema Hub & Financial Hub [R]:**
   - **Cinema Hub:** Quy mô lưu lượng, tỷ trọng cụm rạp, chuyển đổi W2A (Installs, Map Bank, CVR) và tiến độ kỹ thuật cụm Diễn viên.
   - **Financial Hub:** Quy mô lưu lượng, tỷ trọng Non-Paid, mức độ tập trung sản phẩm tín chấp và tín hiệu nhóm Tiện ích Tỷ giá.
   - **Khối đối trọng PLG:** Bắt buộc có khối 3 thẻ so sánh hiệu suất tương tác: Bảng biểu tĩnh (0,0% CTR) vs Tool Tính Lương (33,7% CTR) vs Tool Vay & CIC (38,6% - 43,8% CTR).

4. **Stream 4: Dự Án New User & Phễu Chuyển Đổi Web-to-App [R]:**
   - Phễu chuyển đổi 4 tầng AppsFlyer GPD: Installs -> Registered -> Map Bank -> Active MAU.
   - Phân tích hiệu quả theo hệ điều hành (iOS vs Android) và tỷ lệ KYC/Map Bank.
   - Bóc tách hiệu quả 4 kênh: Banner chào MoMo, Bối cảnh Cinema Hub, Interactive Gamification (Minigame) và Cổng tải app tập trung (`/tai-app`).

5. **Stream 5: Hiệu Suất Công Cụ Tài Chính Tương Tác (Interactive Tools Performance) [R]:**
   - **Quy chuẩn bảng 5 cột tinh gọn duy nhất:**
     `STT | Tên Công Cụ / Tiện Ích | Lượt hiển thị (Imp) | Lượt tương tác (Clicks) | Tỷ lệ tương tác (CTR)`
   - **Quy tắc hiển thị:** Tuyệt đối KHÔNG đưa cột URL kỹ thuật, cột hành động W2A, hay cột đánh giá nhận xét dài dòng vào bảng.
   - **Số liệu MoSpark CMS:** Thống kê đầy đủ các công cụ tương tác thực tế và đối lập với nhóm bảng biểu tĩnh (0% CTR, onsite 48s).
   - **Nhận định điều hành:** 3 gạch đầu dòng phân tích dưới bảng làm rõ công cụ dẫn dắt và cơ sở go-live cho các công cụ tháng kế tiếp.

6. **Stream 6: Trọng Tâm Thảo Luận & Quyết Nghị Ban Giám Đốc [D]:**
   - Mỗi đề xuất cấu trúc chặt chẽ 6 phần: Vấn đề -> Bối cảnh -> Tác động tăng trưởng -> Bảng so sánh các phương án (A vs B) -> Đề nghị với CEO/BOM -> Rủi ro nếu không quyết định.

---

## 4. QUY TẮC ĐỒNG BỘ TAM GIÁC (THREE-WAY SSOT SYNC)

Mọi cập nhật số liệu báo cáo tháng bắt buộc đồng bộ song song 3 thực thể:
1. **Markdown Board Report:** `07_REPORTS/docs/report-thang-XX-YYYY-board.md` và `data/reports/report-thang-XX-YYYY-board.md`.
2. **Web Hubs Dashboard & Slide Deck:** `lib/report/monthly-report-server.ts`, `data/deck/monthly-deck-XX-YYYY.json`, `components/report/monthly/*`.
3. **PowerPoint Deck Template:** `scripts/build_official_templated_pptx.py` -> sinh file `Web_Platform_Thang_XX_YYYY_Pyramid.pptx` đồng bộ Drive và Web Public.

---

## 5. THAM CHIẾU TÀI LIỆU CHI TIẾT

- **Từ điển thuật ngữ báo cáo (SSOT):** [`03_SKILLS/momo-reporting-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-glossary.md)
- **Quy chuẩn gốc cấp công ty:** [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md)
- **Tài liệu Master Framework:** [`03_SKILLS/web-platform-reporting-framework.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/web-platform-reporting-framework.md)
- **Nhật ký Họp & Chỉ đạo Chiến lược:** [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md)
- **Quy tắc Kiến trúc Hệ thống:** [`AGENTS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/AGENTS.md)
- **Định tuyến Tri thức:** [`00_HARNESS_CORE/KNOWLEDGE_ROUTING.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/KNOWLEDGE_ROUTING.md)

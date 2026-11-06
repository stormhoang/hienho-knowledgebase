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
   - **Phân loại Traffic Source SSOT (Non-Paid vs Paid):** BẮT BUỘC phân rã thành 2 nhóm lớn rõ rệt: **Non-Paid Traffic** (tất cả trừ Paid Traffic: Organic, Direct, Referral, Others...) và **Paid Traffic** (Paid). Khi trình bày bảng hoặc danh sách, gom rõ 2 dòng lớn Non-Paid vs Paid, các kênh con đặt thụt dòng dưới Non-Paid, tuyệt đối không để Paid xen kẽ ngang hàng.
   - **Bullet Lead-ins:** Viết tiếng Việt ngắn gọn (`Vượt target:`, `Lưu lượng trực tiếp & sức mạnh thương hiệu:`, `Chuyển dịch SEO sang GEO:`, `Điểm nổi bật:`, `Việc tiếp theo:`). Chỉ giữ tiếng Anh cho thuật ngữ chỉ số: Target, Budget, Actual, MAU, MEU, CVR, Map Bank, OneLink, Installs, New Reg. Toàn bộ báo cáo dùng một ngôn ngữ.
7. **Mật độ thông điệp & bảng biểu:** Tối đa 3 ý chính dưới mỗi tiêu đề, tốt nhất 1-2. Nhiều hơn thì tách slide. Tối đa 2-3 bảng/biểu đồ, không copy dashboard thô.
8. **Trực quan hóa:**
   - Luồng người dùng / Conversion Funnel: Dùng sơ đồ Mermaid (`graph TD` hoặc `graph LR`) + Bảng phân tích chi tiết các bước (Step Breakdown Table).
   - Lộ trình: Dùng Bảng Markdown (`Table`).

---

## 3. TIÊU CHUẨN BÁO CÁO THÁNG ĐIỀU HÀNH WEB PLATFORM (EXECUTIVE 6 STREAMS ARCHITECTURE SSOT)

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

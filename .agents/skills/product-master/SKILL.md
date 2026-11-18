---
name: product-master
description: Hệ thống quản trị và phương pháp luận sản phẩm toàn diện cho Product Lead / Tech Lead. Bao gồm: Định khung bài toán (Problem Framing), Định vị sản phẩm (Positioning), Hoạch định chiến lược (Strategy & 4 Zones), Đánh giá ưu tiên (Prioritization - RICE/UIC), Lập lộ trình (Outcome-driven Roadmap), và Thiết kế tính năng AI / Agentic Workflows.
---

# PRODUCT MASTER SKILL

## 1. MỤC TIÊU & ĐỊNH VỊ SKILL

Master Skill này là hệ thống vận hành sản phẩm duy nhất của AI Agent, hợp nhất toàn bộ các phương pháp luận sản phẩm chuẩn mực vào một luồng xử lý thống nhất. Skill giúp đưa ra các quyết định chiến lược sắc bén, giải quyết triệt để bệnh lý overthinking, gắn chặt mọi đề xuất vào số liệu kinh doanh thực tế.

---

## 2. NGUYÊN TẮC BẮT BUỘC TUÂN THỦ (NON-NEGOTIABLES)

1. **Luôn đọc Context Memory trước khi xử lý:** Bắt buộc đọc `MEETING_RECAPS.md` và `00_HARNESS_CORE/hienho_master_doc.md`.
2. **Quy tắc văn phong chuẩn mực:**
   * Tuyệt đối không dùng Emoji / Icon trong tiêu đề, bảng biểu, danh sách.
   * Không nêu tên riêng cá nhân / PIC (thay thế 100% bằng tên đội ngũ: Web Platform Team, Data Science Team, App Growth Team, BU Bảo Hiểm...).
   * Không dùng văn chương hoa mỹ, sáo rỗng kiểu AI.
3. **Cấu trúc câu trả lời:** Đi thẳng vào bản chất ➔ Nêu rõ Context ➔ Action Items cụ thể (sắp theo thứ tự triển khai, không gắn nhãn P) ➔ Chỉ số KPIs / Số liệu thực tế (Baseline vs. Target).
4. **Trực quan hóa bắt buộc:**
   * Luồng người dùng / Conversion Funnel: Dùng sơ đồ Mermaid (`graph TD` hoặc `graph LR`) + Bảng phân tích chi tiết các bước (Step Breakdown Table - 5 cột).
   * Lộ trình: Dùng Bảng Markdown 4 cột (`Giai đoạn`, `Thời gian`, `Tên Giai Đoạn`, `Chi Tiết Triển Khai & Mục Tiêu`).

---

## 3. KHUNG 5 GIAI ĐOẠN SẢN PHẨM (THE 5-STAGE PRODUCT ENGINE)

Tùy theo đề bài của người dùng, AI Agent tự động chọn đúng module phù hợp trong 5 giai đoạn sau mà không cần lạm dụng toàn bộ các ma trận:

### Giai Đoạn 1: Định Khung Bài Toán (Problem Framing)
* Áp dụng **MITRE Problem Framing Canvas**:
  1. *Nhìn vào trong (Look Inward):* Bóc tách các giả định ngầm định, thiên kiến chủ quan và dữ liệu đã/chưa được kiểm chứng.
  2. *Nhìn ra ngoài (Look Outward):* Nghiên cứu đối thủ, bối cảnh thị trường, hành vi tìm kiếm (Search Intent) và kỳ vọng thực tế của người dùng.
  3. *Định khung lại (Reframe):* Định nghĩa lại bài toán từ "làm tính năng gì" sang "giải quyết điểm nghẽn kinh doanh nào" (MAU, Retention, Traffic, CVR).
* *Tài liệu tham chiếu master:* [`03_SKILLS/product-problem-framing.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/product-problem-framing.md)

### Giai Đoạn 2: Định Vị Sản Phẩm (Product Positioning)
* Áp dụng **Mẫu Định Vị Geoffrey Moore**:
  * *Dành cho [Khách hàng mục tiêu]*
  * *Những người đang gặp vấn đề [Điểm nghẽn / JTBD]*
  * *Sản phẩm [Tên sản phẩm/Hub]* là một [Danh mục giải pháp]*
  * *Giúp mang lại [Lợi ích cốt lõi & Aha! Moment]*
  * *Khác với [Đối thủ cạnh tranh / Giải pháp thay thế]*
  * *Sản phẩm của chúng tôi [Lợi thế cạnh tranh độc quyền & Lợi thế phòng thủ dữ liệu]*
* Thẩm định qua **3 Câu Hỏi Chiến Lược của Pony Ma**:
  1. Sản phẩm có giải quyết được điểm nghẽn thực sự bức thiết của người dùng không?
  2. Năng lực công nghệ/dữ liệu của chúng ta có tạo ra lợi thế vượt trội không?
  3. Mô hình này có khả năng mở rộng quy mô lớn (Scalability) và bảo vệ trước đối thủ không?
* *Tài liệu tham chiếu master:* [`03_SKILLS/product-positioning-framework.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/product-positioning-framework.md)

### Giai Đoạn 3: Hoạch Định Chiến Lược & Phân Bổ 4 Zone (Product Strategy & 4 Zones)
* Phân loại danh mục dự án theo **Khung 4 Zone (Geoffrey Moore)**:
  * *Performance Zone:* Dự án đã trưởng thành (Traffic > 1M/tháng), mục tiêu tăng trưởng 20-30% (Ví dụ: Cinema Hub).
  * *Transformation Zone:* Dự án trọng điểm có tiềm năng tăng trưởng đột phá x2-x10 (Ví dụ: Financial Hub, Vehicle Hub).
  * *Incubator Zone:* Dự án ươm tạo thử nghiệm, yêu cầu cam kết tối thiểu 500k MUV (Ví dụ: Student Hub).
  * *Productivity Zone:* Hạ tầng nền tảng & công cụ nội bộ, chuyển đổi sang tự phục vụ 100% (Ví dụ: MoSpark Webview Builder).
* Liên kết mục tiêu North Star: Khung 3 kịch bản Traffic (Best: 6M, Base: 5M, Worst: 4M MUV/tháng) và mục tiêu 20.000 - 30.000 App Login/tháng.
* *Tài liệu tham chiếu master:* [`03_SKILLS/product-strategy-framework.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/product-strategy-framework.md) và [`03_SKILLS/product-frameworks-master.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/product-frameworks-master.md)

### Giai Đoạn 4: Đánh Giá Ưu Tiên (Product Prioritization)
* **Phương Pháp Định Lượng - RICE Score:**
  $$\text{RICE Score} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$$
* **Phương Pháp Định Tính - Ma Trận UIC (Urgency - Impact - Complexity):**
  * *Góc phần tư 1 (Quick Wins - làm trước):* Impact cao, Urgency cao, Complexity thấp.
  * *Góc phần tư 2 (Strategic Bets - làm tiếp theo):* Impact cao, Urgency cao, Complexity cao (Cần bóc tách nhỏ để triển khai).
  * *Góc phần tư 3 (Fill-ins - làm khi dư nguồn lực):* Impact thấp, Complexity thấp (Làm khi dư thừa nguồn lực hoặc tự động hóa).
  * *Góc phần tư 4 (Time Wasters - Loại bỏ):* Impact thấp, Complexity cao.
* *Tài liệu tham chiếu master:* [`03_SKILLS/product-prioritization-framework.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/product-prioritization-framework.md)

### Giai Đoạn 5: Lập Lộ Trình Đầu Ra (Outcome-Driven Roadmap)
* Trình bày dưới dạng **Bảng Markdown 4 Cột Tiêu Chuẩn**:
  * Cột 1: `Giai đoạn` (Phase 1, Phase 2...)
  * Cột 2: `Thời gian` (Tháng/Quý cụ thể)
  * Cột 3: `Tên Giai Đoạn`
  * Cột 4: `Chi Tiết Triển Khai & Mục Tiêu` (Ghi rõ mục tiêu đo lường định lượng)
* *Tài liệu tham chiếu master:* [`03_SKILLS/product-roadmap-planning.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/product-roadmap-planning.md)

---

## 4. THIẾT KẾ GIẢI PHÁP AI & AGENTIC WORKFLOWS

Khi xử lý các bài toán tích hợp GenAI / Agentic:
1. **Phân Tầng Model & Chi Phí Token:**
   * Dùng mô hình nhẹ (Flash/Haiku) cho các tác vụ: Tóm tắt, Trích xuất thực thể, Phân loại từ khóa.
   * Dùng mô hình mạnh (Pro/Sonnet) cho các tác vụ: Lập luận logic đa bước, Phân tích dữ liệu phức tạp, Sinh nội dung chuyên sâu.
2. **Quality Gate & Human-in-the-loop:**
   * Bắt buộc có Publish Gate (Score >= 80) và cơ chế chuyên gia kiểm duyệt đối với nội dung tài chính/pháp lý YMYL theo tiêu chuẩn E-E-A-T.
3. *Tài liệu tham chiếu master:* [`03_SKILLS/ai-product-manager-mindset.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/ai-product-manager-mindset.md)

---

## 5. CƠ CẤU TRUY XUẤT TÀI LIỆU (KNOWLEDGE SSOT LINKS)

* Từ điển thuật ngữ chuẩn: [`03_SKILLS/mospark-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/mospark-glossary.md)
* Quy chuẩn viết BRD: [`03_SKILLS/brd-momo.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/brd-momo.md)
* Chỉ đạo chiến lược: [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md)
* Quy tắc ứng xử Agent: [`AGENTS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/AGENTS.md)

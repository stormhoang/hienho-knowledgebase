# THƯ VIỆN BỘ MINDSET VÀ SKILLSET DÀNH CHO AI PRODUCT MANAGER & WEB PRODUCT LEAD

Tài liệu này định nghĩa bộ khung tư duy (Mindset) và kỹ năng thực chiến (Skillset) dành cho Web Product Lead và AI Product Manager nhằm khai thác tối đa năng lực của AI Co-pilot và hệ thống Multi-Agent vào toàn bộ vòng đời phát triển sản phẩm Web Platform.

---

## 1. KHUNG TƯ DUY 5 TRỤ CỘT (5 AI-FIRST PRODUCT MINDSETS)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          BỘ MINDSET AI PRODUCT MANAGER                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 1. Context Engineering over Prompting (Tư duy Kiến trúc Bối cảnh)               │
│ 2. Agentic & Multi-Agent Thinking (Tư duy Chuỗi Đa Agent Tự Động)               │
│ 3. Problem Space First, AI Second (Tư duy Bài toán trước, Công nghệ sau)         │
│ 4. Human-in-the-Loop & Trust Guardrails (Tư duy Kiểm soát Rủi ro & QC)         │
│ 5. Outcome-Driven & Token Economics (Tư duy Tối ưu Chi phí & Business Impact)  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Trụ cột 1: Context Engineering over Prompting (Tư duy Kiến trúc Bối cảnh)
* **Bản chất:** Đừng tìm kiếm các "câu prompt thần thánh" rời rạc. Hãy tập trung xây dựng **Hạ tầng Bối cảnh (Context Infrastructure)** cho AI.
* **Thực thi:** Cung cấp đầy đủ Dữ liệu chuẩn gốc (SSOT), Quy chuẩn văn phong, Ranh giới rủi ro (Guardrails) và Định hướng C-Level dưới dạng các file cấu hình cố định. Khi bối cảnh đủ sâu, AI sẽ tự động đưa ra câu trả lời chuẩn xác.

### Trụ cột 2: Agentic & Multi-Agent Thinking (Tư duy Phân công Đa Agent)
* **Bản chất:** Đừng coi AI là một cá nhân làm tất cả mọi việc. Hãy coi AI là một **Tổ chức các Agent chuyên biệt (Multi-Agent System)**.
* **Thực thi:** Bóc tách quy trình làm việc phức tạp thành chuỗi các Agent nhỏ đảm nhận từng khâu (Market Research Agent ➔ UI/UX Designer Agent ➔ Copywriter Agent ➔ Quality Control Agent).

### Trụ cột 3: Problem Space First, AI Second (Tư duy Bài toán trước, Công nghệ sau)
* **Bản chất:** AI là đòn bẩy để giải quyết nhu cầu cốt lõi (Jobs-To-Be-Done) của người dùng và tạo ra tác động kinh doanh (Business Impact), không phải là thứ để phô trương công nghệ.
* **Thực thi:** Luôn bắt đầu từ Tuyên bố bài toán (Problem Statement) và rào cản người dùng trước khi quyết định có tích hợp tính năng AI hay không.

### Trụ cột 4: Human-in-the-Loop & Trust Guardrails (Tư duy Kiểm soát Rủi ro & Lòng tin)
* **Bản chất:** AI đóng vai trò **Sinh nháp & Đề xuất (Drafting & Proposing)**, con người giữ quyền **Quyết định & Kiểm duyệt (Sign-off & Decision Making)**.
* **Thực thi:** Bắt buộc phải có bước kiểm duyệt QC (Quality Control Gate) đối với các thông tin YMYL/Tài chính để ngăn chặn rủi ro tin giả (Hallucination) ảnh hưởng tới uy tín thương hiệu.

### Trụ cột 5: Outcome-Driven & Token Economics (Tư duy Tối ưu Chi phí & Kết quả)
* **Bản chất:** Đo lường thành công của việc ứng dụng AI bằng chỉ số kinh doanh thực tế, không đo bằng số lượng văn bản AI tạo ra.
* **Thực thi:** Theo dõi các chỉ số: Thời gian phát triển giảm từ 2 tuần xuống 1 ngày, Chi phí token/bài giảm 95% (chuyển đổi model Gemini Flash/Mini), Tỷ lệ chuyển đổi Web-to-App CVR tăng x4.

---

## 2. BỘ KỸ NĂNG NĂNG LỰC THỰC CHIẾN (PRACTICAL AI PM SKILLSET)

| Nhóm Kỹ Năng | Kỹ Năng Cụ Thể | Nội Dung & Cách Thực Thi Thực Chiến |
|---|---|---|
| **1. Spec & Knowledge Architecture** | **Kiến trúc hóa Tri thức cho AI Agent** | Khả năng đóng gói kinh nghiệm sản phẩm thành các file chỉ dẫn chuyên sâu (`SKILL.md`, `AGENTS.md`, `KNOWLEDGE_ROUTING.md`), giúp AI Agent tự động vận hành đúng quy chuẩn. |
| | **Thiết kế System Prompt & Context Template** | Nạp sẵn Business Context (12-field templates), quy tắc chấm điểm E-E-A-T và cấu hình nguồn dữ liệu thật vào System Prompt để triệt tiêu lỗi bịa đặt tin tức. |
| **2. GEO & AI Search Literacy** | **Generative Engine Optimization (GEO)** | Tối ưu hóa nội dung website để xuất hiện ưu tiên trong câu trả lời của các AI Search Engine (ChatGPT, Perplexity, Google SGE) qua trích dẫn (AI Citations), Schema Markup và file policy `llms.txt`. |
| | **Programmatic Content & Utility Pipeline** | Xây dựng quy trình tự động hóa sản xuất landing page và công cụ tiện ích (Utility Tools) số lượng lớn dựa trên dữ liệu tìm kiếm (Search Intent). |
| **3. Rapid Prototyping & Validation** | **AI-Powered Vibe Coding & Prototyping** | Dùng AI tự dựng các bản mẫu Widget/Landing Page tương tác (HTML/JS) trong vài giờ để kiểm chứng logic tương tác với các BU thay vì chờ Dev 1-2 tuần. |
| | **Thử nghiệm & Thẩm định Giả thuyết** | Thiết kế luồng A/B Testing linh hoạt, kiểm chứng giả thuyết người dùng ở quy mô nhỏ (Grayscale release) trước khi dồn nguồn lực triển khai hàng loạt. |
| **4. AI Quality & Guardrail Evaluation** | **Xây dựng Quality Gates & Metric Scorecard** | Thiết lập bộ chấm điểm tự động cho sản phẩm (SEO/GEO Scorecard, CSAT, FCR) và kiểm soát lỗi rò rỉ bảo mật/XSS. |
| | **Quản trị Mô hình Chi phí AI (Token Cost)** | Phân tầng lựa chọn mô hình AI (Model Selection): Dùng model nhỏ (Haiku/Flash) cho các tác vụ phân loại/tóm tắt và model lớn (Sonnet/Pro) cho các tác vụ tư duy phức tạp. |
| **5. Agentic Workflow Orchestration** | **Tự động hóa Luồng Công việc Đa Agent** | Thiết kế workflow tự động từ khâu Nghiên cứu từ khóa ➔ Lên Outline ➔ AI Sinh bài viết ➔ Kiểm duyệt QC ➔ Xuất bản 1-click (One-click Publish). |

---

## 3. QUY TRÌNH PHỐI HỢP GIỮA WEB PRODUCT LEAD VÀ AI ASSISTANT

1. **Bước 1 (Input Context):** Web Product Lead đưa ra bài toán kinh doanh hoặc kết quả họp chiến lược.
2. **Bước 2 (Context Retrieval):** AI Assistant đọc bối cảnh từ `MEETING_RECAPS.md`, `decision_log.md` và `KNOWLEDGE_ROUTING.md`.
3. **Bước 3 (Agent Execution):** AI Assistant áp dụng đúng khung tư duy và skill tương ứng để phân tích bài toán, tạo BRD hoặc thiết kế lộ trình.
4. **Bước 4 (Human Sign-off):** Web Product Lead đánh giá, thẩm định và đưa ra quyết định duyệt cuối cùng.

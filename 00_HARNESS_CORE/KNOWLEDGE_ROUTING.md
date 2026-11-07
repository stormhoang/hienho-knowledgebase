# TẦNG KNOWLEDGE ROUTING & PIPELINE CÂU TRẢ LỜI TỐI ƯU (KNOWLEDGE LAYER ARCHITECTURE)

Tài liệu định nghĩa kiến trúc **Tầng Knowledge (Knowledge Layer)** của hệ thống codebase. Thay vì chỉ phân loại câu hỏi (Prompt classification) bề nổi, Tầng Knowledge vận hành như một bộ máy định tuyến tri thức đa lớp (Multi-layer Knowledge Routing Pipeline) để đảm bảo mọi vấn đề người đặt ra đều nhận được **Câu trả lời Tối ưu (Optimal Answer)** chuẩn xác, trung thực và sát bối cảnh kinh doanh.

## Registry tương thích đa Agent

`knowledge_registry.yaml` là lớp metadata bổ sung cho Claude, Antigravity và các Agent khác. Registry không thay thế tài liệu gốc, không khóa quyền đọc trực tiếp và đang vận hành ở chế độ `observe`. Validator tương ứng là `scripts/validate_knowledge_registry.py`; manifest chỉ đọc có thể xuất bằng `scripts/export_agent_context.py`.

---

## 1. KHUNG KIẾN TRÚC 5 TẦNG KNOWLEDGE (5-LAYER KNOWLEDGE PIPELINE)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   TẦNG KNOWLEDGE ROUTING TRUNG TÂM                     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
[TẦNG 1: MEMORY CONTEXT]    [TẦNG 2: PROBLEM FRAMING]   [TẦNG 3: SSOT KNOWLEDGE DOMAIN]
- MEETING_RECAPS.md          - Nhìn vào trong (Assumptions) - Strategic Plan (01)
- decision_log.md            - Nhìn ra ngoài (Biz/User)    - MoSpark Platform (04)
- hienho_master_doc.md       - Định khung lại (Reframe)     - Strategic Hubs (05)
                                                            - Use Cases BRD (06)
                                                            - Reports & Data (07)
    └───────────────────────────────┬───────────────────────────────┘
                                    │
                                    ▼
                    [TẦNG 4: FRAMEWORK & SKILL EXECUTION]
                    - Product Frameworks Master (03)
                    - UIC / RICE Prioritization (03)
                    - CEO Standard BRD (03)
                                    │
                                    ▼
                    [TẦNG 5: OPTIMAL OUTPUT PACKAGING]
                    - Cấu trúc: Context -> Action -> Data
                    - Sơ đồ Mermaid Flow + Step Table
                    - Quy chuẩn: No Emoji, No PIC names
```

---

## 2. QUY TRÌNH VẬN HÀNH CHI TIẾT TỪNG TẦNG KNOWLEDGE

### Agent Execution Contract

Sau khi định tuyến tri thức, Agent phải tra `AGENT_CAPABILITIES.yaml` để chọn đúng entrypoint và kiểm tra thuộc tính `read_only`, `requires_approval`, `external_write`. Mọi thao tác ghi tuân thủ `AGENT_SAFETY_CONTRACT.yaml`. Kết quả trả về theo `AGENT_OUTPUT_CONTRACT.md`.

### Tầng 1: Context Memory Layer (Tầng Bối Cảnh Lịch Sử & Chỉ Đạo - Kích Hoạt Có Điều Kiện)
Chỉ kích hoạt khi thực hiện bài toán Chiến lược cấp cao, Viết báo cáo Lãnh đạo hoặc Lập PRD mới. Đối với các tác vụ kỹ thuật, code review, tra cứu nhanh, Agent bỏ qua Tầng 1 và đi thẳng vào Tầng 3 (SSOT Domain):
- [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md): Chỉ đạo chiến lược của Ban Giám đốc (chỉ đọc mục gần nhất liên quan đến chủ đề).
- [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md): Memory SSOT Hiệu suất: dữ liệu Performance thực tế, Run-rate Target và cơ cấu Kênh/Hubs.
- [`08_DECISION_LOG/decision_log.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/08_DECISION_LOG/decision_log.md): Nhật ký các quyết định kiến trúc và nghiệp vụ đã chốt.
- [`00_HARNESS_CORE/hienho_master_doc.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/hienho_master_doc.md): Tổng quan toàn bộ hệ thống Web Platform & MoSpark (chỉ tham chiếu khi cần đối soát kiến trúc tổng thể).

### Tầng 2: Executive Problem Framing Layer (Tầng Định Khung Bài Toán)
Phân tích vấn đề người dùng đặt ra theo 3 góc nhìn quản trị:
- **Tác động Kinh doanh (Business Metrics):** Tác động như thế nào tới MAU, New Users, W2A Conversion Rate, Doanh thu?
- **Rào cản Trải nghiệm & Niềm tin (Trust & UX Friction):** Bài toán có đụng đến điểm đau (Pain points) hay rào cản an toàn tài chính của người dùng không?
- **Năng lực Nền tảng (MoSpark Platform Capability):** Nền tảng hiện có đáp ứng được chưa hay cần nâng cấp?

### Tầng 3: SSOT Knowledge Domain Layer (Tầng Tri Thức Chuẩn Thuần)
Định tuyến trực tiếp đến đúng nguồn dữ liệu gốc (Single Source of Truth) trong repo:
- **Tăng trưởng & OKRs:** Thư mục [`01_STRATEGIC_PLAN/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/01_STRATEGIC_PLAN).
- **Hạ tầng MoSpark & Tracking Tools:** Thư mục [`04_MOSPARK_PLATFORM/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM) và file SSOT [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md) (Quy chuẩn bắt buộc cho Event Tracking mọi Utility Tools & Calculators).
- **Các cụm Hubs:** Thư mục [`05_HUBS/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS).
- **Dataset Từ Khóa & SEO Inventory Gốc (Use Case Inventory):** Thư mục SSOT [`05_HUBS/inventory/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) (kho dữ liệu CSV nguyên bản bóc tách từng từ khóa và search volume cho Financial, vehicle-hub, insurtech, ota, telco, hospital, Lottery, trust...).
- **Các Use Case BRD:** Thư mục [`06_USE_CASE_MOMO/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO).
- **Báo cáo & Số liệu thực tế:** Thư mục [`07_REPORTS/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS) và file SSOT [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md).
- **Đặc tả PRD:** Thư mục [`09_PRD/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/09_PRD).
- **Tư duy & Triết lý Lãnh đạo:** File [`10_LEADERSHIP_MINDSET/leadership-mindset.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/10_LEADERSHIP_MINDSET/leadership-mindset.md).
- **Tin tức & Thị trường (Gemini Spark):** Thư mục [`11_NEWS_FEED/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/11_NEWS_FEED).
- **Trạng thái triển khai & shipment:** Dùng [`14_ROADMAP/ship_releases.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/14_ROADMAP/ship_releases.json), PRD liên quan và dữ liệu release thực tế. Project không duy trì một hệ thống tasklist nội bộ riêng.

### Tầng 4: Master Skill & Framework Execution Layer (Tầng Thực Thi Master Skills)
Kích hoạt 3 Master Skills trong thư mục [`.agents/skills/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/.agents/skills) kết hợp cùng kho tham chiếu [`03_SKILLS/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS):
- **Product Master (`product-master`):** Kích hoạt cho các bài toán định khung vấn đề, định vị sản phẩm, hoạch định chiến lược 4 Zone, đánh giá ưu tiên RICE/UIC, lập lộ trình và thiết kế luồng AI.
- **Web Platform Reporting (`web-platform-reporting`):** Kích hoạt cho đóng gói báo cáo định kỳ Weekly gửi Executive Leadership và Monthly gửi Ban Giám Đốc. Quy chuẩn trình bày gốc nằm ở [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md), đọc trước khi dựng hoặc review bất kỳ báo cáo/slide nào.
- **Frontend Slides (`frontend-slides`):** Kích hoạt khi cần khởi tạo slide thuyết trình Web hiện đại bằng HTML/CSS hoạt họa chuẩn Stage 16:9 (1920×1080) zero dependencies, phục vụ thuyết trình trực tiếp, pitch deck, reporting và export.
- **Keyword Clustering & Content Strategy (`keyword-clustering-strategy`):** Kích hoạt khi xử lý kho dữ liệu từ khóa Use Case (`05_HUBS/inventory/`), lọc ngữ nghĩa (Semantic Filtering), gom cụm SERP Intent, kiến trúc Topic Cluster, xác định Potential Keywords và xây dựng Content Strategy / Content Plan gắn với Web-to-App. Tài liệu đặc tả kỹ thuật và bàn giao tối ưu: [`00_HARNESS_CORE/KEYWORD_CLUSTERING_OPTIMIZATION_SPEC.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/KEYWORD_CLUSTERING_OPTIMIZATION_SPEC.md).

### Tầng 5: Optimal Output Packaging Layer (Tầng Đóng Gói Câu Trả Lời Tối Ưu)
Kiểm soát chuẩn định dạng đầu ra theo đúng chỉ dẫn [`AGENTS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/AGENTS.md):
- **Cấu trúc câu trả lời:** Đi thẳng vào bản chất ➔ Nêu rõ Context ➔ Action Items cụ thể ➔ Chỉ số KPIs / Số liệu thực tế.
- **Biểu diễn luồng người dùng:** Sơ đồ Mermaid (`graph TD` hoặc `graph LR`) + Bảng phân tích chi tiết các bước.
- **Biểu diễn lộ trình:** Bảng Markdown (`Table`).
- **Quy chuẩn văn phong:** Không Emoji/Icon trong tiêu đề/bảng/danh sách, không tên riêng cá nhân PIC (thay bằng tên team chuyên môn), không dùng từ "sàn Web" (chỉ dùng "nền tảng Web", "Kênh Web", "Web Platform" hoặc "Web"), không từ ngữ hoa mỹ kiểu AI.

---

## 3. NGUYÊN TẮC BẢO ĐẢM CÂU TRẢ LỜI HOÀN HẢO (OPTIMAL ANSWER GUARANTEE)

1. **Không hoang đường dữ liệu (Zero Hallucination):** 100% số liệu và bối cảnh trình bày phải xuất phát từ Tầng 3 (SSOT Knowledge Domain) và Tầng 1 (Memory Context).
2. **Không trả lời bề nổi:** Khi tiếp nhận câu hỏi, Agent phải đi xuyên suốt từ Tầng 1 đến Tầng 5 để tạo ra câu trả lời có chiều sâu quản trị thay vì chỉ giải nghĩa từ ngữ.
3. **Luôn đo lường bằng chỉ số kinh doanh:** Mọi đề xuất sản phẩm đều phải gắn liền với tác động tới MAU, New Users, Web-to-App CR hoặc Doanh thu.

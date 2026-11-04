# SKILL REGISTRY & FRAMEWORK HUB

File chỉ mục và sơ đồ đăng ký trung tâm (Registry Index) giúp AI Agent và đội ngũ nắm bắt hệ thống **3 Master Agent Skills** và thư viện tri thức nghiệp vụ trong codebase.

---

## 1. HỆ THỐNG MASTER AGENT SKILLS (.agents/skills/)

Hệ thống các bộ kỹ năng thực thi cốt lõi của AI Agent:

- **[[.agents/skills/product-master/SKILL.md|product-master]]**: Hệ thống quản trị và phương pháp luận sản phẩm toàn diện cho Product Lead / Tech Lead. Hợp nhất 5 giai đoạn: Định khung bài toán (Problem Framing), Định vị sản phẩm (Positioning), Hoạch định chiến lược & 4 Zones (Strategy), Đánh giá ưu tiên (RICE/UIC Prioritization), Lập lộ trình (Outcome-Driven Roadmap), và Thiết kế tính năng AI / Agentic Workflows.
- **[[.agents/skills/keyword-clustering-strategy/SKILL.md|keyword-clustering-strategy]]**: Hệ thống bóc tách dữ liệu từ khóa từ `05_HUBS/inventory/`, gom cụm ngữ nghĩa (Intent Clustering), tính toán Keyword Difficulty (KD), Opportunity Score, chống ăn thịt từ khóa (Cannibalization Shield), tích hợp Seasonality 5Y và xuất bản sang Web Hubs. Kèm tài liệu bàn giao kỹ thuật: `00_HARNESS_CORE/KEYWORD_CLUSTERING_OPTIMIZATION_SPEC.md`.
- **[[.agents/skills/content-plan-architect/SKILL.md|content-plan-architect]]**: Quy chuẩn tự động lập Kế hoạch Nội dung (Content Plan 7 tầng), quy hoạch lịch xuất bản 30-60-90 ngày theo Quick Wins, dàn ý H2/H3 E-E-A-T, Schema JSON-LD, Silo Linking và GEO Direct Answers cho Web Platform.
- **[[.agents/skills/content-plan-architect-v-hoan/SKILL.md|content-plan-architect-v-hoan]]**: Bản V.Hoan (V3.3) lập content plan Theme > Pillar > Cluster (mỗi Cluster = 1 bài) từ inventory từ khóa MoMo, từ khóa chính là volume cao nhất, chặn thin content và cannibalization, dàn ý H1-H4 gộp heading đối thủ top 1-3 và heading lấp content gap. Chạy bằng `scripts/generate_content_plan.py`.
- **[[.agents/skills/web-platform-reporting/SKILL.md|web-platform-reporting]]**: Quy chuẩn và công cụ tạo báo cáo định kỳ (Weekly gửi Executive Leadership, Monthly gửi Ban Giám Đốc) cho Web Platform theo chuẩn 3 khối nội dung và 2 tầng chỉ số.
- **[[.agents/skills/frontend-slides/SKILL.md|frontend-slides]]**: Tạo slide thuyết trình trực tiếp trên nền tảng Web bằng HTML/CSS/JS hoạt họa mượt mà, zero-dependency, chuẩn stage cố định 16:9 (1920×1080), hỗ trợ đầy đủ bộ preset phong cách (Bold Templates, Clean Modern, Editorial) không lỗi layout.

---

## 2. THƯ VIỆN KHUNG TƯ DUY & PHƯƠNG PHÁP LUẬN SẢN PHẨM (03_SKILLS/)

Kho tài liệu tham chiếu sâu (Single Source of Truth) phục vụ tra cứu chi tiết:

- **[[product-frameworks-master]]**: Thư viện Master các khung tư duy sản phẩm (Mô hình 4 Zone Geoffrey Moore, DHM Gibson Biddle, 4 Product Risks Marty Cagan, Cynefin, Kano, Ansoff, Hook, 3 Horizons).
- **[[product-problem-framing]]**: Phương pháp luận phân tích và định khung bài toán (MITRE Problem Framing Canvas - Look Inward / Look Outward / Reframe).
- **[[product-positioning-framework]]**: Phương pháp luận định vị sản phẩm theo mẫu Geoffrey Moore và 3 câu hỏi thẩm định của Pony Ma.
- **[[product-strategy-framework]]**: Phương pháp luận hoạch định chiến lược sản phẩm từ Tầm nhìn ➔ Chiến lược ➔ OKRs ➔ Lộ trình.
- **[[product-roadmap-planning]]**: Phương pháp luận lập kế hoạch lộ trình dựa trên kết quả đầu ra (Outcome-Driven Roadmap - Bảng Markdown).
- **[[product-prioritization-framework]]**: Phương pháp luận đánh giá ưu tiên RICE Score & Ma trận 4 góc phần tư UIC.
- **[[ai-product-manager-mindset]]**: Bộ khung tư duy (Mindset) và kỹ năng thực chiến (Skillset) cho AI PM & Web Product Lead.

---

## 3. THƯ VIỆN QUẢN TRỊ FINTECH, QUY CHUẨN TÀI LIỆU & BÁO CÁO

- **[[awesome-product-management]]**: Thư viện quy chuẩn Quản trị Sản phẩm chuẩn quốc tế (Tooling, Spec Documentation, Metrics, Reading List).
- **[[awesome-fintech]]**: Thư viện Hệ sinh thái & Mô hình Tài chính Fintech (BaaS, Embedded Finance, APIs kết nối tài chính, Lending/Credit).
- **[[brd-momo]]**: Quy chuẩn viết tài liệu BRD chuẩn CEO Standard (Problem Framing, JTBD, Product Job, Metrics).
- **[[web-platform-reporting-framework]]**: Master Framework cho toàn bộ hệ thống báo cáo định kỳ của Web Platform.
- **[[c-level-reporting-framework]]**: Khung trình bày báo cáo chiến lược dành cho C-Level (Business Impact & Growth).

---

## 4. THƯ VIỆN QUY CHUẨN ĐỒNG BỘ THUẬT NGỮ & TUÂN THỦ

- **[[mospark-glossary]]**: Từ điển thuật ngữ chuẩn hóa các khái niệm sản phẩm và hệ thống trong hệ sinh thái MoSpark / MoMo Web Platform.
- **[[momo-ymyl-guideline]]**: Quy chuẩn tuân thủ E-E-A-T và đánh giá rủi ro đối với mảng sản phẩm tài chính (Your Money Your Life).

---

## 5. CHỈ ĐẠO CHIẾN LƯỢC & QUY TẮC THỰC THI (MANDATORY DIRECTIVES)

- 👉 **[[MEETING_RECAPS]]**: Bối cảnh chiến lược và chỉ đạo trực tiếp từ Ban Giám đốc (anh Công, anh Tường).
- 👉 **[[AGENTS]]**: Master Rules về văn phong Product Lead (Không emoji, không tên riêng PIC, Mermaid User Flow, Roadmap Table).
- 👉 **[[decision_log]]**: Nhật ký các quyết định chiến lược và kỹ thuật đã thống nhất.

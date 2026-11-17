---
name: content-plan-architect
description: Quy chuẩn và động cơ tự động lập Kế hoạch Nội dung (Content Plan 7 tầng), quy hoạch lịch xuất bản 30-60-90 ngày theo Quick Wins, dàn ý H2/H3 E-E-A-T, Schema JSON-LD, Silo Linking và GEO Direct Answers cho MoMo Web Platform.
---

# CONTENT PLAN ARCHITECT SKILL

## 1. MỤC TIÊU & ĐỊNH VỊ SKILL

Skill này định nghĩa chuẩn mực cao nhất để chuyển hóa dữ liệu từ khóa thô (Raw Keyword Inventory tại `05_HUBS/inventory/`) thành một **Bản Kế Hoạch Nội Dung Hoàn Chỉnh (Enterprise Content Plan)** phục vụ trực tiếp cho Đội ngũ Nội dung (`Content Team`) và Đội ngũ Kỹ sư Web (`Web Dev`).

Lấy cảm hứng từ quy trình tự trị khép kín (Autonomous SEO Lifecycle của Wriai), skill này giải quyết triệt để 4 bài toán lớn:
1. **Khử ăn thịt từ khóa (Zero Cannibalization):** 1 Search Intent = 1 URL đích duy nhất. Các biến thể đồng nghĩa được gom làm Secondary Synonyms.
2. **Chuẩn mực E-E-A-T & Độ dài bài viết:** Phân bổ hạn mức từ (`min_words` - `target_words`) và dàn ý H2/H3 Entity Checklist bắt buộc.
3. **Tối ưu hóa Tìm kiếm Tạo sinh (GEO):** Cung cấp sẵn đoạn Direct Answer Snippet 40-60 từ đón đầu Google AI Overviews và Factsheet chuẩn bị cho Knowledge Graph.
4. **Mạng lưới liên kết nội bộ (Silo Topology):** Xác định Parent Hub, Peer In-Silo và Cross-Silo Bridges kèm Anchor Text khuyến nghị.

---

## 2. NGUYÊN TẮC BẮT BUỘC TUÂN THỦ (NON-NEGOTIABLES)

1. **SSOT Data Source:** 100% dữ liệu từ khóa, volume, CPC và độ cạnh tranh phải trích xuất từ `05_HUBS/inventory/`. Không tự suy diễn số liệu thô.
2. **Quy chuẩn văn phong:**
   - Tuyệt đối không dùng Emoji / Icon trong tiêu đề, bảng biểu, danh sách.
   - Không đề cập tên riêng cá nhân / PIC (thay bằng tên đội ngũ: `Content Team`, `SEO Team`, `Web Dev`...).
   - Tuyệt đối không dùng từ "sàn", "sàn Web", "toàn sàn" (chỉ dùng "toàn Website", "nền tảng Web", "Kênh Web", "Web Platform" hoặc "Web").
   - Văn phong Product Lead / Tech Lead: thực tế, cô đọng, sắc bén, định lượng bằng số liệu.
3. **Móc chuyển đổi Web-to-App:** 100% bài viết trong Content Plan phải có điểm chạm Web-to-App cụ thể (Widget tính toán, Tra cứu trực tuyến hoặc Deeplink vào App MoMo).

---

## 3. CẤU TRÚC CHUẨN 7 KHỐI CỦA MỘT BẢN CONTENT PLAN (THE 7-LAYER BLUEPRINT)

Mọi tệp Content Plan lưu tại `06_USE_CASE_MOMO/content-plans/<sector>/<id>-content-plan.md` bắt buộc phải có đầy đủ 7 khối:

### Khối 1: Bảng Kế Hoạch Bài Viết Chi Tiết (Actionable Content Plan)
Bảng quy hoạch 1 Pillar Hub Page + 3-5 Cluster Pages gồm 11 cột chuẩn:
`STT` | `URL Slug` | `Tiêu Đề Bài Viết / Trang Đích` | `Primary Keyword` | `Secondary Synonyms (Đã Gom Chống Ăn Thịt)` | `Search Volume` | `Search Intent` | `Định Dạng Nội Dung` | `Phễu` | `Ưu Tiên` | `Điểm Chạm Web-to-App (CTA Hook)`

### Khối 2: Bảng Phân Bổ Intent & Phễu Chuyển Đổi
Bảng thống kê tỷ lệ phần trăm phân bổ theo Intent (`Informational`, `Commercial`, `Transactional`, `Tool/Calculator`, `Navigational`) và Phễu chuyển đổi (`TOFU`, `MOFU`, `BOFU`) gắn với JTBD của người dùng.

### Khối 3: Chiến Lược Điều Hướng & Trải Nghiệm Người Dùng (UX Flow)
Nguyên tắc luân chuyển người dùng:
- Pillar Page liên kết bối cảnh tới tất cả Cluster Pages.
- 100% Cluster Pages đặt anchor text trong 100 từ đầu tiên dẫn về Pillar Page.
- Móc nối Widget tính toán / tra cứu sang phễu chuyển đổi App MoMo.

### Khối 4: Content Brief & Dàn Ý H2/H3 Entity Checklist
Với từng bài viết trong kế hoạch:
- URL Slug chuẩn SEO.
- Định mức độ dài bài viết:
  - *Master Hub Pillar:* 2.500 - 3.500 từ.
  - *High Conversion Guide (Tool/Transactional):* 1.500 - 2.200 từ.
  - *Comparison & Review (Commercial):* 1.800 - 2.500 từ.
  - *Educational Spoke (Informational):* 1.200 - 1.600 từ.
- Dàn ý H2/H3 chi tiết bao gồm đề mục câu hỏi thường gặp (FAQs) giải quyết các biến thể từ khóa phụ.

### Khối 5: Dữ Liệu Cấu Trúc JSON-LD (Structured Data Schema)
Mã nguồn JSON-LD hoàn chỉnh sẵn sàng để `Web Dev` copy vào code:
- `BreadcrumbList Schema`: Cấu trúc phân cấp Trang chủ ➔ Ngành ➔ Use Case.
- `FAQPage Schema`: Bộ câu hỏi và câu trả lời thực tế theo intent của người dùng.

### Khối 6: Kiến Trúc Liên Kết Nội Bộ (Internal Linking & Silo Matrix)
- *Parent Hub Pillar:* Link trỏ về Cổng dịch vụ cấp 1 kèm Anchor text mỏ neo bắt buộc.
- *Peer In-Silo:* 3-5 bài viết vệ tinh cùng ngành có điểm tương quan cao nhất kèm đường dẫn và Anchor text tự nhiên.
- *Cross-Silo Bridges:* Cầu nối liên kết xuyên ngành bổ trợ chuyển đổi (ví dụ: Vehicle Hub link sang Insurtech, Financial link sang Vehicle).

### Khối 7: Tối Ưu Hóa Tìm Kiếm Tạo Sinh (GEO & AI Direct Answers)
- *Đoạn trích dẫn trực tiếp (40-60 từ):* Viết sẵn dạng định nghĩa cô đọng, rõ thực thể và USP của MoMo để công cụ tìm kiếm AI (Google AI Overviews, SearchGPT, Perplexity) trích dẫn trực tiếp.
- *Bảng thuộc tính thực thể (Knowledge Graph Factsheet):* 6 cặp thuộc tính chuẩn hóa (Phân loại, Đối tượng, Thời gian xử lý, Kỹ thuật, Bảo mật, Kênh chuyển tiếp).

---

## 4. QUY HOẠCH LỊCH TRÌNH XUẤT BẢN 30-60-90 NGÀY (EDITORIAL PHASING)

Để tối ưu hóa ROI và kéo traffic nhanh nhất, việc triển khai Content Plan phải tuân thủ nghiêm ngặt 3 giai đoạn:

| Giai Đoạn | Khung Thời Gian | Trọng Tâm Sản Xuất | Tiêu Chí Lựa Chọn Từ Khóa | Mục Tiêu Kinh Doanh |
| :--- | :---: | :--- | :--- | :--- |
| **Giai Đoạn 1** | Ngày 1-30 | **100% Quick Wins (Đợt 1)** | Search Volume $\ge 1.500$, Mức độ Cạnh tranh Low. Trích xuất từ `07_REPORTS/QUICK_WINS_PORTFOLIO.md`. | Kéo Organic Clicks và New User tăng trưởng ngay trong tháng đầu tiên với chi phí thấp nhất. |
| **Giai Đoạn 2** | Ngày 31-60 | **Master Pillars & BOFU Converters** | Các trang Cột trụ ngành và trang Công cụ / Tra cứu (Intent: `Tool/Calculator` & `Transactional`). | Xây dựng Thẩm quyền chủ đề (Topical Authority) và đẩy mạnh tỷ lệ chuyển đổi Web-to-App. |
| **Giai Đoạn 3** | Ngày 61-90 | **Supporting Spokes & Long-tail Expansion** | Các bài viết giải đáp chi tiết, hướng dẫn thủ tục và câu hỏi thường gặp (Intent: `Informational`). | Phủ kín mạng lưới Semantic Silo, dẫn truyền PageRank bền vững và triệt tiêu 100% khoảng trống nội dung. |

---

## 5. BỘ LỆNH & CÔNG CỤ TỰ ĐỘNG HÓA (CLI & AUTOMATION)

### 1. Sinh Content Plan cho một Use Case cụ thể:
```bash
./.venv/bin/python scripts/generate_content_plan.py <slug_use_case>
# Ví dụ: ./.venv/bin/python scripts/generate_content_plan.py gui-tiet-kiem
```

### 2. Sinh Content Plan hàng loạt cho toàn bộ một Khối Ngành:
```bash
./.venv/bin/python scripts/generate_content_plan.py --sector <tên_ngành>
# Ví dụ: ./.venv/bin/python scripts/generate_content_plan.py --sector Financial
# Ví dụ: ./.venv/bin/python scripts/generate_content_plan.py --sector insurtech
```

### 3. Sinh Content Plan toàn diện cho 188 Use Cases & Cập nhật Mục lục:
```bash
./.venv/bin/python scripts/generate_content_plan.py --all
```
*Lưu ý: Lệnh này sẽ tự động cập nhật tệp mục lục trung tâm tại `06_USE_CASE_MOMO/content-plans/INDEX.md`.*

### 4. Đồng bộ dữ liệu sang Web Platform Hubs:
```bash
./.venv/bin/python scripts/sync_inventory_to_hubs.py
```

### 5. Test toàn vẹn hệ thống (Audit Test Suite):
```bash
./.venv/bin/python scripts/validate_seo_pipeline.py
```
*Yêu cầu bắt buộc: Đạt 100% PASS trước khi bàn giao bản kế hoạch cho các đội ngũ chuyên môn.*

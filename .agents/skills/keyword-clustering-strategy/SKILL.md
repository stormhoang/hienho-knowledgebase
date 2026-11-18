---
name: keyword-clustering-strategy
description: Hệ thống lọc Semantic Keyword, gom cụm Intent Clustering, thiết kế kiến trúc Topic Cluster (Pillar-Cluster-Spoke), đánh giá Potential Keywords và lập Content Strategy, Content Plan chuẩn Tech/Product Lead cho các Use Case thuộc Web Platform.
---

# KEYWORD CLUSTERING & CONTENT STRATEGY SKILL

## 1. MỤC TIÊU & ĐỊNH VỊ SKILL

Skill này là quy trình chuẩn mực chuyển hóa dữ liệu từ khóa thô (Raw Keyword Inventory) tại thư mục SSOT `05_HUBS/inventory/` thành:
1. **Kiến trúc Topic Cluster hoàn chỉnh** (Pillar Page ➔ Cluster Pages ➔ Supporting Spokes).
2. **Ma trận Từ khóa Tiềm năng (Opportunity Matrix)** phân loại chuẩn xác Quick Wins, Strategic Pillars và Commercial Converters.
3. **Chiến lược Nội dung (Content Strategy) và Kế hoạch Bài viết (Content Plan)** gắn chặt với mục tiêu kinh doanh Kênh Web: Tăng trưởng Organic Traffic (MUV, PVs), tối ưu Tỷ lệ Chuyển đổi Web-to-App (W2A CR) và tăng trưởng New Users / Transactions cho MoMo.

---

## 2. NGUYÊN TẮC BẮT BUỘC TUÂN THỦ (NON-NEGOTIABLES)

1. **SSOT Data Source:** 100% số liệu từ khóa, volume, CPC và mức độ cạnh tranh bắt buộc phải trích xuất trực tiếp từ các file CSV trong `05_HUBS/inventory/`. Tuyệt đối không tự suy diễn số liệu thô.
2. **Quy tắc văn phong:**
   - Tuyệt đối không dùng Emoji / Icon trong tiêu đề, bảng biểu, danh sách.
   - Không nêu tên riêng cá nhân / PIC (thay thế bằng tên đội ngũ chuyên môn: Content Team, SEO Team, Web Dev, Growth Team...).
   - Tuyệt đối không dùng từ "sàn", "sàn Web", "toàn sàn" (chỉ dùng "toàn Website", "nền tảng Web", "Kênh Web", "Web Platform" hoặc "Web").
   - Không dùng văn phong hoa mỹ, sáo rỗng kiểu AI.
3. **Triệt tiêu xung đột từ khóa (Zero Keyword Cannibalization):** Mỗi Search Intent chỉ được phân bổ cho duy nhất 1 URL đích. Các từ khóa đồng nghĩa, biến thể lỗi gõ, biến thể số ít/số nhiều phải gom chung vào cùng một cụm URL.
4. **Định hướng Web-to-App:** Mọi bài viết trong Content Plan phải có điểm chạm Web-to-App rõ ràng (Contextual CTA, Mini-tool Widget, Deeplink).

---

## 3. QUY TRÌNH 5 BƯỚC THỰC THI (THE 5-STAGE ENGINE)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PIPELINE TỪ INVENTORY ĐẾN CONTENT PLAN              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
[BƯỚC 1: DATA CLEAN & SEMANTIC FILTER]              [BƯỚC 2: INTENT-BASED CLUSTERING]
- Làm sạch formula: '="text"' ➔ 'text'              - Gom cụm theo Entity cốt lõi & n-gram
- Chuẩn hóa Unicode NFC, sửa lỗi Telex              - 1 Intent = 1 URL (Chống Cannibalization)
- Lọc bỏ Keyword rác & ngoài phạm vi (Out-of-scope) - Phân tách Primary, Secondary, LSI
    │                                                               │
    └───────────────────────────────┬───────────────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
[BƯỚC 3: TOPIC CLUSTER ARCHITECTURE]                [BƯỚC 4: OPPORTUNITY MATRIX]
- Pillar Page (Hub Cột trụ & Utility Tool)          - Tính Opportunity Score
- Cluster Pages (Chuyên sâu từng phân nhóm)          - Phân bổ 4 góc phần tư: Quick Wins,
- Supporting Spokes (Vệ tinh, PAA, FAQs)              Pillars, Converters, Long-tail
- Ma trận Internal Linking 2 chiều                  
    │                                                               │
    └───────────────────────────────┬───────────────────────────────┘
                                    │
                                    ▼
                [BƯỚC 5: CONTENT STRATEGY & CONTENT PLAN]
                - Định vị Funnel: TOFU ➔ MOFU ➔ BOFU
                - Gắn móc chuyển đổi Web-to-App JTBD
                - Bảng Content Plan 10 cột chuẩn triển khai
```

### Bước 1: Data Clean & Semantic Filtering (Làm Sạch & Lọc Ngữ Nghĩa)
- Bóc tách công thức Excel `="val"` thành giá trị chuỗi/số thực.
- Chuẩn hóa lỗi gõ Telex phổ biến trong dataset từ khóa: `ddaaus` ➔ `đấu`, `ddieenj` ➔ `điện`, `tiet kiem` ➔ `tiết kiệm`...
- Nhận diện và loại bỏ các nhóm từ khóa rác:
  - *Từ khóa nhầm lẫn thương hiệu (Brand Misalignment):* Ví dụ trong use case gửi tiết kiệm ngân hàng, loại bỏ "giao hàng tiết kiệm", "gửi hàng tiết kiệm".
  - *Từ khóa vi phạm / tiêu cực:* Các truy vấn liên quan đến lừa đảo không thể điều hướng, vi phạm pháp luật.
  - *Truy vấn điều hướng thuần đối thủ (Navigational Trap):* Các từ khóa login nội bộ app đối thủ không có cơ hội rank tự nhiên và không chuyển đổi được sang MoMo.
- Gắn thẻ Search Intent cho từng từ khóa:
  - `Informational (Info)`: Tìm kiếm thông tin, kiến thức, định nghĩa.
  - `Commercial (Comm)`: So sánh, tìm hiểu giá cả, lãi suất, đánh giá nên chọn loại nào.
  - `Tool/Calculator (Tool)`: Tra cứu số liệu, công cụ tính lãi, kiểm tra thông tin.
  - `Transactional (Trans)`: Có ý định đăng ký, mở tài khoản, thanh toán ngay.
  - `Navigational (Nav)`: Tìm đường dẫn tới cổng dịch vụ hoặc chi nhánh cụ thể.

### Bước 2: Intent-based Clustering (Gom Cụm Từ Khóa & Chống Ăn Thịt Từ Khóa)
- Nhóm các từ khóa có cùng Search Intent và cùng thực thể (Entity) vào 1 Cụm (Cluster).
- Nguyên tắc chống Cannibalization: Nếu Google trả về cùng 1 tập kết quả SERP cho 2 từ khóa (ví dụ: `lãi suất gửi tiết kiệm ngân hàng` và `lãi suất tiền gửi tiết kiệm ngân hàng`), bắt buộc gom vào 1 URL, không tách làm 2 bài viết riêng biệt.
- Trong mỗi Cluster, phân bổ:
  - **Primary Keyword:** Từ khóa có Search Volume cao nhất và mang tính đại diện nhất cho toàn cụm.
  - **Secondary Keywords:** Các biến thể mở rộng, từ khóa dài hơn bổ sung nghĩa.
  - **Semantic / LSI Keywords:** Các thực thể liên quan trực tiếp cần xuất hiện trong tiêu đề H2/H3 hoặc nội dung bài viết.

### Bước 3: Topic Cluster Architecture (Thiết Kế Cấu Trúc Cột Trụ - Vệ Tinh)
Thiết kế cấu trúc website theo mô hình Hub & Spoke:
- **Pillar Page (Core Hub):**
  - Trang trung tâm bao trùm chủ đề lớn của Use Case (ví dụ: Cẩm nang & Bảng Tra cứu Lãi suất Tiết kiệm Ngân hàng Toàn diện).
  - Tích hợp công cụ tương tác (Interactive Utility Widget) phục vụ nhu cầu tính toán/tra cứu tức thì.
- **Cluster Pages (Sub-topics):**
  - Các trang giải quyết triệt để từng phân khúc nhu cầu con (theo thương hiệu, theo kỳ hạn, theo thủ tục).
- **Supporting Spokes (Satellites):**
  - Các bài viết giải đáp thắc mắc chi tiết, câu hỏi People Also Ask (PAA), so sánh trực diện 1-1.
- **Mô hình Internal Linking:**
  - Pillar liên kết xuống tất cả Cluster Pages và nhận liên kết ngược lại từ tất cả Cluster Pages với Contextual Anchor Text chuẩn SEO.
  - Các Cluster Pages cùng ngữ cảnh liên kết ngang (Horizontal Linking) với nhau.
  - Mọi bài viết đều chứa Anchor Text và Button dẫn về Utility Tool hoặc Deeplink mở App MoMo.

### Bước 4: Opportunity Matrix (Đánh Giá Từ Khóa Tiềm Năng)
Tính toán chỉ số **Opportunity Score** cho từng từ khóa:
$$\text{Opportunity Score} = \log_{10}(\text{Volume} + 1) \times (1.2 - \text{Competition Factor}) \times \text{Intent Weight} \times (1 + \text{CPC Bonus})$$

Phân loại từ khóa vào 4 góc phần tư:
1. **Quick Wins:** Volume cao/trung bình, Cạnh tranh thấp (Low PPC Competition). Sản xuất trước để chiếm lĩnh Top SERP nhanh chóng.
2. **Strategic Pillars:** Volume cực lớn, Cạnh tranh trung bình/cao. Cần đầu tư tài nguyên lớn, nội dung chuẩn chuyên gia E-E-A-T và tích hợp Widget tương tác để tạo đòn bẩy dài hạn.
3. **Commercial Converters:** Volume vừa phải nhưng Search Intent mang tính thương mại hoặc hành động cao (Commercial / Transactional / Tool). Đóng vai trò phễu chuyển đổi Web-to-App tốt nhất.
4. **Long-tail / Supporting:** Volume nhỏ (< 100), cạnh tranh thấp. Đóng gói vào mục FAQ của bài viết chính hoặc triển khai ở đợt sau cùng.

### Bước 5: Content Strategy & Content Plan Hoàn Chỉnh
- Thiết lập chiến lược nội dung theo hành trình khách hàng (Customer Journey):
  - **TOFU (Top of Funnel):** Giải quyết nhu cầu tìm kiếm nhanh, tra cứu kiến thức.
  - **MOFU (Middle of Funnel):** Cung cấp góc nhìn phân tích, so sánh, chứng minh tính an toàn và minh bạch.
  - **BOFU (Bottom of Funnel):** Trải nghiệm công cụ tính toán / form tương tác trên Web, kích hoạt CTA mở App MoMo để nhận quyền lợi / thực hiện giao dịch.
- Đóng gói Content Plan dưới dạng Bảng Markdown 10 cột chuẩn:
  - Cột 1: `STT`
  - Cột 2: `URL Slug`
  - Cột 3: `Chủ Đề & Tiêu Đề Dự Kiến`
  - Cột 4: `Primary Keyword`
  - Cột 5: `Secondary Keywords & LSI`
  - Cột 6: `Search Volume (MTD)`
  - Cột 7: `Search Intent`
  - Cột 8: `Định Dạng Nội Dung (Format)`
  - Cột 9: `Giai Đoạn Phễu (TOFU/MOFU/BOFU)`
  - Cột 10: `Móc Chuyển Đổi Web-to-App (CTA Hook)`

---

## 4. HƯỚNG DẪN THỰC THI BẰNG SCRIPT CÔNG CỤ (AUTOMATION SCRIPTS)

### 4.1. Phân tích Cục bộ một File Từ khóa (Single File Intake)
Khi cần trích xuất và xử lý nhanh bất kỳ file từ khóa nào trong `05_HUBS/inventory/`, sử dụng Python Runtime SSOT:
```bash
./.venv/bin/python scripts/keyword_cluster_engine.py "05_HUBS/inventory/<nhóm_ngành>/<file_từ_khóa>.csv"
```
Kết quả trả về tự động bóc tách:
- Tổng số lượng từ khóa và tổng Search Volume toàn bộ tệp.
- Phân bổ các Cụm Topic Cluster chính.
- Danh sách từ khóa tiềm năng xếp hạng theo Opportunity Score, KD (0-100) và phân nhóm Ma trận 4 góc phần tư.

### 4.2. Đồng bộ Toàn diện sang Web Hubs (`react-web-momo`)
Khi cần đồng bộ toàn bộ kho Inventory sang nền tảng Web Hubs:
```bash
./.venv/bin/python scripts/sync_inventory_to_hubs.py
```
Script sẽ tự động:
- Áp dụng `MERGE_MAP` chống phân mảnh (ví dụ: gộp 37 ngân hàng vào `ngan-hang`).
- Lọc nhiễu ngữ nghĩa (Semantic Outlier Filter).
- Chống ăn thịt từ khóa (MoMo Domain SERP Cannibalization Shield).
- Nạp Seasonality 5-Year Google Trends SSOT từ `07_REPORTS/data/theme_seasonality.json`.
- Xuất bản 161 file modular chunks sang `react-web-momo/data/seo-clusters/<sector>/<id>.json`.

---

## 5. TÀI LIỆU BÀN GIAO KỸ THUẬT & ĐẶC TẢ TỐI ƯU HÓA (OPTIMIZATION ROADMAP)

Chi tiết toàn bộ kiến trúc, bài học thực tế, các lỗi đã giải quyết và danh mục 4 nhiệm vụ tối ưu hóa chuyên sâu được lưu trữ tại tài liệu SSOT:
👉 **[`00_HARNESS_CORE/KEYWORD_CLUSTERING_OPTIMIZATION_SPEC.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/KEYWORD_CLUSTERING_OPTIMIZATION_SPEC.md)**.
*(Bao gồm hướng dẫn bàn giao chi tiết dành cho kỹ sư phụ trách tối ưu hóa skill).*

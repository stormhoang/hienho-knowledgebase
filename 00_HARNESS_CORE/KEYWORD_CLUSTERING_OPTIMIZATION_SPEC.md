# BẢN ĐẶC TẢ TỐI ƯU HÓA SKILL KEYWORD CLUSTERING & CRAWL DATA PIPELINE
> **Tài liệu Bàn giao Kỹ thuật (Technical Handover & Optimization Specification)**  
> **Người thực hiện tối ưu:** Hoan (SEO & Keyword Intelligence Engineer)  
> **Phạm vi:** Pipeline xử lý dữ liệu từ khóa thô (`05_HUBS/inventory/`), Gom cụm ngữ nghĩa (Keyword Clustering), Đánh giá tiềm năng (KD, Opportunity Score), Chống ăn thịt từ khóa (Cannibalization Shield) và Xuất bản sang Web Hubs (`react-web-momo`).  
> **Trạng thái hệ thống hiện tại:** 12 Hubs | 161 Themes chuẩn hóa | 292.880 từ khóa sạch | 138.637 từ khóa chống ăn thịt | 210 Seasonality 5Y Curves.

---

## 1. TỔNG QUAN KIẾN TRÚC & DÒNG DỮ LIỆU HIỆN HỮU (CURRENT ARCHITECTURE)

Dữ liệu từ khóa của Web Platform vận hành theo luồng khép kín từ kho dữ liệu thô đến giao diện Web Hubs:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. KHO DỮ LIỆU THÔ (RAW INVENTORY)                                     │
│    Vị trí: 05_HUBS/inventory/<Sector>/<Theme>.csv                      │
│    (Chứa cột Keyword, Volume, CPC, PPC Competition, Trending...)        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. ĐỘNG CƠ XỬ LÝ & NLP TIẾNG VIỆT (KEYWORD INTELLIGENCE ENGINE)        │
│    - Gateway tách từ SSOT: scripts/lib/vi_nlp.py (underthesea/pyvi)    │
│    - Chuẩn hóa Telex / Formula Excel: scripts/lib/keyword_intelligence │
│    - Nhận diện Entity / Brand: scripts/lib/keyword_extractor.py        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. LỌC NGỮ NGHĨA & PHÒNG CHỐNG ĂN THỊT TỪ KHÓA (CANIBALIZATION SHIELD) │
│    - Merge Map: Gom các file phân mảnh (37 banks -> ngan-hang, v.v.)   │
│    - MoMo Domain SERP Shield: Đối soát với URL momo.vn trực tiếp       │
│    - Semantic Domain Filter: Loại bỏ rác, lệch nghĩa (Outliers)        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 4. THUẬT TOÁN ĐỊNH LƯỢNG (SCORING & CLASSIFICATION)                    │
│    - Search Intent Classifier: 5 loại Intent (Info/Comm/Trans/Tool/Nav)│
│    - Keyword Difficulty (KD 0-100): Tính toán định lượng theo formula  │
│    - Opportunity Score & 4 Ma trận góc phần tư (Strategic, Quick Win...)│
│    - Pillar Selection: Chọn từ khóa đại diện Theme (không chọn sub-nav)│
│    - Seasonality 5Y SSOT: scripts/theme_seasonality.py            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 5. XUẤT BẢN & GIAO DIỆN WEB HUBS (REACT-WEB-MOMO CONSUMPTION)          │
│    - Chunks: data/seo-clusters/<sector>/<id>.json (161 files)          │
│    - Master Index: data/seo-clusters/index.json + quick-wins.json      │
│    - UI Keyword Explorer: components/content-plan/KeywordExplorer.tsx  │
│    - UI Seasonality: components/content-plan/SeasonalityCalendar.tsx   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. BÀI HỌC VÀ LỖ HỔNG PHÁT HIỆN QUA CÁC ĐỢT CHẠY THỰC TẾ (LESSONS LEARNED)

Trong quá trình xử lý thực tế các Hub (Financial, OTA, Telco, Vehicle, Insurtech...), hệ thống đã phát hiện nhiều rủi ro cần Hoan chú ý và xử lý triệt để:

### 2.1. Hiện tượng Phân Mảnh Theme (Cannibalization & Entity Fragmentation)
- **Vấn đề đã gặp:** Trong Hub Financial, crawl data ban đầu chứa 37 file CSV riêng lẻ cho 37 ngân hàng (`vietcombank.csv`, `techcombank.csv`, `bidv.csv`...). Nếu giữ nguyên 37 theme riêng lẻ sẽ gây phân mảnh trầm trọng, tạo 37 URL tranh chấp từ khóa về sản phẩm ngân hàng trên Website MoMo.
- **Giải pháp đã áp dụng:** Sử dụng `MERGE_MAP` để gom toàn bộ 37 ngân hàng vào 1 theme duy nhất: `ngan-hang` ("Hệ Thống Ngân Hàng"), chỉ giữ lại các sub-intent bên dưới. Tương tự với `co-tuc` (gom từ `chia-co-tuc`), `vi-tra-sau` (gom từ `mua-truoc-tra-sau`), `ve-xe` (gom từ `xe-khach` và `ve-xe-khach`), `crypto` (gom từ 3 sàn tiền ảo).

### 2.2. Lệch Ngữ Nghĩa Do Dịch Thuật / Đồng Âm Khác Nghĩa (Semantic Drift)
- **Vấn đề đã gặp:** File `gia-pha.csv` trong `ota/` ban đầu bị hệ thống mapping nhầm thành "Cây Gia Phả Dòng Họ" và chứa cả từ khóa nội thất thạch cao (`phào chỉ`, `phào nhôm`, `phào nhựa`). Bản chất use case thuộc OTA phải là **"Giá Vé Phà & Tuyến Phà"** (Phà Cần Giờ, Phà Cát Lái...).
- **Giải pháp đã áp dụng:** Bổ sung bộ lọc Outliers chủ động trong `SemanticDomainFilter` để thanh lọc từ khóa vật liệu xây dựng, trả lại đúng thực thể bến phà / vé phà đường thủy.

### 2.3. Lỗi Trục Tung và Dữ Liệu Giả Trên UI (Dummy Data Fallback)
- **Vấn đề đã gặp:** Biểu đồ xu hướng tìm kiếm trên Hub UI từng dùng hàm sin ngẫu nhiên `Math.sin(i + seed)` và gắn nhãn cảnh báo `Dữ liệu mẫu, chờ KB`, trục Y tự động co dãn gây méo đường cong tìm kiếm.
- **Giải pháp đã áp dụng:** Đã kết nối trực tiếp với Seasonality 5Y SSOT của Google Trends (`calcTrendData`) và nhúng trường `seasonality` trực tiếp vào file JSON của từng theme, khóa trục Y `domain={[0, 'auto']}`.

### 2.4. Trích Xuất Từ Khóa Phụ Thiếu Thông Số Định Lượng
- **Vấn đề đã gặp:** Giao diện Keyword Research cần tra cứu từ khóa phụ có đầy đủ Volume, CPC, Độ khó (KD). Trước đây script chỉ trích xuất từ khóa thô mà không tính KD từ PPC Competition và CPC.
- **Giải pháp đã áp dụng:** Đã bổ sung hàm `calculate_kd(competition, volume, cpc)` và xuất mảng `keywords` gồm top 100-150 từ khóa sạch có đầy đủ chỉ số cho tất cả 161 themes.

---

## 3. PHẠM VI & NHIỆM VỤ TỐI ƯU HÓA DÀNH CHO HOAN (OPTIMIZATION SCOPE)

Nhiệm vụ trọng tâm của Hoan là biến quy trình này thành một **Skill tự động hóa cao cấp, tinh gọn và có tính phòng vệ cao** khi người dùng ném bất kỳ file CSV crawl data mới nào vào `05_HUBS/inventory/`.

### 🎯 Nhiệm vụ 1: Hoàn thiện Công cụ Phân tích Cục bộ (Single-File Intake CLI)
- **Hiện trạng:** Script `scripts/keyword_cluster_engine.py` hiện tại còn đơn giản, dùng pattern từ khóa tĩnh hardcode (chỉ có cho lãi suất và biển số xe).
- **Yêu cầu nâng cấp:**
  1. Viết lại `scripts/keyword_cluster_engine.py` để nhận tham số đường dẫn file CSV bất kỳ:
     ```bash
     ./.venv/bin/python scripts/keyword_cluster_engine.py 05_HUBS/inventory/<Sector>/<file>.csv [--hub <Sector>] [--export]
     ```
  2. Tích hợp trọn vẹn:
     - Tách từ tiếng Việt qua gateway `scripts/lib/vi_nlp.py`.
     - Lọc sạch công thức Excel `="val"`, sửa lỗi Telex.
     - Tự động nhận diện Entity bằng n-gram và tần suất xuất hiện, không hardcode danh sách ngành.
     - Phân loại Intent, tính KD (0-100), Opportunity Score và Quadrant (Quick Win, Strategic Pillar...).
     - Tự động chọn Pillar Keyword chuẩn Theme (không lấy sub-query điều hướng).
  3. Khi thêm cờ `--export`, script tự động đóng gói file JSON tương thích với schema `react-web-momo/data/seo-clusters/<sector>/<id>.json` và cập nhật vào `index.json`.

### 🎯 Nhiệm vụ 2: Tự động hóa Nhận diện Lệch Ngữ Nghĩa (Automated Outlier Purge)
- **Hiện trạng:** Hiện tại các rule lọc outlier vẫn phải bổ sung thủ công bằng regex khi phát hiện từ khóa rác lọt vào.
- **Yêu cầu nâng cấp:**
  1. Xây dựng cơ chế **Semantic Distance Check**: So sánh độ tương đồng ngữ nghĩa giữa từ khóa con với Tên Theme / Pillar Keyword.
  2. Bổ sung từ điển Stopwords và Negative Lexicon mở rộng theo từng Sector (Financial, OTA, Healthcare, Education, Telco...).
  3. Cảnh báo ngay trên terminal danh sách top 10 từ khóa bị nghi ngờ là rác / lệch nghĩa để người dùng xác nhận trước khi đưa vào cluster.

### 🎯 Nhiệm vụ 3: Tối ưu Tốc độ Đồng bộ Cục bộ (Incremental Sync Option)
- **Hiện trạng:** Script `scripts/sync_inventory_to_hubs.py` mỗi lần chạy quét toàn bộ 161 themes trên 12 Hubs, mất từ 1-2 phút.
- **Yêu cầu nâng cấp:**
  1. Thêm cờ `--theme <theme_id>` hoặc `--file <path_to_csv>` vào `sync_inventory_to_hubs.py`.
  2. Cho phép sync riêng 1 theme duy nhất trong < 3 giây mà vẫn cập nhật chính xác `index.json`, `seo-clusters-summary.json` và `quick-wins.json` mà không làm hỏng dữ liệu các theme khác.

### 🎯 Nhiệm vụ 4: Đồng bộ Hoàn Chỉnh với Contract của Web Hubs UI
Đảm bảo mọi file JSON do script sinh ra tuân thủ chính xác Schema của `KeywordExplorer.tsx`:
- `id`: string (slug không dấu)
- `name`: string
- `display_name`: string (tiếng Việt có dấu chuẩn)
- `sector`: string (Hub chuẩn)
- `total_volume`: number
- `clean_keywords_count`: number
- `pillar_keyword`: `{ keyword: string, volume: number, cluster_volume: number, intent: string, secondary_synonyms: string[] }`
- `intent_breakdown`: `{ Informational: number, Commercial: number, ... }`
- `quadrant_breakdown`: `{ "Strategic Pillar": number, "Quick Win": number, ... }`
- `keywords`: mảng từ khóa phụ có `{ keyword, volume, cpc, competition, kd, intent, score, quadrant, synonyms }`
- `seasonality`: mảng 12 số nguyên (0-100) theo Google Trends 5Y SSOT
- `cannibalization_shield`: `{ verdict, risk_level, action, top_live_url, rationale }`
- `geo_optimization`: `{ direct_answer_snippet, entity_facts }`

---

## 4. HỆ THỐNG FILE & CONTRACT KỸ THUẬT CẦN NẮM VỮNG

Khi bắt tay vào code, Hoan cần đọc và kế thừa các file SSOT sau:

| File Đường Dẫn | Vai Trò & Trách Nhiệm |
| :--- | :--- |
| `scripts/lib/keyword_intelligence.py` | **Bộ não thuật toán:** Chứa `calculate_kd`, `calculate_opportunity_score`, `classify_quadrant`, `MultiSignalIntentClassifier`, `SERPCannibalizationShield`. |
| `scripts/lib/vi_nlp.py` | **Gateway NLP Tiếng Việt:** Hàm `segment()`, `segment_text()`, bắt buộc dùng cho mọi tác vụ tách từ / n-gram. |
| `scripts/sync_inventory_to_hubs.py` | **Pipeline đồng bộ Master:** Chứa `MERGE_MAP`, logic bóc tách inventory, sinh modular chunks và push sang UI. |
| `scripts/theme_seasonality.py` | **Seasonality SSOT:** Crawl và chuẩn hóa dữ liệu mùa vụ Google Trends 5 năm (`07_REPORTS/data/theme_seasonality.json`). |
| `05_HUBS/inventory/` | **Kho dữ liệu thô (Input):** Chứa các file CSV được phân theo từng thư mục Hub ngành. |
| `react-web-momo/data/seo-clusters/` | **Đích xuất bản (Output Chunks):** Nơi chứa 161 file modular JSON và `index.json`. |
| `react-web-momo/components/content-plan/KeywordExplorer.tsx` | **Giao diện hiển thị:** Component Next.js đọc dữ liệu từ cluster JSON và hiển thị cho người dùng. |

---

## 5. CÁC QUY TẮC BẮT BUỘC TUÂN THỦ (NON-NEGOTIABLES TRONG WORKSPACE)

1. **Python Environment:** Luôn gọi `./.venv/bin/python <script_path>` (Python 3.12 trong môi trường ảo nội bộ). Tuyệt đối không dùng `python3` trần để tránh macOS fallback về Python 3.9 hệ thống.
2. **SSOT Rule:** Dữ liệu volume, CPC và competition phải lấy từ CSV trong `05_HUBS/inventory/`, không tự bịa đặt số liệu.
3. **Writing Style:** Không dùng Emoji/Icon trong báo cáo và bảng biểu; không dùng từ "sàn" (thay bằng "toàn Website", "Kênh Web", "Web Platform").
4. **Zero Cannibalization:** Mỗi search intent chỉ gán cho 1 URL duy nhất. Nếu có URL momo.vn đang rank tốt, bắt buộc gán verdict `CONSOLIDATE`.

---

## 6. CHECKLIST NGHIỆM THU KHI HOÀN THÀNH (ACCEPTANCE CRITERIA)

- [ ] Chạy lệnh đơn giản phân tích 1 file CSV bất kỳ trong `05_HUBS/inventory/` trả ra kết quả trực quan ngay trên terminal trong < 5 giây.
- [ ] Không còn lỗi lệch nghĩa ngữ nghĩa (Outliers được phát hiện và loại bỏ tự động).
- [ ] Tính năng `--export` sinh ra file JSON hợp lệ, mở trên `KeywordExplorer.tsx` hiển thị mượt mà, đầy đủ Search Volume, KD, CPC, Intent, Google Trends 5Y Seasonality và danh sách từ khóa phụ.
- [ ] Code tuân thủ chuẩn ESLint và kiểm thử thành công bằng `./.venv/bin/python`.

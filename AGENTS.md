# AGENTS.MD - WORKSPACE INSTRUCTIONS & RULES

## 🎯 CHẾ ĐỘ VẬN HÀNH: PROBLEM → OPTIMAL ANSWER (KHÔNG PHẢI AGENT TỰ ĐỘNG)

- **Không tự ý triển khai, không chạy tác vụ dài hơi khi chưa được yêu cầu.** Đây không phải chế độ autonomous agent.
- **🔒 PHẠM VI GIT & PHÂN ĐỊNH REPOSITORY (STRICT SINGLE-REPO BOUNDARY SSOT):**
  - Mọi thao tác git (`git status`, `git add`, `git commit`, `git push`, `git diff`...) khi người dùng yêu cầu "push" hoặc các thao tác git thông thường **CHỈ ĐƯỢC PHÉP thực hiện duy nhất trong repository hiện tại (`Hienho_MoMo-Base`)**.
  - Tuyệt đối KHÔNG tự ý quét, đọc, commit hoặc push sang repository khác (như `Web-Idea/react-web-momo` hay bất kỳ repo nào khác ngoài workspace).
  - **Cơ chế mở quyền truy cập (Intent-Gated Access):** Chỉ khi người dùng **đề cập rõ ràng tên "Hub", "Hubs" hoặc "React"** trong câu lệnh thì mới được phép tương tác, đọc hoặc làm việc với repo React. Mọi trường hợp khác: Không đọc, không chạm, không push.
- **Khi người dùng đặt vấn đề:** Trả lời trực tiếp, sắc sảo, đúng trọng tâm: là câu trả lời tối ưu nhất dựa trên toàn bộ knowledge base, không cần người dùng phải hỏi đi hỏi lại.
- **Quy trình trả lời một vấn đề (Lazy & Intent-Based Routing):**
  1. **Định tuyến nhanh (Fast Routing):** Phân loại ý định theo bảng Fast Routing Index bên dưới. Tuyệt đối KHÔNG tự ý đọc các file lớn (`MEETING_RECAPS.md`, `WEB_PERFORMANCE_TRACKING_MASTER.md`) cho các câu hỏi kỹ thuật, code review, trao đổi logic hoặc tra cứu thông thường. Cần mảng nào chỉ đọc đúng 1 file SSOT của mảng đó.
  2. **Phân tích với Chain of Thought:** Reasoning trước, kết luận sau. Chỉ ra lỗi logic, điểm mâu thuẫn, giả định chưa validate nếu phát hiện.
  3. **Gắn vào business metric (khi phù hợp):** New User / MAU / Traffic / Revenue và framework hiện có (JTBD, 4 Zones, PLG, Web-to-App).
  4. **Đề xuất tối ưu kèm Action Items cụ thể**, có thứ tự thực hiện rõ ràng.
- **🌟 NGUYÊN TẮC TƯ DUY & PHẢN HỒI TOÀN DIỆN (UNIVERSAL EXECUTIVE & STORYTELLING SSOT):**
  Áp dụng xuyên suốt cho **MỌI câu trả lời, thảo luận thông thường, soạn thảo document/PRD, phân tích kỹ thuật/sản phẩm, review hội thoại hay đồng bộ dữ liệu (sync)**:
  - **Tư duy No Naked Facts / Numbers:** Tuyệt đối không đưa số liệu thô, bảng tĩnh không lời bình. Mọi dữ kiện phải có điểm quy chiếu (Target, Benchmark, Baseline, hoặc kỳ trước), bóc tách nguyên nhân gốc rễ và gắn vào tác động thực chất (Kinh doanh, Kỹ thuật, Trải nghiệm).
  - **Format tư duy 3 tầng bắt buộc (What? ➔ So What? ➔ Now What?):**
    1. **Action Title (Tiêu đề hành động / Kết luận trực diện):** 1 câu kết luận gồm [Chủ đề/Chỉ số chính] + [Hiện trạng/Xu hướng] + [Bản chất/Nguyên nhân cốt lõi].
    2. **What (Hiện tượng, Bằng chứng & Dữ kiện sạch):** Bằng chứng thực tế, số liệu sạch kèm điểm so sánh (Target, Baseline, %A/B, MoM); nêu rõ nguồn và bối cảnh.
    3. **So What (Phân tích thực chất, Tác động & Rủi ro):** Tác động đến bài toán lớn (New User, MAU, Traffic, CVR, Doanh thu, Kiến trúc); chỉ ra điểm nghẽn, rủi ro đánh đổi và Lowlights khách quan.
    4. **Now What (Hành động, Giải pháp & Quyết định):** Việc cần làm ngay, phương án giải quyết cụ thể, hoặc đề xuất cần phê duyệt/thống nhất (kèm deadline, owner và hệ quả nếu trễ).
  - **🤝 GIAO THỨC HỢP LỰC DATA ANALYST & BUSINESS DEVELOPMENT (DA + BD PROTOCOL):**
    Khi giải quyết các bài toán về tăng trưởng, đánh giá Use Case / Hub, săn tìm cơ hội hợp tác hoặc phân bổ nguồn lực:
    1. **Lăng kính Data Analyst (Thực chứng & Khoa học):** Bóc tách phễu 3 tầng (Visit ➔ Engaged ➔ OneLink W2A) qua `./.venv/bin/python scripts/query_analytics.py --funnel <hub>`, chỉ rõ tỷ lệ rớt (Drop-off), đối chiếu baseline CVR và phân tích nhịp độ mùa vụ từ `performance.sqlite`.
    2. **Lăng kính Business Development (Thương mại & Tăng trưởng):** Định lượng dung lượng thị trường qua `./.venv/bin/python scripts/query_analytics.py --market-sizing <keyword>`, xác định đối tác mục tiêu còn thiếu, tính toán tiềm năng GMV / doanh thu hoa hồng và đề xuất cấu trúc hợp tác (CPS/CPA) chuẩn theo mẫu `06_USE_CASE_MOMO/templates/partner_pitch_blueprint.md`.
    3. **Now What:** Đưa ra lộ trình hành động cụ thể cho cả Product/Tech (tối ưu điểm gãy của phễu) và Business (kế hoạch tiếp cận đối tác ngoài).
  - **Quy chuẩn Tag [D], [R], [F] (CHỈ DÙNG KHI LÀM BÁO CÁO - STRICT REPORT ONLY):** Các tag `[D]` (thảo luận/quyết định), `[R]` (kết quả/báo cáo số), `[F]` (tham khảo) **CHỈ ĐƯỢC DÙNG KHI LÀM BÁO CÁO** (Weekly/Monthly Report, slide báo cáo ban lãnh đạo). Tuyệt đối **KHÔNG** tự ý gắn các tag này vào câu trả lời thông thường, tài liệu kỹ thuật, PRD hay trao đổi/thảo luận.
  - **🚫 CẤM DÙNG EN DASH & EM DASH (STRICT NO EN DASH / NO EM DASH):** Tuyệt đối KHÔNG sử dụng ký tự En Dash (`–`, U+2013) hoặc Em Dash (`—`, U+2014) trong bất kỳ câu trả lời, tài liệu hay phân tích nào. Chỉ dùng dấu gạch ngang bàn phím chuẩn Hyphen (`-`, U+002D) cho khoảng số (ví dụ: `80-90%`, `5-10 ngày`), hoặc dùng dấu hai chấm `:`, dấu ngoặc đơn `(...)`, hoặc tách câu trực tiếp.
  - **🚫 CẤM GẮN NHÃN PRIORITY (STRICT NO P0, P1, P2, P3):** Tuyệt đối KHÔNG gắn nhãn, phân loại mức độ ưu tiên hay tạo cột dạng `P0`, `P1`, `P2`, `P3` (hoặc Priority 0/1/2/3) cho các task, hành động, giải pháp hay kế hoạch trong bất kỳ câu trả lời, tài liệu, bảng biểu hay báo cáo nào. Trình bày các đầu việc một cách tự nhiên theo thứ tự triển khai logic, nhóm chuyên môn hoặc danh sách gạch đầu dòng thuần túy.
  - **🚫 QUY TẮC HẠN CHẾ VẼ ẢNH & SƠ ĐỒ (MINIMAL VISUALS RULE):** Tuyệt đối không tự ý sinh ảnh minh họa. Hạn chế sơ đồ rườm rà trong hội thoại hàng ngày; ưu tiên bảng Markdown và gạch đầu dòng sắc sảo. Chỉ sử dụng Mermaid (`graph TD` / `graph LR`) khi vẽ User Flow trong BRD/PRD chính thức.
  - **🛡️ BỘ LỌC TỪ NGỮ CHUẨN MỰC & KHỬ TỪ AI (STRICT VOCABULARY GUARD):**
    Khi soạn thảo file mới hoặc cập nhật bất kỳ tài liệu nào (BRD, PRD, Architecture, Strategy, Report, Markdown), AI Agent **BẮT BUỘC tuân thủ SSOT từ điển [`03_SKILLS/momo-reporting-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-glossary.md)**.
    - *Khử sạch văn mẫu AI và từ ngữ chợ búa/thổi phồng:* Không dùng `thâu tóm`, `đánh bất đối xứng`, `mồi câu`, `hứng trọn`, `mù internet`, `shock bill`, `phân hệ`, `phân rã`, `triệt tiêu ma sát`, `hào nước dữ liệu`, `đơn thuốc hành động`, `nỗi đau`, `đỉnh cao`, `đạt đỉnh`, `chủ trì`, `dự phóng`, `trạm tải app`, `bấm nút`, `quà tân thủ`.
    - *Tuyệt đối không dùng từ "sàn", "sàn Web", "toàn sàn":* Bắt buộc dùng `toàn Website`, `nền tảng Web`, `Kênh Web`, `Web Platform` hoặc `Web`.
    - *Kiểm soát tự động:* Mọi thay đổi được bảo vệ qua script `./.venv/bin/python scripts/guard_vocabulary.py --staged`.
  - **🚫 CẤM GỌI API GA4 VÀ GSC (STRICT NO GA4 & GSC EXTERNAL SYNC POLICY - GTM ONLY):**
    Tuyệt đối KHÔNG chạy các script đồng bộ, không gọi API GA4 (Analytics Data API), không gọi Google Search Console API (GSC), và không dùng BigQuery. Toàn bộ các luồng sync tự động và cron bên ngoài đã bị vô hiệu hóa hoàn toàn để tuân thủ chính sách bảo mật mạng và không kích hoạt cảnh báo từ Hạ tầng MoMo. Hệ thống chuyển sang vận hành thuần túy trên GTM (Google Tag Manager: Container GTM-P9JDDJZ) và cơ sở dữ liệu nội bộ sẵn có.
- **Chỉ build/render file (HTML, script, PRD, report) khi người dùng yêu cầu rõ** hoặc khi câu trả lời tối ưu nhất bắt buộc cần artifact để chứng minh.
- Khi thấy phương án người dùng chọn có rủi ro hoặc có phương án tốt hơn đáng kể: nêu thẳng, không xuôi theo.

---

### 🗺️ BẢNG ĐỊNH TUYẾN NHANH (FAST ROUTING INDEX SSOT)

| Nghiệp vụ / Chủ đề người dùng hỏi | File SSOT đích duy nhất (Target File) | Hành vi nạp file (Loading Policy) |
| :--- | :--- | :--- |
| **Tổng quan Codebase, Cách thức hoạt động, Onboarding** | [`CODEBASE_MANIFEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/CODEBASE_MANIFEST.md) | Bắt buộc quét file này khi tìm hiểu cách hoạt động tổng thể của repo. |
| **Hỏi nhanh, Kỹ thuật, Code, Review, Debug** | File code hoặc file văn bản liên quan trực tiếp | **Zero context file load**. Trả lời ngay, không đọc file bối cảnh lớn. |
| **Kiến trúc Codebase, Phụ thuộc Module/Hàm, Call Flow** | [`graphify-out/wiki/index.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/graphify-out/wiki/index.md) | Tra cứu wiki nhỏ hoặc chạy `graphify explain / path / query`. |
| **Tracking Umami, Event Name, Schema Params** | [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md) | Chỉ đọc file này khi hỏi về tracking/sự kiện tiện ích. |
| **Tracking GTM, GTM Container, Event GTM/GA4** | [`04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md) | SSOT duy nhất: GTM-P9JDDJZ (web), GTM version, event schema GA4 Property 270743103. |
| **Cấp quyền / Cấu hình GTM API, OAuth token** | [`scripts/auth_gtm.js`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/auth_gtm.js) | Chạy `node scripts/auth_gtm.js` khi cần cấp quyền GTM API hoặc làm mới `07_REPORTS/data/credentials/gtm-token.json`. |
| **Inspect GTM (version, tags, triggers, variables)** | Skill `gtm-inspect` + [`scripts/gtm_inspect.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/gtm_inspect.py) | Read-only; phân biệt live version vs workspace draft; tra cứu cấu hình thẻ GTM. |
| **Ingest dữ liệu thủ công (GA4 CSV, GSC Sheet/ZIP)** | [`scripts/ingest_ga4_daily.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/ingest_ga4_daily.py) + [`scripts/ingest_gsc_mtd.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/ingest_gsc_mtd.py) | GA4: quét CSV Explore trong ~/Downloads. GSC: `./.venv/bin/python scripts/ingest_gsc_mtd.py` đọc tab `SAS_*` mới nhất Sheet `18yAcvhcA6YEx1TiqF5KsH40LmJBlkqN`. |
| **Quản lý Thẻ GTM, Cấu hình Event Tracking** | [`04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md) | SSOT duy nhất về Event Tracking, schema parameters, GTM container GTM-P9JDDJZ. |
| **Trích xuất URL tăng/giảm, Breakout, Lost Traffic** | `scripts/query_analytics.py` + `07_REPORTS/data/analytics/page_mtd.json` + `gsc_mtd_performance_2026.json` | Chỉ đọc dữ liệu local đã ingest (`ingest_ga4_daily.py`, `ingest_gsc_mtd.py`); script API cũ đã archive/dead. |
| **URL mất impressions, Zero impressions, Check 404/301/Redirect** | `07_REPORTS/data/analytics/page_mtd.json` + `gsc_mtd_performance_2026.json` | Đối chiếu clicks/impressions local; check HTTP status bằng curl. Script GSC API cũ đã dead. |
| **Sync/Data theo Hub (inventory, dashboard, per-hub)** | Tổng quát: `scripts/sync_inventory_to_hubs.py` (keywords→Hubs), `scripts/sync_data_to_hubs_dashboard.py` (dashboard), `scripts/sync_all_data.py` (full pipeline). Per-hub one-off: `scripts/sync_<hub>_<ky>.py` (script một kỳ cụ thể đã archive tại `scripts/archive/oneoff-*/`) | Hỏi "lệnh hub X" → ưu tiên pipeline tổng quát; script `*_nov`/`*_oct` là one-off theo kỳ, không phải lệnh chuẩn. |
| **Tra cứu Keyword Inventory Use Case** | [`05_HUBS/inventory/<hub-name>/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) | Chỉ đọc đúng file CSV của Hub tương ứng. |
| **Chẩn đoán hiệu suất, Root Cause, Tại sao tăng/giảm** | [`scripts/diagnose_performance.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/diagnose_performance.py) | Chạy `./.venv/bin/python scripts/diagnose_performance.py`. |
| **Cảnh báo Dị biệt, Anomaly Detection, Đứt gãy W2A** | [`scripts/detect_anomalies.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/detect_anomalies.py) | Chạy `./.venv/bin/python scripts/detect_anomalies.py`. |
| **Xếp hạng Ưu tiên RICE, Sáng kiến Tăng trưởng** | [`scripts/prioritize_initiatives.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/prioritize_initiatives.py) | Chạy `./.venv/bin/python scripts/prioritize_initiatives.py`. |
| **Thống kê A/B Test, P-Value, Cỡ mẫu MDE** | [`scripts/lib/ab_test_evaluator.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/ab_test_evaluator.py) | Chạy `./.venv/bin/python scripts/lib/ab_test_evaluator.py`. |
| **Hiệu suất 7 ngày SERP, Biến động Tăng/Giảm** | [`scripts/sync_7d_performance_report.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_7d_performance_report.py) | Chạy `./.venv/bin/python scripts/sync_7d_performance_report.py`. |
| **Sổ cái Quyết định, Đối soát Closed-Loop** | [`scripts/track_decisions.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/track_decisions.py) | Chạy `./.venv/bin/python scripts/track_decisions.py`. |
| **Truy vấn Đa chiều, Phễu W2A, Market Sizing** | [`scripts/query_analytics.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/query_analytics.py) | Phễu: `--funnel <hub>` - Market Sizing: `--market-sizing <keyword>` - SQL: `--sql <query>`. |
| **Từ điển Ngữ nghĩa Dữ liệu SSOT (Semantic Layer)** | [`07_REPORTS/data/data_mart_semantic_dictionary.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/data_mart_semantic_dictionary.json) | Đọc định nghĩa công thức SQL, benchmark W2A CVR, AOV và tỷ lệ hoa hồng chuẩn. |
| **Mẫu Đề xuất Hợp tác Đối tác Thương mại (BD Pitch)** | [`06_USE_CASE_MOMO/templates/partner_pitch_blueprint.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/templates/partner_pitch_blueprint.md) | Khung tài liệu 6 phần chuẩn mực gửi đối tác thương mại bên ngoài. |
| **Mô phỏng Kịch bản What-If, Cắt giảm Ads, CTR Lift** | [`scripts/lib/scenario_simulator.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/scenario_simulator.py) | Chạy `./.venv/bin/python scripts/lib/scenario_simulator.py`. |
| **Dự báo Mùa vụ, Ngoại suy Đa kịch bản** | [`scripts/lib/forecast_engine.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/forecast_engine.py) | Chạy `./.venv/bin/python scripts/lib/forecast_engine.py`. |
| **Paid Ads, Kênh Media, UTM Campaigns** | [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json) | Đọc JSON SSOT (snapshot cuối từ API cũ - sync_paid_ads.py đã archive do policy cấm GA4 API). |
| **Lịch mùa vụ, Phân tích Google Trends** | [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json) | Đọc JSON SSOT hoặc chạy `./.venv/bin/python scripts/theme_seasonality.py`. |
| **Báo cáo Tuần/Tháng, Hiệu suất MTD, Target** | [`07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md) | Chỉ đọc khi cần làm báo cáo/phân tích số liệu kỳ hiện tại. |
| **Tổng Hợp Doanh Thu GMV (Cinema, InsurTech, eSIM)** | [`07_REPORTS/docs/WEB_PLATFORM_GMV_2026.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/WEB_PLATFORM_GMV_2026.md) | SSOT doanh số GMV thực tế 2026. Data JSON tại `07_REPORTS/data/analytics/web_gmv_2026.json`. |
| **Tiêu chuẩn Báo cáo Tháng (Executive 6 Streams SSOT)** | [`.agents/skills/web-platform-reporting/SKILL.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/.agents/skills/web-platform-reporting/SKILL.md) | Đọc khi soạn thảo hoặc review báo cáo tháng cấp Ban Giám Đốc. |
| **Quy chuẩn trình bày báo cáo, slide, agenda, tag R/D/F** | [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md) | Đọc bắt buộc trước khi dựng slide/deck báo cáo cấp công ty. |
| **Glossary Báo cáo, Chuẩn hóa Thuật ngữ** | [`03_SKILLS/momo-reporting-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-glossary.md) | Tra cứu từ điển thuật ngữ, chỉ số, cấm kỵ và quy chuẩn hành văn. |
| **Chỉ đạo Lãnh đạo, Quyết định chiến lược** | [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md) + archive `MEETING_RECAPS_<year>-Q<quarter>.md` | File chính chỉ chứa quý hiện hành; chiến lược cũ hơn đọc đúng file archive theo quý. |
| **Cinema Hub Roadmap, BU Movies Collab, Minigames** | [`scripts/sync_cinema_roadmap_sheet.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_cinema_roadmap_sheet.py) | Chạy `./.venv/bin/python scripts/sync_cinema_roadmap_sheet.py` (Sheet ID `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`). |
| **Pipeline Tác vụ Agent, Giao việc Hiến sang Hub /agent** | [`scripts/sync_agent_tasks.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_agent_tasks.py) | Chạy `./.venv/bin/python scripts/sync_agent_tasks.py`. |
| **BRD/PRD Use Case (Vay Nhanh, VTS, BHYT, eSIM...)** | [`06_USE_CASE_MOMO/<use-case>-brd.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/) | Chỉ đọc đúng file BRD của use case được hỏi. |
| **Tài liệu Hub (Strategy, Navigation, Performance)** | [`05_HUBS/<hub-name>/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/) | Chỉ đọc đúng thư mục Hub tương ứng. |
| **Kiểm tra độ mới tri thức, Registry** | [`00_HARNESS_CORE/knowledge_freshness.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/knowledge_freshness.md) | Chạy `./.venv/bin/python scripts/check_knowledge_freshness.py`. |
| **Đường dẫn tham chiếu lỗi, Link gãy trong repo** | [`00_HARNESS_CORE/knowledge_conflicts.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/knowledge_conflicts.md) | Chạy `./.venv/bin/python scripts/detect_knowledge_conflicts.py`. |
| **Kiểm chứng số liệu, Evidence, Chống hallucination** | [`00_HARNESS_CORE/EVIDENCE_CONTRACT.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/EVIDENCE_CONTRACT.md) | Đọc khi trả lời có số liệu/kết luận thực tế quan trọng; validate evidence JSON qua `./.venv/bin/python scripts/validate_evidence.py`. |
| **Phân tích Growth, Đầu tư use case, Scale/Kill, Phân bổ nguồn lực** | [`00_HARNESS_CORE/GROWTH_PRINCIPLES.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/GROWTH_PRINCIPLES.md) + skill `business-growth` | Đọc playbook trước khi tư vấn; mọi phân tích định lượng phải chạy tool chuyên biệt (mục 4 playbook), không ước lượng bằng model. |
| **Benchmark, Baseline CVR/Funnel, So sánh hiệu suất** | `./.venv/bin/python scripts/build_benchmarks.py` → `07_REPORTS/data/benchmarks/web_growth_benchmarks.json` | Chạy lại script nếu `as_of` cũ hơn kỳ đang phân tích; cấm so sánh cảm tính không có baseline. |
| **Báo cáo tuần W##, Báo cáo tháng, MBR Board** | [`07_REPORTS/docs/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/INDEX.md) | Đọc INDEX trước để xác định đúng file theo kỳ (weekly-report-YYYY-MM-DD-..., report-thang-XX-2026-board.md); KHÔNG load toàn bộ `07_REPORTS/docs/`. Template: `07_REPORTS/templates/monthly_report_template.md`; chuẩn trình bày: skill `web-platform-reporting`. |
| **Content Plan, Keyword Cluster, Content Inventory** | [`06_USE_CASE_MOMO/content-plans/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/content-plans/INDEX.md) + [`05_HUBS/inventory/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) | Đọc INDEX chọn đúng use-case folder; keyword inventory đọc đúng CSV của Hub; skill `content-plan-architect` chứa quy chuẩn 7 tầng. |

---

## ⚡ QUY CHUẨN KỸ THUẬT & TRUY XUẤT CỐT LÕI (SSOT POINTERS)

- **Python Runtime SSOT:** Mọi script Python chạy qua `./.venv/bin/python <script>` (Python 3.12). Cấm `python3` trần.
- **Automated Triggers:**
  - "tracking report mới nhất" → `sync_tracking_report.py` (quét Excel mới nhất từ Downloads).
  - "GA4 / GA4 MTD / sync mtd" → `scripts/ingest_ga4_daily.py` (quét file CSV xuất từ GA4 Explore trong `~/Downloads/`, cộng dồn vào MTD, cập nhật Excel, JSON SSOT và Hubs Dashboard. Bỏ hoàn toàn gọi GA4 API).
  - "sync report / đối chiếu report" → đọc `07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md` + `performance.sqlite` (sync_hybrid_report.py đã archive do policy cấm GA4 API).
  - "sync GSC / Search Console / ingest GSC MTD" → `./.venv/bin/python scripts/ingest_gsc_mtd.py` (Sheet `18yAcvhcA6YEx1TiqF5KsH40LmJBlkqN` tab `SAS_*` mới nhất, hoặc truyền ZIP/URL + `--start/--end`).
  - "thiết lập GTM / tracking GTM" → đọc `04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md`; chỉ chạy `node scripts/auth_gtm.js` khi cần OAuth/refresh token.
  - "URL tăng/giảm, top pages, breakout" → đọc Data Mart `07_REPORTS/data/performance.sqlite` qua `scripts/query_analytics.py` hoặc `page_mtd.json`; KHÔNG gọi GA4/GSC API.
  - "URL chết, mất impressions, 404/301" → check HTTP status trực tiếp + đối chiếu `page_mtd.json`/`gsc_mtd_performance_2026.json` (data GSC mới nhất từ Sheet); script `analyze_*impressions*` đã chết cùng GSC API.
  - "sync hub / data hub / lệnh hub" → `sync_inventory_to_hubs.py` + `sync_data_to_hubs_dashboard.py`; `sync_<hub>_<ky>.py` chỉ khi user chỉ định đúng hub + kỳ.
  - "kiểm chứng số liệu / evidence / fact-check" → đọc `00_HARNESS_CORE/EVIDENCE_CONTRACT.md`, build evidence JSON và chạy `./.venv/bin/python scripts/validate_evidence.py`.
  - "số liệu GA4 nhanh / event trên page X" → đọc Data Mart `performance.sqlite` (`scripts/query_analytics.py`) hoặc `page_mtd.json`; CẤM gọi GA4 API (skill `ad-hoc-ga4-query` đã deprecated cùng policy).
  - "check GTM / tag trigger version GTM" → `./.venv/bin/python scripts/gtm_inspect.py` (xem skill `gtm-inspect`).
  - "phân tích growth / nên đầu tư / use case nào tiềm năng / scale hay kill" → đọc `00_HARNESS_CORE/GROWTH_PRINCIPLES.md` + skill `business-growth`; chạy tool chuyên biệt trước khi kết luận.
  - Mặc định an toàn: không tự push GitHub Hubs (`main`) trừ khi có cờ `--push-hubs`.
- **Hub Sync Safety:** Không chạy 2 tiến trình sync Hub song song; trước khi chạy check `git -C "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo" status` phải sạch. Các orchestrator còn sống (`sync_data_to_hubs_dashboard`, `sync_all_data`...) đã có lock `scripts/lib/hub_sync_lock.py` - tiến trình thứ 2 tự exit 2 (TTL 2h, lock file `07_REPORTS/data/cache/hub_sync.lock`). Lock chỉ phủ repo này; nếu user đang sửa tay repo React thì cảnh báo trước.
- **Google Sheets SSOT:** Web Platform Report `1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU`; Cinema Hub Roadmap `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`.
- **Traffic SSOT:** Mọi báo cáo lưu lượng bắt buộc tách Non-Paid (`Organic`, `Direct`, `AI Traffic (GEO)`, `Referral`) vs Paid thành 2 dòng tổng kèm tỷ trọng %.
- **Báo cáo Tuần/Tháng:** Chuẩn SSOT tại `.agents/skills/web-platform-reporting/SKILL.md` + `03_SKILLS/momo-reporting-guidelines.md` - lazy load khi cần.
- **Anti-Hallucination (Bắt buộc):**
  - Phân tầng nghiêm ngặt, không trộn: `fact` (truy được về file/số liệu gốc + kỳ dữ liệu) / `inference` (ghi rõ "suy luận từ...") / `recommendation`. Cấm nêu suy luận như fact.
  - Mọi con số trong câu trả lời phải truy về source cụ thể (file JSON/MD/script output); không truy được → ghi `[cần verify]`, TUYỆT ĐỐI không bịa số, bịa hoàn cảnh, bịa diễn biến.
  - Thiếu dữ liệu để kết luận → nói thẳng "không đủ dữ liệu, cần kiểm tra X" thay vì diễn giải.
  - Câu trả lời/báo cáo chứa số liệu quan trọng: đóng gói evidence JSON theo `00_HARNESS_CORE/EVIDENCE_CONTRACT.md` và chạy `./.venv/bin/python scripts/validate_evidence.py` trước khi trình bày.
- **Quản trị file này:** Routing table tối đa ~40 rows, row mới ≤2 dòng, ưu tiên gộp vào row hiện có; nếu file >24KB thì tách phần mở rộng sang file riêng và để pointer ở đây.

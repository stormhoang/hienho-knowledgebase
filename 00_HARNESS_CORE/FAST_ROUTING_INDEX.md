# FAST ROUTING INDEX & DATA SSOT ROUTING (SSOT)

File này được tách từ `AGENTS.md` để giữ AGENTS.md dưới ngưỡng inject 16KB.
Khi cần định tuyến file SSOT hoặc tra cứu data theo intent, đọc file này.

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
| **Hiệu suất 7 ngày SERP, Biến động Tăng/Giảm** | [`scripts/query_analytics.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/query_analytics.py) + `07_REPORTS/data/performance.sqlite` | `sync_7d_performance_report.py` đã archive (GA4 API dead); dùng `--sql` so sánh 2 cửa sổ 7 ngày trên Data Mart. |
| **Sổ cái Quyết định, Đối soát Closed-Loop** | [`scripts/track_decisions.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/track_decisions.py) | Chạy `./.venv/bin/python scripts/track_decisions.py`. |
| **Truy vấn Đa chiều, Phễu W2A, Market Sizing** | [`scripts/query_analytics.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/query_analytics.py) | Phễu: `--funnel <hub>` - Market Sizing: `--market-sizing <keyword>` - SQL: `--sql <query>`. |
| **Từ điển Ngữ nghĩa Dữ liệu SSOT (Semantic Layer)** | [`07_REPORTS/data/data_mart_semantic_dictionary.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/data_mart_semantic_dictionary.json) | Đọc định nghĩa công thức SQL, benchmark W2A CVR, AOV và tỷ lệ hoa hồng chuẩn. |
| **Mẫu Đề xuất Hợp tác Đối tác Thương mại (BD Pitch)** | [`06_USE_CASE_MOMO/templates/partner_pitch_blueprint.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/templates/partner_pitch_blueprint.md) | Khung tài liệu 6 phần chuẩn mực gửi đối tác thương mại bên ngoài. |
| **Mô phỏng Kịch bản What-If, Cắt giảm Ads, CTR Lift** | [`scripts/lib/scenario_simulator.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/scenario_simulator.py) | Chạy `./.venv/bin/python scripts/lib/scenario_simulator.py`. |
| **Dự báo Mùa vụ, Ngoại suy Đa kịch bản** | [`scripts/lib/forecast_engine.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/forecast_engine.py) | Chạy `./.venv/bin/python scripts/lib/forecast_engine.py`. |
| **Paid Ads, Kênh Media, UTM Campaigns** | [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json) + [`scripts/ingest_paid_ads.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/ingest_paid_ads.py) | Đọc JSON SSOT; nạp data mới từ GA4 Explore CSV: `./.venv/bin/python scripts/ingest_paid_ads.py` (spec export xem skill `paid-ads`). |
| **Lịch mùa vụ, Phân tích Google Trends** | [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json) | Đọc JSON SSOT hoặc chạy `./.venv/bin/python scripts/theme_seasonality.py`. |
| **Báo cáo Tuần/Tháng, Hiệu suất MTD, Target** | [`07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md) | Chỉ đọc khi cần làm báo cáo/phân tích số liệu kỳ hiện tại. |
| **Tổng Hợp Doanh Thu GMV (Cinema, InsurTech, eSIM)** | [`07_REPORTS/docs/WEB_PLATFORM_GMV_2026.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/WEB_PLATFORM_GMV_2026.md) | SSOT doanh số GMV thực tế 2026. Data JSON tại `07_REPORTS/data/analytics/web_gmv_2026.json`. |
| **Tiêu chuẩn Báo cáo Tháng (Executive 6 Streams SSOT)** | [`.agents/skills/web-platform-reporting/SKILL.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/.agents/skills/web-platform-reporting/SKILL.md) | Đọc khi soạn thảo hoặc review báo cáo tháng cấp Ban Giám Đốc. |
| **Quy chuẩn trình bày báo cáo, slide, agenda, tag R/D/F** | [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md) | Đọc bắt buộc trước khi dựng slide/deck báo cáo cấp công ty. |
| **Glossary Báo cáo, Chuẩn hóa Thuật ngữ** | [`03_SKILLS/momo-reporting-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-glossary.md) | Tra cứu từ điển thuật ngữ, chỉ số, cấm kỵ và quy chuẩn hành văn. |
| **Chỉ đạo Lãnh đạo, Quyết định chiến lược** | [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/meetings/MEETING_RECAPS.md) + archive `MEETING_RECAPS_<year>-Q<quarter>.md` | File chính chỉ chứa quý hiện hành; chiến lược cũ hơn đọc đúng file archive theo quý. |
| **Cinema Hub Roadmap, BU Movies Collab, Minigames** | [`scripts/sync_cinema_roadmap_sheet.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_cinema_roadmap_sheet.py) | Chạy `./.venv/bin/python scripts/sync_cinema_roadmap_sheet.py` (Sheet ID `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`). |
| **Pipeline Tác vụ Agent, Giao việc Hiến sang Hub /agent** | [`scripts/sync_agent_tasks.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_agent_tasks.py) | Chạy `./.venv/bin/python scripts/sync_agent_tasks.py`. |
| **BRD/PRD Use Case (Vay Nhanh, VTS, BHYT, eSIM...)** | [`06_USE_CASE_MOMO/<use-case>-brd.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/) | Chỉ đọc đúng file BRD của use case được hỏi. |
| **Tài liệu Hub (Strategy, Navigation, Performance)** | [`05_HUBS/<hub-name>/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/) | Chỉ đọc đúng thư mục Hub tương ứng. |
| **Kiểm tra độ mới tri thức, Registry** | [`00_HARNESS_CORE/knowledge_freshness.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/knowledge_freshness.md) | Chạy `./.venv/bin/python scripts/check_knowledge_freshness.py`. |
| **Đường dẫn tham chiếu lỗi, Link gãy trong repo** | [`00_HARNESS_CORE/knowledge_conflicts.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/knowledge_conflicts.md) | Chạy `./.venv/bin/python scripts/detect_knowledge_conflicts.py` (thêm `--max-broken N` để fail khi link gãy mới; pre-commit đã enforce baseline 3). |
| **Toolchain quản trị tri thức (triage, provenance, inventory, log)** | `scripts/triage_knowledge_conflicts.py`, `scripts/generate_knowledge_provenance.py`, `scripts/inventory_knowledge_base.py`, `00_HARNESS_CORE/KNOWLEDGE_LOG.md` | Chạy tuần tự khi audit knowledge layer; mọi thay đổi knowledge page phải ghi 1 dòng vào `KNOWLEDGE_LOG.md`. |
| **Kiểm chứng số liệu, Evidence, Chống hallucination** | [`00_HARNESS_CORE/EVIDENCE_CONTRACT.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/EVIDENCE_CONTRACT.md) | Đọc khi trả lời có số liệu/kết luận thực tế quan trọng; validate evidence JSON qua `./.venv/bin/python scripts/validate_evidence.py`. |
| **Phân tích Growth, Đầu tư use case, Scale/Kill, Phân bổ nguồn lực** | [`00_HARNESS_CORE/GROWTH_PRINCIPLES.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/GROWTH_PRINCIPLES.md) + skill `business-growth` | Đọc playbook trước khi tư vấn; mọi phân tích định lượng phải chạy tool chuyên biệt (mục 4 playbook), không ước lượng bằng model. |
| **Benchmark, Baseline CVR/Funnel, So sánh hiệu suất** | `./.venv/bin/python scripts/build_benchmarks.py` → `07_REPORTS/data/benchmarks/web_growth_benchmarks.json` | Chạy lại script nếu `as_of` cũ hơn kỳ đang phân tích; cấm so sánh cảm tính không có baseline. |
| **Báo cáo tuần W##, Báo cáo tháng, MBR Board** | [`07_REPORTS/docs/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/INDEX.md) | Đọc INDEX trước để xác định đúng file theo kỳ (weekly-report-YYYY-MM-DD-..., report-thang-XX-2026-board.md); KHÔNG load toàn bộ `07_REPORTS/docs/`. Template: `07_REPORTS/templates/monthly_report_template.md`; chuẩn trình bày: skill `web-platform-reporting`. |
| **Content Plan, Keyword Cluster, Content Inventory** | [`06_USE_CASE_MOMO/content-plans/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/content-plans/INDEX.md) + [`05_HUBS/inventory/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) | Đọc INDEX chọn đúng use-case folder; keyword inventory đọc đúng CSV của Hub; skill `content-plan-architect` chứa quy chuẩn 7 tầng. |

### BẢNG TRA CỨU NHANH DATA SSOT (DATA QUERY ROUTING)

Khi user hỏi số liệu, agent tra bảng này TRƯỚC, đọc đúng file/command, không đoán path, không đọc file lớn:

| Câu hỏi / Intent | Nguồn SSOT đích | Cách truy vấn nhanh |
| :--- | :--- | :--- |
| Traffic, sessions, PV theo ngày/hub/W2A funnel | `07_REPORTS/data/performance.sqlite` | `./.venv/bin/python scripts/query_analytics.py --funnel <hub>` / `--sql <query>` / `--market-sizing <kw>` |
| Chẩn đoán tăng/giảm, anomaly, pacing MTD | `performance.sqlite` + `07_REPORTS/data/monthly/monthly_*_mtd_*d.json` (mới nhất) | `diagnose_performance.py`, `detect_anomalies.py` |
| GSC clicks/impressions/position theo page MTD | `07_REPORTS/data/analytics/page_mtd.json` + `gsc_mtd_performance_2026.json` | Đọc JSON trực tiếp (ingest qua `ingest_gsc_mtd.py`) |
| Paid Ads, kênh media, UTM, CVR W2A | `07_REPORTS/data/analytics/paid_ads_performance.json` | Đọc JSON (ingest qua `ingest_paid_ads.py` từ GA4 Explore CSV) |
| GA4 raw daily theo page×channel | `07_REPORTS/data/ga4_daily/YYYY-MM-DD.csv` | Đọc CSV ngày cụ thể |
| MTD tổng PV/sessions/channels mới nhất | `07_REPORTS/data/monthly/monthly_<YYYY-MM>_mtd_*d.json` (file có số ngày lớn nhất của tháng hiện tại) + `07_REPORTS/data/summary.json` | Đọc file MTD mới nhất |
| URL → Project/Theme/Hub mapping | `07_REPORTS/data/url_project_mapping.json` + `web_dim_page_url.csv` | `scripts/lib/url_project_resolver.py`, `theme_matcher.py` |
| Keyword clusters, content plan | `07_REPORTS/data/inventory_clusters_summary.json` + `05_HUBS/inventory/<hub>/` | `generate_content_plan.py` |
| Mùa vụ, trends theo theme | `07_REPORTS/data/theme_seasonality.json` | `theme_seasonality.py`, `forecast_engine.py` |
| URL inventory live, zero-traffic | `07_REPORTS/data/momo_live_urls.json` | `validate_seo_pipeline.py` |
| SEO news, trending topics | `07_REPORTS/data/seo_news_latest.json` / `seo_news_enriched.json` | `sync_seo_news.py` |
| Lost impressions → zero impressions → audit 404/301 | `gsc_lost_impressions_detail.json` → `gsc_zero_impression_analysis.json` | `audit_actionable_urls.py` (chạy lost trước) |
| GTM tags/triggers/variables live | Container `GTM-P9JDDJZ` | Skill `gtm-inspect` + `scripts/gtm_inspect.py` (read-only) |
| Event schema, tracking params | `04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md` | Đọc doc, không query API |
| Ads segment taxonomy | `04_MOSPARK_PLATFORM/data/ads_segments.json` + `ADS_SEGMENT_DICTIONARY.md` | `generate_ads_segments.py` |
| Tài chính/FinHub YTD | `historical_ga4_gsc_t1_t4_2026.json` + monthly full_month | `calc_finhub_ytd_perf.py` (đọc Google Sheet) |


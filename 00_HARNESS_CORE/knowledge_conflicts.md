# Báo Cáo Xung Đột & Kiểm Tra Đường Dẫn Kho Tri Thức (Knowledge Conflict Report)

- Thời điểm xuất bản: 2026-11-07T13:12:54.414500+00:00
- Chế độ vận hành: observe (Không tự ý sửa đổi mã nguồn)
- Tổng số điểm phát hiện: 64

## 1. Bảng Tổng Hợp Phân Loại

| Phân loại | Số lượng | Ý nghĩa & Mô tả |
| :--- | ---: | :--- |
| `broken_reference` | 5 | Đường dẫn nội bộ không tìm thấy tệp đích |
| `external_reference` | 37 | Tham chiếu sang repo khác, thư mục Downloads hoặc Obsidian |
| `code_path_reference` | 21 | Đường dẫn trong mã nguồn; có thể là tệp sinh runtime |
| `skill_asset_reference` | 1 | Tài nguyên thuộc các gói Agent Skill |

## 2. Nguyên Tắc Xử Lý

- Báo cáo này hoàn toàn mang tính chất kiểm kê và phân loại (observe).
- Tuyệt đối không tự động xóa, đổi tên hoặc hợp nhất nguồn khi chưa có phê duyệt từ Web Product Lead.

## 3. Danh Sách Chi Tiết Theo Tệp Tin Nguồn

### `.agents/rules/graphify.md`

- **Dòng 12:** `graphify-out/wiki/index.md`
  * Phân loại: `skill_asset_reference` | Mã lý do: `skill_package_reference`
  * Chi tiết: Tham chiếu tài nguyên cục bộ bên trong gói agent skill.

### `.agents/skills/sync-all/SKILL.md`

- **Dòng 43:** `react-web-momo/data/seo-news.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `00_HARNESS_CORE/KEYWORD_CLUSTERING_OPTIMIZATION_SPEC.md`

- **Dòng 50:** `data/seo-clusters/index.json`
  * Phân loại: `broken_reference` | Mã lý do: `unresolved_internal_path`
  * Chi tiết: Đường dẫn nội bộ không tìm thấy tệp đích trong repository.

### `00_HARNESS_CORE/hienho_master_doc.md`

- **Dòng 2575:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/01_STRATEGIC_PLAN/mospark-growth-master-plan.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).
- **Dòng 2579:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/01_STRATEGIC_PLAN/seo-geo-direction.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).
- **Dòng 2583:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/01_STRATEGIC_PLAN/momo-content-plan-strategy.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).
- **Dòng 2587:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/01_STRATEGIC_PLAN/web_growth_strategy_brd.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).

### `00_HARNESS_CORE/web_platform_introduction.md`

- **Dòng 6:** `/c:/Klaus/hienho-knowledgebase/00_HARNESS_CORE/hienho_master_doc.md`
  * Phân loại: `external_reference` | Mã lý do: `outside_repository`
  * Chi tiết: Đường dẫn tuyệt đối trỏ ra ngoài phạm vi repository.
- **Dòng 6:** `/c:/Klaus/hienho-knowledgebase/01_STRATEGIC_PLAN/web_growth_strategy_brd.md`
  * Phân loại: `external_reference` | Mã lý do: `outside_repository`
  * Chi tiết: Đường dẫn tuyệt đối trỏ ra ngoài phạm vi repository.

### `04_MOSPARK_PLATFORM/QUIZ_FLOW_SPECIFICATION_FOR_DEV.md`

- **Dòng 233:** `./lib/data/quiz_catalog.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `04_MOSPARK_PLATFORM/mospark_rag_knowledge_base.md`

- **Dòng 310:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_master.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).
- **Dòng 311:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_plg_project.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).
- **Dòng 312:** `/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_genai_content.md`
  * Phân loại: `external_reference` | Mã lý do: `historical_vault_reference`
  * Chi tiết: Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault).

### `05_HUBS/vehicle/vehicle-hub-brd.md`

- **Dòng 1006:** `05_HUBS/vehicle-hub-navigation.md`
  * Phân loại: `broken_reference` | Mã lý do: `unresolved_internal_path`
  * Chi tiết: Đường dẫn nội bộ không tìm thấy tệp đích trong repository.

### `06_USE_CASE_MOMO/trust-brd.md`

- **Dòng 57:** `/Users/hienhv/Downloads/An Toan MoMo - Landing (standalone) (1).html`
  * Phân loại: `external_reference` | Mã lý do: `external_downloads_artifact`
  * Chi tiết: Tham chiếu tệp tin tạm hoặc báo cáo xuất trong thư mục Downloads máy cục bộ.
- **Dòng 124:** `/Users/hienhv/Downloads/An Toan MoMo - Landing (standalone) (1).html`
  * Phân loại: `external_reference` | Mã lý do: `external_downloads_artifact`
  * Chi tiết: Tham chiếu tệp tin tạm hoặc báo cáo xuất trong thư mục Downloads máy cục bộ.
- **Dòng 228:** `/Users/hienhv/Downloads/An Toan MoMo - Landing (standalone) (1).html`
  * Phân loại: `external_reference` | Mã lý do: `external_downloads_artifact`
  * Chi tiết: Tham chiếu tệp tin tạm hoặc báo cáo xuất trong thư mục Downloads máy cục bộ.

### `07_REPORTS/KEYWORD_REALLOCATION_REVIEW.md`

- **Dòng 160:** `data/content-plan-data.json`
  * Phân loại: `broken_reference` | Mã lý do: `unresolved_internal_path`
  * Chi tiết: Đường dẫn nội bộ không tìm thấy tệp đích trong repository.

### `07_REPORTS/docs/monthly-reporting-tool-architecture.md`

- **Dòng 106:** `lib/dashboard/web-data.json`
  * Phân loại: `broken_reference` | Mã lý do: `unresolved_internal_path`
  * Chi tiết: Đường dẫn nội bộ không tìm thấy tệp đích trong repository.

### `13_INTAKE/README.md`

- **Dòng 78:** `lib/dashboard/web-data.json`
  * Phân loại: `broken_reference` | Mã lý do: `unresolved_internal_path`
  * Chi tiết: Đường dẫn nội bộ không tìm thấy tệp đích trong repository.

### `AGENTS.md`

- **Dòng 88:** `/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/web-data.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 88:** `/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/summary.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 93:** `/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/web-data.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 93:** `/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/summary.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `CODEBASE_MANIFEST.md`

- **Dòng 39:** `cache/performance.sqlite`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/archive/sync_mtd_22.py`

- **Dòng 26:** `Idea/react-web-momo/data/analytics/summary.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/auth_gtm.js`

- **Dòng 7:** `gemini/config/mcp_config.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).
- **Dòng 109:** `gemini/config/mcp_config.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/build_october_facts.py`

- **Dòng 13:** `react-web-momo/lib/dashboard/web-data.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 14:** `react-web-momo/lib/dashboard/hub-map.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/cron_gsc_cannibalization.py`

- **Dòng 9:** `07_REPORTS/data/gsc_cannibalization_matrix.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/cron_gsc_crawl_stats.py`

- **Dòng 8:** `07_REPORTS/data/gsc_crawl_stats.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/cron_gsc_keyword_ranking.py`

- **Dòng 9:** `07_REPORTS/data/gsc_keyword_ranking.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/detect_knowledge_conflicts.py`

- **Dòng 144:** `cache/performance.sqlite`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/intake.py`

- **Dòng 225:** `lib/dashboard/web-data.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/lib/hubs_dashboard.py`

- **Dòng 3:** `lib/dashboard/web-data.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/lib/url_project_resolver.py`

- **Dòng 32:** `Idea/react-web-momo/lib/dashboard/hub-map.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/scratch_fix_platform.py`

- **Dòng 84:** `Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/scratch_fix_v2.py`

- **Dòng 31:** `Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/scratch_human_report.py`

- **Dòng 324:** `Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/scratch_strict_audit_report.py`

- **Dòng 290:** `Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/sync_7d_performance_report.py`

- **Dòng 15:** `react-web-momo/data/analytics/gsc_7d_performance.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 17:** `data/reports/index.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).
- **Dòng 263:** `react-web-momo/data/reports/index.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/sync_all_data.py`

- **Dòng 10:** `data/seo-news.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).
- **Dòng 130:** `data/seo-news.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).
- **Dòng 141:** `data/ga4/landing-pages.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/sync_breakout_to_hubs.py`

- **Dòng 14:** `data/analytics/gsc_breakout_pages_7d.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).
- **Dòng 17:** `data/reports/weekly-report-2026-10-26-11-01.md`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).
- **Dòng 19:** `react-web-momo/lib/dashboard/web-data.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/sync_data_mart.py`

- **Dòng 29:** `Idea/react-web-momo/lib/dashboard/hub-map.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/sync_data_to_hubs_dashboard.py`

- **Dòng 9:** `react-web-momo/lib/dashboard/summary.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 10:** `react-web-momo/lib/dashboard/web-data.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 11:** `react-web-momo/data/analytics/ga4-w2a-attribution.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 12:** `react-web-momo/lib/dashboard/hub-map.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).

### `scripts/sync_ga4_to_hubs.py`

- **Dòng 5:** `data/ga4/landing-pages.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/sync_hybrid_report.py`

- **Dòng 312:** `lib/dashboard/summary.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/sync_inventory_to_hubs.py`

- **Dòng 1318:** `data/seo-clusters/index.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/sync_roadmap_to_supabase.py`

- **Dòng 19:** `Idea/react-web-momo/data/roadmap.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 113:** `data/roadmap.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/sync_seo_news.py`

- **Dòng 6:** `data/seo-news.json`
  * Phân loại: `code_path_reference` | Mã lý do: `code_runtime_or_generated_path`
  * Chi tiết: Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output).

### `scripts/update_all_october_reports_30d.py`

- **Dòng 12:** `react-web-momo/data/analytics/monthly-report-2026-10.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 13:** `react-web-momo/data/reports/monthly-index.json`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).
- **Dòng 16:** `react-web-momo/data/reports/report-thang-10-2026-board.md`
  * Phân loại: `external_reference` | Mã lý do: `cross_repository_reference`
  * Chi tiết: Tham chiếu liên kết sang repository Front-end Hub (react-web-momo).


# BÁO CÁO KIỂM SOÁT ĐỘ MỚI NGUỒN TRI THỨC (KNOWLEDGE FRESHNESS SSOT)

> **Thời điểm đối chiếu:** 2026-11-07 | **Chế độ:** observe | **Tổng số nguồn:** 27 | **Nguồn có hạn định:** 5

---

## I. KẾT LUẬN TRỰC DIỆN (ACTION TITLE)
> **Hệ thống giám sát phát hiện 2 nguồn đạt chuẩn độ mới, 0 nguồn trong biên độ bù trễ, và 3 nguồn đã cũ vượt ngưỡng khuyến nghị. Đã kích hoạt cơ chế nhận diện lệch kỳ nhằm ngăn chặn hoàn toàn việc nhầm lẫn giữa thời điểm sửa đổi tệp và kỳ dữ liệu thực tế.**

---

## II. BẰNG CHỨNG & DỮ KIỆN ĐỘ MỚI (WHAT)

### 1. Bảng theo dõi các nguồn dữ liệu có hạn định thời gian

| ID Nguồn | Đường dẫn | Kỳ dữ liệu | Data As Of | Ngày sửa tệp | Tuổi DL | Lệch mtime | Ngưỡng | Trạng thái |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `performance_tracking_master` | [WEB_PERFORMANCE_TRACKING_MASTER.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) | GSC Export 2026-10-10 | 2026-10-10 | 2026-11-06 | 28 ngày | 27 ngày | 7 ngày | 🔴 Đã cũ (Stale) |
| `performance_data_mart` | [performance.sqlite](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/cache/performance.sqlite) | MTD 2026-11 (cắt ngày 2026-11-04) | 2026-11-04 | 2026-11-05 | 3 ngày | 1 ngày | 7 ngày | 🟢 Đạt chuẩn (Fresh) |
| `performance_snapshot_latest` | [PERFORMANCE_SNAPSHOT_LATEST.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md) | Tháng 10/2026 (MTD 9 ngày: 01/10 - 09/10/2026) | 2026-10-10 | 2026-11-07 | 28 ngày | 28 ngày | 7 ngày | 🔴 Đã cũ (Stale) |
| `paid_ads_performance` | [paid_ads_performance.json](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json) | 2026-10-01 đến today | 2026-10-25 | 2026-10-25 | 13 ngày | 0 | 7 ngày | 🔴 Đã cũ (Stale) |
| `theme_seasonality` | [theme_seasonality.json](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json) | today 5-y (cập nhật 2026-10-23) | 2026-10-23 | 2026-10-23 | 15 ngày | 0 | 30 ngày | 🟢 Đạt chuẩn (Fresh) |

### 2. Danh mục nguồn quy chuẩn & lịch sử (Normative & Historical)

| ID Nguồn | Miền (Domain) | Đội ngũ phụ trách | Vai trò | Trạng thái | Kỳ dữ liệu ghi nhận |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `agent_operating_contract` | `agent_governance` | Web Product Lead | primary | active | Không xác định |
| `agent_capabilities` | `agent_governance` | Web Product Lead | primary | active | Không xác định |
| `agent_safety_contract` | `agent_governance` | Web Product Lead | primary | active | Không xác định |
| `agent_output_contract` | `agent_governance` | Web Product Lead | primary | active | Không xác định |
| `evidence_contract` | `evidence` | Web Product Lead | primary | active | Không xác định |
| `team_scope_of_work` | `agent_governance` | Web Product Lead | primary | active | Không xác định |
| `hienho_master_doc` | `agent_governance` | Web Product Lead | reference | active | Không xác định |
| `knowledge_routing` | `knowledge_routing` | Web Product Lead | primary | active | Không xác định |
| `codebase_manifest` | `knowledge_routing` | Web Product Lead | primary | active | Không xác định |
| `orchestrator_engine` | `orchestration` | Web Product Lead | primary | active | Không xác định |
| `dispatch_readme` | `orchestration` | Web Product Lead | primary | active | Không xác định |
| `vocabulary_glossary` | `language_governance` | Web Product Lead | primary | active | Không xác định |
| `decision_log` | `decisions` | Web Product Lead | primary | active | Quyết định gần nhất (2026-10-14) |
| `roadmap_releases` | `roadmap` | Web Platform | primary | active | Bản ghi gần nhất (2026-10-30) |
| `utility_tracking` | `tracking` | SE Team / Thuận | primary | active | Không xác định |
| `cinema_hub_brd` | `hubs_cinema` | Cinema Hub Team | primary | active | Không xác định |
| `cinema_funnel_architecture` | `hubs_cinema` | Cinema Hub Team | primary | active | Không xác định |
| `vehicle_hub_brd` | `hubs_vehicle` | Vehicle Hub Team | primary | active | Không xác định |
| `financial_hub_brd` | `hubs_financial` | Financial Hub Team | primary | active | Không xác định |
| `mospark_rag_knowledge_base` | `mospark_platform` | SE Team / Duy | primary | active | Không xác định |
| `seo_execution_sop` | `frameworks_seo` | SEO Team | primary | active | Không xác định |
| `web_growth_strategy_historical` | `strategic_plan` | Web Product Lead | reference | historical | Dữ liệu đối chiếu lịch sử |

---

## III. PHÂN TÍCH RỦI RO & TÁC ĐỘNG NGHIỆP VỤ (SO WHAT)

1. **Rủi ro nhầm lẫn ngày commit với ngày số liệu (Mtime vs Data Drift):**
   - Khi lập trình viên hoặc AI Agent chạy lệnh git/sync/format, thuộc tính ngày sửa tệp trên ổ đĩa sẽ đổi sang ngày hiện tại.
   - Nếu hệ thống chỉ đọc ngày sửa tệp, Agent sẽ nhầm tưởng snapshot cũ (ví dụ: Snapshot Tháng 10 cắt ngày 10/10) là số liệu mới nhất của Tháng 11.
   - Giải pháp: Bắt buộc đọc trường `data_as_of` và `data_period` trực tiếp từ nội dung tệp.

2. **Tác động đến quyết định vận hành:**
   - Dữ liệu `performance_snapshot_latest` đang dừng ở mốc 10/10/2026 (cũ hơn 7 ngày so với hiện tại). Agent không được dùng số liệu này làm căn cứ chẩn đoán nhịp vận hành hiện tại.
   - Dữ liệu `performance_data_mart` (`performance.sqlite`) có mốc 04/11/2026, là nguồn tươi mới và hợp lệ để phân tích hiệu suất tuần 45.

---

## IV. KẾ HOẠCH XỬ LÝ & HƯỚNG DẪN AGENT (NOW WHAT)

1. **Quy tắc đọc nguồn cho Claude và Antigravity:**
   - Khi truy vấn miền `performance`, ưu tiên truy vấn `performance_data_mart` (`performance.sqlite`) hoặc chạy pipeline đối soát mới.
   - Nếu bắt buộc đọc `performance_snapshot_latest`, phải ghi rõ cảnh báo: *Số liệu trích xuất từ Snapshot Tháng 10/2026, không phản ánh nhịp vận hành Tháng 11*.
2. **Đồng bộ hóa trong pipeline:**
   - Chạy định kỳ `check_knowledge_freshness.py` trong CI để ngăn ngừa tình trạng trích dẫn dữ liệu quá hạn.

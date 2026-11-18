# BÁO CÁO NGUỒN GỐC & TÍNH TOÀN VẸN TRI THỨC (KNOWLEDGE PROVENANCE SSOT)

> **Thời điểm khởi tạo:** 2026-11-14T06:58:27.810705+00:00 | **Chế độ:** observe | **Tổng số nguồn:** 28 | **Xác thực thành công:** 28 | **Thuật toán băm:** sha256

---

## I. KẾT LUẬN TRỰC DIỆN (ACTION TITLE)
> **Hệ thống đã gắn định danh nguồn gốc hệ thống (System of Record), pipeline đồng bộ và mã kiểm tra tính toàn vẹn SHA-256 cho toàn bộ 28 nguồn tri thức SSOT. Cơ chế này bảo đảm tuyệt đối việc cả Claude và Antigravity đều đối chiếu và đọc trên cùng một phiên bản tệp chuẩn xác.**

---

## II. BẰNG CHỨNG NGUỒN GỐC & CHECKSUM (WHAT)

| ID Nguồn | Nguồn hệ thống gốc (System of Record) | Script sinh dữ liệu | Kỳ dữ liệu | Checksum (SHA-256) | Dung lượng |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `agent_operating_contract` | Antigravity Harness Governance | `manual_authoring` | Không xác định | `0d01145ad123...` | 1,854 B |
| `agent_capabilities` | Antigravity Harness Governance | `manual_authoring` | Không xác định | `7c602ba68bb1...` | 2,760 B |
| `agent_safety_contract` | Antigravity Harness Governance | `manual_authoring` | Không xác định | `2fab2d1b6074...` | 559 B |
| `agent_output_contract` | Antigravity Harness Governance | `manual_authoring` | Không xác định | `71b99d023313...` | 1,233 B |
| `evidence_contract` | Antigravity Evidence Verification System | `manual_authoring` | Không xác định | `c754baa205ba...` | 2,131 B |
| `team_scope_of_work` | Web Platform Organizational Charter | `manual_authoring` | Không xác định | `9ac2218f3ee0...` | 21,620 B |
| `hienho_master_doc` | Product Architecture & Strategy Master | `manual_authoring` | Không xác định | `d3799ab1c101...` | 218,539 B |
| `knowledge_routing` | Antigravity Knowledge Routing Policy | `manual_authoring` | Không xác định | `3c66493a6f0b...` | 12,025 B |
| `codebase_manifest` | Git Repository & Codebase Manifest | `manual_authoring` | Không xác định | `49e12be7340e...` | 13,941 B |
| `orchestrator_engine` | Antigravity Orchestration Engine | `manual_authoring` | Không xác định | `ad47398f00f7...` | 15,334 B |
| `dispatch_readme` | Antigravity Task Dispatch Protocol | `manual_authoring` | Không xác định | `33a450ce3059...` | 5,121 B |
| `vocabulary_glossary` | MoMo Reporting Glossary SSOT | `manual_authoring` | Không xác định | `82c92952ef07...` | 60,152 B |
| `performance_tracking_master` | Google Sheets Cloud SSOT (1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU) & BigQuery | `scripts/sync_tracking_report.py` | GSC Export 2026-10-10 | `3735c4a03912...` | 83,660 B |
| `performance_data_mart` | GA4 Data API (270743103) & GSC Search Analytics | `scripts/build_full_funnel_matrix.py` | MTD 2026-11 (cắt ngày 2026-11-04) | `2b360bd27533...` | 121,679,872 B |
| `performance_snapshot_latest` | GA4 Data API & Local History Snapshot | `scripts/sync_ga4_master.py` | Tháng 11/2026 (MTD 13 ngày: 01/11 - 13/11/2026, GA4 Data API, lọc chuẩn hostName == 'www.momo.vn') | `7994d0647202...` | 7,365 B |
| `paid_ads_performance` | GA4 Data API (Property 270743103) Paid Media Channels | `scripts/sync_paid_ads.py` | Không xác định | `c81751da24d8...` | 200,815 B |
| `theme_seasonality` | Google Trends API (pytrends VN) | `scripts/theme_seasonality.py` | Không xác định | `86b19eb558ae...` | 89,270 B |
| `decision_log` | Executive Leadership Alignment & Product Decision Log | `manual_authoring` | Quyết định gần nhất (2026-10-14) | `e42abdfb801f...` | 14,847 B |
| `roadmap_releases` | Engineering Releases & Ship Tracker | `manual_authoring` | Bản ghi gần nhất (2026-10-30) | `91ca395258a8...` | 18,700 B |
| `utility_tracking` | Umami Analytics Cloud Instance & MoSpark Tracking Specification | `manual_authoring` | Không xác định | `b431fff629ae...` | 45,274 B |
| `cinema_hub_brd` | Cinema Hub Business Requirement Document | `manual_authoring` | Không xác định | `d63ee46f332b...` | 167,168 B |
| `vehicle_hub_brd` | Vehicle Hub Business Requirement Document | `manual_authoring` | Không xác định | `4cf567bbd5e9...` | 138,876 B |
| `vehicle_partner_garages` | Danh bạ garage đối tác đã làm sạch (chuẩn hóa tên, khử trùng, có garage_id và search_volume) | `manual_authoring` | Không xác định | `d5d7e7743c84...` | 4,454,224 B |
| `vehicle_partner_garages_raw` | Bản thô danh bạ garage đối tác trước khi làm sạch. Chỉ dùng để đối soát nguồn, không dùng làm số liệu. | `manual_authoring` | Không xác định | `191b1d914dcf...` | 3,599,780 B |
| `financial_hub_brd` | Financial Hub Business Requirement Document | `manual_authoring` | Không xác định | `3e192339e091...` | 127,928 B |
| `mospark_rag_knowledge_base` | MoSpark Platform Architecture & Knowledge Base | `manual_authoring` | Không xác định | `5ea895f4a6f0...` | 19,051 B |
| `seo_execution_sop` | SEO Execution Standard Operating Procedure | `manual_authoring` | Không xác định | `154848a924c9...` | 4,621 B |
| `web_growth_strategy_historical` | Historical Web Growth BRD Archive | `manual_authoring` | Dữ liệu đối chiếu lịch sử | `64bd1fa3a998...` | 8,771 B |

---

## III. PHÂN TÍCH RỦI RO & BẢO ĐẢM TOÀN VẸN (SO WHAT)

1. **Bảo đảm tính nhất quán đa tác tử (Multi-Agent Consensus):**
   - Khi Antigravity và Claude cùng tham gia giải quyết một bài toán hoặc lập báo cáo, hai tác tử phải dùng mã băm SHA-256 để xác nhận trạng thái tệp nguồn.
   - Nếu một tác tử sửa đổi tệp cục bộ mà chưa ghi nhận phiên bản, tác tử còn lại sẽ lập tức phát hiện mã băm không khớp và dừng kết luận sai lệch.

2. **Minh bạch hóa dòng chảy dữ liệu (Data Lineage):**
   - Toàn bộ nguồn dữ liệu định lượng (`performance`, `paid_ads`, `seasonality`) đều được liên kết chính xác tới script sinh tương ứng trong thư mục `scripts/`.
   - Loại bỏ hoàn toàn tình trạng số liệu trôi nổi không rõ nguồn gốc phát sinh.

---

## IV. HƯỚNG DẪN ĐỐI SOÁT & VẬN HÀNH (NOW WHAT)

1. **Lệnh đối soát nhanh cho Agent:**
   - Chạy `./.venv/bin/python scripts/generate_knowledge_provenance.py --verify` để xác nhận toàn bộ 27 nguồn tri thức đang ở trạng thái nguyên vẹn 100%.
2. **Tích hợp vào CI/CD:**
   - Tự động chạy xác thực provenance trong GitHub Actions nhằm ngăn chặn việc đẩy nhầm các tệp bị can thiệp trái phép.

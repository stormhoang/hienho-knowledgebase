# KNOWLEDGE REVIEW (generated)

- Entries: **18** | Ky: 2026-11-19 -> 2026-11-21
- Generated: 2026-11-21 18:52

## Hanh dong

| Action | So luong |
|---|---|
| FIX | 6 |
| REFACTOR | 5 |
| LINT | 3 |
| DECISION | 2 |
| FEAT | 2 |

## Top targets bi dung nhieu nhat

| Target | So lan |
|---|---|
| `00_HARNESS_CORE/FAST_ROUTING_INDEX.md` | 2 |
| `scripts/detect_knowledge_conflicts.py` | 2 |
| `scripts/ingest_ga4_daily.py` | 1 |
| `scripts/ingest_gsc_mtd.py` | 1 |
| `07_REPORTS/data/archive` | 1 |
| `scripts/tests/test_ingest_parsers.py` | 1 |
| `scripts/diagnose_performance.py` | 1 |
| `scripts/lint_knowledge.py` | 1 |
| `00_HARNESS_CORE/KNOWLEDGE_INDEX.md` | 1 |
| `07_REPORTS/docs` | 1 |

## Pattern lap - ung vien bug class can guard/skill

_Chua co target nao bi sua >= 3 lan trong ky nay._

## Chu de nong (keyword trong summary)

`sync` x5, `ingest` x5, `routing` x4, `broken` x4, `push` x4, `archive` x3, `hub_sync_lock` x3, `lock` x3, `16kb` x2, `snapshot` x2, `ai_traffic` x2, `non-paid` x2

## No ky thuat (join voi generated artifacts)

- freshness: {'normative': 22, 'stale': 1, 'fresh': 2, 'unknown': 2, 'historical': 1} (generated 2026-11-20T13:07:06.656869+00:00)
  - STALE: `07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`
- conflicts: 88 findings ({'skill_asset_reference': 3, 'external_reference': 67, 'code_path_reference': 18}), age 0d - broken_reference=0

## Entry gan nhat

- `2026-11-19` [DECISION] [data integrity - RESOLVED] detect_performance flag monthly_11_2026_mtd_19d.json "tổng kênh không khớp tổng PV". Owner quyết: AI Traffic LÀ kênh trong Non-Paid và nằm t
- `2026-11-19` [FIX] [scripts/diagnose_performance.py] parts của validate_snapshot thêm ai_traffic (canonical: AI trong Non-Paid); guard hub pct=None → "Chưa có target" thay vì crash.
- `2026-11-20` [LINT] [scripts/lint_knowledge.py] Khởi tạo Knowledge Health Linter theo Karpathy LLM Wiki pattern; quét broken links, routing targets, En Dash/Em Dash và priority labels; toà
- `2026-11-20` [REFACTOR] [00_HARNESS_CORE/KNOWLEDGE_INDEX.md] Tạo Catalog SSOT tập trung 1 dòng/tài liệu cho 6 khối tri thức cốt lõi (Harness, Strategy, Frameworks, Hubs, Analytics, Toolchain).
- `2026-11-20` [FIX] [00_HARNESS_CORE/FAST_ROUTING_INDEX.md + 07_REPORTS/docs/] Chuẩn hóa toàn bộ đường dẫn tương đối và URL encoded (%20) sang file thực tế; sửa link trỏ Budget 2027 sang bản v2.
- `2026-11-20` [FIX] [react-web-momo/scripts/build-dashboard-data.py] Sua 4 path stale sau khi data/monthly_*.json move vao data/monthly/: glob hub_targets/running, m9_full_path, running report resolve, docstri
- `2026-11-20` [REFACTOR] [scripts/lib/hub_push.py] Tao shared helper commit_and_push_hub gom logic git add/commit/push duplicate tu ingest_ga4_daily + ingest_gsc_mtd; tu dong fallback push_to
- `2026-11-20` [FIX] [hub_sync_lock coverage] Audit toan bo script cham react-web-momo: them hub_sync_lock vao sync_inventory_to_hubs, sync_agent_tasks, sync_seo_news, sync_roadmap_to_su
- `2026-11-21` [FEAT] [scripts/route.py + scripts/harness_doctor.py] Phase 1 harness upgrade: executable router parse FAST_ROUTING_INDEX.md (65 routes, keyword scoring, --list); harness doctor check AGENTS<16K
- `2026-11-21` [FEAT] [scripts/guard_hub_writers.py] Phase 2 loop bat dau: guard enforce moi hub writer co hub_sync_lock + push qua flag. KNOWN_HUB_WRITERS=10 file (9 co lock + sync_tracking_re

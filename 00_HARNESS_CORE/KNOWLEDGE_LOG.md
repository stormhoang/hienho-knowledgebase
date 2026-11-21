# KNOWLEDGE LOG (Append-only)

Nhật ký biến động của knowledge layer. Mọi thao tác INGEST / REFACTOR / SYNC / DECISION / LINT lên file tri thức SSOT phải ghi 1 dòng theo format:

```
[YYYY-MM-DD HH:MM] [ACTION] [TARGET_FILE] [SUMMARY]
```

Quy tắc:
- Append-only: cấm sửa/xóa dòng cũ. Sai thì ghi dòng mới đính chính.
- ACTION: `INGEST` (thêm nguồn), `REFACTOR` (di chuyển/tái cấu trúc), `SYNC` (cập nhật từ pipeline), `DECISION` (quyết định kiến trúc/quy chuẩn), `LINT` (quét/sửa health check), `FIX` (sửa link/nội dung lỗi).
- TARGET_FILE: path tương đối trong repo.
- File này không chứa số liệu nghiệp vụ - chỉ metadata vận hành knowledge layer.

---

[2026-11-19] [REFACTOR] [AGENTS.md + 00_HARNESS_CORE/FAST_ROUTING_INDEX.md] Tách bảng Fast Routing Index + Data SSOT Routing (~90 rows) sang FAST_ROUTING_INDEX.md để AGENTS.md về 15.224 bytes < ngưỡng inject 16KB; trước đó ~47% rules (Anti-Hallucination, ANTI-FABRICATION, Security) nằm ngoài vùng inject.
[2026-11-19] [FIX] [CLAUDE.md] Cập nhật pointer Fast Routing Index sang FAST_ROUTING_INDEX.md.
[2026-11-19] [LINT] [repo-wide] Chạy detect_knowledge_conflicts.py: broken_reference 9 → 3. Fix path `data/monthly_*` → `data/monthly/monthly_*` ở 6 file; repoint row `sync_7d_performance_report.py` (đã archive) sang query_analytics; gỡ bullet `web_platform_performance.xlsx` đã xóa trong 07_REPORTS/README.md. Residual 3: path repo ngoài (MoMatrix/momo.cms) trong weekly reports đã qua - chấp nhận, không verify được local.
[2026-11-19] [DECISION] [scripts/detect_knowledge_conflicts.py] Thêm flag `--max-broken N`; pre-commit hook enforce baseline 3 broken_reference - chặn phát sinh link gãy mới, fail khi số này tăng.
[2026-11-19] [FIX] [scripts/detect_knowledge_conflicts.py + weekly reports] Thêm escape-hatch `<!-- kb:external -->` cho ref cố ý trỏ repo ngoài; annotate 3 path MoMatrix/momo.cms trong weekly reports; hạ pre-commit `--max-broken` về 0 (zero tolerance, broken_reference = 0).
[2026-11-19] [REFACTOR] [scripts/ingest_ga4_daily.py + scripts/ingest_gsc_mtd.py] Gate git commit/push repo Hubs sau cờ `--push-hubs` (trước đây auto-push origin main mỗi lần ingest - vi phạm rule single-repo git boundary). File dashboard vẫn ghi local như cũ.
[2026-11-19] [REFACTOR] [07_REPORTS/data/archive/] Move 9 file zero-reference (baseline_mtd_anchor, cms_projects.csv, data_studio_mtd.csv, ga4_30days_latest, gsc_7d_pages_latest, funnel mtd_13d/22d x3, content_plan_refactor_audit) từ data/ root vào data/archive/.
[2026-11-19] [LINT] [scripts/tests/test_ingest_parsers.py] Thêm 12 unit test cho ingest_paid_ads + ingest_ga4_daily parsers + load_hub_map smoke; tổng suite 60 tests pass.
[2026-11-19] [DECISION] [data integrity - RESOLVED] detect_performance flag monthly_11_2026_mtd_19d.json "tổng kênh không khớp tổng PV". Owner quyết: AI Traffic LÀ kênh trong Non-Paid và nằm trong tổng PV (canonical schema). Restate mtd_19d (actual 3.232.936→3.255.620, +22.684) và mtd_18d (3.102.303→3.124.987) + summary.json + page_mtd checks.ga4_pv + artifact mom_growth_drivers + PERFORMANCE_SNAPSHOT_LATEST.md. Validator sửa: parts gồm ai_traffic. Snapshot cũ hơn (12d-17d) vẫn inconsistency lịch sử - chấp nhận, diagnose chỉ đọc latest. diagnose_performance fix crash hub pct=null (student no target).
[2026-11-19] [FIX] [scripts/diagnose_performance.py] parts của validate_snapshot thêm ai_traffic (canonical: AI trong Non-Paid); guard hub pct=None → "Chưa có target" thay vì crash.
[2026-11-20] [LINT] [scripts/lint_knowledge.py] Khởi tạo Knowledge Health Linter theo Karpathy LLM Wiki pattern; quét broken links, routing targets, En Dash/Em Dash và priority labels; toàn bộ 236 tài liệu tri thức đạt chuẩn 0 errors.
[2026-11-20] [REFACTOR] [00_HARNESS_CORE/KNOWLEDGE_INDEX.md] Tạo Catalog SSOT tập trung 1 dòng/tài liệu cho 6 khối tri thức cốt lõi (Harness, Strategy, Frameworks, Hubs, Analytics, Toolchain).
[2026-11-20] [FIX] [00_HARNESS_CORE/FAST_ROUTING_INDEX.md + 07_REPORTS/docs/] Chuẩn hóa toàn bộ đường dẫn tương đối và URL encoded (%20) sang file thực tế; sửa link trỏ Budget 2027 sang bản v2.
[2026-11-20] [FIX] [react-web-momo/scripts/build-dashboard-data.py] Sua 4 path stale sau khi data/monthly_*.json move vao data/monthly/: glob hub_targets/running, m9_full_path, running report resolve, docstring. Truoc fix: running=None, hubTargets rong, ga4Pv mat. Sau rebuild: running=2026-11 19d, ga4Pv=3.255.620 (restated), 5 hubTargets. Refresh Hub artifacts: web-data.json, page_mtd.json, summary.json x2 (uncommitted trong hub repo).
[2026-11-20] [REFACTOR] [scripts/lib/hub_push.py] Tao shared helper commit_and_push_hub gom logic git add/commit/push duplicate tu ingest_ga4_daily + ingest_gsc_mtd; tu dong fallback push_to_hubs_api.py (REST API) khi git push fail do firewall. Them hub_sync_lock vao __main__ ca 2 ingest scripts (ga4_daily bo qua lock khi --dry-run). --push-hubs van la gate bat buoc.
[2026-11-20] [FIX] [hub_sync_lock coverage] Audit toan bo script cham react-web-momo: them hub_sync_lock vao sync_inventory_to_hubs, sync_agent_tasks, sync_seo_news, sync_roadmap_to_supabase (__main__) va intake.push_to_hubs (wrap _push_to_hubs). Truoc: 4 script ghi hub repo khong lock -> race voi ingest khi chay standalone. Xac nhan: khong script nao git push khi thieu flag; push_to_hubs_api chi chay qua --push-hubs hoac goi truc tiep.
[2026-11-21] [FEAT] [scripts/route.py + scripts/harness_doctor.py] Phase 1 harness upgrade: executable router parse FAST_ROUTING_INDEX.md (65 routes, keyword scoring, --list); harness doctor check AGENTS<16KB, routing targets, skills, registry, conflicts baseline, exit 1 khi FAIL. Fix knowledge_registry.yaml: 3 generator_script stale (build_full_funnel_matrix->sync_data_mart, sync_ga4_master->ingest_ga4_daily, sync_paid_ads->ingest_paid_ads). pre-commit them validate_knowledge_registry observe-warn. FAST_ROUTING_INDEX: +2 rows moi, sua "baseline 3" -> zero-tolerance.

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

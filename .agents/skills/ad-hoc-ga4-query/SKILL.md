---
name: ad-hoc-ga4-query
description: DEPRECATED - GA4/GSC API đã bị cấm theo policy (xem AGENTS.md). Không dùng skill này; đọc dữ liệu local thay thế.
---

> **DEPRECATED 2026-11-20:** Policy mới cấm mọi gọi GA4/GSC API. Skill này và `scripts/lib/ga4_client.py` không còn được dùng. Thay thế: `scripts/query_analytics.py` (Data Mart), `page_mtd.json`, `ingest_ga4_daily.py`, `ingest_gsc_mtd.py`.

# SKILL: AD-HOC GA4 QUERY (/ad-hoc-ga4-query)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi người dùng hỏi số liệu GA4 dạng một lần, không có script chuyên trách:
- *"Event X trên page Y tuần này bao nhiêu?"*
- *"Top pagePath có event Z trong 30 ngày"*
- *"Sessions theo campaign UTM U ngày X"*
- *"So sánh eventCount hôm nay vs tuần trước"*

## 2. NGUYÊN TẮC CỨNG (KHÔNG ĐƯỢC VI PHẠM)

1. **CẤM viết file script mới** cho truy vấn GA4 đơn giản. Dùng shared client `scripts/lib/ga4_client.py`.
2. **CẤM copy-paste `get_ga4_access_token()`** - hàm này đã được SSOT hóa trong `ga4_client.py`.
3. Chỉ tạo file trong `scratch/` khi query có logic phức tạp (>30 dòng: multi-step, join nhiều nguồn, format report riêng). File scratch đặt tên `query_<topic>_<YYYYMMDD>.py`.
4. Property ID SSOT: `270743103` (đã hardcode trong client, không tự đổi).

## 3. CÁCH DÙNG

### Cách 1 - CLI nhanh (không cần viết code):
```bash
./.venv/bin/python scripts/lib/ga4_client.py \
  --dimensions pagePath,eventName \
  --metrics eventCount,totalUsers \
  --start 7daysAgo --end today \
  --filter-field pagePath --filter-value /tai-chinh --filter-type BEGINS_WITH \
  --limit 50
```
Filter types: `EXACT`, `CONTAINS`, `BEGINS_WITH`, `ENDS_WITH`, `REGEXP`.

### Cách 2 - Inline Python cho query phức tạp:
```bash
./.venv/bin/python - <<'EOF'
import sys
sys.path.insert(0, ".")
from scripts.lib.ga4_client import run_report

rows = run_report(
    dimensions=["date", "pagePath"],
    metrics=["sessions", "totalUsers", "engagementRate"],
    start_date="7daysAgo", end_date="today",
    order_bys=[{"dimension": {"dimensionName": "date"}}],
)
for r in rows[:20]:
    print(r)
EOF
```

### API reference (`scripts/lib/ga4_client.py`):
- `run_report(dimensions, metrics, start_date, end_date, dimension_filter, order_bys, limit)` -> list of dict. Tự phân trang tới `limit` (mặc định 100k).
- `run_report_all(...)` -> lấy hết không giới hạn.
- `dimension_filter` theo chuẩn GA4 FilterExpression:
  ```python
  {"filter": {"fieldName": "pagePath",
              "stringFilter": {"matchType": "EXACT", "value": "/tai-chinh"}}}
  # andGroup/orGroup cho filter nhiều điều kiện
  ```
- `start_date`/`end_date`: `"today"`, `"yesterday"`, `"7daysAgo"`, `"30daysAgo"`, `"YYYY-MM-DD"`.

## 4. DIMENSIONS & METRICS THƯỜNG DÙNG (SSOT tham chiếu)

| Mục đích | Dimensions | Metrics |
|---|---|---|
| Event trên 1 page | `pagePath`, `eventName` | `eventCount`, `totalUsers` |
| Funnel W2A | `pagePath`, `eventName` | `eventCount` (filter `click_to_app`, `click_link_url`) |
| Traffic theo kênh | `sessionSource`, `sessionMedium` | `sessions`, `totalUsers`, `engagementRate` |
| Landing page | `landingPage`, `sessionSourceMedium` | `sessions`, `bounceRate` |
| Theo ngày | `date` | bất kỳ metric |
| UTM campaign | `sessionCampaignName`, `sessionSourceMedium` | `sessions`, `conversions` |
| Device/geo | `deviceCategory`, `country` | `sessions`, `totalUsers` |

Full list dimension/metric hợp lệ: GA4 Data API docs (developers.google.com/analytics/devguides/reporting/data/v1/api-schema).

## 5. SAU KHI CÓ KẾT QUẢ

- Trình bày số liệu kèm kỳ dữ liệu (start/end date đã query) - bắt buộc theo Anti-Hallucination rule.
- Nếu pattern query này lặp lại >2 lần → đề xuất user promote thành script chuyên trách trong `scripts/` hoặc bổ sung vào skill hiện có, thay vì tiếp tục ad-hoc.
- Không commit file scratch chứa credentials hoặc data nhạy cảm.

## 6. LIÊN QUAN

- Skill `sync-ads`: pipeline định kỳ Paid Ads (đã có script riêng, không dùng skill này).
- `scripts/query_analytics.py`: query SQLite Data Mart local (khác nguồn - dùng khi cần join đa nguồn đã sync, không gọi API trực tiếp).
- Credentials: `07_REPORTS/data/credentials/ga4-credentials.json` + `ga4-token.json` (OAuth refresh token).
- GSC ad-hoc: dùng `scripts/lib/` chưa có client - nếu cần query GSC Search Analytics ad-hoc, tham khảo pattern trong `scripts/gsc_keyword_ranking.py` (service account `gsc-credentials.json`).

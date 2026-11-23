---
name: sync-ads
description: DEPRECATED - đã gộp vào skill paid-ads. Nạp Paid Ads thủ công từ GA4 Explore CSV qua scripts/ingest_paid_ads.py (GA4 API bị policy cấm).
---


> **DEPRECATED 2026-11-20:** Skill này đã được gộp vào [`paid-ads`](../paid-ads/SKILL.md). `scripts/sync_paid_ads.py` (GA4 Data API) đã archive do policy cấm API.
>
> **Luồng hiện tại:** dùng `scripts/ingest_paid_ads.py` để nạp Paid Ads từ file export GA4 Explore CSV (xem spec export trong skill `paid-ads`), output ghi vào `07_REPORTS/data/analytics/paid_ads_performance.json`.

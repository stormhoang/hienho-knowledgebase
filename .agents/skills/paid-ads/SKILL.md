---
name: paid-ads
description: Báo cáo và kiểm tra các trang web đang chạy Ads, kênh media (Google, TikTok, Facebook, Admicro...) và chuyển đổi Web-to-App.
---

> **DEPRECATED 2026-11-20:** `scripts/sync_paid_ads.py` đã archive do policy cấm GA4 API. Skill này không còn chạy được. Dữ liệu Paid Ads hiện chỉ đọc từ snapshot `07_REPORTS/data/analytics/paid_ads_performance.json` (cập nhật lần cuối trước khi kill API).


# SKILL: PAID ADS & MEDIA CHANNELS TRACKING (/paid-ads)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi người dùng gõ `/paid-ads` hoặc yêu cầu kiểm tra quảng cáo Kênh Web.

## 2. QUY TRÌNH THỰC THI TỰ ĐỘNG
AI Agent tự động thực thi script:
```bash
./.venv/bin/python scripts/sync_paid_ads.py
```
Và đọc dữ liệu SSOT tại:
- JSON: [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json)
- Báo cáo chi tiết: [`07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md)

## 3. TRÌNH BÀY BÁO CÁO
Trình bày bảng phân bổ Kênh Media, Top Landing Pages và chuyển đổi Web-to-App theo văn phong Product Lead / Tech Lead.

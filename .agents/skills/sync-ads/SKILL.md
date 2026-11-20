---
name: sync-ads
description: Tự động truy vấn GA4 Data API, đồng bộ và bóc tách toàn diện Paid Ads, Landing Pages, Kênh Media và hiệu suất Web-to-App.
---

> **DEPRECATED 2026-11-20:** `scripts/sync_paid_ads.py` đã archive do policy cấm GA4 API. Skill này không còn chạy được. Dữ liệu Paid Ads hiện chỉ đọc từ snapshot `07_REPORTS/data/analytics/paid_ads_performance.json` (cập nhật lần cuối trước khi kill API).


# SKILL: PAID ADS & UTM SYNCHRONIZATION PIPELINE (/sync-ads)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi người dùng gõ `/sync-ads`, `/paid-ads` hoặc đưa ra các yêu cầu:
- *"Kiểm tra ads"*
- *"Web đang chạy ads gì"*
- *"Kênh media nào đang chạy ads"*
- *"Update ads performance"*
- *"Hiệu suất Paid Ads MTD"*

## 2. QUY TRÌNH THỰC THI TỰ ĐỘNG

Khi nhận lệnh, AI Agent tự động gọi script chuyên trách:
```bash
./.venv/bin/python scripts/sync_paid_ads.py
```
*(Hoặc tùy biến khoảng ngày: `./.venv/bin/python scripts/cli.py ads --start YYYY-MM-DD --end today`)*

### Các bước script thực hiện:
1. **Truy vấn GA4 Data API (Property `270743103`):**
   - Quét toàn bộ lưu lượng Paid Ads (`cpc`, `paid`, `NativeAds`, `ads`, `cross-network`).
   - Lấy chi tiết `pagePath`, `sessionSourceMedium`, `sessionCampaignName`, `sessionManualAdContent`.
   - Lấy số liệu `screenPageViews`, `sessions`, `totalUsers`.
2. **Đo lường chuyển đổi Web-to-App:**
   - Quét sự kiện `click_to_app` và các sự kiện Game/In-app installs riêng (`gmc_1vuquyt_install`, `clickplay`).
   - Tính toán tỷ lệ chuyển đổi thực chất (CVR = Chuyển đổi / Sessions).
3. **Cập nhật SSOT:**
   - Xuất dữ liệu JSON: `07_REPORTS/data/analytics/paid_ads_performance.json`.
   - Xuất báo cáo Markdown: `07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md`.

## 3. TRÌNH BÀY BÁO CÁO CHO NGƯỜI DÙNG (EXECUTIVE REPORT)
Sau khi đồng bộ xong, AI Agent tự động trình bày kết quả cô đọng chuẩn Product Lead / Tech Lead:
- **Tổng quan:** Tổng Paid Pageviews, Paid Sessions, Số trang đang nhận Ads.
- **Bảng 1: Phân bổ theo Kênh Media (`Source / Medium`):** Google Search Ads, TikTok Ads, Facebook Ads, Admicro Native Ads...
- **Bảng 2: Top Landing Pages chạy Ads nhiều nhất:** URL, Hub sản phẩm, Kênh chủ đạo, Pageviews Ads, Lượt chuyển đổi Web-to-App, CVR (%).
- **Key Takeaways & Rủi ro:** Nêu rõ các kênh đang đốt tiền kém hiệu quả (như TikTok Ads CVR thấp) hoặc kênh mang lại chuyển đổi cao.
- **Quy chuẩn văn phong:** KHÔNG dùng emoji/icon, KHÔNG nêu tên riêng cá nhân, dùng Markdown Tables.

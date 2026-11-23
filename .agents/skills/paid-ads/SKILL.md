---
name: paid-ads
description: Báo cáo và kiểm tra các trang web đang chạy Ads, kênh media (Google, TikTok, Facebook, Admicro...) và chuyển đổi Web-to-App. Data từ GA4 Explore export thủ công qua scripts/ingest_paid_ads.py.
---


# SKILL: PAID ADS & MEDIA CHANNELS TRACKING (/paid-ads)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi người dùng gõ `/paid-ads` hoặc yêu cầu kiểm tra quảng cáo Kênh Web: "web đang chạy ads gì", "kênh media nào đang chạy", "hiệu suất Paid Ads MTD".

## 2. NGUỒN DỮ LIỆU (MANUAL PIPELINE - KHÔNG DÙNG API)

GA4 Data API đã bị policy cấm. Paid Ads được nạp thủ công từ file export GA4 Explore:

- **Ingest script:** `scripts/ingest_paid_ads.py`
- **JSON SSOT:** `07_REPORTS/data/analytics/paid_ads_performance.json`
- **Schema giữ nguyên** như bản API cũ: `summary`, `channels`, `landing_pages` (hub, pageviews, sessions, users, w2a_conversions, cvr_percent, primary_channel, channels_breakdown, campaigns, creatives).

## 3. QUY TRÌNH NẠP DỮ LIỆU (khi user yêu cầu update)

### Bước 1 - User export GA4 Explore (Free form), 2 file:

**File Traffic (bắt buộc):**
- Dimensions: `Page path`, `Session source / medium`
- Khuyến nghị thêm: `Session campaign`, `Session manual ad content`
- Metrics: `Views`, `Sessions`, `Total users`
- Filter: `Session medium` in `cpc`, `paid`, `NativeAds`, `ads` - hoặc `Session default channel group` chứa `Paid`

**File Events (tùy chọn, để có W2A CVR):**
- Dimensions: `Event name`, `Page path`
- Metrics: `Event count`
- Filter: `Event name` in `click_to_app`, `gmc_1vuquyt_install`, `gmc_1vuquyt_clickplay`

Fallback: nếu chỉ export được bản `Page path` + `Session default channel group` (không có source/medium), script vẫn chạy nhưng channel chỉ ở mức `(channel) Paid Search`...

### Bước 2 - Chạy ingest:
```bash
./.venv/bin/python scripts/ingest_paid_ads.py traffic.csv events.csv --start 2026-11-01 --end 2026-11-19
# hoặc bỏ tham số file: tự quét ~/Downloads tìm CSV GA4 Explore mới nhất
./.venv/bin/python scripts/ingest_paid_ads.py
```

### Bước 3 - Trình bày báo cáo (EXECUTIVE REPORT)
- **Tổng quan:** Total Paid PV, Paid Sessions, số trang nhận Ads, số kênh.
- **Bảng 1 - Kênh Media:** channel, pageviews, share %, số trang active.
- **Bảng 2 - Top Landing Pages:** URL, Hub, kênh chủ đạo, PV, W2A conversions, CVR.
- **Key Takeaways:** kênh đốt tiền kém hiệu quả, trang CVR cao.
- **Quy chuẩn:** không emoji, không tên cá nhân, Markdown tables, số liệu phải ghi kỳ dữ liệu (date_range trong JSON).

## 4. LƯU Ý
- Nếu `sessions`/`users`/`w2a` = 0: export thiếu metrics/events tương ứng - báo user bổ sung cột, không kết luận số 0 là thật.
- `cvr_percent` = W2A events / pageviews x 100 (có thể >100% do đa touch, giữ nguyên convention cũ).
- Skill `/sync-ads` là bản deprecated trỏ về skill này.

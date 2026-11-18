---
name: sync-all
description: Đồng bộ toàn bộ dữ liệu Web Platform (Microsoft Clarity API, Web Performance Tracking MTD, Google Trends, Bing Copilot, Web Hubs Distribution).
---

# SKILL: MASTER DATA & API SYNCHRONIZATION PIPELINE (/sync-all)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi người dùng gõ `/sync-all`, `/sync` hoặc đưa ra các yêu cầu tương tự:
- *"Sync toàn bộ dữ liệu"*
- *"Chạy đồng bộ tất cả các luồng API"*
- *"Cập nhật toàn bộ data Web Platform"*

## 2. QUY TRÌNH THỰC THI TỰ ĐỘNG (AUTOMATED WORKFLOW)

Khi nhận lệnh, AI Agent tự động thực thi script điều phối Master:
```bash
./.venv/bin/python scripts/sync_all_data.py
```

### Các Luồng Dữ Liệu Được Đồng Bộ:
1. **Web Performance Tracking MTD:**
   - Quét file Excel tracking mới nhất từ `/Users/hienhv/Downloads/`.
   - Trích xuất số ngày lũy kế MTD, lưu SSOT vào `07_REPORTS/web_performance_tracking.xlsx`.
   - Đẩy dữ liệu sang Web Hubs (`react-web-momo`) cho cả `/dashboard` và `/bang-tin`.
2. **Microsoft Clarity Data Export API:**
   - Kéo 4 requests: URL, Source/Medium, Channel, URL/Source.
   - Nhận diện traffic AI (`chatgpt.com`, `perplexity.ai`, `duck.ai`...), kênh `AiPlatform`.
   - Đo lường 5 chỉ số hành vi (Scroll Depth, Engagement Time, Dead Clicks, Rage Clicks, Quickbacks).
   - Cập nhật snapshot ngày và file SSOT `07_REPORTS/data/clarity/clarity_latest.json`.
3. **Google Trends Demand Validation:**
   - Quét rolling top themes ngành Tài Chính (Giá vàng, Tỷ giá, Vay tín chấp, Ví Trả Sau, Gửi tiết kiệm).
   - Cập nhật địa bàn tìm kiếm (Geo-intent) và các truy vấn tăng đột biến (Rising queries) vào `07_REPORTS/data/google_trends_validation.json`.
4. **Bing AI Performance Ingest:**
   - Tự động nhận diện và nạp các lượt trích dẫn Microsoft Copilot nếu có file export mới trong `Downloads/`.
5. **Web Hubs Distribution:**
   - Đồng bộ kho từ khóa Use Cases (`05_HUBS/inventory/`) sang repo giao diện `react-web-momo`.
6. **SEO News (SEO/GEO/AI Search):**
   - Thu thập tin từ nguồn chính thống (Google Search Central Blog, Google Search Status Dashboard, Search Engine Journal, Search Engine Roundtable).
   - Lọc tin trong 60 ngày (chính thống lấy hết + báo ngoài tối đa 25 tin), bỏ trùng URL.
   - Merge 2 lớp enrichment: Gemini Spark daily reports (`11_NEWS_FEED/*_daily_report.md` - title VN, tóm tắt, action, bổ sung tin ngoài RSS) và overlay thủ công `07_REPORTS/data/seo_news_enriched.json`.
   - Gắn field `insight` từ dữ liệu thật (GSC API, Bing AI Performance, Clarity, Crawl Stats) qua `scripts/seo_news_insights.py`; tin không tính được thì bỏ field, không suy diễn. Dùng `--skip-insights` để chạy nhanh.
   - Xuất SSOT `07_REPORTS/data/seo_news_latest.json` và đẩy sang `react-web-momo/data/seo-news.json` (render tại trang `/content-plan`).

## 3. TRÌNH BÀY BÁO CÁO TỔNG HỢP CHO NGƯỜI DÙNG (EXECUTIVE REPORT)
Sau khi script hoàn thành, trình bày bảng tóm tắt kết quả chuẩn Tech Lead / Product Lead:
- **Bảng trạng thái các luồng:** `Tên luồng` | `Trạng thái` | `Thời gian thực thi`.
- **Chỉ số hiệu suất Kênh Web:** Actual MTD PVs, % Target, Run-rate Forecast.
- **Bảng kênh truy cập (bắt buộc tách Non-Paid / Paid khi trình bày):** Pipeline sync vẫn đồng bộ toàn bộ dữ liệu thô (mọi tổ hợp `sessionDefaultChannelGroup x sessionSource`) sang SSOT và Hub, không lọc bớt. Riêng phần trình bày kết quả cho người dùng phải tách đúng cấu trúc:
  - `Non-Paid` gồm đúng 4 kênh con: `Organic` (Organic Search, trừ nguồn AI) | `Direct` | `AI Traffic (GEO)` (mọi phiên có `sessionSource` khớp ChatGPT/OpenAI, Gemini, Perplexity, Claude, Copilot, DeepSeek, Grok, Meta AI, bất kể channel GA4, cộng kênh `AI Assistant`) | `Referral` (Referral, Unassigned, Organic Social, Organic Video, Organic Shopping, Email và mọi `sessionSource` bắt đầu bằng `in_app`).
  - `Paid Ads` gồm Paid Search, Paid Social, Paid Other, Paid Video, Paid Shopping, Display và `Cross-network` (Performance Max). Tuyệt đối không để Cross-network rơi vào Non-Paid.
  - Bảng có các cột: kỳ hiện tại, kỳ so sánh cùng kỳ, MoM, tỷ trọng; dòng tổng `Non-Paid`, `Paid Ads`, `Toàn Kênh Web` in đậm, 4 kênh con thụt dòng dưới Non-Paid. Tổng các dòng phải khớp tổng GA4.
- **Chỉ số Traffic AI & Trải nghiệm:** Tổng AI Sessions, Top URL nhận traffic AI, Kênh AI phát hiện.
- **Quy chuẩn văn phong:** **KHÔNG dùng Emoji/Icon**, **KHÔNG nêu tên riêng cá nhân**, sử dụng **Markdown Tables** và gạch đầu dòng phân tích trực diện.

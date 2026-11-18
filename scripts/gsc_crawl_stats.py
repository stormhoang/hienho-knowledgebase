#!/usr/bin/env python3
"""
Cron Script: Google Search Console (GSC) Crawl Stats Tracker (90 Days)
Mục đích:
1. Kết nối với Google Search Console API bằng Service Account credentials.
2. Quét dữ liệu Search Analytics breakdown theo ngày để track crawl budget indicators.
3. Trích xuất: total requests, total impressions, avg position breakdown theo ngày.
4. Xuất dữ liệu sang 07_REPORTS/data/gsc_crawl_stats.json.

LƯU Ý QUAN TRỌNG:
- GSC API KHÔNG có endpoint trực tiếp cho Crawl Stats (req/ngày, download/ngày, KB/req).
- Script này dùng Search Analytics API breakdown theo ngày để proxy track crawl health.
- Để lấy Crawl Stats chính xác (req/ngày, KB/req, response time), vẫn cần manual export từ GSC UI.
"""

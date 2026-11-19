# Báo cáo AI Citations & AI Referral - momo.vn (YTD đến 18/11/2026)

> Nguồn dữ liệu:
> - Microsoft Clarity Dashboard export: `07_REPORTS/data/clarity/raw/2026-11-18_dashboard.csv` (kỳ 01/01/2026 - 18/11/2026)
> - Bing/AI Performance Overview export: `07_REPORTS/data/bing_ai/raw/2026-11-18_overview.csv` + `ai_performance_latest.json` (kỳ 01/01/2026 - 16/11/2026, 320 ngày)

---

## 1. Kết luận chính

**AI citations của momo.vn tăng ~3-4x từ Q3/2026, nhưng trọng tâm đang nghiêng về content tiện ích/giải trí thay vì nhóm PFM tài chính là mục tiêu GEO North Star.**

## 2. Tổng quan chỉ số

| Chỉ số | Giá trị | Nguồn |
|---|---|---|
| Page citations (YTD) | 353.193 | Clarity Dashboard |
| Tổng citations theo ngày (YTD, 320 ngày) | 1.071.831 | Bing AI Performance Overview |
| AI referral traffic (YTD) | 28.701 sessions | Clarity Dashboard |
| Share of Authority (SoA) trung bình | 19,26% | Clarity Dashboard |
| Cited pages trung bình/ngày | 464,35 | Bing AI Performance Overview |

## 3. Xu hướng citations theo tháng

| Giai đoạn | Citations/ngày | Cited pages/ngày | Nhận định |
|---|---|---|---|
| T1-T2/2026 | ~1.600-2.400 | ~450-590 | Baseline |
| T3-T4/2026 | ~2.900-3.900 | ~500-670 | Tăng trưởng ổn định |
| T5/2026 | ~2.700 | ~600 | Điều chỉnh nhẹ |
| T6-T7/2026 | ~3.000-3.800 | ~450-590 | Duy trì |
| T8-T9/2026 | ~3.000-4.300 | ~250-380 | Citations tăng, pages giảm |
| T10/2026 | ~5.300 (peak 9.530 ngày 15/10) | ~300-350 | Tăng mạnh |
| T11/2026 (đến 16/11) | ~6.400 (peak 11.920 ngày 12/11) | ~330-380 | Đỉnh từ đầu năm |

- Đà tăng rõ từ tháng 9; đỉnh 11.920 citations/ngày ngày 12/11, gấp ~5-7x baseline T1-T2.
- **Cited pages/ngày giảm từ ~600 (T3-T5) xuống ~330 (T10-T11)**: citations tập trung vào ít trang hơn, rủi ro phụ thuộc page hit.

## 4. Top query clusters theo SoA

| Cluster | Citations | SoA | Nhận định |
|---|---|---|---|
| Giá xăng/xăng dầu | ~75K+ | 10-46% (TB ~25%) | Volume lớn nhất, SoA thấp - cơ hội lớn |
| Tra cứu BHYT | ~50K+ | 20-60% (nhiều query >40%) | Cluster mạnh nhất |
| Phim/Cinema | Rất lớn | 12-30% | Nhiều citations, giá trị thương mại thấp |
| Du lịch Macau | ~19,7K | 14,31% | Một hit content đơn lẻ |
| Phạt nguội | ~2,3K | ~10-12% | Product trọng tâm nhưng AI presence yếu |
| CIC | 379 | 12,99% | Gần như vắng mặt |
| Vay Nhanh / VTS | Hầu như không có | - | Vắng mặt trong top queries |

Chi tiết query nổi bật:
- `giá xăng hôm nay`: 22,73K citations, SoA 10,26%
- `tra cứu giá trị sử dụng thẻ bhyt`: 19,98K, SoA 21,33%
- `chuyến đi đến macau`: 19,72K, SoA 14,31%
- `tra cứu hạn sử dụng thẻ bhyt`: 917, SoA 59,97%
- `tra cứu giá trị sử dụng của thẻ bhyt`: 403, SoA 58,24%
- `check phạt nguội`: 1.870, SoA 10,61%
- `check cic`: 379, SoA 12,99%
- `momo for business`: 603, SoA 33,90%
- `credit card là gì`: 542, SoA 32,75%
- `paypal là gì`: 408, SoA 23,18%

## 5. Top cited pages

| Page | Citations |
|---|---|
| `/tien-ich-giao-thong/gia-xang` | 73,82K |
| `/blog/tra-cuu-gia-tri-su-dung-the-bhyt-c116dt2711` | 66,45K |
| `/blog/cam-nang-du-lich-macau-tu-tuc-c101dt2447` | 19,81K |
| `/cinema/review` | 16,74K |
| `/cinema/trai-buon-nguoi-24991` | 14,78K |
| `/cinema/blog/chi-tiet-nhan-vat-dien-vien-phim-ho-linh-trang-si-2720` | 7.094 |
| `/cinema/phim-dang-chieu` | 7.093 |
| `/phat-nguoi` | 2.411 |
| `/blog/le-hoi-van-hoa-dac-sac-nhat-the-gioi-c101dt2457` | 2.154 |
| `/vi-tra-sau` | 614 |
| `/diem-tin-dung` | 1.373 |
| `/vay-nhanh` | 370 |
| `/bao-hiem-xe-may` | 376 |

Nhận định: nhóm trang tài chính (`/vay-nhanh`, `/diem-tin-dung`, `/vi-tra-sau`, `/bao-hiem-xe-may`) xuất hiện nhưng citations rất nhỏ so với utility content.

## 6. Phân tích (So What)

1. **Moat PLG đang hoạt động đúng hướng.** Trang giá xăng và tra cứu BHYT là utility tool tạo data không scrape được; AI engine cite mạnh vì là nguồn authoritative cho query dạng "hôm nay". Đây là bằng chứng đầu tiên cho thesis anti-LLM moat.

2. **Gap rõ với GEO North Star.** Target "top 3 AI cite cho 20 PFM queries" chưa đạt: cụm credit/insurance mua (CIC, vay nhanh, VTS, BHYT theo nghĩa mua bảo hiểm) gần như không được cite. AI đang cite MoMo như thư viện tra cứu tiện ích, chưa phải tư vấn tài chính. Đây là bước nhảy khác về E-E-A-T và search intent.

3. **Concentration risk.** Cited pages giảm ~45% từ T5 sang T10 trong khi citations tăng; tăng trưởng đến từ vài page hit lớn (xăng, BHYT, phim trending). Mất 1-2 page này là mất phần lớn AI visibility.

4. **AI referral 28,7K sessions/năm** là kênh acquisition mới, hiện chưa đo W2A funnel riêng (Install/Register/Cashin).

## 7. Đề xuất hành động (Now What)

1. Nhân bản pattern BHYT/xăng sang cụm tài chính: CIC score checker, so sánh bảo hiểm xe máy, tính lãi vay (khớp O3 PLG/Utilities-Led SEO).
2. Đẩy E-E-A-T cho nhóm tài chính: named author, nguồn dữ liệu chính thống - vẫn là blocker của GEO/AEO QLCT.
3. Đo AI referral funnel riêng trong GA4, map sang onelink funnel để định lượng đóng góp New User/MAU.
4. Giảm concentration risk: internal link từ page hit (xăng, BHYT) sang cụm tài chính liên quan.
5. Lập dashboard định kỳ: SoA theo 20 target PFM queries, top cited pages, AI referral -> W2A conversion.

## 8. Ghi chú dữ liệu

- File Clarity Dashboard là export nhiều section (metrics, queries, pages); pipeline `ingest_bing_ai.py` hiện chỉ nhận diện format Overview/Queries/Pages chuẩn của Bing Webmaster, chưa parse được format dashboard này.
- File Overview chỉ chứa số liệu tổng hợp ngày, không có breakdown queries/pages (cần export riêng nếu muốn bổ sung).
- Dữ liệu Clarity Dashboard kéo đến 18/11; Overview đến 16/11.

---
*Lập ngày: 18/11/2026 - Văn Hiến / Web Product Lead, GPD*
*Liên quan: GEO North Star (20 target PFM queries), O3 PLG/Utilities-Led SEO, GEO/AEO QLCT project*
*Phân tích chi tiết trong session Devin ngày 18/11/2026*
*Lưu ý: cần verify lại số liệu AI citation là internal estimates của Microsoft Clarity, không phải Google AI Overview trực tiếp.*

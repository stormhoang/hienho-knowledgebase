# Báo cáo Tháng 10/2026 - Nhật ký thay đổi trên Dashboard và PPTX View

> Nguồn: repo `react-web-momo`, trang `/report/monthly`
> Cập nhật: 05/11/2026
> Mục đích: đồng bộ KB với các thay đổi đã chốt trên dashboard, để cập nhật `monthly_report_2026_10.json` và các file md liên quan.

## 1. Cấu trúc PPTX View

PPTX View dùng lại các component của Dashboard Điều Hành. Sửa dashboard thì slide đổi theo. Deck có 8 slide:

| Slide | Nội dung | Headline (lấy từ Pyramid.pptx) |
|---|---|---|
| 1 | Bìa | Web Platform - Báo cáo Điều hành Tháng 10/2026 |
| 2 | Khung 3 Trụ Cột | Web Platform - Báo cáo Điều hành Tháng 10/2026 |
| 3 | Hiệu suất kinh doanh | Traffic Tháng 10 đạt 98,3% target dù kênh trả phí giảm sâu (-60,4% MoM), kênh tự nhiên tiếp tục giữ đà tăng trưởng tốt (+13,5% MoM) |
| 4 | Cinema Hub | Cinema Hub vượt kế hoạch đạt 1,13M Pageviews (101,4% Target); Non-Paid đạt đỉnh 86,4% bù đắp 93% Paid Ads cắt giảm |
| 5 | Financial Hub | Financial Hub đạt 274K PV (+9,6% MoM) nhưng chưa bền vững: Phụ thuộc 37% Paid Ads, 77% traffic dồn vào 3 SP tín chấp |
| 6 | Phễu Web-to-App | Phễu New User tăng gấp đôi từ T7 đến T10, lập kỷ lục 2.389 liên kết ngân hàng (+152%); sẵn sàng đón mục tiêu 30K Install Q4 |
| 7 | Thư viện Công cụ Tiện ích | Chưa có headline trong Pyramid, cần bổ sung |
| 8 | Thảo luận BOM | Discussion Topics: 2 đề xuất phê duyệt gồm Pilot Off-Page Cinema mùa phim Tết 2027 và Mở rộng Gamification Quiz sang CIC |

Đã bỏ: dòng "Mục đích:" trên mỗi slide, số thứ tự trong tiêu đề, dòng lead phụ.

## 2. Nội dung đã bỏ khỏi Dashboard

- Khối "Trọng Tâm Điều Hành Quý 4" (`soWhatInsights`). Lý do: số lệch với bảng kênh (99,2% vs 98,3% target; +416K vs +373K Non-Paid; 733K vs 724K Paid cắt giảm).
- Khối "Xem diễn giải chi tiết 4 quan sát chiến lược" (`observations`).
- Badge và label trên Hub: "Dẫn đầu New User", "Tiện ích Chuyển đổi", "% Organic", pill nhận định bên phải, tag "Chiến Lược" / "Chỉ đạo BOM".
- 4 card KPI (Quy mô, Chất lượng, Thương hiệu, GEO) bỏ phần mô tả bên dưới, xếp 1 hàng ngang.

Dữ liệu `soWhatInsights` và `observations` vẫn còn trong data, chỉ không hiển thị.

## 3. Bảng kênh lưu lượng: chuẩn theo Pyramid

Tên kênh và số liệu lấy từ bảng slide 2 của `Web_Platform_Thang_10_2026_Pyramid.pptx`.

| Kênh lưu lượng | Tháng 7 | Tháng 8 | Tháng 9 | Tháng 10 | % MoM |
|---|---|---|---|---|---|
| KÊNH TỰ NHIÊN (NON-PAID) | 2.669.863 | 2.820.824 | 2.755.766 | 3.128.542 | +13,5% |
| - Organic | 1.875.191 | 1.729.694 | 1.623.796 | 1.715.771 | +5,7% |
| - AI Traffic (GEO) | 12.920 | 13.736 | 13.596 | 18.547 | +36,4% |
| - Direct | 440.855 | 656.271 | 755.896 | 931.731 | +23,3% |
| - Referral | 340.897 | 421.123 | 362.478 | 462.493 | +27,6% |
| KÊNH TRẢ PHÍ (PAID ADS) | 497.958 | 644.539 | 1.197.093 | 473.481 | -60,4% |
| TỔNG LƯỢNG TRUY CẬP (ACTUAL) | 3.167.821 | 3.465.363 | 3.952.859 | 3.602.023 | -8,9% |

Thay đổi so với bản cũ:
- "Organic Search" đổi thành "Organic".
- "Trong đó: Lưu lượng GEO (AI Search)" đổi thành "AI Traffic (GEO)" và tính là một kênh con ngang hàng. T7 và T8 sửa lại thành 12.920 và 13.736.
- Bỏ dòng "Kênh tự nhiên khác". Referral theo Pyramid đã gồm phần này (462.493).
- 4 kênh con cộng đúng bằng tổng Non-Paid 3.128.542.

## 4. Điểm cần đối soát

- Weekly report W44 ghi Referral T10 là 481.040 (+27,9%), Pyramid ghi 462.493 (+27,6%). Cần chốt một nguồn.
- Target T10 của Referral (438.235) là số gộp tạm từ target cũ của Referral và "Kênh tự nhiên khác", chưa có nguồn chính thức.
- Financial Hub: Pyramid ghi 274K PV, weekly W44 ghi 254.077 PV.
- `executive_pillars` trong `monthly_report_2026_10.json` chưa khớp nội dung đang hiển thị trên dashboard.

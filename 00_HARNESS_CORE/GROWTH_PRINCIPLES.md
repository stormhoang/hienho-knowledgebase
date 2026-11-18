# GROWTH PRINCIPLES - WEB BUSINESS GROWTH PLAYBOOK (SSOT)

> Mục đích: Bộ não phân tích growth cho mọi agent trong repo. File này định nghĩa nguyên tắc kinh doanh, công thức tính, decision rules và routing tới công cụ đo lường. Mọi câu trả lời dạng "nên đầu tư vào đâu", "use case nào tiềm năng", "phân bổ nguồn lực thế nào" BẮT BUỘC tham chiếu file này trước khi kết luận.
>
> Nguồn gốc nội dung: `hienho_master_doc.md` (mục 4.3 KPI, 4.3 URL Governance, 4.4 A/B Testing, 4.5 SEO Inventory), `AGENT_OPERATING_CONTRACT.md`, `EVIDENCE_CONTRACT.md`.

---

## 1. NHIỆT KẾ KPI - TỪ BUSINESS Xuống WEB METRIC

Nguyên tắc: web metric chỉ có nghĩa khi gắn được vào business metric. Trình bày tăng trưởng traffic mà không quy về New User / MAU / Revenue là "naked numbers" - vi phạm output contract.

| Tầng | Metric | Định nghĩa chuẩn | Nguồn |
|---|---|---|---|
| Business | New User | Install → Register | momoapp.onelink.vn funnel |
| Business | MAU | Cashin event | Onelink MoMo |
| Business | MEU | Tương tác tính năng trong app | Onelink MoMo |
| Business | DLU | PLG tool engagement | PLG tools |
| Web | Organic Traffic | Sessions từ Organic channel | GA4 |
| Web | AI Citation Rate | MoMo được cite trong AI engine responses | GEO monitoring |
| Market | SoV | % brand search MoMo / tổng brand search thị trường | Keyword tool |

**Quy tắc diễn giải:**
- Traffic tăng nhưng W2A CVR giảm → tăng trưởng "rỗng", cần điều tra chất lượng traffic trước khi ăn mừng.
- Một use case chỉ đáng đầu tư khi thỏa đồng thời: (a) Search Volume thị trường đủ lớn, (b) fit Company Direction (Credit, Insurance, BNPL - Financial), (c) có path rõ ràng tới New User/MAU.

---

## 2. FUNNEL MATH - WEB-TO-APP

### 2.1 Funnel chuẩn

```
Organic Traffic → Onelink Click → App Store → Install → Register → KYC → Cashin → MAU
```

- **Track 1** (`onelink.momo.vn`): existing users - Open + Action.
- **Track 2** (`momoapp.onelink.vn`): new users - Install → Register → KYC → Cashin → MAU.
- New User = Install → Register (định nghĩa business, KHÔNG phải sessions hay clicks).

### 2.2 Cách tính step CVR từ Data Mart

Data Mart SQLite (`07_REPORTS/data/performance.sqlite` hoặc `cache/performance.sqlite`):

- `ga4_landing_pages`: sessions, onelink_clicks_track1/2 theo landing page + channel_group.
- `fact_daily_performance`: daily PV/sessions/users + target pacing theo tháng.
- `gsc_search_analytics`: impressions, clicks, CTR, position theo query/page.

Công thức chuẩn:
- **W2A Click CVR** = `(onelink_clicks_track1 + onelink_clicks_track2) / sessions` per landing page hoặc hub.
- **Hub W2A CVR** = tổng W2A clicks / tổng sessions của hub (xem `v_hub_performance`).
- **Quick Win Potential Gain** = impressions × (CTR benchmark của vị trí mục tiêu - CTR thực tế). Xem `query_analytics.py --quick-wins` (đã implement sẵn).

### 2.3 Giả định chuyển đổi hiện có trong repo

- `scenario_simulator.py` dùng giả định **40% W2A Click → Install** khi ước tính New User. Đây là GIẢ ĐỊNH NỘI BỘ, không phải benchmark đo được - khi trình bày phải ghi rõ "giả định 40%" hoặc thay bằng tỷ lệ thực tế nếu có data AppsFlyer.

### 2.4 Đọc funnel drop-off

- Drop-off lớn nhất thường ở Onelink → Install (app store friction) và Install → Register (onboarding friction).
- Khi phân tích drop-off: luôn chỉ rõ step nào, magnitude bao nhiêu so với kỳ trước/baseline, và có đủ data không (nếu funnel in-app không track được từ web side thì nói thẳng).

---

## 3. NGUYÊN TẮC KINH DOANH CỐT LÕI

### 3.1 SEO/GEO First → Business

Mọi đề xuất SEO/GEO phải trả lời được: tạo ra bao nhiêu New User/MAU/Revenue kỳ vọng, trong bao lâu. Ranking mà không gắn business outcome = hoạt động vô nghĩa về mặt growth.

### 3.2 Search Intent trước mọi thứ

Phân loại intent (Informational / Commercial / Transactional / Navigational) TRƯỚC khi đề xuất content hoặc tối ưu. Sai intent = traffic tăng nhưng CVR sập.

### 3.3 SoV làm thước đo thị trường

Ngưỡng chuẩn (master doc 4.5):
- SoV > 40%: Market Leader - duy trì, mở rộng sang use case lân cận.
- SoV 20-40%: Trung bình - có cơ hội tăng trưởng rõ ràng.
- SoV < 20%: Gap lớn - cần đầu tư nhưng phải chứng minh volume đủ lớn để justify.

### 3.4 Information Gain & Anti-LLM Moat

Content chỉ đáng đầu tư khi có data/góc nhìn không scrape được (PLG tools: calculator, simulator, checker tạo unique data). Content generic trùng lặp sẽ thua cả Google lẫn AI engines.

### 3.5 Traffic Dichotomy

Non-Paid (Organic, Direct, AI Traffic, Referral) là kênh bền vững cốt lõi; Paid là kênh mua traffic. Phân tích luôn tách 2 nhóm - không bao giờ gộp chung khi báo cáo.

### 3.6 YMYL/E-E-A-T Gate

Mọi content tài chính bắt buộc qua Foundation Checklist + named author policy. Content tài chính không đạt E-E-A-T không được publish dù keyword volume lớn.

### 3.7 PLG/Utilities-Led SEO

Ưu tiên build tool (CIC checker, loan calculator, insurance comparison) tạo DLU/MAU trực tiếp - đây là moats có compounding effect, khác với content one-shot.

### 3.8 URL Governance → Business Impact

4 levels can thiệp (master doc 4.3, đã bỏ 410 Gone):
1. **Nofollow + Sitemap removal**: low-value, crawl waste.
2. **301/308 Redirect**: consolidation, topical dilution - chuyển equity về Hub/Pillar.
3. **Noindex**: loại khỏi index, giữ UX.
4. **Mandatory content update**: YMYL outdated, AI citation risk.

Mapping sang growth: Level 2-3 là đòn bẩy tăng trưởng hữu cơ nhanh nhất cho site lớn (3670+ URLs audited trong Zero-Traffic project).

---

## 4. CÔNG CỤ TÍNH TOÁN - ROUTING BẮT BUỘC

| Câu hỏi/Nhu cầu | Tool | Ghi chú |
|---|---|---|
| A/B test có ý nghĩa thống kê? | `scripts/lib/ab_test_evaluator.py` | Two-proportion z-test, p-value, 95% CI, MDE |
| What-if: cắt ads, dịch traffic, lift CVR? | `scripts/lib/scenario_simulator.py` | 4 kịch bản có sẵn, đọc trực tiếp Data Mart |
| Mùa vụ, dự báo đa kịch bản | `scripts/lib/forecast_engine.py` | Ngoại suy từ theme_seasonality |
| Ưu tiên sáng kiến (RICE) | `scripts/prioritize_initiatives.py` | Xếp hạng theo Reach/Impact/Confidence/Effort |
| Chẩn đoán tại sao tăng/giảm | `scripts/diagnose_performance.py` | Root cause drill-down |
| Anomaly, đứt gãy W2A | `scripts/detect_anomalies.py` | Phát hiện outlier so với baseline |
| Tra cứu đa chiều SQL | `scripts/query_analytics.py` | Hubs, W2A drivers, quick wins, cannibalization |
| Đối soát quyết định đã chốt | `scripts/track_decisions.py --audit` | Closed-loop: baseline → target → actual |

**Quy tắc:** khi user hỏi dạng phân tích định lượng mà repo có tool chuyên biệt → PHẢI chạy tool lấy số thật, không tự ước lượng bằng model. Kết quả tool phải gắn `as_of`/period theo EVIDENCE_CONTRACT.

---

## 5. DECISION RULES - KHI NÀO LÀM GÌ

### 5.1 Scale / Maintain / Kill

| Tình huống | Hành động |
|---|---|
| SoV > 40% + CVR trên baseline + volume lớn | Scale - mở rộng sang spoke/use case lân cận |
| SoV 20-40% + có quick wins (pos 4-15, imp cao, CTR thấp) | Tối ưu trước - quick wins ROI cao nhất |
| SoV < 20% + volume nhỏ + không fit financial direction | Kill hoặc park - không justify dev/content resource |
| Traffic tăng nhưng W2A CVR giảm liên tục | Điều tra UX/funnel trước khi đầu tư thêm traffic |
| URL mất impressions + có impressions trước đó | Chạy chuỗi lost-impressions → zero-impressions → audit HTTP status |

### 5.2 Ưu tiên nguồn lực

1. Quick wins SEO (pos 4-15) trước - effort thấp, impact đo được ngay.
2. PLG tools - compounding, tạo DLU/MAU.
3. Content mới - chỉ khi đã có keyword map + intent rõ + E-E-A-T pass.
4. Technical fixes - theo impact lên crawl/index, không fix tràn lan.

### 5.3 Ngưỡng "đủ dữ liệu để kết luận"

- A/B test: cần đạt MDE sample size, p < 0.05 mới được declare winner. Chưa đủ mẫu → "cần chạy thêm", cấm kết luận sớm.
- Trend analysis: tối thiểu so sánh cùng kỳ (WoW/YoY) hoặc cùng độ dài kỳ trước - cấm so sánh kỳ cụt với kỳ đủ.
- SoV/benchmark: chỉ dùng số từ keyword tool có ghi nguồn + thời điểm lấy.

---

## 6. ANTI-PATTERNS - CẤM TUYỆT ĐỐI

1. **Cấm dự báo tương lai như fact**: "tháng sau sẽ đạt X" chỉ được nói dưới dạng scenario/kịch bản có giả định ghi rõ, hoặc output của `forecast_engine.py` kèm confidence.
2. **Cấm suy diễn nhân quả**: correlation ≠ causation. "Traffic giảm vì Google update" chỉ nói được khi có evidence (GSC annotation, timing, third-party confirm). Mặc định: "cần kiểm tra thêm".
3. **Cấm gộp Non-Paid + Paid** khi phân tích hiệu suất.
4. **Cấm dùng số không truy được nguồn** - mọi con số phải link tới file/field cụ thể (EVIDENCE_CONTRACT).
5. **Cấm khuyến nghị mà không có expected outcome đo được** - mọi action item phải kèm metric + baseline + review date.
6. **Cấm so sánh chéo kỳ khác độ dài** (MTD 15 ngày vs full tháng trước) mà không normalize.

---

## 7. EVIDENCE & CLOSED-LOOP

- Mọi phân tích growth có số liệu → build evidence JSON theo `EVIDENCE_CONTRACT.md`, chạy `validate_evidence.py` trước khi trình bày.
- Quyết định chiến lược quan trọng (đầu tư hub mới, kill use case, thay đổi funnel) → ghi vào `track_decisions.py --add` với baseline + target + review date 14-30 ngày.
- Sau review date → `track_decisions.py --audit` tự đối soát actual vs target từ Data Mart. Kết quả feed ngược vào phân tích sau (tránh lặp sai lầm).

---

## 8. FAST CHECKLIST TRƯỚC KHI TRẢ LỜI CÂU HỎI GROWTH

- [ ] Câu trả lời quy về business metric nào? (New User / MAU / Revenue)
- [ ] Số liệu lấy từ đâu, kỳ nào, `as_of` ngày nào?
- [ ] Đã phân biệt fact / inference / recommendation chưa?
- [ ] Có tool chuyên biệt trong repo nên chạy không? (xem mục 4)
- [ ] So sánh có cùng kỳ/độ dài không?
- [ ] Nếu đề xuất hành động: có expected outcome + cách đo không?
- [ ] Có vi phạm anti-pattern nào ở mục 6 không?

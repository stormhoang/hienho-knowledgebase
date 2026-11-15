---
name: business-growth
description: Tư vấn và phân tích Business Growth cho Web Platform - funnel W2A, unit economics, SoV, quyết định scale/kill use case, phân bổ nguồn lực, what-if scenario. Trigger khi user hỏi dạng "nên đầu tư vào đâu", "use case nào tiềm năng", "tại sao CVR thấp", "phân bổ ngân sách", "growth strategy", "prioritize".
---

# SKILL: BUSINESS GROWTH ANALYSIS (/business-growth)

## 1. MỤC TIÊU
Trả lời các câu hỏi growth bằng reasoning kinh doanh có căn cứ số liệu - KHÔNG phải liệt kê số liệu thô.

## 2. QUY TRÌNH BẮT BUỘC TRƯỚC KHI TRẢ LỜI

1. **Đọc playbook**: [`00_HARNESS_CORE/GROWTH_PRINCIPLES.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/GROWTH_PRINCIPLES.md) - chứa KPI hierarchy, funnel math, decision rules, anti-patterns.
2. **Lấy baseline**: đọc [`07_REPORTS/data/benchmarks/web_growth_benchmarks.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/benchmarks/web_growth_benchmarks.json) (chạy `./.venv/bin/python scripts/build_benchmarks.py` nếu stale > 7 ngày so với synced_at).
3. **Chạy tool chuyên biệt** theo câu hỏi (xem bảng routing trong GROWTH_PRINCIPLES.md mục 4):
   - Phân tích định lượng → `query_analytics.py`, `diagnose_performance.py`, `detect_anomalies.py`
   - What-if → `scenario_simulator.py`
   - A/B significance → `ab_test_evaluator.py`
   - Ưu tiên sáng kiến → `prioritize_initiatives.py`
   - Mùa vụ → `forecast_engine.py`
4. **Evidence**: câu trả lời có số liệu → build evidence JSON + `validate_evidence.py` trước khi trình bày.
5. **Quyết định lớn** → ghi `track_decisions.py --add` với baseline/target/review-date.

## 3. CẤU TRÚC CÂU TRẢ LỜI (bắt buộc theo AGENTS.md)

- Action Title: kết luận 1 câu (chỉ số + hiện trạng + bản chất).
- What: số liệu sạch kèm benchmark so sánh (dùng `web_growth_benchmarks.json`, không so cảm tính).
- So What: tác động lên New User / MAU / Revenue.
- Now What: hành động cụ thể + expected outcome đo được + review date.

## 4. NGUYÊN TẮC CỨNG (vi phạm = trả lời sai)

- Mọi con số phải truy về source (Data Mart JSON/DB, file report) - không ước lượng bằng model.
- Phân biệt rõ fact / inference / recommendation.
- Cấm dự báo tương lai như fact; scenario phải ghi giả định.
- Cấm suy diễn nhân quả khi chưa có evidence.
- Non-Paid và Paid luôn tách riêng.
- So sánh phải cùng kỳ/độ dài.
- Thiếu data → nói "không đủ dữ liệu, cần kiểm tra X" thay vì bịa.

## 5. STALENESS RULE

- `web_growth_benchmarks.json` có `as_of` + `generated_at`. Nếu `as_of` cũ hơn kỳ đang phân tích → cảnh báo user và đề xuất chạy lại `build_benchmarks.py` sau khi `sync_all_data.py`/`sync_ga4_master.py` cập nhật Data Mart.

# EVIDENCE CONTRACT

Mọi kết luận có số liệu hoặc khẳng định thực tế phải có evidence record. Evidence không thay thế reasoning, nhưng là điều kiện tối thiểu để kết luận được xem là grounded.

## Schema tối thiểu

```json
{
  "as_of": "2026-11-05",
  "period": "2026-11-01/2026-11-04",
  "claims": [
    {
      "id": "traffic_mtd",
      "claim": "MTD đạt 370310 PV",
      "value": 370310,
      "metric": "pageviews_mtd",
      "unit": "PV",
      "source": "07_REPORTS/data/monthly_11_2026_mtd_4d.json",
      "source_field": "actual_mtd_pv",
      "evidence_type": "fact",
      "confidence": "high"
    }
  ]
}
```

## Quy tắc kiểm chứng

- Mỗi claim phải có `source`, `period`, `evidence_type` và `confidence`.
- JSON đầu vào có thể truyền qua stdin, không cần lưu file cho mỗi câu hỏi. Chỉ lưu record khi cần audit hoặc tái lập báo cáo.
- `source` nội bộ phải là file trong workspace; URL chỉ xác minh cú pháp, Agent vẫn phải tự kiểm tra nội dung nguồn ngoài.
- Với fact từ JSON, `source_field` là đường dẫn key phân tách bằng dấu chấm và `value` phải khớp giá trị gốc. Giá trị tính toán phải ghi rõ phép tính và các claim đầu vào; validator chưa tự chứng minh phép tính.
- Với snapshot `monthly_MM_YYYY_mtd_Nd.json`, `period` phải khớp `YYYY-MM-01/YYYY-MM-NN` và `days_elapsed` phải khớp tên file.
- Phép tính `calculation: {"operator": "subtract", "inputs": ["claim_mới", "claim_cũ"]}` được đối chiếu với hai claim đầu vào. Chỉ dùng để tính mức tăng giữa hai snapshot cùng tháng.
- `as_of` không được muộn hơn ngày hiện tại.
- Dữ liệu quá cũ phải được đánh dấu stale theo ngưỡng của capability.
- `fact`, `inference` và `recommendation` không được trộn lẫn.
- Nếu hai claim dùng cùng metric, cùng period nhưng khác value, phải báo conflict.
- Không được dùng claim có conflict làm kết luận chắc chắn nếu chưa giải quyết.

## QUY TẮC CHỐNG BỊA SỐ (ANTI-FABRICATION - BẮT BUỘC)

Mọi con số trong phân tích, kế hoạch, chiến lược hoặc báo cáo phải thuộc 1 trong 4 loại có nhãn rõ:

| Loại | Điều kiện | Cách ghi |
| :--- | :--- | :--- |
| `fact` | Truy được về file/command output trong session | Ghi nguồn: file + field/period |
| `calculation` | Phép tính từ các fact đã cite | Ghi công thức + input claims |
| `scenario` | Con số mô phỏng/giả định | BẮT BUỘC chạy `scripts/lib/scenario_simulator.py` hoặc `forecast_engine.py`; cấm tự nội suy bằng model |
| `benchmark` | Số tham chiếu thị trường | BẮT BUỘC có nguồn ngoài (báo cáo, tool) + ghi "benchmark, không phải số MoMo" |

**Các hành vi CẤM:**

- Cấm "số mục tiêu ngược": suy ra con số cần đạt để hợp thức hóa kế hoạch (VD: "cần 500K PV/tháng" khi không có cơ sở) rồi trình bày như số thực tế. Nếu là target đề xuất → ghi rõ `target đề xuất - chờ approve`, tách khỏi fact.
- Cấm nội suy/tự ước lượng khi thiếu data (VD: "tháng này chắc khoảng X" dựa trên cảm giác). Thiếu data → nói thiếu, chỉ rõ cần export/bổ sung gì.
- Cấm trộn scenario vào fact: con số từ scenario_simulator/forecast_engine phải luôn kèm nhãn kịch bản, không trình bày ngang hàng số đo thực tế.
- Cấm bịa benchmark: "trung bình ngành khoảng X%" không nguồn → xóa hoặc ghi `[cần verify]`.
- Cấm "làm tròn có lợi": làm tròn số liệu theo hướng có lợi cho luận điểm; mọi làm tròn phải giữ nguyên thứ tự độ lớn và ghi rõ.

**Khi không chắc:** trả lời "không có dữ liệu để kết luận X - cần chạy Y / export Z". Một câu trả lời thiếu số nhưng trung thực luôn tốt hơn một kế hoạch đẹp với số bịa.

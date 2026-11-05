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
- `as_of` không được muộn hơn ngày hiện tại.
- Dữ liệu quá cũ phải được đánh dấu stale theo ngưỡng của capability.
- `fact`, `inference` và `recommendation` không được trộn lẫn.
- Nếu hai claim dùng cùng metric, cùng period nhưng khác value, phải báo conflict.
- Không được dùng claim có conflict làm kết luận chắc chắn nếu chưa giải quyết.

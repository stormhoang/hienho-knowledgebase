# KHUNG ĐÁNH GIÁ VÀ SẮP XẾP ƯU TIÊN YÊU CẦU SẢN PHẨM (PRODUCT PRIORITIZATION FRAMEWORK)

Khung đánh giá ưu tiên giúp Product Manager sàng lọc danh sách yêu cầu khổng lồ (Backlog) để chọn ra những hạng mục mang lại giá trị cao nhất với chi phí thực hiện tối ưu.

---

## 1. MÔ HÌNH ƯU TIÊN RICE (RICE SCORING MODEL)

Áp dụng cho việc chấm điểm định lượng các tính năng hoặc dự án:

$$RICE Score= \frac{Reach\times Impact\times Confidence}{Effort}$$

- **Reach (Độ phủ):** Số lượng người dùng bị ảnh hưởng trong một khoảng thời gian nhất định.
- **Impact (Mức độ tác động):** Mức độ ảnh hưởng đến trải nghiệm hoặc chỉ số kinh doanh (3 = Cực lớn, 2 = Lớn, 1 = Vừa, 0.5 = Nhỏ).
- **Confidence (Độ tin cậy):** Mức độ tự tin vào dữ liệu phân tích (100% = Rất chắc chắn, 80% = Trung bình, 50% = Giả định).
- **Effort (Chi phí nguồn lực):** Tổng thời gian làm việc của team (tính theo Man-month hoặc Person-weeks).

---

## 2. MA TRẬN 4 GÓC PHẦN TƯ UIC (URGENCY - IMPORTANCE - COST)

Áp dụng cho việc ra quyết định nhanh trong thực chiến sản phẩm (Triết lý Tencent):

```
                       TẦM QUAN TRỌNG (IMPORTANCE)
                                   ▲
                                   │
      GÓC PHẦN TƯ 2                │      GÓC PHẦN TƯ 1
  Quan trọng / Không khẩn cấp      │   Quan trọng / Khẩn cấp
  -> Lên kế hoạch chiến lược       │   -> ƯU TIÊN XỬ LÝ NGAY
                                   │
───────────────────────────────────┼───────────────────────────────────► MỨC ĐỘ KHẨN CẤP
                                   │                                      (URGENCY)
      GÓC PHẦN TƯ 4                │      GÓC PHẦN TƯ 3
 Không quan trọng / Không khẩn cấp │   Không quan trọng / Khẩn cấp
  -> Trì hoãn hoặc Loại bỏ         │   -> Ủy quyền / Xử lý nhanh
                                   │
```

- **Kích thước chi phí (Cost):** Yêu cầu có cùng điểm quan trọng và khẩn cấp thì ưu tiên làm tính năng có Chi phí (Cost) thấp trước để giải phóng tài nguyên.

---

## 3. NGUYÊN TẮC VÀNG TRONG SẮP XẾP ƯU TIÊN

1. **Thoát khỏi bẫy "Ai to tiếng hơn thì làm trước":** Dùng số liệu và ma trận ưu tiên minh bạch thay vì ý kiến chủ quan.
2. **Ưu tiên sự cố khả dụng (Usability Bugs):** Các lỗi ảnh hưởng đến dòng tiền hoặc trải nghiệm cốt lõi luôn được xử lý trước tiên.
3. **Loại bỏ tính năng ít giá trị:** Sẵn sàng từ bỏ các yêu cầu có chi phí cao nhưng điểm tác động thấp.

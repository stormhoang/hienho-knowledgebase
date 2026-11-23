# ADS SEGMENT DICTIONARY (TỪ ĐIỂN PHÂN KHÚC ADS MANAGER - PHIÊN BẢN 2.0)

> **Quy chuẩn nguồn sự thật duy nhất (SSOT):** Bảng danh mục Segment dịch vụ chuẩn hóa dùng chung cho toàn bộ nền tảng Ads Manager và Web Platform momo.vn.

## 1. Nguyên Tắc Phân Định: Segment (Dịch Vụ) vs Page Type (Loại Trang)

- **Segment (Dịch vụ / Sản phẩm kinh doanh):** Đại diện cho dịch vụ kinh doanh cụ thể (ví dụ: `Vay Nhanh`, `Ví Trả Sau`, `Cinema`, `Vé Xe`, `Y Tế`, `Dịch Vụ Công`). Đây là trường chính mà PM/Marketer lựa chọn khi tạo chiến dịch quảng cáo.
- **Page Type (Loại trang / Định dạng nội dung):** Đại diện cho loại hình trang hiển thị (ví dụ: `Blog`, `Tin Tức`, `Hỏi đáp`, `Guide`, `Landing Page`, `Home Page`). Đây là trường lọc phụ để thu hẹp phạm vi nhắm mục tiêu.

### Các Chuẩn Hóa Cốt Lõi Được Áp Dụng:
1. **Hợp nhất Cinema:** Toàn bộ rạp chiếu phim, bài đánh giá phim, trang cụm rạp CGV/Lotte/Galaxy/BHD quy tụ về 1 Segment duy nhất: `Cinema` (`seg_cinema`).
2. **Hợp nhất phân mảnh:** `Student Pass` + `Student Hub` gộp thành `Student`; `Game` + `Nạp thẻ Game` gộp thành `Game`; `Phạt Nguội` + `Nộp Phạt CSGT` gộp thành `Phạt Nguội`.
3. **Sửa lệch Hub:** `Điểm Tín Dụng`, `Tiệm Vàng Online` chuyển về `Financial Hub`; `Nhận Tiền Quốc Tế` chuyển về `Payment Hub`.
4. **Bổ sung 6 Segment còn thiếu:** `Y Tế`, `Dịch Vụ Công`, `Vé Tàu`, `Bảo Hiểm Du Lịch`, `Đăng Kiểm`, `Tiện Ích Đời Sống`.
5. **Bổ sung Segment Toàn Website:** Nhận diện các trang CSKH, bảo mật, giới thiệu ví chung (`seg_toan_website`).
6. **Giải cứu 2.297 URL vô thừa nhận:** Tự động phân loại toàn bộ bài viết trong `/blog/`, `/tin-tuc/`, `/hoi-dap/`, `/huong-dan/` về đúng Segment tương ứng.

## 2. Thống Kê Tổng Quan (Cập nhật: 2026-11-18)

- **Tổng số Segment hợp lệ:** 78 dịch vụ kinh doanh.
- **Tổng số Quy tắc URL bao phủ:** 3,012 rules.
- **Tổng số URL đã phân loại:** 28,299 URLs trên toàn bộ website momo.vn.
- **Số lượng Hub:** 14 Hub dịch vụ.

## 3. Danh Mục Segment Chi Tiết Theo Hub

### Financial Hub (Dịch vụ Tài chính)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ví Trả Sau** | `seg_vi_tra_sau` | 116 | 137 | Blog, Campaign Page, Guide (+5) | `https://www.momo.vn/vi-tra-sau/*` |
| **Quản Lý Chi Tiêu** | `seg_quan_ly_chi_tieu` | 97 | 21 | Blog, Landing Page, Page | `https://www.momo.vn/quan-ly-chi-tieu` |
| **Vay Nhanh** | `seg_vay_nhanh` | 70 | 166 | Blog, Guide, Home Page (+5) | `https://www.momo.vn/vay-nhanh` |
| **Chứng Khoán** | `seg_chung_khoan` | 41 | 40 | Blog, Hỏi đáp, Landing Page (+2) | `https://www.momo.vn/chung-khoan` |
| **Tiết Kiệm Online** | `seg_tiet_kiem_online` | 18 | 40 | Blog, Landing Page, Page (+2) | `https://www.momo.vn/tiet-kiem-online` |
| **Điểm Tín Dụng** | `seg_diem_tin_dung` | 17 | 10 | Blog, Home Page, Landing Page | `https://www.momo.vn/diem-tin-dung` |
| **Trung Tâm Tài Chính** | `seg_trung_tam_tai_chinh` | 16 | 75 | Blog, Landing Page, Page (+2) | `https://www.momo.vn/tai-chinh` |
| **Mở Thẻ Tín Dụng** | `seg_mo_the_tin_dung` | 13 | 48 | Blog, Hỏi đáp, Landing Page (+2) | `https://www.momo.vn/mo-the-tin-dung` |
| **Chứng Chỉ Quỹ** | `seg_chung_chi_quy` | 11 | 4 | Blog, Landing Page, Page | `https://www.momo.vn/chung-chi-quy` |
| **Mở tài khoản ngân hàng** | `seg_mo_tai_khoan_ngan_hang` | 6 | 3 | Landing Page | `https://www.momo.vn/mo-tai-khoan-ngan-hang` |
| **Thanh Toán Thẻ Tín Dụng** | `seg_thanh_toan_the_tin_dung` | 3 | 3 | Landing Page, Page | `https://www.momo.vn/thanh-toan-the-tin-dung` |
| **Tỷ Giá** | `seg_ty_gia` | 2 | 8 | Blog, Page, Tool Page | `https://www.momo.vn/tai-chinh/ty-gia/*` |
| **Giá Vàng** | `seg_gia_vang` | 2 | 2 | Page, Tin Tức, Tool Page | `https://www.momo.vn/tai-chinh/gia-vang/*` |
| **Lãi Suất** | `seg_lai_suat` | 2 | 1 | Page, Tool Page | `https://www.momo.vn/tai-chinh/lai-suat` |
| **Quỹ Nhóm** | `seg_quy_nhom` | 2 | 1 | Landing Page | `https://www.momo.vn/quy-nhom` |
| **Túi Thần Tài** | `seg_tui_than_tai` | 1 | 21 | Hỏi đáp, Page, Tin Tức | `https://www.momo.vn/tui-than-tai` |
| **Trả Góp Apple** | `seg_tra_gop_apple` | 1 | 1 | Page | `https://www.momo.vn/tra-gop-san-pham-apple` |
| **Thanh Toán Khoản Vay** | `seg_thanh_toan_khoan_vay` | 1 | 1 | Page | `https://www.momo.vn/thanh-toan-khoan-vay` |
| **Sàn Đầu Tư** | `seg_san_dau_tu` | 1 | 1 | Page | `https://www.momo.vn/san-dau-tu` |
| **Tiệm Vàng Online** | `seg_tiem_vang_online` | 1 | 1 | Landing Page | `https://www.momo.vn/tiem-vang-online` |
| **Quỹ** | `seg_quy` | 1 | 0 | Mini Web | `https://www.momo.vn/quy-nhom*` |

### Insurance Hub (Bảo hiểm)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bảo Hiểm Ô Tô** | `seg_bao_hiem_o_to` | 77 | 96 | Blog, Home Page, Hỏi đáp (+4) | `https://www.momo.vn/bao-hiem-o-to` |
| **Bảo Hiểm Y Tế** | `seg_bao_hiem_y_te` | 39 | 63 | Blog, Guide, Home Page (+4) | `https://www.momo.vn/bao-hiem-y-te` |
| **Bảo Hiểm Xe Máy** | `seg_bao_hiem_xe_may` | 37 | 34 | Blog, Guide, Home Page (+3) | `https://www.momo.vn/bao-hiem-xe-may` |
| **Bảo Hiểm** | `seg_bao_hiem` | 16 | 86 | Blog, Home Page, Hỏi đáp (+4) | `https://www.momo.vn/bao-hiem/tra-cuu-bao-hiem` |
| **Bảo Hiểm Du Lịch** | `seg_bao_hiem_du_lich` | 6 | 9 | Landing Page, Product Page | `https://www.momo.vn/bao-hiem-du-lich` |
| **Bảo Hiểm Sức Khỏe** | `seg_bao_hiem_suc_khoe` | 1 | 7 | Blog, Hỏi đáp, Landing Page (+1) | `https://www.momo.vn/bao-hiem-suc-khoe` |
| **Bảo Hiểm Xã Hội** | `seg_bao_hiem_xa_hoi` | 1 | 1 | Landing Page | `https://www.momo.vn/bao-hiem-xa-hoi` |

### Travel Hub (Du lịch và Đi lại)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OTA** | `seg_ota` | 1000 | 703 | Blog, Destination Page, Home Page (+6) | `https://www.momo.vn/du-lich-di-lai` |
| **Vé Xe** | `seg_ve_xe` | 130 | 5,390 | Blog, Guide, Home Page (+5) | `https://www.momo.vn/ve-xe` |
| **Vé Tàu** | `seg_ve_tau` | 35 | 31 | Hỏi đáp, Landing Page, News (+3) | `https://www.momo.vn/ve-tau/*` |
| **Cross Border** | `seg_cross_border` | 5 | 5 | Landing Page | `https://www.momo.vn/thanh-toan-quoc-te` |

### Cinema Hub (Phim và Giải trí)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cinema** | `seg_cinema` | 160 | 1,025 | Blog, Cineplex Page, Guide (+6) | `https://www.momo.vn/cinema` |

### Telco Hub (Viễn thông và Nạp thẻ)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Data** | `seg_data` | 252 | 80 | Blog, Guide, Home Page (+5) | `https://www.momo.vn/nap-data` |
| **Sim** | `seg_sim` | 165 | 65 | Blog, Home Page, News (+1) | `https://www.momo.vn/sim-so-dep` |
| **Esim** | `seg_esim` | 27 | 45 | Blog, Landing Page, News (+1) | `https://www.momo.vn/esim-du-lich` |
| **Nạp tiền điện thoại** | `seg_nap_tien_dien_thoai` | 2 | 1 | Landing Page | `https://www.momo.vn/nap-tien-dien-thoai*` |
| **Airtime** | `seg_airtime` | 1 | 0 | Landing Page | `https://www.momo.vn/airtime*` |

### Vehicle Hub (Xe và Tiện ích Giao thông)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phạt Nguội** | `seg_phat_nguoi` | 19 | 38 | Blog, Home Page, Landing Page (+3) | `https://www.momo.vn/phat-nguoi` |
| **Tiện Ích Giao Thông** | `seg_tien_ich_giao_thong` | 13 | 15 | Blog, Landing Page, Mini Web | `https://www.momo.vn/tien-ich-giao-thong` |
| **Phí Không Dừng** | `seg_phi_khong_dung` | 9 | 14 | Blog, Hỏi đáp, Landing Page (+2) | `https://www.momo.vn/phi-khong-dung` |
| **Đăng Kiểm** | `seg_dang_kiem` | 5 | 4 | Blog, Landing Page, Page | `https://www.momo.vn/dang-kiem/*` |
| **Trạm sạc** | `seg_tram_sac` | 4 | 1 | Mini Web, Tool Page | `https://www.momo.vn/tien-ich-giao-thong/tr...` |
| **Cây xăng** | `seg_cay_xang` | 4 | 1 | Mini Web, Tool Page | `https://www.momo.vn/tien-ich-giao-thong/ca...` |
| **Giá xăng** | `seg_gia_xang` | 4 | 1 | Mini Web, Tool Page | `https://www.momo.vn/tien-ich-giao-thong/gi...` |
| **Garage** | `seg_garage` | 2 | 0 | Tool Page | `https://www.momo.vn/tien-ich-giao-thong/ga...` |
| **Hãng Xe** | `seg_hang_xe` | 2 | 0 | Tool Page | `https://www.momo.vn/tien-ich-giao-thong/ha...` |

### Billpay Hub (Hóa đơn và Đời sống)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Điện** | `seg_dien` | 16 | 73 | Blog, Guide, Hỏi đáp (+3) | `https://www.momo.vn/tin-tuc/khuyen-mai/the...` |
| **Billpay** | `seg_billpay` | 11 | 10 | Landing Page | `https://www.momo.vn/thanh-toan-hoa-don` |
| **Nước** | `seg_nuoc` | 10 | 23 | Blog, Guide, Hỏi đáp (+2) | `https://www.momo.vn/nuoc` |
| **Internet** | `seg_internet` | 9 | 16 | Blog, Guide, Hỏi đáp (+1) | `https://www.momo.vn/internet*` |
| **Phí Xét Tuyển** | `seg_phi_xet_tuyen` | 6 | 5 | Blog, Landing Page | `https://www.momo.vn/phi-xet-tuyen` |
| **Truyền Hình** | `seg_truyen_hinh` | 4 | 6 | Guide, Hỏi đáp, Landing Page | `https://www.momo.vn/truyen-hinh` |
| **Chung Cư** | `seg_chung_cu` | 4 | 1 | Landing Page | `https://www.momo.vn/chung-cu` |
| **Y Tế** | `seg_y_te` | 3 | 7 | Landing Page, Merchant page, Page | `https://www.momo.vn/thanh-toan-momo-benh-v...` |
| **Học Phí** | `seg_hoc_phi` | 3 | 25 | Blog, Hỏi đáp, Landing Page (+1) | `https://www.momo.vn/thanh-toan-momo-the-ho...` |
| **Dịch Vụ Công** | `seg_dich_vu_cong` | 2 | 8 | Hỏi đáp, Landing Page, Page | `https://www.momo.vn/dich-vu-cong/*` |

### Merchant Hub (Đối tác và Doanh nghiệp)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Merchant** | `seg_merchant` | 163 | 17,780 | Blog, Home Page, Landing Page (+4) | `https://www.momo.vn/tho-dia-momo` |
| **Soundbox** | `seg_soundbox` | 46 | 20 | Blog, News, Page | `https://www.momo.vn/loa-momo` |

### Game Hub (Cộng đồng Game)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Game** | `seg_game` | 51 | 169 | Blog, FAQ, Guide (+5) | `https://www.momo.vn/nap-the-game` |

### Payment Hub (Thanh toán và Chuyển tiền)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P2P** | `seg_p2p` | 29 | 77 | Blog, Guide, Hỏi đáp (+4) | `https://www.momo.vn/chuyen-tien` |
| **Dịch vụ liên kết** | `seg_dich_vu_lien_ket` | 15 | 14 | Blog, Landing Page, Mini Web | `https://www.momo.vn/dat-xe-cong-nghe` |
| **Tiktok** | `seg_tiktok` | 11 | 9 | Blog, Guide, Home Page (+2) | `https://www.momo.vn/nap-xu-tiktok` |
| **Application Store** | `seg_application_store` | 8 | 7 | Landing Page | `https://www.momo.vn/uu-dai-icloud` |
| **Hoàn Tiền Mua Sắm** | `seg_hoan_tien_mua_sam` | 5 | 5 | Landing Page | `https://www.momo.vn/hoan-tien-mua-sam` |
| **Nhận Tiền Quốc Tế** | `seg_nhan_tien_quoc_te` | 2 | 13 | Blog, Hỏi đáp, Landing Page | `https://www.momo.vn/nhan-tien-quoc-te` |
| **XU** | `seg_xu` | 1 | 1 | Landing Page | `https://www.momo.vn/xu` |

### Student Hub (Gói Sinh viên)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Student** | `seg_student` | 12 | 22 | Blog, Landing Page, News (+1) | `https://www.momo.vn/student-pass/back-to-s...` |

### New User Hub (Khách hàng mới)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **New User** | `seg_new_user` | 40 | 15 | Landing Page, News | `https://www.momo.vn/xac-thuc-nfc` |

### Lottery Hub (Vé số)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vé số** | `seg_ve_so` | 7 | 20 | Blog, Guide, Hỏi đáp (+3) | `https://www.momo.vn/tin-tuc/thong-bao/huon...` |

### General Platform (Nền tảng và Tiện ích chung)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Khuyến mãi** | `seg_khuyen_mai` | 36 | 27 | Home Page, Landing Page, Page (+1) | `https://www.momo.vn/tin-tuc/khuyen-mai` |
| **Campaign** | `seg_campaign` | 34 | 28 | Campaign Page, Landing Page, Mini Web (+1) | `https://www.momo.vn/tin-tuc/khuyen-mai/gia...` |
| **Donation** | `seg_donation` | 23 | 109 | Landing Page, Page | `https://www.momo.vn/vi-nhan-ai` |
| **Trust** | `seg_trust` | 14 | 19 | Landing Page | `https://www.momo.vn/an-toan-bao-mat` |
| **Toàn Website** | `seg_toan_website` | 3 | 1,344 | Blog, Guide, Home Page (+3) | `https://www.momo.vn/` |
| **Tiện Ích Đời Sống** | `seg_tien_ich_doi_song` | 2 | 147 | Blog, Hỏi đáp, Tin Tức (+1) | `https://www.momo.vn/blog/than-so-hoc-*` |
| **Tìm Kiếm** | `seg_tim_kiem` | 2 | 0 | Mini Web | `https://www.momo.vn/tim-kiem` |
| **Tuyển Dụng** | `seg_tuyen_dung` | 2 | 0 | Landing Page | `https://www.momo.vn/careers` |

## 4. Hướng Dẫn Tích Hợp Vào Ads Manager

### Cấu trúc Payload Campaign khi tạo Ad:
```json
{
  "campaign_id": "camp_2026_q2_vaynhanh_01",
  "ad_name": "Floating Dock - Khoản vay nhanh 10 triệu",
  "target_segment": "seg_vay_nhanh",
  "target_page_types": ["Blog", "Landing Page"],
  "exclude_urls": ["/vay-nhanh/dieu-khoan"]
}
```

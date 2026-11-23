# ADS SEGMENT DICTIONARY (TỪ ĐIỂN PHÂN KHÚC ADS MANAGER)

> **Quy chuẩn nguồn sự thật duy nhất (SSOT):** Toàn bộ danh mục Segment trong Ads Manager được chuẩn hóa trực tiếp từ `project_name` trong bảng `DIM_URL` (`web_dim_page_url.csv`).

## 1. Nguyên Tắc Phân Định: Segment (Dịch Vụ) vs Page Type (Loại Trang)

Trong kiến trúc nhắm mục tiêu (Targeting) của Ads Manager, hệ thống phân biệt rạch ròi 2 khái niệm:

- **Segment (Dịch vụ / Sản phẩm kinh doanh):** Đại diện cho nghiệp vụ kinh doanh của MoMo (ví dụ: `Vay Nhanh`, `Ví Trả Sau`, `Bảo Hiểm Xe Máy`, `Cinema`, `Vé Xe`, `OTA`, `Túi Thần Tài`). Đây là trường chính mà PM/Marketer lựa chọn khi tạo chiến dịch quảng cáo.
- **Page Type (Loại trang / Định dạng nội dung):** Đại diện cho loại hình trang hiển thị (ví dụ: `Blog`, `Tin Tức`, `Hỏi đáp`, `Guide`, `Landing Page`, `Home Page`). Các định dạng này **không phải là Segment độc lập** mà là trường lọc phụ (Secondary Filter) nằm ngang qua các Segment.

### Điểm Chuẩn Hóa Cốt Lõi:
1. **Hợp nhất Cinema:** Toàn bộ các nhánh con (`Cinema_Home Page`, `Cinema_Page`, `Cinema_Blog`, `Cinema_Cineplex Page`, `Cinema_Landing Page`, `Cinema_News`) được quy tụ về một Segment duy nhất mang tên **`Cinema`** (mã `seg_cinema`).
2. **Bóc tách Blog, Tin Tức, Hỏi đáp:** Các nhãn `Blog`, `Tin Tức`, `Hỏi đáp`, `Guide` được chuyển về đúng bản chất là `Page Type`. Khi muốn đặt Ads trên bài viết blog về Vay Nhanh, PM sẽ chọn `Segment = Vay Nhanh` và tùy chọn `Page Type = Blog`.

## 2. Thống Kê Tổng Quan (Cập nhật: 2026-11-17)

- **Tổng số Segment hợp lệ:** 74 dịch vụ.
- **Tổng số Quy tắc URL bao phủ:** 2,995 rules.
- **Tổng số URL đã phân loại:** 25,980 URLs trên toàn bộ website momo.vn.
- **Phân bổ:** 14 Hub dịch vụ.

## 3. Danh Mục Segment Chi Tiết Theo Hub

### Financial Hub (Dịch vụ Tài chính)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ví Trả Sau** | `seg_vi_tra_sau` | 116 | 74 | Blog, Campaign Page, Home Page (+3) | `https://www.momo.vn/vi-tra-sau/*` |
| **Quản Lý Chi Tiêu** | `seg_quan_ly_chi_tieu` | 97 | 21 | Blog, Landing Page, Page | `https://www.momo.vn/quan-ly-chi-tieu` |
| **Vay Nhanh** | `seg_vay_nhanh` | 70 | 104 | Blog, Guide, Home Page (+3) | `https://www.momo.vn/vay-nhanh` |
| **Chứng Khoán** | `seg_chung_khoan` | 41 | 18 | Blog, Landing Page, Page | `https://www.momo.vn/chung-khoan` |
| **Tiết Kiệm Online** | `seg_tiet_kiem_online` | 18 | 18 | Landing Page, Page, Tool Page | `https://www.momo.vn/tiet-kiem-online` |
| **Trung Tâm Tài Chính** | `seg_trung_tam_tai_chinh` | 16 | 75 | Blog, Landing Page, Page (+2) | `https://www.momo.vn/tai-chinh` |
| **Mở Thẻ Tín Dụng** | `seg_mo_the_tin_dung` | 13 | 13 | Landing Page, Page | `https://www.momo.vn/mo-the-tin-dung` |
| **Chứng Chỉ Quỹ** | `seg_chung_chi_quy` | 11 | 3 | Blog, Landing Page, Page | `https://www.momo.vn/chung-chi-quy` |
| **Mở tài khoản ngân hàng** | `seg_mo_tai_khoan_ngan_hang` | 6 | 3 | Landing Page | `https://www.momo.vn/mo-tai-khoan-ngan-hang` |
| **Thanh Toán Thẻ Tín Dụng** | `seg_thanh_toan_the_tin_dung` | 3 | 3 | Landing Page, Page | `https://www.momo.vn/thanh-toan-the-tin-dung` |
| **Tỷ Giá** | `seg_ty_gia` | 2 | 5 | Page, Tool Page | `https://www.momo.vn/tai-chinh/ty-gia/*` |
| **Giá Vàng** | `seg_gia_vang` | 2 | 1 | Page, Tool Page | `https://www.momo.vn/tai-chinh/gia-vang/*` |
| **Lãi Suất** | `seg_lai_suat` | 2 | 1 | Page, Tool Page | `https://www.momo.vn/tai-chinh/lai-suat` |
| **Quỹ Nhóm** | `seg_quy_nhom` | 2 | 1 | Landing Page | `https://www.momo.vn/quy-nhom` |
| **Túi Thần Tài** | `seg_tui_than_tai` | 1 | 1 | Page | `https://www.momo.vn/tui-than-tai` |
| **Trả Góp Apple** | `seg_tra_gop_apple` | 1 | 1 | Page | `https://www.momo.vn/tra-gop-san-pham-apple` |
| **Thanh Toán Khoản Vay** | `seg_thanh_toan_khoan_vay` | 1 | 1 | Page | `https://www.momo.vn/thanh-toan-khoan-vay` |
| **Sàn Đầu Tư** | `seg_san_au_tu` | 1 | 1 | Page | `https://www.momo.vn/san-dau-tu` |
| **Quỹ** | `seg_quy` | 1 | 0 | Mini Web | `https://www.momo.vn/quy-nhom*` |

### Insurance Hub (Bảo hiểm)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bảo Hiểm Ô Tô** | `seg_bao_hiem_o_to` | 79 | 92 | Blog, Home Page, Landing Page (+3) | `https://www.momo.vn/bao-hiem-o-to` |
| **Bảo Hiểm Y Tế** | `seg_bao_hiem_y_te` | 39 | 38 | Blog, Home Page, Landing Page (+2) | `https://www.momo.vn/bao-hiem-y-te` |
| **Bảo Hiểm Xe Máy** | `seg_bao_hiem_xe_may` | 37 | 26 | Blog, Home Page, News (+1) | `https://www.momo.vn/bao-hiem-xe-may` |
| **Bảo Hiểm** | `seg_bao_hiem` | 20 | 17 | Home Page, Landing Page, Page (+1) | `https://www.momo.vn/bao-hiem/tra-cuu-bao-hiem` |
| **Bảo Hiểm Sức Khỏe** | `seg_bao_hiem_suc_khoe` | 1 | 1 | Landing Page | `https://www.momo.vn/bao-hiem-suc-khoe` |
| **Bảo Hiểm Xã Hội** | `seg_bao_hiem_xa_hoi` | 1 | 1 | Landing Page | `https://www.momo.vn/bao-hiem-xa-hoi` |

### Travel Hub (Du lịch và Đi lại)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OTA** | `seg_ota` | 1027 | 671 | Blog, Destination Page, Home Page (+4) | `https://www.momo.vn/du-lich-di-lai` |
| **Vé Xe** | `seg_ve_xe` | 134 | 5,358 | Blog, Home Page, Landing Page (+2) | `https://www.momo.vn/ve-xe` |
| **Cross Border** | `seg_cross_border` | 5 | 5 | Landing Page | `https://www.momo.vn/thanh-toan-quoc-te` |

### Cinema Hub (Phim và Giải trí)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cinema** | `seg_cinema` | 160 | 1,013 | Blog, Cineplex Page, Home Page (+3) | `https://www.momo.vn/cinema` |

### Telco Hub (Viễn thông và Nạp thẻ)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Data** | `seg_data` | 252 | 49 | Blog, Home Page, Landing Page (+2) | `https://www.momo.vn/nap-data` |
| **Sim** | `seg_sim` | 165 | 65 | Blog, Home Page, News (+1) | `https://www.momo.vn/sim-so-dep` |
| **Esim** | `seg_esim` | 27 | 45 | Blog, Landing Page, News (+1) | `https://www.momo.vn/esim-du-lich` |
| **Nạp tiền điện thoại** | `seg_nap_tien_ien_thoai` | 2 | 1 | Landing Page | `https://www.momo.vn/nap-tien-dien-thoai*` |
| **Airtime** | `seg_airtime` | 1 | 0 | Landing Page | `https://www.momo.vn/airtime*` |

### Vehicle Hub (Xe và Tiện ích Giao thông)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phạt Nguội** | `seg_phat_nguoi` | 18 | 37 | Blog, Home Page, Landing Page (+2) | `https://www.momo.vn/phat-nguoi` |
| **Tiện Ích Giao Thông** | `seg_tien_ich_giao_thong` | 14 | 16 | Blog, Landing Page, Mini Web | `https://www.momo.vn/tien-ich-giao-thong` |
| **Phí Không Dừng** | `seg_phi_khong_dung` | 9 | 9 | Blog, Hỏi đáp, Landing Page (+1) | `https://www.momo.vn/phi-khong-dung` |
| **Trạm sạc** | `seg_tram_sac` | 4 | 1 | Mini Web, Tool Page | `https://www.momo.vn/tien-ich-giao-thong/tr...` |
| **Cây xăng** | `seg_cay_xang` | 4 | 1 | Mini Web, Tool Page | `https://www.momo.vn/tien-ich-giao-thong/ca...` |
| **Giá xăng** | `seg_gia_xang` | 4 | 1 | Mini Web, Tool Page | `https://www.momo.vn/tien-ich-giao-thong/gi...` |
| **Garage** | `seg_garage` | 2 | 0 | Tool Page | `https://www.momo.vn/tien-ich-giao-thong/ga...` |
| **Hãng Xe** | `seg_hang_xe` | 2 | 0 | Tool Page | `https://www.momo.vn/tien-ich-giao-thong/ha...` |
| **Nộp Phạt CSGT** | `seg_nop_phat_csgt` | 1 | 0 | Landing Page | `https://www.momo.vn/tien-ich-giao-thong/no...` |

### Billpay Hub (Hóa đơn và Đời sống)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Điện** | `seg_ien` | 16 | 13 | Blog, Landing Page, News | `https://www.momo.vn/tin-tuc/khuyen-mai/the...` |
| **Billpay** | `seg_billpay` | 11 | 10 | Landing Page | `https://www.momo.vn/thanh-toan-hoa-don` |
| **Nước** | `seg_nuoc` | 10 | 8 | Blog, Landing Page | `https://www.momo.vn/nuoc` |
| **Internet** | `seg_internet` | 9 | 6 | Blog, Landing Page | `https://www.momo.vn/internet*` |
| **Phí Xét Tuyển** | `seg_phi_xet_tuyen` | 6 | 5 | Blog, Landing Page | `https://www.momo.vn/phi-xet-tuyen` |
| **Truyền Hình** | `seg_truyen_hinh` | 4 | 1 | Landing Page | `https://www.momo.vn/truyen-hinh` |
| **Chung Cư** | `seg_chung_cu` | 4 | 1 | Landing Page | `https://www.momo.vn/chung-cu` |
| **Học Phí** | `seg_hoc_phi` | 3 | 1 | Landing Page | `https://www.momo.vn/thanh-toan-momo-the-ho...` |

### Merchant Hub (Đối tác và Doanh nghiệp)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Merchant** | `seg_merchant` | 164 | 17,782 | Blog, Home Page, Landing Page (+3) | `https://www.momo.vn/tho-dia-momo` |
| **Soundbox** | `seg_soundbox` | 46 | 20 | Blog, News, Page | `https://www.momo.vn/loa-momo` |

### Game Hub (Cộng đồng Game)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Game** | `seg_game` | 50 | 44 | Blog, FAQ, Landing Page (+2) | `https://www.momo.vn/nap-the-game` |
| **Nạp thẻ Game** | `seg_nap_the_game` | 1 | 1 | Landing Page | `https://www.momo.vn/tin-tuc/tin-tuc-su-kie...` |

### Payment Hub (Thanh toán và Chuyển tiền)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P2P** | `seg_p2p` | 29 | 24 | Landing Page, News | `https://www.momo.vn/chuyen-tien` |
| **Dịch vụ liên kết** | `seg_dich_vu_lien_ket` | 15 | 14 | Blog, Landing Page, Mini Web | `https://www.momo.vn/dat-xe-cong-nghe` |
| **Tiktok** | `seg_tiktok` | 11 | 9 | Blog, Guide, Home Page (+2) | `https://www.momo.vn/nap-xu-tiktok` |
| **Application Store** | `seg_application_store` | 8 | 7 | Landing Page | `https://www.momo.vn/uu-dai-icloud` |
| **Hoàn Tiền Mua Sắm** | `seg_hoan_tien_mua_sam` | 5 | 5 | Landing Page | `https://www.momo.vn/hoan-tien-mua-sam` |
| **XU** | `seg_xu` | 1 | 1 | Landing Page | `https://www.momo.vn/xu` |

### Student Hub (Gói Sinh viên)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Student Pass** | `seg_student_pass` | 9 | 15 | Landing Page, News | `https://www.momo.vn/student-pass/back-to-s...` |
| **Student Hub** | `seg_student_hub` | 3 | 7 | Blog, Landing Page, School Page | `https://www.momo.vn/sinh-vien` |

### New User Hub (Khách hàng mới)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **New User** | `seg_new_user` | 40 | 15 | Landing Page, News | `https://www.momo.vn/xac-thuc-nfc` |

### Lottery Hub (Vé số)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vé số** | `seg_ve_so` | 7 | 5 | Blog, Landing Page, News | `https://www.momo.vn/tin-tuc/thong-bao/huon...` |

### General Platform (Tiện ích Nền tảng chung)

| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Khuyến mãi** | `seg_khuyen_mai` | 36 | 27 | Home Page, Landing Page, Page (+1) | `https://www.momo.vn/tin-tuc/khuyen-mai` |
| **Campaign** | `seg_campaign` | 34 | 28 | Campaign Page, Landing Page, Mini Web (+1) | `https://www.momo.vn/tin-tuc/khuyen-mai/gia...` |
| **Donation** | `seg_donation` | 23 | 109 | Landing Page, Page | `https://www.momo.vn/vi-nhan-ai` |
| **Điểm Tín Dụng** | `seg_iem_tin_dung` | 17 | 10 | Blog, Home Page, Landing Page | `https://www.momo.vn/diem-tin-dung` |
| **Trust** | `seg_trust` | 14 | 19 | Landing Page | `https://www.momo.vn/an-toan-bao-mat` |
| **Tìm Kiếm** | `seg_tim_kiem` | 2 | 0 | Mini Web | `https://www.momo.vn/tim-kiem` |
| **Tuyển Dụng** | `seg_tuyen_dung` | 2 | 0 | Landing Page | `https://www.momo.vn/careers` |
| **Nhận Tiền Quốc Tế** | `seg_nhan_tien_quoc_te` | 2 | 1 | Landing Page | `https://www.momo.vn/nhan-tien-quoc-te` |
| **Tiệm Vàng Online** | `seg_tiem_vang_online` | 1 | 1 | Landing Page | `https://www.momo.vn/tiem-vang-online` |

## 4. Hướng Dẫn Tích Hợp Vào Ads Manager UI & Runtime

### Cấu trúc Schema Ad Campaign:
```json
{
  "campaign_id": "camp_2026_q2_vaynhanh_01",
  "ad_name": "Banner Vay Nhanh 10 Trieu",
  "target_segment": "seg_vay_nhanh",
  "target_page_types": ["Blog", "Landing Page"],
  "exclude_urls": ["/vay-nhanh/dieu-khoan"]
}
```

### Cơ chế Khớp tại Trình Duyệt (Runtime Matcher):
1. Khi người dùng vào trang (ví dụ `momo.vn/vay-nhanh/blog/mua-sh-tra-gop-2717`), script Ads Manager đọc URL và đối chiếu với tập rules của `ads_segments.json`.
2. Khớp đúng rule của `seg_vay_nhanh` với page_type là `Blog`.
3. Tải và hiển thị ngay các quảng cáo nhắm mục tiêu vào `seg_vay_nhanh`.

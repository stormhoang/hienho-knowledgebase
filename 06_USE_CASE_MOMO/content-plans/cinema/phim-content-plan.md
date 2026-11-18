# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - THEME: PHIM CHIẾU RẠP MỚI NHẤT

- **Theme:** Phim Chiếu Rạp Mới Nhất
- **Hub:** cinema
- **URL Pillar Hub:** `/phim/`
- **Tổng từ khóa thô ban đầu:** 659 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 13 từ khóa
- **Từ khóa nhận từ CSV theme khác cùng Hub:** 187 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 39 từ khóa
- **Số lượng URLs phân bổ:** 6 URLs (1 Pillar Hub + 5 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Đợt Sản Xuất | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/phim/` | Cẩm Nang & Bảng Tra Cứu Phim Chiếu Rạp Mới Nhất Toàn Diện | `phim` | mua vé phim, mua vé rạp chiếu phim quốc gia, mua vé phim online | 1,000,410 | `Informational` | Pillar Hub Page + Interactive Widget | `TOFU` | `Đợt 1` | Đặt Vé Phim Rạp Chiếu Mới Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 2 | `/phim/cam-nang/` | Cẩm nang & Hỏi đáp Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết | `phim hàn quốc` | đông phim, phim online, phim đam my | 1,473,250 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Phim Rạp Chiếu Mới Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 3 | `/phim/phim-hoat-hinh-anime/` | Phim Hoạt Hình & Anime Hot Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết | `anime hay` | hoạt hình 3d, phim hoạt hình, hoat hinh | 1,161,320 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Phim Rạp Chiếu Mới Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 4 | `/phim/phim-chieu-rap-moi-nhat/` | Phim Chiếu Rạp Mới Nhất Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết | `phim chiếu rạp` | phim mới, phim rạp, yêu phim mới | 523,570 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Phim Rạp Chiếu Mới Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 5 | `/phim/top-phim-hay-danh-gia/` | Top Phim Hay & Đánh Giá Phim Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết | `phim hay` | vietsub, phim hay net, phim vietsub | 445,840 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Phim Rạp Chiếu Mới Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 6 | `/phim/the-loai-phim-tuyen-tap/` | Thể Loại Phim & Tuyển Tập Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết | `phim lẻ` | phim hành động, phim tình cảm, phim kinh dị | 162,120 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Phim Rạp Chiếu Mới Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/phim/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:

### Bài 1: `Cẩm Nang & Bảng Tra Cứu Phim Chiếu Rạp Mới Nhất Toàn Diện`
- **URL Slug:** `/phim/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `phim`
- **Secondary Synonyms:** mua vé phim, mua vé rạp chiếu phim quốc gia, mua vé phim online, mua vé phim cgv
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phim
   - ### H3 5.1: Mua vé phim?
   - ### H3 5.2: Mua vé rạp chiếu phim quốc gia?
   - ### H3 5.3: Mua vé phim online?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 2: `Cẩm nang & Hỏi đáp Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/phim/cam-nang/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `phim hàn quốc`
- **Secondary Synonyms:** đông phim, phim online, phim đam my, phim 1080
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phim hàn quốc
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phim hàn quốc
   - ### H3 5.1: Đông phim?
   - ### H3 5.2: Phim online?
   - ### H3 5.3: Phim đam my?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 3: `Phim Hoạt Hình & Anime Hot Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/phim/phim-hoat-hinh-anime/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `anime hay`
- **Secondary Synonyms:** hoạt hình 3d, phim hoạt hình, hoat hinh, phim anime
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về anime hay
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về anime hay
   - ### H3 5.1: Hoạt hình 3d?
   - ### H3 5.2: Phim hoạt hình?
   - ### H3 5.3: Hoat hinh?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 4: `Phim Chiếu Rạp Mới Nhất Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/phim/phim-chieu-rap-moi-nhat/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `phim chiếu rạp`
- **Secondary Synonyms:** phim mới, phim rạp, yêu phim mới, phim mới cgv
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phim chiếu rạp
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phim chiếu rạp
   - ### H3 5.1: Phim mới?
   - ### H3 5.2: Phim rạp?
   - ### H3 5.3: Yêu phim mới?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 5: `Top Phim Hay & Đánh Giá Phim Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/phim/top-phim-hay-danh-gia/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `phim hay`
- **Secondary Synonyms:** vietsub, phim hay net, phim vietsub, phim 18 vietsub
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phim hay
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phim hay
   - ### H3 5.1: Vietsub?
   - ### H3 5.2: Phim hay net?
   - ### H3 5.3: Phim vietsub?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 6: `Thể Loại Phim & Tuyển Tập Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/phim/the-loai-phim-tuyen-tap/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `phim lẻ`
- **Secondary Synonyms:** phim hành động, phim tình cảm, phim kinh dị, phim ma kinh dị
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phim lẻ
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phim lẻ
   - ### H3 5.1: Phim hành động?
   - ### H3 5.2: Phim tình cảm?
   - ### H3 5.3: Phim kinh dị?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

---

## 5. DỮ LIỆU CẤU TRÚC JSON-LD (STRUCTURED DATA SCHEMA) CHO WEB DEV

Đội ngũ Frontend tại `hubs-momo` có thể sao chép trực tiếp 2 khối Schema này vào thẻ `<script type="application/ld+json">` của trang:

### A. BreadcrumbList Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Trang chủ",
      "item": "https://momo.vn"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Cinema",
      "item": "https://momo.vn/cinema"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Phim Chiếu Rạp Mới Nhất",
      "item": "https://momo.vn/phim"
    }
  ]
}
```

### B. FAQPage Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "Hỏi đáp thường gặp về Phim Chiếu Rạp Mới Nhất",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Cẩm nang & Hỏi đáp Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về phim hàn quốc được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Phim Hoạt Hình & Anime Hot Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về anime hay được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Phim Chiếu Rạp Mới Nhất Phim Chiếu Rạp Mới Nhất: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về phim chiếu rạp được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    }
  ]
}
```

---

## 6. KIẾN TRÚC LIÊN KẾT NỘI BỘ (INTERNAL LINKING & SILO MATRIX)

Phân tầng dòng chảy uy tín trang (PageRank) và định vị chuyên môn chủ đề (Topic Authority):

### A. Parent Hub Pillar:
- **Trang Cột Trụ Cấp 1:** `[Tiện Ích Nền Tảng](/tien-ich)`
- **Anchor Text Mỏ Neo:** `"Hệ sinh thái tiện ích Web MoMo"`

### B. Liên kết ngang cùng Hub (Peer In-Silo):
| Thứ tự | Theme Bổ Trợ | Đường Dẫn Khuyến Nghị | Anchor Text Tự Nhiên | Độ Tương Đồng | Search Volume |
| :---: | :--- | :--- | :--- | :---: | :---: |
| 1 | `Lịch Chiếu Phim Rạp` | `/lich-phim/` | `lịch chiếu phim` | `0.222` | 625,580 |
| 2 | `Rạp Chiếu Phim & Cụm Rạp` | `/rap/` | `phim chiếu rạp` | `0.2` | 1,229,160 |
| 3 | `Đặt Vé Phim Online` | `/dat-phim/` | `đặt vé cgv` | `0.19` | 14,050 |
| 4 | `Giá Vé Xem Phim & Khuyến Mãi` | `/ve-xem-phim/` | `vé xem phim` | `0.03` | 0 |

### C. Cầu nối liên kết xuyên Hub (Cross-Silo Bridges):
| Thứ tự | Theme Đích | Hub | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |

---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "Phim là dịch vụ tổng hợp lịch chiếu, giá vé và sơ đồ ghế ngồi thời gian thực của toàn bộ các cụm rạp chiếu phim lớn trên cả nước (CGV, Lotte, Galaxy, BHD, Beta). Người xem có thể dễ dàng so sánh suất chiếu gần nhất, áp dụng mã giảm giá độc quyền và đặt vé trực tuyến nhận vé điện tử Smart Ticket vào thẳng phòng chiếu."

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
| Hệ thống chuỗi rạp liên kết | CGV Cinemas, Lotte Cinema, Galaxy, BHD Star, Beta Cinemas, Cinestar |
| Khung phân loại độ tuổi khán giả | Nhãn P (Phổ biến), K (Dưới 13 tuổi có bảo trợ), T13, T16, T18 và C (Cấm) |
| Cơ chế đồng bộ suất chiếu | Đồng bộ API thời gian thực với hệ thống bán vé của từng cụm rạp |
| Hình thức vé vào phòng chiếu | Vé điện tử (Smart Ticket QR) quét mã vào thẳng rạp không cần in vé giấy |
| Phụ thu định dạng trải nghiệm | Áp dụng định dạng 3D, IMAX, 4DX, ScreenX và các dòng ghế đôi Sweetbox/VIP |
| Quy định pháp lý chuyên ngành | Luật Điện ảnh & Thông tư 05/2023/TT-BVHTTDL của Bộ Văn hóa, Thể thao và Du lịch |

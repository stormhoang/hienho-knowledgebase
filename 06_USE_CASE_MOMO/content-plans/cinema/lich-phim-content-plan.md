# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - THEME: LỊCH CHIẾU PHIM RẠP

- **Theme:** Lịch Chiếu Phim Rạp
- **Hub:** cinema
- **URL Pillar Hub:** `/lich-phim/`
- **Tổng từ khóa thô ban đầu:** 2,559 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 1 từ khóa
- **Từ khóa nhường cho theme khác cùng Hub (chống trùng giữa các plan):** 100 từ khóa
- **Từ khóa nhận từ CSV theme khác cùng Hub:** 91 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 104 từ khóa
- **Số lượng URLs phân bổ:** 5 URLs (1 Pillar Hub + 4 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Đợt Sản Xuất | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/lich-phim/` | Cẩm Nang & Bảng Tra Cứu Lịch Chiếu Phim Rạp Toàn Diện | `lịch chiếu phim` | lịch chiếu phim tuần này, lịch chiếu phim chủ nhật tuần này, lịch chiếu phim mới | 74,240 | `Informational` | Pillar Hub Page + Interactive Widget | `TOFU` | `Đợt 1` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 2 | `/lich-phim/lich-phim-theo-cum-rap/` | Lịch Phim Theo Cụm Rạp Toàn Quốc Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `lịch chiếu phim cgv` | cgv lịch chiếu, lịch chiếu phim lotte, lịch chiếu phim galaxy | 396,730 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 3 | `/lich-phim/thong-tin-suat-chieu-lich-rap/` | Thông Tin Suất Chiếu & Lịch Rạp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `lịch phim` | lịch chiếu, lịch chiếu phim long an, lịch chiếu phim venus hải dương | 39,320 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 1` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 4 | `/lich-phim/lich-chieu-hom-nay-cuoi-tuan/` | Lịch Chiếu Phim Hôm Nay & Cuối Tuần Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `phim chiếu rap hôm nay` | lịch chiếu phim hôm nay, phim rạp hôm nay, lịch chiếu phim rạp quốc gia hôm nay | 39,030 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 1` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 5 | `/lich-phim/cam-nang/` | Cẩm nang & Hỏi đáp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `lam sơn square` | moveek com, em và trịnh moveek, giá vé movie red | 1,000 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/lich-phim/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:

### Bài 1: `Cẩm Nang & Bảng Tra Cứu Lịch Chiếu Phim Rạp Toàn Diện`
- **URL Slug:** `/lich-phim/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `lịch chiếu phim`
- **Secondary Synonyms:** lịch chiếu phim tuần này, lịch chiếu phim chủ nhật tuần này, lịch chiếu phim mới, lịch phim tuần này
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lịch chiếu phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lịch chiếu phim
   - ### H3 5.1: Lịch chiếu phim tuần này?
   - ### H3 5.2: Lịch chiếu phim chủ nhật tuần này?
   - ### H3 5.3: Lịch chiếu phim mới?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 2: `Lịch Phim Theo Cụm Rạp Toàn Quốc Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/lich-phim/lich-phim-theo-cum-rap/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `lịch chiếu phim cgv`
- **Secondary Synonyms:** cgv lịch chiếu, lịch chiếu phim lotte, lịch chiếu phim galaxy, lịch chiếu phim rạp quốc gia
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lịch chiếu phim cgv
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lịch chiếu phim cgv
   - ### H3 5.1: Cgv lịch chiếu?
   - ### H3 5.2: Lịch chiếu phim lotte?
   - ### H3 5.3: Lịch chiếu phim galaxy?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 3: `Thông Tin Suất Chiếu & Lịch Rạp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/lich-phim/thong-tin-suat-chieu-lich-rap/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `lịch phim`
- **Secondary Synonyms:** lịch chiếu, lịch chiếu phim long an, lịch chiếu phim venus hải dương, lịch chiếu phim mạc ly
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lịch phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lịch phim
   - ### H3 5.1: Lịch chiếu?
   - ### H3 5.2: Lịch chiếu phim long an?
   - ### H3 5.3: Lịch chiếu phim venus hải dương?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 4: `Lịch Chiếu Phim Hôm Nay & Cuối Tuần Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/lich-phim/lich-chieu-hom-nay-cuoi-tuan/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `phim chiếu rap hôm nay`
- **Secondary Synonyms:** lịch chiếu phim hôm nay, phim rạp hôm nay, lịch chiếu phim rạp quốc gia hôm nay, lịch phim hôm nay
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phim chiếu rap hôm nay
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phim chiếu rap hôm nay
   - ### H3 5.1: Lịch chiếu phim hôm nay?
   - ### H3 5.2: Phim rạp hôm nay?
   - ### H3 5.3: Lịch chiếu phim rạp quốc gia hôm nay?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 5: `Cẩm nang & Hỏi đáp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/lich-phim/cam-nang/`
- **Chỉ tiêu độ dài:** `1,200 - 1,600 từ` (Cấp bậc: `Educational Spoke`)
- **Primary Keyword:** `lam sơn square`
- **Secondary Synonyms:** moveek com, em và trịnh moveek, giá vé movie red
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lam sơn square
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lam sơn square
   - ### H3 5.1: Moveek com?
   - ### H3 5.2: Em và trịnh moveek?
   - ### H3 5.3: Giá vé movie red?
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
      "name": "Lịch Chiếu Phim Rạp",
      "item": "https://momo.vn/lich-phim"
    }
  ]
}
```

### B. FAQPage Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "Hỏi đáp thường gặp về Lịch Chiếu Phim Rạp",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Lịch Phim Theo Cụm Rạp Toàn Quốc Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về lịch chiếu phim cgv được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Thông Tin Suất Chiếu & Lịch Rạp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về lịch phim được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Lịch Chiếu Phim Hôm Nay & Cuối Tuần Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về phim chiếu rap hôm nay được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
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
| 1 | `Rạp Chiếu Phim & Cụm Rạp` | `/rap/` | `phim chiếu rạp` | `0.273` | 1,229,160 |
| 2 | `Đặt Vé Phim Online` | `/dat-phim/` | `đặt vé cgv` | `0.16` | 14,050 |
| 3 | `Phim Chiếu Rạp Mới Nhất` | `/phim/` | `phim` | `0.115` | 5,409,760 |
| 4 | `Giá Vé Xem Phim & Khuyến Mãi` | `/ve-xem-phim/` | `vé xem phim` | `0.027` | 0 |

### C. Cầu nối liên kết xuyên Hub (Cross-Silo Bridges):
| Thứ tự | Theme Đích | Hub | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |

---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "Lịch chiếu phim là dịch vụ tổng hợp lịch chiếu, giá vé và sơ đồ ghế ngồi thời gian thực của toàn bộ các cụm rạp chiếu phim lớn trên cả nước (CGV, Lotte, Galaxy, BHD, Beta). Người xem có thể dễ dàng so sánh suất chiếu gần nhất, áp dụng mã giảm giá độc quyền và đặt vé trực tuyến nhận vé điện tử Smart Ticket vào thẳng phòng chiếu."

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
| Hệ thống chuỗi rạp liên kết | CGV Cinemas, Lotte Cinema, Galaxy, BHD Star, Beta Cinemas, Cinestar |
| Khung phân loại độ tuổi khán giả | Nhãn P (Phổ biến), K (Dưới 13 tuổi có bảo trợ), T13, T16, T18 và C (Cấm) |
| Cơ chế đồng bộ suất chiếu | Đồng bộ API thời gian thực với hệ thống bán vé của từng cụm rạp |
| Hình thức vé vào phòng chiếu | Vé điện tử (Smart Ticket QR) quét mã vào thẳng rạp không cần in vé giấy |
| Phụ thu định dạng trải nghiệm | Áp dụng định dạng 3D, IMAX, 4DX, ScreenX và các dòng ghế đôi Sweetbox/VIP |
| Quy định pháp lý chuyên ngành | Luật Điện ảnh & Thông tư 05/2023/TT-BVHTTDL của Bộ Văn hóa, Thể thao và Du lịch |

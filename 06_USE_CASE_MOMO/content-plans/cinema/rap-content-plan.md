# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - THEME: RẠP CHIẾU PHIM & CỤM RẠP

- **Theme:** Rạp Chiếu Phim & Cụm Rạp
- **Hub:** cinema
- **URL Pillar Hub:** `/rap/`
- **Tổng từ khóa thô ban đầu:** 1,154 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 4 từ khóa
- **Từ khóa nhường cho theme khác cùng Hub (chống trùng giữa các plan):** 197 từ khóa
- **Từ khóa nhận từ CSV theme khác cùng Hub:** 20 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 55 từ khóa
- **Số lượng URLs phân bổ:** 5 URLs (1 Pillar Hub + 4 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Đợt Sản Xuất | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/rap/` | Cẩm Nang & Bảng Tra Cứu Rạp Chiếu Phim & Cụm Rạp Toàn Diện | `rạp chiếu phim` | giá vé metiz, giá vé avatar 3d, metiz giá vé | 91,050 | `Informational` | Pillar Hub Page + Interactive Widget | `TOFU` | `Đợt 1` | Đặt Vé Cụm Rạp CGV, Lotte, Galaxy -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 2 | `/rap/he-thong-rap-lotte-galaxy-bhd/` | Hệ Thống Rạp Lotte, Galaxy & BHD Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `rạp chiếu phim quốc gia` | rạp beta giải phóng, rạp chiếu phim quốc gia thái hà, rạp beta | 219,920 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Cụm Rạp CGV, Lotte, Galaxy -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 3 | `/rap/cam-nang/` | Cẩm nang & Hỏi đáp Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `rạp phim` | phim chiếu rạp hay, phim đang chiếu rap, phim hay chiếu rạp | 137,760 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Cụm Rạp CGV, Lotte, Galaxy -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 4 | `/rap/rap-chieu-phim-gan-day/` | Rạp Chiếu Phim Gần Đây & Phòng Chiếu Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `rạp chiếu phim gần đây` | rap phim gần đây, rạp imax, rạp phim gần nhất | 100,890 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 2` | Đặt Vé Cụm Rạp CGV, Lotte, Galaxy -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 5 | `/rap/he-thong-rap-cgv/` | Hệ Thống Rạp CGV Cinemas Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `rạp cgv` | cgv gần đây, rạp phim cgv, cgv linh đàm | 26,680 | `Informational` | Educational Guide & FAQ | `TOFU` | `Đợt 1` | Đặt Vé Cụm Rạp CGV, Lotte, Galaxy -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/rap/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:

### Bài 1: `Cẩm Nang & Bảng Tra Cứu Rạp Chiếu Phim & Cụm Rạp Toàn Diện`
- **URL Slug:** `/rap/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `rạp chiếu phim`
- **Secondary Synonyms:** giá vé metiz, giá vé avatar 3d, metiz giá vé, đánh giá phim chiếu rạp
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về rạp chiếu phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về rạp chiếu phim
   - ### H3 5.1: Giá vé metiz?
   - ### H3 5.2: Giá vé avatar 3d?
   - ### H3 5.3: Metiz giá vé?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 2: `Hệ Thống Rạp Lotte, Galaxy & BHD Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/rap/he-thong-rap-lotte-galaxy-bhd/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `rạp chiếu phim quốc gia`
- **Secondary Synonyms:** rạp beta giải phóng, rạp chiếu phim quốc gia thái hà, rạp beta, beta mỹ đình
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về rạp chiếu phim quốc gia
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về rạp chiếu phim quốc gia
   - ### H3 5.1: Rạp beta giải phóng?
   - ### H3 5.2: Rạp chiếu phim quốc gia thái hà?
   - ### H3 5.3: Rạp beta?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 3: `Cẩm nang & Hỏi đáp Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/rap/cam-nang/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `rạp phim`
- **Secondary Synonyms:** phim chiếu rạp hay, phim đang chiếu rap, phim hay chiếu rạp, phim mới chiếu rạp
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về rạp phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về rạp phim
   - ### H3 5.1: Phim chiếu rạp hay?
   - ### H3 5.2: Phim đang chiếu rap?
   - ### H3 5.3: Phim hay chiếu rạp?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 4: `Rạp Chiếu Phim Gần Đây & Phòng Chiếu Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/rap/rap-chieu-phim-gan-day/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `rạp chiếu phim gần đây`
- **Secondary Synonyms:** rap phim gần đây, rạp imax, rạp phim gần nhất, rạp lamour
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về rạp chiếu phim gần đây
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về rạp chiếu phim gần đây
   - ### H3 5.1: Rap phim gần đây?
   - ### H3 5.2: Rạp imax?
   - ### H3 5.3: Rạp phim gần nhất?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 5: `Hệ Thống Rạp CGV Cinemas Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/rap/he-thong-rap-cgv/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `rạp cgv`
- **Secondary Synonyms:** cgv gần đây, rạp phim cgv, cgv linh đàm, ve cgv
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về rạp cgv
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về rạp cgv
   - ### H3 5.1: Cgv gần đây?
   - ### H3 5.2: Rạp phim cgv?
   - ### H3 5.3: Cgv linh đàm?
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
      "name": "Rạp Chiếu Phim & Cụm Rạp",
      "item": "https://momo.vn/rap"
    }
  ]
}
```

### B. FAQPage Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "Hỏi đáp thường gặp về Rạp Chiếu Phim & Cụm Rạp",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hệ Thống Rạp Lotte, Galaxy & BHD Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về rạp chiếu phim quốc gia được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Cẩm nang & Hỏi đáp Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về rạp phim được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Rạp Chiếu Phim Gần Đây & Phòng Chiếu Rạp Chiếu Phim & Cụm Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về rạp chiếu phim gần đây được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
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
| 1 | `Lịch Chiếu Phim Rạp` | `/lich-phim/` | `lịch chiếu phim` | `0.412` | 625,580 |
| 2 | `Đặt Vé Phim Online` | `/dat-phim/` | `đặt vé cgv` | `0.286` | 14,050 |
| 3 | `Phim Chiếu Rạp Mới Nhất` | `/phim/` | `phim` | `0.125` | 5,409,760 |
| 4 | `Giá Vé Xem Phim & Khuyến Mãi` | `/ve-xem-phim/` | `vé xem phim` | `0.029` | 0 |

### C. Cầu nối liên kết xuyên Hub (Cross-Silo Bridges):
| Thứ tự | Theme Đích | Hub | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |

---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "Rạp chiếu phim là dịch vụ tổng hợp lịch chiếu, giá vé và sơ đồ ghế ngồi thời gian thực của toàn bộ các cụm rạp chiếu phim lớn trên cả nước (CGV, Lotte, Galaxy, BHD, Beta). Người xem có thể dễ dàng so sánh suất chiếu gần nhất, áp dụng mã giảm giá độc quyền và đặt vé trực tuyến nhận vé điện tử Smart Ticket vào thẳng phòng chiếu."

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
| Hệ thống chuỗi rạp liên kết | CGV Cinemas, Lotte Cinema, Galaxy, BHD Star, Beta Cinemas, Cinestar |
| Khung phân loại độ tuổi khán giả | Nhãn P (Phổ biến), K (Dưới 13 tuổi có bảo trợ), T13, T16, T18 và C (Cấm) |
| Cơ chế đồng bộ suất chiếu | Đồng bộ API thời gian thực với hệ thống bán vé của từng cụm rạp |
| Hình thức vé vào phòng chiếu | Vé điện tử (Smart Ticket QR) quét mã vào thẳng rạp không cần in vé giấy |
| Phụ thu định dạng trải nghiệm | Áp dụng định dạng 3D, IMAX, 4DX, ScreenX và các dòng ghế đôi Sweetbox/VIP |
| Quy định pháp lý chuyên ngành | Luật Điện ảnh & Thông tư 05/2023/TT-BVHTTDL của Bộ Văn hóa, Thể thao và Du lịch |

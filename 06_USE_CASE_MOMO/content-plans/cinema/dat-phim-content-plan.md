# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - THEME: ĐẶT VÉ PHIM ONLINE

- **Theme:** Đặt Vé Phim Online
- **Hub:** cinema
- **URL Pillar Hub:** `/dat-phim/`
- **Tổng từ khóa thô ban đầu:** 402 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 0 từ khóa
- **Nguồn dữ liệu gộp theo theme:** dat-phim.csv, mua-ve-phim.csv
- **Từ khóa nhường cho theme khác cùng Hub (chống trùng giữa các plan):** 35 từ khóa
- **Từ khóa nhận từ CSV theme khác cùng Hub:** 34 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 21 từ khóa
- **Số lượng URLs phân bổ:** 3 URLs (1 Pillar Hub + 2 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Đợt Sản Xuất | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/dat-phim/` | Cẩm Nang & Bảng Tra Cứu Đặt Vé Phim Online Toàn Diện | `đặt vé phim` | đặt phim, đặt vé phim online, app đặt vé phim | 1,310 | `Transactional` | Pillar Hub Page + Interactive Widget | `TOFU` | `Đợt 1` | Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 2 | `/dat-phim/dat-ve-cgv-lotte/` | Đặt Vé CGV & Lotte Cinema Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết | `đặt vé cgv` | cgv đặt vé, combo bắp nước cgv, mua ve cgv | 7,480 | `Transactional` | Step-by-step How-to & Action Form | `BOFU` | `Đợt 1` | Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 3 | `/dat-phim/dat-ve-galaxy-cinestar-beta/` | Đặt Vé Galaxy, Cinestar & Beta Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết | `đặt vé rạp chiếu phim quốc gia` | đặt vé galaxy, đặt vé cinestar, giá vé bhd lê văn việt | 4,260 | `Transactional` | Step-by-step How-to & Action Form | `BOFU` | `Đợt 1` | Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/dat-phim/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:

### Bài 1: `Cẩm Nang & Bảng Tra Cứu Đặt Vé Phim Online Toàn Diện`
- **URL Slug:** `/dat-phim/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `đặt vé phim`
- **Secondary Synonyms:** đặt phim, đặt vé phim online, app đặt vé phim, đặt vé coi phim
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về đặt vé phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: Hồ sơ và điều kiện cần chuẩn bị trước khi thực hiện
   - ## H2 4: Quy trình 3 bước thực hiện giao dịch nhanh chóng trên điện thoại
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về đặt vé phim
   - ### H3 5.1: Đặt phim?
   - ### H3 5.2: Đặt vé phim online?
   - ### H3 5.3: App đặt vé phim?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 2: `Đặt Vé CGV & Lotte Cinema Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/dat-phim/dat-ve-cgv-lotte/`
- **Chỉ tiêu độ dài:** `1,500 - 2,200 từ` (Cấp bậc: `High Conversion Guide`)
- **Primary Keyword:** `đặt vé cgv`
- **Secondary Synonyms:** cgv đặt vé, combo bắp nước cgv, mua ve cgv, đặt vé lotte cinema
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về đặt vé cgv
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: Hồ sơ và điều kiện cần chuẩn bị trước khi thực hiện
   - ## H2 4: Quy trình 3 bước thực hiện giao dịch nhanh chóng trên điện thoại
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về đặt vé cgv
   - ### H3 5.1: Cgv đặt vé?
   - ### H3 5.2: Combo bắp nước cgv?
   - ### H3 5.3: Mua ve cgv?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 3: `Đặt Vé Galaxy, Cinestar & Beta Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/dat-phim/dat-ve-galaxy-cinestar-beta/`
- **Chỉ tiêu độ dài:** `1,500 - 2,200 từ` (Cấp bậc: `High Conversion Guide`)
- **Primary Keyword:** `đặt vé rạp chiếu phim quốc gia`
- **Secondary Synonyms:** đặt vé galaxy, đặt vé cinestar, giá vé bhd lê văn việt, đặt vé metiz
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về đặt vé rạp chiếu phim quốc gia
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: Hồ sơ và điều kiện cần chuẩn bị trước khi thực hiện
   - ## H2 4: Quy trình 3 bước thực hiện giao dịch nhanh chóng trên điện thoại
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về đặt vé rạp chiếu phim quốc gia
   - ### H3 5.1: Đặt vé galaxy?
   - ### H3 5.2: Đặt vé cinestar?
   - ### H3 5.3: Giá vé bhd lê văn việt?
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
      "name": "Đặt Vé Phim Online",
      "item": "https://momo.vn/dat-phim"
    }
  ]
}
```

### B. FAQPage Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "Hỏi đáp thường gặp về Đặt Vé Phim Online",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Đặt Vé CGV & Lotte Cinema Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về đặt vé cgv được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Đặt Vé Galaxy, Cinestar & Beta Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về đặt vé rạp chiếu phim quốc gia được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
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
| 2 | `Rạp Chiếu Phim & Cụm Rạp` | `/rap/` | `phim chiếu rạp` | `0.238` | 1,229,160 |
| 3 | `Phim Chiếu Rạp Mới Nhất` | `/phim/` | `phim` | `0.125` | 5,409,760 |
| 4 | `Giá Vé Xem Phim & Khuyến Mãi` | `/ve-xem-phim/` | `vé xem phim` | `0.059` | 0 |

### C. Cầu nối liên kết xuyên Hub (Cross-Silo Bridges):
| Thứ tự | Theme Đích | Hub | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |

---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "Đặt vé phim là dịch vụ tổng hợp lịch chiếu, giá vé và sơ đồ ghế ngồi thời gian thực của toàn bộ các cụm rạp chiếu phim lớn trên cả nước (CGV, Lotte, Galaxy, BHD, Beta). Người xem có thể dễ dàng so sánh suất chiếu gần nhất, áp dụng mã giảm giá độc quyền và đặt vé trực tuyến nhận vé điện tử Smart Ticket vào thẳng phòng chiếu."

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
| Hệ thống chuỗi rạp liên kết | CGV Cinemas, Lotte Cinema, Galaxy, BHD Star, Beta Cinemas, Cinestar |
| Khung phân loại độ tuổi khán giả | Nhãn P (Phổ biến), K (Dưới 13 tuổi có bảo trợ), T13, T16, T18 và C (Cấm) |
| Cơ chế đồng bộ suất chiếu | Đồng bộ API thời gian thực với hệ thống bán vé của từng cụm rạp |
| Hình thức vé vào phòng chiếu | Vé điện tử (Smart Ticket QR) quét mã vào thẳng rạp không cần in vé giấy |
| Phụ thu định dạng trải nghiệm | Áp dụng định dạng 3D, IMAX, 4DX, ScreenX và các dòng ghế đôi Sweetbox/VIP |
| Quy định pháp lý chuyên ngành | Luật Điện ảnh & Thông tư 05/2023/TT-BVHTTDL của Bộ Văn hóa, Thể thao và Du lịch |

# 11_NEWS_FEED: CỔNG TIẾP NHẬN & CẬP NHẬT TIN TỨC THỊ TRƯỜNG (GEMINI SPARK INGESTION)

Thư mục này là điểm tiếp nhận dữ liệu chuyên biệt dành cho **Gemini Spark** cập nhật tin tức thị trường, biến động ngành, chính sách và xu hướng công nghệ mới nhất phục vụ các dự án Web Platform và 5 Strategic Hubs.

---

## 1. CẤU TRÚC THƯ MỤC CON

```
11_NEWS_FEED/
├── README.md               # Quy chuẩn định dạng & hướng dẫn vận hành
├── YYYY-MM-DD_daily_report.md  # [VỊ TRÍ CHUẨN DUY NHẤT] Bản tin tổng hợp theo ngày; scripts/sync_seo_news.py và AGENTS.md đọc tại đây
├── daily/                  # Chỉ để mẫu tham khảo (sample_news_template.md); KHÔNG ghi bản sao bản tin ngày vào đây
├── topics/                 # Chỉ chứa tin chuyên sâu riêng cho 1 Hub, KHÔNG chép lại nguyên bản tin ngày
│   ├── financial/          # Tài chính, ngân hàng, lãi suất, giá vàng, tỷ giá, NHNN
│   ├── cinema/             # Doanh thu rạp, phim bom tấn, xu hướng giải trí
│   ├── vehicle/            # Giao thông, giá xăng, trạm sạc EV, bảo hiểm xe
│   ├── student/            # Giới trẻ, sinh viên, xu hướng đại học, Gen Z
│   └── tech_ai_seo/        # AI Search, thuật toán Google, GEO, AEO, công nghệ Web
└── raw/                    # Dữ liệu nguồn thô hoặc JSON/RSS do Gemini Spark đẩy vào
```

---

## 2. QUY CHUẨN ĐỊNH DẠNG BẢN TIN (OUTPUT SCHEMA DÀNH CHO GEMINI SPARK)

Khi Gemini Spark xuất bản bài viết hoặc bản tin vào thư mục này, nội dung cần tuân thủ cấu trúc chuẩn Product Lead:

```markdown
---
date: YYYY-MM-DD
source: [Tên nguồn báo / Trang tin / Cơ quan ban hành]
source_url: [Đường dẫn nguồn gốc]
category: [financial | cinema | vehicle | student | tech_ai_seo]
hubs_impacted: [Financial Hub | Cinema Hub | Vehicle Hub | Student Hub | Web Overview]
priority: [P0_Urgent | P1_High | P2_Normal]
tags: [Từ khóa chính liên quan]
---

# [TIÊU ĐỀ BẢN TIN / SỰ KIỆN]

### 1. Tóm Tắt Bản Tin (Executive Summary)
- Tóm tắt 2-4 gạch đầu dòng cốt lõi về bản chất sự việc, dữ liệu thực tế và thời điểm diễn ra.

### 2. Phân Tích Ý Nghĩa & Tác Động ("So What?")
- Phân tích sự dịch chuyển của thị trường hoặc hành vi người dùng.
- Tác động trực tiếp đến lưu lượng tìm kiếm tự nhiên (Search Intent) hoặc phễu Web-to-App của MoMo.

### 3. Cơ Hội & Đề Xuất Hành Động Cho Web Platform (Actionable Items)
- **Content & SEO:** Từ khóa mới cần phủ ngay, chủ đề cần GenAI viết gấp.
- **Product & Utility:** Tiện ích/Widget cần cập nhật dữ liệu (ví dụ: bảng tỷ giá, giá xăng mới, lãi suất mới).
- **Campaign / Co-marketing:** Cơ hội kết nối với các đối tác hoặc đẩy banner ngữ cảnh.
```

---

## 3. NGUYÊN TẮC VẬN HÀNH & KIỂM DUYỆT
- **Zero Hallucination:** Mọi tin tức cập nhật phải có nguồn trích dẫn rõ ràng (`source` và `source_url`).
- **Không dùng Emoji / Icon:** Giữ văn phong cô đọng, sắc sảo, chuyên nghiệp.
- **Một bản tin, một vị trí:** Mỗi bản tin ngày chỉ ghi đúng 1 file `11_NEWS_FEED/YYYY-MM-DD_daily_report.md`. Không ghi bản sao sang `daily/` hay `topics/`; bản sao trùng nội dung sẽ bị xóa khi rà soát.
- **Map 1-1 với 5 Strategic Hubs:** Ưu tiên phân loại tin tức trực tiếp vào đúng nhóm chủ đề tại thư mục `topics/` để các đội ngũ nghiệp vụ dễ dàng tra cứu.

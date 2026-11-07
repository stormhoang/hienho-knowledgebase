# MASTER WEB PRODUCT PRD TEMPLATE

> **Mục đích:** Template chuẩn hóa dành cho **Web Platform** để xây dựng Đặc tả Yêu cầu Sản phẩm Kênh Web (Web Product PRD) theo cấu trúc 4 Phần Tiêu Chuẩn: Overview, Market Research, Product Structure (Site, Content & Umami Tracking) và SEO/GEO On-Page.
>
> **Nguyên tắc biên soạn (Anti-Slop):**
> 1. Giữ nguyên thuật ngữ tiếng Anh chuyên ngành (Product-Led Growth, W2A Funnel, Edge Cases, Universal Link, Deep Link, Attribution Tracking, Latency, Data Contract, Unit Economics...). Không dịch máy gượng gạo sang tiếng Việt.
> 2. Số liệu phải có nguồn trích xuất xác thực (Ahrefs, GSC, Umami) hoặc gắn nhãn `[Assumption]` kèm công thức suy luận Bottom-up. Không tự sinh số liệu giả.
> 3. Lập luận tập trung vào tính phản trực giác (Counter-intuitive), điểm mù thị trường và lợi thế bất đối xứng của Kênh Web MoMo.

---

## THÔNG TIN TỔNG QUAN (METADATA)

| Hạng Mục | Chi Tiết |
| :--- | :--- |
| **Tên Sản Phẩm / Use Case** | `[Tên Sản Phẩm Web - Ví dụ: Vehicle Hub / Tra Cứu Phạt Nguội / Bảo Hiểm]` |
| **Canonical Root URL** | `momo.vn/[product-slug]/` |
| **Trạng Thái Tài Liệu** | `[ ] DRAFT` &nbsp;\|&nbsp; `[ ] UNDER REVIEW` &nbsp;\|&nbsp; `[ ] APPROVED` &nbsp;\|&nbsp; `[ ] IN BUILD` &nbsp;\|&nbsp; `[ ] LIVE` |
| **Governance** | **Web Product Lead:** [Tên Đội Ngũ / Role]<br>**Lead Engineer:** [Tên Đội Ngũ / Role]<br>**Business Owner:** [Tên Đội Ngũ / BU]<br>**PMM:** [Tên Đội Ngũ / Role] |
| **Mốc Tiến Độ Dự Kiến** | Kick-off: `[DD/MM/YYYY]` &rarr; Dev Test: `[DD/MM/YYYY]` &rarr; Pilot: `[DD/MM/YYYY]` &rarr; Go-Live: `[DD/MM/YYYY]` |

---

## 1. PRODUCT OVERVIEW

### 1.1 Elegant Framing
*(Bản tuyên ngôn định vị sắc bén, chỉ ra điểm mù của thị trường và lý do tồn tại cốt lõi của Kênh Web. Viết cô đọng theo 3 luận điểm:)*

1. **Điểm mù của thị trường & đối thủ:** Các bên thứ ba ngoài Open Web đang giải quyết bài toán này ra sao? (Ví dụ: UX lỗi thời, quảng cáo rác, bắt giải CAPTCHA phức tạp, không có hạ tầng tài chính/thanh toán khép kín).
2. **Điểm nghẽn nội tại nếu chỉ làm trên App (App-only Boundary):** Nếu chỉ giam mình trong ứng dụng di động đóng, MoMo sẽ hoàn toàn "vô hình" trước lượng tìm kiếm tự nhiên khổng lồ của người dùng ngoài Open Web.
3. **Lợi thế bất đối xứng của Kênh Web MoMo (MoMo Asymmetric Advantage):** Tận dụng sức mạnh thương hiệu MoMo và năng lực công nghệ để tạo tiện ích Web mở, tốc độ cao (0-CAPTCHA real-time) làm điểm chạm đầu phễu thu hút và chuyển đổi người dùng về App.

### 1.2 Product Vision & PLG Funnel
Tầm nhìn dài hạn của sản phẩm và phễu tăng trưởng Product-Led Growth (PLG) 4 bước:

$$Search Demand (Google/AI) \longrightarrow Web Utility Page \longrightarrow In-App Product/Hub \longrightarrow User Acquisition / Transaction$$

* **Kênh Web (Web Platform):** Thu hút Organic Traffic quy mô lớn từ Open Web, giải quyết nhu cầu tìm kiếm tức thời không cần đăng nhập trước, khởi tạo định danh và kích hoạt Web-to-App.
* **In-App Product (BU Owner):** Điểm đến lưu trữ, quản lý, tự động hóa và cung cấp trải nghiệm sản phẩm sâu (Retention & Engagement).
* **Lớp Sản Phẩm Thương Mại:** Tạo chuyển đổi doanh thu trực tiếp (Doanh thu bán hàng, Phí dịch vụ, GTV...).
* **Strategic Boundaries (What We Will NOT Do):** Định rõ những gì Kênh Web kiên quyết không làm (Ví dụ: không lưu trữ phiên đăng nhập phức tạp trên Web, không biến Web thành bản sao đầy đủ của App, không giữ chân người dùng ở lại đọc tin tức nếu không tạo ra chuyển đổi).

---

## 2. MARKET RESEARCH

### 2.1 Market Sizing & Opportunity (Dạng Bài Luận Lập Luận Từ Dưới Lên - Bottom-up)
*(Bài luận phân tích quy mô thị trường dựa trên Search Demand và Unit Economics, tuyệt đối không trích dẫn số liệu dân số vĩ mô vô thưởng vô phạt. Cấu trúc bài luận gồm 3 tầng:)*

* **Tầng 1 - Addressable Search Demand:** Tổng lượng tìm kiếm hàng tháng trên Open Web bóc tách theo từng cụm nhu cầu. Số liệu trích xuất từ đâu (`Nguồn: Ahrefs / Google Search Console [Tháng/Năm]`).
* **Tầng 2 - Capture Capacity:** Khả năng chiếm lĩnh Organic CTR của MoMo khi lên Top 1 - 3 Google (Ước tính traffic thực tế Kênh Web có thể hứng được hàng tháng).
* **Tầng 3 - Funnel Conversion & Unit Economics:** Lượng Traffic ước tính sẽ chuyển đổi thành bao nhiêu Web-to-App Installs, New Registered Users, hoặc giao dịch thương mại. So sánh giá trị lưu lượng tự nhiên này với chi phí nếu phải trả tiền mua qua Paid Search / Paid Ads (CAC quy đổi).

### 2.2 Competitor Gap Analysis
* **Thực trạng đối thủ bên thứ ba:** Phân tích điểm yếu chí mạng của các website đối thủ hiện tại (UX kém, nhiều popup rác, bắt giải CAPTCHA, thiếu cổng thanh toán hoặc không có khả năng bảo chứng giao dịch).
* **Cơ hội bứt phá của MoMo (MoMo Advantage):** Điểm khác biệt vượt trội của Kênh Web MoMo (0-CAPTCHA, UI/UX hiện đại chuẩn Web Platform, đồng bộ dữ liệu In-App, bảo chứng thương hiệu uy tín).

### 2.3 User Pain Points & Search Demand Inventory
* **User Pain Points (JTBD):** Mô tả 3-4 rào cản lớn nhất của người dùng khi tìm kiếm và sử dụng dịch vụ trên Web.
* **Search Demand Inventory:**

| Nhóm Nhu Cầu (Search Cluster) | Mẫu Từ Khóa Tìm Kiếm (Query Examples) | Monthly Search Volume | Loại Intent (Search Intent) | Nguồn Dữ Liệu |
| :--- | :--- | :---: | :--- | :--- |
| **Nhóm 1: Core Utility** | `[Từ khóa 1]`, `[Từ khóa 2]` | [Volume] | Transactional / High-Intent | Ahrefs / GSC |
| **Nhóm 2: Informational** | `[Từ khóa 3]`, `[Từ khóa 4]` | [Volume] | Informational / Research | Ahrefs / GSC |
| **Nhóm 3: Local GEO** | `[Từ khóa 5]`, `[Từ khóa 6]` | [Volume] | Local Intent / O2O | Ahrefs / GSC |

---

## 3. PRODUCT STRUCTURE

### 3.1 Site Structure (Silo Sitemap & Routing Rules)
Cấu trúc Kênh Web được chia thành **2 Nhóm Cấu Trúc Rõ Ràng**:

#### Nhóm A: Trang Chủ Hub & Các Spoke Pages Trực Thuộc (`/[hub-slug]/*`)

| STT | Tên Trang / Sub-page | URL Canonical | Phân Cấp Routing | Vai Trò Trong Cấu Trúc Sitemap |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Trang Chủ Hub** | `/[hub-slug]/` | Master Hub Root | Cổng tổng điều hướng 360°, tích hợp công cụ tra cứu trung tâm |
| 2 | **[Spoke Page 1]** | `/[hub-slug]/[spoke-1]/` | Spoke Sub-page | Trang tiện ích / thông tin chuyên sâu 1 |
| 3 | **[Spoke Page 2]** | `/[hub-slug]/[spoke-2]/` | Spoke Sub-page | Trang bản đồ địa điểm GEO 2 |
| 4 | **Blog / Cẩm Nang** | `/[hub-slug]/blog/` | Spoke Sub-page | Trang bài viết tư vấn, hướng dẫn và thông tin ngành |

#### Nhóm B: Các Trang Use Case Độc Lập (Top-Level Standalone Canonical URLs)

| STT | Tên Use Case Standalone | URL Canonical | Phân Cấp Routing | Vai Trò & Điểm Khác Biệt Trong Cấu Trúc |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **[Use Case Standalone 1]** | `/[usecase-1-slug]/` | Root Standalone | Utility / Landing độc lập Top 1 Google cho use case 1 |
| 2 | **[Use Case Standalone 2]** | `/[usecase-2-slug]/` | Root Standalone | Trang tiện ích độc lập phục vụ sản phẩm thương mại 2 |

#### Quy Chuẩn Routing URL Technical Rules:
1. **Case Sensitivity:** 100% URL viết chữ thường (lowercase).
2. **Trailing Slash:** Tất cả URL kết thúc bằng dấu gạch chéo `/`.
3. **Canonical Reference:** 100% trang bắt buộc có thẻ `<link rel="canonical" href="..." />` trỏ về chính URL chuẩn tuyệt đối.

---

### 3.2 Content Structure Từng Trang (Functions, Components & UI Specifications)

Bảng đặc tả cấu trúc nội dung chi tiết từng khối thành phần cho từng loại trang:

| Trang / Nhóm Dịch Vụ | Tên Component / Section | Nhu Cầu Người Dùng (JTBD) | Giải Pháp Cấu Trúc (Solution) | Thành Phần UI (UI Components) & Functions |
| :--- | :--- | :--- | :--- | :--- |
| **Master Hub**<br>`/[hub-slug]/` | **Hero & Master Search** | "Tôi muốn tra cứu/sử dụng tiện ích ngay lập tức." | Ô nhập liệu thông minh 1-click + Button Action. | Headline H1 + Input Field + Nút Action 1-click |
| | **Quick Utilities Grid** | "Tôi muốn truy cập nhanh các tiện ích phổ biến." | Grid 6 Card phím tắt điều hướng 6 Spoke cốt lõi. | Grid 6 Card phím tắt tiện ích |
| | **Real-time Data Feed** | "Tôi muốn xem dữ liệu biến động thời gian thực." | Dynamic Feed dữ liệu cập nhật thời gian thực. | Bảng dữ liệu / Map Widget vị trí lân cận |
| | **Local GEO Selector** | "Tôi muốn lọc địa điểm tại khu vực sắp di chuyển đến." | Dropdown lọc Tỉnh/Thành &rarr; Quận/Huyện. | Dropdown chọn Tỉnh/Thành &rarr; Quận/Huyện |
| | **FAQ Accordion Block** | "Tôi muốn giải đáp thắc mắc thường gặp." | Accordion Q&A gắn Schema `FAQPage`. | Accordion list các câu hỏi & câu trả lời |
| **[Standalone Page]**<br>`/[usecase-slug]/` | **Hero & Tool Input** | "Tôi muốn sử dụng công cụ tra cứu/báo giá ngay." | Form nhập liệu trực tiếp bypass CAPTCHA. | Form nhập thông tin + Nút Tra cứu / Báo giá |
| | **Result & Smart CTA** | "Tôi muốn xem kết quả và thực hiện giao dịch." | Output màn hình kết quả + Smart CTA mở App MoMo. | Khối hiển thị kết quả + Banner CTA Web-to-App |
| | **SEO Explanatory Block** | "Tôi muốn đọc hướng dẫn và bảng tra chi tiết." | Nội dung bài viết tư vấn chuẩn SEO 800-1200 từ. | Bài viết hướng dẫn từng bước & Bảng tra chi tiết |

---

### 3.3 Umami Event Tracking theo Touchpoint

*(Quy tắc SSOT: Khai báo chính xác Event Name và Parameters theo đúng quy chuẩn từ file `04_MOSPARK_PLATFORM/umami_utility_tracking.md`)*

| Touchpoint / Vị Trí Tương Tác | Hành Động Người Dùng (User Action) | Umami Event Name | Event Parameters Schema |
| :--- | :--- | :--- | :--- |
| **Hero Search Form** | nhấp vào nút Tra cứu / Tìm kiếm | `search_submit` | `{ query: string, provider?: string }` |
| **Smart W2A CTA Banner** | nhấp vào nút điều hướng mở App MoMo | `w2a_click` | `{ campaign: string, target_screen: string }` |
| **Quick Utilities Grid** | Bấm phím tắt dịch vụ trên Hub | `utility_click` | `{ utility_id: string, destination_url: string }` |
| **GEO Filter Bar** | Chọn bộ lọc Tỉnh/Thành, Quận/Huyện | `filter_select` | `{ province: string, district?: string }` |
| **Merchant Card Snippet** | Bấm vào thẻ địa điểm chi tiết | `merchant_click` | `{ merchant_id: string, category: string }` |
| **Form Báo Giá / Mua Hàng** | nhấp vào nút xem báo giá / mua sản phẩm | `form_submit` | `{ product_id: string, amount?: number }` |

---

## 4. SEO / GEO ONPAGE

### 4.1 Meta Data (Title, Description, Headings, OpenGraph & Social Cards)

#### A. Công Thức Meta Tag Standards

| Loại Trang | Công Thức Tag `<title>` (Max 60 chars) | Công Thức `<meta description>` (150-160 chars) |
| :--- | :--- | :--- |
| **Master Hub** | `[Tên Hub] MoMo - [Lợi ích cốt lõi] 3 Phút` | `[Mô tả tổng quan hệ sinh thái + danh sách tiện ích chính + Call-to-action trên MoMo.]` |
| **Standalone Use Case** | `[Tên Use Case] Online (Không CAPTCHA) - MoMo` | `[Mô tả ngắn chứa từ khóa chính + tính năng nổi bật + Lời kêu gọi hành động.]` |
| **Spoke GEO Page** | `Bản Đồ [Tên Tiện Ích] Gần Đây - MoMo` | `[Mô tả tìm vị trí trạm/garage gần nhất + bộ lọc địa phương + chỉ đường Google Maps.]` |

#### B. Quy Chuẩn Heading Hierarchy (H1 - H4)
* **Quy tắc H1:** Mỗi trang có duy nhất **1 thẻ `<h1>`** đặt tại Hero Section chứa từ khóa chính.
* **Cấu trúc phân cấp chuẩn:**
  ```text
  H1: [Từ khóa chính trang]
     ├── H2: [Tính năng / Công cụ tra cứu cốt lõi]
     ├── H2: [Bảng thông tin / Dữ liệu thời gian thực]
     ├── H2: [Hướng dẫn chi tiết luồng sử dụng]
     │      ├── H3: [Bước 1: ...]
     │      └── H3: [Bước 2: ...]
     └── H2: [Câu hỏi thường gặp (FAQ Accordion)]
  ```

#### C. Social Share Cards Structure (OpenGraph & Twitter)
```html
<meta property="og:type" content="website" />
<meta property="og:title" content="[Title Social Share]" />
<meta property="og:description" content="[Description Social Share]" />
<meta property="og:image" content="https://img.mservice.io/[product-slug]/og-[page-slug].jpg" />
<meta property="og:url" content="https://momo.vn/[product-slug]/[page-slug]/" />
<meta name="twitter:card" content="summary_large_image" />
```

---

### 4.2 Schema.org JSON-LD Specifications

Mỗi loại trang bắt buộc khai báo mã JSON-LD chuẩn trong thẻ `<head>`:

#### A. Master Hub Page (`/[hub-slug]/`)
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://momo.vn/#website",
      "url": "https://momo.vn/",
      "name": "MoMo"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://momo.vn/" },
        { "@type": "ListItem", "position": 2, "name": "[Tên Hub]", "item": "https://momo.vn/[hub-slug]/" }
      ]
    }
  ]
}
```

#### B. Standalone Utility Page (`/[usecase-slug]/`)
Khai báo Schema `@type`: `WebApplication`, `GovernmentService` (nếu có), `FAQPage`.

#### C. GEO Local Pages (`/tram-sac/`, `/garage/`, `/bai-do-xe/`)
Khai báo Schema `@type`: `LocalBusiness` / `AutomotiveBusiness` / `EVChargingStation` / `ParkingFacility`.

---

### 4.3 Sitemap & Technical SEO

1. **Cấu trúc Sub-Sitemaps Index (`sitemap_index.xml`):**
   * `sitemap-[product]-hub.xml`: Trang chủ Hub & các Spoke Pages (`priority: 1.0`, `changefreq: daily`).
   * `sitemap-[product]-standalone.xml`: Các trang Standalone Root-Level (`priority: 0.9`, `changefreq: daily`).
   * `sitemap-merchant.xml`: Các trang chi tiết Merchant đối tác (`priority: 0.6`, `changefreq: weekly`).
2. **Quy tắc Quản lý Crawl Budget:** Trả mã HTTP `410 Gone` và xóa khỏi Sitemap đối với các trang Merchant ngưng hoạt động.
3. **Canonical Rules:** 100% trang có thẻ canonical tự tham chiếu tuyệt đối.

---

### 4.4 GEO / AIO (Generative Engine Optimization cho AI Search)

Để tối ưu khả năng xuất hiện trên Google AI Overview, ChatGPT, Perplexity và Gemini:

1. **Direct Answer Block (25 - 40 từ):** Ngay dưới mỗi tiêu đề `<h2>` của khối FAQ hoặc Hướng dẫn, bắt buộc chứa 1 câu trả lời tóm tắt trực tiếp định dạng Entity-Attribute-Value:
   * *Ví dụ:* **"[Tên dịch vụ] trên MoMo cho phép người dùng [Hành động] trực tuyến trong 1 phút bằng cách [Các bước chính] mà không cần [Rào cản cũ]."**
2. **Standard HTML / Markdown Tables:** Đóng gói toàn bộ dữ liệu so sánh, bảng giá, bảng tra cứu bằng bảng Markdown chuẩn với header và alignment rõ ràng để AI Bot dễ trích xuất.
3. **Authoritative Citations:** Chèn dẫn nguồn tham chiếu trực tiếp đến các cổng thông tin chính phủ / văn bản pháp luật / đối tác chính thức.

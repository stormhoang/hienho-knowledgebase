# Web Health & URL Governance Policy
## momo.vn - Platform Health Management

> **Phiên bản:** 2.0 | **Ngày tạo:** 2026-05-22 | **Ngày hiệu lực:** Sau khi VP phê duyệt
> **Owner:** Văn Hiến - Web Product Lead, Web Platform, GPD
> **Phê duyệt:** Công - VP, Growth Platform Division
> **Trạng thái:** Draft - Pending VP Approval
> **Chu kỳ review:** 6 tháng / khi có thay đổi platform lớn

---

## TÓM TẮT ĐIỀU HÀNH

Chính sách này thiết lập tiêu chuẩn bắt buộc về quản lý vòng đời URL trên www.momo.vn, nhằm bảo vệ hiệu suất SEO/GEO, ngăn ngừa rủi ro AI Search trích dẫn thông tin tài chính sai, và đảm bảo sức khoẻ toàn bộ domain trong dài hạn.

**Vấn đề cốt lõi:** Mô hình PLG của MoMo cho phép Cell Teams tự đưa sản phẩm lên web qua API, nhưng thiếu cơ chế quản lý vòng đời URL sau khi sản phẩm ngưng. Hệ quả là tích lũy crawl waste, pha loãng Topical Authority, và rủi ro AI Search engine trích dẫn thông tin lỗi thời gây hại cho người dùng.

**Giải pháp:** 4 cấp độ xử lý URL theo mức độ nghiêm trọng + quy trình 3 giai đoạn vận hành liên tục.

---

## MỤC LỤC

1. [Mục đích & Phạm vi áp dụng](#1-mục-đích--phạm-vi-áp-dụng)
2. [Định nghĩa thuật ngữ](#2-định-nghĩa-thuật-ngữ)
3. [Chính sách lõi & Nguyên tắc bắt buộc](#3-chính-sách-lõi--nguyên-tắc-bắt-buộc)
4. [4 Cấp độ Xử lý URL](#4-4-cấp-độ-xử-lý-url)
5. [Pre-Launch Gate](#5-pre-launch-gate)
6. [Quy trình Vận hành](#6-quy-trình-vận-hành)
7. [Exception Management](#7-exception-management)
8. [Ma trận RACI & Ownership](#8-ma-trận-raci--ownership)
9. [Chế tài & Enforcement](#9-chế-tài--enforcement)
10. [KPIs & Reporting](#10-kpis--reporting)
11. [Review & Maintenance](#11-review--maintenance)
12. [Phụ lục A: Rủi ro Triển khai](#phụ-lục-a-rủi-ro-triển-khai)
- [Phê duyệt](#phê-duyệt)
- [Changelog](#changelog)

---

## 1. Mục đích & Phạm vi áp dụng

### 1.1 Mục đích

Chính sách này nhằm:
- Thiết lập tiêu chuẩn bắt buộc về chất lượng URL trên www.momo.vn
- Bảo vệ Crawl Budget và Topical Authority của domain
- Ngăn ngừa AI Search engine trích dẫn thông tin tài chính lỗi thời từ momo.vn
- Tạo cơ chế governance rõ ràng giữa Growth Platform và Cell Teams trong toàn bộ vòng đời URL

### 1.2 Phạm vi áp dụng

**Áp dụng cho:**
- Tất cả URL trên domain www.momo.vn và subdomain thuộc sở hữu MoMo
- Tất cả Cell Teams có sản phẩm hoặc tính năng hiển thị trên web
- Tất cả Dynamic Pages được tạo bởi API của Cell Teams
- Tất cả Landing Pages, Hub Pages, Blog Pages, Product Pages

**Không áp dụng cho:**
- Trang kỹ thuật nội bộ: robots.txt, sitemap.xml, các file config hệ thống
- Trang xác thực danh tính: login, register, OTP flow
- API endpoints không phục vụ người dùng cuối

### 1.3 Ngày hiệu lực

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đối tượng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày hiệu lực</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL mới (chưa publish)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ngay khi VP ký phê duyệt</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL hiện có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Theo lộ trình Zero-Traffic URL Audit Q2/2026</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Exception đã tồn tại</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review trong 30 ngày kể từ ngày hiệu lực</td>
    </tr>
  </tbody>
</table>

---

## 2. Định nghĩa thuật ngữ

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật ngữ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Địa chỉ trang web duy nhất trên momo.vn. Ví dụ: momo.vn/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cell Team</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhóm sản phẩm nội bộ sở hữu một tính năng/Use Case cụ thể trên web MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cell PO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product Owner của Cell Team - người chịu trách nhiệm quyết định và phản hồi về các trang web thuộc Use Case đó</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hub Page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang danh mục/tổng hợp của một nhóm sản phẩm. Ví dụ: momo.vn/bao-hiem là Hub Page của nhóm Bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Dynamic Page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang được tạo tự động từ API của Cell Team, nội dung thay đổi theo data. Ví dụ: trang merchant, trang rạp chiếu phim</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Life-cycle URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL có vòng đời xác định trước: campaign ngắn hạn, event theo mùa, khuyến mãi có ngày kết thúc</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Zero-Traffic URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL có dưới 100 organic sessions trong 90 ngày liên tiếp, đo bởi GA4 + GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Organic Traffic</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lượt truy cập từ kết quả tìm kiếm tự nhiên (Google, Bing, AI Search). Không bao gồm paid, direct, referral</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tài chính cốt lõi</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhóm Use Case gắn trực tiếp với Revenue/User Acquisition: Vay Nhanh, Ví Trả Sau (BNPL), Bảo hiểm xe máy, Bảo hiểm ô tô, Bảo hiểm y tế, CIC Score, Tiết kiệm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>YMYL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Your Money Your Life - nội dung có ảnh hưởng trực tiếp đến quyết định tài chính: lãi suất, phí, điều kiện vay, điều khoản bảo hiểm. Yêu cầu cập nhật bắt buộc mỗi 90 ngày</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Topical Authority</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mức độ Google/AI đánh giá momo.vn là nguồn uy tín về một chủ đề. Bị pha loãng khi domain tồn tại quá nhiều trang chủ đề ngoài chuyên môn cốt lõi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Crawl Budget</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giới hạn số trang Googlebot crawl trên momo.vn trong một khoảng thời gian. Trang kém chất lượng tiêu tốn crawl budget không hiệu quả, kéo hiệu suất toàn domain xuống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>W2A (Web-to-App)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ chuyển đổi từ người dùng web sang người dùng App (Install hoặc Register), đo bởi Appsflyer/Onelink</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Noindex</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chỉ thị kỹ thuật bằng meta tag hoặc HTTP header yêu cầu Google không đưa trang vào kết quả tìm kiếm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Growth Platform</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Team Web Platform - cụ thể là Web Product Lead (Hiến) và Head of Web Platform (Bảo)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Growth Plan</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kế hoạch tăng trưởng tối thiểu 6 tháng bao gồm: target keyword cluster, traffic milestone, resource commit</td>
    </tr>
  </tbody>
</table>

---

## 3. Chính sách lõi & Nguyên tắc bắt buộc

### 3.1 Tuyên bố chính sách

**Mọi URL trên www.momo.vn bắt buộc phải đáp ứng ít nhất 1 trong 3 tiêu chí sau:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chí</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngưỡng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn đo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Traffic</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có organic traffic ổn định</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối thiểu 100 sessions/90 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Authority</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuộc tài chính cốt lõi hoặc có Exception approval</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh sách tại mục 2 + Exception Log</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Manual audit</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Plan</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có Growth Plan được Web Product Lead approve</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối thiểu 6 tháng, đủ 3 thành phần bắt buộc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth Plan document</td>
    </tr>
  </tbody>
</table>

**URL không đáp ứng bất kỳ tiêu chí nào bắt buộc phải được xử lý theo 4 cấp độ tại Mục 4.**

### 3.2 Nguyên tắc bắt buộc

1. **Không publish nếu chưa qua Pre-Launch Gate.** Mọi trang mới phải được Web Product Lead approve trước khi đưa lên Production.
2. **Không để trang YMYL lỗi thời quá 90 ngày.** Cell Team bắt buộc cập nhật nội dung YMYL tối thiểu mỗi 3 tháng.
3. **Không redirect 308 về trang không liên quan nội dung.** Nghiêm cấm redirect về trang chủ khi không có Hub phù hợp - phải dùng Noindex (Cấp 3).
4. **Growth Platform có quyền áp dụng Cấp 1 không cần xin phép** khi Cell PO không phản hồi trong 10 ngày làm việc.
5. **Exception bắt buộc phải có VP approve.** Web Product Lead không có thẩm quyền tự approve exception cho Use Case ngoài tài chính cốt lõi.

---

## 4. 4 Cấp độ Xử lý URL

### Tổng quan

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cấp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành động kỹ thuật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tính đảo ngược</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giảm ưu tiên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nofollow + Gỡ Sitemap</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - dễ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuyển hướng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">308 Redirect về Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - khó</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ẩn khỏi Index</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Noindex + Gỡ Sitemap</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - dễ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cập nhật bắt buộc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content refresh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không áp dụng</td>
    </tr>
  </tbody>
</table>

---

### Cấp 1: Nofollow + Gỡ khỏi Sitemap

**Áp dụng khi URL rơi vào ít nhất 1 trường hợp:**
- Dưới 100 organic sessions/90 ngày, không đúng authority, và không có Growth Plan
- Cell PO không phản hồi trong 10 ngày làm việc kể từ thông báo
- Cấp 4 không được thực thi trong 14 ngày làm việc (fallback bắt buộc)

**Cơ chế kỹ thuật:**
- Thêm `rel="nofollow"` vào các internal links trỏ đến trang
- Gỡ URL khỏi sitemap.xml
- Trang vẫn tồn tại và người dùng truy cập được qua link trực tiếp

**Thời hạn với Cell Team:** 3 tháng để cải thiện chỉ số hoặc nộp Growth Plan đạt chuẩn. Hết 3 tháng không có tiến triển - Growth Platform chuyển Cấp 2 hoặc Cấp 3.

---

### Cấp 2: 308 Redirect về Hub Page

**Áp dụng khi:**
- Sản phẩm đã ngưng hoàn toàn VÀ còn tồn tại Hub Page liên quan đang hoạt động

**Cơ chế kỹ thuật:**
- Thiết lập HTTP 308 Permanent Redirect từ URL cũ về Hub Page gần nhất về chủ đề
- Giá trị SEO (link equity) được chuyển về Hub

**Ràng buộc bắt buộc:** Hub Page đích phải liên quan trực tiếp về nội dung. **Nghiêm cấm** redirect về trang chủ hoặc trang không cùng chủ đề.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trường hợp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hợp lệ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/khuyen-mai/cinema-tet-2025 → momo.vn/cinema</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">✅</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/bao-hiem-xe-may/brand-xyz (ngưng bán) → momo.vn/bao-hiem-xe-may</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">✅</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/game/event-cu → momo.vn (trang chủ)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">❌</td>
    </tr>
  </tbody>
</table>

---

### Cấp 3: Noindex - Ẩn khỏi Google Index

**Áp dụng khi:**
- Sản phẩm đã ngưng hoàn toàn VÀ không có Hub Page phù hợp để chuyển hướng
- URL có Life-cycle xác định đã hết hạn (campaign, event, khuyến mãi)

**Cơ chế kỹ thuật:**
- Thêm `<meta name="robots" content="noindex, nofollow">` vào `<head>` của trang
- Hoặc HTTP header: `X-Robots-Tag: noindex, nofollow`
- Gỡ URL khỏi sitemap.xml
- Trang vẫn tồn tại trên server - người dùng có link trực tiếp vẫn truy cập được

**Lý do chọn Noindex thay vì 410 Gone:**
- Khả thi về nền tảng kỹ thuật: chỉ cần meta tag hoặc HTTP header, không cần server-level config
- Reversible: nếu sản phẩm được tái kích hoạt, xoá meta tag là đủ

---

### Cấp 4: Cập nhật nội dung bắt buộc

**Áp dụng khi:**
- URL có ít nhất 100 organic sessions/90 ngày VÀ nội dung YMYL đã lỗi thời (lãi suất, phí, điều kiện)
- URL đúng authority nhưng chưa cập nhật quá 90 ngày (YMYL) hoặc quá 180 ngày (non-YMYL)

**Thời hạn bắt buộc:** Cell Team có **14 ngày làm việc** để cập nhật kể từ ngày nhận thông báo.

**Fallback bắt buộc:** Quá 14 ngày không cập nhật - Growth Platform áp dụng Cấp 1 ngay lập tức. Cell Team vẫn có nghĩa vụ hoàn thành cập nhật.

---

## 5. Pre-Launch Gate

### Điều kiện publish

Mọi trang/sản phẩm mới **bắt buộc phải được Web Product Lead approve** trước khi đưa lên Production. Trang không có approval không được publish.

### Checklist 5 tiêu chí

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chí</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pass/Fail</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Growth Plan</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Roadmap tối thiểu 6 tháng kèm keyword cluster, traffic milestone 3 tháng, tên người phụ trách content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead approve</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Chất lượng nội dung</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nội dung đầy đủ, chính xác. Không phải trang trống hoặc raw API data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead review</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>API ổn định</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API đã QA, có fallback UI rõ khi API lỗi. Không để trang trắng hoặc error message lộ ra người dùng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dev/QC confirm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dev</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cam kết cập nhật</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">YMYL: tối thiểu mỗi 90 ngày. Non-YMYL: tối thiểu mỗi 180 ngày. Cell PO ký xác nhận</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO ký</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cấu hình SEO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Index strategy, schema markup, internal linking, canonical tag đã review và approve</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead approve</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
  </tbody>
</table>

**Growth Plan tối thiểu phải bao gồm 3 thành phần:**
1. Target keyword cluster - tối thiểu 5 từ khóa chính
2. Traffic milestone sau 3 tháng - con số sessions cụ thể
3. Người phụ trách content - tên cá nhân, không phải tên team

**Kết quả Pre-Launch Gate:**
- Pass tất cả 5 tiêu chí: Được publish lên Production theo index strategy đã duyệt
- Fail bất kỳ 1 tiêu chí: Không được publish. Ngoại lệ - publish Cấp 1 (nofollow + không vào sitemap) nếu Cell Team có lý do kỹ thuật phải đặt URL sớm và được Web Product Lead chấp thuận

---

## 6. Quy trình Vận hành

### Giai đoạn 1: Pre-Launch

Xem Mục 5. Web Product Lead là gate duy nhất.

---

### Giai đoạn 2: Giám sát hàng tháng

Growth Platform thực hiện URL Health Scan vào **tuần đầu mỗi tháng** và gửi báo cáo cho từng Cell PO trong 5 ngày làm việc.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ số</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngưỡng cảnh báo</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn dữ liệu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Zero-Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dưới 100 organic sessions/90 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 URL trở lên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi API</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang trả về nội dung trống hoặc error message hiển thị</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 URL trở lên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Health check tự động</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">YMYL quá hạn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">YMYL không cập nhật quá 90 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 URL trở lên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CMS audit</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thin content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dưới 300 từ nội dung unique, không tính navigation và footer</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 URL trở lên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Crawl tự động</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Index errors</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL submitted sitemap nhưng không được index</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trên 5% tổng submitted</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Coverage</td>
    </tr>
  </tbody>
</table>

**Output bắt buộc:** Dashboard + email gửi Cell PO kèm danh sách URL vi phạm cụ thể, cấp độ đề xuất xử lý, và deadline phản hồi.

---

### Giai đoạn 3: Xử lý khi phát hiện vấn đề

```
Growth Platform phát hiện vấn đề
→ Gửi thông báo cho Cell PO (kèm danh sách URL + cấp độ đề xuất + deadline)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
         v
Cell PO phản hồi trong 10 ngày làm việc?
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
    |-- KHÔNG → Growth Platform áp Cấp 1 ngay (không cần xin phép)
    |            → Báo cáo lên HoD của Cell Team
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
    └-- CÓ → Xác định trạng thái sản phẩm
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
              |-- Sản phẩm ĐANG HOẠT ĐỘNG
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
              |    |-- Nội dung YMYL lỗi thời
              |    |   → Cấp 4: Cell Team có 14 ngày cập nhật
              |    |   → Quá hạn: Cấp 1 tự động
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
              |    └-- Vấn đề khác (thin content, API lỗi, zero-traffic)
              |        → Cấp 1: Cell Team có 3 tháng cải thiện
              |        → Hết 3 tháng không tiến triển: chuyển Cấp 2 hoặc Cấp 3
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
              └-- Sản phẩm ĐÃ NGƯNG / Không có kế hoạch
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                   |-- Còn Hub Page liên quan đang hoạt động
                   |   → Cấp 2: 308 Redirect về Hub
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                   └-- Không có Hub phù hợp
                       → Cấp 3: Noindex + Gỡ Sitemap
```

**Web Product Lead** thực thi kỹ thuật. **Dev** hỗ trợ khi cần thay đổi ở server hoặc CMS level. Kết quả cập nhật vào báo cáo tháng tiếp theo.

---

## 7. Exception Management

### 7.1 Tiêu chí được xét exception

Use Case ngoài tài chính cốt lõi được giữ lại trên momo.vn nếu đồng thời đáp ứng **cả 2 tiêu chí:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chí</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngưỡng tối thiểu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn đo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trên 300,000 sessions/quý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 - Organic channel</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web-to-App Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trên 5%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer/Onelink - Install hoặc Register</td>
    </tr>
  </tbody>
</table>

*Ngưỡng này được xây dựng dựa trên benchmark Cinema - Use Case non-financial hiệu quả nhất hiện tại: >1M sessions/quý, W2A 12.1%.*

### 7.2 Quy trình nộp exception

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Bước</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành động</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thời hạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO nộp Exception Request cho Web Product Lead kèm: GA4 export 90 ngày, Appsflyer export 90 ngày, Growth Plan 6 tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead review và đề xuất lên VP</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5 ngày làm việc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VP approve hoặc reject</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5 ngày làm việc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VP (Công)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead thông báo kết quả + ghi vào Exception Log</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2 ngày làm việc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
  </tbody>
</table>

### 7.3 Điều kiện duy trì exception

- Exception có hiệu lực **6 tháng** kể từ ngày VP approve
- Cell PO có trách nhiệm **tái xét** trước khi hết hạn để gia hạn
- Exception **tự động hết hạn** nếu chỉ số traffic hoặc W2A giảm dưới ngưỡng trong 2 quý liên tiếp mà không có kế hoạch phục hồi được VP approve

### 7.4 Exception Log hiện hành

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Case</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lý do</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày VP approve</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hết hạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cinema</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic >1M sessions/quý, W2A 12.1%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pending</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pending</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chờ policy hiệu lực</td>
    </tr>
  </tbody>
</table>

---

## 8. Ma trận RACI & Ownership

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hoạt động</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Web Product Lead (Hiến)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cell PO</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dev (Trọng)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">DA Team</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">VP (Công)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL Health Scan hàng tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phân loại cấp độ xử lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực thi Cấp 1 (nofollow/sitemap)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực thi Cấp 2 (308 redirect)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực thi Cấp 3 (noindex)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xác nhận trạng thái sản phẩm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực thi Cấp 4 (content update)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pre-Launch Gate approve/reject</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Exception Request - đề xuất</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">A</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Escalate Cell PO không hợp tác</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">A</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Monitoring dashboard</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Policy review định kỳ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">C</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">I</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">A</td>
    </tr>
  </tbody>
</table>

*R = Responsible | A = Accountable | C = Consulted | I = Informed*

---

## 9. Chế tài & Enforcement

### 9.1 Quyền hạn của Growth Platform

**Growth Platform có quyền áp dụng ngay, không cần xin phép:**
- Cấp 1 khi Cell PO không phản hồi trong 10 ngày làm việc
- Cấp 1 khi Cấp 4 quá 14 ngày làm việc không được thực thi

**Growth Platform bắt buộc phải escalate lên VP trước khi thực thi:**
- Cấp 2 (308 Redirect) khi Cell PO phản đối
- Cấp 3 (Noindex) khi Cell PO phản đối
- Mọi trường hợp Cell PO từ chối phối hợp sau khi đã áp Cấp 1

### 9.2 Hậu quả không tuân thủ

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vi phạm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hậu quả ngay lập tức</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hậu quả leo thang</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không phản hồi trong 10 ngày làm việc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth Platform áp Cấp 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Báo cáo lên HoD của Cell Team</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cấp 4 quá 14 ngày không thực thi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cấp 1 tự động</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ghi nhận trong báo cáo quý gửi VP</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO từ chối phối hợp sau Cấp 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Escalate VP</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VP quyết định và chỉ đạo trực tiếp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Publish URL không qua Pre-Launch Gate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead yêu cầu takedown hoặc áp Cấp 1 ngay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Báo cáo HoD + VP</td>
    </tr>
  </tbody>
</table>

### 9.3 Dispute Resolution

Khi Cell PO không đồng ý với quyết định phân loại cấp độ của Web Product Lead:

1. Cell PO nộp objection bằng văn bản cho Web Product Lead trong **5 ngày làm việc** kể từ thông báo
2. Web Product Lead và Cell PO họp trong **3 ngày làm việc** để align
3. Không đồng thuận: escalate lên VP (Công). **Quyết định của VP là cuối cùng.**

---

## 10. KPIs & Reporting

### 10.1 KPIs chính sách

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chu kỳ đo</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ URL indexed/submitted sitemap</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng so với baseline Q1/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Coverage</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Crawl errors & Soft 404</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giảm 20% mỗi quý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Coverage</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">YMYL pages cập nhật đúng chu kỳ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CMS audit</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL đang ở Cấp 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giảm dần, mục tiêu 0 sau 12 tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng quý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal log</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thời gian xử lý từ phát hiện đến thực thi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dưới 14 ngày làm việc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal log</td>
    </tr>
  </tbody>
</table>

### 10.2 Lịch báo cáo

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Báo cáo</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tần suất</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Gửi đến</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL Health Report</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng tháng, tuần đầu tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell POs + HoD liên quan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Policy Compliance Summary</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng quý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VP (Công)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Exception Log update</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khi có thay đổi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VP (Công)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
  </tbody>
</table>

---

## 11. Review & Maintenance

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trigger</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chu kỳ review</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Định kỳ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6 tháng/lần</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead + VP</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google algorithm update lớn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trong 30 ngày sau update</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thay đổi platform MoSpark hoặc CMS lớn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trước khi platform change deploy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead + Dev</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Zero-Traffic URL Audit Q2/2026 hoàn thành</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trong 30 ngày sau khi audit xong</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
  </tbody>
</table>

**Mọi thay đổi nội dung chính sách bắt buộc phải được VP approve trước khi có hiệu lực.**
Thay đổi nhỏ về threshold và tiêu chí đo lường: Web Product Lead có thể cập nhật và thông báo VP trong 5 ngày làm việc.

---

## Phụ lục A: Rủi ro Triển khai

*Tài liệu làm việc nội bộ - không phải nội dung governance chính thức.*

### A.1 Rủi ro còn mở

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mức độ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khuyến nghị</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiếu automation cho monthly monitoring - Web Product Lead dễ overload bandwidth khi carry nhiều workstream song song</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Prioritize automation dashboard (Umami Module 5). Xem xét giao execution monitoring cho DA Team (Hải)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell PO từ chối phối hợp kéo dài - Growth Platform không có quyền force Cell Team không qua VP</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình - Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Policy chỉ có răng khi VP mandate được giao rõ ràng và HoD các Cell Team được thông báo trước</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth Plan template chưa formalize trong MoSpark flow - Cell PO có thể nộp kế hoạch chung chung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tích hợp Growth Plan template vào MoSpark onboarding Q3/2026</td>
    </tr>
  </tbody>
</table>

### A.2 Rủi ro đã đóng

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải pháp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xung đột 410 Gone vs Noindex</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cấp 3 thay bằng Noindex - khả thi kỹ thuật hơn, reversible</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v1.1</td>
    </tr>
  </tbody>
</table>

---

## Phê duyệt

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Họ tên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chức vụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày ký</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chữ ký</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Policy Owner</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Văn Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead, Web Platform, GPD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">____________</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">____________</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Approver</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">____________</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VP, Growth Platform Division</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">____________</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">____________</td>
    </tr>
  </tbody>
</table>

*Chính sách có hiệu lực kể từ ngày Approver ký phê duyệt.*

---

## Changelog

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Version</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-22</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo từ GPD-Web Platform SEO_GEO 2026.md. Thêm phân tích khả thi.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-22</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cấp 3 thay 410 Gone bằng Noindex.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-22</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rewrite toàn bộ theo chuẩn Governance Document. Thêm: Scope, Glossary, Exception Management (với ngưỡng định lượng), Enforcement & Consequences, Dispute Resolution, Review Cadence, Approval Block. Phần Risk Analysis chuyển thành Phụ lục A.</td>
    </tr>
  </tbody>
</table>

---

*Policy Owner: Web Platform Team, Growth Platform Division*
*Phê duyệt cần thiết: VP Công (GPD) trước khi distribute cho Cell Teams*

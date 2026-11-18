# MoSpark - AI-Powered Growth Platform
## Product Vision & PRD

> **Owner:** Văn Hiến (Web Product Lead) | **Version:** v3.4 | **Updated:** 2026-05-31

---

## MỤC LỤC

1. [Product Vision](#1-product-vision)
2. [Bối cảnh Chiến lược](#2-bối-cảnh-chiến-lược)
3. [Vấn đề cần giải](#3-vấn-đề-cần-giải)
4. [Users & JTBD](#4-users--jtbd)
5. [Kiến trúc Platform](#5-kiến-trúc-platform)
6. [Module Catalog](#6-module-catalog)
7. [North Star & KPIs](#7-north-star--kpis)
8. [Data Governance](#8-data-governance)
9. [Roadmap 2026](#9-roadmap-2026)
10. [Rủi ro & Giảm thiểu](#10-rủi-ro--giảm-thiểu)
11. [RACI & Collaboration](#11-raci--collaboration)
12. [Tài liệu Liên kết](#12-tài-liệu-liên-kết)
13. [Version Log](#13-version-log)

---

## 1. Product Vision

### 1.1. Phát biểu Tầm nhìn

> **"MoSpark là nền tảng Growth Intelligence của momo.vn: CEO, VP và Head of BU thấy rõ Market Sizing từng Use Case để ra quyết định triển khai đúng - PM/PO tự chủ thực thi từ ý tưởng đến kết quả kinh doanh thực, không phụ thuộc Dev."**

> **Elegant Problem:** momo.vn không thể tăng trưởng organic bền vững khi PM phụ thuộc Dev cho mọi thứ, AI sản xuất content không có guardrail, và không ai biết MoMo đang chiếm bao nhiêu % thị trường tìm kiếm.

MoSpark không phải là một CMS nâng cấp. Đây là nền tảng cho phép Web MoMo chủ động tăng trưởng - từ sản xuất nội dung, phân phối Ads đến chuyển đổi Web-to-App - theo một quy trình có thể lặp lại, đo lường được và ngày càng ít cần can thiệp thủ công.

### 1.2. Nguyên tắc vận hành

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguyên tắc</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ý nghĩa thực tế</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PM/PO self-service</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM tạo Landing Page trong 1-2 ngày thay vì 1-2 tuần. Chạy Ads mà không cần nhờ Dev.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quality gate bắt buộc</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có trang nào được live khi chưa qua SEO/GEO Scoring. Publish phải đúng ngay từ đầu.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Use Case là đơn vị gốc</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mọi content, Ads, analytics đều gắn theo Use Case - không gắn theo Cell Team hay Division.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1 Keyword = 1 URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hệ thống tự block nếu tạo 2 bài cùng primary keyword. Không để cạnh tranh nội bộ.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>AI sản xuất, người chịu trách nhiệm</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI draft, con người review và sign-off - đặc biệt với nội dung tài chính (YMYL).</td>
    </tr>
  </tbody>
</table>

### 1.3. Định vị

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chiều</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CMS cũ (Admin Panel)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">HubSpot</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoSpark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mạnh nhất</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản lý nội dung tĩnh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đo lường sau publish</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quality gate + AI production trước publish</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yếu nhất</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phụ thuộc Dev cho mọi thứ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có hard block</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Visibility tracking sau publish (đang build)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phù hợp nhất</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo 2022-2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">B2B Marketing platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo 2026+ - AI-native fintech growth</td>
    </tr>
  </tbody>
</table>

---

## 2. Bối cảnh Chiến lược

### 2.1. Mandate Chiến lược

momo.vn Website không còn là corporate site hay blog SEO đơn thuần. MoSpark được xây để hiện thực hóa 3 vai trò chiến lược:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoSpark đóng góp gì</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Financial & Payment Authority</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm đến uy tín, tiếng nói có thẩm quyền trong ngành tài chính/thanh toán Việt Nam</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quality Gate bắt buộc, Named Author Policy, E-E-A-T content chuẩn YMYL</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Entry Point từ Search</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm chạm đầu tiên đón traffic tìm kiếm tự nhiên - cả Google lẫn AI Search</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO Inventory, GenAI Content Engine, llms.txt pipeline</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ecosystem Support Layer</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nền tảng hỗ trợ toàn bộ hệ sinh thái kinh doanh & thanh toán của MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Use Case ID gắn kết mọi module, Ads Manager, Web-to-App attribution</td>
    </tr>
  </tbody>
</table>

**Flow bất biến - mọi quyết định sản phẩm đều trace về đây:**
```
Content → Keywords → Ranking → Use Case → User Journey → App/Transaction (New User / MAU)
```

Mục tiêu không dừng ở pageview. Mục tiêu là kích hoạt hành vi chuyển đổi trong App.

### 2.2. 4 Growth Pillars - Kiến trúc Thị trường

momo.vn không tổ chức theo BU - tổ chức theo Product / Search Ecosystem. 4 Pillars là 4 growth engine độc lập, mỗi Pillar sở hữu một vertical thị trường để chiếm thị phần tìm kiếm:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pillar</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Cases</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chiến lược Content</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ràng buộc bắt buộc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P1 - Tài chính & Tín dụng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CIC Score, Ví Trả Sau, Vay Nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub-Spoke + Interactive Tools (tính lãi, mô phỏng CIC)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Named Author Policy - hard gate trước launch</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P2 - Bảo hiểm Công nghệ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH xe máy, BHYT, BHXH, BH ô tô</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Neutral Aggregator - cổng so sánh trung lập</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không dùng geo-based URL cho bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P3 - Dịch vụ Công & Tiện ích</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt Nguội, Hóa đơn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API real-time + pSEO (63 tỉnh)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">llms.txt mandatory trước rollout</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P4 - Đời sống & Merchant</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cinema, OTA, eSIM, Merchant</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Intent-first, Merchant Detail Page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Noindex mandatory cho URL hết hạn (410 Gone đã bỏ - hạ tầng không hỗ trợ)</td>
    </tr>
  </tbody>
</table>

**Utility-First** là nguyên tắc vận hành: Interactive tools (calculator, simulator, checker) là core value thực sự - content là supporting layer tạo discoverability và giáo dục. Mỗi Use Case mới phải trả lời: "Utility tool của Use Case này là gì?"

### 2.3. Bối cảnh thị trường

AI Search đang thay đổi cách người dùng tìm kiếm thông tin tài chính:
- Google searches/user giảm ~20% YoY năm 2025.
- ChatGPT: 700M weekly active users, tăng 2x trong 6 tháng.
- Perplexity: 780M queries/tháng, tăng 20%+ MoM.
- AI Overviews xuất hiện trên 13-30% queries - fintech là category trigger cao.
- Người dùng VN đang hỏi AI: *"ví điện tử nào tốt nhất"*, *"vay tiền online uy tín"*. Nếu MoMo không có structured context, AI trả lời theo nội dung của competitor.

MoMo từng ghi nhận 0% AI Chatbot referral so với Wise.com 40%+. Sau khi pilot `llms.txt` trên Phạt Nguội (May 2026), chúng ta bước đầu nhận được hơn 660 citations và lượng traffic thực tế từ ChatGPT. Trước xu thế dịch chuyển mạnh mẽ của người dùng sang các công cụ AI Search và Chatbot thế hệ mới, đây là cơ hội vàng để MoMo nhanh chóng hoàn thiện và scale up hạ tầng GEO, củng cố vị thế dẫn đầu thị phần hiển thị trên các công cụ tìm kiếm thế hệ mới.

---

## 3. Vấn đề cần giải

### 3.1. PM/PO phụ thuộc Dev cho mọi thứ

- Tạo Landing Page: chờ Dev sprint, mất 1-2 tuần.
- Chạy Ads: nhờ Dev hardcode, mỗi campaign mất nhiều ngày.
- Thay đổi nội dung nhỏ: vẫn phải raise ticket.

Hậu quả: PM không prototype được, requirement "bay bổng" vì không thấy thực tế. Campaign chậm, missed opportunity.

### 3.2. Content production thiếu chuẩn hóa

- AI cá nhân (ChatGPT/Claude) dùng rời rạc, mỗi người prompt một kiểu khác nhau.
- Không có Business Context làm nền - AI dễ bịa thông tin sản phẩm.
- Không có gate chặn nội dung kém chất lượng trước khi publish. YMYL content tài chính có thể lên live không qua review.
- Không track được MoMo đang xuất hiện bao nhiêu % trong AI Search.

### 3.3. Quản lý Web đang theo Cell Team, không theo Use Case

- Media Team phải đăng nhập vào từng Cell Team (Vay, Cinema, Bảo hiểm...) để đăng 1 bài blog. Không có single interface.
- URL chồng chéo: `momo.vn/blog/*` và `momo.vn/{use-case}/blog/*` tồn tại song song, cạnh tranh lẫn nhau (Keyword Cannibalization).
- Analytics bị phức tạp hóa do URL structure không thống nhất.
- Ads conflict: nhiều Division muốn chạy Ads đồng thời trên cùng một trang, không có cơ chế quản lý.

### 3.4. MoSpark KHÔNG phải

Scope rõ không kém scope có. Dưới đây là những gì MoSpark không làm - để tránh scope creep và giữ đúng mandate:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoSpark KHÔNG phải</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lý do cần nói rõ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Một CMS thụ động thay thế Admin Panel</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoSpark là Growth OS có Quality Gate và AI Production tích hợp - không đơn thuần thay cái cũ bằng cái tương đương</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Công cụ tự publish không kiểm soát</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mọi trang đều phải qua SEO/GEO Scoring Gate - không có ngoại lệ, không có bypass dù PM/PO tự làm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thay thế Dev hoàn toàn</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM/PO tự làm LP và Ads Manager trong phạm vi đã build - module mới vẫn cần Dev theo spec</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Platform để AI tự publish YMYL content</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI draft - con người review và sign-off trước publish, bắt buộc với nội dung tài chính</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giải pháp mở rộng cho tất cả BU cùng lúc</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GTM bắt đầu từ User Growth - chứng minh giá trị trước, scale từng Pillar có dữ liệu sau</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hệ thống tích hợp Payment trực tiếp</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Excluded scope do rào cản pháp lý và after-sale service - không phải roadmap</td>
    </tr>
  </tbody>
</table>

---

## 4. Users & JTBD

### 4.1. Nhóm người dùng

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Persona</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ai</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pain point</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cần gì từ MoSpark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PM/PO Cell Team</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PO Vay Nhanh, Cinema, Bảo Hiểm, Phạt Nguội...</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phụ thuộc Dev cho LP, Ads, content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tạo LP, chạy Ads, nhập Business Context trong cùng ngày</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Content Writer / Media Team</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Writers, Agency content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng nhập nhiều CMS, prompt AI mỗi người mỗi kiểu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 interface duy nhất, AI pipeline chuẩn hóa, không cần học lại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Product Lead</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Văn Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Audit thủ công từng trang, không có SoV visibility</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quality gate tự động, SoV dashboard, data để quyết định đầu tư Use Case nào</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Platform Admin</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo (Web Platform Manager)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads conflict giữa Division, không có inventory view</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Placement Registry, enforce policy, không cần review từng campaign</td>
    </tr>
  </tbody>
</table>

### 4.2. Jobs To Be Done cụ thể

**PM/PO cần:**
1. Tạo LP mới cho campaign mà không cần Dev - xong trong 1 ngày.
2. Biết Use Case của mình đang chiếm bao nhiêu % market (SoV) để justify budget đầu tư.
3. Chạy Ads đúng trang, đúng context, đo được click → install.
4. Nhập Business Context 1 lần, AI dùng làm nền cho tất cả bài blog sau đó.

**Content Writer cần:**
1. Viết bài đạt SEO/GEO E-E-A-T mà không phải nhớ hết các quy tắc.
2. Biết ngay primary keyword mình chọn đã có người dùng chưa - tránh viết trùng.
3. Biết bài đang thiếu gì để đạt điểm 80+.

**Web Product Lead cần:**
1. Block được nội dung kém chất lượng trước khi ảnh hưởng domain authority.
2. Thấy được AI engine đang cite MoMo như thế nào cho từng Use Case.
3. Ưu tiên Use Case nào đáng đầu tư dựa trên Market Volume và SoV gap thực tế.

---

## 5. Kiến trúc Platform

MoSpark vận hành theo 5 lớp, phủ kín toàn bộ lifecycle từ market research đến conversion, đo lường và tối ưu liên tục:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Layer</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Modules</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>L5</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth Intelligence</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 2-3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO Citation Monitor, Experiment Engine, Revenue Attribution, Content Intelligence</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Close feedback loop: đo lường toàn bộ vòng lặp, học hỏi, cải tiến compound</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>L4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Performance Loop</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Auto-Refresh, SoV Tracker, Content Decay Detection, Health Alert, Semantic Linking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Feed data ngược lại để tối ưu tiếp</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>L3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quality Gate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO/GEO Scoring 100pt, Hard Block CWV, Legal Review, YMYL Guard</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Block nội dung xấu trước publish</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>L2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Distribution & Conversion + PLG</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active - Scaling</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads Manager, Widget Library, PLG Tool Builder, Onelink, Umami Attribution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Convert traffic thành App user + PLG Tools tạo data moat chống LLM</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>L1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Production</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active - Pilot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO Inventory, Business Context, 7-Step AI Workflow, Blog Editor</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sản xuất nội dung đạt chuẩn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>F</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Foundation - Use Case System</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Always-on</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Use Case ID, Market Map, Keyword Registry, URL Governance, PLG Tool Registry</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đơn vị gốc kết nối tất cả modules</td>
    </tr>
  </tbody>
</table>

### 5.1. Layer 1 - Content Production

- **7-Step Workflow:** Market Selection → Business Context → Keyword Registry → AI Outline → Manual Edit → AI Blog Detail → SEO/GEO Score → Sync & Publish.
- **Engine:** Claude API với Grounding Search (luôn kiểm tra thông tin thực tế).
- **Chống Cannibalization:** Keyword Master Registry check trùng trước khi tạo bài. 1 keyword = 1 bài, không có ngoại lệ.
- **Business Context 12 fields** là source of truth - AI chỉ viết trong ranh giới PM đã xác nhận. Không bịa tính năng, không nhắc competitor.

### 5.2. Layer 2 - Distribution & Conversion

- **Ads Manager:** Core Ops (Widget/Balloon) → Traffic Inventory (Placement Registry) → Retargeting & Multi-tenant.
- **Native Widget (format chủ lực):** Nhúng shortcode `[widget:phat-nguoi]` trực tiếp vào bài blog. Trải nghiệm tự nhiên nhất, W2A conversion cao nhất, không interrupt SEO.
- **Attribution:** Umami (on-site) + Appsflyer/Onelink (Web-to-App) + GA4 (marketing).

### 5.3. Layer 3 - Quality Gate

- **5-Block Scoring (100 điểm):** Technical SEO+CWV (30pt) | On-Page Content (35pt) | Structured Data+GEO (20pt) | OG Tags (5pt) | Manual Review (10pt).
- **Hard Block:** Canonical sai, Robots=noindex, LCP>2.5s, INP>200ms, CLS>0.1, Không có CTA, Primary Keyword trống.
- **Ngưỡng Publish:** Score < 60 hoặc có Hard Block → Blocked hoàn toàn | 60-79 → Warning | ≥ 80 → Pass.

### 5.4. Layer 4 - Performance Loop (Phase 2+)

- **GSC Auto-Refresh:** Phát hiện content decay → kích hoạt AI Enhance.
- **SoV Dashboard:** Theo dõi AI citation rate theo Use Case trên ChatGPT, Perplexity, Google AI Overviews.
- **Health Alert:** Cảnh báo URL 404, traffic sụt bất thường.
- **Semantic Linking:** Gợi ý internal link dựa trên vector embeddings.

### 5.5. Danh mục 7 loại trang chiến lược

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Pattern</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại trang</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò SEO/GEO</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Builder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/{mini-web}</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mini Web Use Case</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rank transactional keywords, capture intent mua hàng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing Page Builder</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/{mini-web}/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth Blog (Use Case)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Satellite content, dồn Link Equity về Mini Web</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth Blog (General)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational keywords, Topical Authority</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Merchant Page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cross-sell, Local SEO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LP Builder + Merchant Module</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tin-tuc*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">News/Communications</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand presence, PR</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CMS</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/hoi-dap*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Help Center</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User support, Featured Snippets</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Help Center Module</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing Page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Campaign / Promotion</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Conversion-focused, không cần rank dài hạn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LP Builder</td>
    </tr>
  </tbody>
</table>

---

## 6. Module Catalog

### 6.1. Tổng quan

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Module</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing Page Builder</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tạo Landing Page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Production - Q2 Onboarding GPD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo + Thuận</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Content Production</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active - Pilot Phạt Nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trọng (AI Tool/Model/Workflow), Thuận (GenAI Hình), Lộc (phân quyền User), Hiến (govern)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads Manager</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web-to-App Conversion</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">V1.2 Production - Pilot User Growth</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1→2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận, Bảo</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO/GEO Scoring Gate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quality Control</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active - All Page Types</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận (build), Hiến (govern)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO Inventory</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Market Map & SoV</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active (Manual) → Dashboard Integration</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1→2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận, Hiến</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Crawler Policy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">llms.txt + robots.txt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">robots.txt L1 Deployed</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến (spec), Web Platform</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Help Center Agentic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI-powered FAQ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Registered - Agentic Org Program</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migration</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin Panel → MoSpark</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Structure & Mapping Phase</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo + Thuận + Lộc</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PLG Tool Builder</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility Tool Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning - Spec Phase</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo + Thuận + Hiến</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Experiment Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Native AB Testing</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận + DA</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M11</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Revenue Attribution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web-to-App ROI Pipeline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận + DA (Hải)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Intelligence</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Decay Detection + Opportunity</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2→3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận + Hiến</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M13</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO Citation Monitor</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Engine Citation Tracking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến (spec) + Thuận</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M14</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">HRM API Sync (LnD)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đồng bộ Data Nhân sự / Phân quyền</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ý tưởng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2H Customer KB</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tích hợp Meeting Notes / JTBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ý tưởng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo</td>
    </tr>
  </tbody>
</table>

---

### 6.2. M1 - Landing Page Builder

**Mục đích:** PM/PO tự tạo Landing Page mà không cần Dev sprint.

**Trạng thái:** Production. Q2 onboarding GPD.

**Năng lực cốt lõi:**
- Block-based WYSIWYG builder.
- Template library theo Use Case (tài chính, bảo hiểm, BNPL).
- CTA + Onelink integration built-in.
- SEO/GEO Scoring Gate bắt buộc trước Publish.
- Mobile-first preview.

**Success Metrics:**
- Time-to-live LP: từ 1-2 tuần → dưới 1 ngày.
- 80%+ LP mới do PM/PO tự tạo, không qua Dev.

---

### 6.3. M2 - GenAI Content Engine

**Mục đích:** Chuẩn hóa quy trình sản xuất Blog/Mini Web bằng AI. Đảm bảo E-E-A-T, không có nội dung trùng keyword, sẵn sàng cho AI Search citation.

**Trạng thái:** Active. Pilot Phạt Nguội xong. Scale sang Financial products (Vay Nhanh, Ví Trả Sau, CIC).

**Tam giác dữ liệu:**
1. **Business Context (BU):** Value Prop, Trust Signals, Disclaimer, Blacklist Terms - 12 fields chuẩn. PM xác nhận và chịu trách nhiệm pháp lý.
2. **Market/Cluster (Hiến - SEO Tools):** Volume, Keyword, Intent - dữ liệu thị trường định lượng.
3. **GenAI Engine:** AI viết bài trong ranh giới Business Context + Keyword từ thị trường.

**7-Step Workflow:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Bước</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành động</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạo Use Case + Project Mapping</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Use Case ID</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM/Growth</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhập Business Context 12 fields</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Context Layer (Source of Truth)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM/Growth + Web Product Lead</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạo Primary Keyword + Secondary, check trùng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keyword Master Registry</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Team</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI tạo dàn ý → Content edit → PM approve</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Outline Final</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content + PM</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI viết bài chi tiết theo Outline đã approve</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Detail Draft</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI (Claude API)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review chất lượng, SEO/GEO Score, sign-off</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Verified Content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sync qua Blog Editor → Publish</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Live on momo.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Team</td>
    </tr>
  </tbody>
</table>

**3 Rules không được phá vỡ:**
- **Project-First:** Keyword không tồn tại nếu không gắn Use Case.
- **1-1 Mapping:** 1 Primary Keyword = 1 URL. Tạo trùng → bị block.
- **Single Ownership:** 1 Keyword chỉ thuộc 1 Project.

**Success Metrics:**
- Năng suất: 10 bài/tháng/writer → 20 bài/tháng/writer.
- Quality: 100% bài AI qua Hard Block của Scoring Gate.
- SOV Target: ≥ 30% citation rate cho Primary Keywords của Use Case.

---

### 6.4. M3 - Ads Manager

**Mục đích:** Phân phối nội dung khuyến mãi đúng trang, đúng context để chuyển đổi traffic Web thành App user hoặc reactivate MAU. PM/PO tự chạy, không cần Dev.

**Trạng thái:** V1.2 Production. Pilot User Growth. Trọng tâm đang chuyển sang Native Widget.

**So với Athena (In-App Ads):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chiều</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Athena (App)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ads Manager (Web)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User identity</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã định danh, có lịch sử giao dịch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Anonymous (Web chưa có Login)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Targeting</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Audience Segment (behavioral)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL context của trang (intent-based)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bidding</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - 3 chiến lược</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Priority-based, không bidding</td>
    </tr>
  </tbody>
</table>

**5 Ad Formats:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Format</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mức interrupt</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phù hợp với</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Native Widget (Shortcode)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất thấp - PLG</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Article, Mini Web</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A Conversion cao nhất</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Balloon / Float Icon</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tất cả trang</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic + Awareness</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Inline Banner</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog/News</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Awareness</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sticky Bar</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing Page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Popup</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao - <em>chỉ LP có promotion</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing Page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic (hạn chế)</td>
    </tr>
  </tbody>
</table>

**Phased Roadmap:**

**Phase 1 - MVP (Q2/2026 - Đang làm):**
- Widget Library: Phạt Nguội + BHYT embed qua CMS Shortcode `[widget:phat-nguoi]`.
- URL context targeting cơ bản.
- Umami Reach Estimate khi setup campaign (28-day visitors per Use Case).
- Auto-Publish cho PM/PO ở giai đoạn < 50 campaigns.

**Phase 2 - Inventory Management (Q3/2026):**
- **Placement Registry:** Toàn bộ ad slots đăng ký tập trung - Use Case Placements + Shared-source GPD.
- **Conflict Resolution:** Tự động detect và resolve khi nhiều campaign tranh cùng placement.
- **SEO Inventory Dashboard:** Market Volume per Use Case, bar chart breakdown.
- Global guardrail cứng: max 1 Popup/session, max 2 Balloon cùng lúc.

**Phase 3 - Retargeting & Multi-tenant (Q4/2026):**
- **On-site Retargeting:** Local Storage ghi vết intent, reactivate khi user vào trang dùng chung. Không cần Login, 100% anonymous.
- **Multi-tenant:** PM/PO Division tự tạo và vận hành campaign trong phạm vi Placement của Division.
- **Umami Dashboard per Division:** Impression, Click, CTR, Dismiss Rate.

**KPIs:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTR (Traffic campaigns)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.4%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4%+</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dismiss Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">78.3%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 65%</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Time-to-live campaign</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhiều ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 1 ngày</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Placement conflict rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 10%</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Division self-service rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">80%+</td>
    </tr>
  </tbody>
</table>

---

### 6.5. M4 - SEO/GEO Scoring Gate

**Mục đích:** Block nội dung không đủ chuẩn trước khi Publish. Không có ngoại lệ, không có cách bypass.

**Trạng thái:** Active. Áp dụng cho tất cả Page Types.

**Scoring Model (100 điểm):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Block</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kiểm tra gì</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 - Technical SEO + CWV</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">30</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Canonical, Robots, H1, LCP/INP/CLS</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2 - On-Page Content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">35</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Wordcount, Keyword density/placement, CTA</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3 - Structured Data + GEO Signals</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Schema, FAQ, Entity, datePublished, Fact Density</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4 - OG/Social Meta</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">og:title, og:description, og:image</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5 - Manual Review</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Preview, Mobile check, GSC status, Sitemap</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tổng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>100</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
  </tbody>
</table>

**Publish Gate:**
- Score < 60 hoặc có Hard Block → Nút Publish bị disable hoàn toàn.
- Score 60-79 → Publish với badge "⚠ Cần tối ưu".
- Score ≥ 80 → Publish bình thường.

**9 Hard Block Conditions:** Canonical không tồn tại | Canonical sai URL | Robots = noindex | LCP > 2.5s | INP > 200ms | CLS > 0.1 | Không có CTA | Primary Keyword trống | CWV chưa Run.

---

### 6.6. M5 - SEO Inventory

**Mục đích:** Là điểm khởi đầu của mọi dự án trên MoSpark. Quyết định Use Case nào đáng làm, Keyword nào nên sản xuất trước.

**Trạng thái:** Phase 1 Live (Manual - Excel). Phase 2 Planning (tích hợp Dashboard vào CMS).

**Luồng khởi tạo dự án:**

1. Xác định Use Case → tra Total Search Volume trong Inventory.
2. Hệ thống tự phân nhóm ưu tiên (4 tiers):
   - **Market Leader (SoV > 40%):** Duy trì, scale ngách.
   - **High Potential (SoV 20-40%):** Scale nội dung mạnh.
   - **Gap lớn (SoV < 20%):** Xây mới nền tảng.
   - **Mass Traffic:** Kéo user lớn về hệ sinh thái (Phạt Nguội, BHXH...).
3. PM nhập Business Context 12 fields.
4. Kick-off 7-Step GenAI Workflow.

**Priority Scoring (SEO-ICE):**
```
Opportunity Score = Search Volume × (Target SoV - MoMo SoV) × Expected W2A CR
Priority Score = Opportunity Score / Complexity (1-5)
```

**SoV Formula:**
```
SoV MoMo = Impression (GSC) / Total Volume Search
```

---

### 6.7. M6 - AI Crawler Policy

**Mục đích:** Kiểm soát cách AI systems hiểu và cite MoMo. Đây là foundation cho GEO - nếu robots.txt block nhầm search crawlers, mọi effort GEO đều vô nghĩa.

**Trạng thái:** robots.txt Layer 1 (`/*?` fix) đã Deploy. llms.txt chưa triển khai.

**3 loại AI crawler, 3 cách xử lý:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Xử lý</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search/RAG crawler</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">OAI-SearchBot, Claude-SearchBot, PerplexityBot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>ALLOW</strong> - phục vụ user queries real-time</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Training crawler</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GPTBot, ClaudeBot, Google-Extended</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Policy decision</strong> - chờ Legal</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Aggressive scraper</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bytespider, CCBot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>BLOCK</strong> - không có referral benefit</td>
    </tr>
  </tbody>
</table>

**llms.txt Architecture:**
- `momo.vn/llms.txt` - Master index (Layer 1 - cần làm).
- `momo.vn/{product}/llms-full.txt` - Full doc per product (Layer 2).
- Content rule: Giữ định nghĩa sản phẩm, điều kiện, quy trình. Loại bỏ lãi suất cụ thể, promotional copy, testimonials.

---

### 6.8. M7 - Help Center Agentic

**Mục đích:** Chuyển FAQ tĩnh thành AI Agent - user hỏi gì được trả lời ngay, giảm friction trước khi abandon.

**Trạng thái:** Đã đăng ký Agentic Org Program. Chờ phê duyệt.

---

### 6.9. M8 - Migration (Admin Panel → MoSpark)

**Mục đích:** Hợp nhất toàn bộ nội dung từ Admin Panel cũ sang MoSpark. Single Interface cho Media Team.

**Trạng thái:** Structure & Mapping Phase. Zero Redirect approach đã approve.

**Blog 2-Tier (giữ nguyên URL, không redirect):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tier</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier 1 - Basic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">General, News, FAQ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier 2 - Advanced</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/{use-case}/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay Nhanh, Cinema, BH Ô tô, BH Xe máy</td>
    </tr>
  </tbody>
</table>

**3 Migration Phases:** Foundation + `/blog/*` (4-6 tuần) → 4 special Use Case blogs (6-8 tuần) → Optimization + Decommission Admin Panel cũ (4 tuần).

**Success Gate:** Traffic retention > 98% | Indexation 100% trong 14 ngày | Zero redirect.

---

### 6.10. M9 - PLG Tool Builder

**Mục đích:** Chuẩn hóa build và deploy Utility Tools trên momo.vn. PM/PO tự tạo Calculator, Checker và Comparison tool mà không cần Dev sprint. Mỗi tool tạo ra interaction data độc quyền - đây là anti-LLM moat thực sự của momo.vn.

**Trạng thái:** Planning - Spec Phase.

**Vì sao PLG Tool là core value, không phải nice-to-have:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kênh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cơ chế chuyển đổi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Số bước đến intent cao nhất</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User đọc → có thể click CTA → có thể download App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3-4 bước, intent decay theo mỗi bước</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PLG Tool</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User DÙNG tool để giải quyết việc → nhận kết quả → CTA sau result</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1-2 bước, intent ở đỉnh khi nhận kết quả</td>
    </tr>
  </tbody>
</table>

Utility-First không phải slogan - đây là cơ chế chuyển đổi khác nhau về cấu trúc.

**4 Tests phân biệt PLG Tool thực sự với widget thông thường:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Test</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Câu hỏi kiểm tra</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pass khi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>JTBD Test</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tool giải quyết JTBD cụ thể mà không cần user download App trước?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User hoàn thành task trong 1 phiên trên web</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Data Test</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tool tạo interaction data mà LLM không thể có từ nguồn khác?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Data là unique: usage patterns, regional distribution, real-time inputs</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1-2-3 Test</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User nhận kết quả trong 3 bước, không cần hướng dẫn?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No tutorial needed, no drop-off mid-flow</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Funnel Test</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA sau kết quả dẫn về App feature tương ứng một cách tự nhiên?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA xuất hiện sau result, không interrupt trước</td>
    </tr>
  </tbody>
</table>

**3 Loại PLG Tool - Taxonomy:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cơ chế</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ trên momo.vn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pillar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Type A - Calculator</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User nhập thông số → tính theo công thức → kết quả số</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tính lãi vay, Tính phí BH xe máy, Tính lãi tiết kiệm, Tính mức phạt theo lỗi vi phạm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P1, P2, P3</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Type B - Checker / Lookup</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User nhập ID → query API real-time → kết quả cụ thể</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra phạt nguội (biển số xe), Tra điểm tín dụng CIC, Tra BHXH eligibility</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P1, P3</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Type C - Comparison / Aggregator</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Platform pull data nhiều nguồn → user filter → bảng so sánh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">So sánh gói BH xe máy, So sánh gói cước viễn thông, So sánh lãi suất tiết kiệm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P2, P4</td>
    </tr>
  </tbody>
</table>

**Mapping PLG Tools theo 4 Growth Pillars:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pillar</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tools cần build</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Data được tạo ra</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đợt Triển Khai</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P1 - Tài chính & Tín dụng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loan calculator, CIC score simulator, VTS eligibility checker</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhu cầu vay theo khu vực, phân phối credit score người dùng thực tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P2 - Bảo hiểm Công nghệ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH cost calculator (xe máy, ô tô, BHYT), Plan comparison</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phân phối mức phí thị trường, preference theo gói, demographic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P3 - Dịch vụ Công & Tiện ích</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt nguội lookup (LIVE - mở rộng), BHXH checker, Hóa đơn lookup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Volume tra cứu theo loại vi phạm, khu vực, thời điểm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LIVE - scale</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P4 - Đời sống & Merchant</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Merchant finder, Cinema showtime lookup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Demand theo khu vực, genre preference, payment pattern</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 3</td>
    </tr>
  </tbody>
</table>

**Builder Requirements - PM/PO phải tự làm được không qua Dev:**

1. Chọn Tool Type (Calculator / Checker / Comparison)
2. Define inputs: tên field, data type, required/optional, validation rule
3. Configure logic: công thức tính (Type A) | API endpoint + params (Type B) | data source + filter columns (Type C)
4. Set result format: số đơn | bảng chi tiết | Yes/No + lý do | range
5. Add CTA sau result: text, Onelink deep link đến App feature cụ thể
6. Set tracking: submit_tool + view_result + click_cta - tự động, không config thêm
7. Embed via shortcode: `[tool:loan-calculator]` vào bất kỳ page nào trong MoSpark
8. Preview mobile/desktop → Publish

**Data Pipeline - Cách PLG Tools tạo anti-LLM Moat:**

```
User query → Tool interaction → Result served
                 ↓ (anonymous log, no PII)
         Aggregate weekly batch
                 ↓
    Unique Insights được publish:
    "Mức phạt vượt đèn đỏ trung bình tại HCM: Xđ (Y tra cứu, tháng Z/2026)"
    "Người VN vay trung bình Xtr, kỳ hạn Y tháng, lãi suất kỳ vọng Z%/năm"
                 ↓
    Data Articles → GEO Citation Signal → LLM-proof unique content
```

Không có competitor nào có data này. Không LLM nào có thể fabricate data này. Đây là moat duy nhất bền vững trong thời đại AI content.

**Success Metrics:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tool sessions/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lượt sử dụng per tool</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 100K/tool Đợt 1 trong 6 tháng live</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tool → CTA click rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% user click CTA sau khi nhận result</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 15%</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tool → Onelink (W2A proxy)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sessions từ tool có click Onelink</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Baseline Q3/2026</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Data points collected</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Anonymous interaction records</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 1M/tool/năm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI citation từ tool data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI engines cite MoMo data insights trong responses</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Measure Q4/2026</td>
    </tr>
  </tbody>
</table>

---

### 6.11. M10 - Experiment Engine

**Mục đích:** Infrastructure để PM/PO chạy AB test trên Web mà không cần Dev. Section 7.4 mandates AB Test Hypothesis trong mọi spec - M10 là infrastructure để mandate đó có nghĩa thực tế thay vì chỉ là formality.

**Trạng thái:** Planning. Prerequisite trước khi scale M1 (LP Builder) ra toàn GPD.

**Gap hiện tại:** MoSpark track events nhưng không có infrastructure để *serve variants*. Mọi claim "cải tiến" sau publish là opinion, không phải data.

**Capabilities:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Capability</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Variant assignment</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL-based (A/B routes riêng) hoặc component-based (in-page swap không reload)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Traffic split</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM set % phân chia, system assign ngẫu nhiên + consistent per session</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Statistical engine</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tính significance khi đủ sample size. Alert khi p < 0.05</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Auto-winner</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Winner xác định → notify PM → 1-click promote variant lên production</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Experiment log</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Full history: experiment ID, variants, duration, sample size, winner, uplift</td>
    </tr>
  </tbody>
</table>

**Integration:** Events từ experiment tự động gắn `experiment_id` + `variant` vào Umami. Success metric lấy từ downstream: Install, KYC, Transaction (Appsflyer pipeline).

**Success Metrics:**
- Experiments launched per quarter: 10+
- % LP mới có ít nhất 1 completed experiment trước khi scale: 80%+
- Winner detection time trung bình: < 21 ngày

---

### 6.12. M11 - Revenue Attribution Pipeline

**Mục đích:** Trace đầy đủ từ Web content/tool → Web-to-App → New User / MAU / Transaction. Business Owner mindset yêu cầu PM và Hiến biết ROI của từng Use Case - hiện tại không có cách đo end-to-end.

**Trạng thái:** Planning. Cần Umami + Appsflyer ổn định trước khi build unified layer.

**Pipeline 4 lớp:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Layer</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Track gì</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tool</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web behavior</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Session → Page → Content → Tool → CTA click</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Umami per URL group</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content attribution</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Onelink click → source URL → device</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer + Umami</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Channel attribution</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Install funnel</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Install → Register → KYC → Cashin</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer Track 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User funnel</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Revenue proxy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transaction type + frequency per cohort</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App event → BigQuery</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Revenue signal</td>
    </tr>
  </tbody>
</table>

**Unified View per Use Case:**
```
Use Case: Vay Nhanh [tháng X/2026]
├── Organic sessions: 120,000
├── Onelink clicks: 4,200 (3.5% CTR)
├── Installs: 1,260 (30% click → install)
├── KYC completed: 630 (50% install → KYC)
├── First loan: 189 (30% KYC → transaction)
└── CAC proxy: [total web cost / New User attributed]
```

**Success Metrics:**
- Full attribution pipeline live cho top 5 Use Cases: Q3/2026
- % Use Cases có ROI dashboard đủ để justify continued investment: 100% Q4/2026
- CAC per Use Case tracked và có trend line improving QoQ

---

### 6.13. M12 - Content Intelligence Loop

**Mục đích:** Phát hiện content decay trước khi thành zero-traffic URL. Surface keyword opportunities chưa được cover. Đóng feedback loop giữa publish và optimize - thứ hiện tại bị đứt hoàn toàn sau bước publish.

**Trạng thái:** Planning. Phase 2. Context: 3,670 zero-traffic URLs hiện tại là hậu quả trực tiếp của việc thiếu module này.

**12a. Content Decay Detection:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Signal</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Threshold</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic giảm > 20% trong 4 tuần liên tiếp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Warning</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Alert Hiến + Media Team</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic giảm > 50% trong 8 tuần</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Critical</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Enhancement queue - draft re-write</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Zero traffic > 90 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Zero-traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL audit: 410 Gone / Redirect / Rewrite decision</td>
    </tr>
  </tbody>
</table>

GSC integration: weekly pull impression + click per URL. Dashboard severity: Warning / Critical / Zero count by Use Case và Pillar.

**12b. Keyword Opportunity Surfacing:**
- **Near miss list:** GSC queries MoMo rank position 4-15 × volume > 1K/tháng → sorted by (Volume × Position Gap). Brief content update được auto-generate.
- **White space:** keyword cluster có volume nhưng 0 URL của MoMo → new content brief tự động đưa vào GenAI queue.
- **Cluster gap:** so sánh keyword coverage hiện có với SEO Inventory target per Use Case.

**Success Metrics:**
- Zero-traffic URL mới sau khi M12 live: 0/tháng
- Near miss keywords promoted lên top 3 per quarter: 20+
- Decay detection coverage: 100% URLs đang live được monitor weekly

---

### 6.14. M13 - GEO Citation Monitor

**Mục đích:** Đo North Star GEO: MoMo được cite trong top 3 AI engine responses cho 20 target PFM queries. Hiện không có cách đo tự động - đây là blocker để biết GEO strategy có work không và llms.txt có effect gì.

**Trạng thái:** Planning. Build song song với M6 (llms.txt rollout).

**Monitoring Setup:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">AI Engine</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Method</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ChatGPT (GPT-4o)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">OpenAI API query + parse response</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Weekly</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Perplexity</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Perplexity API query + source detection</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Weekly</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google AI Overview</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC AI referral data + manual sampling</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Weekly</td>
    </tr>
  </tbody>
</table>

**Query Library - 20 Seed Queries × 4 Pillars:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pillar</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ seed queries</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P1 - Tài chính</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vay tiền online uy tín VN", "check điểm tín dụng miễn phí", "ví điện tử có BNPL VN"</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P2 - Bảo hiểm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"bảo hiểm xe máy bắt buộc là gì", "so sánh gói bảo hiểm sức khỏe VN"</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P3 - Tiện ích</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"tra cứu phạt nguội online", "kiểm tra BHXH còn bao nhiêu tháng"</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P4 - Đời sống</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"thanh toán vé CGV bằng ví điện tử", "mua esim du lịch Thái Lan giá rẻ"</td>
    </tr>
  </tbody>
</table>

**Dashboard Metrics:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hiện tại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target Year 1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Citation Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% queries MoMo xuất hiện trong response</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">30%+ (bắt đầu từ P3)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Citation Position</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thứ tự xuất hiện trong response</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top 3</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Citation Accuracy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Claim MoMo được cite có đúng không</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100% accurate</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Weekly trend</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Change after llms.txt events</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Positive correlation</td>
    </tr>
  </tbody>
</table>

**Trigger:** Citation Rate giảm đột ngột → check llms.txt status + content freshness + competitor action.

**Success Metrics:**
- 20 target queries tracked weekly: Q3/2026
- Citation Rate > 30% cho P3 queries (data-rich, easiest entry point): Q4/2026
- Citation Rate > 20% across all 4 Pillars: End 2027

---

### 6.15. M14 - HRM API Sync (LnD Integration)

**Mục đích:** Xây dựng nền tảng định danh và phân quyền tự động cho MoSpark thông qua việc đồng bộ với hệ thống quản trị nhân sự (HRM). Mở rộng quản lý User khi hệ thống scale-up.

**Bối cảnh:** MoMo đang triển khai dự án LnD (Product Led Growth) do các Head of BU/VP chia sẻ khóa học (Text/Doc) trên `product.momo.vn`. Dự án này làm việc mật thiết với HR. Ý tưởng của anh Bảo là tận dụng việc này để MoSpark đồng bộ API trực tiếp với HRM.

**Dữ liệu đồng bộ (từ HRM về MoSpark):**
- Email
- Tên nhân viên
- Phòng ban (Department / Division)
- Cấp bậc (Level)
- Thời gian gia nhập (Onboarding Time)

**Giá trị mang lại:**
- **Automated RBAC:** Tự động map user vào đúng phân quyền Role và Use Case (Cell Team) trên MoSpark dựa vào phòng ban và level, không cần tạo tài khoản thủ công.
- **Scale-up Ready:** Sẵn sàng cho việc mở rộng số lượng User quản trị trên MoSpark khi GTM toàn bộ các Division.

---

### 6.16. M15 - 2H Customer Knowledge Base

**Mục đích:** Làm dồi dào Knowledge Base của MoMo trên MoSpark bằng nguồn dữ liệu định tính cực kỳ quý giá từ người dùng thực tế (Customer Insight).

**Bối cảnh:** Dự án "2H Customer" - MoMo thuê công ty Research tìm kiếm người dùng. Các cấp Manager+ đi survey khách hàng, lắng nghe, ghi âm, take note, và viết Meeting Minutes Note trên web 2H Customer. Anh Bảo có định hướng muốn thu thập toàn bộ Meeting Notes này.

**Giải pháp:**
- Thu thập và lưu trữ Meeting Notes dưới định dạng **Markdown**.
- Markdown là format tối ưu để LLMs (AI) có thể đọc hiểu và vector hóa.
- Biến các notes này thành toàn bộ Context / JTBD (Jobs To Be Done) của người dùng thực/tiềm năng (tại sao họ dùng hoặc không dùng MoMo).
- **Ứng dụng:** Trở thành nền tảng cơ sở (Foundational Base) cực kỳ vững chắc cho RAG/GenAI Workflow (M2) của MoSpark, giúp AI viết nội dung sát với insight người dùng thực tế hơn.

---

## 7. North Star & KPIs

### 7.1. North Star Metrics

MoSpark đóng góp vào 2 NSM của MoMo Web:

**New User Acquisition:**
```
Organic Traffic → Content/Tool → Ads Manager → Onelink → Install → Register → New User
```

**MAU Uplift:**
```
User trên Web → Ads (reactivation) → App Open → MAU
```

**GEO North Star (12 tháng):**
```
MoMo được cite trong top 3 AI engine responses cho 20 target PFM queries.
Engines: Google AI Overview, ChatGPT, Perplexity.
Current: Tỉ lệ trích dẫn tổng thể còn thấp (từng ghi nhận 0% AI Chatbot referral vs Wise.com 40%+; hiện bắt đầu có tín hiệu từ pilot Phạt Nguội).
```

### 7.2. Platform KPIs

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KPI</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target 2026</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sessions từ Organic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng trưởng YoY per Use Case</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SoV per Use Case</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Impression (GSC) / Total Volume Search</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + SEO Inventory</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 40% cho top 3 Use Case</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A Conversion Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click Onelink / Web Sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer + Umami</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Baseline → +2% per campaign</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Citation Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo được cite trong AI engine responses</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Manual test + GA4 AI referral</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">30% cho Primary Keywords</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Quality Score</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% bài đạt ≥ 80 SEO/GEO Score</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoSpark internal</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100% bài mới ≥ 80</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM/PO Self-Service Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% LP/Campaign do PM/PO tự tạo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoSpark logs</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">80%+</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Time-to-Publish</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Từ brief đến live</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoSpark logs</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LP < 1 ngày, Blog < 3 ngày</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Zero Hardcode Violation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Campaign bypass Ads Manager</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Platform audit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0 violations</td>
    </tr>
  </tbody>
</table>

### 7.3. OKR Alignment 2026

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">OKR</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoSpark đóng góp gì</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">O1: New User Growth via Organic & W2A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M2 (GenAI Content) + M3 (Ads Manager) → tăng organic traffic và W2A CR</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">O2: Platform Stability & Technical Readiness</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M4 (Scoring Gate) + M6 (AI Crawler Policy) → không có bad pages live</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">O3: PLG/Utilities-Led SEO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M3 (Widget Library) + M2 (Tool content) → CIC checker, Loan calculator, Insurance tool</td>
    </tr>
  </tbody>
</table>

### 7.4. Measurement-First - Bắt buộc với mọi Spec

"Tốc độ ship mà không có AB test thì không thể cải tiến." MoSpark không chỉ là nơi tạo trang - là nơi học hỏi và cải tiến liên tục. Mọi spec/BRD gửi cho Web Platform phải có 2 field bắt buộc trước khi bắt đầu build:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Field</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Yêu cầu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">PIC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tracking Event Schema</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">List event cần track: event name, properties, trigger condition. Không skip với lý do "sẽ làm sau"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến define standard, DA execute</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>AB Test Hypothesis</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Variant A (baseline) vs Variant B (thay đổi) + success metric cụ thể. Không phải "test xem sao"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM/PO của Use Case đó</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Success Metric trace về NSM</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Metric chính phải trace về New User / MAU / W2A CR - không chỉ pageview hay session</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến sign-off</td>
    </tr>
  </tbody>
</table>

Thiếu Tracking Event Schema hoặc AB Test Hypothesis - spec chưa complete, Web Platform không bắt đầu build.

---

## 8. Data Governance

### 8.1. Use Case là đơn vị gốc

Mọi entity trên MoSpark đều gắn vào `use_case_id`. Đây là sợi chỉ kết nối tất cả modules:

```
Use Case: Phạt Nguội
    ├── SEO Inventory: market_volume, momo_sov
    ├── Business Context: 12 fields, PM xác nhận
    ├── Keyword Registry: primary_keywords (unique)
    ├── Blog Content: /phat-nguoi/blog/*
    ├── Mini Web: /phat-nguoi
    ├── Ads Placements: Balloon + Widget
    └── Analytics: Umami URL group + GA4 segment
```

### 8.2. Chống Cannibalization - 3 lớp bảo vệ

- **Lớp 1 - SEO Inventory:** `primary_keyword` là UNIQUE trong database. Không cho 2 Use Case dùng cùng keyword.
- **Lớp 2 - GenAI Content:** Unique ID Check tại Keyword Master Registry trước mọi luồng sản xuất.
- **Lớp 3 - Blog Editor:** Bottom-Up Sync: khi Editor nhập Primary Keyword, tự check với Registry.

### 8.3. Quality Gate tổng hợp

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Gate</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điều kiện pass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Business Context Complete</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đủ 12 fields, PM xác nhận pháp lý - không thể proceed nếu thiếu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Outline Approval</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM approve outline trước khi AI viết bài</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO/GEO Score ≥ 60</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có Hard Block - Publish bị disable nếu fail</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CWV Pass</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 - Hard Block</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA Present</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Field CTA không rỗng - Hard Block</td>
    </tr>
  </tbody>
</table>

---

## 9. Roadmap 2026

### Phase 1: Foundation & Scale (Q2/2026 - Đang làm)

**Mục tiêu:** Stabilize production pipeline + chứng minh W2A conversion với Phạt Nguội pilot.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Deliverable</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LP Builder - GPD Onboarding</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">In Progress</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content: Scale Financial (Vay, VTS, CIC)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trọng + Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">In Progress</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads Manager Widget: Phạt Nguội + BHYT Shortcode</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">In Progress</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Umami Live - Phạt Nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">This week</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO Inventory Dashboard v1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận (schema) + Hiến (data)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">robots.txt Layer 2+3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến (spec) + Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
    </tr>
  </tbody>
</table>

### Phase 2: Optimization Loops (Q3-Q4/2026)

**Mục tiêu:** Đóng vòng lặp tối ưu - từ publish đến measure đến improve.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Deliverable</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timeline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads Manager Phase 2: Placement Registry + Conflict Resolution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Multi-Division song song</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Auto-Refresh: Phát hiện Content Decay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Enhance tự động</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO SoV Dashboard: AI citation tracking per Use Case</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Visibility vào AI Search</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads Manager Phase 3: Retargeting + Multi-tenant</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q4/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM self-service hoàn chỉnh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">llms.txt: Master index + per-product full doc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO first-mover</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Interactive Blocks: Calculator, Simulator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q4/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PLG/Utilities SEO, anti-LLM moat</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Health Alert: 404 + Traffic anomaly detection</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q4/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Zero zero-traffic URL mới</td>
    </tr>
  </tbody>
</table>

### Phase 3: Agentic Growth (2027+)

**Mục tiêu:** AI chủ động vận hành vòng lặp tăng trưởng, ít can thiệp thủ công.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Capability</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">White Space Discovery</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI phát hiện ngách thị trường chưa có đối thủ, đề xuất Use Case mới.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Autonomous Campaign</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI lên plan, tạo content, setup Ads, monitor và optimize.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Personalized LP</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nội dung thay đổi theo hành vi và nguồn traffic từng user.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Agentic Help Center</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Agent thay FAQ tĩnh, xử lý real-time support.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Semantic Linking Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vector embeddings tự gợi ý và chèn internal link tối ưu.</td>
    </tr>
  </tbody>
</table>

---

## 10. Rủi ro & Giảm thiểu

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Impact</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cách xử lý</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM publish message sai trên trang tài chính YMYL</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Business Context 12 fields + Legal Workflow + Web Product Lead sign-off</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuận overload khi deliver nhiều modules song song</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Scope nhỏ theo Phase, gate rõ trước khi move module tiếp</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Division bypass Ads Manager - nhờ Dev hardcode</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"No hardcode" policy do Bảo enforce + training PM/PO trước khi access</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads conflict giữa Division gây spam UX</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Conflict Detection tự động (Phase 2) + Platform Admin resolve trước live</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ads ảnh hưởng SEO - bounce rate tăng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến monitor SEO signals; guardrail cứng (1 Popup/session)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migration gây traffic drop</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp (Zero Redirect)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Monitor 2 tuần post-migration, rollback plan per phase</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Citation Rate không cải thiện sau llms.txt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Treat như infrastructure; review sau 6 tháng với 3 signals</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cannibalization vẫn xảy ra qua edge cases</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triple-layer prevention (Inventory + GenAI Registry + Blog Editor sync)</td>
    </tr>
  </tbody>
</table>

---

## 11. RACI & Collaboration

### 11.1. Phân vai

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trách nhiệm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Không làm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Văn Hiến (Web Product Lead)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Set SEO/GEO standard, govern Quality Gate, input Market data, sign-off YMYL, audit AI Citation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không execute tracking, không direct với Dev mà không có spec</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo (Web Platform Manager)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product direction MoSpark, Placement Registry, enforce "no hardcode", PO Web Platform sprint</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không làm trực tiếp với Agency hay Media Team</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thuận + Lộc (Developers)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Build tất cả modules theo spec, Widget Library, database</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không tham gia campaign creation khi đã có self-service</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trọng (Developer)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content Engine - AI Tool, Model, Workflow (lõi engine). Thuận lo GenAI Hình (Gallery), Lộc lo phân quyền User</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không build các module khác của MoSpark</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Media Team (BMC)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content production theo brief Hiến, điền Business Context cùng PM, off-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không làm trực tiếp với Web Platform - technical request qua Hiến</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PM/PO Cell Team</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo Use Case, xác nhận Business Context (chịu trách nhiệm pháp lý), approve Outline, tự tạo LP + Ads</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không chỉnh code hoặc nhờ Dev bypass MoSpark</td>
    </tr>
  </tbody>
</table>

### 11.2. Escalation Path

Platform issues → Bảo → Hiến review (nếu SEO impact).
Content quality → Hiến → Media Team (nếu Media Team cần training).
Resource/Policy → Hiến → Bảo → Công (VP).

---

## 13. Version Log

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phiên bản</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v2.6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo cấu trúc Growth OS.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v2.7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-16</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bổ sung GSC Loop & Semantic Linking.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v2.8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-16</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tái cấu trúc footer + version log.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v3.0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tái viết thành Product Vision + PRD đầy đủ. Tổng hợp 8 module.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v3.1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Viết lại ngôn ngữ cho rõ hơn, bỏ văn phong hàn lâm. Bổ sung Bối cảnh Chiến lược từ meetings (Anh Công, Huy Lê, A.Tường).</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v3.2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Redesign Section 2: xóa meeting-transcript style, thay bằng Mandate Chiến lược (2.1) + 4 Growth Pillars (2.2) + đổi tên 2.2 cũ thành 2.3. Bổ sung Elegant Problem Statement (Section 1.1), MoSpark KHÔNG phải (Section 3.4), Measurement-First bắt buộc (Section 7.4).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v3.3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bổ sung 5 modules mới M9-M13: PLG Tool Builder (full spec với 4-test framework + 3 tool types + data pipeline), Experiment Engine, Revenue Attribution Pipeline, Content Intelligence Loop, GEO Citation Monitor. Update kiến trúc platform lên 5 lớp. Update Module Catalog table. Thêm 3 Mermaid diagrams cho M9: 4-Test Decision Framework, Tool Types + Pillar Mapping, Data Pipeline → GEO Moat.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v3.4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-05-31</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Consistency fix</strong>: (1) M2 GenAI ownership sửa thành Trọng (AI Tool/Model/Workflow) + Thuận (GenAI Hình) + Lộc (phân quyền User) + Hiến (govern), bổ sung Trọng vào RACI 11.1; (2) Pillar P4 (2.2) bỏ 410 Gone thay Noindex (hạ tầng không hỗ trợ); (3) Escalation path 11.2 sửa Tuệ → Bảo (Tuệ nghỉ cuối T5/2026).</td>
    </tr>
  </tbody>
</table>

---

*Owner: Văn Hiến (Web Product Lead) | Version: v3.4 | Updated: 2026-05-31*

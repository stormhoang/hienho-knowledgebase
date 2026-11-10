# PRODUCT REQUIREMENT DOCUMENT (PRD) - SYSTEM ARCHITECTURE

*Tài liệu Đặc tả Chiến lược Định danh Người dùng & Kiến trúc Hệ thống Quản trị Cửa hàng (User Authentication Strategy & Merchant Portal Architecture PRD)*

## 📋 THÔNG TIN CHUNG (Metadata)
> *   **Tên dự án / Sản phẩm (PRODUCT NAME):** Web User Authentication Strategy & Merchant Portal Architecture
> *   **Đầu mối Cell Team (PO & Tech Lead):** GPD - Web Platform
> *   **Web Product Lead (Duyệt dự án):** Hien.ho
> *   **Trạng thái tài liệu (Document status):** DRAFT
> *   **Tiến độ dự kiến:** Q3/2026 (Kick-off) ➔ Q3/2026 (Pilot) ➔ Q4/2026 (Go-Live)
> *   **Loại yêu cầu:** [x] Tính năng mới | [ ] Cải tiến/Thay đổi cấu trúc

---

## I. TÀI LIỆU LIÊN QUAN (References)
*   **Đặc tả định danh Web-to-App:** [mospark_user_identity_tracking.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/mospark_user_identity_tracking.md)
*   **PRD Trang Đối Tác (SME detail page):** [doi-tac-prd.md](doi-tac-prd.md)
*   **BRD Merchant Page (MMP):** [doi-tac-brd.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/doi-tac-brd.md)
*   **PRD Web Identity Mapping (Use Cases):** [web-identity-mapping-prd.md](web-identity-mapping-prd.md)

---

## II. CHIẾN LƯỢC ĐỊNH DANH NGƯỜI DÙNG (User Authentication Strategy)

### 1. Nguyên tắc cốt lõi (Core Principles)
*   **Định danh thực thể vật lý thật:** Hệ thống hướng tới xác thực các thực thể vật lý có thật ngoài đời (người dùng thật, nhu cầu thật), tuyệt đối không chạy theo số lượng tài khoản ảo hoặc ảo hóa dữ liệu.
*   **Kiểm soát rủi ro H2 2026 (H2 Risk Control):**
    *   MoMo **chưa áp dụng các chương trình tặng thưởng/khuyến mại lớn** trên kênh Web nhằm triệt tiêu động cơ của các đối tượng gian lận (fraud/cheat) tấn công hệ thống.
    *   Phạm vi định danh trên Web trong giai đoạn H2 chỉ dừng lại ở mức độ: **Thu thập thông tin hành vi** và cho phép **tương tác đóng góp nội dung** (User Generated Content - UGC) của người dùng đã xác thực.
    *   Mọi hoạt động thanh toán (payment), đối soát tài chính hoặc áp dụng khuyến mãi nhạy cảm **bắt buộc phải thực hiện bên trong App MoMo** để đảm bảo an toàn tuyệt đối.

### 2. Ba cấp độ xác thực đề xuất (Three Levels of Authentication)

```
+----------------------------------------------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cấp độ 3: MoMo App Auth (Xác thực tài khoản MoMo in-app qua QR/OTP/wui)</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
+----------------------------------------------------------------------------+
                                      ▲
+----------------------------------------------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cấp độ 2: Online Verification (Xác thực Số điện thoại/Zalo hoặc Social)</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
+----------------------------------------------------------------------------+
                                      ▲
+----------------------------------------------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cấp độ 1: Basic Info (Thu thập Name, YOB, Address theo nhu cầu dự án)</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
+----------------------------------------------------------------------------+
```

*   **Cấp độ 1: Basic Info (Thông tin cơ bản):**
    *   Thu thập các thông tin nền tảng tối giản: Tên, Năm sinh (YOB), Địa chỉ, phân vùng khu vực.
    *   Áp dụng cho các tính năng không nhạy cảm (ví dụ: cá nhân hóa widget thời tiết, giá xăng dầu, hoặc lưu lịch sử tra cứu biển số xe ẩn danh).
*   **Cấp độ 2: Online Verification (Xác thực trực tuyến):**
    *   Xác thực qua tài khoản Mạng xã hội (Facebook/Google) hoặc số điện thoại (OTP SMS / Zalo ZNS).
    *   *Chính sách ưu tiên SME:* Đối với tệp khách hàng hộ kinh doanh (SME), **Số điện thoại và Zalo được ưu tiên hoàn toàn so với Email**. Khảo sát thực tế cho thấy tới 95% nhóm tiểu thương không nhớ mật khẩu email hoặc không có thói quen chủ động kiểm tra hòm thư email cá nhân hàng ngày.
*   **Cấp độ 3: MoMo App Authentication (Xác thực liên kết ứng dụng MoMo):**
    *   Liên kết trực tiếp với tài khoản MoMo đang hoạt động của người dùng.
    *   *Cơ chế công nghệ mới:* Tích hợp token bảo mật dùng một lần (Secure Web Token) sinh ra khi quét mã QR đăng nhập trên Web, hoặc tự động stitch thông tin thông qua tham số `wui` (Website User ID) truyền từ Appsflyer OneLink khi người dùng nhảy từ App ra Web hoặc ngược lại.

---

## III. CASE STUDY TRIỂN KHAI THỰC TẾ: MERCHANT PAGE & SOUNDBOX

### 1. Mô hình hoạt động (Operating Model)
*   Đội ngũ Salesman đi thị trường bán thiết bị loa thanh toán (Loa MoMo/Soundbox) cho các hộ kinh doanh vừa và nhỏ (SME Merchant).
*   Mỗi Merchant khi mua loa sẽ được cấp một trang web riêng gọi là **Merchant Page** trên hệ thống `momo.vn/merchant/{slug}`. Trang web này đóng vai trò như một trang thông tin cửa hàng tích hợp (tương tự Google Business Profile) giúp họ hiển thị trực tuyến, tiếp cận khách hàng xung quanh và tối ưu hóa SEO địa phương.

### 2. Quy trình kích hoạt và Quản lý thông tin (Activation & Management Flow)
*   **Tạo trang Preview trong 10 phút:** Dựa trên thông tin cơ bản (địa chỉ, tên cửa hàng) mà Merchant cung cấp cho Salesman tại thời điểm mua loa, hệ thống sẽ tự động khởi tạo một trang Merchant Page dưới dạng xem trước (Preview) chỉ trong vòng 10 phút thông qua pipeline GenAI.
*   **Quản lý trên di động:** Merchant đăng nhập bằng số điện thoại của mình (OTP Zalo/SMS) để quản lý trang cửa hàng trực tiếp trên thiết bị di động (giao diện Mobile Web/PWA). Merchant có quyền đề xuất chỉnh sửa: Tên cửa hàng, Logo, Địa chỉ, Menu món ăn, hoặc cập nhật Giá cả dịch vụ.
*   **Cơ chế kiểm soát dữ liệu (Approval Flow):**
    *   Để tránh rủi ro Merchant nhập sai chính tả, đưa thông tin sai lệch hoặc hình ảnh không phù hợp lên trang public, Merchant **không có quyền chỉnh sửa trực tiếp vào cơ sở dữ liệu công cộng (public database)**.
    *   Mọi yêu cầu chỉnh sửa của Merchant được lưu dưới dạng một **ghi chú đề xuất (Proposal Note)** ở một luồng dữ liệu độc lập (Draft State).
    *   Nhân viên nội bộ MoMo (Staff / Sales phụ trách địa bàn) sẽ kiểm tra, phê duyệt các đề xuất này trong trang quản trị nội bộ thì thông tin mới chính thức được cập nhật lên trang công cộng của Merchant.

---

## IV. THIẾT KẾ KIẾN TRÚC HỆ THỐNG & PHÂN QUYỀN

Đội ngũ kỹ thuật thống nhất thiết kế một hệ thống quản trị độc lập, tách biệt rõ ràng hai luồng dữ liệu nội bộ (internal) và công cộng (public) để đảm bảo an toàn tuyệt đối.

```
                  +-------------------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">[ INTERNET ]</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                  +-------------------------------------------------+
                           │                               │
            (VPN & Smart Gate Auth)                 (Public Access)
                           │                               │
                           ▼                               ▼
               Tên miền: m.momo.vn               Tên miền: momo.vn
               [ STAFF / SALES PORTAL ]          [ MERCHANT BAY (MB) ]
               - Công nghệ: Refine B5            - Công nghệ: React / Next.js
               - Quyền: Duyệt & Can thiệp DB     - Quyền: Đề xuất chỉnh sửa (Draft)
                           │                               │
                           └───────────────┬───────────────┘
                                           │
                                           ▼
                                 [ API GATEWAY (Netcore) ]
                                 - Bảo vệ & Route traffic
                                           │
                                           ▼
                                  [ DATABASE LAYER ]
                                  - 1 Database (PostgreSQL)
                                  - 1 Supabase Instance
                                  - Bảo mật qua Role & RLS
```

### 1. Phân lập Nhóm Người dùng (User Segregation)

#### Nhóm Nhân viên nội bộ (Staff / Sales):
*   **Phương thức truy cập:** Bắt buộc phải thông qua mạng nội bộ công ty (VPN).
*   **Đăng nhập:** Sử dụng email công ty đuôi `@mservice.com.vn` và đăng nhập thông qua cổng xác thực bảo mật Smart/MoMo Gate.
*   **Tên miền quản trị:** Hệ thống cấp một tên miền riêng biệt là **`m.momo.vn`** (Merchant Administration Manager) phục vụ cho nhóm này.
*   **Quyền hạn:** Phân quyền mức cao (Admin/Moderator). Kiểm tra, duyệt hoặc từ chối các đề xuất chỉnh sửa từ Merchant. Có quyền can thiệp, cập nhật trực tiếp vào dữ liệu gốc (Public tables).

#### Nhóm Người dùng bên ngoài (Merchant / Social User / Student):
*   **Phương thức truy cập:** Truy cập qua môi trường mạng công cộng (Public Internet).
*   **Tên miền:** Sử dụng tên miền chính thống **`momo.vn/`** (ví dụ: `momo.vn/merchant/{slug}`).
*   **Đăng nhập:** Đăng nhập bằng Số điện thoại (ưu tiên) hoặc tài khoản Mạng xã hội.
*   **Quyền hạn:** Chỉ có quyền đề xuất dữ liệu (Draft suggestions). Không có quyền ghi trực tiếp vào bảng dữ liệu public của cơ sở dữ liệu.

### 2. Kiến trúc Công nghệ (Tech Stack)
*   **Frontend:** React, TypeScript (TS).
*   **Admin Framework:** **Refine B5** (React-based admin framework tích hợp Bootstrap 5) được chọn để xây dựng giao diện CMS Admin nhanh chóng cho Staff trên tên miền `m.momo.vn`.
*   **Backend & API Gateway:** Sử dụng **.NET Core (Netcore)** để làm tầng API Gateway/Proxy nhằm bảo vệ cơ sở dữ liệu Supabase, kiểm soát routing, giới hạn tần suất (rate-limit) và quản lý session token.
*   **Ứng dụng di động:** Định hướng phát triển theo mô hình **PWA (Progressive Web App)** giúp các Merchant dễ dàng cài đặt trang quản trị cửa hàng trực tiếp lên màn hình điện thoại di động mà không cần tải từ App Store/Google Play.
*   **Cơ sở dữ liệu (Database Layer):**
    *   Thống nhất sử dụng mô hình **1 Database - 1 Supabase** để quản lý đồng thời cả vai trò của trang quản trị nội bộ (MAM) lẫn trang hiển thị cửa hàng công cộng (Merchant Bay).
    *   Việc cách ly và phân quyền dữ liệu được thực thi nghiêm ngặt thông qua cơ chế **Phân quyền vai trò Database (Roles)** kết hợp chính sách bảo mật dòng **Row Level Security (RLS)** trên PostgreSQL, tránh việc chia tách thành nhiều database vật lý gây phức tạp trong vận hành.

---

## V. DATABASE SCHEMA & ROW LEVEL SECURITY (RLS) DESIGN

### 1. Database Schema
Để hỗ trợ luồng duyệt đề xuất (Approval Flow) và phân lập dữ liệu, cơ sở dữ liệu Supabase sử dụng 2 bảng chính:

```sql
-- 1. Bảng dữ liệu cửa hàng chính thức (Public Data)
CREATE TABLE merchants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug VARCHAR(256) UNIQUE NOT NULL,
    shop_name VARCHAR(256) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(32) NOT NULL,
    logo_url TEXT,
    menu JSONB,                  -- Lưu trữ menu món ăn và giá cả
    status VARCHAR(32) DEFAULT 'PREVIEW', -- PREVIEW, PUBLISHED, SUSPENDED
    owner_phone VARCHAR(32),     -- SĐT của Merchant sở hữu
    created_by VARCHAR(128),     -- Email của Salesman tạo trang
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. Bảng lưu trữ đề xuất chỉnh sửa của Merchant (Draft/Notes Flow)
CREATE TABLE merchant_proposals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    merchant_id UUID REFERENCES merchants(id) ON DELETE CASCADE,
    proposed_changes JSONB NOT NULL, -- Chứa các trường muốn thay đổi (e.g. {shop_name: "Tên mới"})
    status VARCHAR(32) DEFAULT 'PENDING', -- PENDING, APPROVED, REJECTED
    notes TEXT,                      -- Ghi chú của Merchant hoặc phản hồi của Staff
    reviewed_by VARCHAR(128),    -- Email của Staff phê duyệt
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### 2. Cấu hình Row Level Security (RLS) trên Supabase
Supabase thực thi bảo mật dữ liệu dựa trên JWT Token được gửi từ Netcore API Gateway. Dưới đây là các chính sách RLS mẫu để phân quyền giữa Staff và Merchant:

```sql
-- Bật RLS cho các bảng
ALTER TABLE merchants ENABLE ROW LEVEL SECURITY;
ALTER TABLE merchant_proposals ENABLE ROW LEVEL SECURITY;

-- Tạo Roles trong Database
-- Role 1: 'staff' (Nhân viên truy cập qua m.momo.vn)
-- Role 2: 'merchant_user' (Merchant đăng nhập qua OTP Số điện thoại trên momo.vn)

-- CHÍNH SÁCH CHO BẢNG MERCHANTS:
-- 1. Staff có quyền xem và sửa đổi toàn bộ thông tin merchants
CREATE POLICY staff_all_merchants ON merchants
    FOR ALL
    TO staff
    USING (true)
    WITH CHECK (true);

-- 2. Merchant chỉ có quyền XEM thông tin cửa hàng của chính mình (qua SĐT đã xác thực)
CREATE POLICY merchant_view_own ON merchants
    FOR SELECT
    TO merchant_user
    USING (owner_phone = auth.jwt()  ➔ > 'phone_number');

-- CHÍNH SÁCH CHO BẢNG MERCHANT_PROPOSALS (LUỒNG ĐỀ XUẤT):
-- 1. Staff có quyền xem và cập nhật trạng thái duyệt đề xuất
CREATE POLICY staff_manage_proposals ON merchant_proposals
    FOR ALL
    TO staff
    USING (true)
    WITH CHECK (true);

-- 2. Merchant chỉ có quyền TẠO và XEM các đề xuất của chính mình
CREATE POLICY merchant_create_own_proposal ON merchant_proposals
    FOR INSERT
    TO merchant_user
    WITH CHECK (
        EXISTS (
            SELECT 1 FROM merchants
            WHERE merchants.id = merchant_id
            AND merchants.owner_phone = auth.jwt()  ➔ > 'phone_number'
        )
    );

CREATE POLICY merchant_view_own_proposal ON merchant_proposals
    FOR SELECT
    TO merchant_user
    USING (
        EXISTS (
            SELECT 1 FROM merchants
            WHERE merchants.id = merchant_id
            AND merchants.owner_phone = auth.jwt()  ➔ > 'phone_number'
        )
    );
```

---

## VI. BẢO MẬT & VẬN HÀNH (Security & Operations)

### 1. Kiểm soát Truy cập VPN & Smart Gate
*   **MAM (`m.momo.vn`):** DNS của tên miền `m.momo.vn` cấu hình riêng ở mức DNS nội bộ hoặc phân giải IP chỉ chấp nhận dải IP của VPN công ty.
*   **Smart Gate Authentication:** Tầng API Gateway Netcore chặn toàn bộ request vào `m.momo.vn` nếu không có JWT Token hợp lệ sinh ra từ cổng Smart Gate xác thực email `@mservice.com.vn`.

### 2. Ngăn ngừa Lọt dữ liệu và Chống Spam
*   **Merchant Pages (`momo.vn/`):** Không expose bất kỳ API Supabase trực tiếp nào ra môi trường client public. Toàn bộ request đi qua YARP Proxy (Netcore) để filter dữ liệu nhạy cảm (như `owner_phone`, `created_by` không bao giờ được trả về Client).
*   **Rate Limiting:** Tầng API Gateway áp dụng limit tối đa 10 đề xuất chỉnh sửa/merchant/ngày để chống spam spamming DB.

---

## LỊCH SỬ THAY ĐỔI (Changelog)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phiên bản</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày cập nhật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Người thực hiện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung thay đổi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-07-20</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Agent</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo tài liệu đặc tả chiến lược định danh và kiến trúc hệ thống quản trị cửa hàng (MAM vs MB).</td>
    </tr>
  </tbody>
</table>

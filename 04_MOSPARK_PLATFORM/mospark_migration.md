# MoSpark - Migration
ark Migration - System Consolidation

> - **Project Manager:** Anh Bảo (Web Platform Manager)
> - **Governance & SEO Strategy:** Văn Hiến (Web Product Lead)
> - **System Architect / Migration Mapper:**  [Cần xác định] Người chịu trách nhiệm định nghĩa cấu trúc dữ liệu, sơ đồ chuyển dịch và liên kết hệ thống.
> - **Lead Engineers:** Võ Minh Thuận, Lê Đăng Lộc
> - **Status:** Active - Structure & Mapping Phase

---

## 1. Hệ thống hiện tại: Admin Panel Tool (CMS)
Đây là hệ thống CMS trung tâm phục vụ quản lý và vận hành toàn bộ nội dung và tính năng Mini Web, Landing Page, Blog, News, FAQ, Guide trên Web MoMo hiện nay.
*   **Vai trò**: Nền tảng cốt lõi để các Division/Center quản trị nội dung độc lập.
*   **Các Module đang vận hành**:
    *   **CMS**: Quản lý và xuất bản Mini Web & Landing Page.
    *   **Ads Manager**: Quản lý và phân phối Ads Campaign.
    *   **FlexData Management**: Quản lý dữ liệu động cho các Mini Web.
    *   **Multilingual**: Hỗ trợ đa ngôn ngữ.

## 2. Nền tảng chiến lược: MoSpark (AI-powered Platform)
MoSpark không phải là một hệ thống build mới hoàn toàn mà là **bản nâng cấp thế hệ mới** của Admin Panel Tool với tech stack tương thích AI-powered tốt hơn.
*   **Triết lý**: Giữ lại những gì đang hoạt động tốt (Continuity), đồng thời mở ra khả năng mới về AI.
*   **Thành tựu bước đầu**: Module **Landing Page Builder** đã chứng minh tính đúng đắn, giúp PM/PO có thể tự thao tác trực quan mà không phụ thuộc Dev/Media Team.
*   **Vision**: Trở thành nền tảng AI-powered Web App/Content của MoMo giúp vận hành và tăng trưởng mọi sản phẩm Web - từ Landing Page đến Mini Web, từ Content đến Web Application.

## 3. Nguyên nhân (Causes)
*   **Legacy Architecture**: Hệ thống cũ được xây dựng theo nhu cầu bộc phát của từng thời kỳ, dẫn đến việc "vá" thêm Admin Tool để phục vụ các sản phẩm phức tạp.
*   **Silo Mindset**: Việc chia Cell Team ban đầu nhằm mục đích phân quyền, nhưng lại vô tình tạo ra các "ốc đảo" dữ liệu và vận hành tách biệt.

## 4. Hậu quả (Consequences)

### 3.1. Bóc tách Vận hành (Operational Fragmentation)
*   **Điểm nghẽn của Media Team**: Đội ngũ Media Team (quản lý toàn bộ nội dung) phải thoát ra và đăng nhập vào từng Cell Team để đăng bài. Ví dụ: Để đăng 1 bài blog về Vay, họ không thể đăng từ giao diện chính mà phải vào Cell Team Vay.
*   **Inconsistency**: Giao diện, Menu Header/Footer và các thành phần UI có thể bị lệch nhau giữa các Cell Team do không có sự quản lý tập trung.

### 3.2. Bóc tách SEO & URL (URL Fragmentation)
*   **Cấu trúc chồng chéo**:
    *   Silo 1: `momo.vn/blog/*` (Hub content)
    *   Silo 2: `momo.vn/{use-case}/blog/*` (Vay, Cinema, Bảo hiểm...)
*   **Rủi ro SEO**: Keyword Cannibalization (các trang tự cạnh tranh lẫn nhau), phân tán sức mạnh domain (Link Equity) và gây khó khăn cho việc tối ưu Authority cho toàn site.
*   **Tracking**: Việc đo lường (GA4/Umami) bị phức tạp hóa do cấu trúc URL không thống nhất.

## 5. Phương hướng xử lý (Proposed Solutions)

### 5.1. Hợp nhất Nền tảng (Consolidation)
*   Chuyển toàn bộ dữ liệu từ CMS cũ và Admin Tool sang **MoSpark**.
*   **Single Interface**: Media Team chỉ cần một lối vào duy nhất để quản trị mọi nội dung.

### 5.2. Quản trị theo Use Case-based (Thay vì Cell Team)
*   Thay thế việc phân quyền theo "Cửa sổ Cell Team" bằng việc quản trị theo "Use Case".
*   Media Team có thể lọc nội dung theo Use Case ngay trên giao diện chính.

**Use Case System - Core Feature:**

MoSpark sử dụng **Use Case** như một cơ chế phân loại và phân phối nội dung đa năng. Mọi content (Blog, News, Landing Pages, Mini Web, Ads) đều được gán vào một Use Case để tự động hóa việc distribution và targeting.

**Lợi ích của Use Case System:**
1. **Content Distribution:** Tự động hiển thị Blog/News đúng Use Case trên Landing Page
2. **Ads Targeting:** Ads xuất hiện đúng segmentation dựa trên Use Case
3. **Unified Management:** Quản lý tất cả content của một Use Case từ 1 interface
4. **Cross-Content Linking:** Tự động gợi ý internal links cùng Use Case
5. **Analytics Segmentation:** Đo lường performance theo từng Use Case

### 5.3. Blog Module - 2 Tiers Architecture

**Giải pháp tối ưu: Giữ nguyên URL structure, unify management interface.**

#### Tier 1: Basic Blog (Default)
*   **Path:** `momo.vn/blog/*`
*   **Scope:** General content, News, Guides, FAQ (đa số blog content)
*   **Management:** Unified CRUD interface trên MoSpark
*   **Use Case:** `General` (mặc định)

#### Tier 2: Advanced Blog (Special Cases)
*   **Path:** `momo.vn/{use-case}/blog/*`
*   **Scope:** 4 Use Cases đặc biệt (Vay Nhanh, Cinema, BH Ô tô, BH Xe máy)
*   **Management:** Same CRUD interface + custom path configuration
*   **Use Cases:** `VayNhanh`, `Cinema`, `BaoHiemOTo`, `BaoHiemXeMay`

**Lý do không consolidate về `/blog/`:**
*   **Zero traffic loss:** Không redirect → Không lost traffic, không lost ranking
*   **SEO preservation:** Giữ nguyên URL authority đã build
*   **No cannibalization:** Mỗi Use Case có URL space riêng
*   **Future-proof:** Dễ thêm special case mới

**User Flow:**
1. Editor tạo Blog Post → Chọn Use Case
2. System auto-determine URL dựa trên config
3. Publish → Content được tạo đúng URL pattern

### 5.4. Migration Strategy - Zero Redirect Approach

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Case</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Current URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoSpark URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Migration Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">General</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Direct migration (no URL change)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay Nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/vay-nhanh/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/vay-nhanh/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Direct migration (no URL change)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cinema</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/cinema/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/cinema/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Direct migration (no URL change)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Ô tô</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-o-to/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-o-to/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Direct migration (no URL change)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Xe máy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-xe-may/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-xe-may/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Direct migration (no URL change)</td>
    </tr>
  </tbody>
</table>

**→ ZERO redirects needed!** Tất cả URLs được giữ nguyên.

---

## 6. Migration Mapping Framework (The "Structure" Layer)
Đây là tầng logic định nghĩa cách hệ thống được "xây lại" trên MoSpark. Người đảm nhiệm vai trò này phải trả lời 3 câu hỏi cốt lõi:

### 6.1. Move cái gì? (Inventory Audit)
*   **Content Assets**: Blog, News, Guide, FAQ, Landing Pages.
*   **Navigation Assets**: Menu Header/Footer theo từng Cell Team.
*   **Technical Assets**: Metadata, Schema, Redirect rules, Tracking codes.

### 6.2. Đặt ở đâu? (Mapping Schema)
**Blog Content - 2 Tiers:**
*   **Tier 1 - Basic Blog:** `momo.vn/blog/*` (General content, News, Guides, FAQ)
*   **Tier 2 - Advanced Blog:** `momo.vn/{use-case}/blog/*` (4 special cases: Vay Nhanh, Cinema, BH Ô tô, BH Xe máy)

**Product Content:**
*   Giữ nguyên cấu trúc `/vay-nhanh`, `/bao-hiem-xe-may`, `/cinema`, v.v.

**Documentation:**
*   Các trang hướng dẫn tập trung về `/guide/`

### 6.3. Liên kết đến cái gì? (Connectivity & Internal Link)
*   **Global Navigation:** Hợp nhất toàn bộ Menu Cell Team thành một **Master Menu** có khả năng thay đổi context theo Use Case.
*   **Contextual Linking:** Tự động gợi ý nội dung liên quan dựa trên Use Case (Ví dụ: Trang Vay Nhanh tự động link tới các Blog thuộc Use Case VayNhanh).
*   **Zero Redirect Strategy:** Không redirect vì URLs được giữ nguyên.

---

## 7. Migration Phases

### Phase 1: Foundation & Basic Blog (4-6 tuần)
**Mục tiêu:** Thiết lập infrastructure và migrate Basic Blog

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Task</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Setup MoSpark Blog Module (default path <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/blog</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo/Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog CRUD interface</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Implement Project Tag system</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo/Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tag-based filtering</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migrate <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/blog/*</code> content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến + Media Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">All general blog posts</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Validate: Traffic, ranking, indexation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO audit report</td>
    </tr>
  </tbody>
</table>

**Success Criteria:**
- 100% `/blog/*` content migrated
- Zero traffic drop
- All URLs indexed within 14 days

### Phase 2: Advanced Blog - Special Cases (6-8 tuần)
**Mục tiêu:** Migrate 4 Use Cases đặc biệt với custom paths

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Task</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Implement Blog Path Configuration</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo/Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin-configurable routing</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Add 4 special cases to config</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Config schema</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migrate <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/vay-nhanh/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến + Media Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay Nhanh blog posts</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migrate <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/cinema/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến + Media Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cinema blog posts</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migrate <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-o-to/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến + Media Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Ô tô blog posts</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Migrate <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-xe-may/blog/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến + Media Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Xe máy blog posts</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Validate: Traffic retention per Use Case</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO audit report</td>
    </tr>
  </tbody>
</table>

**Success Criteria:**
- 100% special case content migrated
- Zero traffic drop per Use Case
- All URLs retain ranking

### Phase 3: Optimization & Decommission (4 tuần)
**Mục tiêu:** Optimize cross-blog experience và deprecate hệ thống cũ

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Task</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cross-blog internal linking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo/Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Auto-suggest links</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Unified search across all blog paths</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo/Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Global search</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Analytics consolidation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DA (Hải)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Unified dashboard</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deprecate Admin Tool V1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Shutdown old system</td>
    </tr>
  </tbody>
</table>

**Success Criteria:**
- Single interface for all blog management
- 50% reduction in content production time
- Old system fully decommissioned

---

## 8. Success Metrics (Migration Phase)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timeline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Traffic Retention</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>98%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">30 days post-migration per phase</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Indexation Rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14 days post-migration</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ranking Stability</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Current positions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No drop >2 positions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Per Use Case</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Operational Speed</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">X hours/week</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0.5X hours/week</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60 days post-migration</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>SEO/GEO Score Compliance</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>80%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ongoing</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Zero Redirect Success</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100% URLs preserved</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">All phases</td>
    </tr>
  </tbody>
</table>

---
*Document: BRD-MoSpark-Migration-2026 · v1
---

---

## Change Log
- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.

## References & Alignment
- **Master Strategy:** [[mospark_master]]

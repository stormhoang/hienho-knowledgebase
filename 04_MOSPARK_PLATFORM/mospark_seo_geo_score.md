# MoSpark - SEO/GEO Scoring System
Hệ thống tự động kiểm duyệt & chấm điểm SEO/GEO chất lượng nội dung

> - **Dự án:** MoSpark Web Platform
> - **Khối phụ trách:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Trọng (Tech/API), Thuận (UI), Lộc (Access Control)
> - **Phiên bản:** 1.3.1 · June 2026

---

## 1. Executive Summary

### 1.1. Bối cảnh (Situation)
MoSpark cho phép Editor tự động hóa việc sinh nội dung qua GenAI và tạo trang nhanh chóng. Tuy nhiên, nếu thiếu đi một hệ thống kiểm duyệt chặt chẽ ngay tại điểm xuất bản (Publish Point), nền tảng rất dễ sản sinh ra rác dữ liệu, làm giảm điểm E-E-A-T và gây ảnh hưởng xấu tới toàn bộ domain `momo.vn`.

### 1.2. Vấn đề cốt lõi (Complication)
- **Thiếu Rào Cản Kỹ Thuật:** Lỗi On-page SEO, thiếu Schema hoặc Core Web Vitals (CWV) kém không được phát hiện kịp thời.
- **Rủi Ro YMYL:** MoMo là domain tài chính, Google áp chuẩn duyệt khắt khe. Bài viết thiếu Disclaimer hoặc cấu trúc lỏng lẻo sẽ bị phạt.
- **Tín Hiệu GEO Yếu:** Các AI Search Engines không tìm thấy đủ "Fact Density" hoặc Schema phù hợp để trích dẫn nội dung của MoMo.

### 1.3. Giải pháp (Resolution)
Tích hợp **SEO/GEO Checklist Scoring** trực tiếp vào **Section SEO** của MoSpark Admin để tự động chấm điểm và validate chất lượng mỗi page.
- Tạo một "trạm kiểm soát" (Governance Gate) với các điều kiện chặn cứng (Hard Block).
- Tính điểm tự động để phân loại (Pass/Warning/Blocked) trước khi bài viết được xuất bản ra ngoài.

---

## 2. Stakeholder (Nhóm người dùng chính)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trách nhiệm chính</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Content Editor</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Viết nội dung, nhập Metadata.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhập Primary Keyword, rà soát cảnh báo từ Score Panel và tối ưu bài viết đạt ngưỡng Pass.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Product Lead</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết kế bộ quy tắc Scoring.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Duy trì và nâng cấp các tiêu chuẩn SEO/GEO/CWV để phù hợp với thuật toán của Google/AI.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Developer (Tech Team)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cài đặt logic parse DOM & check API.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai các thuật toán auto-check và tích hợp Lighthouse API cho CWV.</td>
    </tr>
  </tbody>
</table>

---

## 3. Bài Toán Cần Giải & Success Metrics

### 3.1. Mục tiêu chiến lược (Objective & Scope)
- **Mục tiêu:** Tích hợp SEO/GEO Checklist Scoring trực tiếp vào Section SEO của MoSpark Admin để validate chất lượng của mỗi page trước khi Publish. Biến khu vực nhập dữ liệu SEO thành một "trạm kiểm soát" chất lượng, đảm bảo không có page nào được publish khi chưa đạt ngưỡng tối thiểu về Technical SEO, On-Page Content, và GEO readiness.
- **Áp dụng cho:** Tất cả page type trên MoSpark (Mini Web, Landing Page, Blog, Merchant Page).
- **Trigger:** Editor tạo page mới trên MoSpark, page ở trạng thái Draft, editor muốn Publish lần đầu.
- **Out of scope:** Post-publish monitoring, A/B test scoring, tracking parameter validation, xử lý noindex intentional.

### 3.2. Success Metrics (SMART)
- **Quality Assurance:** 100% trang mới trên MoSpark pass mức điểm tối thiểu 60/100 và không vi phạm lỗi Hard Block nào.
- **Performance:** 100% trang xuất bản vượt qua bài test LCP (≤ 2.5s) và CLS (≤ 0.1).
- **Automation:** Giảm 90% thời gian Review On-page của Web Product Lead do hệ thống đã tự động cảnh báo lỗi.

---

## 4. Workflow & User Flow

```mermaid
flowchart TD
    A([Bắt đầu: Keywords & Bài viết sync từ\nGenAI Content Engine]) --> B[Đẩy vào Blog/Merchant Editor\n(Trạng thái Draft)]
    B --> C{1. Kiểm tra\nĐiều kiện cứng}

    C -- "Thiếu Keyword / CWV / Hard Block" --> C1([CASE 1: CHẶN PUBLISH\n(Buộc Editor Review & Sửa)])

    C -- "Pass hết Điều kiện cứng" --> D[2. Tính điểm SEO/GEO]

    D --> E{3. Phân loại điểm?}

    E -- "Score < 60" --> C1

    E -- "Score 60 - 79" --> D1([CASE 2: CHO PHÉP PUBLISH\nTrạng thái: Cần tối ưu])

    E -- "Score ≥ 80" --> D2([CASE 3: CHO PHÉP PUBLISH\nTrạng thái: Tốt])
```

---

## 5. Input Model

Các field editor phải nhập trước khi Scoring chạy. Map với field hiện có trong MoSpark:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Field</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Source</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Meta Title</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sinh từ Editor/GenAI</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dùng để check length, keyword placement</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Meta Description</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sinh từ Editor/GenAI</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dùng để check length</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Primary Keyword</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sync từ GenAI Content Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 từ khóa duy nhất. Nền tảng chặn Publish nếu trường này rỗng.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Secondary Keywords</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sync từ GenAI Content Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh sách từ khóa phụ. Optional.</td>
    </tr>
  </tbody>
</table>

> **Lưu ý Data Flow:** Toàn bộ Keywords (Primary/Secondary) sẽ được hệ thống `GenAI Content Engine` tạo và map tự động dựa trên Keyword Master Registry, sau đó đẩy (push) trực tiếp sang Blog Editor dưới dạng Draft. Editor không cần nhập tay ở bước này. Tuy nhiên, trước khi bấm Publish, **hệ thống Score sẽ làm nhiệm vụ chặn (Hard Block) để Editor phải Review lại chất lượng bài sinh ra từ AI.**

### 5.1 Primary Keyword

**Định nghĩa:** **1 từ khóa duy nhất** mà page được thiết kế để rank chính. Đây là từ khóa có priority cao nhất, thường có search volume cao, intent rõ ràng, và value conversion cao nhất. (Ví dụ: "vay tiền", "bảo hiểm")

**Validation Rules (Review Phase):**
- **Bắt buộc:** Không được để trống.
- **Min length:** Tối thiểu 2 ký tự.
- **Max length:** Tối đa 50 ký tự.
- **Ký tự hợp lệ:** Tiếng Việt (có dấu), chữ, số, dấu cách. Không chứa ký tự đặc biệt.
- **Không phải toàn số:** Phải chứa ít nhất 1 ký tự chữ.

**UI/UX:** Label "Primary Keyword *", Text Input (đã auto-fill từ GenAI), Character counter (X/50), Real-time validation.

### 5.2 Secondary Keywords

**Định nghĩa:** Danh sách các từ khóa phụ, bổ trợ cho Primary để cover thêm keyword variants, long-tail searches. (Ví dụ: "vay nhanh, vay online")

**Validation Rules (Review Phase):**
- **Optional:** Được phép để trống.
- **Format:** Cách nhau bởi dấu phẩy + space.
- **Max từ khóa:** Tối đa 10 từ khóa phụ.
- **Max length mỗi từ:** 50 ký tự.
- **Không trùng lặp:** Loại bỏ keyword trùng. Có cảnh báo nhẹ nếu chứa một phần Primary Keyword.

### 5.3 Integration với SEO/GEO Scoring
- **Primary Keyword:** Dùng check H1 (1.6), Density (2.2), Placement (2.3), Entity Context (3.4).
- **Secondary Keywords:** Check tần suất xuất hiện (2.4).
- **Behavior khi thay đổi:** Nếu thay đổi Keyword sau khi Run Score, điểm reset về "Chưa chạy" và yêu cầu Run lại.

### 5.4 Lưu ý cho Dev (Parsing)
Dev split `keywords` array từ field. Validate theo format regex.
Fallback: Nếu Publish mà Primary trống → nút Publish bị disable hoàn toàn.

---

## 6. Scoring Model (SEO/GEO Disciplines)

Để đảm bảo chuẩn thuật ngữ chuyên ngành và phân tách rõ ràng trách nhiệm tối ưu, checklist được chia thành 3 Blocks (Nhóm). Mỗi item trong nhóm sẽ có cờ `Hard Block`, nếu vi phạm sẽ khóa nút Publish.

### 6.1 Tổng điểm: 100 điểm (Cố định)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Block / Nhóm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm tối đa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Block 1 - Technical SEO & CWV</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>25</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nền tảng kỹ thuật và hiệu năng bắt buộc.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Block 2 - On-Page SEO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>55</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối ưu hóa nội dung hiển thị và từ khóa.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Block 3 - GEO & Entity Signals</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>20</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tín hiệu cấu trúc dữ liệu cho AI Search.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tổng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>100</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
  </tbody>
</table>

### 6.2 Ngưỡng Publish (Hard Gate)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Case</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điều kiện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Behavior của Nút Publish</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CASE 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blocked</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vi phạm bất kỳ 1 lỗi <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Hard Block</code> HOẶC Tổng điểm < 60</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Disabled</code> hoàn toàn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CASE 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Warning</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pass toàn bộ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Hard Block</code> VÀ Tổng điểm 60-79</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Enabled</code> (Hiển thị badge "⚠ Cần tối ưu")</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CASE 3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Pass</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pass toàn bộ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Hard Block</code> VÀ Tổng điểm ≥ 80</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Enabled</code> (Trạng thái "Tốt")</td>
    </tr>
  </tbody>
</table>

---

## 7. Chi tiết Checklist & Logic Tính Toán (Dành cho Editor & Dev)

### 7.1 Block 1: Technical SEO & Core Web Vitals (25 Điểm)
*Các yếu tố nền tảng để Googlebot thu thập dữ liệu và trải nghiệm người dùng.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng mục</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hard Block</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải thích cho Editor</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật toán Tính toán (Computation for Dev)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Canonical Tag</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phải trỏ đúng URL chuẩn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Parse <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><head></code> tìm <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><link rel="canonical" href="..."></code>. Khớp giá trị <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">href</code> với URL thực tế.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Robots Meta</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>YES</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cho phép Google Bot đọc trang.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Parse <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><head></code> tìm <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><meta name="robots"></code>. Giá trị bắt buộc chứa <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">index, follow</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CWV: LCP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thời gian tải nội dung chính ≤ 2.5s.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger API gọi Google PSI (thông qua Signed URL). Lấy <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">largest-contentful-paint</code>. Trả Fail nếu <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">> 2.5s</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CWV: INP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Độ trễ tương tác ≤ 200ms.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lấy trường <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">interaction-to-next-paint</code> từ PSI. Trả Fail nếu <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">> 200ms</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CWV: CLS</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm giật lag Layout ≤ 0.1.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lấy trường <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">cumulative-layout-shift</code> từ PSI. Trả Fail nếu <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">> 0.1</code>.</td>
    </tr>
  </tbody>
</table>

---

### 7.2 Block 2: On-Page SEO (55 Điểm)
*Tối ưu hóa trực tiếp trên nội dung bài viết.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng mục</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hard Block</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải thích cho Editor</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật toán Tính toán (Computation for Dev)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Primary Keyword</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>YES</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Từ khóa chính không được trống.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lấy array <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">keywords[0]</code>. Trả Fail nếu <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">length == 0</code> hoặc <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">< 2 chars</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Call-to-Action</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phải có ít nhất 1 nút bấm (W2A).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trong Editor, track button component. Fallback: tìm <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">data-cta="true"</code> hoặc <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><a class="momo-btn"></code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>H1 Tag</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 thẻ H1 duy nhất, chứa từ khóa.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đếm <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><h1/></code> trong body (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">count == 1</code>). Dùng Regex <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/keyword/i</code> check string bên trong thẻ.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Meta Title</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Độ dài 40-60 ký tự.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đếm length của field Meta Title. Phải nằm trong Range <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[40, 60]</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Meta Description</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Độ dài 120-160 ký tự.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đếm length của field Meta Description. Nằm trong Range <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[120, 160]</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Wordcount</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Độ dài text đủ chuẩn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Strip HTML tags, split text bằng khoảng trắng. Trả Pass nếu length ≥ 800 (Mini-web) hoặc ≥ 300 (Landing).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Keyword Density</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mật độ từ khóa chính 1-2%.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đếm tổng keyword (regex <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/\bkeyword\b/gi</code>) chia cho Wordcount tổng. Nằm trong <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[0.01, 0.02]</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Image Alt Text</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ảnh có text chú thích.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm thẻ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><img></code>. Pass nếu 100% các thẻ có <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">alt</code> và length > 0.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Encoding Error</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không lỗi font Tiếng Việt.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Regex check ký tự `/?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">□/` do unicode lỗi. Trả Pass nếu count == 0.</td>
    </tr>
  </tbody>
</table>

---

### 7.3 Block 3: GEO & Entity Signals (20 Điểm)
*Tối ưu hóa dữ liệu cấu trúc cho AI Search.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng mục</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hard Block</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải thích cho Editor</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật toán Tính toán (Computation for Dev)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Schema JSON-LD</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khai báo chuẩn dữ liệu.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Regex tìm <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><script type="application/ld+json"></code>. <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">JSON.parse</code> content, check tồn tại <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">@type</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Internal Links</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Liên kết chéo về MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Parse <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">href</code> của <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><a></code>. Pass nếu có URL chứa <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Social Meta (OG)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Share Facebook/Zalo chuẩn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Parse <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><head></code> tìm <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">meta property="og:..."</code>. Pass nếu đủ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">title</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">description</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">url</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">image</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Fact Density</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối thiểu 3 số liệu (%, tỷ, triệu).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Regex `/\b(\d+(?:\.\d+)?)\s*(%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">triệu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tỷ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VNĐ)\b/g`. Đẩy mảng ra Modal UI. Editor xác nhận -> Pass.</td>
    </tr>
  </tbody>
</table>

> **Quy tắc Scale điểm Block 3:**
> - **Trang Blog & Mini Web:** Áp dụng toàn bộ (20đ).
> - **Trang Landing Page & Merchant Page:** Bỏ qua kiểm tra `3.4 Fact Density`. Backend tự Scale điểm: `Block3_Score = (Điểm_Thực_Đạt / 15) * 20` (Làm tròn toán học).

---

## 8. CWV Integration - Performance Tooling (Offline)

### Lý do tích hợp
Core Web Vitals (LCP, INP, CLS) là yếu tố xếp hạng quan trọng của Google. Mặc dù không còn bị xem là **Hard Block** để tránh gây khó khăn cho Editor, nhưng điểm số sẽ bị trừ rất nặng nếu tải trang chậm, khiến bài viết khó đạt ngưỡng "Tốt" (≥ 80 điểm). Việc tích hợp công cụ đo đạc tại bước này giúp phát hiện Regression Layout trước khi trang Live.

### Implementation Method (Draft Signed URL)
- Vì trang đang ở chế độ Draft (chưa Live), có cơ chế Auth bảo vệ, Google PageSpeed Insights (PSI) API không thể truy cập trực tiếp URL.
- **Giải pháp (Bypass Auth):**
  1. Khi user click `Run CWV Check`, Backend cấp tốc sinh ra 1 Temporary Signed URL (Ví dụ: `momo.vn/draft/abc?token=xyz...`) cho phép bypass Authentication, TTL (Time-to-live) là 3 phút.
  2. Backend call Google PSI API với URL này.
  3. Nhận kết quả Lab Data và render về Score Panel. Hết 3 phút Token tự hủy.
- **Reset State:** Cứ mỗi lần Editor ấn `Save Draft` (làm thay đổi nội dung), điểm số CWV tự động reset về `0` (Trạng thái "Chưa kiểm tra"). Editor buộc phải `Run CWV Check` lại trước khi Publish.

---

## 9. UI Requirements (Score Panel)

Score Panel tích hợp trực tiếp bên dưới các trường nhập liệu SEO, phản ánh đúng cấu trúc Technical, On-Page và GEO.

```text
┌──────────────────────────────────────────────┐
│  SEO/GEO Score                               │
│                                              │
│  ████████████████░░░░  78/100                │
│  Status: ⚠ WARNING - Cần tối ưu thêm         │
│                                              │
│  ▼ Block 1 - Technical SEO (10/25) ⚠          │
│    [✗] Core Web Vitals (LCP chậm)            │
│    [✓] Canonical & Robots hợp lệ (Bắt buộc)  │
│                                              │
│  ▼ Block 2 - On-Page SEO (43/55)  ⚠          │
│    [✓] Có Primary Keyword (Bắt buộc)         │
│    [✓] Có Call-to-Action                     │
│    [✓] H1 chứa từ khóa                       │
│    [✗] Meta Title & Description chưa chuẩn   │
│    [✓] Độ dài nội dung (Wordcount)           │
│    [✓] Mật độ từ khóa (Density)              │
│    [✗] Thiếu Alt Text hình ảnh               │
│                                              │
│  ▼ Block 3 - GEO & Entity (10/20) ⚠          │
│    [✓] Schema JSON-LD                        │
│    [✓] Internal Links                        │
│    [✗] Thiếu Social Meta (OG Tags)           │
│    [✗] Fact Density (Thiếu số liệu)          │
│                                              │
│  [Run CWV Check]                             │
│                                              │
│  [Save Draft]          [⚠ Publish - Warning] │
└──────────────────────────────────────────────┘
```
> **Trường hợp Hard Block Fail:** UI progress bar chuyển sang màu Đỏ. Hiển thị dòng Text: `🛑 Bị chặn: Vi phạm [Tên Lỗi]. Vui lòng khắc phục!`. Nút Publish bị mờ (Disabled).

---

## 10. Technical Notes & API Hooks (Dành cho Trọng)

- **Integration Target:** Toàn bộ logic Block và CWV Check áp dụng chung cho cả `Blog Editor` và `Merchant Editor`. Khác biệt duy nhất nằm ở hàm Scale điểm Block 3.
- **Trigger Event:** Score Calculator sẽ tự động chạy ngầm mỗi khi user nhập text xong (Debounce 2s) đối với các lỗi On-Page và GEO (trừ CWV).
- **Publish Hook Gate:** Backend chỉ mở API Endpoint `/api/v1/publish` nếu check database (hoặc Redis Session) thỏa mãn: `Hard_Blocks_Failed == 0`. Nếu front-end bypass mở khóa nút Publish bằng inspect element, request bắn lên Backend vẫn sẽ trả mã lỗi `403 Forbidden` kèm thông báo chặn Publish.

---

## 10.5. Kế hoạch Nâng cấp & Tích hợp H2/2026 (Blog Editor Integration)

Trong H2/2026, hệ thống SEO/GEO Scoring System sẽ được tích hợp sâu vào Blog Editor nhằm siết chặt quy trình kiểm duyệt chất lượng đầu ra:

1. **Real-time Editor Score Panel:** Tích hợp bộ chấm điểm thời gian thực trực tiếp trên giao diện của Blog Editor (Tiptap). Điểm số và các cảnh báo sẽ thay đổi tự động dựa trên hành vi gõ văn bản của Editor (Debounce 2s).
2. **Automated Hard Block Gate:** Vô hiệu hóa nút Publish và chặn cứng API Endpoint `/api/v1/publish` nếu bài viết dính 1 trong 9 lỗi chặn cứng hoặc tổng điểm SEO/GEO < 60/100.
3. **YMYL & E-E-A-T Compliance Audit:** Tự động đối chiếu thông tin tác giả (Author Box, Social Links) và sự hiện diện của tuyên bố miễn trừ trách nhiệm (Disclaimer) đối với các bài viết tài chính nhạy cảm.
4. **CTA Limit Verification:** Tự động quét và cảnh báo lỗi nếu bài viết vượt quá số lượng tối đa cho phép là 2 CTAs.

---

## 11. Giải thích Thuật ngữ (Glossary)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật ngữ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải thích</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hard Block</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điều kiện chặn cứng - nếu item này fail, nút Publish bị vô hiệu hóa hoàn toàn, bất kể tổng điểm bao nhiêu.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Draft</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản nháp - trạng thái trang đã được lưu nhưng chưa live, chưa ảnh hưởng trang đang chạy.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Publish</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hành động đưa trang mới lên live lần đầu tiên.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Score Panel</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng chấm điểm SEO/GEO tích hợp trong MoSpark Admin.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CWV (Core Web Vitals)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bộ 3 chỉ số hiệu năng trang web cốt lõi của Google: LCP, INP, CLS - ảnh hưởng trực tiếp đến thứ hạng tìm kiếm.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>LCP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Largest Contentful Paint - thời gian tải phần nội dung lớn nhất hiển thị lên màn hình. Ngưỡng tốt: ≤ 2.5s.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>INP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Interaction to Next Paint - thời gian phản hồi khi người dùng tương tác (click, gõ phím). Ngưỡng tốt: ≤ 200ms.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>CLS</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cumulative Layout Shift - mức độ giật layout bất ngờ khi trang tải. Ngưỡng tốt: ≤ 0.1.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>FCP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">First Contentful Paint - thời gian xuất hiện nội dung đầu tiên. Ngưỡng tốt: ≤ 1.8s.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>TTFB</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Time to First Byte - thời gian server phản hồi byte đầu tiên. Ngưỡng tốt: ≤ 800ms.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>SEO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search Engine Optimization - tối ưu hóa để trang được tìm thấy trên Google và các công cụ tìm kiếm.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GEO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Generative Engine Optimization - tối ưu hóa để nội dung được trích dẫn bởi AI (ChatGPT, Perplexity, Google AI Overviews).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>E-E-A-T</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Experience, Expertise, Authoritativeness, Trustworthiness - bộ tiêu chí Google dùng để đánh giá chất lượng nội dung.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>YMYL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Your Money Your Life - nhóm nội dung nhạy cảm (tài chính, sức khỏe, pháp lý) bị Google đánh giá khắt khe hơn.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Canonical tag</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thẻ HTML khai báo URL "chính thống" của trang, giúp Google không bị confuse khi có nhiều URL tương tự.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Robots meta</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thẻ HTML chỉ định Google có được phép crawl và index trang hay không. Giá trị chuẩn: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">index, follow</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>DOM</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Document Object Model - cấu trúc HTML được dựng lên trong trình duyệt. System "parse DOM" nghĩa là đọc và phân tích cấu trúc HTML đó.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>JSON-LD</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">JavaScript Object Notation for Linked Data - định dạng khai báo Schema (dữ liệu có cấu trúc) trong thẻ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><script></code> của trang.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Schema / Structured Data</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dữ liệu có cấu trúc - thông tin được đánh dấu theo chuẩn Schema.org để AI và Google hiểu rõ nội dung trang hơn.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>SERP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search Engine Results Page - trang kết quả tìm kiếm của Google.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GSC</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google Search Console - công cụ miễn phí của Google để theo dõi hiệu suất tìm kiếm và phát hiện lỗi kỹ thuật.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Orphan page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang mồ côi - trang không được link đến từ bất kỳ trang nào khác trên site, Googlebot khó tìm thấy.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Fact Density</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mật độ số liệu - mức độ xuất hiện của số liệu, thống kê, dữ kiện cụ thể trong nội dung. AI engine ưu tiên trích dẫn nội dung có fact density cao.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Topical Authority</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thẩm quyền chủ đề - mức độ Google/AI đánh giá một site là nguồn đáng tin cậy về một chủ đề cụ thể.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Disclaimer</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tuyên bố từ chối trách nhiệm - đoạn văn bắt buộc trên nội dung tài chính, nhắc người đọc rằng nội dung chỉ mang tính thông tin, không phải tư vấn đầu tư.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Lab data</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dữ liệu đo lường trong môi trường kiểm soát (Lighthouse headless) - đo trên máy chủ, không phải dữ liệu thực từ người dùng.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Field data</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dữ liệu thực tế từ người dùng thật (Chrome UX Report) - chính xác hơn lab data nhưng chỉ có với trang đã có traffic.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Signed URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL tạm thời có gắn token bảo mật, cho phép truy cập trang Draft không cần đăng nhập trong thời gian giới hạn.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Headless Chrome</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trình duyệt Chrome chạy không có giao diện (ẩn), dùng để tự động hóa việc mở trang và đo hiệu năng trên server.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Internal link</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Liên kết nội bộ - link từ một trang trên momo.vn trỏ đến một trang khác cũng trên momo.vn.</td>
    </tr>
  </tbody>
</table>

---

## 12. Change Log

- **v2.0 (2026-06-01):** Tái cấu trúc (Re-architect) hoàn toàn mô hình điểm từ dạng Blocks sang dạng Tiers (Mandatory -> Basic -> Advanced). Nhúng thẳng thuật toán Computation Logic vào bảng để Tech Team làm Spec API.

- **v1.3.1 (2026-06-01):** Di chuyển Bảng Thuật Ngữ (Glossary) xuống cuối trang, trước Change Log, để ưu tiên luồng đọc Workflow và Input Model lên trên. Re-number các Heading tương ứng.
- **v1.3 (2026-06-01):** Chuẩn hóa toàn bộ cấu trúc tài liệu theo template của `mospark_genai_content.md`. Phục hồi các phần cốt lõi: Executive Summary, Stakeholders, và Bài toán cần giải. Re-format Headers và Bullet points.
- **v1.2 (2026-06-01):** Bổ sung chi tiết toàn bộ các quy chuẩn từ bản gốc: Bảng thuật ngữ, Input Model Validation, Chi tiết CWV Integration, Technical Notes cho Dev và Hard Block Summary.
- **v1.1 (2026-05-31):** Tái cấu trúc format presentation chuẩn hóa theo template của MoSpark GenAI Content Engine. Gom nhóm Header, Executive Summary, Roadmap và Tài liệu liên kết.
- **v1.0 (2026-04-15):** Khởi tạo tài liệu MVP Checklist.

---
*Maintained by: Văn Hiến (Web Product Lead) | Last updated: 2026-06-01*

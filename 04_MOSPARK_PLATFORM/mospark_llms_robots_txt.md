# MoSpark - LLMs Robots.txt
& Robots.txt - Operational Skill Document

> - **Document type:** Operational Skill
> - **Audience:** Web Platform Team (Bảo + members)
> - **Owner:** Web Platform · GPD · Văn Hiến
> - **Last updated:** Tháng 5/2026
> - **Status:** In Progress - robots.txt Lớp 1 DEPLOYED

---

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Bối cảnh: Search đang chuyển sang AI](#2-bối-cảnh)
3. [Robots.txt - Tình trạng hiện tại & Nâng cấp](#3-robotstxt)
4. [LLMs.txt - Là gì và nguyên lý vận hành](#4-llmstxt---là-gì)
5. [Tại sao MoMo cần làm ngay](#5-why-now)
6. [Case Studies](#6-case-studies)
7. [MoMo nên làm thế nào - Strategy & Architecture](#7-strategy)
8. [How: Setup](#8-how-setup)
9. [How: Content Generation - Tự động hóa](#9-how-content-generation)
10. [How: Maintain](#10-how-maintain)
11. [How: Debug & Validate](#11-how-debug)
12. [How: Follow - Theo dõi và cải tiến](#12-how-follow)

---

## 1. Executive Summary

Hai file `robots.txt` và `llms.txt` cùng nhau tạo thành **AI Crawler Policy** của momo.vn - quyết định AI systems hiểu MoMo như thế nào, được phép truy cập gì, và trả lời người dùng ra sao khi được hỏi về MoMo.

**Tình trạng hiện tại:**
- `robots.txt` tồn tại nhưng chưa có AI crawler policy. Toàn bộ training crawlers (GPTBot, ClaudeBot, Bytespider) đang crawl momo.vn mà không có chủ ý rõ ràng. Param `?date=` trên `momo.vn/ve-xe` đang tạo crawl budget waste và GSC 404 warnings mặc dù đã có canonical.
- `llms.txt` chưa tồn tại. AI không có structured context về MoMo → risk misrepresentation khi user hỏi AI về sản phẩm tài chính của MoMo.

**Giải pháp:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">File</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Action</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đợt Triển Khai</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">robots.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nâng cấp: fix param issue + add AI crawler policy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1 - Làm trước</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai mới: master index + per-product full doc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2 - Làm sau khi robots.txt ổn</td>
    </tr>
  </tbody>
</table>

**Robots.txt phải được nâng cấp trước.** `llms.txt` hoàn toàn vô nghĩa nếu AI search crawlers bị block hoặc bị ảnh hưởng bởi conflicting directives.

---

## 2. Bối cảnh: Search đang chuyển sang AI

### 2.1 Thay đổi hành vi tìm kiếm

- Google searches per US user giảm gần 20% year-over-year năm 2025
- Google search traffic đến publishers giảm 33% giữa Nov 2024 và Nov 2025
- ChatGPT: 700M weekly active users, tăng 2x trong 6 tháng
- Perplexity: 780M queries/tháng, growth 20%+ MoM
- Google AI Overviews: xuất hiện trên 13-30% queries, fintech là category trigger cao

Người dùng Việt Nam đang hỏi AI: *"ví điện tử nào tốt nhất"*, *"vay tiền online uy tín"*, *"lãi suất MoMo bao nhiêu"*. Nếu AI không có context đúng về MoMo, nó trả lời dựa trên training data cũ hoặc content của competitor.

### 2.2 AI crawler traffic đang scale nhanh

- OpenAI ChatGPT-User requests tăng 2,800%, đạt 1.3% tổng web requests năm 2025
- Googlebot AI features tăng 96% year-over-year
- ClaudeBot tăng 800% đầu 2026 khi Anthropic scale web search API
- Applebot-Extended tăng mạnh với Apple Intelligence, đạt 5.8% tổng crawl traffic

AI crawlers không còn là edge case trong server logs - chúng đang là một phần significant của traffic.

### 2.3 Hai loại AI crawler - Phân biệt cốt lõi

Mọi quyết định về robots.txt và llms.txt đều xoay quanh sự phân biệt này:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục đích</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoMo nên?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Search/RAG crawler</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Index real-time để trả lời user queries</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">OAI-SearchBot, Claude-SearchBot, PerplexityBot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MUST ALLOW</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Training crawler</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thu thập data để train LLM model</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GPTBot, ClaudeBot, Google-Extended</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Policy decision</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Aggressive scraper</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Scrape không có referral benefit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bytespider, CCBot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đề xuất block</strong></td>
    </tr>
  </tbody>
</table>

Search crawlers = GEO visibility. Training crawlers = data licensing question. Aggressive scrapers = không có upside, chỉ có cost.

---

## 3. Robots.txt - Tình trạng hiện tại & Nâng cấp

### 3.1 Robots.txt hiện tại của momo.vn

```
User-agent: *
Allow: /
Disallow: /error/500
Disallow: /Files
Disallow: /help
Disallow: /inbienlai
Disallow: /tim-kiem
Disallow: /_next/
Disallow: /view-app/

## Disallow Param
Disallow: /*fromType=
Disallow: /*flightType=
Disallow: /*fbclid=

Sitemap: https://www.momo.vn/sitemap-1.1.xml
```

### 3.2 Phân tích tình trạng hiện tại

**Phần Disallow paths - Đánh giá từng directive:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Directive</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đánh giá</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/error/500</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Block trang lỗi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/Files</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Block file storage</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/help</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần xem lại</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Help content có giá trị cho AI hiểu sản phẩm MoMo - đang block cả SEO lẫn AI</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/inbienlai</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không cần index</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tim-kiem</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search result page, không có giá trị crawl</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/_next/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Next.js static assets</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/view-app/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App deep link view</td>
    </tr>
  </tbody>
</table>

**Vấn đề 1 - `/help` đang bị block:**
Nếu đây là trang hướng dẫn sử dụng sản phẩm, đây là content có giá trị cho cả SEO index lẫn AI understanding. Cần Web Platform + Web Platform confirm mục đích thực sự trước khi quyết định giữ hay bỏ directive này.

**Vấn đề 2 - Không có AI crawler policy:**
`User-agent: * Allow: /` có nghĩa tất cả crawlers được phép crawl toàn bộ site - bao gồm Bytespider (ByteDance), CCBot (Common Crawl), và tất cả training crawlers. Đây không phải lỗi, nhưng là **policy mặc định không có chủ ý**. MoMo chưa bao giờ thực sự quyết định có muốn content của mình vào training data AI hay không.

**Vấn đề 3 - Param `?date=` trên `momo.vn/ve-xe`:**

Đây là vấn đề cụ thể nhất và có thể fix ngay.

`momo.vn/ve-xe?date=2024-01-15` là URL có tính thời gian - khi ngày đó qua đi, URL trả về 404. Mặc dù canonical đã được set về `momo.vn/ve-xe`, nhưng:

- Googlebot vẫn **crawl** URL có param, chỉ không **index** nó
- Khi URL parameterized trả về 404 thay vì 200 + canonical, GSC báo 404 warning
- Crawl budget bị lãng phí vào hàng nghìn date-specific URLs đã expired
- AI crawlers không tôn trọng canonical như Googlebot - có thể crawl và cache thông tin expired

Canonical giải quyết indexation nhưng **không giải quyết crawl budget và 404 signal**. Cần block param này trong robots.txt.

**Phần Param hiện tại - Đánh giá:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Param</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đánh giá</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/*fbclid=</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng <strong>Replaced</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã cover bởi <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Disallow: /*?</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/*fromType=</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng một phần <strong>Replaced</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã cover bởi <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Disallow: /*?</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/*flightType=</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đúng một phần <strong>Replaced</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã cover bởi <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Disallow: /*?</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">?date=</code> trên <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/ve-xe</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>RESOLVED</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cover bởi <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Disallow: /*?</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Disallow: /*?</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>DEPLOYED</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Block toàn bộ URL có query string - thay thế tất cả param rules cũ</td>
    </tr>
  </tbody>
</table>

### 3.3 Cải thiện robots.txt - Theo 3 lớp

**Lớp 1 - Fix param (DEPLOYED):**

`Disallow: /*?` đã được Dev deploy - block toàn bộ URL có query string trên momo.vn. Cover hết `?date=`, `?fbclid=`, `?fromType=`, `?flightType=` và mọi param khác trong một directive duy nhất. Các param rules cũ (`/*fromType=`, `/*flightType=`, `/*fbclid=`) đã redundant và có thể cleanup khỏi robots.txt.

```
# DEPLOYED
Disallow: /*?
```

**Lưu ý cần verify với Dev:** `/*?` cũng block `?utm_source=`, `?ref=` và các marketing params. Không ảnh hưởng indexing (canonical đã xử lý) nhưng cần confirm không có use case nào cần crawler access URL có param.

**Lớp 2 - Block aggressive scrapers (không cần policy decision, chỉ cần confirm):**

Bytespider và CCBot không có referral traffic benefit - chỉ scrape data cho training. Không có upside khi allow, chỉ có cost về bandwidth và data:

```
# Aggressive scrapers - không có referral traffic benefit
User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /
```

**Lớp 3 - AI Training Crawler Policy (cần quyết định từ Product/Legal):**

Đây là quyết định về data licensing - không phải quyết định kỹ thuật. Web Platform implement theo option MoMo chọn.

**Option A - Allow tất cả training crawlers:**

```
# Training crawlers - allow toàn bộ (default hiện tại, explicit declaration)
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /
```

Trade-off: Content MoMo xuất hiện trong training data → AI biết về MoMo nhiều hơn, describe chính xác hơn long-term. Nhưng MoMo không có thỏa thuận hay compensation từ các AI labs khi dùng content.

**Option B - Block tất cả training crawlers:**

```
# Block training crawlers - chỉ allow search/RAG crawlers
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /
```

Trade-off: Bảo vệ content khỏi bị dùng để train AI. Nhiều fintech lớn chọn option này. Nhưng AI model sẽ biết ít hơn về MoMo từ training data - phụ thuộc nhiều hơn vào llms.txt và real-time search.

**Option C - Allow search, block training (Recommended pattern của industry):**

```
# Search/RAG crawlers - allow (phục vụ user queries real-time)
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

# Training crawlers - block (data licensing question)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /
```

Trade-off: Cân bằng tốt nhất giữa GEO visibility (allow search crawlers) và data protection (block training crawlers). Đây là approach của nhiều fintech và publisher lớn. Nhược điểm: AI model's background knowledge về MoMo phụ thuộc hoàn toàn vào real-time retrieval, không có training data backup.

**Option D - Allow có chọn lọc theo path:**

```
# Chỉ allow training crawlers vào blog và trang sản phẩm public
User-agent: GPTBot
Allow: /tin-tuc/
Allow: /vay-nhanh
Allow: /bao-hiem
Allow: /esim-du-lich
Disallow: /

User-agent: ClaudeBot
Allow: /tin-tuc/
Allow: /vay-nhanh
Allow: /bao-hiem
Allow: /esim-du-lich
Disallow: /
```

Trade-off: Kiểm soát chi tiết nhất - AI chỉ train trên content MoMo muốn. Nhưng maintenance cao khi có product mới, và logic phức tạp dễ có conflict.

### 3.4 Robots.txt sau khi nâng cấp - Mẫu tổng hợp

Template dưới đây áp dụng Lớp 1 + Lớp 2 + Option C (chỗ `[OPTION]` thay bằng option MoMo chọn):

```
# ==========================================
# momo.vn robots.txt
# Last updated: 2026-05-04
# Policy: AI Search/RAG - Allow | AI Training - Allow
# ==========================================

# === ANTHROPIC CRAWLERS ===
# ClaudeBot: training data - Allow (GEO signal)
User-agent: ClaudeBot
Allow: /

# Claude-SearchBot: index for Claude search - Allow
User-agent: Claude-SearchBot
Allow: /

# Claude-User: fetch khi user query Claude - Allow
User-agent: Claude-User
Allow: /

# === OPENAI CRAWLERS ===
# GPTBot: training data - Allow
User-agent: GPTBot
Allow: /

# OAI-SearchBot: ChatGPT search indexing - Allow
User-agent: OAI-SearchBot
Allow: /

# ChatGPT-User: user-initiated fetch - Allow
User-agent: ChatGPT-User
Allow: /

# === GOOGLE AI ===
# Google-Extended: Gemini training - Allow
User-agent: Google-Extended
Allow: /

# === OTHER AI SEARCH ===
User-agent: PerplexityBot
Allow: /

User-agent: Applebot-Extended
Allow: /

# === AGGRESSIVE SCRAPERS - BLOCK ===
User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /

# === DEFAULT - ALL OTHER CRAWLERS ===
User-agent: *
Allow: /

# Kỹ thuật/internal paths
Disallow: /error/500
Disallow: /Files
Disallow: /inbienlai
Disallow: /tim-kiem
Disallow: /_next/
Disallow: /view-app/

# === PARAM DISALLOW ===
Disallow: /*?
Disallow: /*?*fromType=
Disallow: /*?*flightType=
Disallow: /*?*fbclid=

# === SITEMAP ===
Sitemap: https://www.momo.vn/sitemap-1.1.xml
```

**Lưu ý về `/help`:** Giữ nguyên trong template trên - cần Web Platform + Web Platform confirm mục đích trước khi quyết định.

### 3.5 Giới hạn của robots.txt cần biết

robots.txt hoạt động theo honor system. Một số thực tế:

- 72% AI crawlers vi phạm robots.txt theo nghiên cứu 2025
- Trung bình 156 violation requests per site trong 3 tuần
- Bytespider đặc biệt aggressive - block trong robots.txt giảm nhưng không triệt tiêu hoàn toàn
- robots.txt là signal, không phải firewall

Nếu MoMo cần bảo vệ nghiêm ngặt hơn: rate limiting theo user-agent ở CDN/server level là layer tiếp theo, nằm ngoài scope của BRD này.

---

## 4. LLMs.txt - Là gì và nguyên lý vận hành

### 4.1 Định nghĩa

`llms.txt` là plain-text Markdown file đặt tại root domain (`momo.vn/llms.txt`), thiết kế để cung cấp structured context cho Large Language Models **tại inference time** - tại thời điểm user đang đặt câu hỏi cho AI, không phải lúc AI crawler index web.

Standard được Jeremy Howard (Answer.AI) đề xuất ngày 3/9/2024. Voluntary standard - không có enforcement, nhưng adoption tăng nhanh trong tech và fintech toàn cầu. Tính đến tháng 7/2025: hơn 950 domains đã implement.

### 4.2 Vị trí trong hệ sinh thái file

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">File</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đối tượng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timing</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục đích</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">robots.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search + AI crawlers</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Crawl time</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Allow/disallow crawling, training policy</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sitemap.xml</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search indexers</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Index time</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">List URLs cần index</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LLMs</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Inference time</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Context để AI trả lời đúng về MoMo</td>
    </tr>
  </tbody>
</table>

Ba file cùng tồn tại, phục vụ ba mục đích khác nhau. `robots.txt` là prerequisite - phải đúng trước khi `llms.txt` có tác dụng.

### 4.3 Cơ chế hoạt động - Inference-time RAG

```
User hỏi: "Vay tiền online uy tín ở Việt Nam?"
        ↓
AI retrieve các sources liên quan từ index
        ↓
AI parse nội dung - khó với HTML phức tạp
        ↓  ← llms.txt can thiệp tại đây
AI chọn content phù hợp trong context window giới hạn
        ↓
AI generate câu trả lời + cite nguồn
```

**Không có `llms.txt`:** momo.vn có 100+ pages - AI không thể đọc hết. HTML phức tạp làm AI parse sai, bỏ sót, hoặc hallucinate thông tin về MoMo.

**Có `llms.txt`:** AI đọc một Markdown file súc tích - biết ngay sản phẩm nào tồn tại, page nào authoritative, URL nào cần ưu tiên.

### 4.4 Ba layer của implementation đầy đủ

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Layer</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">File</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/llms.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Master index - tổng quan toàn bộ sản phẩm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/{product}/llms-full.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Full documentation per product</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 1-2</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/{page}/index.md</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Clean Markdown per page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 3 - defer</td>
    </tr>
  </tbody>
</table>

### 4.5 Format chuẩn

```markdown
# [Brand Name]
> [One-liner mô tả - 1-2 câu factual, không marketing]

[2-3 câu context về brand]

## [Category sản phẩm]
- [Tên sản phẩm](URL): Mô tả ngắn, factual

## Optional
- [Nội dung phụ](URL): AI có thể skip nếu context window ngắn
```

**`## Optional` có semantic đặc biệt theo spec:** AI có thể bỏ qua section này khi context window bị giới hạn. Dùng cho blog, FAQ phụ, landing pages secondary. Core product pages phải ở sections trước `Optional`.

---

## 5. Tại sao MoMo cần làm ngay

### 5.1 Khuyến cáo từ chuyên gia và tổ chức

- **Jeremy Howard (Answer.AI):** Khuyến cáo implement sớm trước khi AI crawlers solidify behavior
- **Search Engine Journal (2025):** Liệt kê `llms.txt` là một trong 5 GEO signals cần setup trong 2025
- **Ahrefs GEO Guide (2025):** Recommend như bước đầu tiên trong AI search optimization checklist
- **Google A2A Protocol:** Google đưa `llms.txt` vào Agents-to-Agents protocol (experimental)

### 5.2 First-mover window

Tính đến tháng 5/2025, chưa có confirmed case nào từ major Vietnamese fintech (ZaloPay, VPBank, Cake, TPBank) deploy `llms.txt`. Window sẽ đóng khi AI platforms chính thức announce support.

### 5.3 Risk của việc không làm

**Misrepresentation risk:** AI cite thông tin sai về MoMo - lãi suất cũ, tính năng deprecated, URL sai. Ảnh hưởng trực tiếp brand trust và conversion.

**Passive positioning:** AI describe MoMo theo cách nó tự suy ra từ HTML hỗn độn, thay vì theo cách MoMo muốn được nhìn nhận là super app tài chính, không chỉ là ví điện tử.

### 5.4 Honest caveat

Tính đến tháng 8/2025, chưa có major AI platform nào chính thức confirm họ đọc `llms.txt` trong inference pipeline. Log analysis trên 1,000 domains cho thấy không có AI crawler nào request file `llms.txt` trực tiếp. Tuy nhiên:

- Effort implementation thấp, downside risk gần như bằng 0
- File có giá trị nội bộ ngay lập tức (manual upload vào AI tools, documentation nội bộ)
- Khi standard được adopt chính thức, MoMo đã sẵn sàng thay vì phải rush

Treat đây là infrastructure investment với asymmetric risk/reward, không phải guaranteed traffic lever.

---

## 6. Case Studies

### 6.1 Mastercard - Fintech benchmark (Deep dive)

Mastercard là fintech toàn cầu có cấu trúc product phức tạp - case study relevant nhất với MoMo.

**Implementation:**
- `developer.mastercard.com/llms.txt` - Master index list toàn bộ products kèm link đến documentation từng service
- Mỗi service có `llms-full.txt` riêng: feature descriptions, quick start, API reference, error codes
- Mỗi page có Markdown version bằng cách thêm `/index.md` vào URL
- File tự động update khi documentation thay đổi trong CMS - không có manual step

**Lesson cho MoMo:** Tách `llms-full.txt` theo từng product, không gộp vào một file. Auto-generate từ CMS là target, không phải nhập tay.

### 6.2 Stripe - Payment fintech

Stripe prioritize content có highest user intent thay vì list tất cả URLs.

**Lesson cho MoMo:** Prioritize product pages có highest search intent (vay, bảo hiểm, eSIM) trong master `llms.txt`. Secondary content vào `## Optional`.

### 6.3 Cloudflare - Infrastructure

Cloudflare tập trung vào use-case description - viết để AI answer user questions, không phải để developer integrate API.

**Lesson cho MoMo:** Approach đúng hơn với MoMo. User hỏi AI về sản phẩm MoMo để quyết định dùng hay không. Content phải answer: "MoMo vay được bao nhiêu?" chứ không phải "MoMo API endpoint là gì?"

### 6.4 FastHTML (Answer.AI) - Reference implementation

Ngoài `llms.txt` cơ bản, họ tạo thêm `llms-ctx.txt` và `llms-ctx-full.txt` dùng XML-based structure tối ưu cho từng AI platform.

**Lesson:** Pattern này relevant ở Phase 4 khi MoMo muốn optimize riêng cho Claude vs ChatGPT vs Gemini.

---

## 7. MoMo nên làm thế nào - Strategy & Architecture

### 7.1 File architecture

```
momo.vn/robots.txt                     ← Nâng cấp (P0)
momo.vn/llms.txt                       ← Layer 1: Master index (P1)
momo.vn/vay-nhanh/llms-full.txt        ← Layer 2: Full doc (P1)
momo.vn/vi-tra-sau/llms-full.txt
momo.vn/bao-hiem/llms-full.txt
momo.vn/esim-du-lich/llms-full.txt
momo.vn/quan-ly-chi-tieu/llms-full.txt
[defer] momo.vn/{page}/index.md        ← Layer 3 (Phase 3)
```

### 7.2 Nguồn content và cách generate

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Có sẵn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chất lượng cho AI</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dùng cho</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Metadata (Title/Description/URL)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có trong Supabase</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình - viết cho SEO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Master <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms.txt</code> - link list</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Long Content (Rich Text/HTML, SSR)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có trong CMS</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao - có heading structure</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms-full.txt</code> - body content</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms_summary</code> field (field mới)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có, cần add</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao nhất - viết đúng mục đích</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Master <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms.txt</code> - description per product</td>
    </tr>
  </tbody>
</table>

### 7.3 Nguyên tắc content

**Giữ lại khi generate:**
- Định nghĩa sản phẩm, điều kiện eligibility, quy trình step-by-step
- Danh sách đối tác (EVF, MCredit, VietCredit, MBV với Vay Nhanh)
- FAQ nếu có trong Long Content

**Loại bỏ khi generate:**
- Bảng lãi suất số cụ thể - thay đổi thường xuyên, AI cite sai theo thời gian
- Promotional copy ("Chỉ với một chạm", "lối tắt nhanh gọn")
- Testimonials và user reviews
- Navigation, footer, breadcrumb
- Thông tin promotion theo thời gian

### 7.4 Ownership

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Deliverable</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Content owner</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Technical owner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">robots.txt</code> nâng cấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform (spec)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform (implement)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms_summary</code> per product</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform + BU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform (add field vào CMS)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Long Content quality</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team + BU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Auto-generate pipeline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quarterly review</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform (URL check)</td>
    </tr>
  </tbody>
</table>

---

## 8. How: Setup

### 8.1 Thứ tự thực hiện

```
Bước 1: Nâng cấp robots.txt (P0)
  → Fix /ve-xe?date= param
  → Block Bytespider + CCBot
  → Add AI training policy (theo option MoMo chọn)
  → Explicit allow cho search crawlers
        ↓
Bước 2: Baseline metrics
  → Pull GA4: sessions từ AI platforms (perplexity.ai, chatgpt.com, claude.ai)
  → Ghi lại làm baseline
        ↓
Bước 3: Confirm canonical URLs
  → Web Platform cung cấp danh sách
  → Web Platform verify 200 OK, không có redirect chain
        ↓
Bước 4: Add llms_summary field vào Supabase CMS
        ↓
Bước 5: Deploy llms.txt master index + llms-full.txt per product
        ↓
Bước 6: Validate + monitor
```

### 8.2 Server requirements cho llms.txt

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Requirement</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Spec</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lý do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">https://momo.vn/llms.txt</code> (root)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI crawlers expect ở đây theo spec</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content-Type</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">text/plain; charset=utf-8</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không phải HTML hay JSON</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">HTTP Status</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">200 OK trực tiếp - không redirect</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Redirect chain làm crawlers bỏ qua</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">HTTPS</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bắt buộc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI crawlers không fetch HTTP</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">File size</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khuyến nghị dưới 50KB cho master</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Context window efficiency</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cache</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Public, TTL 1 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không quá stale</td>
    </tr>
  </tbody>
</table>

### 8.3 Cấu trúc llms.txt master - Mẫu cho momo.vn

```markdown
# MoMo

> MoMo (momo.vn) là ví điện tử và super app tài chính hàng đầu Việt Nam,
> cung cấp dịch vụ thanh toán, vay tiền, bảo hiểm, đầu tư, và tiện ích
> đời sống cho hơn 31 triệu người dùng tại Việt Nam.

MoMo được vận hành bởi Service (Công ty Cổ phần Dịch vụ Di Động Trực Tuyến),
được cấp phép bởi Ngân hàng Nhà nước Việt Nam. Khả dụng trên iOS và Android.

## Sản phẩm tín dụng

- [Vay Nhanh](https://momo.vn/vay-nhanh): [llms_summary - Vay Nhanh]
  Full documentation: https://momo.vn/vay-nhanh/llms-full.txt

- [Ví Trả Sau](https://momo.vn/vi-tra-sau): [llms_summary - VTS]
  Full documentation: https://momo.vn/vi-tra-sau/llms-full.txt

- [Kiểm tra tín dụng CIC](https://momo.vn/kiem-tra-lich-su-tin-dung):
  [llms_summary - CIC]

## Bảo hiểm

- [Bảo hiểm](https://momo.vn/bao-hiem): [llms_summary - Insurance]
  Full documentation: https://momo.vn/bao-hiem/llms-full.txt

## Du lịch và tiện ích

- [eSIM Du lịch](https://momo.vn/esim-du-lich): [llms_summary - eSIM]
  Full documentation: https://momo.vn/esim-du-lich/llms-full.txt

## Công cụ tài chính cá nhân

- [Quản lý Chi tiêu](https://momo.vn/quan-ly-chi-tieu): [llms_summary - QLCT]

## Optional

- [Blog Du lịch](https://momo.vn/tin-tuc/du-lich): Hướng dẫn du lịch
  tích hợp thông tin dịch vụ MoMo.
- [Blog Tài chính](https://momo.vn/tin-tuc/tai-chinh): Kiến thức tài chính
  cá nhân cho người dùng phổ thông Việt Nam.
- [llms-full.txt tổng hợp](https://momo.vn/llms-full.txt): Toàn bộ
  documentation chi tiết tất cả sản phẩm MoMo.
```

---

## 9. How: Content Generation - Tự động hóa

### 9.1 Vấn đề cần giải quyết

**Input hiện tại:**
- Metadata: Title, Description, Keyword, URL - viết cho SEO, không phải cho AI
- Long Content: Rich Text/HTML, SSR, do Media Team + BU viết, chứa noise (pricing tables, promotional copy, testimonials)
- Không có Markdown version

**Output cần đạt:**
- `llms.txt` master: Markdown sạch, dưới 50KB, factual, auto-generated
- `llms-full.txt` per product: Markdown đủ context, đã filter noise, không cần review thủ công

### 9.2 Option A - Thêm `llms_summary` field vào CMS

**Mô tả:** Web Platform thêm field mới vào Supabase schema. Field này chứa 2-3 câu mô tả factual về sản phẩm - viết đúng cho AI đọc. Media Team/BU + Web Platform điền một lần, pipeline tự pull vào `llms.txt` master.

**Gợi ý field spec:**
- Field name: `llms_summary`
- Type: Plain text (không phải rich text)
- Max length: 300 ký tự (~2-3 câu)
- Required: Không - nếu rỗng thì fallback về meta description
- Visibility: Chỉ trong CMS admin, không render ra frontend

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">--</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">--</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ưu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Output chất lượng cao, đúng product positioning. Không phụ thuộc meta description viết cho SEO</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhược</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần effort điền field mới cho tất cả product pages hiện có</td>
    </tr>
  </tbody>
</table>

### 9.3 Option B - Structured Long Content với auto-tagging

**Mô tả:** Web Platform định nghĩa heading structure chuẩn trong CMS template. Khi Media Team/BU dùng headings theo structure này, CMS tự động gán attributes vào HTML output. Pipeline extract đúng sections, bỏ qua noise.

**Sections nên extract:**
- Định nghĩa sản phẩm (H2: "X là gì?")
- Ưu điểm, tính năng chính
- Quy trình, hướng dẫn
- Điều kiện
- Đối tác
- FAQ

**Sections nên exclude:**
- Pricing/lãi suất tables (class hoặc attribute riêng)
- Testimonial blocks
- Promotional banner sections

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">--</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">--</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ưu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team/BU viết bình thường, không cần biết về llms.txt. Filter noise tự động</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhược</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần enforce heading structure trong CMS. Long Content hiện tại có thể cần migration</td>
    </tr>
  </tbody>
</table>

### 9.4 Option C - Pipeline-level filter (không thay đổi CMS)

**Mô tả:** Giữ CMS như hiện tại. Pipeline fetch HTML từ SSR page, apply filter rules để strip noise (pricing tables, testimonials, promotional copy), convert toàn bộ sang Markdown.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">--</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">--</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ưu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không cần thay đổi CMS, không cần train Media Team/BU</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhược</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Filter rules brittle - khi HTML structure thay đổi, pipeline break. Khó filter promotional copy hoàn toàn bằng pattern matching</td>
    </tr>
  </tbody>
</table>

### 9.5 Đề xuất kết hợp

- **Option A** cho master `llms.txt`: `llms_summary` field đảm bảo quality của overview per product
- **Option B** cho `llms-full.txt`: structured Long Content với auto-tagging
- **Option C** làm fallback cho Phase 1 nếu A+B cần thêm thời gian setup

### 9.6 Trigger generate

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Option</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trade-off</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Manual trigger qua CI/CD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Run pipeline khi có product change</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đơn giản nhất, phù hợp setup hiện tại</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CMS publish hook</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự trigger khi editor publish</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Near real-time, cần implement webhook</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Scheduled (nếu có cron)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chạy định kỳ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không real-time nhưng đảm bảo sync</td>
    </tr>
  </tbody>
</table>

Với setup hiện tại (CI/CD có, cron không có): **Manual trigger** là khả dụng ngay.

### 9.7 Content rules cho Media Team/BU

Web Platform chịu trách nhiệm communicate rules sau đến Media Team/BU:

**Nên làm:**
- Dùng H2 cho section chính, H3 cho subsection - không skip heading level
- Mỗi section một chủ đề rõ ràng
- Viết factual - AI sẽ đọc và cite nội dung này

**Không viết:**
- Lãi suất số cụ thể theo gói - thay bằng range hoặc link đến trang lãi suất
- Câu marketing: "chỉ với một chạm", "nhanh chóng tiện lợi hơn bao giờ hết"
- Thông tin promotion theo thời gian

---

## 10. How: Maintain

### 10.1 Hai loại update

**Ad-hoc - Trigger ngay:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trigger</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product mới có landing page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thêm vào <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms.txt</code> + tạo <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms-full.txt</code> + điền <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms_summary</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL thay đổi hoặc permanent redirect</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Update URL trong tất cả files + robots.txt nếu liên quan</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product deprecated</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xóa khỏi <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms.txt</code>, archive <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">llms-full.txt</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phát hiện AI cite sai về MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review Long Content + re-generate</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sản phẩm mới có tính thời gian (param issue)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Add param vào robots.txt Disallow trước khi launch</td>
    </tr>
  </tbody>
</table>

**Quarterly review:**

```
[ ] Verify tất cả URLs trong llms.txt trả về 200 OK
[ ] Check product/feature mới cần add không
[ ] Query ChatGPT + Perplexity về MoMo - AI đang nói gì?
[ ] Pull GA4 AI referral report
[ ] Check server logs: AI crawlers fetch frequency
[ ] Review robots.txt: có crawler mới cần add policy không
[ ] Check llmstxt.org changelog - spec update không?
[ ] Re-generate toàn bộ nếu có nhiều thay đổi tích lũy
```

### 10.2 Workflow update

```
Phát hiện cần update
        ↓
Update nguồn: Long Content trong CMS và/hoặc llms_summary field
        ↓
Trigger CI/CD pipeline re-generate
        ↓
Pipeline auto-generate file mới
        ↓
Deploy lên server
        ↓
Quick verify: fetch file, check content đúng không
```

### 10.3 Version control

Tất cả files quản lý trong Git. Commit message format:
- `[robots] Block Bytespider, add OAI-SearchBot explicit allow`
- `[llms] Add eSIM to master index`
- `[llms] Regenerate Vay Nhanh after Long Content update`

---

## 11. How: Debug & Validate

### 11.1 Validate sau deploy

**robots.txt:**
- Fetch `momo.vn/robots.txt` - verify nội dung đúng với version đã approve
- Test: user-agent simulator để verify AI search crawlers không bị block
- Monitor GSC Coverage report sau 2-4 tuần - `?date=` 404 warnings phải giảm

**llms.txt:**
- Fetch `https://momo.vn/llms.txt` → 200 OK, Content-Type `text/plain`
- Không có redirect trước 200
- Content là Markdown, H1 đầu tiên là "MoMo"
- Tất cả URLs là absolute với `https://`

**Test với AI:**
Upload `llms.txt` lên ChatGPT, hỏi: *"Dựa trên file này, MoMo có những sản phẩm gì?"* - Nếu AI list đúng sản phẩm thì content architecture đang hoạt động.

### 11.2 Khi AI mention sai hoặc không mention MoMo

```
Bước 1: robots.txt có block search crawler không?
  → Verify OAI-SearchBot, Claude-SearchBot, PerplexityBot đều allow

Bước 2: llms.txt có accessible không?
  → Fetch file, check 200 OK và Content-Type

Bước 3: Content có đúng format không?
  → Validate Markdown structure, check H1, blockquote

Bước 4: Manual test with AI
  → Nếu AI trả lời đúng khi upload file: vấn đề là AI chưa index (chờ 2-4 tuần)
  → Nếu AI trả lời sai khi upload file: vấn đề là content → review Long Content nguồn
```

### 11.3 Monitor AI crawler activity

Web Platform filter trong server logs các user-agents:

```
OAI-SearchBot, ChatGPT-User, GPTBot
ClaudeBot, Claude-SearchBot, Claude-User
PerplexityBot, Applebot-Extended
Bytespider (để verify block đang hoạt động)
```

Nếu sau 4 tuần không có fetch nào từ search crawlers → kiểm tra lại robots.txt.

### 11.4 Track AI referral traffic trong GA4

Custom channel group:
```
Channel: AI Referral
Sources: perplexity.ai, chatgpt.com, claude.ai, bing.com/chat, you.com
```

Report monthly, so sánh với baseline đã ghi trước deploy.

### 11.5 Citation quality test - Monthly

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Query</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kỳ vọng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"MoMo vay tiền như thế nào?"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mention Vay Nhanh, đúng đối tác</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM du lịch Nhật Bản mua ở đâu?"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo được mention</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Ví điện tử VN nào có bảo hiểm xe máy?"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo bảo hiểm được mention</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"MoMo là gì?"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Describe là super app, không chỉ payment app</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Vay tiền online uy tín Việt Nam"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo trong danh sách</td>
    </tr>
  </tbody>
</table>

---

## 12. How: Follow - Theo dõi và cải tiến

### 12.1 Nguồn theo dõi

**Chính thức:**
- `llmstxt.org` - Changelog của spec
- `github.com/AnswerDotAI/llms-txt` - Issues và PRs
- Google Search Central Blog - AI Overview và A2A updates
- Cloudflare Radar - AI crawler traffic trends

**Industry:**
- Search Engine Journal, Ahrefs Blog - Weekly cho GEO/AI search updates

**Trigger cần action ngay:**
- AI platform chính thức announce support llms.txt → update và re-test
- Spec thay đổi format → review và update tất cả files
- AI crawler mới xuất hiện → add vào robots.txt

### 12.2 Roadmap theo phase

**Phase 1 - Foundation (tháng 1-2):**
- Nâng cấp robots.txt: fix param + block aggressive scrapers + AI training policy
- Deploy `momo.vn/llms.txt` master index
- Deploy `llms-full.txt` cho 3 use case priority: Vay Nhanh, Bảo hiểm, eSIM
- Add `llms_summary` field vào CMS
- Setup GA4 AI referral tracking + server log monitoring

**Phase 2 - Expand (tháng 3-4):**
- Deploy `llms-full.txt` cho: VTS, CIC, Quản lý chi tiêu
- Implement structured Long Content (Option B)
- Submit vào llmstxt directories (llmstxt.site, directory.llmstxt.cloud)
- First quarterly review

**Phase 3 - Per-page Markdown (tháng 5-6):**
- Evaluate effort implement `/index.md` endpoint per page
- Pilot với 3-5 high-traffic pages
- Rollout nếu crawler data tích cực

**Phase 4 - Advanced (tháng 7+):**
- `llms-ctx.txt` pattern: XML-based, optimize per AI platform
- Auto-generate từ CMS publish hook thay vì manual CI/CD
- Internal tooling để validate files trước khi deploy

### 12.3 Quyết định scale investment sau 6 tháng

Review 3 signals:

**Signal 1 - AI crawler activity:** Server logs cho thấy AI search crawlers fetch với tần suất tăng dần → tiếp tục invest.

**Signal 2 - AI referral traffic:** GA4 cho thấy sessions từ AI platforms tăng vs baseline → correlation positive, tiếp tục invest.

**Signal 3 - Citation quality:** Monthly test cho thấy AI describe MoMo chính xác hơn → content đang có effect, tiếp tục maintain.

Nếu sau 6 tháng cả 3 signals đều flat → giữ maintenance tối thiểu, không invest thêm cho đến khi AI platforms chính thức confirm support.

---

*Living document - update khi có thay đổi về standard, product, hoặc learnings từ monitoring.*

*Web Platform · GPD | momo.vn | Văn Hi- **Master Strategy:** [[mospark_master]]

---

## Change Log
- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.


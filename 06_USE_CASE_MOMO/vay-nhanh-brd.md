# BRD: Vay Nhanh

> - **Dự án:** Vay Nhanh Web Growth & Conversion Platform
> - **URL chính:** momo.vn/vay-nhanh
> - **Khối phụ trách:** FS (Financial Services) - Loan
> - **Phiên bản:** 1.2 · Tháng 7/2026
> - **Trạng thái:** In Progress - Execution Phase (Updated Media Team Plan)

---

## Executive Summary

**Situation:** Vay Nhanh (momo.vn/vay-nhanh) là sản phẩm tín dụng tiêu dùng không thế chấp cốt lõi của MoMo, hoạt động trên nền lending license qua đối tác MCash. Web channel đang có nền tảng nhất định: Q1/2026 ghi nhận 70.533 clicks từ GSC, 2.64M impressions, ranking top 2-3 cho hầu hết head terms chính. Thị trường search lending tại Việt Nam đạt 4.22M searches/tháng - MoMo có thể tiếp cận 3.22M vol sau khi loại trừ ngân hàng, CTTC và noise.

**Complication:** Web channel đang underperform so với potential: traffic giảm từ đỉnh 159K views/tháng (Jun 2024) xuống 47K (Jan 2026), CTR sụt từ 5.73% (Jan 2025) xuống 2.74% (Jan 2026). Ba nguyên nhân chính: (1) AI Overview cannibalization từ Q2/2025 - click giảm dù impression ổn định; (2) Content stagnation - không có sub-pages theo segment, MoMo chỉ defend bằng domain authority; (3) Competitor đầu tư content sub-pages nhiều hơn trong 12 tháng qua. MoMo hiện chỉ capture ~2.2% của 3.22M addressable pool.

**Resolution:** Dự án có hai mục tiêu song song: (1) **SEO/GEO Recovery** - đạt Top 1 cho 10 head terms trước EOY 2026, expand sang 12 sub-pages mid-tail targeting segment-specific intent; (2) **PLG Conversion** - revamp Simulator thành conversion engine thực sự với amortization schedule và Onelink deep link truyền context từ web vào app. Thành công đo bằng Clicks từ 70.533 → 98.908 (Q4/2026), CTR từ 2.66% → 3.61%, và Web-to-App Onelink click rate ≥ 15% của sessions.

---

## 1. Bối Cảnh Thị Trường

### 1.1 Traffic Decline Analysis

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Period</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Monthly Views</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CTR (GSC)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Clicks (GSC)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhận xét</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jun 2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">159.454 (peak)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đỉnh lịch sử</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jan 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">91.860</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5.73%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">33.249</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vẫn healthy</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jun 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">68.992</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.84%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24.919</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giảm mạnh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dec 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">44.785</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.42%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21.956</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tiếp tục giảm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jan 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">47.140</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.74%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24.753</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Baseline hiện tại</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Q1/2026</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>~47K avg</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2.66%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>70.533</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Baseline KPI</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Q4/2026 Target</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3.61%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>98.908</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>+40.2%</strong></td>
    </tr>
  </tbody>
</table>

**Key observation:** Click-to-App (~42% of Traffic trong 2025) là tỷ lệ ổn định - vấn đề cốt lõi là **Traffic đang giảm**, không phải Conversion đang giảm. Chiến lược đúng: recover Traffic trước (SEO/content), optimize Conversion sau (Simulator UX).

**Hypothesis 3 nguyên nhân Traffic decline:**
1. **AI Overview cannibalization:** Từ May/2025 Google AIO tăng mạnh tại VN - CTR giảm từ 5.73% → 2.74% trong 12 tháng là signal rõ của AIO.
2. **Content stagnation:** Không có content mới, không có sub-pages - MoMo defend bằng domain authority, không có content moat.
3. **Competitor content investment:** FE Credit, Home Credit, Doctordong đầu tư content sub-pages nhiều hơn trong 12 tháng qua.

### 1.2 Market Demand (từ Research 11.345 keywords)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoMo Fit</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay (core)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.132.450</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Direct</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub + sub-pages</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ứng dụng cho vay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">805.870</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Comparison</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog comparison</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay ngân hàng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">521.950</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Partial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog only</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nợ xấu / CIC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">326.600</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog CIC education</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Công ty cho vay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">208.020</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Competitor</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Skip</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Định nghĩa + FAQ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">160.510</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TOFU/GEO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog + FAQ schema</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lãi suất vay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">90.850</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Calculator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator SEO</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo branded</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">46.940</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Navigational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub defend</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Total</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>4.218.610</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MoMo addressable</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3.223.170</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loại NH, CTTC, noise</td>
    </tr>
  </tbody>
</table>

**Critical finding - Nợ xấu cluster:** Tổng 326.600 vol nhưng 63% là informational (check CIC, kiểm tra nợ xấu). Chỉ ~3% là transactional intent. Không build landing page vay ở cluster này - chỉ blog CIC education.

**Volume distribution → sub-page strategy:**
- 46 head keywords = 1.548.700 vol (48%) - priority số 1
- 496 mid-tail (1K-10K) = 1.296.200 vol - 12 sub-pages + blog
- 8.305 long tail (<100 vol) - programmatic SEO, chưa ưu tiên

### 1.3 Competitive Landscape

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Competitor</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Brand vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm mạnh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cơ hội MoMo khai thác</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Home Credit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">159.490</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Network, brand lớn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">UX tệ, site chậm, content heavy</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Doctordong</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">128.940</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Digital-native, UX tốt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có hệ sinh thái app rộng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FE Credit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">98.790</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Volume content, 100+ landing pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobile kém, không có super-app</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Asset Credit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">67.510</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lãi suất cạnh tranh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand nhỏ</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MoMo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>65.240</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Super-app, 31M users, brand trust cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand vol vay chỉ bằng 1/2 Home Credit</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mcredit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">51.970</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Agri/rural network</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Digital yếu</td>
    </tr>
  </tbody>
</table>

**MoMo chỉ cover 6% market share về Brand search** trong ngành vay - structural gap dài hạn, không giải được bằng SEO content đơn thuần. Cần brand awareness investment song song.

**Ranking baseline (T1/2026) và Target EOY:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keyword</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Position T1/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target EOY 2026</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">165.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">110.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay online nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">40.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay nhanh online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">22.200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền online nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền mặt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay trả góp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1</td>
    </tr>
  </tbody>
</table>

### 1.4 International Benchmark

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Platform</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Market</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Key Learning</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Implication cho MoMo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jiebei (Ant Financial)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">China</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loan offer in-app dựa trên credit score, không cần user apply</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web page nên focus vào "kiểm tra hạn mức" thay vì "apply vay" - lower commitment CTA</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Klarna</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">EU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loan calculator chiếm 50% viewport above fold; APR minh bạch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator phải hiển thị tổng tiền trả và tổng lãi rõ ràng - transparency = trust</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kredivo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Indonesia</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Calculator embedded in hero, không cần scroll</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator phải visible ở fold 1 trên mobile - điểm quan trọng nhất hiện đang thiếu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tonik Bank</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Philippines</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Result card design nổi bật; comparison table vs traditional bank</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Result card design quan trọng hơn input form</td>
    </tr>
  </tbody>
</table>

---

## 2. Định Hướng Dự Án

### Dự án phục vụ điều gì?

Hai mục tiêu song song, không tách rời:

1. **SEO/GEO Recovery:** Recover và vượt ranking - Top 1 cho 10 head terms trước EOY 2026, expand sang 12 sub-pages mid-tail.
2. **PLG Conversion:** Revamp Simulator thành conversion engine thực sự - truyền context từ web vào app qua Onelink, giảm friction Web-to-App.

### Ai được phục vụ?

**Segment 1 - Emergency Borrower (BOFU · High urgency):**
Freelancer / công nhân / hộ kinh doanh nhỏ 25-40 tuổi, cần tiền trong ngày. Bị push bởi: ngân hàng hẹn 3-5 ngày, vay người thân ngại, app khác không tin tưởng. Pull bởi: duyệt 5 phút, chỉ cần CCCD, giải ngân vào ví ngay. Anxiety chính: lãi suất thực sự bao nhiêu, có bị lộ data không.

**Segment 2 - Comparison Researcher (MOFU):**
28-45 tuổi, thu nhập ổn định, đang cân nhắc vay tiêu dùng, search Google để research. Anxiety cao nhất: "2.72%/tháng flat rate nghĩa là gì? Tổng tôi trả bao nhiêu?"

**Segment 3 - Rejected Borrower / CIC Concerned (MOFU · Sensitive):**
Đã bị ngân hàng từ chối hoặc lo ngại về CIC score. Cần lựa chọn uy tín khi không đủ điều kiện ngân hàng. **YMYL red line:** Không claim "bỏ qua CIC" hay "hỗ trợ nợ xấu" nếu MoMo vẫn check CIC.

**Segment 4 - First-time Digital Borrower (TOFU):**
Lần đầu nghĩ đến vay online, chưa có kinh nghiệm. Pull bởi: MoMo brand quen từ thanh toán, App Store rating tốt, 31M users social proof.

### Dự án này KHÔNG phải là gì?

- KHÔNG cover loan underwriting decisions và credit policy - BU Credit team.
- KHÔNG cover App UX flow sau khi user click Onelink - App Product Owner.
- KHÔNG quản lý SEM campaign cho vay nhanh keywords - Media team.
- KHÔNG cover pricing và interest rate decisions - BU/Finance.
- KHÔNG cover paid influencer hoặc TikTok content - BMC.

---

## 3. JTBD Analysis

### Job #VN-01 - Vay Khẩn Cấp (Urgency Borrower)

> "Khi tôi cần tiền gấp, tôi muốn vay online uy tín không cần đến ngân hàng, để giải quyết vấn đề ngay hôm nay."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Functional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hoàn tất apply và nhận tiền trong ngày, chỉ cần CCCD, không phải đến chi nhánh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Emotional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không stress khi gấp tiền, tự giải quyết được vấn đề, không phải xin tiền ai</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Social</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giữ được hình ảnh tự chủ tài chính, không ai biết mình cần tiền gấp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trigger</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chi phí y tế đột xuất · Sửa xe · Tiền nhà cuối tháng · Cơ hội kinh doanh ngắn hạn</td>
    </tr>
  </tbody>
</table>

**Serve bằng:** Hub page với Simulator fold 1, friction tối thiểu, CTA "Vay ngay" · /vay-nhanh/khan-cap

### Job #VN-02 - Nghiên cứu Trước Khi Vay (Comparison Researcher)

> "Khi tôi đang cân nhắc vay, tôi muốn hiểu rõ lãi suất và so sánh các lựa chọn, để ra quyết định mà không bị lừa."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Functional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tính được tổng chi phí thực sự, so sánh các lựa chọn, hiểu rõ điều kiện</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Emotional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">An tâm rằng mình chọn thông minh, không bị lừa bởi lãi suất ẩn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Social</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Là người tiêu dùng thông minh, biết quản lý tài chính</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trigger</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấy quảng cáo vay nhưng nghi ngờ · Cần vay số tiền lớn · Đang compare nhiều options</td>
    </tr>
  </tbody>
</table>

**Serve bằng:** Simulator với amortization schedule · Blog "Lãi suất vay tiêu dùng tính thế nào" · /vay-nhanh/tinh-lai

### Job #VN-03 - Tìm Lựa Chọn Khi Bị Từ Chối (Rejected Borrower)

> "Khi tôi không đủ điều kiện vay ngân hàng, tôi muốn biết còn lựa chọn uy tín nào, để vay mà không bị lợi dụng."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Functional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm được giải pháp vay không yêu cầu CIC sạch hoặc thu nhập cố định</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Emotional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cảm thấy vẫn có lựa chọn, không bị loại trừ, không bị lợi dụng khi đang khó</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Social</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Muốn giải quyết kín đáo, không để người thân biết</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trigger</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bị ngân hàng từ chối · Không có hợp đồng lao động · Cần tiền nhưng có nợ xấu</td>
    </tr>
  </tbody>
</table>

**Serve bằng:** Blog CIC education (không phải landing page vay) · CTA sang tra cứu CIC trong app

### Job #VN-04 - Tìm Hiểu Vay Online Lần Đầu (First-time Borrower)

> "Khi tôi lần đầu muốn vay online, tôi muốn hiểu quy trình và trust platform, để vay mà không lo rủi ro."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Functional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiểu quy trình vay, biết cần chuẩn bị gì, tin được platform</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Emotional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">An tâm về bảo mật thông tin, không sợ bị lừa đảo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Social</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Muốn được tư vấn như người dùng lần đầu, không bị phán xét</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trigger</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lần đầu nghe đến vay app · Bạn bè đã dùng giới thiệu · Thấy quảng cáo MoMo</td>
    </tr>
  </tbody>
</table>

**Serve bằng:** Blog "App vay tiền online uy tín 2026" → internal link về hub page

---

## 4. Kiến Trúc & Scope Build

### 4.1 URL Architecture

**Hub:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Content Type</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">165.000+</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pillar Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Anchor toàn bộ cluster, Simulator fold 1</td>
    </tr>
  </tbody>
</table>

**Sub-pages - Đợt 1 (ưu tiên cao):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Segment</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/chi-can-cmnd</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emergency + Underbanked</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">USP rõ nhất của MoMo</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/khan-cap</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~8.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emergency</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU urgency</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/tieu-dung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.900</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Comparison</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay tiêu dùng segment</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/tinh-lai</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator SEO standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #VN-02</td>
    </tr>
  </tbody>
</table>

**Sub-pages - Đợt 2:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Segment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/sinh-vien</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~9.200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Student</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/cong-nhan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~9.600</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blue-collar worker</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/freelancer</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~5.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Freelancer</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/5-trieu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~3.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Small amount</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/dieu-kien</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Eligibility info</td>
    </tr>
  </tbody>
</table>

**Blog cluster:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">JTBD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/cic-la-gi-kiem-tra-no-xau</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21K+15K+13K cluster</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #VN-03</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/lai-suat-vay-tieu-dung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">90.000 cluster</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #VN-02</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/app-vay-tien-online-uy-tin</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~18.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational/Comparison</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #VN-04</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/vay-tin-chap-la-gi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">11.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #VN-04</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/tat-toan-la-gi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational/GEO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #VN-02</td>
    </tr>
  </tbody>
</table>

**Loại khỏi scope:** /vay-nhanh/30-trieu, /50-trieu (vol < 900 riêng lẻ); /vay-nhanh/ho-tro-no-xau (YMYL risk, không phù hợp positioning).

### 4.2 PLG Tool - Simulator v2 Requirements

Simulator là conversion engine cốt lõi - cần revamp từ công cụ tính cơ bản thành trải nghiệm tư vấn tài chính.

**Vấn đề hiện tại:** Tính toán cơ bản, không có amortization, không truyền context qua Onelink, không visible ở fold 1 trên mobile.

**Yêu cầu Simulator v2:**
- Input: Slider số tiền vay (6M-100M VNĐ) + quick-select chips; Lựa chọn kỳ hạn (6/9/12/15/18/24 tháng)
- Logic: Flat rate 2.72%/tháng (hiển thị disclaimer); Amortization schedule (reducing balance method)
- Output - Result Card: Tiền trả mỗi tháng (dominant); Tương đương X.XXXđ/ngày; Tổng tiền trả / Tổng tiền lãi; CTA → Onelink với full context (số tiền + kỳ hạn + UTM)
- Output - Amortization Table: Collapsible toggle; Từng tháng: Trả gốc / Tiền lãi / Tổng trả / Dư nợ
- Pre-fill theo sub-page: /vay-nhanh → 20tr/18th; /khan-cap → 10tr/6th; /sinh-vien → 6tr/15th; /cong-nhan → 10tr/12th
- **Mobile requirement (hard gate):** Simulator visible hoàn toàn ở fold 1 trên viewport < 600px. Đây là blocker - không launch nếu không đạt.

### 4.3 Deeplink & Attribution Architecture

**Onelink setup:** Mỗi CTA từ web → app truyền đủ context: số tiền, kỳ hạn, source page, UTM campaign. Fallback: App Store (new user) / mở in-app VayNhanh feature (existing user) / QR code (desktop).

**GA4 Events cần setup:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Event</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">simulator_interaction</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User thay đổi số tiền hoặc kỳ hạn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">amortization_expanded</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User mở bảng amortization</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">onelink_click</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User click CTA → Onelink (kèm amount, term, page)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sticky_cta_click</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click sticky bar mobile</td>
    </tr>
  </tbody>
</table>

### 4.5 Content Strategy

**4 Content Pillars:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pillar</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pages</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">JTBD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional Landing Pages (BOFU)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vay nhanh" core cluster (165K+ vol)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub + /chi-can-cmnd + /khan-cap</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Segment Pages (MOFU)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Audience + purpose mid-tail</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/sinh-vien, /cong-nhan, /freelancer, /tieu-dung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #1, #2</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Financial Education Blog (TOFU)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational clusters</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CIC, lãi suất, app comparison, tất toán</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Job #3, #4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO/AEO Structured Answers</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Overview, ChatGPT, Gemini citation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ answers ≤ 2 paragraphs, standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">All Jobs</td>
    </tr>
  </tbody>
</table>

**GEO - Target Queries:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target Query</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vay tiền online uy tín ở đâu 2026"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~18K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"lãi suất vay MoMo bao nhiêu"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~5K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q2/2026</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vay MoMo cần điều kiện gì"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~3K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q2/2026</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"CIC là gì"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vay tín chấp là gì"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">18.1K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
    </tr>
  </tbody>
</table>

**GEO Answer format mẫu - "Lãi suất vay MoMo bao nhiêu?":**
> "Lãi suất Vay Nhanh MoMo tham khảo là 2.72%/tháng tính theo phương pháp flat rate - nghĩa là lãi được tính trên số tiền gốc ban đầu suốt kỳ vay. Mức lãi suất thực tế phụ thuộc vào lịch sử giao dịch MoMo và hồ sơ tín dụng của từng khách hàng. Ví dụ: vay 20 triệu đồng trong 18 tháng, tổng tiền lãi ước tính khoảng 9.8 triệu đồng."

### 4.6 YMYL Content Gates

Bắt buộc với mọi page Vay Nhanh trước publish:

- LoanProduct schema với đầy đủ fields, validate Rich Results Test (0 errors)
- FAQPage schema cho FAQ section
- Disclaimer lãi suất tham khảo + ghi nguồn
- NHNN license reference (hoặc MCash lending entity)
- Ngày publish + ngày cập nhật hiển thị
- Không claim "không CIC" / "bỏ qua nợ xấu" khi thực tế vẫn check
- Simulator visible fold 1 trên mobile (viewport < 600px)
- Onelink CTA có amount + term + UTM
- FAQ answers standalone (không dùng "như đề cập ở trên")
- FAQ primary match PAA phrasing từ SERP thực

### 4.7 Off-page Strategy

**Approach:** Duy trì textlink homepage trên 2 báo lớn (DA ≥ 60); bổ sung PR articles khi launch sub-pages đợt 1. Ưu tiên anchor text đa dạng (không all "vay nhanh") để tránh penalty. Coordinate với SEM - deploy backlink đồng thời với SEM campaign để maximize SOV.

**Existing backlinks đã live (2025):** tienphong.vn · kinhtedothi.vn · vietnambiz.vn · thuonghieucongluan.com.vn · thethaovanhoa.vn · tuoitrexahoi.vn · baolamdong.vn · nghean24h.vn · baothanhhoa.vn · vietnammoi.vn

### 4.8 Cross-sell & Ecosystem Map

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trigger</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cross-sell</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rationale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator kết quả < 5 triệu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Suggest Ví Trả Sau (BNPL alternative, không lãi đến 45 ngày)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Amount nhỏ phù hợp VTS hơn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator kết quả > 50 triệu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Disclaimer: xem xét Vay Ngân Hàng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Honest UX, không push ngoài khả năng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog CIC education</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA: Tra Cứu CIC trong app (không push vay)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User chưa sẵn sàng convert</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/lai-suat-vay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal link → /vay-nhanh/tinh-lai → Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Funnel dẫn đến Simulator</td>
    </tr>
  </tbody>
</table>

---

## 5. Success Metrics

### 5.1 North Star Metric

**Web-to-App Activated Users từ Organic** - Số user đến web, interact với Simulator, bấm Onelink và activate vay trong app. Đo qua Onelink clicks (GA4) được attributed từ momo.vn/vay-nhanh/*.

### 5.2 Organic Performance (GSC)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Q1/2026 Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Q4/2026 Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tracking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Clicks/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">70.533</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>98.908</strong> (+40.2%)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC CTR</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.66%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3.61%</strong> (+0.95pp)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Impressions/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.648.592</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2.738.777</strong> (+3.4%)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top 1 cho head terms</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0/10 keywords</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>10/10</strong> EOY 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC / Ahrefs</td>
    </tr>
  </tbody>
</table>

**Target logic:** Head terms cluster ~560K vol/tháng hiện ở #2-3 - cần content depth + E-E-A-T + backlink investment để push lên #1. "Vay online" (#6) và "vay trả góp" (#25) cần effort lớn nhất.

### 5.3 Web-to-App Conversion

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timeframe</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tracking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator interaction rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>40% sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 events</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Onelink click rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≥ 15% sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 events</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click-to-App rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~42% of Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Recover 45%+</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q4/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer</td>
    </tr>
  </tbody>
</table>

### 5.4 Content Scale

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timeframe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sub-pages live</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12 sub-pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q3/2026</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog posts live</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~3-5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15+ bài</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q4/2026</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO citation cho target queries</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5+ queries cited</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Q4/2026</td>
    </tr>
  </tbody>
</table>

---

## 6. Dependencies & Constraints

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dependency</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Blocker?</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform - Simulator v2 build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Revamp Simulator: amortization + Onelink deep link + mobile fold 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pending sprint</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU Credit - Onelink template & loan rate config</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Confirm Onelink template ID, rate config dynamic vs static</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần confirm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DA Team - GA4 events + Appsflyer setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Events: simulator_interaction, onelink_click; Appsflyer VN activation mapping</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần setup trước launch</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU/Legal - Content YMYL approval</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Duyệt sub-pages và blog YMYL trước publish. Cần SLA rõ (5-7 ngày/bài)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có SLA</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform - Blog CMS platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Confirm CMS platform cho blog layer (current vs Next.js standalone)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pending</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team team - Blog 15+ bài</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Viết theo keyword brief, qua BU/Legal duyệt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phụ thuộc capacity + Legal SLA</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Off-page campaign</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Backlink deployment coordinate với sub-page launch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Planning</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM Team - Campaign phối hợp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deploy SEM đồng thời với backlink push để maximize SOV</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phối hợp theo phase</td>
    </tr>
  </tbody>
</table>

**Constraints:**
- Mọi content tài chính phải qua Legal review trước publish (YMYL compliance).
- Media Team không làm việc trực tiếp với Web Platform - mọi request kỹ thuật qua Web Product Lead.
- Simulator rate không hardcode - phải lấy từ config để update khi BU thay đổi.
- URL structure giữ nguyên momo.vn - không thay đổi domain/subdomain.

---

## 7. Risk Assessment

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Impact</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Overview tiếp tục cannibalize clicks dù rank #1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Market</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Build GEO layer song song - capture AIO citation thay vì chống lại</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform sprint không available Q2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Execution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Escalate sớm nếu không có resource; Simulator là critical path</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU/Legal approval delay sub-page content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Execution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Establish SLA sớm, brief format chuẩn để tăng tốc review</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lãi suất MoMo thay đổi - hardcode trong Simulator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Technical</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Simulator lấy rate từ config, không hardcode</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo brand vol vay vẫn thấp vs competitor</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Market</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand awareness là long-term play, không giải được bằng SEO - acknowledge trong KPI</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTR tiếp tục giảm dù impressions tăng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Market</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Title tag A/B test; Rich snippet optimization; FAQPage structured snippet</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Onelink tracking không setup kịp → mất data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không launch sub-pages nếu tracking chưa có - data loss không phục hồi</td>
    </tr>
  </tbody>
</table>

---

## Appendix A: Keyword Priority Matrix (Top 25)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keyword</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Position (T1/2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">165.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">110.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền online chuyển khoản ngay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">49.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay online nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">40.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền góp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay trả góp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay nhanh momo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">22.200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Navigational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền nhanh chỉ cần cmnd</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/chi-can-cmnd</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">cic là gì</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/cic-la-gi</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay nhanh online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">22.200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">app vay tiền online uy tín</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">18.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/app-vay-tien-uy-tin</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tín chấp là gì</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">11.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/vay-tin-chap-la-gi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiêu dùng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.900</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/tieu-dung</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tất toán là gì</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/tat-toan-la-gi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay công nhân</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9.600</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/cong-nhan</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay sinh viên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4.400</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/sinh-vien</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">công thức tính lãi kép</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/lai-suat-vay + Simulator</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">kiểm tra nợ xấu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">13.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/cic-la-gi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">check cic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/cic-la-gi</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay nhanh 500k</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/5-trieu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vay tiền app</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">18.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/app-vay-tien-uy-tin</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tính lãi suất vay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.400</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/vay-nhanh/tinh-lai</td>
    </tr>
  </tbody>
</table>

---

## Appendix B: Traffic & KPI History

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Period</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Traffic (Views)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Click to App</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CTR (GSC)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Clicks (GSC)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jan 2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">75.757</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">37.194</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Apr 2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">145.943</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">49.258</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jun 2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>159.454</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>52.404</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dec 2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">116.672</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">37.676</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5.47%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">37.099</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jan 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">91.860</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">33.655</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>5.73%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">33.249</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jun 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">68.992</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24.341</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.84%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24.919</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dec 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">44.785</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">17.932</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.42%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21.956</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jan 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">47.140</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">19.770</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.74%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24.753</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Feb 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">32.263</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">13.905</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.31%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">18.312</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Q1/2026</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>~47K avg</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>~18K avg</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2.66%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>70.533</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Q4/2026 Target</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3.61%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>98.908</strong></td>
    </tr>
  </tbody>
</table>

---

## Change Log
- **Tháng 7/2026 (v1.2):** Cập nhật vai trò Media Team phụ trách chính (incharge chính) và các định hướng tối ưu SEO Onpage/Technical/Content/Offpage từ tài liệu Media Team Plan 2026 (tối ưu slider review, đẩy long content lên trước blog, bổ sung các schema LoanOrCredit/FAQPage/BreadcrumbList/Organization, chuẩn hóa E-E-A-T tác giả YMYL, bổ sung dẫn luật/thông tư NHNN, disavow spam link và đa dạng hóa anchor text backlink).
- **Tháng 4/2026 (v1.0):** Khởi tạo tài liệu - keyword research, competitive analysis, Simulator spec, sub-page architecture.
- **Tháng 5/2026 (v1.1):** Chuẩn hóa tài liệu - loại bỏ thông tin vận hành, tên nhân sự, code blocks kỹ thuật, budget cụ thể; chuẩn bị cho Head of BU / C-Level review.

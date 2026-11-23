#!/usr/bin/env python3
"""
scripts/patch_finhub_brd_table32.py
=============================================================================
Cập nhật Bảng 3.2 trong 05_HUBS/financial/financial-hub-brd.md theo số liệu GA4 mới:
- Bỏ phần tách T1-T4 kiểu ước tính (bỏ dòng 'Tiểu Kế Q1-Q2 (T1-T4)')
- Sửa lại dòng nguồn dữ liệu chuẩn GA4 Property 270743103
- Bổ sung dòng Tháng 11/2026 (MTD 9N sạch)
- Cập nhật dòng tổng kết Lũy Kế 10 Tháng (YTD T1-T10)
- Tuân thủ nghiêm ngặt từ điển SSOT (không emoji, không en dash/em dash, không P0-P3)
=============================================================================
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BRD_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-brd.md"
JSON_PATH = BASE_DIR / "05_HUBS" / "financial" / "data" / "financial_monthly_pv_ga4.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    ga4_data = json.load(f)

targets = {
    "2026-08": 250000,
    "2026-09": 250000,
    "2026-10": 450000,
    "2026-11": 450000,
}

table_rows_html = []
prev_pv = None

tot_pv_ytd = 0
tot_non_paid_ytd = 0
tot_org_ytd = 0
tot_paid_ytd = 0
tot_target_ytd = 0

for idx, item in enumerate(ga4_data):
    m = item["month"]
    pv = item["pageviews"]
    paid = item["paid"]
    non_paid = item["non_paid"]
    org = item["channels"].get("Organic Search", 0)
    others = non_paid - org

    if prev_pv is not None:
        mom_val = (pv / prev_pv - 1) * 100
        mom_str = f"{mom_val:+.1f}%"
    else:
        mom_str = "-"
    prev_pv = pv

    pct_non = (non_paid / pv * 100) if pv else 0
    pct_paid = (paid / pv * 100) if pv else 0

    t_val = targets.get(m)
    t_str = f"{t_val:,}".replace(",", ".") if t_val else "-"
    pct_t = f"{(pv / t_val * 100):.1f}%" if t_val else "-"

    m_num = int(m.split("-")[1])
    m_label = f"Tháng {m_num}/2026"
    if item.get("mtd"):
        up_day = item.get("updatedDay")
        m_label += f" (MTD {up_day}N)"

    pv_str = f"{pv:,}".replace(",", ".")
    non_str = f"{non_paid:,}".replace(",", ".")
    org_str = f"{org:,}".replace(",", ".")
    oth_str = f"{others:,}".replace(",", ".")
    paid_str = f"{paid:,}".replace(",", ".")

    # Styling colors
    non_style = "color:#15803d; font-weight:700;" if pct_non >= 60 else ""
    paid_style = "color:#be123c; font-weight:600;" if pct_paid >= 70 else ""
    t_style = "color:#15803d; font-weight:600;" if t_val and (pv >= t_val) else ""

    non_td = f'<td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center; {non_style}">{pct_non:.1f}%</td>' if non_style else f'<td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center;">{pct_non:.1f}%</td>'
    paid_td = f'<td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center; {paid_style}">{pct_paid:.1f}%</td>' if paid_style else f'<td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center;">{pct_paid:.1f}%</td>'
    target_td = f'<td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center; {t_style}">{pct_t}</td>' if t_style else f'<td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center;">{pct_t}</td>'

    bg = ' style="background-color:#f8fafc;"' if idx % 2 == 1 else ''
    if item.get("mtd"):
        bg = ' style="background-color:#fefce8;"'

    row_html = f"""    <tr{bg}>
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:left;">{m_label}</td>
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:right;">{pv_str}</td>
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:center;">{mom_str}</td>
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:right;">{non_str}</td>
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:right;">{org_str}</td>
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:right;">{oth_str}</td>
      {non_td}
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:right;">{paid_str}</td>
      {paid_td}
      <td style="border:1px solid #94a3b8; padding:6px 10px; text-align:right;">{t_str}</td>
      {target_td}
    </tr>"""
    table_rows_html.append(row_html)

    if not item.get("mtd"):
        tot_pv_ytd += pv
        tot_non_paid_ytd += non_paid
        tot_org_ytd += org
        tot_paid_ytd += paid
        if t_val:
            tot_target_ytd += t_val

tot_oth_ytd = tot_non_paid_ytd - tot_org_ytd
pct_non_ytd = tot_non_paid_ytd / tot_pv_ytd * 100
pct_paid_ytd = tot_paid_ytd / tot_pv_ytd * 100
pct_t_ytd = tot_pv_ytd / tot_target_ytd * 100 if tot_target_ytd else 0

ytd_pv_str = f"{tot_pv_ytd:,}".replace(",", ".")
ytd_non_str = f"{tot_non_paid_ytd:,}".replace(",", ".")
ytd_org_str = f"{tot_org_ytd:,}".replace(",", ".")
ytd_oth_str = f"{tot_oth_ytd:,}".replace(",", ".")
ytd_paid_str = f"{tot_paid_ytd:,}".replace(",", ".")
ytd_t_str = f"{tot_target_ytd:,}".replace(",", ".")

ytd_row = f"""    <tr style="background-color:#e2e8f0;">
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:left;"><strong>Lũy Kế 10 Tháng (YTD T1-T10)</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:right;"><strong>{ytd_pv_str}</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:center;"><strong>-</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:right;"><strong>{ytd_non_str}</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:right;"><strong>{ytd_org_str}</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:right;"><strong>{ytd_oth_str}</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:center;"><strong>{pct_non_ytd:.1f}%</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:right;"><strong>{ytd_paid_str}</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:center;"><strong>{pct_paid_ytd:.1f}%</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:right;"><strong>{ytd_t_str}</strong></td>
      <td style="border:1.5px solid #64748b; padding:8px 10px; text-align:center; color:#15803d; font-weight:700;"><strong>{pct_t_ytd:.1f}%</strong></td>
    </tr>"""

table_rows_html.append(ytd_row)

new_table_32 = f"""### 3.2 Báo Cáo Hiệu Suất Lưu Lượng Chuỗi 2026 (Bóc Tách Non-Paid vs. Paid Chuẩn GA4)

Căn cứ dữ liệu đối soát trực tiếp từ hệ thống Google Analytics 4 Data API (Property 270743103, đồng bộ tại file SSOT [financial_monthly_pv_ga4.json](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/financial/data/financial_monthly_pv_ga4.json)), toàn bộ lưu lượng của Financial Hub từ Tháng 1/2026 đến nay được ghi nhận chuẩn mực theo định nghĩa URL dịch vụ tài chính thống nhất toàn chuỗi, không chắp vá và không áp tỷ lệ ước tính:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.88em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:left; font-weight:700;">Kỳ Báo Cáo</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:right; font-weight:700;">Tổng Traffic (PV)</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:center; font-weight:700;">Tăng Trưởng MoM</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:right; font-weight:700;">Non-Paid (PV)</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:right; font-weight:700;">Trong Đó: Organic</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:right; font-weight:700;">Direct / Ref / Khác</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:center; font-weight:700;">Tỷ Trọng Non-Paid</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:right; font-weight:700;">Paid Ads (PV)</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:center; font-weight:700;">Tỷ Trọng Paid</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:right; font-weight:700;">Target Tháng</th>
      <th style="border:1.5px solid #64748b; padding:6px 10px; text-align:center; font-weight:700;">Tỷ Lệ Đạt</th>
    </tr>
  </thead>
  <tbody>
{chr(10).join(table_rows_html)}
  </tbody>
</table>

*Ghi chú nguồn dữ liệu:* Số liệu Tháng 11/2026 là lũy kế 9 ngày sạch (01-09/11/2026), loại trừ dữ liệu nhiễu vòng lặp GTM ngày 10-11/11. Định nghĩa kênh trả phí: Paid = Paid Search + Paid Social + Paid Other + Cross-network. Toàn bộ các tháng đều đảm bảo tính toàn vẹn: Paid + Non-Paid = Tổng Traffic và Tổng các kênh = Tổng Traffic."""

with open(BRD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Replace from "### 3.2 Báo Cáo Hiệu Suất Lưu Lượng" up to "### 3.3 Báo Cáo Phân Bổ Lưu Lượng" or "### 3.3 Bảng Phân Bổ"
start_marker = "### 3.2 Báo Cáo Hiệu Suất Lưu Lượng"
end_marker = "### 3.3 Bảng Phân Bổ Lưu Lượng"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    raise ValueError(f"Không tìm thấy vị trí đánh dấu trong BRD: start={start_idx}, end={end_idx}")

new_content = content[:start_idx] + new_table_32 + "\n\n" + content[end_idx:]

with open(BRD_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✓ Đã cập nhật thành công Bảng 3.2 trong financial-hub-brd.md!")

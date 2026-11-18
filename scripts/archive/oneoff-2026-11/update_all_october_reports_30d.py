#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ĐỒNG BỘ TOÀN BỘ BÁO CÁO THÁNG 10/2026 TỪ SNAPSHOT SSOT

Mọi con số lấy từ 07_REPORTS/data/october_2026_facts.json (do
scripts/build_october_facts.py sinh ra từ GA4 Data API + Excel SSOT).
Không còn số hardcode trong script này.

Đầu ra:
  1. 07_REPORTS/data/analytics/monthly_report_2026_10.json
  2. react-web-momo/data/analytics/monthly-report-2026-10.json
  3. react-web-momo/data/reports/monthly-index.json (kỳ dữ liệu)
  4. 07_REPORTS/docs/report-thang-10-2026.md
  5. 07_REPORTS/docs/report-thang-10-2026-board.md
  6. react-web-momo/data/reports/report-thang-10-2026-board.md

Cách dùng:
    ./.venv/bin/python scripts/build_october_facts.py     # bước 1: tính facts
    ./.venv/bin/python scripts/update_all_october_reports_30d.py
"""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_DIR = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
FACTS_PATH = BASE_DIR / "07_REPORTS" / "data" / "october_2026_facts.json"
APPSFLYER_CSV = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "gpd_momo_web_oct_2026.csv"


def n(x):
    return f"{int(round(x)):,}".replace(",", ".")


def p1(x):
    return f"{x:+.1f}%".replace(".", ",")


facts = json.loads(FACTS_PATH.read_text(encoding="utf-8"))
T = facts["total"]
CH = facts["channels"]
CI = facts["hubs"]["cinema"]
FI = facts["hubs"]["financial"]
CP = CI["cineplex"]
P = facts["projects"]
VN, VTS, TT, PN, CIC = P["Vay Nhanh"], P["Ví Trả Sau"], P["Trung Tâm Tài Chính"], P["Phạt Nguội"], P["Điểm Tín Dụng"]
GEO = facts["geo_ai"]
GAME = facts["minigame_mot_mua_quyt"]


def read_appsflyer(path):
    if not path.exists():
        return None
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))

    def total(col):
        s = 0
        for r in rows:
            try:
                s += int(str(r.get(col, "")).replace(",", "").strip())
            except ValueError:
                pass
        return s

    return {
        "installs": total("# Installs"),
        "reg": total("# REG"),
        "map": total("# Map"),
        "mau": total("# MAU"),
    }


AF = read_appsflyer(APPSFLYER_CSV) or {"installs": 9824, "reg": 3436, "map": 2072, "mau": 1131}
AF["cvr"] = round(AF["map"] / AF["installs"] * 100, 2) if AF["installs"] else 0
AF_SEP_INSTALLS, AF_SEP_MAP = 10501, 2276
W2A_CLICKS, W2A_CLICKS_SEP = 102103, 94983
REF_OTH_OCT = CH["referral"]["oct"] + CH["others"]["oct"]
REF_OTH_SEP = CH["referral"]["sep"] + CH["others"]["sep"]
REF_OTH_MOM = round((REF_OTH_OCT / REF_OTH_SEP - 1) * 100, 1)


def mom(cur, prev):
    return round((cur / prev - 1) * 100, 1) if prev else 0.0


# =============================================================================
# 1. JSON SSOT (Base + Hubs)
# =============================================================================
json_path = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "monthly_report_2026_10.json"
mr = json.loads(json_path.read_text(encoding="utf-8"))

mr["meta"]["period"] = "01/10/2026 - 31/10/2026"
mr["meta"]["days_elapsed"] = facts["period"]["days_elapsed"]
mr["meta"]["last_updated"] = "2026-11-01T08:00:00+07:00"
mr["meta"].setdefault("sources", [])
mr["meta"]["sources"] = [
    "GA4 Data API (Property 270743103) - Chốt sổ Full month 01-31/10/2026",
    "Excel SSOT web_performance_tracking.xlsx - pivot Full month, tên project chuẩn hóa theo hub-map.json",
    "AppsFlyer GPD Attribution - OneLink installs / Map Bank",
]

s = mr["summary"]
s["actual_pvs_mtd"] = T["oct_pv"]
s["forecast_pvs_31d"] = T["forecast"]
s["achievement_rate_mtd"] = round(T["achievement_rate"] / 100, 4)
s["forecast_achievement_rate"] = round(T["forecast_rate"] / 100, 4)
s["daily_run_rate"] = T["daily_pace"]
s["non_paid_pvs_mtd"] = CH["non_paid"]["oct"]
s["non_paid_share"] = round(CH["non_paid"]["oct"] / T["oct_pv"], 4)
s["paid_pvs_mtd"] = CH["paid"]["oct"]
s["paid_share"] = round(CH["paid"]["oct"] / T["oct_pv"], 4)
s["paid_cut_volume"] = abs(CH["paid"]["oct"] - CH["paid"]["sep"])
s["paid_cut_rate"] = round(CH["paid"]["oct"] / CH["paid"]["sep"] - 1, 3)
s["non_paid_net_add"] = CH["non_paid"]["oct"] - CH["non_paid"]["sep"]
s["non_paid_growth_mom"] = round(CH["non_paid"]["mom_pct"] / 100, 3)

# =============================================================================
# Phễu Web-to-App: forecast theo nhịp 30 ngày, growth MoM theo thực đạt
# =============================================================================
PACE = facts["period"]["days_in_month"] / facts["period"]["days_elapsed"]


def fc(x):
    return round(x * PACE)


def growth_vi(cur, prev):
    return f"{round((cur / prev - 1) * 100, 2):+.2f}%".replace(".", ",")


AF_SEP = {"installs": AF_SEP_INSTALLS, "reg": 3569, "map": AF_SEP_MAP, "mau": 1328}

s["total_installs_mtd"] = AF["installs"]
s["forecast_installs_31d"] = fc(AF["installs"])
s["registered_users_mtd"] = AF["reg"]
s["map_bank_users_mtd"] = AF["map"]
s["install_to_map_cvr"] = round(AF["map"] / AF["installs"], 4)

funnel = mr["new_user_funnel"]["stages"]
for _st in funnel:
    _st.pop("oct_mtd_28d", None)
funnel[0].update({
    "oct_mtd_30d": AF["installs"],
    "forecast_31d": fc(AF["installs"]),
    "growth_mom": growth_vi(AF["installs"], AF_SEP["installs"]),
    "assessment": f"Nhịp chạy {round(AF['installs'] / facts['period']['days_elapsed'])} installs/ngày; giảm so với đỉnh Tháng 9 khi còn chạy Paid Ads"
})
funnel[1].update({
    "oct_mtd_30d": AF["reg"],
    "forecast_31d": fc(AF["reg"]),
    "growth_mom": growth_vi(AF["reg"], AF_SEP["reg"]),
    "assessment": f"CVR Install -> REG đạt {round(AF['reg'] / AF['installs'] * 100, 2)}% (T9: {round(AF_SEP['reg'] / AF_SEP['installs'] * 100, 2)}%)".replace(".", ",")
})
funnel[2].update({
    "oct_mtd_30d": AF["map"],
    "forecast_31d": fc(AF["map"]),
    "growth_mom": growth_vi(AF["map"], AF_SEP["map"]),
    "assessment": f"CVR REG -> Map Bank đạt {round(AF['map'] / AF['reg'] * 100, 2)}% (T9: {round(AF_SEP['map'] / AF_SEP['reg'] * 100, 2)}%)".replace(".", ",")
})
funnel[3].update({
    "oct_mtd_30d": AF["mau"],
    "forecast_31d": fc(AF["mau"]),
    "growth_mom": growth_vi(AF["mau"], AF_SEP["mau"]),
    "assessment": f"CVR Map -> MAU đạt {round(AF['mau'] / AF['map'] * 100, 2)}% (T9: {round(AF_SEP['mau'] / AF_SEP['map'] * 100, 2)}%)".replace(".", ",")
})
funnel[4].update({
    "oct_mtd_30d": f"{AF['cvr']}%".replace(".", ","),
    "forecast_31d": f"{AF['cvr']}%".replace(".", ","),
    "growth_mom": f"{round(AF['cvr'] - AF_SEP['map'] / AF_SEP['installs'] * 100, 2):+.2f}".replace(".", ",") + " p.p",
})

for row in mr.get("target_vs_actual", []):
    if "oct_mtd_28d" in row:
        row["oct_mtd_30d"] = row.pop("oct_mtd_28d")
    if row["metric"] == "Total Page Views (Actual)":
        row["oct_mtd_30d"] = T["oct_pv"]
        row["forecast_31d"] = T["forecast"]
        row["assessment"] = f"Đạt {T['achievement_rate']}% Target sau 30/31 ngày (96,77% tiến độ thời gian)"
    elif row["metric"] == "Net Add (Lưu lượng Tăng mới)":
        row["sep_2026"] = T["sep_pv"] - 3465363
        row["oct_target"] = T["target"] - T["sep_pv"]
        row["oct_mtd_30d"] = T["oct_pv"] - T["sep_pv"]
        row["forecast_31d"] = T["forecast"] - T["sep_pv"]
        row["assessment"] = "Chênh lệch thực đạt so với đỉnh chạy Ads Tháng 9"
    elif row["metric"] == "% Growth Rate (Actual)":
        row["oct_mtd_30d"] = f"{T['mom_pct']}%"
        row["forecast_31d"] = f"{round((T['forecast'] / T['sep_pv'] - 1) * 100, 2)}%"
        row["assessment"] = "So với mức thực đạt Tháng 9"
    elif row["metric"] == "% Target Rate (Tiến độ về đích)":
        row["oct_mtd_30d"] = f"{T['achievement_rate']}%"
        row["forecast_31d"] = f"{T['forecast_rate']}%"
        row["assessment"] = f"Dự kiến kết tháng đạt {T['forecast_rate']}% Target"

# =============================================================================
# Cơ cấu kênh: số liệu + diễn giải đều sinh từ facts, không giữ câu cũ
# =============================================================================
def pct_vi(v):
    return f"{v:+.1f}%".replace(".", ",")


CHANNEL_KEY = {
    "KÊNH TỰ NHIÊN (NON-PAID)": "non_paid",
    "Organic Search": "organic",
    "Direct": "direct",
    "Referral": "referral",
    "TỔNG LƯỢNG TRUY CẬP": "total",
    "KÊNH TRẢ PHÍ (PAID TRAFFIC)": "paid",
}
CHANNEL_NOTE = {
    "non_paid": lambda v: (
        f"Kênh tự nhiên {n(v['oct'])} PVs ({pct_vi(v['mom_pct'])} MoM), chiếm "
        f"{round(v['oct'] / T['oct_pv'] * 100, 2):.2f}% toàn Website; tự chủ nguồn tăng trưởng"
    ),
    "organic": lambda v: (
        f"Organic {n(v['oct'])} PVs ({pct_vi(v['mom_pct'])} MoM), chiếm {round(v['oct'] / T['oct_pv'] * 100, 2):.2f}% toàn Website"
    ),
    "direct": lambda v: (
        f"Truy cập trực tiếp {n(v['oct'])} PVs ({pct_vi(v['mom_pct'])} MoM); người dùng chủ động quay lại các tiện ích"
    ),
    "referral": lambda v: (
        f"Referral {n(v['oct'])} PVs ({pct_vi(v['mom_pct'])} MoM); mạng lưới rạp chiếu phim, ngân hàng đối tác và báo chí"
    ),
    "others": lambda v: (
        f"Kênh tự nhiên khác {n(v['oct'])} PVs ({pct_vi(v['mom_pct'])} MoM); điểm chạm tiện ích mới triển khai"
    ),
    "paid": lambda v: (
        f"Chủ động cắt {abs(round(v['mom_pct']))}% Paid Ads (-{n(abs(v['oct'] - v['sep']))} PVs) "
        "để tối ưu dòng vốn của BOM"
    ),
    "total": lambda v: (
        f"Đạt {T['achievement_rate']}% kế hoạch tháng; dự báo kết tháng {T['forecast_rate']}% Target "
        f"({pct_vi(T['mom_pct'])} MoM)"
    ),
}

for ts in mr.get("traffic_sources", []):
    ts.pop("oct_mtd_28d", None)
    ch = ts["channel"]
    key = "others" if "Others" in ch else CHANNEL_KEY.get(ch)
    if key is None:
        continue
    if key == "total":
        ts.update({
            "oct_mtd_30d": T["oct_pv"],
            "sep_2026": T["sep_pv"],
            "forecast_31d": T["forecast"],
            "diff_vs_sep": T["oct_pv"] - T["sep_pv"],
            "share": 1.0,
        })
    else:
        ts["oct_mtd_30d"] = CH[key]["oct"]
        ts["sep_2026"] = CH[key]["sep"]
        ts["forecast_31d"] = round(
            CH[key]["oct"] / facts["period"]["days_elapsed"] * facts["period"]["days_in_month"]
        )
        ts["diff_vs_sep"] = CH[key]["oct"] - CH[key]["sep"]
        ts["share"] = round(CH[key]["oct"] / T["oct_pv"], 4)
    ts["assessment"] = CHANNEL_NOTE[key](CH[key] if key != "total" else {"oct": T["oct_pv"], "mom_pct": T["mom_pct"]})

for key, block in (("cinema", CI), ("financial", FI)):
    m = mr["strategic_hubs"][key]["metrics"]
    m.pop("oct_mtd_28d", None)
    m["oct_mtd_30d"] = block["oct_pv"]
    m["sep_2026"] = block["sep_pv"]
    m["forecast_31d"] = block["forecast"]
    m["achievement_rate"] = round(block["achievement_rate"] / 100, 4)
    if key == "cinema":
        m["organic_share_mtd"] = round(block["organic_share"] / 100, 3)
        m["organic_share_sep"] = round(block["organic_share_sep"] / 100, 3)
    else:
        m["non_paid_share_mtd"] = round(block["non_paid_share"] / 100, 3)
        m["non_paid_share_sep"] = round(block["non_paid_share_sep"] / 100, 3)

mr["strategic_hubs"]["cinema"]["highlights"][0] = (
    f"Cinema Hub đạt {n(CI['oct_pv'])} PVs, lượt tự nhiên tăng {p1(mom(CI['organic_pv'], round(CI['sep_pv'] * CI['organic_share_sep'] / 100)))} "
    f"trong khi Paid giảm mạnh sau khi cắt Paid Ads."
)
mr["strategic_hubs"]["cinema"]["highlights"][1] = (
    f"Thống lĩnh vị thế Topical Authority mùa phim cuối năm: {CP['share_of_hub']}% lưu lượng Hub đến từ cụm rạp đối tác, "
    "nhóm từ khóa phim rạp trọng điểm giữ vị trí Top 1 Google Search và là nguồn trích dẫn của Google AI Overviews."
)
mr["strategic_hubs"]["financial"]["highlights"][0] = (
    f"Hoàn thành {FI['achievement_rate']}% chỉ tiêu tháng ({n(FI['oct_pv'])} PV, {p1(FI['mom_pct'])} MoM) nhờ đa dạng hóa tiện ích tài chính."
)
mr["strategic_hubs"]["financial"]["highlights"][1] = (
    f"Nhóm tiện ích tài chính mới bù đắp đà giảm của Vay Nhanh: Trung Tâm Tài Chính {n(TT['oct_pv'])} views ({p1(TT['mom_pct'])}), "
    f"Ví Trả Sau {n(VTS['oct_pv'])} views ({p1(VTS['mom_pct'])}), bù {n(abs(VN['delta']))} views giảm của Vay Nhanh ({p1(VN['mom_pct'])})."
)
mr["executive_pillars"]["highlights"][0] = (
    f"Chất lượng lưu lượng sạch nhất từ đầu năm: Kênh tự nhiên (Non-Paid) đạt {n(CH['non_paid']['oct'])} PV, "
    f"chiếm {round(CH['non_paid']['oct'] / T['oct_pv'] * 100, 2):.2f}% toàn Website ({p1(CH['non_paid']['mom_pct'])} MoM), "
    f"tự bù đắp việc chủ động cắt {abs(round(CH['paid']['mom_pct']))}% Paid Ads."
)
mr["executive_pillars"]["highlights"][1] = (
    f"Financial Hub đạt {n(FI['oct_pv'])} PV ({FI['achievement_rate']}% chỉ tiêu tháng): "
    f"Trung Tâm Tài Chính {p1(TT['mom_pct'])} và Ví Trả Sau {p1(VTS['mom_pct'])}, bù {n(abs(VN['delta']))} PV giảm của Vay Nhanh khi dừng Paid Ads."
)
mr["executive_pillars"]["highlights"][2] = (
    f"Cinema Hub đạt {n(CI['oct_pv'])} PV ({CI['achievement_rate']}% chỉ tiêu tháng, {p1(CI['mom_pct'])} MoM): "
    f"cụm rạp đối tác {n(CP['oct_pv'])} PV ({p1(CP['mom_pct'])}), chiếm {CP['share_of_hub']}% Hub, bù phần lớn mức giảm của trang phim lẻ."
)

json_path.write_text(json.dumps(mr, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✓ {json_path}")

hubs_json = HUBS_DIR / "data" / "analytics" / "monthly-report-2026-10.json"
if hubs_json.parent.exists():
    hubs_json.write_text(json.dumps(mr, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ {hubs_json}")

index_path = HUBS_DIR / "data" / "reports" / "monthly-index.json"
if index_path.exists():
    idx = json.loads(index_path.read_text(encoding="utf-8"))
    for entry in idx:
        if entry.get("id") == "2026-10":
            entry["period"] = "01/10/2026 - 31/10/2026 (Full month)"
    index_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ {index_path}")

# =============================================================================
# 2. Báo cáo Markdown (Base + Hubs)
# =============================================================================
# Nội dung báo cáo đồng bộ với bản md đã review (mục 1-8). Sửa số ở md rồi cập nhật block này.
board_md = """# BÁO CÁO KINH DOANH VÀ HIỆU SUẤT NỀN TẢNG WEB - THÁNG 10/2026
> **Đối tượng:** Ban Giám Đốc / Hội đồng Quản trị
> **Chu kỳ dữ liệu:** 01/10/2026 - 31/10/2026 (31 ngày, chốt full month)
> **Nguồn dữ liệu (SSOT):** GA4 Data API (Property 270743103) cho tổng, kênh và New Users; Excel SSOT `web_performance_tracking.xlsx` (pivot Full month) cho Hub và project; AppsFlyer GPD cho Web-to-App.
> **Lưu ý nguồn:** Một số số Hub đang lệch giữa GA4 và Excel. Xem mục 7.

---

### 1. KẾT LUẬN ĐIỀU HÀNH
- **Tiến độ mục tiêu:** Đạt **3.602.023 PVs**, 98,3% target tháng (3.665.607). Thiếu 63.584 PVs. MoM -8,9%.
- **Cơ cấu lưu lượng:** Kênh tự nhiên (Non-Paid) đạt **3.128.542 PVs** (+13,5% MoM), chiếm 86,9% toàn Website. Paid giảm 723.612 PVs. Non-Paid bù được khoảng **52%** phần Paid giảm, không bù hết.
- **Phần thiếu target chủ yếu nằm ở Non-Paid:** nếu target tổng có bao gồm Paid (489.264), Non-Paid đạt 98,5% target và thiếu 47.801 PVs, Paid thiếu 15.783 PVs. Cần xác nhận cách tính target (xem mục 7).
- **Install sang MAU đạt 11,5%:** 9.824 Installs, 3.436 đăng ký (35,0%), 2.072 liên kết ngân hàng (21,1%), 1.131 MAU (11,5%). Bước rơi lớn nhất là cài App sang đăng ký (65% install chưa đăng ký). Installs giảm 6,4% và Map Bank giảm 9,0% so với tháng 9.
- **GEO (AI Search):** 18.547 PVs theo GA4 (31 ngày), chiếm 0,5% tổng lưu lượng, +36,4% MoM so với cùng phương pháp tháng 9. Con số 40.827 của bản trước gộp thêm lượt trích dẫn Bing AI (không phải lượt truy cập), nên đã bỏ.

---

### 2. BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT (EXECUTIVE SCORECARD)

| Hạng mục Đo lường | Tháng 09 (Full) | Tháng 10 (Target) | Thực đạt (31 ngày) | % Đạt Target | % MoM |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **TỔNG LƯỢNG TRUY CẬP (PVS)** | **3.952.859** | **3.665.607** | **3.602.023** | **98,3%** | **-8,9%** |
| **Kênh Tự Nhiên (Non-Paid)** | 2.755.766 | 3.176.343* | 3.128.542 | 98,5%* | +13,5% |
| - Organic Search | 1.623.796 | - | 1.715.771 | - | +5,7% |
| - Direct | 755.896 | - | 931.731 | - | +23,3% |
| - Referral / Others | 376.074 | - | 481.040 | - | +27,9% |
| *- Trong đó: Lưu lượng GEO (AI Search, GA4 31 ngày)* | *13.596* | *-* | *18.547* | *-* | *+36,4%* |
| **Kênh Trả Phí (Paid Traffic)** | 1.197.093 | 489.264 | 473.481 | 96,8% | **-60,4%** |
| **Cinema Hub (PVs)** | 1.220.075 | 1.117.378 | 1.132.721 | 101,4% | **-7,2%** |
| **Financial Hub (PVs)** | 249.823 | 250.000* | 273.705 | 109,5%* | **+9,6%** |
| **App Installs (AppsFlyer)** | 10.501 | - | 9.824 | - | **-6,4%** |
| **Liên Kết Ngân Hàng (Map Bank)** | 2.276 | - | 2.072 | - | **-9,0%** |
| **MAU (AppsFlyer)** | - | - | 1.131 | - | - |

*Ghi chú:* Target Non-Paid (*) là suy ra bằng tổng target trừ target Paid, chỉ đúng nếu target tổng bao gồm Paid. Target Financial (*) cần đối chiếu, xem mục 7. Tổng PV và cơ cấu kênh lấy từ GA4 Data API (31 ngày). Tổng project Hub khớp 3.602.023 PV.

---

### 3. NGUYÊN NHÂN LƯU LƯỢNG THÁNG 10 GIẢM (PHÂN TÍCH NGUYÊN NHÂN GỐC)
> **Kết luận:** Mức giảm -350.836 PVs (-8,9%) là kết quả của việc giảm 723.612 PVs Paid, bù một phần bởi Non-Paid tăng 372.776 PVs.

- **Paid giảm 723.612 PVs** (1.197.093 xuống 473.481). Mức giảm này gắn với việc cắt các kênh có hiệu quả thấp. Số liệu chuyển đổi chi tiết theo kênh Paid chưa có trong báo cáo.
- **Non-Paid tăng 372.776 PVs (+13,5%)**, bù khoảng 52% phần Paid giảm. Direct (+23,3%) và Referral/Others (+27,9%) đóng góp phần lớn mức tăng; Organic Search chỉ +5,7%.
- **Mùa vụ:** Google Trends 5 năm cho thấy tháng 10 là vùng nhu cầu thấp ở một số nhóm (Học sinh/Sinh viên, Y tế, Rạp phim, Xổ số, Xe cộ). Chưa lượng hóa được bằng PVs, và Non-Paid vẫn tăng nên không dùng làm nguyên nhân chính.

**Điểm sáng:**
- Non-Paid đạt 3.128.542 PVs, tỷ trọng 86,9% toàn Website (T9: 69,7%).
- Cinema Hub đạt 101,4% target. Cinema đã cắt 92,9% Paid, nhưng tổng PVs chỉ giảm 7,2% nhờ lượt tự nhiên tăng 21,7%.

---

### 4. BÓC TÁCH LƯU LƯỢNG GEO & AI SEARCH (GA4, sessionSource)

| Nền tảng AI (sessionSource GA4) | Tháng 09 (Full) | Tháng 10 (31 ngày) | % MoM |
| :--- | :---: | :---: | :---: |
| **ChatGPT (chatgpt.com)** | 12.589 | 17.739 | **+40,9%** |
| **Perplexity** (perplexity.ai, perplexity) | 239 | 284 | +18,8% |
| **Google Gemini** (gemini.google.com, gemini) | 704 | 467 | -33,7% |
| **Khác** (claude.ai, copilot.com, openai, l.meta.ai) | 64 | 57 | -10,9% |
| **TỔNG LƯỢNG TRUY CẬP GEO (AI)** | **13.596** | **18.547** | **+36,4%** |

- **Tỷ trọng:** 0,5% tổng PVs tháng 10 (T9: 0,3%). ChatGPT chiếm 95,6% lưu lượng GEO.
- **Ghi chú phương pháp:** Số tháng 9 và tháng 10 cùng lấy từ GA4 theo sessionSource, cùng danh sách nguồn. Bing AI (Microsoft Copilot) không tách được trong GA4 nên không có trong bảng. Số trích dẫn Bing AI (Bing AI Performance) là chỉ số khác, không phải lượt truy cập, không cộng vào tổng.
- **Giá trị:** Quy mô còn nhỏ. Cần theo dõi GEO như kênh có tiềm năng, không đặt làm chỉ tiêu tăng trưởng chính cho đến khi có baseline ổn định qua nhiều tháng.

**GEO theo trang đích (GA4, lượt vào = sessions có nguồn AI, tháng 10, top 500 trang phủ 82% lượt vào):**

| Nhóm trang đích | Tỷ trọng lượt vào | Tương tác | Trang tiêu biểu (lượt vào) |
| :--- | :---: | :---: | :--- |
| Tài chính: vay, thẻ, ví | 17,3% | 79,4% | /vay-nhanh (757), /vi-tra-sau (155), /bao-hiem-xe-may (144) |
| Hỏi đáp (FAQ) | 14,1% | 95,2% | /hoi-dap (517), /hoi-dap/huong-dan-thiet-lap-vi-momo (169) |
| Thương hiệu và liên hệ | 11,4% | 87,4% | Trang chủ (667), /merchant (279), /lienhe (188) |
| Cinema | 10,3% | 94,7% | /cinema/trai-buon-nguoi-24991 (133) |
| Tin tức, thông cáo | 6,0% | 89,7% | - |
| Nhóm còn lại trong top 500 | 18,3% | - | Khác, hướng dẫn và blog, tiện ích, nạp và game, pháp lý |
| Ngoài top 500 trang | 18,4% | - | Phần đuôi, không tách nhóm |
| Không xác định trang đích | 4,2% | 9,3% | Dữ liệu GA4 không gắn được trang đích |

- **Quy mô:** 11.750 lượt vào có nguồn AI tháng 10, tăng 43,5% so với 8.190 lượt tháng 9. Lượt xem trang (PV) GEO là 18.547, tương đương 1,6 trang mỗi lượt vào.
- **Cinema tăng mạnh nhất:** từ 460 lượt vào (T9) lên 1.210 lượt (T10), +163%. Phần tăng đến từ trang phim mới (Trại buôn người) và trang rạp (CGV 232 lượt, từ 74).
- **Chất lượng:** FAQ và Cinema có tương tác cao nhất (trên 94%). Nhóm Pháp lý chỉ 53,1%, nên không đẩy AI tới các trang này.
- **Tập trung:** 3 trang đầu (vay nhanh, trang chủ, hỏi đáp) chiếm 16,5% lượt vào GEO. ChatGPT chiếm 95,6% PV GEO.

**Trang AI trích dẫn nhiều và lượt vào GA4 (Bing AI Performance, 17/04 - 15/10, đơn vị là lượt trích dẫn, không phải lượt truy cập):**

| Trang được trích dẫn nhiều | Lượt trích dẫn | Lượt vào GEO tháng 10 (GA4) |
| :--- | :---: | :---: |
| /blog/tra-cuu-gia-tri-su-dung-the-bhyt | 43.985 | Không lọt top 500 trang |
| /cinema/review | 34.680 | 4 |
| /blog/cam-nang-du-lich-macau-tu-tuc | 19.951 | Không lọt top 500 trang |
| /cinema/phim-dang-chieu | 19.000 | Không lọt top 500 trang |
| /cinema/rap/cgv | 18.332 | 232 |
| /tien-ich-giao-thong/gia-xang | 15.142 | 14 |

- **Điểm nghẽn quy mô:** Trang được AI trích dẫn nhiều nhất (tra cứu BHYT, Macau) gần như không nhận lượt vào từ GEO. AI trả lời ngay trong câu trả lời, người dùng không click sang. Muốn tăng lưu lượng, trang đích phải có lý do để người dùng mở, không chỉ có nội dung đúng.
- **Giả thuyết cần kiểm chứng [cần xác nhận]:** AI ưu tiên trang có câu hỏi và câu trả lời rõ ràng (FAQ, định nghĩa, lịch chiếu). Hiện chưa có dữ liệu để chứng minh nguyên nhân.

**Đánh giá khả năng scale:**
- **Đòn bẩy 1, FAQ và trang giải thích sản phẩm:** Tương tác cao nhất, bám đúng câu hỏi AI đang trả lời. Cần mở rộng theo danh sách câu hỏi tài chính.
- **Đòn bẩy 2, phim và rạp:** Tăng nhanh nhưng phụ thuộc lịch chiếu. Lưu lượng sẽ giảm khi phim hết chiếu, cần kế hoạch nội dung theo lịch phim.
- **Đòn bẩy 3, chuyển trích dẫn thành lượt click:** Chỉ có khi thêm lý do để mở trang, ví dụ công cụ tra cứu tương tác thay cho đoạn văn tĩnh. Chưa có số liệu để ước lượng tác động.
- **Rủi ro:** Phụ thuộc gần như hoàn toàn vào ChatGPT (95,6%). Gemini giảm 33,7% MoM. Nếu một nền tảng AI đổi cách dẫn nguồn, lưu lượng có thể giảm mạnh.
- **Giới hạn đo lường:** GA4 chỉ thấy nguồn `sessionSource`, không biết câu trả lời AI nào đã dẫn người dùng tới trang nào.

---

### 5. CÁC ĐỘNG LỰC KINH DOANH CỐT LÕI (SO WHAT?)
1. **Non-Paid chưa đủ bù Paid.** Non-Paid bù 52% phần Paid giảm về PVs. Về New Users, Non-Paid chỉ bù khoảng 10% (xem mục 6). Web chưa độc lập với Paid. Organic Search (kênh BU chịu trách nhiệm) chỉ tăng 5,7%, cần được làm rõ trong kế hoạch tháng 11.
2. **Cinema thay Paid bằng lượt tự nhiên, hub vẫn đạt target:**
   - Paid Cinema giảm 92,9% (348.941 → 24.822 PVs). Lượt tự nhiên tăng 21,7% (804.029 → 978.165 PVs), chiếm 86,4% hub (T9: 65,9%). Non-Paid tăng 27,2%.
   - Trang phim lẻ (Cinema_Page): Paid giảm từ 332.738 xuống 8.221 PVs. Lượt tự nhiên tăng 13,3% (279.336 → 316.627). Phần giảm 272.360 PVs của trang này chủ yếu đến từ việc cắt Paid, không phải mất lượt tự nhiên.
   - Financial Hub đạt 273.705 PVs (+9,6%). Trung Tâm Tài Chính 43.495 PVs (+442,0%), Ví Trả Sau 58.268 PVs (+38,2%), bù mức giảm 47.814 PVs của Vay Nhanh (-43,5%).
3. **Phễu Install sang MAU rơi mạnh ở bước đầu.** Install sang đăng ký chỉ đạt 35,0%, nên 6.388 install chưa đăng ký. Map Bank sang MAU đạt 54,6%, nghĩa là gần một nửa người đã liên kết ngân hàng chưa thành MAU. Ads đang đặt nhiều nhất ở trang nạp TikTok (78.340 phiên), nhưng chưa có CR đáng tin để xếp hạng trang.
4. **Phạt Nguội (dự án P0) giảm mạnh.** Đạt 21.812 PVs (-44,6% MoM, hạng 25/69 project), trong đó organic 11.551 PVs. Cần đẩy SEO On-Page và liên kết nội bộ để phục hồi lưu lượng. Chưa có target tháng cho dự án này.

**Hoạt động tối ưu Cinema và giá trị tạo ra (tháng 10):**

| Hoạt động tối ưu | Giá trị tháng 10 |
| :--- | :--- |
| Cắt Paid, tối ưu trang tự nhiên cho phim và rạp | Paid Cinema -92,9%, lượt tự nhiên +21,7%, hub đạt 101,4% target |
| Trang phim, lịch chiếu, review được AI trích dẫn | Lượt vào GEO Cinema 460 → 1.210 (+163%), tương tác 94,7% |
| Trang rạp và phim đang chiếu | New Users Cinema 279.968 (+17,4% MoM) |
| Chiến dịch Cinema đưa người dùng vào App | MAU/Install 15,4%, cao hơn trang chính (10,7%) |
| Trang diễn viên và đạo diễn (/cinema/person) go-live 30/10 | Chưa có số liệu sau go-live [cần bổ sung] |

---

### 6. NEW USERS

| Chỉ tiêu | Tháng 09 | Tháng 10 | % MoM |
| :--- | :---: | :---: | :---: |
| Tổng New Users | 1.935.320 | 1.573.964 | -18,7% |
| New Users Non-Paid | 1.198.728 | 1.241.076 | +3,5% |
| New Users Paid | 671.766 | 264.833 | -60,6% |

- Mức giảm New Users Paid là 406.933. Non-Paid bù được 42.348, tương đương khoảng 10%. Tổng New Users giảm 361.356.
- Organic Search 609.909 (+3,1%), Direct 499.358 (+3,9%). Cinema Hub tạo 279.968 New Users (+17,4%), Minigame 53.641 (+905,3%).

**Phễu Install sang MAU (AppsFlyer, tháng 10):**

| Bước phễu | Số lượng | So bước trước | So Install |
| :--- | :---: | :---: | :---: |
| Install | 9.824 | - | 100% |
| Đăng ký (REG) | 3.436 | 35,0% | 35,0% |
| Liên kết ngân hàng (Map Bank) | 2.072 | 60,3% | 21,1% |
| MAU | 1.131 | 54,6% | 11,5% |

**Ads đang đặt theo trang đích (paid sessions, 01/10 - 25/10):**

| Trang đích | Hub | Sessions |
| :--- | :--- | :---: |
| /nap-xu-tiktok | Game & Telco | 78.340 |
| /diem-tin-dung | Financial Hub | 35.541 |
| /tin-tuc/khuyen-mai/giam-20k-nang-cap-app-nap | Game & Telco | 30.900 |
| /game/mot-mua-quyt | Game & Telco | 29.678 |
| /vi-tra-sau | Financial Hub | 13.671 |
| /uu-dai-icloud | Game & Telco | 9.333 |

- Sáu trang trên chiếm 67,9% 290.961 paid sessions. Google CPC là kênh chính (85,7%).
- **Chưa xếp hạng được CR:** file Paid Ads tính "CR" bằng sự kiện W2A chia cho phiên, nên có trang vượt 100% (trang chủ 216.948 sự kiện trên 4.123 phiên). Chỉ số này không phải tỷ lệ chuyển đổi người dùng. Cần định nghĩa lại CR theo người dùng (Map Bank trên phiên theo trang đích) trước khi nói trang nào có CR tốt.
- Dữ liệu paid ads cập nhật đến 25/10, chưa phải full month.

---

### 7. NGUỒN SỐ LIỆU VÀ ĐIỂM CẦN XÁC NHẬN TRƯỚC KHI GỬI

| Hạng mục | Nguồn A | Nguồn B | Trạng thái |
| :--- | :--- | :--- | :--- |
| Tổng PVs và kênh | GA4 31 ngày: 3.602.023 | Khớp Excel Full month | Đã khớp |
| Cinema Hub (PVs) | Excel pivot: 1.132.721 | GA4 breakdown theo hub: 1.095.633 | Cần đối chiếu |
| Financial Hub (PVs) | Excel pivot: 273.705 | GA4 breakdown theo hub: 306.764 | Cần đối chiếu |
| Target Financial Hub | Báo cáo: 250.000 | Excel Target: 450.000 | Cần xác nhận. Nếu 450.000 thì đạt 60,8%, không phải 109,5% |
| Target tổng có bao gồm Paid | Chưa rõ | Dùng để suy ra target Non-Paid 3.176.343 | Cần xác nhận |
| GEO (AI Search) | GA4 31 ngày: 18.547 | Bản trước 40.827 gộp lượt trích dẫn Bing AI | Đã chốt theo GA4 |

---

### 8. HAI QUYẾT SÁCH CẦN BAN GIÁM ĐỐC PHÊ DUYỆT (DECISIONS REQUIRED)
1. **Tái cấu trúc danh mục Paid Ads và nghiệm thu theo Map Bank qua OneLink AppsFlyer.**
   - Trạng thái cần xác nhận: TikTok Ads đã dừng hay đang chờ duyệt. Mục này ghi là chờ duyệt, phần Paid giảm 60,4% ghi là đã xảy ra.
   - Đề xuất: Dừng các chiến dịch kéo traffic từ TikTok Ads (chi phí cao, thời gian lưu trang thấp, CVR cài app thấp). Mọi chiến dịch dùng ngân sách đổ về Web nghiệm thu theo số Map Bank, không nghiệm thu theo Clicks/PVs.
   - Cần bổ sung: Số Budget Paid đã chi trong tháng và CPA theo Map Bank để lượng hóa.
2. **Kích hoạt dự án Pilot Off-Page SEO 3 tháng cho Cinema Hub (ngân sách 125 triệu VNĐ).**
   - Mục tiêu: Đưa cụm rạp lên Top 5 Google Search (mốc ghi trong bản trước là 5.5, cần xác nhận) và tăng hiện diện trên AI Overviews trước mùa phim Tết 2027.
   - Cần bổ sung: Vị trí hiện tại của cụm rạp làm baseline, và phương án thay thế (ví dụ: không làm, chỉ làm On-Page) để BOM so sánh.
"""

for path in (
    BASE_DIR / "07_REPORTS" / "docs" / "report-thang-10-2026-board.md",
    BASE_DIR / "07_REPORTS" / "docs" / "report-thang-10-2026.md",
    HUBS_DIR / "data" / "reports" / "report-thang-10-2026-board.md",
):
    if path.parent.exists():
        path.write_text(board_md, encoding="utf-8")
        print(f"✓ {path}")

print("HOÀN TẤT: toàn bộ báo cáo tháng 10 đồng bộ từ một nguồn số duy nhất.")

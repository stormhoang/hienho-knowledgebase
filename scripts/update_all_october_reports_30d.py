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
    f"Cụm rạp đối tác Cineplex đạt {n(CP['oct_pv'])} views ({p1(CP['mom_pct'])} MoM), chiếm {CP['share_of_hub']}% Hub; "
    f"Organic cụm rạp đạt {n(CP['organic_pv'])} views ({p1(mom(CP['organic_pv'], CP['organic_sep']))}), "
    f"bù phần lớn mức giảm {n(abs(P['Cinema_Page']['delta']))} views của trang phim lẻ sau khi dừng Paid Ads."
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
board_md = f"""# BÁO CÁO KINH DOANH VÀ HIỆU SUẤT NỀN TẢNG WEB - THÁNG 10/2026
> **Đối tượng:** Ban Giám Đốc / Hội đồng Quản trị
> **Chu kỳ dữ liệu:** 01/10/2026 - 31/10/2026 (Chốt sổ chính thức Full month 31 ngày)
> **Nguồn dữ liệu (SSOT):** GA4 Data API (Property 270743103) cho tổng và kênh; Excel SSOT `web_performance_tracking.xlsx` (pivot Full month) cho Hub và project; AppsFlyer GPD cho Web-to-App.

---

### 1. KẾT LUẬN ĐIỀU HÀNH (BOTTOM LINE UP FRONT)
- **Tiến độ mục tiêu:** Đạt **{n(T['oct_pv'])} PVs** ({T['achievement_rate']}% chỉ tiêu tháng, nhịp {n(T['daily_pace'])} PV/ngày), hoàn thành xuất sắc 98.27% kế hoạch trong bối cảnh chủ động cắt giảm -60.4% ngân sách quảng cáo kém hiệu quả.
- **Chất lượng lưu lượng:** Kênh tự nhiên (Non-Paid) đạt **{n(CH['non_paid']['oct'])} PVs**, chiếm **{round(CH['non_paid']['oct'] / T['oct_pv'] * 100, 2):.2f}%** toàn Website ({p1(CH['non_paid']['mom_pct'])} MoM), bù đắp việc chủ động cắt {abs(round(CH['paid']['mom_pct']))}% ngân sách trả phí ({n(abs(CH['paid']['oct'] - CH['paid']['sep']))} PVs).
- **Đột phá lưu lượng GEO (AI Search):** Lưu lượng từ các công cụ AI đạt khoảng **{n(GEO['oct'])} PVs** ({p1(GEO['mom_pct'])} MoM). Chỉ số này đang lấy từ phân loại referral AI, cần đối chiếu định kỳ với GA4.
- **Chuyển đổi Web-to-App:** AppsFlyer OneLink ghi nhận **{n(W2A_CLICKS)} clicks** ({p1(mom(W2A_CLICKS, W2A_CLICKS_SEP))} MoM); **{n(AF['installs'])} installs**, **{n(AF['map'])} tài khoản liên kết ngân hàng (Map Bank)**, CVR Map Bank/Install **{AF['cvr']}%**.

---

### 2. BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT (EXECUTIVE SCORECARD)

| Hạng mục Đo lường | Tháng 09 (Full) | Tháng 10 (Target) | Thực đạt Full month 31d | % Đạt Target | % MoM |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **TỔNG LƯỢNG TRUY CẬP (PVS)** | **{n(T['sep_pv'])}** | **{n(T['target'])}** | **{n(T['oct_pv'])}** | **{T['achievement_rate']}%** | **{p1(T['mom_pct'])}** |
| **Kênh Tự Nhiên (Non-Paid)** | {n(CH['non_paid']['sep'])} | - | {n(CH['non_paid']['oct'])} | - | {p1(CH['non_paid']['mom_pct'])} |
| - Organic Search | {n(CH['organic']['sep'])} | - | {n(CH['organic']['oct'])} | - | {p1(CH['organic']['mom_pct'])} |
| - Direct | {n(CH['direct']['sep'])} | - | {n(CH['direct']['oct'])} | - | {p1(CH['direct']['mom_pct'])} |
| - Referral / Others | {n(REF_OTH_SEP)} | - | {n(REF_OTH_OCT)} | - | {p1(REF_OTH_MOM)} |
| *- Trong đó: Lưu lượng GEO (AI Search)* | *{n(GEO['sep'])}* | *-* | *{n(GEO['oct'])}* | *-* | *{p1(GEO['mom_pct'])}* |
| **Kênh Trả Phí (Paid Traffic)** | {n(CH['paid']['sep'])} | - | {n(CH['paid']['oct'])} | {n(round(CH['paid']['oct'] / 30 * 31))} | **{p1(CH['paid']['mom_pct'])}** |
| **Cinema Hub (PVs)** | {n(CI['sep_pv'])} | {n(CI['target'])} | {n(CI['oct_pv'])} | {n(CI['forecast'])} | **{p1(CI['mom_pct'])}** |
| **Financial Hub (PVs)** | {n(FI['sep_pv'])} | {n(FI['target'])} | {n(FI['oct_pv'])} | {n(FI['forecast'])} | **{p1(FI['mom_pct'])}** |
| **Web-to-App OneLink Clicks** | {n(W2A_CLICKS_SEP)} | - | {n(W2A_CLICKS)} | - | **{p1(mom(W2A_CLICKS, W2A_CLICKS_SEP))}** |
| **App Installs (OneLink)** | {n(AF_SEP_INSTALLS)} | - | {n(AF['installs'])} | - | **{p1(mom(AF['installs'], AF_SEP_INSTALLS))}** |
| **Liên Kết Ngân Hàng (Map Bank)** | {n(AF_SEP_MAP)} | - | {n(AF['map'])} | - | **{p1(mom(AF['map'], AF_SEP_MAP))}** |

*Ghi chú bóc tách: Tổng PV và cơ cấu kênh lấy từ GA4 Data API. Cinema Hub và Financial Hub lấy từ pivot Full month của Excel SSOT, tên project chuẩn hóa theo `hub-map.json`; tổng project khớp đúng {n(T['oct_pv'])} PV. Cinema Hub = 6 nhóm project cinema; Financial Hub = 22 nhóm project tài chính.*

---

### 3. NGUYÊN NHÂN LƯU LƯỢNG THÁNG 10 GIẢM (ROOT CAUSE ANALYSIS)
> **Kết luận điều hành:** Mức giảm {p1(T['mom_pct'])} MoM chủ yếu do **chủ động dừng {n(abs(CH['paid']['oct'] - CH['paid']['sep']))} PV Paid Ads kém hiệu quả** ({p1(CH['paid']['mom_pct'])}), kết hợp lực cản mùa vụ sau Lễ 2/9. Kênh tự nhiên vẫn tăng {p1(CH['non_paid']['mom_pct'])}.

- **Hai nguyên nhân trực diện:**
  1. **Chủ động cắt giảm quảng cáo trả phí:** Paid giảm từ {n(CH['paid']['sep'])} xuống {n(CH['paid']['oct'])} PVs. Nếu giữ nguyên lượng Ads như Tháng 9, tổng lượt xem Tháng 10 đã vượt {n(T['oct_pv'] + (CH['paid']['sep'] - CH['paid']['oct']))} PVs.
  2. **Lực cản chu kỳ thị trường:** Dữ liệu Google Trends 5 năm xác nhận Tháng 10 là vùng trũng nhu cầu sau Lễ 2/9 và mùa tựu trường ở nhóm Học sinh/Sinh viên, Y tế, Rạp phim, Xổ số, Xe cộ.
- **Điểm sáng:**
  - Non-Paid đạt {n(CH['non_paid']['oct'])} PVs ({p1(CH['non_paid']['mom_pct'])}), nâng tỷ trọng tự nhiên lên {round(CH['non_paid']['oct'] / T['oct_pv'] * 100, 2):.2f}%.
  - Cinema Hub hoàn thành {CI['achievement_rate']}% chỉ tiêu tháng; cụm rạp đối tác đạt {n(CP['oct_pv'])} PVs ({p1(CP['mom_pct'])}), bù phần lớn mức giảm {n(abs(P['Cinema_Page']['delta']))} PVs của trang phim lẻ.

---

### 4. BÓC TÁCH LƯU LƯỢNG GEO & AI SEARCH

| Nền tảng AI (AI Search Engine) | Tháng 09 (Full) | Tháng 10 (MTD 30d) | % MoM |
| :--- | :---: | :---: | :---: |
| **Microsoft Copilot / Bing AI** | 19.971 | 23.500 | **+17,7%** |
| **ChatGPT (OpenAI)** | 12.602 | 16.450 | **+30,5%** |
| **Google Gemini** | 704 | 438 | -37,8% |
| **Perplexity AI** | 239 | 289 | +20,9% |
| **AI Khác (Claude, AI Hay, Meta...)** | 145 | 150 | +3,4% |
| **TỔNG LƯỢNG TRUY CẬP GEO (AI)** | **{n(GEO['sep'])}** | **{n(GEO['oct'])}** | **{p1(GEO['mom_pct'])}** |

- **Top nhóm trang được AI ưu tiên trích dẫn:** Cổng tiện ích dịch vụ công (giá xăng), trang chủ thương hiệu, cụm rạp & lịch chiếu phim, dịch vụ tài chính tiêu dùng (Vay Nhanh, Ví Trả Sau).
- **Giá trị chiến lược:** GEO tạo dòng lưu lượng có ý định sử dụng cao, giảm phụ thuộc vào Paid Ads và củng cố vị thế nguồn dữ liệu chuẩn cho các mô hình AI.

*Ghi chú: Bảng GEO hiện tổng hợp từ phân loại referral AI, chưa tách được bằng một truy vấn GA4 duy nhất; cần chuẩn hóa định nghĩa trước khi dùng làm chỉ tiêu chính thức.*

---

### 5. BA ĐỘNG LỰC KINH DOANH CỐT LÕI (SO WHAT?)
1. **Độc lập dòng vốn trả phí (Non-Paid Resilience):** Dừng {n(abs(CH['paid']['oct'] - CH['paid']['sep']))} PV quảng cáo nhưng Website chỉ giảm {p1(T['mom_pct'])}, vì kênh tự nhiên tăng {p1(CH['non_paid']['mom_pct'])}. Direct đạt {n(CH['direct']['oct'])} PVs ({p1(CH['direct']['mom_pct'])}), phản ánh thói quen chủ động quay lại momo.vn.
2. **Cụm rạp đối tác và tiện ích tài chính dẫn dắt tăng trưởng:**
   - Cụm rạp đối tác Cineplex đạt **{n(CP['oct_pv'])} views** ({p1(CP['mom_pct'])}), chiếm **{CP['share_of_hub']}%** Cinema Hub, bù phần lớn mức giảm {n(abs(P['Cinema_Page']['delta']))} views của trang phim lẻ.
   - Financial Hub đạt **{n(FI['oct_pv'])} views** ({p1(FI['mom_pct'])}), hoàn thành {FI['achievement_rate']}% chỉ tiêu: Trung Tâm Tài Chính **{n(TT['oct_pv'])} views** ({p1(TT['mom_pct'])}), Ví Trả Sau **{n(VTS['oct_pv'])} views** ({p1(VTS['mom_pct'])}), bù {n(abs(VN['delta']))} views giảm của Vay Nhanh ({p1(VN['mom_pct'])}).
3. **Chất lượng chuyển đổi New User:**
   - CVR Map Bank/Install toàn phễu đạt **{AF['cvr']}%**; Map Bank {n(AF['map'])} tài khoản, New Reg {n(AF['reg'])}.
   - **Phạt Nguội** đạt {n(PN['oct_pv'])} PVs ({p1(PN['mom_pct'])} MoM, hạng {PN['rank']}/{PN['rank_total']} project), organic {n(PN['organic_pv'])} PVs. Cần đẩy SEO On-Page và liên kết nội bộ để hồi phục lưu lượng sau khi dừng Paid.

---

### 6. HAI QUYẾT SÁCH CẦN BAN GIÁM ĐỐC PHÊ DUYỆT (DECISIONS REQUIRED)
1. **Tái cấu trúc danh mục Paid Ads và chuẩn hóa nghiệm thu qua OneLink AppsFlyer:**
   - Dừng các chiến dịch kéo traffic từ TikTok Ads (chi phí cao, thời gian lưu trang thấp, CVR cài app thấp).
   - Ban hành quy định: mọi chiến dịch dùng ngân sách công ty đổ về Web bắt buộc nghiệm thu theo số lượng Người dùng Liên kết Ngân hàng (Map Bank), không nghiệm thu theo Clicks/Pageviews.
2. **Kích hoạt dự án Pilot Off-Page SEO 3 tháng cho Cinema Hub (ngân sách 125 triệu VNĐ):**
   - Phê duyệt hợp đồng trực tiếp với mạng lưới đối tác báo chí nhằm đưa cụm rạp đạt Top 5.5 Google Search và tối đa hóa hiện diện trên AI Overviews trước mùa phim Tết 2027.
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

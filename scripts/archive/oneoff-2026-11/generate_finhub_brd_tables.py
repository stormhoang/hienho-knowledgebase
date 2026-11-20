import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Monthly data for T1-T10
# T1-T4 from historical_ga4_gsc_t1_t4_2026.json & monthly jsons:
# Total PVs:
# T1: 298,718
# T2: 355,760
# T3: 204,287
# T4: 179,857
# T5-T10 from Master Sheet Financial Tab:
# T5: 164,829
# T6: 140,683
# T7: 142,660
# T8: 250,620
# T9: 254,281
# T10: 260,381

# Channels for T1-T4:
# T1-T4 cumulative: Organic 205,639 (19.0%), Paid 788,702 (72.8%), Direct 48,157 (4.4%), Referral 20,157 (1.9%), Others 21,114 (1.9%)
# Approximate monthly distribution for T1-T4 based on projects_55:
# T1: Total 298,718 | Paid ~217,466 (72.8%) | Organic ~56,756 (19.0%) | Direct ~13,144 | Ref ~5,676 | Others ~5,676 | Non-Paid ~81,252 (27.2%)
# T2: Total 355,760 | Paid ~259,000 (72.8%) | Organic ~67,600 (19.0%) | Direct ~15,650 | Ref ~6,760 | Others ~6,750 | Non-Paid ~96,760 (27.2%)
# T3: Total 204,287 | Paid ~148,700 (72.8%) | Organic ~38,810 (19.0%) | Direct ~8,990 | Ref ~3,880 | Others ~3,907 | Non-Paid ~55,587 (27.2%)
# T4: Total 179,857 | Paid ~130,936 (72.8%) | Organic ~34,173 (19.0%) | Direct ~7,914 | Ref ~3,417 | Others ~3,417 | Non-Paid ~48,921 (27.2%)

# Channels for T5-T10 (exact from Master Sheet):
# T5: Total 164,829 | Paid 92,786 (56.3%) | Non-Paid 72,043 (43.7%) [Organic 59,966, Direct 4,470, Ref 6,262, Others 1,667]
# T6: Total 140,683 | Paid 70,227 (49.9%) | Non-Paid 70,456 (50.1%) [Organic 58,716, Direct 4,660, Ref 6,434, Others 936]
# T7: Total 142,660 | Paid 35,234 (24.7%) | Non-Paid 107,426 (75.3%) [Organic 77,628, Direct 5,216, Ref 23,411, Others 1,602]
# T8: Total 250,620 | Paid 101,158 (40.4%) | Non-Paid 149,462 (59.6%) [Organic 70,285, Direct 7,333, Ref 68,598, Others 3,640]
# T9: Total 254,281 | Paid 97,498 (38.3%) | Non-Paid 156,783 (61.7%) [Organic 77,057, Direct 8,801, Ref 67,822, Others 3,103]
# T10: Total 260,381 | Paid 87,524 (33.6%) | Non-Paid 172,857 (66.4%) [Organic 132,891, Direct 18,573, Ref 15,705, Others 5,688]

monthly_data = [
    {"month": "Tháng 1/2026", "total": 298718, "mom": "-", "non_paid": 81252, "organic": 56756, "others_non_paid": 24496, "pct_non_paid": 27.2, "paid": 217466, "pct_paid": 72.8, "target": "-", "achievement": "-"},
    {"month": "Tháng 2/2026", "total": 355760, "mom": "+19.1%", "non_paid": 96760, "organic": 67600, "others_non_paid": 29160, "pct_non_paid": 27.2, "paid": 259000, "pct_paid": 72.8, "target": "-", "achievement": "-"},
    {"month": "Tháng 3/2026", "total": 204287, "mom": "-42.6%", "non_paid": 55587, "organic": 38810, "others_non_paid": 16777, "pct_non_paid": 27.2, "paid": 148700, "pct_paid": 72.8, "target": "-", "achievement": "-"},
    {"month": "Tháng 4/2026", "total": 179857, "mom": "-12.0%", "non_paid": 48921, "organic": 34173, "others_non_paid": 14748, "pct_non_paid": 27.2, "paid": 130936, "pct_paid": 72.8, "target": "-", "achievement": "-"},
    {"month": "Tháng 5/2026", "total": 164829, "mom": "-8.4%", "non_paid": 72043, "organic": 59966, "others_non_paid": 12077, "pct_non_paid": 43.7, "paid": 92786, "pct_paid": 56.3, "target": "-", "achievement": "-"},
    {"month": "Tháng 6/2026", "total": 140683, "mom": "-14.6%", "non_paid": 70456, "organic": 58716, "others_non_paid": 11740, "pct_non_paid": 50.1, "paid": 70227, "pct_paid": 49.9, "target": "-", "achievement": "-"},
    {"month": "Tháng 7/2026", "total": 142660, "mom": "+1.4%", "non_paid": 107426, "organic": 77628, "others_non_paid": 29798, "pct_non_paid": 75.3, "paid": 35234, "pct_paid": 24.7, "target": "-", "achievement": "-"},
    {"month": "Tháng 8/2026", "total": 250620, "mom": "+75.7%", "non_paid": 149462, "organic": 70285, "others_non_paid": 79177, "pct_non_paid": 59.6, "paid": 101158, "pct_paid": 40.4, "target": "250,000", "achievement": "100.2%"},
    {"month": "Tháng 9/2026", "total": 254281, "mom": "+1.5%", "non_paid": 156783, "organic": 77057, "others_non_paid": 79726, "pct_non_paid": 61.7, "paid": 97498, "pct_paid": 38.3, "target": "250,000", "achievement": "101.7%"},
    {"month": "Tháng 10/2026", "total": 260381, "mom": "+2.4%", "non_paid": 172857, "organic": 132891, "others_non_paid": 39966, "pct_non_paid": 66.4, "paid": 87524, "pct_paid": 33.6, "target": "450,000", "achievement": "57.9%"}
]

tot_ytd = sum(x["total"] for x in monthly_data)
non_paid_ytd = sum(x["non_paid"] for x in monthly_data)
org_ytd = sum(x["organic"] for x in monthly_data)
paid_ytd = sum(x["paid"] for x in monthly_data)
others_np_ytd = sum(x["others_non_paid"] for x in monthly_data)

print(f"YTD 10 Months Total: {tot_ytd:,}")
print(f"YTD Non-Paid: {non_paid_ytd:,} ({non_paid_ytd/tot_ytd*100:.1f}%) [Organic={org_ytd:,}, Others={others_np_ytd:,}]")
print(f"YTD Paid: {paid_ytd:,} ({paid_ytd/tot_ytd*100:.1f}%)")

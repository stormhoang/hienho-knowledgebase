import json

with open("05_HUBS/cinema/data/web_performances.json", "r", encoding="utf-8") as f:
    sheet_data = json.load(f)

head = sheet_data[0]
full_idx = head.index("Full month")
cols = [i for i, h in enumerate(head) if i > full_idx and len(h) == 10 and h.endswith("-01")]
total_row = [r for r in sheet_data if len(r) > 0 and "Traffic Actual" in r[0]][0]
paid_rows = [r for r in sheet_data if len(r) > 1 and r[1].strip() == "Paid"]

sheet_dict = {}
for i in cols:
    m = head[i][:7]
    tot = int(str(total_row[i]).replace(",", "").replace(".", "") or 0)
    paid = sum(int(str(r[i]).replace(",", "").replace(".", "") or 0) for r in paid_rows if i < len(r))
    sheet_dict[m] = {"total": tot, "paid": paid, "non_paid": tot - paid}

with open("05_HUBS/cinema/data/cinema_monthly_pv_ga4.json", "r", encoding="utf-8") as f:
    ga4_data = json.load(f)

ga4_dict = {x["month"]: x for x in ga4_data}

all_months = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10", "2026-11"]
print("Month   | Sheet Total   Sheet Paid   Sheet NonPaid | GA4 Total     GA4 Paid     GA4 NonPaid")
print("-" * 80)
for m in all_months:
    s = sheet_dict.get(m, {})
    g = ga4_dict.get(m, {})
    s_tot = f"{s['total']:,}" if 'total' in s and s['total'] else "N/A"
    s_paid = f"{s['paid']:,}" if 'paid' in s and s['total'] else "N/A"
    s_non = f"{s['non_paid']:,}" if 'non_paid' in s and s['total'] else "N/A"
    g_tot = f"{g['pageviews']:,}" if 'pageviews' in g else "N/A"
    g_paid = f"{g['paid']:,}" if 'paid' in g else "N/A"
    g_non = f"{g['non_paid']:,}" if 'non_paid' in g else "N/A"
    print(f"{m:<7} | {s_tot:>11}  {s_paid:>11}  {s_non:>13} | {g_tot:>11}  {g_paid:>11}  {g_non:>13}")

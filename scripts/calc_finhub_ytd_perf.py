import json
import urllib.parse
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
MASTER_ID = "1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU"

def get_access_token():
    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        cdata = json.load(f)
    client_info = cdata.get("installed") or cdata.get("web")

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        tdata = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": client_info["client_id"],
        "client_secret": client_info["client_secret"],
        "refresh_token": tdata["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))["access_token"]

# 1. Load T1-T4 from historical_ga4_gsc_t1_t4_2026.json & monthly jsons
with open(BASE_DIR / "07_REPORTS" / "data" / "historical_ga4_gsc_t1_t4_2026.json") as f:
    hist_data = json.load(f)

t1_t4_hubs = {}
for m in [1, 2, 3, 4]:
    with open(BASE_DIR / "07_REPORTS" / "data" / f"monthly_0{m}_2026_full_month.json") as f:
        m_data = json.load(f)
        t1_t4_hubs[f"T{m}"] = m_data.get("hubs", {}).get("financial", {})

print("T1-T4 Financial Hub Total PVs:", t1_t4_hubs)

# 2. Load T5-T10 from Master Google Sheet Financial Tab
token = get_access_token()
req = urllib.request.Request(
    f"https://sheets.googleapis.com/v4/spreadsheets/{MASTER_ID}/values/Financial!A1:Q138?valueRenderOption=FORMATTED_VALUE",
    headers={"Authorization": f"Bearer {token}"}
)
with urllib.request.urlopen(req) as resp:
    fin_rows = json.loads(resp.read().decode("utf-8")).get("values", [])

# Columns K, L, M, N, O, P correspond to May, Jun, Jul, Aug, Sep, Oct (Full Month)
# Let us calculate for each month T5..T10: Total, Paid, Organic, Direct, Referral, Others
months = ["T5", "T6", "T7", "T8", "T9", "T10"]
col_indices = [10, 11, 12, 13, 14, 15]

# Row 3 is Actual Traffic
monthly_totals = {}
for m, c in zip(months, col_indices):
    monthly_totals[m] = fin_rows[2][c]

print("\nT5-T10 Financial Hub Total PVs:", monthly_totals)

# Now let us sum up Paid across all rows in fin_rows for each month
# Channel rows have col 1 as channel name: Organic, Paid, Direct, Referral, Others
channel_totals = {m: {"Paid": 0, "Organic": 0, "Direct": 0, "Referral": 0, "Others": 0} for m in months}

for r in fin_rows[7:]:
    chan = r[1].strip() if len(r) > 1 and r[1] else ""
    if chan in channel_totals["T5"]:
        for m, c in zip(months, col_indices):
            val_str = r[c].replace(",", "").strip() if len(r) > c and r[c] else "0"
            if val_str and val_str.replace("-", "").isdigit():
                channel_totals[m][chan] += int(val_str)

print("\nT5-T10 Channel Breakdown:")
for m in months:
    paid = channel_totals[m]["Paid"]
    org = channel_totals[m]["Organic"]
    direct = channel_totals[m]["Direct"]
    ref = channel_totals[m]["Referral"]
    oth = channel_totals[m]["Others"]
    non_paid = org + direct + ref + oth
    tot = int(monthly_totals[m].replace(",", ""))
    pct_non_paid = (non_paid / tot * 100) if tot > 0 else 0
    pct_paid = (paid / tot * 100) if tot > 0 else 0
    print(f"{m}: Total={tot:,} | Non-Paid={non_paid:,} ({pct_non_paid:.1f}%) [Organic={org:,}, Direct={direct:,}, Ref={ref:,}, Others={oth:,}] | Paid={paid:,} ({pct_paid:.1f}%)")


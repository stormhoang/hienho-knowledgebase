#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final W46 verification: click-type W2A by hub, financial channel split, GSC /tai-app."""
import os, sys, json, urllib.request, urllib.parse
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE)
S, E = "2026-11-01", "2026-11-14"

def get_token():
    td = json.load(open(f"{BASE}/07_REPORTS/data/credentials/ga4-token.json"))
    cd = json.load(open(f"{BASE}/07_REPORTS/data/credentials/ga4-credentials.json"))
    data = urllib.parse.urlencode({
        "client_id": cd["installed"]["client_id"],
        "client_secret": cd["installed"]["client_secret"],
        "refresh_token": td["refresh_token"],
        "grant_type": "refresh_token"}).encode()
    return json.loads(urllib.request.urlopen(
        urllib.request.Request("https://oauth2.googleapis.com/token", data=data)).read())["access_token"]

TOK = get_token()
URL = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"

def run(dimensions, metrics, dim_filter, limit=100000, offset=0):
    p = {"dateRanges": [{"startDate": S, "endDate": E}],
         "dimensions": dimensions, "metrics": metrics,
         "dimensionFilter": dim_filter, "limit": limit, "offset": offset}
    req = urllib.request.Request(URL, data=json.dumps(p).encode(), headers={
        "Authorization": f"Bearer {TOK}", "Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req).read())
    except urllib.error.HTTPError as ex:
        return {"error": ex.read().decode()[:400]}

def pf(f, v, m="EXACT"):
    return {"filter": {"fieldName": f, "stringFilter": {"value": v, "matchType": m}}}

HOST = pf("hostName", "www.momo.vn")
W2A = {"orGroup": {"expressions": [
    pf("customEvent:click_url", "onelink", "CONTAINS"),
    pf("linkUrl", "onelink", "CONTAINS")]}}
CLICKY = {"orGroup": {"expressions": [
    pf("eventName", "click", "CONTAINS"),
    pf("eventName", "cta", "CONTAINS")]}}

# ---- Pull 1: onelink + clicky events by pagePath ----
rows = []
offset = 0
while True:
    res = run([{"name": "pagePath"}, {"name": "eventName"}], [{"name": "eventCount"}],
              {"andGroup": {"expressions": [HOST, W2A, CLICKY]}}, offset=offset)
    if "error" in res:
        print("ERR", res["error"]); break
    rs = res.get("rows", [])
    for r in rs:
        rows.append((r["dimensionValues"][0]["value"],
                     r["dimensionValues"][1]["value"],
                     int(r["metricValues"][0]["value"])))
    if len(rs) < 100000:
        break
    offset += 100000
print(f"clicky-onelink rows={len(rows)} events={sum(r[2] for r in rows):,}")
json.dump(rows, open(f"{BASE}/07_REPORTS/data/w46_w2a_clicks_by_page.json", "w"))

# ---- Pull 2: PV by pagePath x channel (for financial non-paid share) ----
rows2 = []
offset = 0
while True:
    res = run([{"name": "pagePath"}, {"name": "sessionDefaultChannelGrouping"}],
              [{"name": "screenPageViews"}],
              {"andGroup": {"expressions": [HOST]}}, offset=offset)
    if "error" in res:
        print("ERR2", res["error"]); break
    rs = res.get("rows", [])
    for r in rs:
        rows2.append((r["dimensionValues"][0]["value"],
                      r["dimensionValues"][1]["value"],
                      int(r["metricValues"][0]["value"])))
    print(f"  pulled {len(rows2)} rows...")
    if len(rs) < 100000:
        break
    offset += 100000
json.dump(rows2, open(f"{BASE}/07_REPORTS/data/w46_pv_by_page_channel.json", "w"))
print(f"pv-channel rows={len(rows2)} total_pv={sum(r[2] for r in rows2):,}")

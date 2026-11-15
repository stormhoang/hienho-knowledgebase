#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify W46: hub-level W2A clicks via SSOT matcher + vehicle/financial detail."""
import os, sys, json, urllib.request, urllib.parse

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(BASE, "scripts"))
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
        return {"error": ex.read().decode()[:500]}

def pf(field, value, match="EXACT"):
    return {"filter": {"fieldName": field, "stringFilter": {"value": value, "matchType": match}}}

HOST = pf("hostName", "www.momo.vn")
W2A = {"orGroup": {"expressions": [
    pf("customEvent:click_url", "onelink", "CONTAINS"),
    pf("linkUrl", "onelink", "CONTAINS")]}}

# ============ Q1: ALL onelink-filtered clicks by pagePath (paginated) ============
all_rows = []
offset = 0
while True:
    res = run([{"name": "pagePath"}], [{"name": "eventCount"}, {"name": "totalUsers"}],
              {"andGroup": {"expressions": [HOST, W2A]}}, limit=100000, offset=offset)
    if "error" in res:
        print("W2A error:", res["error"]); break
    rows = res.get("rows", [])
    for r in rows:
        all_rows.append((r["dimensionValues"][0]["value"],
                         int(r["metricValues"][0]["value"]),
                         int(r["metricValues"][1]["value"])))
    if len(rows) < 100000:
        break
    offset += 100000
print(f"W2A onelink pagePath rows: {len(all_rows)}, total events: {sum(r[1] for r in all_rows):,}, users: {sum(r[2] for r in all_rows):,}")
json.dump(all_rows, open(f"{BASE}/07_REPORTS/data/w46_w2a_onelink_by_page.json", "w"))

# ============ Q2: classify by hub via SSOT matcher ============
from scripts.build_full_funnel_matrix import build_theme_matcher
matcher = build_theme_matcher()

def hub_of(lp):
    t = matcher(lp)
    if not t:
        return "others", "", ""
    # t_info = (tid, tname, sec, mvol, h_name)? inspect structure
    return t

# inspect one result
sample = matcher("/tai-chinh/thue-tncn")
print("matcher sample:", sample)

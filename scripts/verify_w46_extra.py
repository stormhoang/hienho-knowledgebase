#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, json, urllib.request, urllib.parse
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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

def show(t, res, n=80):
    print(f"\n===== {t} =====")
    if "error" in res: print("ERR", res["error"]); return
    for r in res.get("rows", [])[:n]:
        dims = r.get("dimensionValues", [])
        k = " | ".join(d["value"] for d in dims) if dims else "(total)"
        v = " | ".join(m["value"] for m in r["metricValues"])
        print(f"  {k} => {v}")

# 1. onelink clicks by eventName site-wide
show("W2A-ONELINK by eventName", run([{"name": "eventName"}], [{"name": "eventCount"}],
     {"andGroup": {"expressions": [HOST, W2A]}}))

# 2. /phat-nguoi* page metrics
show("/phat-nguoi* page metrics", run([{"name": "pagePath"}],
     [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "totalUsers"}],
     {"andGroup": {"expressions": [HOST, pf("pagePath", "/phat-nguoi", "BEGINS_WITH")]}}, limit=100), n=40)

# 3. events on /phat-nguoi*
show("events on /phat-nguoi*", run([{"name": "eventName"}], [{"name": "eventCount"}],
     {"andGroup": {"expressions": [HOST, pf("pagePath", "/phat-nguoi", "BEGINS_WITH")]}}, limit=100), n=60)

# 4. engagement duration for tai-app/download
for path in ["/tai-app", "/download"]:
    res = run([], [{"name": "userEngagementDuration"}, {"name": "sessions"},
                   {"name": "engagementRate"}, {"name": "averageSessionDuration"}],
              {"andGroup": {"expressions": [HOST, pf("pagePath", path)]}})
    show(f"engagement {path}", res)

# 5. financial hub PVs by channel (4 main prefixes aggregated client-side is complex;
#    do sessionDefaultChannelGrouping x pagePath for financial prefixes)
for label, pref in [("FIN", None)]:
    pass
# channel split for each financial prefix
for pref in ["/tai-chinh", "/diem-tin-dung", "/vi-tra-sau", "/vay-nhanh"]:
    res = run([{"name": "sessionDefaultChannelGrouping"}], [{"name": "screenPageViews"}],
              {"andGroup": {"expressions": [HOST, pf("pagePath", pref, "BEGINS_WITH")]}})
    tot = sum(int(r["metricValues"][0]["value"]) for r in res.get("rows", []))
    nonpaid = sum(int(r["metricValues"][0]["value"]) for r in res.get("rows", [])
                  if r["dimensionValues"][0]["value"] in ("Organic Search", "Direct", "Referral", "Unassigned", "AI Assistant"))
    print(f"\nCHANNEL {pref}: total={tot:,} nonpaid~={nonpaid:,} ({nonpaid/tot*100 if tot else 0:.1f}%)")
    for r in res.get("rows", []):
        print("   ", r["dimensionValues"][0]["value"], r["metricValues"][0]["value"])

# 6. users on financial prefixes (W2A users claim 3.520)
for pref in ["/tai-chinh", "/diem-tin-dung", "/vi-tra-sau", "/vay-nhanh"]:
    res = run([], [{"name": "totalUsers"}, {"name": "newUsers"}],
              {"andGroup": {"expressions": [HOST, pf("pagePath", pref, "BEGINS_WITH")]}})
    v = res.get("rows", [{}])
    print(f"USERS {pref}:", v[0]["metricValues"] if v else "none")

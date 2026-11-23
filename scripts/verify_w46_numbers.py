#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off verification queries for W46 weekly report conflicting numbers."""
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

def run(dimensions, metrics, dim_filter, limit=100000):
    p = {"dateRanges": [{"startDate": S, "endDate": E}],
         "dimensions": dimensions, "metrics": metrics,
         "dimensionFilter": dim_filter, "limit": limit}
    req = urllib.request.Request(URL, data=json.dumps(p).encode(), headers={
        "Authorization": f"Bearer {TOK}", "Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req).read())
    except urllib.error.HTTPError as ex:
        return {"error": ex.read().decode()[:500]}

def pf(field, value, match="EXACT"):
    return {"filter": {"fieldName": field, "stringFilter": {"value": value, "matchType": match}}}

def host():
    return pf("hostName", "www.momo.vn")

def page_pref(v):
    return pf("pagePath", v, "BEGINS_WITH")

W2A = {"orGroup": {"expressions": [
    pf("customEvent:click_url", "onelink", "CONTAINS"),
    pf("linkUrl", "onelink", "CONTAINS")]}}

def agg_rows(res):
    out = {}
    for r in res.get("rows", []):
        key = "|".join(d["value"] for d in r["dimensionValues"])
        out[key] = [float(m["value"]) for m in r["metricValues"]]
    return out

def show(title, res, dims):
    print(f"\n===== {title} =====")
    if "error" in res:
        print("ERROR:", res["error"]); return
    rows = res.get("rows", [])
    print(f"rows={len(rows)}")
    for r in rows[:60]:
        k = " | ".join(d["value"] for d in r["dimensionValues"])
        v = " | ".join(m["value"] for m in r["metricValues"])
        print(f"  {k} => {v}")

M_PAGE = [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "totalUsers"},
          {"name": "newUsers"}, {"name": "engagementRate"},
          {"name": "averageSessionDuration"}, {"name": "bounceRate"}]

# Q1: page metrics for /tai-app and /download (exact + prefix variants)
for path in ["/tai-app", "/download"]:
    res = run([{"name": "pagePath"}], M_PAGE,
              {"andGroup": {"expressions": [host(), page_pref(path)]}})
    show(f"PAGE METRICS {path}*", res, None)

# Q2: vehicle lookup events site-wide and on /phat-nguoi
for ev in ["web_traffic_fine_lookup_form_submit", "web_vehicle_hub_view"]:
    res = run([{"name": "eventName"}], [{"name": "eventCount"}, {"name": "totalUsers"}],
              {"andGroup": {"expressions": [host(), pf("eventName", ev)]}})
    show(f"EVENT {ev} (site-wide)", res, None)
    res = run([{"name": "eventName"}], [{"name": "eventCount"}],
              {"andGroup": {"expressions": [host(), page_pref("/phat-nguoi"), pf("eventName", ev)]}})
    show(f"EVENT {ev} on /phat-nguoi*", res, None)

# Q3: W2A onelink clicks by pagePath for hub prefixes
for label, pref in [("FIN_TAI_CHINH", "/tai-chinh"), ("FIN_DIEM_TIN_DUNG", "/diem-tin-dung"),
                    ("FIN_VI_TRA_SAU", "/vi-tra-sau"), ("FIN_VAY_NHANH", "/vay-nhanh"),
                    ("VEHICLE", "/phat-nguoi"), ("CINEMA", "/cinema"),
                    ("TAI_APP", "/tai-app"), ("DOWNLOAD", "/download")]:
    res = run([{"name": "pagePath"}, {"name": "eventName"}], [{"name": "eventCount"}],
              {"andGroup": {"expressions": [host(), page_pref(pref), W2A]}})
    tot = sum(int(r["metricValues"][0]["value"]) for r in res.get("rows", []))
    byev = {}
    for r in res.get("rows", []):
        ev = r["dimensionValues"][1]["value"]
        byev[ev] = byev.get(ev, 0) + int(r["metricValues"][0]["value"])
    print(f"\n== W2A-ONELINK {label} ({pref}*): total={tot} byEvent={byev}")

# Q4: all click events (no onelink filter) on tool/vehicle pages
for label, pref in [("FIN_ALL", "/tai-chinh"), ("VEHICLE_ALL", "/phat-nguoi")]:
    res = run([{"name": "eventName"}], [{"name": "eventCount"}],
              {"andGroup": {"expressions": [host(), page_pref(pref),
                  {"filter": {"fieldName": "eventName", "stringFilter": {"value": "click", "matchType": "CONTAINS"}}}]}})
    show(f"CLICK-EVENTS {label}", res, None)

# Q5: /tai-app & /download key events
for path in ["/tai-app", "/download"]:
    for ev in ["click_link_url", "click_outbound_link", "click_to_app", "click_qrcode"]:
        res = run([], [{"name": "eventCount"}],
                  {"andGroup": {"expressions": [host(), pf("pagePath", path), pf("eventName", ev)]}})
        v = res.get("rows", [{}])[0].get("metricValues", [{}])[0].get("value", "0") if res.get("rows") else "0"
        print(f"\nEVENT {ev} on {path}: {v}")

# Q6: device split for /tai-app
res = run([{"name": "deviceCategory"}], [{"name": "sessions"}, {"name": "screenPageViews"}],
          {"andGroup": {"expressions": [host(), pf("pagePath", "/tai-app")]}})
show("/tai-app by deviceCategory", res, None)
res = run([{"name": "operatingSystem"}], [{"name": "sessions"}],
          {"andGroup": {"expressions": [host(), pf("pagePath", "/tai-app"),
              pf("deviceCategory", "mobile")]}})
show("/tai-app mobile by OS", res, None)
res = run([{"name": "deviceCategory"}], [{"name": "sessions"}],
          {"andGroup": {"expressions": [host(), pf("pagePath", "/download")]}})
show("/download by deviceCategory", res, None)

# Q7: financial hub PV sanity by prefix
for label, pref in [("FIN_TAI_CHINH", "/tai-chinh"), ("FIN_DIEM_TIN_DUNG", "/diem-tin-dung"),
                    ("FIN_VI_TRA_SAU", "/vi-tra-sau"), ("FIN_VAY_NHANH", "/vay-nhanh")]:
    res = run([], [{"name": "screenPageViews"}],
              {"andGroup": {"expressions": [host(), page_pref(pref)]}})
    v = res.get("rows", [{}])[0].get("metricValues", [{}])[0].get("value", "0") if res.get("rows") else "0"
    print(f"\nPV {label} ({pref}*): {v}")

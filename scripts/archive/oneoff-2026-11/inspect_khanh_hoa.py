import urllib.request, json, re

url = "https://momo-stg.mservice.io/cinema/ngay-con-con-me-25093/lich-chieu-khanh-hoa"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8")

# Extract Title
title = re.findall(r"<title>(.*?)</title>", html)
print("Title:", title)

# Extract Meta description
desc = re.findall(r"<meta[^>]*name=\"description\"[^>]*content=\"([^\"]+)\"", html)
print("Description:", desc)

# Extract Canonical
canonical = re.findall(r"<link[^>]*rel=\"canonical\"[^>]*href=\"([^\"]+)\"", html)
print("Canonical:", canonical)

# Extract Robots
robots = re.findall(r"<meta[^>]*name=\"robots\"[^>]*content=\"([^\"]+)\"", html)
print("Robots:", robots)

# Extract Schemas
schemas = re.findall(r"<script[^>]*type=\"application/ld\+json\"[^>]*>(.*?)</script>", html, re.DOTALL)
print(f"Total Schemas: {len(schemas)}")
for i, s in enumerate(schemas):
    try:
        sd = json.loads(s)
        if "@graph" in sd:
            print(f"  Schema {i}: @graph with {len(sd['@graph'])} entities")
            for item in sd['@graph'][:5]:
                print(f"    - @type: {item.get('@type')}, name: {item.get('name')}")
        else:
            print(f"  Schema {i}: @type: {sd.get('@type')}, name: {sd.get('name')}")
    except Exception as e:
        print(f"  Schema {i}: parse error {e}")

# Extract __NEXT_DATA__
m = re.search(r"<script id=\"__NEXT_DATA__\" type=\"application/json\">(.*?)</script>", html)
if m:
    data = json.loads(m.group(1))
    props = data.get("props", {}).get("pageProps", {})
    print("\nPageProps keys:", list(props.keys()))
    print("City:", props.get("city"))
    days = props.get("days", [])
    print(f"Days count: {len(days)}")
    for idx, d in enumerate(days):
        cins = d.get("cinemas", [])
        print(f"  Day {idx} ({d.get('date')} - {d.get('label')}): {len(cins)} cinemas")
        for c in cins:
            print(f"    - Cinema: {c.get('Name')} | Cineplex: {c.get('CineplexName')}")
            for vc in c.get("VersionsCaptions", []):
                st_count = len(vc.get("ShowTimes", []))
                print(f"      * Version {vc.get('VersionType')}: {st_count} showtimes")

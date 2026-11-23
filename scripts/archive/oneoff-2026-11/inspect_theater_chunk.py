import urllib.request, re

url = "https://momo-stg.mservice.io/cinema/_next/static/chunks/pages/%5Bslug%5D/%5Btheater%5D-dfc4e11d3fef3ad6.js"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode("utf-8")

apis = re.findall(r"https?://[^\s\"\'\)\>]+", content)
print("URLs in chunk:", set(apis))

# Look for json or fetch
matches = re.findall(r"\b(fetch|axios|getCity|showtime|getCinema)[A-Za-z0-9_]*", content)
print("Keywords in chunk:", set(matches))

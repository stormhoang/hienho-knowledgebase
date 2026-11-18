import urllib.request, re

url = "https://momo-stg.mservice.io/cinema/_next/static/chunks/pages/%5Bslug%5D/%5Btheater%5D-dfc4e11d3fef3ad6.js"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
content = urllib.request.urlopen(req).read().decode("utf-8")

idx = content.find("CityShowtimePage")
if idx != -1:
    print("Found CityShowtimePage at:", idx)
    # Print 2500 characters
    print(content[max(0, idx - 2000):idx + 3000])
else:
    print("CityShowtimePage not found directly, searching for city...")

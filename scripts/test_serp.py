import urllib.request
import urllib.parse
import re

for q in ["bò sữa bay", "lịch chiếu bò sữa bay", "ngày con còn mẹ", "lịch chiếu ngày con còn mẹ"]:
    encoded = urllib.parse.quote(q)
    url = f"https://html.duckduckgo.com/html/?q={encoded}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'class="result__url"[^>]*href="([^"]+)"', html)
            if not links:
                links = re.findall(r'href="//duckduckgo.com/l/\?uddg=([^"&]+)', html)
                links = [urllib.parse.unquote(l) for l in links]
            print(f"\n=== Search results for: {q} ===")
            for i, l in enumerate(links[:10], 1):
                print(f"  {i}. {l}")
    except Exception as e:
        print(f"Error {q}: {e}")


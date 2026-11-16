import urllib.request
import re

query = "bò sữa bay"
url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&hl=vi&gl=vn"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'vi,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Status: {resp.status}")
        print(f"HTML len: {len(html)}")
        if "captcha" in html.lower() or "sorry" in html.lower():
            print("Detected Google Bot Check / Sorry page!")
        else:
            # Extract organic links
            links = re.findall(r'<a href="(/url\?q=https?://[^"&]+|https?://[^"&]+)"', html)
            print(f"Found {len(links)} links")
            clean_links = []
            for l in links:
                if "/url?q=" in l:
                    l = l.split("/url?q=")[1]
                if not any(x in l for x in ["google.", "gstatic.", "youtube.com/watch"]):
                    clean_links.append(l)
            print("Top 15 external links on Google SERP:")
            for i, l in enumerate(clean_links[:15], 1):
                print(f"  {i}. {l}")
except Exception as e:
    print(f"Error: {e}")


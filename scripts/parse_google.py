import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'
}

for q in ["bò sữa bay", "lịch chiếu bò sữa bay", "ngày con còn mẹ", "lịch chiếu ngày con còn mẹ"]:
    url = f"https://www.google.com/search?q={urllib.parse.quote(q)}&hl=vi&gl=vn"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        soup = BeautifulSoup(resp.read(), 'html.parser')
    
    # In modern Google, organic results are inside divs with jscontroller or class
    # Let us find all a tags that have href starting with http and not google.com
    anchors = soup.find_all('a', href=True)
    domains = []
    for a in anchors:
        href = a['href']
        if href.startswith('http') and 'google.com' not in href and 'gstatic.com' not in href:
            text = a.get_text(strip=True)[:40]
            if text and not any(href == d[0] for d in domains):
                domains.append((href, text))
    
    print(f"\n==================== Google SERP: '{q}' ====================")
    for i, (href, text) in enumerate(domains[:12], 1):
        print(f"  {i}. {href} [{text}]")


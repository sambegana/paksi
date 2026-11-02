"""Kumpulkan semua judul berita yang memuat 'walhi' dari Google News RSS.
Jendela 2 hari agar tidak mencapai batas 100 hasil per kueri.
Pakai: python3 collect_walhi.py korpus_walhi_raw.json
"""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, datetime as dt, time, sys
OUT = sys.argv[1]
start, end, step = dt.date(2026, 6, 1), dt.date(2026, 11, 3), 2
res = []
d = start
while d < end:
    e = min(d + dt.timedelta(days=step), end)
    q = f"walhi after:{d} before:{e}"
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": q, "hl": "id", "gl": "ID", "ceid": "ID:id"})
    for _ in range(3):
        try:
            x = urllib.request.urlopen(url, timeout=30).read(); break
        except Exception:
            time.sleep(3)
    items = [{"title": i.findtext("title"), "date": i.findtext("pubDate"), "src": i.findtext("source"), "link": i.findtext("link")}
             for i in ET.fromstring(x).iter("item")]
    res.append({"from": str(d), "to": str(e), "n": len(items), "items": items})
    print(d, len(items), flush=True)
    time.sleep(0.4)
    d = e
json.dump(res, open(OUT, "w"), ensure_ascii=False)

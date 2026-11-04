"""Kueri khusus per isu: walhi + kata kunci isu (dicocokkan Google News ke judul ATAU isi berita).
Jendela 7 hari. Pakai: python3 collect_per_isu.py korpus_per_isu_raw.json"""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, datetime as dt, time, sys
Q = {
 "Pesisir & Laut": 'walhi (pesisir OR nelayan OR reklamasi OR mangrove OR "pasir laut" OR "pulau kecil" OR "pulau-pulau kecil" OR tambak OR perairan OR "wilayah tangkap" OR abrasi OR kepulauan OR KKP)',
 "Hutan & Kebun": 'walhi (hutan OR karhutla OR sawit OR deforestasi OR perkebunan OR "masyarakat adat" OR konsesi)',
 "Tambang & Energi": 'walhi (tambang OR nikel OR "batu bara" OR smelter OR PLTU OR geotermal OR "panas bumi" OR energi OR PLTN)',
 "Perkotaan & Tata Ruang": 'walhi (kota OR "tata ruang" OR RTRW OR sampah OR TPA OR banjir OR "data center" OR PSN OR "polusi udara")',
 "Iklim & Global": 'walhi (iklim OR emisi OR karbon OR COP31 OR NDC OR "perdagangan karbon" OR "dana iklim")',
 "Ekosistem Esensial & Pangan": 'walhi (pangan OR "food estate" OR petani OR gambut OR karst OR DAS OR sungai OR "mata air" OR "cetak sawah")',
}
res = {}
for isu, q in Q.items():
    d = dt.date(2026, 6, 1); res[isu] = []
    while d < dt.date(2026, 11, 3):
        e = min(d + dt.timedelta(days=7), dt.date(2026, 11, 3))
        url = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": f"{q} after:{d} before:{e}", "hl": "id", "gl": "ID", "ceid": "ID:id"})
        for _ in range(3):
            try: x = urllib.request.urlopen(url, timeout=30).read(); break
            except Exception: time.sleep(3)
        items = [{"title": i.findtext("title"), "date": i.findtext("pubDate"), "src": i.findtext("source"), "link": i.findtext("link")} for i in ET.fromstring(x).iter("item")]
        res[isu].append({"from": str(d), "to": str(e), "n": len(items), "items": items})
        time.sleep(0.4); d = e
    print(isu, sum(w["n"] for w in res[isu]), "capped:", sum(w["n"] >= 100 for w in res[isu]), flush=True)
json.dump({"kueri": Q, "hasil": res}, open(sys.argv[1], "w"), ensure_ascii=False)

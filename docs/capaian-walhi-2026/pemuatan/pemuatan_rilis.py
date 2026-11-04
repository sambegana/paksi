"""Ukur pemuatan satu rilis: cari berita kasus -> buka isi -> cek sebutan WALHI dan penutur.
Pakai: python3 pemuatan_rilis.py <tanggal YYYY-MM-DD> <out.json> <kueri1> [kueri2 ...]"""
import sys, json, re, time, datetime as dt, urllib.request, urllib.parse, xml.etree.ElementTree as ET
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gn_decode import decode
import trafilatura
d0 = dt.date.fromisoformat(sys.argv[1]); out = sys.argv[2]; queries = sys.argv[3:]
A, B = d0 - dt.timedelta(days=1), d0 + dt.timedelta(days=15)
NAMA = ["Uli Arta Siagian", "Boy Jerry Even Sembiring", "Teo Reffelsen", "Dana Prima Tarigan", "Mida Saragih", "Musdalifah Jamal",
        "Wahyu Eka", "Umi Ma'rufah", "Umi Ma’rufah", "Patria Rizky", "Faisal Ratuela", "Christine Constanta", "Fanny Tri Jambore", "Parid Ridwanuddin"]
items = {}
for q in queries:
    u = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": f"{q} after:{A} before:{B}", "hl": "id", "gl": "ID", "ceid": "ID:id"})
    for i in ET.fromstring(urllib.request.urlopen(u, timeout=30).read()).iter("item"):
        t = i.findtext("title"); src = i.findtext("source") or ""
        if src.strip().upper() == "WALHI": continue
        items.setdefault(t, {"judul": t, "media": src, "tanggal": i.findtext("pubDate")[5:16], "link": i.findtext("link"), "kueri": []})["kueri"].append(q)
    time.sleep(0.5)
for it in items.values():
    try:
        url = decode(it["link"]); it["url"] = url
        html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "walhi-media-monitor/0.1 (riset pemberitaan; non-komersial)"}), timeout=25).read()
        txt = trafilatura.extract(html, include_comments=False) or ""
        it["teks_terbaca"] = len(txt) > 300
        it["walhi_di_isi"] = len(re.findall(r"walhi", txt, re.I))
        it["walhi_di_judul"] = bool(re.search(r"walhi", it["judul"], re.I))
        it["penutur_walhi"] = [n for n in NAMA if n.lower() in txt.lower()]
        m = re.search(r"[^.]*walhi[^.]*\.", txt, re.I); it["kalimat_walhi"] = m.group(0).strip()[:300] if m else ""
    except Exception as e:
        it["teks_terbaca"] = False; it["galat"] = str(e)[:120]
    time.sleep(0.6)
json.dump(list(items.values()), open(out, "w"), ensure_ascii=False, indent=1)
for it in sorted(items.values(), key=lambda x: x["tanggal"]):
    flag = ("TIDAK TERBACA" if not it.get("teks_terbaca") else f"WALHI x{it['walhi_di_isi']}") 
    print(f"{it['tanggal']} | {it['media'][:18]:18s} | {flag:14s} | {','.join(it.get('penutur_walhi', []))[:40]:40s} | {it['judul'][:80]}")

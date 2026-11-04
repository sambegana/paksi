"""Sapu berita lewat NAMA pengkampanye (termasuk salah ketik) untuk satu periode.

Pakai: python3 -I sapu_nama.py --roster roster.json --mulai 2026-11-01 --selesai 2026-11-30 --out sapu_nama.json

1. Untuk tiap orang di roster, kueri Google News per minggu dengan beberapa varian ejaan nama.
2. Isi berita diambil (tanpa menembus proteksi bot). Nama dicari di isi secara fleksibel: cocok bila ada
   rangkaian kata dengan kemiripan >= 0,85 terhadap salah satu varian (menangkap "Mida Saragi", "Styawan").
3. Kueri yang tetap gagal dicatat di "kueri_gagal".
"""
import datetime as dt, difflib, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gn_decode import decode  # noqa: E402
import trafilatura  # noqa: E402

UA = {"User-Agent": "walhi-media-monitor/0.1 (riset pemberitaan; non-komersial)"}
ORANG = {}  # diisi dari --roster


KUERI_GAGAL = []  # kueri yang tetap gagal setelah diulang; WAJIB dilaporkan, bukan dianggap 0 hasil


def rss(q, a, b):
    u = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": f"{q} after:{a} before:{b}", "hl": "id", "gl": "ID", "ceid": "ID:id"})
    for tunggu in (5, 20, 60, 120):
        try:
            return list(ET.fromstring(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()).iter("item"))
        except Exception:
            time.sleep(tunggu)  # 503/429 = dibatasi Google; tunggu makin lama
    KUERI_GAGAL.append(f"{q} | {a}..{b}")
    print("PERINGATAN: kueri gagal:", q, a, b, flush=True)
    return []


def cocok_fleksibel(teks, varian, ambang=0.85):
    kata = re.findall(r"[a-z'’]+", teks.lower().replace("’", "'"))
    for v in varian:
        n = len(v.split())
        for i in range(len(kata) - n + 1):
            seg = " ".join(kata[i:i + n])
            r = difflib.SequenceMatcher(None, seg, v).ratio()
            if r >= ambang:
                return seg, round(r, 2)
    return None


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--roster", required=True); ap.add_argument("--mulai", required=True); ap.add_argument("--selesai", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(); out = a.out
    for nama, v in json.load(open(a.roster)).items():
        ORANG[nama] = (v["bidang"] or v["peran"], v["kueri"], v["cocok"])
    start, end = dt.date.fromisoformat(a.mulai), dt.date.fromisoformat(a.selesai) + dt.timedelta(days=1)
    items = {}
    for nama, (bidang, kueri, _) in ORANG.items():
        d = start
        while d < end:
            e = min(d + dt.timedelta(days=7), end)
            for q in kueri:
                for i in rss(q, d, e):
                    t = i.findtext("title"); src = (i.findtext("source") or "").strip()
                    if src.upper() == "WALHI":
                        continue
                    it = items.setdefault(t, {"judul": t, "media": src, "tanggal": i.findtext("pubDate")[5:16], "link": i.findtext("link"), "dicari_lewat": set()})
                    it["dicari_lewat"].add(nama)
                time.sleep(0.4)
            d = e
        print(nama, "->", sum(nama in it["dicari_lewat"] for it in items.values()), flush=True)
    for it in items.values():
        it["dicari_lewat"] = sorted(it["dicari_lewat"])
        try:
            it["url"] = decode(it.pop("link"))
            html = urllib.request.urlopen(urllib.request.Request(it["url"], headers=UA), timeout=25).read()
            txt = trafilatura.extract(html, include_comments=False) or ""
        except Exception as ex:
            txt = ""; it["galat"] = str(ex)[:100]; it.pop("link", None)
        it["teks_terbaca"] = len(txt) > 300
        it["nama_di_isi"] = {}
        if it["teks_terbaca"]:
            for nama, (_, _, var) in ORANG.items():
                m = cocok_fleksibel(txt, var)
                if m:
                    it["nama_di_isi"][nama] = {"tertulis": m[0], "kemiripan": m[1]}
            it["walhi_di_isi"] = len(re.findall("walhi", txt.lower()))
        time.sleep(0.5)
    json.dump({"orang": {k: v[0] for k, v in ORANG.items()}, "kueri_gagal": KUERI_GAGAL, "berita": list(items.values())}, open(out, "w"), ensure_ascii=False, indent=1)
    print("total berita:", len(items), "| terbaca:", sum(i["teks_terbaca"] for i in items.values()), "| kueri gagal:", len(KUERI_GAGAL))


if __name__ == "__main__":
    main()

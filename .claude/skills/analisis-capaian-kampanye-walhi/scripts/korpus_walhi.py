"""Kumpulkan korpus berita WALHI dari Google News RSS untuk satu periode.

Pakai: python3 -I korpus_walhi.py --mulai 2026-11-01 --selesai 2026-11-30 --out korpus.json

Isi korpus:
- "umum": semua item untuk kueri "walhi", jendela 2 hari (agar tidak kena batas 100 hasil per kueri).
- "per_isu": kueri "walhi (kata kunci isu)", jendela 7 hari; Google mencocokkan judul ATAU isi berita.
Kueri yang tetap gagal setelah diulang dicatat di "kueri_gagal" — laporkan, jangan dianggap 0 hasil.
Jangan jalankan bersamaan dengan sapuan besar lain (Google membalas 503).
"""
import argparse, datetime as dt, json, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

UA = {"User-Agent": "walhi-media-monitor/0.1 (riset pemberitaan; non-komersial)"}
KUERI_ISU = {
    "Pesisir & Laut": 'walhi (pesisir OR nelayan OR reklamasi OR mangrove OR "pasir laut" OR "pulau kecil" OR "pulau-pulau kecil" OR tambak OR perairan OR "wilayah tangkap" OR abrasi OR kepulauan OR KKP)',
    "Hutan & Kebun": 'walhi (hutan OR karhutla OR sawit OR deforestasi OR perkebunan OR "masyarakat adat" OR konsesi)',
    "Tambang & Energi": 'walhi (tambang OR nikel OR "batu bara" OR smelter OR PLTU OR geotermal OR "panas bumi" OR energi OR PLTN)',
    "Urban": 'walhi (kota OR "tata ruang" OR RTRW OR sampah OR TPA OR banjir OR "data center" OR PSN OR "polusi udara")',
    "Iklim & Isu Global": 'walhi (iklim OR emisi OR karbon OR COP OR NDC OR "perdagangan karbon" OR "dana iklim")',
    "Pangan & Ekosistem Esensial": 'walhi (pangan OR "food estate" OR petani OR gambut OR karst OR DAS OR sungai OR "mata air" OR "cetak sawah")',
}
GAGAL = []


def rss(q, a, b):
    u = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": f"{q} after:{a} before:{b}", "hl": "id", "gl": "ID", "ceid": "ID:id"})
    for tunggu in (5, 20, 60, 120):
        try:
            x = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()
            return [{"title": i.findtext("title"), "date": i.findtext("pubDate"), "src": i.findtext("source"), "link": i.findtext("link")}
                    for i in ET.fromstring(x).iter("item")]
        except Exception:
            time.sleep(tunggu)
    GAGAL.append(f"{q} | {a}..{b}"); print("PERINGATAN kueri gagal:", q, a, b, flush=True)
    return []


def jendela(mulai, selesai, hari):
    d = mulai
    while d <= selesai:
        e = min(d + dt.timedelta(days=hari), selesai + dt.timedelta(days=1))
        yield d, e
        d = e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mulai", required=True); ap.add_argument("--selesai", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    m, s = dt.date.fromisoformat(a.mulai), dt.date.fromisoformat(a.selesai)
    umum = []
    for d, e in jendela(m, s, 2):
        items = rss("walhi", d, e); umum.append({"from": str(d), "to": str(e), "n": len(items), "items": items})
        time.sleep(0.4)
    print("umum:", sum(w["n"] for w in umum), "| jendela kena batas 100:", sum(w["n"] >= 100 for w in umum), flush=True)
    per_isu = {}
    for isu, q in KUERI_ISU.items():
        per_isu[isu] = []
        for d, e in jendela(m, s, 7):
            items = rss(q, d, e); per_isu[isu].append({"from": str(d), "to": str(e), "n": len(items), "items": items})
            time.sleep(0.4)
        print(isu, sum(w["n"] for w in per_isu[isu]), "| kena batas:", sum(w["n"] >= 100 for w in per_isu[isu]), flush=True)
    json.dump({"periode": [a.mulai, a.selesai], "kueri_isu": KUERI_ISU, "umum": umum, "per_isu": per_isu, "kueri_gagal": GAGAL},
              open(a.out, "w"), ensure_ascii=False)
    print("selesai | kueri gagal:", len(GAGAL))


if __name__ == "__main__":
    main()

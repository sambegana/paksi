"""Ukur pemuatan dan cari kandidat respons pemerintah untuk SATU rilis.

Pakai:
  python3 -I pemuatan_rilis.py --id R16 --tanggal 2026-09-24 --out hasil/R16.json \
      --kueri 'walhi "tambak pantura"' --kueri '"revitalisasi tambak" pantura' \
      --jejaring "KOMPI" --jejaring "KIARA" [--hari 14]

Langkah:
1. Kueri Google News per kasus, rentang H-1 s.d. H+hari (default 14). Item dari kanal WALHI dibuang.
2. Tautan Google News diurai ke URL asli; isi berita diambil dengan trafilatura.
   Situs yang memblokir pembaca otomatis TIDAK ditembus; untuk itu dipakai tanda indeks:
   apakah item muncul di kueri yang memuat kata "walhi".
3. Dari isi berita dicatat: jumlah sebutan WALHI, penutur WALHI, jejaring yang disebut,
   dan kalimat yang memuat lembaga/pejabat pemerintah (kandidat bukti respons).
"""
import argparse, datetime as dt, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gn_decode import decode  # noqa: E402
import trafilatura  # noqa: E402

UA = {"User-Agent": "walhi-media-monitor/0.1 (riset pemberitaan; non-komersial)"}
NAMA = ["Uli Arta Siagian", "Boy Jerry Even Sembiring", "Teo Reffelsen", "Dana Prima Tarigan", "Mida Saragih",
        "Musdalifah Jamal", "Wahyu Eka", "Umi Ma'rufah", "Umi Ma’rufah", "Patria Rizky", "Faisal Ratuela",
        "Christine Constanta", "Fanny Tri Jambore", "Parid Ridwanuddin"]
PEMERINTAH = (r"\b(presiden|istana|wapres|menteri|menko|wamen|dirjen|direktur jenderal|kementerian|kemen[a-z]+|kkp|klh|"
              r"kemenhut|esdm|atr/bpn|bpn|komdigi|kemendagri|polri|polda|polres|kapolri|kapolda|bareskrim|"
              r"gubernur|pemprov|bupati|pemkab|wali ?kota|pemkot|dprd?|komisi [ivx]+|bp batam|boppj|bpgmn|bnpb|"
              r"kejaksaan|kejagung|satgas|juru bicara|jubir|kepala dinas|dinas|dlh)\b")
VERBA = r"\b(kata|ujar|ucap|tegas|menegaskan|menyatakan|mengatakan|menjelaskan|menyebut|membantah|menanggapi|merespons|menjawab|berjanji|memastikan|mengklaim)\b"


def rss(q, a, b):
    u = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": f"{q} after:{a} before:{b}", "hl": "id", "gl": "ID", "ceid": "ID:id"})
    for _ in range(3):
        try:
            return list(ET.fromstring(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()).iter("item"))
        except Exception:
            time.sleep(3)
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True); ap.add_argument("--tanggal", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--kueri", action="append", required=True); ap.add_argument("--jejaring", action="append", default=[])
    ap.add_argument("--hari", type=int, default=14)
    a = ap.parse_args()
    d0 = dt.date.fromisoformat(a.tanggal)
    A, B = d0 - dt.timedelta(days=1), d0 + dt.timedelta(days=a.hari + 1)
    items = {}
    for q in a.kueri:
        for i in rss(q, A, B):
            t = i.findtext("title"); src = (i.findtext("source") or "").strip()
            if src.upper() == "WALHI":
                continue
            it = items.setdefault(t, {"judul": t, "media": src, "tanggal": i.findtext("pubDate")[5:16], "link": i.findtext("link"), "kueri": []})
            it["kueri"].append(q)
        time.sleep(0.5)
    for it in items.values():
        it["indeks_walhi"] = any("walhi" in q.lower() for q in it["kueri"])
        it["walhi_di_judul"] = bool(re.search("walhi", it["judul"], re.I))
        try:
            it["url"] = decode(it["link"])
            html = urllib.request.urlopen(urllib.request.Request(it["url"], headers=UA), timeout=25).read()
            txt = trafilatura.extract(html, include_comments=False) or ""
        except Exception as e:
            txt = ""; it["galat"] = str(e)[:120]
        it["teks_terbaca"] = len(txt) > 300
        if it["teks_terbaca"]:
            low = txt.lower()
            it["walhi_di_isi"] = len(re.findall("walhi", low))
            it["penutur_walhi"] = [n for n in NAMA if n.lower() in low]
            it["jejaring_di_isi"] = [j for j in a.jejaring if j.lower() in low]
            kal = re.split(r"(?<=[.!?”\"])\s+", txt)
            it["kalimat_pemerintah"] = [k.strip()[:280] for k in kal if re.search(PEMERINTAH, k, re.I) and re.search(VERBA, k, re.I)][:6]
            it["kalimat_walhi"] = [k.strip()[:240] for k in kal if "walhi" in k.lower()][:2]
        it.pop("link", None)
        time.sleep(0.6)
    res = {"id": a.id, "tanggal": a.tanggal, "rentang": [str(A), str(B)], "kueri": a.kueri, "jejaring": a.jejaring,
           "jumlah_berita": len(items), "berita": sorted(items.values(), key=lambda x: x["tanggal"])}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(res, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(f"{a.id}: {len(items)} berita | terbaca {sum(i['teks_terbaca'] for i in items.values())} | "
          f"WALHI (isi/indeks) {sum(bool(i.get('walhi_di_isi')) or i['indeks_walhi'] for i in items.values())} | "
          f"jejaring {sum(bool(i.get('jejaring_di_isi')) for i in items.values())} | "
          f"kalimat pemerintah {sum(len(i.get('kalimat_pemerintah', [])) for i in items.values())}")


if __name__ == "__main__":
    main()

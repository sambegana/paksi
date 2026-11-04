"""Sapu berita lewat NAMA pengkampanye (termasuk salah ketik), 1 Agu – 2 Nov 2026.

Pakai: python3 -I sapu_nama.py <keluaran.json>

1. Untuk tiap orang, kueri Google News per minggu dengan beberapa varian ejaan nama.
2. Isi berita diambil (tanpa menembus proteksi bot). Nama dicari di isi secara fleksibel:
   cocok bila ada rangkaian kata yang kemiripannya >= 0,85 dengan salah satu varian
   (menangkap salah ketik seperti "Mida Saragi" atau "Wahyu Eka Styawan").
3. Berita yang tidak terbaca tetap dicatat, dengan tanda bahwa nama hanya cocok lewat indeks Google.
"""
import datetime as dt, difflib, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gn_decode import decode  # noqa: E402
import trafilatura  # noqa: E402

UA = {"User-Agent": "walhi-media-monitor/0.1 (riset pemberitaan; non-komersial)"}
ORANG = {  # nama: (bidang, [varian kueri], [varian untuk pencocokan isi])
    "Mida Saragih": ("Pesisir & Laut", ['"Mida Saragih"', '"Mida Saragi"', 'Mida walhi pesisir'], ["mida saragih"]),
    "Umi Ma'rufah": ("Hutan & Kebun", ['"Umi Ma\'rufah"', '"Umi Marufah"', '"Umi Ma’rufah"'], ["umi ma'rufah", "umi marufah"]),
    "Wahyu Eka Setyawan": ("Urban", ['"Wahyu Eka Setyawan"', '"Wahyu Eka Styawan"', '"Wahyu Eka Setiawan"', '"Wahyu Eka" walhi'], ["wahyu eka setyawan"]),
    "Musdalifah Jamal": ("Pangan & Ekosistem Esensial", ['"Musdalifah Jamal"', '"Musdalifa Jamal"', 'Musdalifah walhi'], ["musdalifah jamal"]),
    "Patria Rizky Ananda": ("Iklim & Isu Global", ['"Patria Rizky"', '"Patria Rizki"', 'Patria walhi iklim'], ["patria rizky ananda", "patria rizky"]),
    "Faisal Ratuela": ("Tambang & Energi", ['"Faisal Ratuela"', '"Faizal Ratuela"', 'Ratuela walhi'], ["faisal ratuela"]),
    "Uli Arta Siagian": ("Pimpinan (Kadiv Kampanye)", ['"Uli Arta Siagian"', '"Uli Artha Siagian"', '"Uli Siagian" walhi'], ["uli arta siagian", "uli siagian"]),
    "Boy Jerry Even Sembiring": ("Pimpinan (Direktur Eksekutif)", ['"Boy Jerry Even Sembiring"', '"Boy Even Sembiring"', '"Boy Sembiring" walhi'], ["boy jerry even sembiring", "boy even sembiring"]),
    "Teo Reffelsen": ("Pimpinan (Manajer Hukum)", ['"Teo Reffelsen"', '"Teo Refelsen"', 'Reffelsen walhi'], ["teo reffelsen"]),
    "Dana Prima Tarigan": ("Pimpinan (Kadep Komstrat)", ['"Dana Prima Tarigan"', '"Dana Tarigan" walhi'], ["dana prima tarigan"]),
    "Christine Constanta": ("Respons cepat", ['"Christine Constanta"', '"Christin Constanta"'], ["christine constanta"]),
}


def rss(q, a, b):
    u = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": f"{q} after:{a} before:{b}", "hl": "id", "gl": "ID", "ceid": "ID:id"})
    for _ in range(3):
        try:
            return list(ET.fromstring(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()).iter("item"))
        except Exception:
            time.sleep(3)
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


def main(out):
    start, end = dt.date(2026, 8, 1), dt.date(2026, 11, 3)
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
    json.dump({"orang": {k: v[0] for k, v in ORANG.items()}, "berita": list(items.values())}, open(out, "w"), ensure_ascii=False, indent=1)
    print("total berita:", len(items), "| terbaca:", sum(i["teks_terbaca"] for i in items.values()))


if __name__ == "__main__":
    main(sys.argv[1])

"""Periode: 1 Agustus – 31 Oktober 2026.
Kaitkan siaran pers WALHI dengan pemberitaan media.

Masukan : siaran_pers.csv (dikode manual), korpus_walhi_raw.json, korpus_per_isu_raw.json
Keluaran: pemuatan_siaran_pers.csv  (berapa berita media memuat tiap siaran pers)
          berita_per_isu.json        (jumlah berita per isu, versi lama vs versi baru)
Aturan:
- Berita media = item korpus yang bukan dari kanal WALHI. Semua item berasal dari kueri yang memuat
  "walhi", jadi WALHI disebut di judul atau isi.
- Satu berita "memuat" sebuah siaran pers bila judulnya cocok dengan salah satu kata kunci rilis
  (A+B = keduanya harus ada) dan terbit 1 hari sebelum s.d. 21 hari sesudah rilis. Bila cocok dengan
  beberapa rilis, berita diberikan ke rilis terdekat sebelumnya.
- Isu berita = isu dari kata kunci isu (dengan aturan lokus untuk pesisir) DITAMBAH isu utama dan isu
  kedua dari siaran pers yang dimuatnya. Satu berita boleh masuk lebih dari satu isu.
"""
import csv, json, os, re, sys, email.utils, datetime as dt
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import classify  # noqa: E402

AWAL, AKHIR = dt.date(2026, 8, 1), dt.date(2026, 10, 31)  # periode analisis
dalam = lambda d: AWAL <= d <= AKHIR

KODE = {"PL": "Pesisir & Laut", "HK": "Hutan & Kebun", "TE": "Tambang & Energi", "PT": "Perkotaan & Tata Ruang",
        "IG": "Iklim & Global", "EP": "Ekosistem Esensial & Pangan", "LN": "Lintas isu", "KL": "Kelembagaan"}
ISU6 = [KODE[k] for k in ("PL", "HK", "TE", "PT", "IG", "EP")]

# Aturan lokus pesisir: laut, pesisir, perairan, pulau kecil (bukan pulau besar), kasus pesisir dari siaran pers.
PESISIR_LOKUS = (r"perairan|pulau-pulau kecil|pulau kecil|daerah kepulauan|pulau(?!\s+(jawa|sumatera|sumatra|kalimantan|"
                 r"sulawesi|papua|bali|borneo)\b)\s+[a-z]|rempang|\bobi\b|kawasi|gelasa|batu beriga|pantura|giant sea wall|"
                 r"tanggul laut|wilayah tangkap|petambak|pasir laut|\bbopp|otorita pantai|batam")
ISU_RE = dict(classify.ISU)
ISU_RE["Pesisir & Laut"] = ISU_RE["Pesisir & Laut"] + "|" + PESISIR_LOKUS


def match_kw(kw, title):
    if not kw:
        return False
    t = classify.bersih(title).lower()
    for alt in kw.split("|"):
        if all(re.search(part.strip(), t) for part in alt.split("+")):
            return True
    return False


def load_media():
    g = json.load(open(os.path.join(HERE, "korpus_walhi_raw.json")))
    p = json.load(open(os.path.join(HERE, "korpus_per_isu_raw.json")))["hasil"]
    seen = {}
    def add(i, asal):
        if (i["src"] or "").strip().upper() == "WALHI":
            return
        t = i["title"]
        d = email.utils.parsedate_to_datetime(i["date"]).date()
        if t not in seen:
            seen[t] = {"title": t, "date": d, "src": i["src"], "asal": set()}
        seen[t]["asal"].add(asal)
    for w in g:
        for i in w["items"]:
            add(i, "umum")
    for isu, ws in p.items():
        for w in ws:
            for i in w["items"]:
                add(i, isu)
    return list(seen.values())


rel = [r for r in csv.DictReader(open(os.path.join(HERE, "siaran_pers.csv")))]
for r in rel:
    r["d"] = dt.date.fromisoformat(r["tanggal"])
rel = [r for r in rel if dalam(r["d"])]
aktif = [r for r in rel if r["jenis"] in ("rilis", "kajian")]
media = [m for m in load_media() if dalam(m["date"])]

# --- pemuatan per siaran pers ---
muat = defaultdict(list)
for m in media:
    cand = [r for r in aktif if match_kw(r["kata_kunci"], m["title"]) and -1 <= (m["date"] - r["d"]).days <= 21]
    if cand:
        best = min(cand, key=lambda r: abs((m["date"] - r["d"]).days) if m["date"] >= r["d"] else 99)
        muat[id(best)].append(m)
        m["rilis"] = best

rows = []
for r in aktif:
    ms = muat[id(r)]
    rows.append({"tanggal": r["tanggal"], "judul": r["judul"], "isu_utama": KODE[r["isu_utama"]],
                 "isu_kedua": KODE.get(r["isu_kedua"], ""), "kata_kunci": r["kata_kunci"],
                 "diukur": "ya" if r["kata_kunci"] else "tidak (tanpa kata kunci khas)",
                 "berita_media": len(ms), "judul_memuat_walhi": sum(bool(re.search("walhi", x["title"], re.I)) for x in ms),
                 "media_berbeda": len({x["src"] for x in ms}),
                 "contoh_judul": " || ".join(x["title"][:110] for x in ms[:3])})
with open(os.path.join(HERE, "pemuatan_siaran_pers.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# --- isu per berita: lama (kata kunci isu saja, judul memuat WALHI) vs baru ---
def isu_baru(m):
    s = {k for k, p in ISU_RE.items() if re.search(p, classify.bersih(m["title"], m["src"]), re.I)}
    r = m.get("rilis")
    if r:
        for c in (r["isu_utama"], r["isu_kedua"]):
            if c in ("PL", "HK", "TE", "PT", "IG", "EP"):
                s.add(KODE[c])
    return s

lama_items, _ = classify.load(os.path.join(HERE, "korpus_walhi_raw.json"))
lama_items = [i for i in lama_items if dalam(email.utils.parsedate_to_datetime(i["date"]).date())]
lama = Counter(k for i in lama_items for k in classify.tag(i["title"]))
baru_judul = Counter(); baru_semua = Counter(); irisan = Counter(); media_isu = defaultdict(set)
for m in media:
    s = isu_baru(m)
    in_title = bool(re.search("walhi", classify.bersih(m["title"], m["src"]), re.I))
    for k in s:
        baru_semua[k] += 1; media_isu[k].add(m["src"])
        if in_title:
            baru_judul[k] += 1
    if "Pesisir & Laut" in s:
        for k in s - {"Pesisir & Laut"}:
            irisan[k] += 1

prod = Counter(KODE[r["isu_utama"]] for r in aktif)
prod2 = Counter(KODE[r["isu_kedua"]] for r in aktif if r["isu_kedua"])
pick = defaultdict(lambda: [0, 0, 0])  # rilis diukur, rilis dimuat >=1, total berita
for row in rows:
    if row["diukur"] == "ya":
        p = pick[row["isu_utama"]]; p[0] += 1; p[1] += row["berita_media"] > 0; p[2] += row["berita_media"]

out = {"jumlah_media": len(media), "rilis_total": len(rel), "rilis_aktif": len(aktif),
       "dikecualikan": Counter(r["jenis"] for r in rel if r not in aktif),
       "produksi_utama": prod, "produksi_kedua": prod2, "pemuatan": {k: v for k, v in pick.items()},
       "lama_judul_walhi": lama, "baru_judul_walhi": baru_judul, "baru_semua_berita": baru_semua,
       "media_berbeda": {k: len(v) for k, v in media_isu.items()}, "irisan_pesisir": irisan,
       "berita_terkait_rilis": sum(1 for m in media if m.get("rilis"))}
json.dump(out, open(os.path.join(HERE, "berita_per_isu.json"), "w"), ensure_ascii=False, indent=1, default=list)

print("berita media unik:", len(media), "| terkait siaran pers:", out["berita_terkait_rilis"])
print("siaran pers:", len(rel), "aktif:", len(aktif), "dikecualikan:", dict(out["dikecualikan"]))
print(f"{'isu':28s} rilis(utama) +kedua | diukur dimuat% berita/rilis | judul lama -> baru | semua berita")
for k in ISU6 + ["Lintas isu"]:
    p = pick.get(k, [0, 0, 0])
    print(f"{k:28s} {prod.get(k,0):5d} {prod2.get(k,0):6d}   | {p[0]:3d} {100*p[1]/max(p[0],1):5.0f}% {p[2]/max(p[0],1):6.1f}  | "
          f"{lama.get(k,0):4d} -> {baru_judul.get(k,0):4d} | {baru_semua.get(k,0):4d}")
print("irisan pesisir:", dict(irisan))

"""Susun data final respons pemerintah atas rilis WALHI Agustus–Oktober 2026.

Masukan : rilis_base.csv, pengodean/respons_rilis_agu_okt_mentah.json (hasil multi-agen + verifikasi),
          pemuatan/hasil/P14.json (dikode terpisah)
Keluaran: respons_final.csv (satu baris per rilis), tindakan_unik.csv (outcome tanpa hitungan ganda),
          ringkasan_per_isu.json

Keputusan penyunting (dicatat di sini supaya bisa diperiksa):
- Skor akhir = skor_final pemeriksa adversarial.
- R37 (desakan ke Singapura): lembaga dituju pemerintah asing -> dikeluarkan dari statistik respons
  pemerintah Indonesia, dicatat terpisah. Panel Singapura sudah berproses sejak 23–25 Okt (sebelum rilis).
- R28 = rilis offset PTAR (menurut rekap Excel) = P10 versi publik -> digabung; P10 dibuang sebagai duplikat.
- R22 (DRAFT AAL RSPO): tidak ada bukti terbit -> tidak dihitung.
- Tindakan nyata (skor >= 3) diberi tingkat kecocokan dengan inti tuntutan: inti / sebagian / generik.
  "Generik" = tindakan umum karhutla yang tidak menyentuh inti tuntutan; tetap skor 3 tetapi tidak dihitung
  sebagai tindakan nyata untuk isu tersebut.
- Pimpinan dan Hukum (Boy, Uli, Dana, Teo, Christine, Melva, Tubagus) tidak dikreditkan sebagai PJ isu.
"""
import csv, json, os, statistics
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PIMPINAN = {"Boy Jerry Even Sembiring", "Uli Arta Siagian", "Dana Prima Tarigan", "Teo Reffelsen", "Christine Constanta", "Melva Harahap", "Tubagus Soleh Ahmadi"}
KAMPANYE = {"Mida Saragih": "Pesisir & Laut", "Umi Ma'rufah": "Hutan & Kebun", "Umi Ma’rufah": "Hutan & Kebun", "Wahyu Eka": "Urban",
            "Musdalifah Jamal": "Pangan & Ekosistem Esensial", "Patria Rizky": "Iklim & Isu Global", "Faisal Ratuela": "Tambang & Energi"}
KECOCOKAN = {"R02": "sebagian", "R05": "sebagian", "R07": "inti", "R09": "sebagian", "P07": "inti", "P08": "generik", "R21": "inti",
             "R25": "inti", "R35": "inti", "P09": "sebagian", "R20": "generik"}
TINDAKAN = [  # outcome unik -> rilis yang tuntutannya disentuh
    ("T1", "2026-09-03", "Kemenhut", "Membekukan izin 5 PBPH di Kalbar (371.560 ha), termasuk Mayawana", "pembekuan izin", "R05;R07",
     "https://www.betahita.id/berita/12326/lima-korporasi-hutan-di-kalbar-dibekukan-termasuk-mayawana", "konvergensi"),
    ("T2", "2026-09-21", "Kemenhut", "Mencabut izin 5 perusahaan terkait karhutla; 4 di antaranya ada di daftar laporan WALHI", "pencabutan izin", "R02;R05;R07;P07",
     "https://www.betahita.id/berita/12401/izin-5-perusahaan-kembali-dicabut-karena-karhutla", "menyentuh daftar WALHI"),
    ("T3", "2026-09-13", "KLH", "Menyegel 50 badan usaha terkait karhutla (27 ribu ha konsesi terbakar); berlanjut hingga 68 konsesi per Oktober", "penyegelan", "R07;P08;R20",
     "https://mediaindonesia.com/humaniora/932875/27-ribu-hektare-konsesi-terbakar-klh-segel-50-badan-usaha-terkait-karhutla", "konvergensi; tanggal mulai belum terverifikasi"),
    ("T4", "2026-10-21", "Kemenhut", "Membekukan izin 6 PBPH lagi disertai paksaan pemulihan (total 32 perusahaan disanksi)", "pembekuan izin", "R07;P09",
     "https://katadata.co.id/berita/nasional/6ad8994f68262/pemerintah-bekukan-enam-perusahaan-penyebab-karhutla", "konvergensi"),
    ("T5", "2026-10-29", "Polri (Bareskrim)", "Menetapkan korporasi tersangka karhutla (9 → 11 → 20, termasuk 4 PMA) dan mengusulkan pencabutan izin 23 korporasi; nama tidak dibuka", "penetapan tersangka", "R02;R05;R25",
     "https://katadata.co.id/amp/berita/nasional/6ae3056c011da/polri-umumkan-20-perusahaan-tersangka-karhutla-empat-berstatus-modal-asing", "konvergensi"),
    ("T6", "2026-10-23", "Kementerian Hukum", "Menyerahkan seluruh data pemilik manfaat korporasi terduga karhutla kepada aparat penegak hukum", "penyerahan data/penyidikan", "R35",
     "https://nasional.kontan.co.id/news/walhi-desak-penegakan-hukum-karhutla-sasar-pemilik-manfaat-korporasi", "searah kajian Siapa di Balik Api"),
    ("T7", "2026-10-15", "Polda Kalsel", "Menaikkan laporan WALHI Kalsel ke penyidikan; 4 korporasi ditetapkan tersangka (20 Okt)", "penyidikan/penetapan tersangka", "R21",
     "", "langsung ke WALHI (Kapolda menyebut laporan WALHI Kalsel)"),
    ("T8", "2026-09-01", "Pemprov Kalteng, Pemkot Palangka Raya", "Membuka rumah oksigen gratis (2 lokasi provinsi; 43 titik kota) dan bus oksigen gratis bagi korban asap", "layanan kesehatan", "R09",
     "https://infopublik.id/kategori/prioritas-nasional-2026/985772/kabut-asap-mencekam-rumah-oksigen-dibuka-palangka-raya", "konvergensi; tanpa evakuasi dan jaminan pengobatan menyeluruh"),
]
JENIS = {0: "tidak ada respons", 1: "ditolak", 2: "diakui/dijanjikan", 3: "tindakan parsial", 4: "dipenuhi"}

base = {r["id"]: r for r in csv.DictReader(open(os.path.join(HERE, "rilis_base.csv")))}
raw = json.load(open(os.path.join(HERE, "pengodean", "respons_rilis_agu_okt_mentah.json")))
kode = {}
for g in raw:
    ver = {x["id"]: x for x in g["verifikasi"]["rilis"]}
    for k in g["kode"]["rilis"]:
        v = ver[k["id"]]
        k["skor_final"] = v["skor_final"]; k["alasan_verifikasi"] = v["alasan"]; k["keyakinan_final"] = v["keyakinan"]
        k["respons"] = k["respons"] + v["respons_tambahan"]
        kode[k["id"]] = k
p14 = json.load(open(os.path.join(HERE, "pemuatan", "hasil", "P14.json")))
kode["P14"] = {"id": "P14", "tuntutan_ringkas": base["P14"]["tuntutan_utama"], "lembaga_dituju": base["P14"]["lembaga_dituju"],
               "berita_kasus": 3, "berita_memuat_walhi": 3, "berita_jejaring_tanpa_walhi": 0, "berita_kontra": 0,
               "penutur_terdeteksi": sorted({n for b in p14["berita"] for n in b.get("penutur_walhi", [])}), "jejaring_terdeteksi": [],
               "respons": [], "skor_final": 0, "hari_ke_respons": -1, "konvergensi": False, "keyakinan_final": "sedang",
               "alasan_verifikasi": "Tidak ditemukan tanggapan BOPPJ/Kemenko Infrastruktur atas kritik segmen 3.3 setelah 11 Sep. Pernyataan Presiden 16 Sep (GSW mulai 2027) bukan tanggapan atas tuntutan.",
               "catatan": "Dikode penyunting; 3 berita relevan (Betahita, Suara, Kompasiana) dari 6 yang terkumpul."}
kode["R28"] = dict(kode["P10"], id="R28", catatan="Digabung dengan P10 (rilis offset PTAR). " + kode["P10"]["catatan"])
kode["P15"] = {"id": "P15", "tuntutan_ringkas": base["P15"]["tuntutan_utama"], "lembaga_dituju": base["P15"]["lembaga_dituju"],
               "berita_kasus": 0, "berita_memuat_walhi": 0, "berita_jejaring_tanpa_walhi": 0, "berita_kontra": 0, "penutur_terdeteksi": [],
               "jejaring_terdeteksi": [], "respons": [], "skor_final": 0, "hari_ke_respons": -1, "konvergensi": False, "keyakinan_final": "rendah",
               "alasan_verifikasi": "Tidak ditemukan jejak publik rilis maupun tanggapan BOPPJ/KLH atas kritik prosedur GSW pada Oktober 2026; proyek tetap berjalan.",
               "catatan": "Dikode penyunting dari daftar divisi; tanggal pasti belum diketahui."}
kode["P16"] = dict(kode["P05"], id="P16", catatan="Satu tuntutan dengan P05 (RUU Daerah Kepulauan); kode respons mengikuti P05. " + kode["P05"].get("catatan", ""))


def kelompok_penutur(rid, k):
    b = base[rid]
    m = b["masuk_per_isu"]
    if rid == "R28":
        return "pimpinan/Hukum"  # rekap Excel: dasar topik, suara Uli & Dana
    if m == "ya":
        return "pengkampanye"
    if m.startswith("ya ("):
        return "pimpinan/Hukum"
    if m.startswith("catatan"):
        return "catatan lembaga"
    if m.startswith("tunda"):
        return "tidak dihitung"
    terdeteksi = k.get("penutur_terdeteksi", []) if k else []
    if any(any(n.startswith(p.split()[0]) and p in n or n in p for p in KAMPANYE) for n in terdeteksi):
        return "pengkampanye (dari isi berita)"
    if any(n in PIMPINAN for n in terdeteksi):
        return "pimpinan/Hukum (dari isi berita)"
    return "penutur tidak diketahui"


rows = []
for rid, b in base.items():
    if rid == "P10":
        continue
    k = kode.get(rid)
    kel = kelompok_penutur(rid, k)
    status = "dihitung"
    if b.get("daftar_divisi") == "tidak":
        status = "catatan: di luar daftar divisi"
    elif rid == "R37":
        status = "catatan: pemerintah asing"
    elif kel in ("catatan lembaga",) or b["jenis_tuntutan"] == "umum":
        status = "catatan: lembaga/tuntutan umum"
    elif kel == "tidak dihitung":
        status = "tidak dihitung: DRAFT"
    skor = k["skor_final"] if k else ""
    bukti = next((r["url"] for r in (k or {}).get("respons", []) if r.get("url")), "")
    isu, pj = b["bidang_topik"], (b.get("pj_bidang", "") if kel.startswith("pengkampanye") else "")
    if kel == "pengkampanye (dari isi berita)":  # aturan rekap tim: rilis masuk bidang pengkampanye yang dikutip
        for nama, bid in KAMPANYE.items():
            if any(nama in n or n in nama for n in (k or {}).get("penutur_terdeteksi", [])):
                isu, pj = bid, {"Wahyu Eka": "Wahyu Eka Styawan", "Patria Rizky": "Patria Rizky Ananda", "Umi Ma’rufah": "Umi Ma'rufah"}.get(nama, nama)
                break
    rows.append({
        "id": rid, "tanggal": b["tanggal"], "judul": b["judul_singkat"], "isu": isu, "penutur": kel, "daftar_divisi": b.get("daftar_divisi", ""), "sifat": b.get("sifat", ""),
        "pj_pengkampanye": pj,
        "status": status, "tuntutan": (k or {}).get("tuntutan_ringkas", b["tuntutan_utama"]), "lembaga_dituju": (k or {}).get("lembaga_dituju", b["lembaga_dituju"]),
        "skor": skor, "jenis_respons": JENIS.get(skor, "") if skor != "" else "tidak dikode",
        "kecocokan_tindakan": KECOCOKAN.get(rid, "") if skor != "" and skor >= 3 else "",
        "tindakan_unik": ";".join(t[0] for t in TINDAKAN if rid in t[5].split(";")),
        "hari_ke_respons": (k or {}).get("hari_ke_respons", ""), "konvergensi": (k or {}).get("konvergensi", ""),
        "berita_kasus": (k or {}).get("berita_kasus", ""), "berita_memuat_walhi": (k or {}).get("berita_memuat_walhi", ""),
        "berita_jejaring_tanpa_walhi": (k or {}).get("berita_jejaring_tanpa_walhi", ""), "berita_kontra": (k or {}).get("berita_kontra", ""),
        "penutur_di_berita": "; ".join((k or {}).get("penutur_terdeteksi", [])), "jejaring_di_berita": "; ".join((k or {}).get("jejaring_terdeteksi", [])),
        "keyakinan": (k or {}).get("keyakinan_final", ""), "bukti_utama": bukti,
        "respons_ringkas": " | ".join(f'{r["tanggal"]} {r["lembaga"]}: {r["isi"]}' for r in (k or {}).get("respons", []))[:900],
        "alasan_verifikasi": (k or {}).get("alasan_verifikasi", "")[:900],
    })
rows.sort(key=lambda r: (r["isu"], r["tanggal"]))
with open(os.path.join(HERE, "respons_final.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, list(rows[0].keys())); w.writeheader(); w.writerows(rows)
with open(os.path.join(HERE, "tindakan_unik.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["kode", "tanggal", "lembaga", "tindakan", "jenis", "rilis_terkait", "bukti", "atribusi"]); w.writerows(TINDAKAN)

# ringkasan per isu (hanya status "dihitung")
ISU = ["Hutan & Kebun", "Pesisir & Laut", "Urban", "Pangan & Ekosistem Esensial", "Iklim & Isu Global", "Tambang & Energi"]
out = {}
for isu in ISU:
    rs = [r for r in rows if r["isu"] == isu and r["status"] == "dihitung"]
    s = [r["skor"] for r in rs]
    nyata = [r for r in rs if r["skor"] >= 3 and r["kecocokan_tindakan"] in ("inti", "sebagian")]
    hari = [r["hari_ke_respons"] for r in rs if isinstance(r["hari_ke_respons"], int) and r["hari_ke_respons"] >= 0]
    out[isu] = {
        "rilis": len(rs), "oleh_pengkampanye": sum(r["penutur"].startswith("pengkampanye") for r in rs),
        "oleh_pimpinan_hukum": sum(r["penutur"].startswith("pimpinan") for r in rs), "penutur_tidak_diketahui": sum(r["penutur"] == "penutur tidak diketahui" for r in rs),
        "ada_respons": sum(v >= 1 for v in s), "ditolak": s.count(1), "dijanjikan": s.count(2), "tindakan_parsial": s.count(3), "dipenuhi": s.count(4),
        "tindakan_nyata": len(nyata), "tindakan_generik": sum(r["skor"] >= 3 and r["kecocokan_tindakan"] == "generik" for r in rs),
        "pct_ada_respons": round(100 * sum(v >= 1 for v in s) / len(s)) if s else 0, "pct_tindakan_nyata": round(100 * len(nyata) / len(s)) if s else 0,
        "median_hari_ke_respons": statistics.median(hari) if hari else None,
        "tindakan_unik": sorted({t for r in nyata for t in r["tindakan_unik"].split(";") if t}),
        "berita_kasus": sum(r["berita_kasus"] or 0 for r in rs), "berita_kontra": sum(r["berita_kontra"] or 0 for r in rs),
        "berita_memuat_walhi": sum(r["berita_memuat_walhi"] or 0 for r in rs), "berita_jejaring": sum(r["berita_jejaring_tanpa_walhi"] or 0 for r in rs),
        "rata_walhi_per_rilis": round(sum(r["berita_memuat_walhi"] or 0 for r in rs) / len(rs), 1) if rs else 0,
    }
allr = [r for r in rows if r["status"] == "dihitung"]
s = [r["skor"] for r in allr]
out["_total"] = {"rilis": len(allr), "ada_respons": sum(v >= 1 for v in s), "tindakan_nyata": sum(r["skor"] >= 3 and r["kecocokan_tindakan"] in ("inti", "sebagian") for r in allr),
                 "pct_ada_respons": round(100 * sum(v >= 1 for v in s) / len(s)), "pct_tindakan_nyata": round(100 * sum(r["skor"] >= 3 and r["kecocokan_tindakan"] in ("inti", "sebagian") for r in allr) / len(s)),
                 "tindakan_unik": len(TINDAKAN), "catatan": Counter(r["status"] for r in rows if r["status"] != "dihitung"),
                 "berita_kasus": sum(r["berita_kasus"] or 0 for r in allr), "berita_memuat_walhi": sum(r["berita_memuat_walhi"] or 0 for r in allr),
                 "berita_jejaring": sum(r["berita_jejaring_tanpa_walhi"] or 0 for r in allr), "berita_kontra": sum(r["berita_kontra"] or 0 for r in allr),
                 "median_walhi_per_skor": {lv: statistics.median([r["berita_memuat_walhi"] for r in allr if r["skor"] == lv] or [0]) for lv in range(5)},
                 "n_per_skor": {lv: sum(r["skor"] == lv for r in allr) for lv in range(5)}}
json.dump(out, open(os.path.join(HERE, "ringkasan_per_isu.json"), "w"), ensure_ascii=False, indent=1, default=list)
for k, v in out.items():
    print(k, {x: v[x] for x in v if x not in ("tindakan_unik",)} if k != "_total" else v)
for r in rows:
    if r["status"] == "dihitung" and r["penutur"] in ("penutur tidak diketahui",) or r["penutur"].endswith("(dari isi berita)"):
        print("  penutur:", r["id"], r["penutur"], "|", r["penutur_di_berita"])

"""Gabungkan pengodean respons (agen pengode + pemeriksa) dengan daftar rilis dan keputusan penyunting.

Pakai:
  python3 -I gabung_respons.py --base rilis_base.csv --kode kode_respons.json \
      --keputusan keputusan.json --tindakan tindakan_unik.csv --out-dir .

--kode menerima dua bentuk:
  a) keluaran alur multi-agen: [{"kelompok":..., "kode":{"rilis":[...]}, "verifikasi":{"rilis":[...]}}, ...]
  b) daftar objek rilis yang sudah punya "skor_final".
--keputusan (opsional), contoh:
  {"keluarkan": {"R37": "pemerintah asing", "R22": "DRAFT"}, "gabung": {"R28": "P10"}, "salin_kode": {"P16": "P05"},
   "kecocokan": {"R07": "inti", "R20": "generik"}, "skor": {"P01": 0}}
"gabung": target memakai kode sumber dan sumber dibuang (duplikat). "salin_kode": dua rilis berbeda berbagi bukti; keduanya dihitung.
Aturan status:
  - daftar_divisi == "tidak"  -> catatan: di luar daftar divisi
  - jenis_tuntutan == "umum" atau sifat momen lembaga tanpa tuntutan spesifik -> catatan: tuntutan umum
  - masuk_per_isu diawali "catatan" (momen lembaga, lintas bidang) -> catatan: lembaga/lintas bidang
  - di "keluarkan" -> catatan: <alasan>
  - selain itu -> dihitung
Tindakan nyata = skor >= 3 dan kecocokan inti/sebagian. Skor >= 3 tanpa kecocokan dianggap "sebagian" dan diberi peringatan.
"""
import argparse, collections, csv, json, os, statistics

PIMPINAN = {"Boy Jerry Even Sembiring", "Uli Arta Siagian", "Dana Prima Tarigan", "Teo Reffelsen", "Christine Constanta",
            "Melva Harahap", "Tubagus Soleh Ahmadi"}
JENIS = {0: "tidak ada respons", 1: "ditolak", 2: "diakui/dijanjikan", 3: "tindakan parsial", 4: "dipenuhi"}


def muat_kode(path):
    raw = json.load(open(path))
    kode = {}
    if raw and isinstance(raw, list) and "kelompok" in raw[0]:
        for g in raw:
            ver = {v["id"]: v for v in (g.get("verifikasi") or {}).get("rilis", [])}
            for k in g["kode"]["rilis"]:
                v = ver.get(k["id"], {})
                k["skor_final"] = v.get("skor_final", k["skor"]); k["alasan_verifikasi"] = v.get("alasan", "")
                k["keyakinan_final"] = v.get("keyakinan", k.get("keyakinan", "")); k["respons"] = k["respons"] + v.get("respons_tambahan", [])
                kode[k["id"]] = k
    else:
        kode = {k["id"]: k for k in raw}
    return kode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True); ap.add_argument("--kode", required=True)
    ap.add_argument("--keputusan"); ap.add_argument("--tindakan"); ap.add_argument("--out-dir", default=".")
    a = ap.parse_args()
    base = {r["id"]: r for r in csv.DictReader(open(a.base))}
    kode = muat_kode(a.kode)
    kp = json.load(open(a.keputusan)) if a.keputusan else {}
    for kunci in ("gabung", "salin_kode"):
        for tujuan, sumber in kp.get(kunci, {}).items():
            if sumber in kode:
                kode[tujuan] = dict(kode[sumber], id=tujuan)
    tindakan = list(csv.DictReader(open(a.tindakan))) if a.tindakan else []
    rows = []
    for rid, b in base.items():
        if rid in kp.get("gabung", {}).values() and rid not in kp.get("gabung", {}):
            continue  # sumber gabungan tidak dihitung dua kali
        k = kode.get(rid, {})
        skor = kp.get("skor", {}).get(rid, k.get("skor_final", ""))
        m = b.get("masuk_per_isu", "")
        penutur = ("pengkampanye" if m == "ya" else "pimpinan/Hukum" if m.startswith("ya (") else "catatan" if m.startswith("catatan") else "?")
        if b.get("daftar_divisi") == "tidak":
            status = "catatan: di luar daftar divisi"
        elif m.startswith("catatan"):
            status = "catatan: lembaga/lintas bidang"
        elif rid in kp.get("keluarkan", {}):
            status = "catatan: " + kp["keluarkan"][rid]
        elif b.get("jenis_tuntutan") == "umum" or skor == "":
            status = "catatan: tuntutan umum / tidak dikode"
        else:
            status = "dihitung"
        kc = ""
        if skor != "" and int(skor) >= 3:
            kc = kp.get("kecocokan", {}).get(rid, "")
            if not kc and status == "dihitung":
                kc = "sebagian"; print(f"PERINGATAN {rid}: skor {skor} tanpa kecocokan; dianggap 'sebagian'. Isi keputusan.json.")
        bukti = next((r["url"] for r in k.get("respons", []) if r.get("url")), "")
        rows.append({"id": rid, "tanggal": b.get("tanggal", ""), "judul": b.get("judul_singkat", ""), "bidang": b.get("bidang_topik", ""),
                     "pj": b.get("pj_bidang", "") if penutur == "pengkampanye" else "", "penutur": penutur, "status": status,
                     "tuntutan": k.get("tuntutan_ringkas", b.get("tuntutan_utama", "")), "lembaga_dituju": k.get("lembaga_dituju", b.get("lembaga_dituju", "")),
                     "skor": skor, "jenis_respons": JENIS.get(int(skor), "") if skor != "" else "", "kecocokan": kc,
                     "tindakan_unik": ";".join(t["kode"] for t in tindakan if rid in t["rilis_terkait"].split(";")),
                     "hari_ke_respons": k.get("hari_ke_respons", ""), "konvergensi": k.get("konvergensi", ""),
                     "berita_kasus": k.get("berita_kasus", ""), "berita_memuat_walhi": k.get("berita_memuat_walhi", ""),
                     "berita_jejaring_tanpa_walhi": k.get("berita_jejaring_tanpa_walhi", ""), "berita_kontra": k.get("berita_kontra", ""),
                     "penutur_di_berita": "; ".join(k.get("penutur_terdeteksi", [])), "keyakinan": k.get("keyakinan_final", ""),
                     "bukti_utama": bukti, "alasan": k.get("alasan_verifikasi", "")[:900],
                     "respons_ringkas": " | ".join(f'{r["tanggal"]} {r["lembaga"]}: {r["isi"]}' for r in k.get("respons", []))[:900]})
    rows.sort(key=lambda r: (r["bidang"], r["tanggal"]))
    os.makedirs(a.out_dir, exist_ok=True)
    with open(os.path.join(a.out_dir, "respons_final.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    out = {}
    hit = [r for r in rows if r["status"] == "dihitung"]
    for bid in sorted({r["bidang"] for r in hit}):
        rs = [r for r in hit if r["bidang"] == bid]; s = [int(r["skor"]) for r in rs]
        nyata = [r for r in rs if int(r["skor"]) >= 3 and r["kecocokan"] in ("inti", "sebagian")]
        hari = [int(r["hari_ke_respons"]) for r in rs if str(r["hari_ke_respons"]).lstrip("-").isdigit() and int(r["hari_ke_respons"]) >= 0]
        out[bid] = {"rilis": len(rs), "oleh_pengkampanye": sum(r["penutur"] == "pengkampanye" for r in rs),
                    "oleh_pimpinan_hukum": sum(r["penutur"] == "pimpinan/Hukum" for r in rs),
                    "ada_respons": sum(v >= 1 for v in s), "ditolak": s.count(1), "dijanjikan": s.count(2), "tindakan_parsial": s.count(3),
                    "dipenuhi": s.count(4), "tindakan_nyata": len(nyata),
                    "tindakan_generik": sum(int(r["skor"]) >= 3 and r["kecocokan"] == "generik" for r in rs),
                    "pct_ada_respons": round(100 * sum(v >= 1 for v in s) / len(s)), "pct_tindakan_nyata": round(100 * len(nyata) / len(s)),
                    "median_hari_ke_respons": statistics.median(hari) if hari else None,
                    "berita_memuat_walhi": sum(int(r["berita_memuat_walhi"] or 0) for r in rs)}
    s = [int(r["skor"]) for r in hit]
    out["_total"] = {"rilis": len(hit), "ada_respons": sum(v >= 1 for v in s),
                     "tindakan_nyata": sum(v["tindakan_nyata"] for k, v in out.items() if k != "_total"),
                     "pct_ada_respons": round(100 * sum(v >= 1 for v in s) / len(s)) if s else 0,
                     "catatan": collections.Counter(r["status"] for r in rows if r["status"] != "dihitung"), "tindakan_unik": len(tindakan)}
    out["_total"]["pct_tindakan_nyata"] = round(100 * out["_total"]["tindakan_nyata"] / len(s)) if s else 0
    json.dump(out, open(os.path.join(a.out_dir, "ringkasan_per_bidang.json"), "w"), ensure_ascii=False, indent=1)
    for k, v in out.items():
        print(k, v)


if __name__ == "__main__":
    main()

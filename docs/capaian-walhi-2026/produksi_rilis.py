"""Produksi rilis per bidang & PJ, dan suara pimpinan/Hukum (sebagai catatan). Jalankan setelah final_respons.py."""
import collections, csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
base = {r["id"]: r for r in csv.DictReader(open(os.path.join(HERE, "rilis_base.csv")))}
fin = list(csv.DictReader(open(os.path.join(HERE, "respons_final.csv"))))
PJ = {"Hutan & Kebun": "Umi Ma'rufah", "Pesisir & Laut": "Mida Saragih", "Urban": "Wahyu Eka Styawan",
      "Pangan & Ekosistem Esensial": "Musdalifah Jamal", "Iklim & Isu Global": "Patria Rizky Ananda", "Tambang & Energi": "Faisal Ratuela"}
prod = {}
for isu, pj in PJ.items():
    rs = [r for r in fin if r["isu"] == isu and r["status"] == "dihitung"]
    bln = collections.Counter(r["tanggal"][5:7] for r in rs)
    prod[isu] = {"pj": pj, "total": len(rs), "pengkampanye": sum(r["penutur"].startswith("pengkampanye") for r in rs),
                 "pimpinan": sum(r["penutur"].startswith("pimpinan") for r in rs), "tidak_diketahui": sum(r["penutur"] == "penutur tidak diketahui" for r in rs),
                 "agu": bln.get("08", 0), "sep": bln.get("09", 0), "okt": bln.get("10", 0)}
PIM = {"Uli Arta Siagian": "Kadiv Kampanye", "Boy Jerry Even Sembiring": "Direktur Eksekutif", "Dana Prima Tarigan": "Kadep Komunikasi",
       "Teo Reffelsen": "Manajer Hukum & Pembelaan", "Christine Constanta": "Hukum (respons cepat)", "Melva Harahap": "Manajer Penanganan Bencana",
       "Tubagus Soleh Ahmadi": "Kadep Keorganisasian"}
pim = collections.Counter()
for r in fin:
    if r["status"].startswith("tidak dihitung"):
        continue
    src = base[r["id"]].get("suara_pimpinan", "") if r["id"].startswith("R") else r["penutur_di_berita"]
    if r["id"] == "P12":
        src += "; Christine Constanta"
    for n in PIM:
        if n in src or (n.split()[0] in ("Uli", "Boy", "Teo", "Christine") and n.split()[0] in src):
            pim[n] += 1
json.dump({"produksi": prod, "suara_pimpinan": {n: {"peran": PIM[n], "rilis": pim[n]} for n in PIM if pim[n]}},
          open(os.path.join(HERE, "produksi_rilis.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(prod, ensure_ascii=False)); print(pim)

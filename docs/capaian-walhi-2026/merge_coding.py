"""Gabungkan pengodean per isu (pengodean/respons_*.json) menjadi narasi_respons.csv.
Aturan rekonsiliasi didokumentasikan di OVERRIDE di bawah."""
import json, csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
for f in "HABCD":
    for x in json.load(open(os.path.join(HERE, "pengodean", f"respons_{f}.json"))):
        x["_src"] = f; rows.append(x)
key = lambda x: (x["_src"], x["label_pendek"])
# (sumber, label lama) -> perubahan. None = buang (duplikat di isu lain).
OVERRIDE = {
 ("A", "Regulasi data center"): None,
 ("A", "Izin pasir laut Bintan"): None,                 # periode Agu–Okt: hanya disuarakan 7 Jun
 ("A", "Adopsi AO ICJ iklim"): None,                    # periode Agu–Okt: terakhir disuarakan 31 Jul
 ("B", "PETI Sumbar: operator jerat"): {"skor": "0", "catatan_tambah": " Periode Agu–Okt: penindakan terjadi Juli (di luar periode); tidak ditemukan tindakan baru 1 Agu–2 Nov, pemodal belum disentuh."},                   # duplikat B "Data center: Komdigi akui" (Perkotaan)
 ("B", "Beriga: DPRD revisi zonasi"): None,             # duplikat A Batu Beriga (Pesisir); skor lebih rendah dipakai
 ("C", "Tidak ditemukan") : "cek",                      # dua baris; ditangani per narasi di bawah
 ("C", "Sebagian izin dibekukan"): {"skor": "2", "catatan_tambah": " Diturunkan 3→2 oleh penyunting: pembekuan izin adalah penindakan karhutla, bukan evaluasi izin gambut."},
}
LABEL = {
 ("A", "PSN tambak Pantura Jabar"): "Batalkan PSN tambak Pantura",
 ("A", "Oil spill Lampung Timur"): "Usut limbah minyak Lampung",
 ("A", "IUP PT Timah Batu Beriga"): "Cabut IUP Timah Batu Beriga",
 ("A", "Izin pasir laut Bintan"): "Tolak izin pasir laut Bintan",
 ("A", "Adopsi AO ICJ iklim"): "Adopsi putusan ICJ iklim",
 ("A", "Hak komunitas jelang COP31"): "Hak komunitas di COP31",
 ("A", "Audit proyek karbon"): "Audit proyek karbon",
 ("A", "Dana iklim Kalbar Rp39 M"): "Buka dana iklim Kalbar",
 ("A", "Pengesahan RUU Iklim"): "Sahkan RUU Perubahan Iklim",
 ("B", "PETI Sumbar: operator jerat"): "Tindak tambang emas ilegal",
 ("B", "Ungaran: ESDM tetap lanjut"): "Tolak PLTP Gunung Ungaran",
 ("B", "LTJ Mamuju: tanpa respons"): "Batalkan tambang LTJ Mamuju",
 ("B", "Transisi energi: nihil"): "Transisi energi berkeadilan",
 ("B", "Pangandaran: tanpa respons"): "Usut tumpahan batu bara",
 ("B", "Batu: janji kaji beli lahan"): "Lindungi mata air Kota Batu",
 ("B", "Jatiluhur stop, AMDAL dikaji"): "Kaji data center Jatiluhur",
 ("B", "Data center: Komdigi akui"): "Moratorium data center",
 ("B", "TPA: KLH akui, ancam sanksi"): "Hentikan open dumping TPA",
 ("B", "RTRW Aceh: tanpa respons"): "Revisi Raqan RTRW Aceh",
 ("B", "Galodo Solok: tanpa respons"): "Audit tata ruang Solok",
 ("C", "Sebagian izin dibekukan"): "Audit izin konsesi gambut",
 ("C", "BPGMN dibentuk"): "Pulihkan ekosistem gambut",
 ("C", "Janji perketat pengawasan"): "Evaluasi food estate Papua",
}
out = []
for x in rows:
    k = key(x); o = OVERRIDE.get(k)
    if o is None and k in OVERRIDE: continue
    if x["_src"] == "C" and x["label_pendek"] == "Tidak ditemukan":
        n = x["narasi_walhi"]
        if "Batu" in n: continue                         # duplikat B mata air Kota Batu (Perkotaan)
        x["label_pendek"] = "Evaluasi tambang DAS Kapuas" if "Kapuas" in n else "Tumpang tindih DAS Aia Dingin"
    if isinstance(o, dict):
        x["skor"] = o["skor"]; x["catatan"] = x.get("catatan", "") + o["catatan_tambah"]
    x["label_pendek"] = LABEL.get(k, x["label_pendek"])
    out.append(x)

RINGKAS = {  # label_pendek -> (lembaga, respons ringkas)
 "Batalkan PSN tambak Pantura": ("KKP", "KKP menyatakan proyek tetap berjalan (24 Sep)."),
 "Usut limbah minyak Lampung": ("KLH, DLH Lampung", "DLH Lampung sidak (13 Okt); hasil uji belum dibuka."),
 "Cabut IUP Timah Batu Beriga": ("KKP, ESDM, Pemprov Babel", "DPRD Babel dukung zona tangkap nelayan; IUP belum dicabut."),
 "Tolak izin pasir laut Bintan": ("KKP", "KKP: “bukan penambangan pasir laut” (24 Jul)."),
 "Sanksi korporasi": ("Kemenhut, KLH, Polri", "32 izin dibekukan, 5 dicabut, 20 korporasi tersangka."),
 "Umumkan nama tersangka": ("Polri", "Presiden: nama diumumkan “pada saatnya” (22 Okt)."),
 "Kesehatan korban asap": ("Pemerintah pusat/daerah", "Tidak ditemukan."),
 "Status bencana nasional": ("Presiden", "Menko Polkam: belum berencana menetapkan."),
 "Pemulihan lahan terbakar": ("KLH, Kemenhut", "Tidak ditemukan."),
 "Gugatan Pasal 72": ("Menhut", "Belum ada (baru 7 hari)."),
 "Tindak tambang emas ilegal": ("Polda Sumbar", "2 operator ekskavator tersangka; pemodal belum disentuh."),
 "Tolak PLTP Gunung Ungaran": ("ESDM", "ESDM: proyek tetap berjalan bertahap (2 Sep)."),
 "Batalkan tambang LTJ Mamuju": ("Presiden, Pemprov Sulbar", "Tidak ditemukan."),
 "Transisi energi berkeadilan": ("Pemerintah pusat", "Tidak ditemukan."),
 "Usut tumpahan batu bara": ("KLH, DLH Jabar", "Tidak ditemukan setelah 10 Sep."),
 "Lindungi mata air Kota Batu": ("Pemkot Batu", "Wali Kota janji bentuk tim kajian pembelian lahan."),
 "Kaji data center Jatiluhur": ("Pemprov Jabar, Pemkab Purwakarta", "Proyek tetap dihentikan; AMDAL dibahas (5 Okt)."),
 "Moratorium data center": ("Komdigi", "Menkomdigi akui masalah air; tanpa moratorium."),
 "Hentikan open dumping TPA": ("KLH, pemda", "Menteri LH akui tenggat terlewat, ancam sanksi."),
 "Revisi Raqan RTRW Aceh": ("DPRA, Pemerintah Aceh", "Tidak ditemukan."),
 "Audit tata ruang Solok": ("Pemkab Solok, Pemprov Sumbar", "Tidak ditemukan."),
 "Adopsi putusan ICJ iklim": ("KLH", "KLH akan pertimbangkan dalam NDC kedua."),
 "Hak komunitas di COP31": ("Delegasi COP31", "Tidak ditemukan."),
 "Audit proyek karbon": ("Kemenhut", "Tidak ditemukan."),
 "Buka dana iklim Kalbar": ("Pemprov Kalbar", "Tidak ditemukan."),
 "Sahkan RUU Perubahan Iklim": ("DPR, Pemerintah", "Tidak ditemukan setelah 22 Okt."),
 "Audit izin konsesi gambut": ("Kemenhut, ATR/BPN", "Izin 6 perusahaan dibekukan (karhutla, bukan audit gambut)."),
 "Pulihkan ekosistem gambut": ("Presiden", "BPGMN dibentuk; kepala dilantik 15 Okt."),
 "Evaluasi food estate Papua": ("Kemenko Pangan", "Wamenko Pangan janji perketat pengawasan."),
 "Evaluasi tambang DAS Kapuas": ("ESDM, KLH, pemda", "Tidak ditemukan."),
 "Tumpang tindih DAS Aia Dingin": ("ATR/BPN, Kemenhut", "Tidak ditemukan."),
}
for x in out:
    x["lembaga_ringkas"], x["respons_ringkas"] = RINGKAS[x["label_pendek"]]
ISU_KEDUA = {
 "Batalkan PSN tambak Pantura": "Ekosistem Esensial & Pangan", "Usut limbah minyak Lampung": "Tambang & Energi",
 "Cabut IUP Timah Batu Beriga": "Tambang & Energi", "Kaji ulang Giant Sea Wall": "Perkotaan & Tata Ruang",
 "Koreksi RUU Daerah Kepulauan": "Tambang & Energi", "Moratorium data center": "Pesisir & Laut",
 "Kaji data center Jatiluhur": "Ekosistem Esensial & Pangan", "Lindungi mata air Kota Batu": "Ekosistem Esensial & Pangan",
 "Revisi Raqan RTRW Aceh": "Tambang & Energi", "Audit tata ruang Solok": "Hutan & Kebun",
 "Tolak PLTP Gunung Ungaran": "Ekosistem Esensial & Pangan", "Transisi energi berkeadilan": "Iklim & Global",
 "Usut tumpahan batu bara": "Pesisir & Laut", "Tindak tambang emas ilegal": "Hutan & Kebun",
 "Kesehatan korban asap": "Perkotaan & Tata Ruang", "Pemulihan lahan terbakar": "Ekosistem Esensial & Pangan",
 "Audit proyek karbon": "Hutan & Kebun", "Buka dana iklim Kalbar": "Hutan & Kebun", "FOLU Net Sink terancam": "Hutan & Kebun",
 "Audit izin konsesi gambut": "Hutan & Kebun", "Pulihkan ekosistem gambut": "Pesisir & Laut",
 "Evaluasi food estate Papua": "Hutan & Kebun", "Evaluasi tambang DAS Kapuas": "Tambang & Energi",
 "Tumpang tindih DAS Aia Dingin": "Hutan & Kebun",
}
for x in out:
    x["isu_kedua"] = ISU_KEDUA.get(x["label_pendek"], "")
ORDER = ["Pesisir & Laut", "Hutan & Kebun", "Tambang & Energi", "Perkotaan & Tata Ruang", "Iklim & Global", "Ekosistem Esensial & Pangan"]
out.sort(key=lambda x: (ORDER.index(x["isu"]), -int(x["jumlah_judul"])))
F = ["isu", "isu_kedua", "label_pendek", "lembaga_ringkas", "respons_ringkas", "narasi_walhi", "tanggal", "alamat", "jumlah_judul", "respons_pemerintah", "skor", "url_narasi", "url_respons", "catatan"]
with open(os.path.join(HERE, "narasi_respons.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, F, extrasaction="ignore"); w.writeheader(); w.writerows(out)
from collections import Counter
c = Counter(x["isu"] for x in out); print(len(out), dict(c))
for x in out: print(x["isu"][:12], x["skor"], x["label_pendek"])

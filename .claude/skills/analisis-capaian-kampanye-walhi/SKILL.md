---
name: analisis-capaian-kampanye-walhi
description: >-
  Analisis capaian kampanye WALHI Eksekutif Nasional per periode (bulanan/triwulan): daftar rilis per bidang dan PJ,
  pemberitaan media (termasuk berita yang menyebut WALHI hanya di isi), dan respons pemerintah atas tuntutan
  tiap rilis (skala 0–4, tindakan nyata), lalu memperbarui laporan divisi kampanye (.docx) dengan data dan
  gambar baru. Pakai skill ini setiap kali pengguna menyebut laporan divisi kampanye, capaian kampanye, rekap
  rilis/siaran pers WALHI, pemberitaan WALHI, respons pemerintah atas rilis, kliping media pengkampanye,
  atau meminta analisis "bulan berikutnya", walaupun tidak menyebut nama skill ini.
---

# Analisis Capaian Kampanye WALHI

Skill ini mengulang metode yang dipakai untuk laporan Agustus–Oktober 2026. Fokusnya **outcome**: apakah
pemerintah merespons tuntutan WALHI, dan apakah responsnya berupa tindakan nyata. Jumlah berita hanya konteks.

Tulis semua keluaran dalam bahasa Indonesia yang lugas. Pengguna adalah tim kampanye, bukan tim pelibatan publik.

## Masukan yang diminta ke pengguna

1. **Periode** (mis. 1–30 November 2026).
2. **Laporan divisi kampanye** (.docx) periode itu. Tabel rilisnya (kolom Bulan, Judul, Bidang, Pengkampanye)
   adalah **acuan resmi** jumlah rilis. Jangan menghitung ulang rilis dari folder atau situs lalu menimpa angka tim.
3. Opsional: daftar siaran pers dan kliping dari tim bidang (mis. tim PELA), rekap Excel, dan hitungan manual
   berita per pengkampanye. Dipakai untuk kalibrasi.

Kalau periode atau laporan belum ada, minta dulu. Jangan menebak.

## Alur kerja

Kerjakan di folder kerja baru, mis. `docs/capaian-walhi-<yyyy-mm>/`. Jalankan Python dengan `python3 -I`.
Semua skrip ada di `scripts/` skill ini; tiap skrip punya penjelasan pemakaian di bagian atas berkasnya.

### 1. Daftar rilis (acuan: laporan divisi)

```bash
python3 -I scripts/ekstrak_tabel_rilis.py laporan_divisi.docx tabel_rilis.json
```

Skrip mencari tabel dengan kolom Bulan–Judul–Bidang–Pengkampanye dan menandai judul ganda. Laporkan ke pengguna:
jumlah baris, jumlah per bidang, dan setiap kemungkinan duplikat (judul sama di dua bulan, atau satu paket
"kesaksian" + rilis). **Ikuti keputusan pengguna** soal duplikat; jangan menghapus diam-diam.

Lalu buat `rilis_base.csv` (skema di `references/struktur_data.md`): satu baris per rilis dengan tanggal terbit,
bidang, PJ, sifat (isu bidang / momen lembaga), tuntutan utama, lembaga yang dituju, kueri kasus, dan jejaring.
Isi tuntutan dan lembaga dari judul rilis dan pemberitaannya. Tanggal: ambil dari baris "Jakarta, [tanggal]" atau
tanggal tayang publik; bulan di folder sering salah (rilis 25–29 bisa tercatat bulan berikutnya).

Aturan atribusi bidang (dari rekap tim):
- Pengkampanye bidang dikutip atau jadi narahubung → rilis masuk bidangnya.
- Hanya pimpinan atau Hukum yang bicara → rilis masuk bidang pemilik topik, ditandai "disuarakan pimpinan/Hukum",
  **tidak dikreditkan** ke pengkampanye. Capaian pimpinan hanya dicatat sebagai catatan.
- Momen lembaga tanpa tuntutan spesifik (HUT, TAP MPR, pidato presiden, dua tahun pemerintahan) dihitung di
  produksi rilis, tetapi tidak dikode responsnya.
- Daftar orang, peran, dan variasi ejaan nama: `references/roster.md` dan `scripts/roster.json`.

### 2. Pemberitaan umum per isu

```bash
python3 -I scripts/korpus_walhi.py --mulai 2026-11-01 --selesai 2026-11-30 --out korpus.json
python3 -I scripts/hitung_pemberitaan.py --korpus korpus.json --mulai 2026-11-01 --selesai 2026-11-30 --out pemberitaan.json
```

`korpus_walhi.py` mengambil semua berita Google News yang memuat "walhi" (jendela 2 hari) ditambah kueri khusus
per isu (cocok ke judul atau isi). `hitung_pemberitaan.py` memilah per isu dengan kata kunci isu dan **aturan lokus**
(berita tambang, PSN, atau data center di laut, pesisir, perairan, atau pulau kecil ikut dihitung di Pesisir & Laut).
Satu berita boleh masuk lebih dari satu isu; laporkan irisannya. Rinciannya: `references/metode.md` bagian 2.

### 3. Pemuatan tiap rilis dan kandidat respons

Untuk setiap rilis bertuntutan spesifik:

```bash
python3 -I scripts/pemuatan_rilis.py --id R05 --tanggal 2026-11-12 --out hasil/R05.json \
  --kueri 'walhi "<kasus>"' --kueri '"<kasus>" <lokasi>' --kueri '<jejaring> <kasus>' --jejaring KIARA
```

Rentang H-1 s.d. H+14. Pakai tiga jenis kueri: kasus + "walhi", kasus tanpa "walhi", dan jejaring + kasus. Isi berita
dibaca untuk menghitung sebutan WALHI, penutur, jejaring, dan kalimat pejabat (kandidat bukti respons).
Lengkapi dengan sapuan nama pengkampanye (menangkap wawancara/talkshow di luar rilis dan salah ketik nama):

```bash
python3 -I scripts/sapu_nama.py --roster scripts/roster.json --mulai 2026-11-01 --selesai 2026-11-30 --out sapu_nama.json
```

Kalau tim bidang memberi kliping manual (spreadsheet), gabungkan dengan hasil otomatis untuk bidang itu tanpa duplikat dan
tandai di gambar (lihat `references/metode.md` bagian 2). Unduh Google Sheet yang dibagikan dengan
`https://docs.google.com/spreadsheets/d/<ID>/export?format=xlsx`.

Kode sikap tiap berita: memuat pesan WALHI/jejaring, kontra-narasi (mis. "aktivis" pro-proyek), atau konteks.
Kontra-narasi bukan respons resmi; catat terpisah.

### 4. Pengodean respons pemerintah

Ikuti `references/skala_respons.md`. Ringkasnya: skor 0 tidak ada; 1 ditolak; 2 diakui/dijanjikan; 3 tindakan
terverifikasi yang searah tetapi sebagian; 4 dipenuhi. Respons dicari dari tanggal rilis sampai akhir periode + 2
hari, dari lembaga yang dituju atau yang berwenang, **termasuk respons kepada jejaring**. Respons sebelum tanggal
rilis tidak dihitung. Ragu → skor lebih rendah. Skor 3–4 wajib punya bukti resmi atau dua media berbeda.

Untuk lebih dari ~10 rilis, pakai multi-agen bila pengguna setuju (template: `references/workflow_respons.js`):
satu agen pengode per kelompok bidang, lalu satu agen pemeriksa per kelompok yang tugasnya **membantah** skor.
Setelah itu periksa sendiri semua skor ≥ 3: keluarkan respons pemerintah asing dari statistik, tandai "generik"
bila buktinya hanya tindakan umum yang sudah dipakai di rilis lain, dan susun **tindakan unik** (satu tindakan
dihitung sekali walau menjawab beberapa rilis).

```bash
python3 -I scripts/gabung_respons.py --base rilis_base.csv --kode kode_respons.json \
  --keputusan keputusan.json --tindakan tindakan_unik.csv --out-dir .
```

### 5. Gambar dan laporan

```bash
python3 -I scripts/buat_gambar.py --tabel tabel_rilis.json --pemberitaan pemberitaan.json \
  --ringkasan ringkasan_per_bidang.json --out figures/
```

Empat gambar: (1) rilis per bidang, (2) rilis per bulan per bidang, (3) pemberitaan per isu, (4) tangga respons
per bidang. Perbarui laporan divisi **di tempat**: ganti gambar, perbarui caption dan paragraf pemberitaan/respons,
tambahkan daftar tindakan nyata, pertahankan komentar yang ada (balas, jangan hapus). Pakai
`scripts/docx_edit.py` dengan berkas spesifikasi JSON (contoh di bagian atas skrip), lalu validasi dan render
halaman yang berubah untuk dicek visual. Bagian di luar pemberitaan, respons, dan gambar milik tim; jangan diubah
kecuali angka rilis yang bertentangan dengan tabel rilisnya sendiri (laporkan perubahan itu).

### 6. Laporan ke pengguna

Sampaikan singkat: angka utama, perubahan yang dibuat, keputusan yang perlu pengguna ambil (duplikat, penutur
belum diketahui, rilis publik di luar daftar divisi), dan keterbatasan. Commit dan push bila bekerja di repo.

## Jebakan yang sudah pernah terjadi

Baca `references/jebakan.md` sebelum menghitung. Yang paling sering: kueri Google yang gagal (503) tercatat
sebagai 0 hasil; nama media di akhir judul ikut tercocokkan kata kunci ("Terasbatam"); "ikan" cocok di
"hentikan"; "Pulau Kalimantan" dikira pulau kecil; satu tindakan pemerintah terhitung di banyak rilis; dan ejaan
nama pengkampanye di media berbeda dengan rekap internal.

## Referensi

- `references/metode.md` — kerangka metode lengkap dan dasar teorinya; baca saat menulis bagian metode laporan.
- `references/skala_respons.md` — aturan dan contoh pengodean respons.
- `references/roster.md` — orang, bidang, peran, ejaan.
- `references/struktur_data.md` — skema CSV/JSON antar-langkah.
- `references/jebakan.md` — kesalahan yang harus dicegah.
- `references/workflow_respons.js` — template alur multi-agen pengode + pemeriksa.

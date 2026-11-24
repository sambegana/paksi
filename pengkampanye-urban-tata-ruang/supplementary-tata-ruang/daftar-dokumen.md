---
jenis: indeks
diperbarui: 2026-11-24
isu: [isu-tata-ruang]
---

# Supplementary tata ruang

Folder dokumen sumber tata ruang: RTRW, RDTR, RTR KSN, KLHS, peta, materi teknis, dan sejenisnya.
Dokumen di sini adalah **bahan primer** untuk memverifikasi klaim di [[isu-tata-ruang]] dan
[[benang-merah]], misalnya soal mekanisme PSN memperoleh KKPR tanpa kesesuaian RTRW.

## Cara menambah dokumen

1. Unggah berkas ke folder ini. Lewat GitHub web: buka folder → *Add file* → *Upload files*.
   Bisa juga menaruhnya di folder vault lewat Obsidian lalu push, atau melampirkannya di sesi Claude
   dan minta dimasukkan.
2. Beri nama dengan pola: `<jenis>-<wilayah>-<tahun>-<nomor-peraturan>.<ext>`
   Contoh: `rtrw-dki-jakarta-2012-perda-1-2012.pdf`, `rdtr-kota-batam-2024-perwako-xx.pdf`.
   Gunakan huruf kecil dan tanda `-`, tanpa spasi.
3. Tambahkan satu baris di tabel di bawah. Tautan `[[nama-berkas.pdf]]` bisa dibuka langsung di Obsidian.

## Batasan

- **Repo ini publik.** Hanya unggah dokumen yang memang publik, seperti perda, peta resmi, dan
  dokumen konsultasi publik. Draf internal, dokumen yang didapat lewat jalur tidak resmi, atau
  dokumen berisi data pribadi warga sebaiknya tidak ditaruh di sini.
- **Ukuran berkas.** Unggahan lewat GitHub web dibatasi 25 MB per berkas, dan git menolak berkas di
  atas 100 MB. Berkas yang lebih besar disimpan bertingkat:
  1. **Sumber resmi dulu.** Kalau dokumennya sudah ada di JDIH pemda, GISTARU ATR/BPN, atau
     Ina-Geoportal, cantumkan tautan itu dan tanggal unduh. Versi resmi lebih kuat sebagai rujukan.
  2. **Berkas utuh di Google Drive** dengan akses *Anyone with the link → Viewer*, lalu tempel tautannya
     di tabel. Drive gratis hanya 15 GB; berkas ratusan GB butuh paket berbayar atau Shared Drive lembaga.
  3. **Potongan yang dipakai masuk ke folder ini**: batang tubuh perda (pasal pola/struktur ruang,
     zonasi, ketentuan peralihan), peta pola ruang wilayah kasus, tabel indikasi program. Potongan
     inilah yang bisa dibaca di Obsidian dan diperiksa Claude. Berkas utuh berukuran ratusan GB tidak
     bisa dibaca sekaligus.
  - Untuk data spasial (SHP, geodatabase), ambil layer yang relevan saja untuk kecamatan kasus.
  - Jangan pakai Git LFS (kuota gratis 1 GB) atau memecah berkas agar muat di GitHub.

## Untuk Claude: membaca berkas yang hanya ada di Drive

Berkas Drive yang dibagikan *Anyone with the link* bisa diunduh di sesi cloud (diuji 2026-11-24
untuk PDF 132 MB). Ambil ID dari tautan (`/file/d/<ID>/view`), lalu:

```bash
mkdir -p "$SCRATCH/drive" && curl -sL -o "$SCRATCH/drive/<nama>.pdf" \
  "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"
file "$SCRATCH/drive/<nama>.pdf"   # pastikan PDF, bukan halaman HTML
```

`$SCRATCH` = direktori scratchpad sesi. Simpan di sana, bukan di repo. Untuk teks, baca dulu versi
`-teks.md` yang sudah ada di folder ini. Unduh PDF utuh hanya bila perlu peta atau lampiran.

Batasan: tautan mati bila pemiliknya mengubah akses atau menghapus berkas. Drive kadang membatasi
unduhan berkas yang sering diakses. Berkas yang jauh lebih besar dari sisa disk sesi tidak bisa
diunduh utuh. Situs dengan pemeriksaan anti-bot (mis. peraturan.bpk.go.id) **tidak bisa** diunduh
otomatis: minta pengguna mengunduh manual lalu menaruhnya di folder Drive di atas.

## Daftar dokumen

Berkas diunggah dari folder Drive pengguna ([Supplementary Tata Ruang](https://drive.google.com/drive/folders/1JM063wyd3ub_RqUTq7kLNPYcM3TDcKJf)),
ditambah dokumen resmi yang dicari dari situs pemerintah. Ditambahkan 2026-11-24.

### Regulasi (resmi)

| Berkas / tautan | Jenis | Wilayah | Nomor & tahun | Status berlaku | Sumber | Catatan |
|---|---|---|---|---|---|---|
| [[regulasi-perda-dki-7-2024-rtrw-jakarta-2024-2044-teks]] · [[regulasi-perda-dki-7-2024-rtrw-jakarta-2024-2044-batang-tubuh.pdf]] · [PDF utuh 132 MB di Drive](https://drive.google.com/file/d/15J0TdPr0A4F1sHsvAD7B1DmHcS_vhL8s/view) | RTRW | Provinsi DKI Jakarta | Perda 7/2024, LD 2024 No. 103 | **Berlaku**; menggantikan Perda 1/2012 | Salinan pengguna; [JDIH DKI](https://jdih.jakarta.go.id) | Batang tubuh hal. 1–169, penjelasan 170–196, lampiran 197–372 (peta hal. 263–294). PDF batang tubuh = hal. 1–196. Teks = ekstraksi otomatis seluruh 372 halaman |
| [[regulasi-pergub-dki-31-2022-rdtr-wp-jakarta.pdf]] | RDTR | Provinsi DKI Jakarta | Pergub 31/2022 | Berlaku; belum ada perubahan yang terkonfirmasi (dicek sekilas 2026-11-24) | [DCKTRP DKI](https://dcktrp.jakarta.go.id/website-admin/storage/peraturan/Pergub%20no%2031%20tahun%202022.pdf) | **Identik byte-per-byte** dengan salinan resmi DCKTRP (200 hal., tanpa lampiran peta). Menggantikan Perda 1/2014 RDTR-PZ |
| [[regulasi-perda-dki-1-2012-rtrw-jakarta-2030.pdf]] | RTRW | Provinsi DKI Jakarta | Perda 1/2012 | **Dicabut**, diganti Perda 7/2024 | [Situs Pemprov DKI (Distamhut)](https://flona.jakarta.go.id/assets/data/data-peraturan/PERDA-01_TAHUN_2012-TENTANG-RTRW_2030.pdf) | Pembanding: apa yang berubah dari RTRW 2030 ke 2044 |
| [Perpres 60/2020 di BPK](https://peraturan.bpk.go.id/Download/199214/Perpres%20Nomor%2060%20Tahun%202020.pdf) *(belum diunggah)* | RTR KSN | Jabodetabek-Punjur | Perpres 60/2020 | Berlaku per laporan 2020; status terbaru belum dicek | BPK | Situs BPK memblokir unduhan otomatis. **Unduh manual lewat browser lalu unggah ke sini.** Rujukan di atas RTRW untuk Jakarta dan kota sekitarnya |

### Peta

| Berkas | Isi | Sumber | Catatan |
|---|---|---|---|
| [[peta-rtrw-jakarta-2030-jakarta-timur.pdf]] | Peta RTRW 2030 Jakarta Timur, 10 lembar | Salinan pengguna; nama berkas asli menunjukkan unggahan Scribd, bukan sumber resmi | Peta era Perda 1/2012 (sudah dicabut) |

### Kajian & bahan pendukung (bukan dokumen resmi)

| Berkas | Isi | Catatan |
|---|---|---|
| [[kajian-studio-pwk-ut-2026-rtrw-jakarta-timur-laporan.pdf]] | Laporan akhir Studio PWK (STPL 4219) Universitas Terbuka 2026: RTRW Jakarta Timur 2024–2044, WP Pasar Rebo, Kramat Jati, Jatinegara, Pulogadung, Cakung (317 hal.) | **Latihan akademik mahasiswa**, bukan rencana resmi. Berguna untuk profil wilayah dan isu |
| [[kajian-studio-pwk-ut-2026-rtrw-jakarta-timur-presentasi.pdf]] · [[kajian-studio-pwk-ut-2026-rtrw-jakarta-timur-ringkasan.pdf]] · [[kajian-studio-pwk-ut-2026-rtrw-jakarta-timur-poster.pdf]] | Presentasi (71 hal.), ringkasan (15 hal., berbasis gambar), poster | Studio yang sama |
| [[kajian-studio-pwk-ut-2026-rtrw-jakarta-timur-infografis.jpg]] · [[kajian-studio-pwk-ut-2026-peta-pola-ruang-jakarta-timur.jpg]] · [[kajian-studio-pwk-ut-2026-peta-struktur-ruang-jakarta-timur.jpg]] | Infografis, peta rencana pola ruang & struktur ruang (1:150.000) | Studio yang sama. Usulannya antara lain "normalisasi 18 km tanggul sungai", yang **berseberangan** dengan arah naturalisasi di [[isu-sungai]] |
| [[jurnal-jsg-2026-pemetaan-partisipatif-betawi-ciliwung.pdf]] | Artikel *Jurnal Sains Geografi* 4(2) 2026: pemetaan partisipatif kearifan lokal Betawi di bantaran Ciliwung segmen Jaksel–Jaktim | Penulis kedua dari [[padepokan-ciliwung-condet]]. Terkait [[ciliwung]], [[condet]] |
| [[peta-rancangan-pemetaan-partisipatif-ciliwung-2026.jpg]] | Rancangan jalur pemetaan partisipatif 2026 (33,3 km) vs jalur 2021 (19 km, 22 titik) | Pendamping artikel jurnal di atas |
| [[proposal-cbrut-wisata-kota-regeneratif-jakarta-500.pdf]] | Proposal "Wisata Kota Regeneratif Berbasis Komunitas (CBRUT)": ruang hijau dan sungai menuju 500 tahun Jakarta (22 Juni 2027), 20 hal. | Nama berkas asli "TMD_PCC", kemungkinan dari Padepokan Ciliwung Condet (belum dipastikan) |

### Dicari, belum ditemukan / belum diunggah
- **Perpres Rencana Induk Pembangunan Kawasan Aglomerasi (RIPKA)** sesuai UU 2/2024 tentang DKJ: penyusunannya dimulai Agustus 2025; status pengesahan belum terverifikasi.
- **Peta resmi Perda 7/2024** dalam format data (SHP/GDB): cek GISTARU ATR/BPN dan portal Jakarta Satu.
- **KLHS RTRW Jakarta 2024–2044**: belum dicari.

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
ditambah dokumen resmi yang dicari dari situs pemerintah. Ditambahkan 2026-11-24; gelombang kedua (Perpres 60/2020, Perpres 87/2011, Perda Batam 3/2021) ditambahkan di hari yang sama.

### Regulasi (resmi)

| Berkas / tautan | Jenis | Wilayah | Nomor & tahun | Status berlaku | Sumber | Catatan |
|---|---|---|---|---|---|---|
| [[regulasi-perda-dki-7-2024-rtrw-jakarta-2024-2044-teks]] · [[regulasi-perda-dki-7-2024-rtrw-jakarta-2024-2044-batang-tubuh.pdf]] · [PDF utuh 132 MB di Drive](https://drive.google.com/file/d/15J0TdPr0A4F1sHsvAD7B1DmHcS_vhL8s/view) | RTRW | Provinsi DKI Jakarta | Perda 7/2024, LD 2024 No. 103 | **Berlaku**; menggantikan Perda 1/2012 | Salinan pengguna; [JDIH DKI](https://jdih.jakarta.go.id) | Batang tubuh hal. 1–169, penjelasan 170–196, lampiran 197–372 (peta hal. 263–294). PDF batang tubuh = hal. 1–196. Teks = ekstraksi otomatis seluruh 372 halaman |
| [[regulasi-pergub-dki-31-2022-rdtr-wp-jakarta.pdf]] | RDTR | Provinsi DKI Jakarta | Pergub 31/2022 | Berlaku; belum ada perubahan yang terkonfirmasi (dicek sekilas 2026-11-24) | [DCKTRP DKI](https://dcktrp.jakarta.go.id/website-admin/storage/peraturan/Pergub%20no%2031%20tahun%202022.pdf) | **Identik byte-per-byte** dengan salinan resmi DCKTRP (200 hal., tanpa lampiran peta). Menggantikan Perda 1/2014 RDTR-PZ |
| [[regulasi-perda-dki-1-2012-rtrw-jakarta-2030.pdf]] | RTRW | Provinsi DKI Jakarta | Perda 1/2012 | **Dicabut**, diganti Perda 7/2024 | [Situs Pemprov DKI (Distamhut)](https://flona.jakarta.go.id/assets/data/data-peraturan/PERDA-01_TAHUN_2012-TENTANG-RTRW_2030.pdf) | Pembanding: apa yang berubah dari RTRW 2030 ke 2044 |
| [[regulasi-perpres-60-2020-rtr-jabodetabekpunjur-teks]] · [PDF utuh 55 MB di Drive](https://drive.google.com/file/d/1Y1lINTF8VvzOm2yen-S7daWogzoty7g4/view) | RTR KSN | Jabodetabek-Punjur | Perpres 60/2020 | Berlaku per laporan 2020; perubahan setelahnya belum dicek | Diunggah pengguna ke Drive 2026-11-24; [BPK](https://peraturan.bpk.go.id/Download/199214/Perpres%20Nomor%2060%20Tahun%202020.pdf) | 199 hal. Pasal 81: Zona B8 (kawasan reklamasi) berdaya dukung rendah, rawan intrusi & abrasi, tetap untuk permukiman/perdagangan/industri (hal. 133). Pasal 122: "kebijakan strategis nasional" bisa menambah kegiatan di zona lindung (hal. 185). Kata "penurunan muka tanah" tidak ditemukan |
| [[regulasi-perpres-87-2011-rtr-bbk-teks]] · [[regulasi-perpres-87-2011-rtr-bbk-batang-tubuh.pdf]] · lampiran di Drive: [I struktur](https://drive.google.com/file/d/1oNO3nkVl555bdL6ryithWn_LD_NO3vst/view), [II pola](https://drive.google.com/file/d/1QMpyF3JsARoYQUsez-gfOZDD1b4wvMYU/view), [III indikasi program](https://drive.google.com/file/d/1Zwh3_ZPOYBcEhl7ihkO1fKN87g4aDhr5/view) | RTR KSN | Batam, Bintan, Karimun | Perpres 87/2011 | Berlaku menurut konsiderans Perda Batam 3/2021; perubahan setelahnya belum dicek | Diunggah pengguna ke Drive 2026-11-24 | 139 hal. Pasal 56: sempadan waduk 50–100 m dari titik pasang air tertinggi (hal. 57). Pasal 62(2): ±40 kampung tua di Batam, termasuk Nongsa Pantai, Teluk Mata Ikan, Batu Besar, ditetapkan Zona L3 (hal. 62). Kampung tua Rempang tidak tercantum, hanya situs Jepang Sembulang |
| [[regulasi-perda-batam-3-2021-rtrw-batam-2021-2041-teks-ocr]] · [[regulasi-perda-batam-3-2021-rtrw-batam-2021-2041.pdf]] | RTRW | Kota Batam | Perda 3/2021 | Berlaku | Diunggah pengguna ke Drive 2026-11-24 | **Pindaian tanpa teks; teks = OCR**. Isi: batang tubuh hal. 1–97, penjelasan hal. 98–112, tabel indikasi program hal. 114–152. Pasal 28: cagar budaya hanya 5 situs, tanpa kampung tua (hal. 35). Pasal 29: mangrove ±404 ha. Pasal 30: RTH ≥30% (20% publik, 10% privat). Pasal 35: industri ±11.603 ha, termasuk 663 ha yang masih hutan lindung, 1.151 ha HPK di Galang, dan 3.628 ha reklamasi perairan (hal. 39–40). Kata "pusat data", "KLHS", dan "kampung" tidak ditemukan di OCR batang tubuh dan penjelasan (hal. 1–112). Hal. 114–152 = tabel indikasi program yang diputar, tidak terbaca OCR. Peta lampiran tidak ada di PDF ini |

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

Hasil penelusuran web 2026-11-24 ([[2026-11-24-peta-belajar-tata-ruang]]). Status tautan dicek dari sesi cloud.

| Bahan | Temuan | Tautan / langkah |
|---|---|---|
| **RDTR Nongsa & Kabil** | Ada: **Perwali Batam 60/2021** tentang RDTR WP Nongsa, Batam Kota, Bengkong, Batu Ampar, Lubuk Baja, Sekupang, dan Batu Aji 2021–2041 (Berita Daerah 2021 No. 847), dirujuk di Perwali Batam 3/2022. Naskahnya belum ditemukan daring | Minta ke DCKTR Kota Batam atau PPID Pemkot Batam; cek GISTARU ATR/BPN untuk peta RDTR. Rujukan: [Perwali Batam 3/2022 di BPK](https://peraturan.bpk.go.id/Download/300605/Perwali%20Batam%20No%203%20Tahun%202022.pdf) (unduh manual lewat browser) |
| Forum Penataan Ruang Kota Batam | Perwali Batam 3/2022 mengatur mekanisme dan tata kerja Forum Penataan Ruang (sasaran advokasi, setara FPRD Jakarta) | [BPK](https://peraturan.bpk.go.id/Download/300605/Perwali%20Batam%20No%203%20Tahun%202022.pdf) (unduh manual) |
| KLHS RTRW Batam 2021 | Belum ditemukan. Yang tersedia: KLHS **RDTR** WP Sagulung, Sungai Beduk, Belakang Padang (memuat tinjauan RTRW 2021–2041). KLHS RDTR Nongsa tidak ditemukan | [KLHS RDTR Sagulung](https://silh.batam.go.id/web/wp-content/uploads/2023/08/KLHS-RDTR-WP-Sagulung.pdf) (tautan hidup, 12 MB) · [Sungai Beduk](https://silh.batam.go.id/web/wp-content/uploads/2023/08/Dokumen-KLHS-RDTR-WP-Sungai-Beduk.pdf) · [Belakang Padang](https://silh.batam.go.id/web/wp-content/uploads/2023/08/Dokumen-RDTR-KLHS-Belakang-Padang_V23Feb2022.pdf). KLHS RTRW dan KLHS RDTR Nongsa: permohonan KIP ke DLH Kota Batam |
| KLHS RTRW Jakarta 2024–2044 | Belum ditemukan. Ada **KLHS Revisi RTRW Jakarta 2030, validasi Desember 2018** (kemungkinan KLHS proses revisi yang berujung di Perda 7/2024), tetapi tautan di situs DLH DKI kini **404** | Tautan lama: dinaslhdki.id/files/kajian/2018/KLHS-RTRW-2018/LAPORAN-KLHS-RTRW-JAKARTA-2030-final-Validasi-2018.pdf (mati). Coba Wayback Machine, lalu permohonan KIP ke DLH DKI dan DCKTRP. Kepgub DKI 188/2022 membentuk pokja KLHS untuk RDTR |
| Peta lampiran Perda Batam 3/2021 | Pasal pola ruang merujuk Peta Pola Ruang skala 1:25.000 di Lampiran II; belum ditemukan daring | JDIH Kota Batam / DCKTR Batam; Lembaran Daerah 2021 No. 3 |
| Salinan resmi Statuta WALHI 2025 | Tidak dipublikasikan di walhi.or.id | Minta ke Eksekutif Nasional (internal) |
| Naskah resmi Deklarasi Sumba | Ada di situs WALHI (versi ID dan EN); situs memblokir unduhan otomatis, buka lewat browser | [ID](https://walhi.or.id/uploads/WALHI%202025-2029/Dokumen/Naskah%20Deklarasi%20Keadilan%20Ekologis_id_A4.pdf) · [EN](https://walhi.or.id/uploads/WALHI%202025-2029/Dokumen/Naskah%20Deklarasi%20Keadilan%20Ekologis_en.pdf) |
| Perubahan Perpres 87/2011 | Tidak ditemukan perpres perubahan; pasal.id mencantumkan "berlaku" | Cek riwayat di [JDIH BPK](https://peraturan.bpk.go.id/Details/41235/perpres-no-87-tahun-2011) |
| Bacaan pendukung | Mongabay, 7 Apr 2026: "Tata ruang Batam antara ambisi industri dan krisis lingkungan" | [Mongabay](https://mongabay.co.id/2026/04/07/tata-ruang-batam-antara-ambisi-industri-dan-krisis-lingkungan/) |

Lainnya:
- **Peta lampiran Perda Batam 3/2021** (peta struktur & pola ruang skala kota): PDF 152 hal. hanya memuat batang tubuh, penjelasan, dan tabel indikasi program.
- **Perubahan atas Perpres 87/2011 dan Perpres 60/2020** (bila ada): belum dicek.
- **Perpres Rencana Induk Pembangunan Kawasan Aglomerasi (RIPKA)** sesuai UU 2/2024 tentang DKJ: penyusunannya dimulai Agustus 2025; status pengesahan belum terverifikasi.
- **Peta resmi Perda 7/2024** dalam format data (SHP/GDB): cek GISTARU ATR/BPN dan portal Jakarta Satu.
- **KLHS RTRW Jakarta 2024–2044**: belum dicari.

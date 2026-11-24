---
jenis: sesi
tanggal: 2026-11-21
sumber: https://claude.ai/code/session_01HPqUVJyCM8iNH99CBDD7NW
isu: [sungai, air, tata-ruang, sampah, iklim, advokasi]
tag: [ciliwung, normalisasi, naturalisasi, pramono, jakarta-500, sumur-resapan, penurunan-muka-tanah, atlas-sungai, sempadan, standar-pemindahan]
---

# Sungai DAS urban Jakarta: dari normalisasi vs naturalisasi ke "Ruang Air Jakarta" dan atlas koridor sungai

## Pertanyaan / tujuan
Pengguna ingin belajar isu sungai/DAS perkotaan, mulai dari normalisasi vs naturalisasi, lalu bergeser ke strategi kampanye dan pengorganisasian warga bantaran (berangkat dari Padepokan Ciliwung Condet) dengan momentum HUT ke-500 Jakarta (22 Juni 2027). Pertanyaan berurutan: (1) normalisasi vs naturalisasi; (2) usulan memetakan perusahaan perusak hulu + tegas IPAL + kampanye + tim warga berperahu tiap 5 km; (3) rencana mendesak Gubernur Pramono menolak betonisasi, fokus EbA, "naturalisasi tanpa penggusuran" dengan FPIC; (4) cakupan diperluas ke seluruh sungai Jakarta (Condet hanya contoh): apa motivasi Pramono, percontohannya, pro-kontra, narasi tandingan; (5) nama pengganti "naturalisasi" + sumur resapan wajib di bangunan untuk mencegah penurunan tanah; (6) baca ruang Jakarta dengan data, preseden luar negeri, "what is to be done".

## Yang dihasilkan
Enam artefak HTML (seri "Catatan belajar · Sungai & DAS perkotaan"):
- Modul 1 — Sungai Kota: Normalisasi dan Naturalisasi: https://claude.ai/artifact/FeqXtTwprsNJSGFbwH1hPg (penampang + rumus Manning, matriks 9 kriteria, 6 studi kasus, regulasi, tabel sempadan, 8 pertanyaan menilai ruas, kurikulum 10 minggu)
- Modul 2 — Memulihkan Sungai Jakarta: https://claude.ai/artifact/M6Ybv3tbP7z9eYhbPF8nS4 (ulasan 3 usulan, empat masalah berbeda, urutan tuas, tahapan 0–2/2–5/5–20 th, model "penjaga sungai", Singapore River & Citarum Harum)
- Modul 3 — Ciliwung Menuju 5 Abad: https://claude.ai/artifact/6QdVyqK8VePErrBmgUJymb (garis waktu kebijakan Condet, 5 tuntutan, standar pemindahan, tangga bukti inventarisasi, peta aktor, jadwal 7 bulan, risiko)
- Modul 4 — Membaca Normalisasi Pramono: https://claude.ai/artifact/4sKqX3wyRC9fdL8niGsg5H (motivasi diucapkan vs struktural, paket banjir Pemprov, percontohan, tabel pro-kontra dengan tingkat bukti, narasi pengganti, bantahan, tipologi ruas A/B/C)
- Modul 5 — Ruang Air Jakarta: https://claude.ai/artifact/W4CdWMR16juNLP4xLb5AFj (nama berlapis, tangga transisi kota air Brown dkk. 2009, empat pilar, riwayat sumur resapan, kalkulator, penurunan tanah, desain kewajiban)
- Modul 6 — Rencana Ruang Air Jakarta (atlas kerja): https://claude.ai/artifact/UmPj4jyeBuS8pADfMk9n1n (analisis data terbuka: ESA WorldCover 2021, OSM, Microsoft Building Footprints; peta segmen 500 m; 12 lahan kandidat; 7 preseden; 5 pekerjaan; rencana 12 bulan; direktori 16 sumber data)
- Skrip analisis geospasial hanya di folder scratch sesi (bisa terhapus); tidak disimpan ke repo. Tidak ada branch.

## Pokok pembelajaran
1. "Normalisasi vs naturalisasi" adalah bingkai keliru: keduanya menjawab pertanyaan berbeda (kapasitas vs sistem hidup), skalanya hanya alur sementara banjir ditentukan di tingkat DAS, dan variabel kuncinya **ruang/lahan, bukan material** — untuk debit sama, [[naturalisasi-sungai]] butuh penampang lebih lebar (persamaan Manning). Klaim "naturalisasi tanpa penggusuran" harus diuji dengan hitungan.
2. Sungai kota rusak karena tutupan kedap air yang terhubung ke drainase ([[urban-stream-syndrome]], Walsh dkk. 2005; [[impervious-cover-model]], Schueler 1994: mulai turun ~10%, rusak berat >25%). Analisis sesi: **79% daratan Jakarta terbangun** → sungai tidak bisa diselamatkan dari alur saja; air harus ditahan di persil.
3. Pencemar terbesar sungai Jakarta adalah limbah rumah tangga (jaringan air limbah perpipaan baru melayani sebagian sangat kecil kota), bukan pabrik; masalah hulu Ciliwung (Puncak) adalah alih fungsi lahan → banjir & sedimen. "Sungai bagus" = empat masalah berbeda (air tercemar, sampah, banjir, sungai mati) dengan tuas berbeda. Lihat [[isu-sampah]], [[isu-air]].
4. Kampanye perilaku hanya menyentuh motivasi ([[com-b]]); buang sampah ke sungai sering soal tiadanya layanan angkut (kesempatan). Layanan dulu, kampanye kemudian. Tim pembersih sungai berperahu sudah ada (UPK Badan Air Dinas LH, PPSU) dan sungai tetap kotor → rancang ulang jadi [[penjaga-sungai]] (pantau, lapor, audit merek untuk [[tanggung-jawab-produsen-diperluas]], kinerja = sampah masuk turun, bukan tonase).
5. [[pramono-anung]] sudah memilih normalisasi (penlok Cawang–Cililitan, anggaran pembebasan Rp 232 M); motivasinya bukan ideologi beton tapi tekanan banjir Maret 2025, hasil terukur dalam satu periode, birokrasi siap (BBWS), selaras pusat. Kewenangan desain tanggul ada di [[bbws-ciliwung-cisadane]]/Kementerian PU, gubernur memegang pembebasan lahan.
6. Tidak ada evaluasi publik banjir sebelum-sesudah normalisasi per ruas; kedua kubu berdebat dengan anekdot (702→68 titik banjir 2015–2018 tak bisa diatribusikan; Kampung Pulo terendam 2020 tak membuktikan gagal). Menuntut evaluasi independen = posisi paling kredibel.
7. Gunakan **narasi pengganti, bukan narasi tandingan** ([[narasi-pengganti]], Lakoff 2004): "Jakarta 500: kota yang memberi ruang bagi air dan bagi warganya." Celah terbaik: Pramono sendiri (Jan 2026) mengakui akar banjir = hilangnya daerah resapan → tagih konsistensinya.
8. [[tipologi-ruas-abc]]: A sudah dibeton (perbaiki), B celah berpenghuni (tuntaskan beda + standar pemindahan), C masih hijau (lindungi). Data sesi memetakannya ke Ciliwung: selatan Jagakarsa–Condet ±24 km hijau (C), tengah Cawang–Manggarai ±13 km padat = wilayah penlok (B), utara Manggarai–laut ±10 km terbangun (A). [[pesanggrahan]] koridor hijau paling utuh (20,7 dari 24,1 km).
9. Prioritas baru: **melindungi koridor hijau sebelum dibangun** (penetapan garis sempadan resmi, jalur hijau di [[rtrw-rdtr]], moratorium izin di sempadan) — paling murah karena belum ada warga yang digusur; ruas hijau justru paling sepi pembela.
10. FPIC keliru untuk warga kampung kota (hak masyarakat adat). Pakai [[standar-pemindahan-warga]]: Prinsip Dasar PBB 2007, Komentar Umum No. 7, ESS5 Bank Dunia/IFC PS5, [[uu-pengadaan-tanah]], [[perpres-62-2018-dampak-sosial-pengadaan-tanah]]. "Tidak ada pemindahan tanpa standar" lebih kuat daripada "tanpa penggusuran" mutlak.
11. Sumur resapan hampir tidak mencegah penurunan tanah (penyebab: sedotan air tanah dalam yang terpisah lapisan lempung); yang terbukti (Tokyo, Bangkok) = air perpipaan + larang & tegakkan sedotan → [[pergub-dki-zona-bebas-air-tanah]] dan target [[pam-jaya]] 100% 2030. Air hujan membantu bila **ditampung-dan-dipakai**. Kewajiban persil sudah ada sejak Kepgub 115/2001 & [[pergub-sumur-resapan]] 20/2013 (era Jokowi): "Kami tidak minta Pemprov menggali sumur; kami minta Pergub 2013 ditegakkan ke pemilik gedung."
12. [[kota-peka-air]] (Brown, Keath & Wong 2009): Jakarta berinvestasi di tahap 3 (drainase/tanggul) padahal tahap 1 (air perpipaan) dan 2 (sanitasi) belum tuntas → tanah terus turun, sungai tetap cemar. "Ruang Air" = tuntaskan fondasi + lompat ke tahap 4–5, tanpa membuang tahap 3.

## Keputusan & sikap
- Pengguna memutuskan jalur: **kampanye advokasi & pengorganisasian massa** warga bantaran, inventarisasi keberhasilan komunitas, momentum 5 abad Jakarta [kata-pengguna].
- Pengguna menegaskan cakupan **seluruh sungai Jakarta**, Condet hanya contoh [kata-pengguna].
- Pengguna ingin bahasa lain untuk "naturalisasi" agar tidak identik program Anies [kata-pengguna]. Usulan sesi: nama berlapis — **Ruang Air Jakarta** (publik), **Kota Peka Air** (kebijakan), empat pilar: Ruang untuk Kali · Persil Menahan Hujannya · Berhenti Menyedot · Kali Bersih dari Hulu.
- Sikap yang disarankan: "Beton bukan pilihan pertama" (bukan "tolak beton"); posisikan gerakan sebagai penyedia solusi program banjir Pramono; bingkai lintas gubernur (Ali Sadikin 1974, Basuki 2015, konsep 2019); jangan sebut nama gubernur sebelumnya; selalu sebut yang disetujui sebelum yang ditolak; setiap klaim ekologis wajib angka/kajian; jangan membela rumah kering di hulu dengan mengorbankan rumah basah di hilir.
- Setiap aksi harus berujung instrumen tertulis (Pergub, Kepgub, baris anggaran, PKS); momen 500 tahun untuk regulasi/komitmen, uang lewat Musrenbang 2027 → RKPD/APBD 2028.

## Koreksi penting
- "Pencemar utama = perusahaan di hulu" → [dikoreksi] beban organik terbesar dari limbah domestik; hulu Ciliwung = alih fungsi lahan (banjir/sedimen) [belum-diverifikasi untuk besaran].
- "Bentuk tim warga berperahu" → [dikoreksi] sudah ada (UPK Badan Air Dinas LH, PPSU); perlu dirancang ulang, bukan dibuat baru.
- "Seret Pramono tolak betonisasi" → [dikoreksi] Pramono sudah meneken penlok & menganggarkan Rp 232 M; tuntutan realistis = pengecualian ruas Condet ke hulu + standar pemindahan.
- "FPIC untuk warga bantaran" → [dikoreksi] FPIC melekat pada masyarakat adat (UNDRIP Ps. 10, ILO 169); gunakan standar penggusuran PBB/ESS5/Perpres 62/2018.
- "Naturalisasi tanpa penggusuran" → [dikoreksi] rencana naturalisasi 2019 pun mensyaratkan pembebasan 118 bidang di 4 kelurahan (±Rp 160 M); naturalisasi butuh lahan lebih lebar.
- "Sumur resapan mencegah land subsidence" → [dikoreksi] hampir tidak; penawarnya berhenti menyedot air tanah dalam. Tanah yang sudah turun tidak bisa naik.
- "Sumur resapan netral politik" → [dikoreksi] identik Anies 2021; anggaran 2022 dicoret DPRD dengan fraksi PDIP ikut mendorong.
- "EbA bisa menggantikan tanggul" → klaim belum punya bukti hidraulik; EbA = bagian strategi adaptasi, bukan pengganti.
- Klaim Pramono "lebih dari 40% banjir Jakarta dari Ciliwung" → belum ditemukan kajian publik pendukung [belum-diverifikasi].
- Cheonggyecheon sering dikutip sebagai naturalisasi → [dikoreksi] itu lanskap/peremajaan kota, airnya dipompa; tak memenuhi kriteria Palmer dkk. 2005.
- Angka 702→68 titik banjir (BPBD 2015–2018) → tidak bisa dipakai sebagai bukti efek normalisasi (angka seluruh kota, curah hujan berbeda).

## Belum selesai / langkah berikutnya
- [ ] Cek peta penlok resmi: apakah ruas depan Padepokan / Balekambang termasuk? (menentukan strategi mencegah vs membentuk ulang)
- [ ] Permohonan informasi publik (UU 14/2008) ke Dinas SDA: dasar angka "40%", peta penlok semua ruas (Krukut, Cakung Lama, Mampang), debit rencana & periode ulang BBWS, status penetapan garis sempadan
- [ ] Data kejadian banjir per kelurahan (BPBD) untuk membandingkan ruas sudah/belum dinormalisasi; data kondisi warga pasca-relokasi sejak 2015
- [ ] Susur kali Ciliwung selatan & Pesanggrahan dengan formulir yang sama; cek status 12 lahan kandidat via BPN/RDTR
- [ ] Inventarisasi kasus dengan format tetap & tangga bukti (termasuk kasus gagal)
- [ ] Cari mitra kampus untuk pemodelan hidraulik opsi hibrida ruas Condet; cari juru bicara teknis & ahli hidrogeologi
- [ ] Cek nomor dan isi Standar Norma dan Pengaturan Komnas HAM tentang hak atas tempat tinggal layak
- [ ] Pelajari laporan evaluasi Citarum Harum; kontrak politik JRMK dengan dua gubernur sebelumnya
- [ ] Uji nama "Ruang Air" ke warga, dinas, jurnalis
- [ ] Modul 3 masih membingkai tuntutan pertama khusus Condet — tawaran mengubahnya ke kerangka A/B/C belum dijawab pengguna
- [ ] Tawaran: simpan skrip analisis ke repo, buat formulir susur kali / pelacak 12 lahan — belum dijawab
- [ ] Verifikasi angka studi kasus (BBWS, PUB, Rijkswaterstaat), angka Tokyo/Bangkok, syarat SNI, status perluasan zona bebas air tanah

## Terkait
- [[isu-sungai]] [[isu-air]] [[isu-tata-ruang]] [[isu-sampah]] [[isu-iklim-kota]] [[isu-advokasi-kebijakan]] [[isu-hutan-kota]]
- [[2026-11-17-hutan-kota-ui-sekolah-rakyat]] (Jagakarsa/Srengseng Sawah berada di zona hijau Ciliwung selatan; aktor Pramono sama)
- [[jakarta]] [[ciliwung]] [[condet]] [[pesanggrahan]] [[pramono-anung]] [[bbws-ciliwung-cisadane]] [[pam-jaya]]
- [[adaptasi-berbasis-ekosistem]] [[kota-peka-air]] [[standar-pemindahan-warga]] [[tipologi-ruas-abc]] [[narasi-pengganti]]

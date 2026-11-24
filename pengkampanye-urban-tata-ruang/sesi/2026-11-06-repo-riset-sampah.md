---
jenis: sesi
tanggal: 2026-11-06
sumber: branch origin/claude/riset-advokasi-sampah (+ berkas tambahan di origin/claude/wawancara-kontan)
isu: [sampah, iklim, advokasi, sungai, air, tata-ruang]
tag: [epr, p75, psel, perpres-109-2025, danantara, saset, pemulung, cop31, analisis-struktural, policy-brief, siaran-pers, wawancara-kontan, verifikasi-fakta, metana, sndc]
---

# Repo riset advokasi sampah hulu–hilir: "Hulu Dibiarkan, Hilir Dibakar" (6–10 Nov 2026)

> Tanggal log = commit pertama riset sampah (2026-11-06, `3028b13`). Dua commit 2026-10-08 di branch yang sama
> adalah pipeline arsip media Delta Kapuas (`tools/arsip_dk/`, `docs/rencana-penamaan-delta-kapuas.md`), topik lain,
> tidak diekstraksi di sini. Branch `claude/wawancara-kontan` hanya menambah: `reports/Wawancara Kontan sampah plastik.md`,
> `research_notes/.../pembanding_negara_penduduk.md`, serta versi lain `Konteks diskusi`/`Framework rilis`.
> Transkrip sesinya ditangani agen lain; log ini hanya membaca berkas repo.

## Pertanyaan / tujuan
- Membangun basis bukti dan produk advokasi WALHI soal kebijakan sampah: menggeser tanggung jawab dari warga ke
  **produsen dan negara**, menolak pembakaran ([[solusi-palsu]]), dan memanfaatkan jendela kebijakan (Permen pengganti
  P.75, COP31 Antalya 9–20 Nov 2026, Jakstranas baru, Prolegnas 2027).
- Prinsip kerja yang dipegang sepanjang repo: **"bingkai kritis, senjata empiris"** — pembingkaian dari ekologi politik,
  tetapi setiap angka berlabel verifikasi dan rumusan "aman-kutip".

## Yang dihasilkan
(semua path di branch `origin/claude/riset-advokasi-sampah` kecuali disebut lain)
- `reports/Kebijakan sampah hulu hilir Indonesia.md` — laporan riset utama (rantai material, peta kebijakan, matriks 18 bidang
  masalah, Bacchi/IDS/keadilan ekologis, inventaris 136 dokumen WALHI, kontra-argumen, pintu masuk advokasi).
  Versi HTML bergambar `reports/hulu-dibiarkan-hilir-dibakar.html` (v3), artifact https://claude.ai/artifact/J6q3T4mtmrvuUBVkJfA8r1
- `reports/Policy brief - Hulu Dibiarkan Hilir Dibakar.md` (draf, ±1.870 kata, 32 rujukan, ditujukan ke Deputi PSLB3 KLH/BPLH;
  enam pengaman untuk Permen pengganti P.75) + `reports/Catatan penyusun policy brief.md` (uji 15 butir, status tiap angka).
  Tab utama Claude Doc https://claude.ai/artifact/EQPWUETUTHSac9dLfUeoNS
- `reports/Matriks tuntutan sampah.md` — 11 klaster tuntutan–risiko–pengaman–garis merah, 13 kontradiksi siap kutip,
  daftar "angka yang JANGAN dipakai".
- `reports/Siaran pers global COP31 - revisi.md` — "Tungku untuk Produsen, Asap untuk Warga", **dikirim 7 Nov 2026**
  (tab "Siaran pers global (7 Nov)" di Doc yang sama). `reports/Draf rilis sampah.md` — rilis nasional (ditunda) + lembar fakta.
- `reports/Analisis struktural krisis sampah.md` (10 Nov) — Causal Layered Analysis 5 lapis, uji penjelasan tandingan, titik ungkit.
- `docs/Konteks diskusi isu sampah.md` (ingatan kerja: posisi, data terverifikasi, klaim terkoreksi, status produk),
  `docs/Framework rilis WALHI - gaya [dua juru bicara senior].md` (anatomi rilis + aturan senior), `docs/Bedah rilis - Plastik Naik Rakyat Tercekik.md`.
- `reports/Wawancara Kontan - draf jawaban dan bacaan.md` (9 jawaban versi ketiga + daftar bacaan); di branch
  `claude/wawancara-kontan`: `reports/Wawancara Kontan sampah plastik.md` (strategi, jebakan bingkai, amunisi berlabel).
- 28 catatan riset di `research_notes/Kebijakan sampah hulu hilir Indonesia/` (+ `pembanding_negara_penduduk.md` di branch Kontan).

## Pokok pembelajaran
1. **Asimetri penegakan adalah tesis inti.** Produsen wajib mengelola kemasan sejak [[uu-pengelolaan-sampah]] Ps. 15 (2008),
   tetapi [[peta-jalan-pengurangan-sampah-produsen]] (P.75/2019) tanpa mekanisme sanksi: 842 dibina → 386 terdaftar → 79 peta jalan
   → **28 melaksanakan & melapor** (KLH, Okt 2026); nol sanksi ke produsen ditemukan. Sebaliknya 343 TPA disanksi, 44 TPA diselidiki
   pidana, dua mantan kepala dinas (Bali, DKI) dijerat pidana. [diverifikasi-di-sesi]
2. **Hilir dikunci sebelum hulu bergerak.** [[perpres-psel]] (Perpres 109/2025): USD 0,20/kWh 30 tahun dibeli [[pln]], pasokan
   ≥1.000 t/hari, lahan gratis dari pemda, **kompensasi** (bukan "denda") bila pasokan kurang, tipping fee dihapus, [[danantara]]
   memimpin. EPR wajib baru 2028. Menteri LH sendiri: bila pemilahan berhasil, PSEL hanya kebagian 15–20% sampah →
   kebijakan **menghukum daerah yang berhasil memilah**. → [[lock-in-psel]]
3. **Rantai logika PSEL patah di A1 dan H1** ([[rekonstruksi-teori-kebijakan]]): sampah ±40% sisa makanan, kadar air >70% vs syarat
   mesin <20% (Putri Cempo); 2 dari 12 PLTSa beroperasi; produsen absen dari rantai kebijakan. Kegagalan lalu dialamatkan ke
   "sampah warga basah" (Sutton 1999 via Kartodihardjo). Rumusan pengganti: *"negara belum membangun pengumpulan terpilah, tetapi
   sudah membeli mesin yang hanya bekerja bila sampah terpilah."*
4. **Kesenjangan yang didukung data adalah kota–desa, bukan Jawa–luar Jawa** ([[keadilan-spasial]]): SKI 2023 — perdesaan 80,8% membakar,
   5,7% diangkut; perkotaan 40,2% vs 43,3%; Kalbar 72,6% membakar, 6,7% diangkut; DKI 1,2% membakar. Podes 2024: 69,84% desa menimbun/membakar,
   ±80% desa tanpa TPS. Mandat angkut ada di kab/kota (PP 81/2012); desa tanpa mandat/pos anggaran. [diverifikasi-di-sesi untuk SKI]
5. **Tesis "produsen penyebab" hanya kuat untuk aliran kemasan (±20%).** Untuk sisa makanan (±40%) penyebab strukturalnya negara yang tak
   membangun layanan terpilah. Rumusan tahan uji: *produsen bertanggung jawab atas residu, negara atas layanan, dan pembakaran adalah
   titik temu yang membebaskan keduanya.* → [[hulu-hilir-sampah]]
6. **Hulu dan hilir dipegang kelompok yang sama:** anak usaha [[chandra-asri]] (penerima tax holiday 20 tahun) di konsorsium PSEL Serang Raya,
   pertamina-power-indonesia di Yogyakarta Raya, bakrie-power di Surabaya Raya; produsen barang konsumsi menghitung RDF di tanur semen
   sebagai "dikumpulkan dan diproses" (54% plastik Unilever Indonesia 2022 ke RDF). Negara menyubsidi hulu (tax holiday, HGBT, PSN, bea masuk 0%)
   dan tak memungut cukai plastik tiga APBN berturut-turut. [belum-diverifikasi untuk porsi saham & angka 54%]
7. **Pemulung = subsidi tersembunyi bagi produsen** ([[subsidi-tersembunyi-pemulung]]): 65% PET terkumpul di Jabodetabek; ±80% daur ulang
   tercatat dikerjakan informal (World Bank WaW 3.0, olahan); "nearly all recycling volumes" (SYSTEMIQ untuk CGF). Program Agustus 2026 hanya diskon
   iuran BPJS-TK (Rp16.800→Rp8.400), tanpa dasar regulasi; Menteri: "Pemulung kita ganti dengan pekerja pemilah sampah".
8. **EPR wajib bisa dibajak** ([[kepatuhan-semu-epr]]): Filipina menghitung kiln semen sebagai pemulihan, India ±700.000 sertifikat palsu, Vietnam
   tarif di bawah biaya riil. Yang menentukan: apa yang dihitung, siapa mengaudit, berapa iurannya → enam pengaman di policy brief.
9. **Lima pola dasar sistem** (Senge/Meadows) cocok dengan bukti: memindahkan beban (terpenting), memindahkan beban ke pihak lain, perbaikan yang gagal,
   tujuan yang merosot, yang kuat makin kuat. Tiga titik ungkit kosong: **ukuran resmi** ("terkelola" → "timbulan berkurang"), **keterbukaan data**
   (volume kemasan per produsen, biaya kompensasi PSEL), **mandat layanan desa**. → [[titik-ungkit-meadows]]
10. **Iklim: SNDC merencanakan emisi limbah 2030 naik ±74% dari 2019** di ketiga skenario, dan menghitung PLTSa/RDF/SRF sebagai mitigasi; KLH: sampah
    ±61% emisi metana nasional, tanpa target metana; Indonesia tak tercantum di 65 pendukung Deklarasi Metana Organik COP29. RUPTL 2025–2034
    mengklasifikasikan sampah sebagai EBT (PLTSa 453 MW). [diverifikasi-di-sesi]
11. **Disiplin label menyelamatkan kredibilitas:** banyak angka populer gerakan ternyata keliru/lemah (lihat Koreksi). Klaim ke perusahaan hanya dengan
    atribusi (audit BFFP, data perusahaan sendiri, siaran pers KLH) dan kata "diduga/tercantum".
12. **Aturan rilis senior WALHI:** maks 2 halaman, tuntutan dinarasikan dengan alamat ("Karena itu WALHI meminta KLH untuk…"), lead 5W+1H, kutipan
    langsung, satu rilis satu isu. Plus prinsip pengguna: **petakan janji pemerintah dulu** — tuntut *selisih* antara janji dan isinya, bukan hal yang
    sudah dijanjikan. → [[peta-janji-pemerintah]]

## Keputusan & sikap
- **PSEL, PLTSa, RDF, pirolisis, co-processing tanur semen ditolak total.** Pembakaran bukan daur ulang dan tak boleh dihitung sebagai pemenuhan EPR
  (posisi minimum di brief: iuran produsen tidak boleh membiayai pembakaran dalam bentuk apa pun).
- **EPR mengikat** sesuai Ps. 15: iuran produsen membiayai pengangkutan sampai desa; **iuran tidak menggantikan kewajiban negara**.
- Pembakaran sampah rumah tangga dibingkai sebagai **akibat kegagalan layanan**, bukan kebiasaan warga. Contoh pengalaman pengguna: di kampungnya
  di Kalimantan warga membawa sendiri sampah ke TPS, lalu sampahnya dibakar. [kata-pengguna]
- Karhutla dari bakar sampah: cukup satu kalimat, bingkai kegagalan layanan (BPBD Lamandau, Pemkot Pekanbaru), tidak masuk brief.
- Global/COP31: tolak kredit karbon & kredit plastik dari pembakaran/TPA lewat Pasal 6.2/6.4; akui komunitas lewat Pasal 6.8; dukung pembatasan produksi
  plastik primer; buka daftar delegasi & sponsor paviliun.
- Prinsip kehati-hatian: setiap tuntutan punya pengaman (urutan: fasilitas dulu, larangan kemudian; penegakan ke produsen/distributor, bukan warung).
- Editorial: "desakan" bukan "ujian"; tanpa pembanding Manila/Filipina sebagai model sukses; tanpa nomor telepon; nama perusahaan hanya berdasar data
  mereka sendiri/audit teratribusi; sponsor ditulis "tercantum sebagai sponsor dan mitra".
- Policy brief ditandatangani WALHI sendiri, gaya Tempo Institute + WALHI; Opsi 4 = rancangan KLH + enam pengaman (bukan tandingan).

## Koreksi penting
- "14% polusi Jakarta dari bakar sampah" → tidak valid; kajian ITB–Vital Strategies hanya 9–11% PM2.5 dari pembakaran terbuka biomassa & bahan lain di dua lokasi pinggiran. [dikoreksi]
- "9,02 juta t CO2e metana TPA (2025)" → estimasi WALHI sendiri (334.109 t CH4); inventaris resmi penimbunan TPA ±39,3 juta t CO2e (2022, GWP AR2). [dikoreksi]
- "260 dari 514 kab/kota darurat sampah" → KLH: "lebih dari 160" (Okt 2025). "Rp89 triliun untuk 33 PSEL" → Rp87–91 T (Pandu/Rosan). [dikoreksi]
- Perpres 109/2025 memuat **kompensasi** dan wanprestasi (Ps. 17(2)d–e), bukan "denda"; "denda" hanya ucapan Menteri. [dikoreksi]
- Laporan "The Fraud of Plastic Recycling" (2024) diterbitkan Center for Climate Integrity, bukan CIEL; PRAISE 2018, IPRO 2020; eco-modulation PPWR UE tidak berlaku
  segera; Leuwigajah 2005 (TLH menulis 2006). [dikoreksi]
- "Saset adalah pajak kemiskinan / lebih mahal per ml" → bukti bercampur (India & Filipina saset lebih murah per ml); klaim "40%" tak terlacak. Pakai: *saset murah
  di kasir karena biaya pengumpulan & pencemarannya tidak masuk harga.* [dikoreksi]
- "Pemerintah hanya menyalahkan warga" → *tanggung jawab produsen sudah masuk pidato, tetapi diagnosis akar masalah tetap perilaku warga, dan aturan yang mengikat
  produsen belum terbit.* [dikoreksi]
- "Indonesia menolak pembatasan produksi plastik" → "belum menyatakan dukungan pada target pengurangan produksi yang mengikat". [dikoreksi]
- "Indonesia belum punya EPR wajib" → World Bank mencatat EPR Indonesia "Mandatory/legally-binding" (P.75). Pakai: *wajib di atas kertas: hanya peta jalan, tanpa iuran
  & sanksi; 28 dari 842.* "Produsen membayar nol" harus diberi "sampai hari ini" (rancangan pengganti P.75 menjanjikan iuran). [dikoreksi]
- Putri Cempo & Bali: kajian WALHI 2024 (dibaca primer 10 Nov) mencatat sampah Bali **diterima dan diolah** sebagai fakta; motif "menyeimbangkan komposisi" hanya
  dugaan ("suspected"). Jangan tulis motif sebagai temuan. [dikoreksi]
- Kasus e-waste Batam: 914 kontainer = total **tiga** importir (Esun 386, Logam Internasional Jaya 412, Batam Battery Recycle 116), 822 dan 914 kasus yang sama;
  "Brokers of Shame" (BAN) mengaitkan PT Esun, bukan LIJ; PT Genesis didakwa soal pengelolaan/dumping B3, bukan impor. [dikoreksi]
- "Perpres 97/2017 dasar EPR" (TLH 2026) keliru — itu Jakstranas; "P.75 Tahun 2018" di rilis KLH salah ketik; "Menteri LH Hanif" untuk peristiwa setelah 27 Apr 2026 →
  Moh Jumhur Hidayat. "Jawa vs luar Jawa" selisih hanya ±5,5 poin. "Siklus tutup" tidak terkonfirmasi. Perbandingan PSEL 1,5–2,5× belanja persampahan pemda =
  hitungan penyusun berkeyakinan rendah, jangan disebut "subsidi". [dikoreksi]

## Belum selesai / langkah berikutnya
- [ ] Cek JDIH KLH: apakah Permen pengganti P.75 sudah terbit (cari "Nomor 15 Tahun 2026"); target penetapan Nov 2026, sebelumnya Sep 2026.
- [ ] Baca teks resmi Perpres 109/2025 (Ps. 4, 17, 18, 20 dan pasal transisi; klausul terminasi PJBL).
- [ ] Verifikasi keanggotaan anak usaha Chandra Asri di konsorsium PSEL Serang Raya (dokumen Danantara/keterbukaan TPIA) sebelum dipakai di rilis.
- [ ] Permohonan informasi publik: angka kompensasi PSEL ke PLN + BPP pembanding (Kemenkeu, PLN); studi kelayakan/AMDAL/PJBL per lokasi (model Benowo).
- [ ] Lampiran P.70/2016 (frekuensi uji dioksin) dan Lampiran P.75/2019 (klaim saset <50 ml/5 ml); rilis OECD 2024 (96% vs 55%); tabel asli Podes 2024.
- [ ] Data lapangan pertama: harga per ml 10–15 pasang saset vs botol di satu warung & satu minimarket.
- [ ] Prolegnas Prioritas 2027 sebagai jendela revisi UU 18/2008 (bahas dengan atasan); revisi UU PPLH (Prioritas 2026) sebagai kendaraan alternatif.
- [ ] Tawaran belum diambil: lembar satu halaman untuk tim Antalya; rilis "rapor" pascasesi paviliun (sesi C2 14 Nov, MoU opsional; C3 16 Nov EPR);
      revisi policy brief dengan rekonstruksi Perpres 109 sebagai figur utama.
- [ ] Wawancara Kontan: izin bicara atas nama WALHI Nasional dan koordinasi dengan juru bicara sampah (Manajer Kampanye Keadilan Urban); langkah ketiga
      ("buka data volume kemasan") belum jadi tuntutan resmi WALHI — minta persetujuan.
- [ ] Kantor WALHI mana yang ikut audit BFFP; daftar resmi CCAC (apakah Indonesia bergabung belakangan); status Suwung pasca 31 Juli 2026 & transisi Bangun/Tropodo.

## Terkait
- [[isu-sampah]] · [[isu-iklim-kota]] · [[isu-advokasi-kebijakan]] · [[isu-sungai]] · [[isu-air]] · [[isu-tata-ruang]]
- Konsep: [[hulu-hilir-sampah]], [[solusi-palsu]], [[tanggung-jawab-produsen-diperluas]], [[keadilan-ekologis]], [[keadilan-spasial]],
  [[ekologi-politik]], [[privatisasi-layanan-dasar]], [[transisi-berkeadilan]], [[partisipasi-bermakna]], [[kerentanan-iklim]]
- Regulasi: [[uu-pengelolaan-sampah]], [[perpres-psel]], [[peta-jalan-pengurangan-sampah-produsen]], [[uu-pplh]], [[amdal]], [[uu-cipta-kerja]]
- Aktor: [[kementerian-lh]], [[danantara]], [[pln]], [[walhi]], [[kementerian-esdm]], [[pemprov-dki-jakarta]]
- Tempat: [[solo-putri-cempo]], [[jakarta]], [[batam]], [[kalimantan-barat]]
- Ekstraksi entitas: `ekstrak/D-sampah-repo.md`

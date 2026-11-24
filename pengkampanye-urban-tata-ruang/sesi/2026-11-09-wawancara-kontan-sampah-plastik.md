---
jenis: sesi
tanggal: 2026-11-09
sumber: https://claude.ai/code/session_01HPqUVK3RM5Qw5VcV9A6mCK
isu: [sampah, advokasi, iklim]
tag: [wawancara-media, kontan, saset, epr, psel, bingkai, koreksi-klaim, pembanding-negara]
---

# Persiapan wawancara tertulis Tabloid Kontan: sampah plastik (WALHI)

## Pertanyaan / tujuan
Pengguna (staf baru WALHI Nasional, pengkampanye urban & tata ruang) diwawancarai tertulis oleh wartawan Tabloid Kontan (media bisnis) dengan 9 pertanyaan soal sampah plastik: konsumsi vs sistem, titik lemah rantai, ketergantungan plastik sekali pakai, saset/multilapis, daur ulang ekonomis, kapasitas industri daur ulang, fokus hilir vs hulu, tiga langkah mendesak, kondisi saat ini. Pengguna ingin **menjawab sendiri**: Claude diminta memberi strategi, menandai jebakan bingkai, mengajukan pertanyaan balik, dan mengecek klaim — bukan menulis draf. Permintaan tambahan selama sesi: pembanding dengan negara berpenduduk setara, framing dengan rumus risiko BNPB (R = H × V / C), "jadi juru bicara sampah WALHI" (lensa juru bicara), cek ulang kebijakan terbaru, dan memakai kerangka analisis kebijakan Kartodihardjo.

## Yang dihasilkan
Berkas di branch `origin/claude/wawancara-kontan` (di-commit & push oleh sesi):
- `reports/Wawancara Kontan sampah plastik.md` — strategi 3 pesan, tabel jebakan+amunisi per pertanyaan (berlabel), §2b pembanding negara & BNPB, §2c cek ulang kebijakan 9 Nov 2026, §2d lensa juru bicara WALHI (kerangka IDS), §2e lima tema Kartodihardjo dipetakan ke pertanyaan, §2f koreksi & amunisi dari analisis struktural (10 Nov), §3 daftar yang harus dihindari, §4 pertanyaan balik.
- `research_notes/Kebijakan sampah hulu hilir Indonesia/pembanding_negara_penduduk.md` — data World Bank What a Waste 3.0 (versi Mar 2026) dan Cottom dkk. 2024 (Nature).
- Pembaruan `docs/Konteks diskusi isu sampah.md` bagian 6 (temuan sesi Kontan), plus dua merge dari `claude/riset-advokasi-sampah` (satu konflik diselesaikan dengan mempertahankan kedua versi).
Commit kunci: 19d30dc, 4a2f509, c4f0a96, 1239f9b, 213c6d1, 047fd1c. Tidak ada artefak claude.ai.

## Pokok pembelajaran
1. **Jangan jawab 9 pertanyaan; ulangi 3 pesan.** 1/2/7/9 = "di mana masalahnya", 4/5/6 = "saset & daur ulang", 3 varian dari 1, 8 = tuntutan. Kalimat pertama tiap jawaban harus bisa berdiri sendiri sebagai kutipan (tabloid memotong).
2. **Pesan inti usulan**: (P1) masalahnya di desain produk dan di negara, bukan di dompet warga — desa 80,8% RT membakar, 5,7% diangkut (SKI 2023); (P2) produsen membayar nol, publik menanggung — 28 dari 842 produsen menjalankan & melaporkan peta jalan [[peta-jalan-pengurangan-sampah-produsen]]; (P3) saset tak selesai dengan daur ulang/pembakaran; (P4 opsional) negara mengunci hilir (PSEL 30 tahun) sebelum hulu bergerak (EPR penuh 2028). Rumus aman: **"produsen yang memproduksi masalahnya, negara yang membiarkannya."**
3. **Bingkai media bisnis: "siapa yang membayar?"** — APBD, PLN/APBN, warga (asap), pemulung (±80% daur ulang tercatat dikerjakan sektor informal) vs produsen yang hari ini belum membayar.
4. **Jebakan bingkai**: No. 3 paling berbahaya (warga dijadikan pelaku → ganti subjek: warga tidak diberi pilihan; "sampah belum dipilah" → "negara belum membangun pengumpulan terpilah"); No. 1 dikotomi palsu; No. 5 "ekonomis" membuka jalan ke RDF/pembakaran berlabel daur ulang → jawab tegas "tidak" (kasus CreaSolv Unilever); No. 6 jujur soal ketiadaan angka daur ulang per polimer → kritik transparansi; No. 7 menguntungkan asal dibuktikan dengan urutan waktu.
5. **Rancangan pengganti P.75 sudah memuat iuran produsen ke PRO nonprofit** ("dihitung secara proporsional berdasarkan volume dan jenis kemasan"; importir ikut; KLH 8 Sep 2026). Jadi "produsen membayar nol" harus diberi keterangan "sampai hari ini". Empat tuntutan konstruktif: iuran cukup untuk angkut sampai desa? RDF/pembakaran dihitung "terkelola"? ada target pengurangan, bukan hanya pengumpulan? saset disentuh?
6. **World Bank mengode EPR Indonesia "mandatory/legally-binding"** (berdasar P.75/2019) → hindari "Indonesia belum punya EPR wajib"; pakai "wajib di atas kertas, tanpa iuran dan sanksi; 28 dari 842".
7. **Beban dilempar ke bawah**: SE Menteri LH No. 2/2026 meminta pemda membuat Perda pembatasan plastik sekali pakai (>300 kab/kota sudah punya, dari 216 pada 2025) — produsen tidak disasar.
8. **Pembanding negara**: memilih karena jumlah penduduk lemah secara analitis; pakai Brasil (sama UMIC, cakupan pengumpulan 93% vs Indonesia 62,5%) dan AS (untuk ekspor risiko). Porsi plastik di sampah Indonesia 19,2% tertinggi di antara 6 negara. Cottom 2024: emisi plastik Indonesia 3,4 Mt/th (2020), peringkat 3 dunia, setara Nigeria; di Global South plastik fleksibel lebih mungkin lepas (56:44) — mendukung argumen saset.
9. **Rumus BNPB punya jebakan**: "kapasitas rendah" mengundang solusi "tambah kapasitas" = insinerator. Pengaman: ancaman (H) **diproduksi** produsen (intensitas kemasan, bukan perilaku konsumen); kapasitas (C) juga regulasi/kelembagaan (EPR yang ditegakkan); insinerator menaikkan kerentanan (V) warga sekitar. Cukup jadi kerangka berpikir, tak perlu disebut ke wartawan.
10. **Lensa juru bicara WALHI (kerangka IDS: diskursus–aktor–kepentingan)**: diskursus "kesadaran warga" & "sampah = energi"; aktor KLH, Danantara, PLN, pemenang tender, 74 entitas konsultasi EPR (mayoritas industri; tanpa LSM/pemulung); kepentingan: kontrak 30 tahun hilir dikunci sekarang, iuran hulu baru 2028. Garis WALHI: krisis sampah = kegagalan negara; sampah layanan publik, bukan bisnis.
11. **Kartodihardjo (5 tema) → pertanyaan**: isi (asumsi kebijakan PSEL patah: sampah basah, produsen absen) → No. 7; proses/wacana (Sutton 1999: kegagalan dialamatkan ke "orang di lapangan") → No. 1, 3; organisasi (pemda tanggung kompensasi, APBD persampahan rata-rata 0,53%) → No. 2; dampak/distribusi biaya → No. 6, 8; konteks (100% terkelola 2028, 33 PSEL) → No. 9. Kritik: analisis itu membedah PSEL, wawancara soal plastik — jangan semua jawaban ditarik ke PSEL.
12. **Amunisi struktural (10 Nov)**: kutipan Reuters 2022 — eksekutif Unilever menyebut saset multilapis "evil because you cannot recycle it", tapi di Sri Lanka melobi "sachets are a poor man's commodity"; kantong plastik berbayar 2016 turunkan pemakaian 25–30% lalu dihentikan; cukai plastik diusulkan sejak 2016 tak pernah dipungut; bank sampah 1,7–2,7% sampah nasional; survei Greenpeace 2021: 55% warga menunjuk produsen, ~70% mau isi ulang bila harga sama.

## Keputusan & sikap
- Tanggung jawab ditempatkan pada **produsen** (terutama besar/global) dan **negara**, bukan warga; paradigma keadilan ekologis WALHI; prinsip "bingkai kritis, senjata empiris" [kata-pengguna, dari prompt sesi].
- PSEL/insinerator ditolak; pembakaran, RDF, co-processing semen **bukan daur ulang** dan tidak boleh dihitung sebagai EPR.
- Jawaban harus konsisten dengan siaran pers WALHI jelang COP31 (7 Nov 2026) "Tungku untuk Produsen, Asap untuk Warga" (lima desakan).
- Menyebut nama perusahaan hanya dengan atribusi (audit BFFP yang WALHI ikut laksanakan, atau data perusahaan sendiri); tulis "Santos Jaya Abadi/Kapal Api"; tanpa kata sifat menuduh.
- Koordinasi dengan juru bicara sampah WALHI Nasional dan atasan sebelum mengirim (pengguna menyatakan sudah dapat izin).
- Kutipan juru bicara bukan pengganti — telepon langsung 15 menit lebih akurat.
- No. 8 diselaraskan dengan rilis COP31: (1) EPR mengikat dengan iuran yang membiayai pengangkutan sampai desa, pembakaran tidak dihitung; (2) larangan bertahap saset + kewajiban guna ulang/isi ulang; (3) hentikan PSEL, alihkan anggaran ke pengumpulan terpilah, kompos, perlindungan pemulung.

## Koreksi penting
- "14% polusi Jakarta dari bakar sampah" → tidak valid.
- 9,02 Mt CO2e → estimasi WALHI sendiri, bukan inventaris resmi.
- "Rp89 triliun" (dipakai di judul rilis WALHI) → tak ada sumber resmi; pakai "sekitar Rp87–91 T" dengan atribusi (Rosan, Okt 2025: Rp91 T; Pandu, Mei 2026: ±Rp87 T).
- "Denda" bagi pemda dalam Perpres 109/2025 → teksnya "kompensasi".
- "Pembakaran naik dari Riskesdas 2018" → metode survei beda; jangan dibandingkan.
- "Luar Jawa jauh lebih parah" → kesenjangan yang didukung data adalah kota vs desa.
- Filipina/Manila sebagai model keberhasilan EPR → jangan (pembakaran di kiln ikut dihitung); boleh dipakai hanya untuk "multinasional yang sama patuh EPR wajib di sana".
- Sutton (1999) via Kartodihardjo → semula tak ada di repo; kemudian ditemukan di `rekonstruksi_teori_kebijakan_perpres109.md` (Pendahuluan hlm. 19–20). Untuk tabloid bisnis, pakai idenya tanpa nama akademisi.
- "Putri Cempo menerima/mendatangkan sampah dari Bali/luar daerah" → hanya sumber sekunder & klaim warga; yang terdokumentasi baru rencana kerja sama.
- Saset "pajak kemiskinan"/"lebih mahal per ml" → di India & Filipina saset dilaporkan lebih murah; data Indonesia tidak ada. Pakai: "saset murah di kasir karena biaya pengumpulan dan pencemarannya tidak masuk harga".
- "Pemerintah hanya menyalahkan warga" → Menteri LH pernah menyatakan EPR akan diwajibkan; pakai "tanggung jawab produsen sudah masuk pidato, tapi diagnosis akarnya tetap perilaku warga dan aturan mengikat belum terbit".
- "Indonesia menolak pembatasan produksi plastik" → "belum menyatakan dukungan pada target pengurangan produksi yang mengikat".
- "Resin baru murah mematikan daur ulang" → tidak berlaku 2026 (harga resin naik).
- "Pembayaran PSEL 1,5–2,5× belanja persampahan pemda" → keyakinan rendah, jangan dipakai.
- "Indonesia peringkat 2 dunia polusi plastik" (Jambeck 2015, data 2010) → versi terbaru Cottom 2024: peringkat 3.
- Laman KLH menulis "Permen LHK Nomor 75 Tahun 2018" → seharusnya 2019.
- "Kesadaran tidak berpengaruh" → studi Medan 2026 juga menemukan pengaruh pendidikan; jangan diklaim.

## Belum selesai / langkah berikutnya
- [ ] Pengguna belum mengirim tiga pesan inti versinya sendiri, tenggat & format dari wartawan, dan pilihan pembanding (Brasil/AS).
- [ ] Siapkan jawaban susulan "Bukankah saset membantu warga miskin membeli porsi kecil?".
- [ ] Cek JDIH KLH tepat sebelum mengirim: apakah pengganti P.75 terbit November 2026 (target ini baru dari ringkasan pencarian).
- [ ] Cek Nota Keuangan/RAPBN 2027 soal cukai plastik.
- [ ] Cek ulang APBD persampahan 0,53% (Bappenas, SIPD 2025) dan kutipan asli Menteri LH soal PSEL hanya kebagian 15–20% sampah.
- [ ] Artikel Kontan soal risiko fiskal pemenang tender PSEL tidak terbaca (HTTP 403).
- [ ] Data per negara Cottom (AS, Pakistan, Brasil, Bangladesh) hanya ada di SD_03 Dryad (1,45 GB) — belum dibuka.
- [ ] Selisih timbulan Indonesia di World Bank (55,4 Mt) vs SIPSN publik (25–33 Mt) belum dijelaskan.
- [ ] Beri keterangan "sampai hari ini" pada bingkai "produsen membayar nol" di siaran pers COP31 dan draf policy brief.

## Terkait
- [[isu-sampah]] · [[isu-advokasi-kebijakan]] · [[isu-iklim-kota]]
- [[tanggung-jawab-produsen-diperluas]] · [[peta-jalan-pengurangan-sampah-produsen]] · [[uu-pengelolaan-sampah]] · [[perpres-psel]] · [[se-menlh-2-2026-plastik-sekali-pakai]] · [[jakstranas-sampah]]
- [[hulu-hilir-sampah]] · [[solusi-palsu]] · [[kerentanan-iklim]] · kerangka-risiko-bnpb · [[segitiga-diskursus-aktor-kepentingan]] · [[ekonomi-saset]] · [[subsidi-tersembunyi-pemulung]]
- [[walhi]] · [[kementerian-lh]] · [[danantara]] · [[pln]] · [[unilever]] · [[break-free-from-plastic]] · [[chandra-asri]]
- [[solo-putri-cempo]] · [[jakarta]] · [[kalimantan-barat]]
- Sesi kembar: [[2026-11-15-kampanye-sampah-zero-waste-psel]]

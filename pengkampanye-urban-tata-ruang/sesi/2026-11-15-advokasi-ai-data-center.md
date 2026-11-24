---
jenis: sesi
tanggal: 2026-11-15
sumber: https://claude.ai/code/session_01HPqUVJRX6ht5MZZh6D6cvz
isu: [data-center, air, iklim, tata-ruang, advokasi]
tag: [ai-data-center, agen-persona, batam, nongsa, sambau, jatiluhur, bdx, danantara, byoe, new-asia-forum, amdal-kawasan, perpres-ai, ruptl, pln, johor, rapor-operator, kip, dosir]
---

# Advokasi AI data center: riset 8 agen ber-persona, dosir, dan strategi "Syarat Dulu, Baru Server"

## Pertanyaan / tujuan
Pengguna (pengkampanye WALHI, Eksekutif Nasional) akan mengadvokasikan isu AI data center. Dari ponsel ia minta [kata-pengguna]:
- beberapa agen dengan keahlian berbeda (AI, lingkungan, keduanya, strategi, ekonomi, dll.), masing-masing memakai persona tokoh nyata (mis. "profesor AI atau mantan pekerja Anthropic yang keluar karena tahu bahaya AI");
- analisis seluruh masalah AI global, terutama AI data center, karena menurutnya "masalah di Indonesia bakal di AI data center-nya";
- mind map masalah, penjelasan naratif dengan cerita dan figure;
- dikerucutkan ke kasus Indonesia yang sudah ada dan yang akan datang, serta apa yang perlu ia lakukan sebagai pengkampanye.

Di akhir sesi ia minta jawaban dalam bentuk HTML ("pake answer me with html").

Catatan: sesi dimulai 15 Nov 2026 pukul 00:39 UTC dan selesai sekitar 01:06 UTC.

## Yang dihasilkan
**Artefak**
- Dosir lengkap "Peta masalah AI dan data center": peta pikiran interaktif dengan 10 cabang (tiap butir diberi label global/Indonesia dan kekuatan bukti), 9 grafik, kisah global dan Indonesia, 8 titik panas, celah hukum, daftar klaim yang sebaiknya tidak dipakai, strategi 90 hari. URL: https://claude.ai/artifact/EgyW97B4WhH7Qsxj2kmTdE (privat).
- `ringkasan.html`: jawaban akhir dalam bentuk HTML, dikirim sebagai berkas, tidak diterbitkan sebagai artefak.

**Berkas di branch `origin/claude/trusting-cori-urr48o`, folder `docs/advokasi-ai-datacenter/`**
- `riset/01-orang-dalam-ai.md`: persona orang dalam AI (lensa Timnit Gebru dan Mrinank Sharma). Isi: logika scaling, risiko AI non-lingkungan, narasi industri yang perlu dibongkar.
- `riset/02-ilmuwan-lingkungan.md`: persona ilmuwan lingkungan (Luccioni, Ren, de Vries-Gao, IEA). Isi: listrik, emisi, air, material, metrik.
- `riset/03-ekologi-politik-global.md`: persona Karen Hao/Kate Crawford (+Couldry & Mejias). Isi: rantai ekstraksi dan 15 kasus perlawanan global.
- `riset/04-inventaris-dc-indonesia.md`: persona jurnalis investigasi data. Isi: inventaris proyek, angka nasional, aktor dan aliran uang, titik panas.
- `riset/05-dampak-lokal-indonesia.md`: persona ahli lapangan. Isi: energi, air, lahan, dan sosial per klaster, plus hitungan ilustratif Batam.
- `riset/06-ekonomi-politik.md`: persona Acemoglu/Mazzucato/Bhima Yudhistira. Isi: gelembung AI, siapa yang membayar, insentif, lapangan kerja.
- `riset/07-hukum-kebijakan.md`: persona ala ICEL. Isi: peta regulasi, celah, tuas hukum, usulan kebijakan.
- `riset/08-strategi-kampanye.md`: persona Gary Cook + Marshall Ganz. Isi: diagnosis, theory of change, power mapping, kalender, tuntutan, narasi, rencana 90 hari, red team.
- `dosir.html` (sumber artefak) dan `ringkasan.html`.

## Pokok pembelajaran
1. **Inti masalah Indonesia ada tiga hal yang saling mengunci: listrik, air, izin.**
   - Listrik: grid ~82% fosil (Ember 2024) dan PLN menyebut ~20 GW permintaan [[isu-data-center]] di luar RUPTL 69,5 GW [diverifikasi-di-sesi].
   - Air: surplus air Batam hanya ~80 L/detik [diverifikasi-di-sesi].
   - Izin: DC di kawasan industri/KEK/KPBPB cukup RKL-RPL rinci yang disahkan pengelola kawasan, tanpa AMDAL sendiri dan tanpa konsultasi publik. Nomor pasalnya [belum-diverifikasi].
2. **Konflik sudah nyata, bukan potensi.**
   - [[batam]]: aksi warga Teluk Mata Ikan (Des 2024), KEK Nongsa (19 Sep 2026), dan gerbang Nongsa Digital Park (5 Okt 2026, ±300 warga Kavling Sambau) [diverifikasi-di-sesi].
   - [[jatiluhur-purwakarta]]: Gubernur Jabar menghentikan konstruksi BDx CGK4 karena belum ada AMDAL dan PBG [diverifikasi-di-sesi].
   - Tanggalnya 28 atau 30 Sep 2026, dan kapasitasnya 640 atau 120 MW. Keduanya [belum-diverifikasi] karena sumber berbeda.
3. **Kausalitas "data center mematikan air warga Batam" lemah.** Keyakinannya rendah–sedang: BP Batam menyalahkan El Niño (IPA Nongsa turun 90→25 L/detik), dan laporan "pipa khusus Duriangkang" dibantah. Bingkai yang aman: *"Air warga mati, air kawasan mengalir. Buka meternya."* Penolakan membuka data dijadikan bahan kampanye.
4. **Data resmi BP Batam sendiri sudah cukup tajam:** 10 DC pada 2032 butuh 32 juta L/hari (8,4% pasokan Batam), sama dengan estimasi WALHI [diverifikasi-di-sesi]. Kontrak listrik DC Batam (1.291 MVA) sudah melampaui beban puncak kota (780 MW) [diverifikasi-di-sesi].
5. **Celah hukum utama** (lihat [[amdal]], [[uu-cipta-kerja]]):
   - Permen LHK 4/2021 memperlakukan DC sebagai "multisektor" dengan ambang lahan ≥5 ha atau bangunan ≥10.000 m², tanpa ambang MW [diverifikasi-di-sesi].
   - Pemicu lain yang bisa dipakai: air sungai/danau ≥250 L/detik (BDx 384 L/detik), air tanah ≥50 L/detik, pembangkit ≥100 MW.
   - Perpres AI yang masih rancangan belum memuat pasal lingkungan, sehingga menjadi jendela advokasi termurah.
6. **[[isu-iklim-kota]] / emisi:** emisi Microsoft naik 25% dalam satu tahun (FY2025) karena DC AI. Akuntansi market-based bisa menyembunyikan emisi: Scope 2 DC Meta 2024 tercatat 135 t (pasar) vs 5,86 juta t (lokasi) [diverifikasi-di-sesi]. Tuntut Scope 2 berbasis lokasi dan CFE per jam.
7. **Iklim tropis boros air.** Data Microsoft FY25 untuk DC Jakarta: ~3,8 L air ditarik per kWh, tertinggi dari 29 lokasinya. Angka ini dihitung agen dari tabel Microsoft, fasilitasnya kecil, dan yang diukur adalah penarikan, bukan konsumsi. Kuat sebagai pertanyaan, lemah sebagai vonis [diverifikasi-di-sesi].
8. **Lapangan kerja sangat kecil.** DC hanya menghasilkan ~5–12 pekerjaan permanen per Rp1 T, dibanding rata-rata investasi nasional ~1.426 per Rp1 T (hitungan agen dari rasio 0,15–0,35 FTE/MW). Untuk Jatiluhur, janji 2.000–3.000 pekerja dibanding ~18–42 pekerja permanen [belum-diverifikasi: hitungan agen].
9. **Siapa yang membayar ([[pln]], APBN).** Subsidi + kompensasi listrik APBN 2026 sebesar Rp245,58 T, dengan tarif ditahan. Tanpa tarif DC yang terbuka dan skema take-or-pay, biaya pembangkit untuk DC bisa berpindah ke uang pajak [diverifikasi-di-sesi].
10. **Johor sebagai senjata argumen:** tarif air khusus DC RM5,33/m³ (1 Agu 2025), wajib air daur ulang, persetujuan Tier 1–2 dihentikan (Nov 2025), dan investasi tetap datang. Moratorium tanpa standar regional hanya memindahkan beban dari Singapura ke Johor lalu ke Batam ("kebocoran").
11. **Momen terdekat:** [[danantara]] akan mengumumkan investasi DC/AI (termasuk DC 1 GW) di New Asia Forum, Bali, 3–4 Des 2026. Doktrinnya "Bring Your Own Energy" untuk proyek >500 MW, yang tanpa syarat EBT bisa menjadi pintu PLTU/PLTG captive. Di samping itu, insentif pengganti tax holiday (dihentikan Kemenkeu 4 Nov 2026) sedang dirancang.
12. **Pola kesenjangan data adalah temuan advokasi tersendiri:** tidak ada register nasional DC, angka IDPRO berubah-ubah (456/520/630/650 MW), hyperscaler tidak mengungkap MW/air/listrik, dan kontrak PLN hanya menyebut MVA. Ini menyambung ke [[kedaulatan-data]] dan [[partisipasi-bermakna]].

## Keputusan & sikap
- **Ajukan syarat, bukan penolakan.** Pesan inti: *"Pusat data AI boleh dibangun, tapi tidak dengan air warga dan listrik batu bara. Syarat dulu, baru izin."* Moratorium nasional dinilai tidak realistis. Yang bisa dimenangkan adalah moratorium bersyarat lokal (Batam, DAS Citarum–Jatiluhur) ditambah standar nasional.
- **Empat tujuan antara (12–18 bulan):**
  - TA1: moratorium bersyarat;
  - TA2: keterbukaan wajib dan register nasional, lewat Perpres AI atau Permen Komdigi;
  - TA3: ambang AMDAL khusus DC (usulan ilustratif ≥20 MW, genset dihitung kumulatif, tenant kawasan wajib AMDAL sendiri);
  - TA4: EBT *additional*, tanpa captive fosil.
  - TA2, insentif bersyarat, dan "buka data" adalah kemenangan antara yang realistis. TA1 di Batam dan larangan penuh captive dipakai sebagai jangkar tawar.
- **Prioritas tiga langkah pertama untuk kapasitas satu orang:**
  - KIP gelombang 1 ke BP Batam, KLH, PLN, dan Pemkab Purwakarta;
  - surat terbuka "Tiga Syarat BYOE" ke Danantara sebelum New Asia Forum (EBT additional, tanpa captive fosil, buka risiko negara);
  - membentuk tim warga di Sambau.
- **Klaim yang dibuang dari materi WALHI:**
  - "satu prompt = sebotol air";
  - kaitan nikel Indonesia ke AI;
  - Rempang sebagai lokasi DC (hanya relevan sebagai pola tata kelola);
  - DC menggusur sawah Karawang;
  - bingkai anti-teknologi atau kiamat AI;
  - klaim satu-sumber cut-and-fill Teluk Mata Ikan.
- **Persona tokoh hanya sudut pandang, bukan juru bicara.** Semua agen dilarang mengarang kutipan. Bagian "self" dalam public narrative sengaja dikosongkan untuk diisi dari pengalaman pengkampanye sendiri.
- **Yang sengaja tidak dikerjakan dalam 90 hari:** nikel, pelabel data, deepfake, e-waste, dan litigasi berat. Gugatan PTUN baru diajukan *setelah* izin terbit atau konstruksi berjalan, dengan warga sebagai penggugat bersama (pelajaran PTUN Jakarta 2025 yang menolak legal standing WALHI).
- **SWRO diterima sebagai solusi parsial yang sah.** Yang dituntut adalah AMDAL brine, sumber energinya, dan dasar hukum tertulis.

## Koreksi penting
- **"Satu prompt ChatGPT = sebotol air"** [dikoreksi]: dengan angka energi per prompt terbaru dan parameter Indonesia, satu botol 500 mL setara kira-kira 400 prompt. Untuk skala, pakai angka kampus: DC 100 MW ≈ 2 juta L/hari (IEA).
- **Nikel → AI** [dikoreksi]: kajian IEA tentang mineral untuk DC menyebut tembaga, silikon, tanah jarang, dan galium, tetapi tidak menyebut nikel. Tidak ada pelacakan nikel Morowali/Halmahera ke DC mana pun. Narasi yang bisa dipertahankan hanya "ledakan AI menambah permintaan logam global yang di Indonesia diproduksi dengan PLTU captive".
- **Dugaan awal pengguna** bahwa masalah Indonesia ada di DC dinilai "sebagian besar tepat, tapi belum lengkap" [kata-pengguna]: intinya listrik fosil, air, dan perizinan tertutup, bukan DC per se.
- **PP 5/2021 sudah dicabut** oleh PP 28/2025, yang berlaku sejak 5 Juni 2025. Brief agen hukum masih merujuk PP 5/2021 [diverifikasi-di-sesi].
- **Angka yang harus diseragamkan sebelum publikasi:**
  - BDx 640/650 vs 120 MW;
  - tanggal penghentian 28 vs 30 Sep;
  - proyek Batam: 10 (BP Batam/Katadata) vs 16 (BP Batam per 29 Sep) vs 16–18 (WALHI);
  - "220.000 orang" memakai 150 L/orang/hari, sementara Katadata memakai 100 L;
  - pipeline nasional ±6–7 GW (keyakinan rendah).
- **Klaim dari pengetahuan umum agen strategi, bukan dari riset** [belum-diverifikasi]: biodata Gary Cook dan kasus Duke Energy, latar Marshall Ganz, komitmen *water positive* 2030 Microsoft, GTC NVIDIA biasanya Maret, Komisi XII DPR, tenggat KIP ±10+7 hari kerja, isu serikat PLN soal power wheeling.

## Belum selesai / langkah berikutnya
- [ ] Verifikasi butir hukum [CEK] bersama ICEL/LBH:
  - nomor pasal pengecualian tenant kawasan (PP 22/2021 Ps. 10, PP 28/2025 Ps. 102);
  - apakah Permen LHK 4/2021 sudah diganti;
  - tingkat risiko KBLI DC di PP 28/2025 dan kode KBLI 2025 (63101/63102);
  - status uji materi WALHI atas UU 6/2023 di MK dan HUM Perpres 112/2022 di MA;
  - apakah genset dihitung sebagai "pembangkit" untuk ambang 100 MW;
  - tenggat KIP.
- [ ] Seragamkan angka yang bertentangan (lihat Koreksi).
- [ ] Kirim KIP gelombang 1 (alokasi air per tenant dan meter jalur pipa ke kawasan; AMDAL kawasan Nongsa/Kabil; kontrak MVA dan REC PLN; KKPR/PBG BDx).
- [ ] Surat "Tiga Syarat BYOE", briefing jurnalis 1 Des, dan aksi di New Asia Forum 3–4 Des 2026.
- [ ] Pengaduan Komnas HAM (10 Des, hak atas air) dan Ombudsman (layanan air Sambau/Mata Ikan).
- [ ] "Buku Harian Air Nongsa" (8–12 minggu, bersama warga dan akademisi) dan rapor operator ala Clicking Clean lewat BHRRC.
- [ ] Masukan klausul pelaporan energi dan air ke rancangan Perpres AI dan Permen Komdigi standar pusat data. Kertas posisi insentif bersyarat dengan *clawback* bersama CELIOS ke BKF.
- [ ] Riset yang belum tergali karena kuota pencarian web habis: kualitas Citarum/Cikarang dan sumber air DC Cikarang, klaster Surabaya/Kendal, dampak AI pada pekerja BPO dan kreatif Indonesia, faktor emisi resmi sistem Batam, serapan kerja riil, Equinix/NTT, progres Indosat–NVIDIA Surakarta, status KEK Digital Bintan, beneficial owner EGSB/Altiva/Range IDC.
- [ ] Isi bagian "self" dalam public narrative dari pengalaman pengkampanye sendiri.

## Terkait
- [[isu-data-center]] · [[isu-air]] · [[isu-iklim-kota]] · [[isu-tata-ruang]] · [[isu-advokasi-kebijakan]]
- Konsep: [[ekstraktivisme-digital]] · [[kedaulatan-data]] · [[keadilan-lingkungan]] · [[ekologi-politik]] · [[solusi-palsu]] · [[partisipasi-bermakna]] · [[teori-perubahan]] · [[transisi-berkeadilan]] · [[privatisasi-layanan-dasar]] · [[kolonialisme-data]] · [[paradoks-jevons]] · [[additionality]] · [[moratorium-bersyarat]]
- Regulasi: [[amdal]] · [[uu-pplh]] · [[uu-cipta-kerja]] · [[uu-sumber-daya-air]] · [[pp-pste]] · [[kkpr]] · [[perpres-112-2022]] · [[pp-28-2025-perizinan-berbasis-risiko]] · [[permen-lhk-4-2021]] · [[perpres-ai]] · [[uu-kip]]
- Aktor: [[bp-batam]] · [[pln]] · [[danantara]] · [[kementerian-lh]] · [[kementerian-komdigi]] · [[kementerian-esdm]] · [[walhi]] · [[bdx-indonesia]] · [[dayone]] · [[idpro]] · [[nvidia]] · [[microsoft]] · trend-asia · celios · icel
- Tempat: [[batam]] · [[nongsa-sambau]] · [[kabil]] · [[jatiluhur-purwakarta]] · [[batang-kitb]] · [[bintan]] · [[bekasi-cikarang-karawang]] · [[singapura-johor]]

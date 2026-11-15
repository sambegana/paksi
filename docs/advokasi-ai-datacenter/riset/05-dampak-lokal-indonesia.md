# 05 — Dampak Ekologis & Sosial Lokal Data Center AI di Indonesia

*Agen riset persona: "Ahli lingkungan lapangan Indonesia". Status per 15 November 2026.*

## Pembuka persona

Saya membaca data center dari sisi daerah aliran sungai, waduk, dan gardu induk, tidak dari brosur investasi. Di lapangan pertanyaannya sederhana: dari waduk mana airnya, dari pembangkit apa listriknya, lahan siapa yang ditimbun, dan siapa yang antre jeriken saat musim kemarau. Untuk Indonesia, jawabannya untuk pertama kali sudah terlihat di **Batam (Sambau dan Teluk Mata Ikan, Nongsa)** dan **Jatiluhur (Purwakarta)**. Di dua tempat ini konflik air data center sudah jadi berita, aksi warga, dan intervensi pemerintah daerah. Di klaster lain (Bekasi–Karawang, Batang, Surabaya), dampaknya masih berupa risiko yang bisa dihitung, belum konflik yang terdokumentasi. Saya memisahkan dua kategori ini dengan tegas.

**Lima temuan kunci**
1. **Batam adalah titik paling rawan.** Sistem listriknya terisolasi (~930 MW pasokan, beban puncak ~780 MW per Oktober 2026), airnya 100% dari waduk tadah hujan, dan pipeline data center yang dipetakan BP Batam mencapai **1,47 GW IT**. ([Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/); [Accura](https://accura.co.id/knowledge/241))
2. **Konflik air sudah nyata.** Ada aksi warga Teluk Mata Ikan (Desember 2024), di KEK Nongsa (19 September 2026), dan di gerbang Nongsa Digital Park (5 Oktober 2026). BP Batam membantah data center sebagai penyebab, tetapi kemudian mewajibkan data center membangun SWRO (desalinasi) sendiri.
3. **Jatiluhur:** Gubernur Jabar menghentikan sementara konstruksi kampus AI BDx (640 MW) karena belum ada AMDAL dan PBG. Proyeksi kebutuhan airnya 384 L/detik, hampir sama dengan seluruh pemakaian historis PDAM Purwakarta dari waduk (~380 L/detik). ([Katadata](https://katadata.co.id/digital/teknologi/6ac1cc3fd9e4c/kdm-setop-proyek-data-center-bdx-di-jatiluhur-konsumsi-air-jadi-sorotan))
4. **Energi:** data center menambah beban pada grid yang masih ~82% fosil ([Ember](https://ember-energy.org/countries-and-regions/indonesia/)). RUPTL 2025–2034 menaruh 3,4 GW batu bara dan 9,3 GW gas di lima tahun pertama ([CREA](https://energyandcleanair.org/wp/wp-content/uploads/2025/09/CREA_EN-IDN-Briefing-Indonesias-RUPTL-2025-2034_-Fossils-first-renewables-later.pdf)), sementara PLN menyebut permintaan data center bisa mencapai **25.297 MW pada 2034** ([Jakarta Globe](https://jakartaglobe.id/tech/data-center-power-demand-to-reach-25297-mw-by-2034-pln-says)).
5. **Kaitan yang lemah:** kaitan dengan sawah Karawang, Rempang Eco City, dan nikel Morowali/Halmahera **belum** didukung bukti langsung. Jangan dijadikan klaim utama.

---

## 1. Klaster Batam / Kepulauan Riau

### Energi
- **Sistem terisolasi dan berbasis gas.** Per Oktober 2026, pasokan sekitar 930 MW, beban puncak sekitar 780 MW, cadangan "hampir 20%". Target pasokan 1.200–1.300 MW pada akhir 2027. Pertumbuhan beban lebih dari 15%/tahun, sementara nasional 3–4%. ([Batam Pos, 10/11/2026](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/)) BMI menegaskan grid Batam tidak bisa menarik daya dari sistem nasional saat pasokan ketat. ([TNGlobal/BMI, 26/10/2026](https://technode.global/2026/10/26/data-centers-to-strain-power-supply-across-four-asian-hubs-bmi/))
- **Bauran.** Pembangkit utamanya gas: PLTGU Tanjung Uncang 109 MW, PLTG Medco 70 MW, PLTMG sewa Maxpower hingga 150 MW. Ada juga **PLTU batu bara Tanjung Kasam 2×55 MW**. ([GoWest.id, 19/10/2026](https://gowest.id/kapasitas-listrik-batam-2026/)) Pada 2026 PLN Batam masih membuka tender batu bara untuk Tanjung Kasam ([PLN Batam](https://www.plnbatam.com/wp-content/uploads/2026/03/Pengumuman-Pengadaan-Batubara-Tj-Kasam-2026-Ext-3-2.pdf)). Persentase bauran terbaru tidak ditemukan. Data lama menyebut sekitar 70% gas dan 30% batu bara ([ESDM](https://www.esdm.go.id/id/media-center/arsip-berita/pln-batam-tidak-disubsidi-dan-tidaklagi-gunakan-solar)).
- **Kontrak data center melampaui beban puncak saat ini.** DayOne Kabil 511 MVA (April 2026), Altiva Nongsa 2×345 MVA (Juli 2026), NeutraDC-Nxera 90 MVA. ([Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/)) BMI memperkirakan data center bisa menjadi **lebih dari separuh konsumsi listrik Batam dan menyerap 89% tambahan pembangkitan**. Tambahan itu termasuk dua PLTG 300 MW. ([TNGlobal/BMI](https://technode.global/2026/10/26/data-centers-to-strain-power-supply-across-four-asian-hubs-bmi/))
- **Pembangkit baru = gas.** PLTGU Batam #1 120 MW di Kabil (target September 2028), PLTGU Batam 3 & 4 sekitar 300 MW. Gas Natuna mulai mengalir 27 Oktober 2026. ([Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/); [GoWest.id](https://gowest.id/kapasitas-listrik-batam-2026/))
- **Pembangkit sendiri.** Analisis industri menyebut banyak data center di Batam "mempertimbangkan pembangkit gas captive sebagai jembatan" ([Petroraya](https://www.petroraya.com/article/indonesias-data-center-boom-meets-an-energy-reality/)). Saya **tidak menemukan** data center yang terkonfirmasi sudah mengoperasikan pembangkit gas sendiri.
- **Ekspor listrik ke Singapura.** MoU 3,4 GW surya dan baterai sampai 2035 ([Tempo](https://www.tempo.co/ekonomi/indonesia-dan-singapura-teken-mou-ekspor-listrik-3-4-gw-hingga-2035-1685795)). Pada November 2026 rencana ini ditahan di tengah ketegangan soal kabut asap. Ekonom menilai alasan "kebutuhan domestik" lemah karena defisit Batam hanya sekitar 40 MW ([CNN Indonesia, 3/11/2026](https://www.cnnindonesia.com/ekonomi/20261103065142-85-1422552/bahlil-tahan-ekspor-energi-ke-singapura-untung-atau-buntung)). Pertanyaan advokasi yang relevan: **surya Kepri dibangun untuk siapa?** Untuk ekspor ke Singapura, untuk menutup permintaan data center, atau untuk warga? Saya tidak menemukan pernyataan WALHI Riau/Kepri soal ini.

### Air
- **Neraca sangat tipis.** Kebutuhan sekitar 3.700 L/detik, produksi rata-rata sekitar 4.500 L/detik dengan kehilangan 16%, surplus hanya **sekitar 80 L/detik** ([Batam Pos](https://metropolis.batampos.co.id/air-terjaga-investasi-berdaya/)). Masih ada **18 "stress area"** dengan layanan air kurang dari 8 jam/hari ([Batam Pos, 4/10/2026](https://metropolis.batampos.co.id/18-wilayah-batam-masih-jadi-stress-area-bp-batam-siapkan-rp122-t/)). Air tanah dilarang permanen. Duriangkang memasok sekitar 80% kebutuhan kota ([Katadata](https://katadata.co.id/data-center-batam/en)).
- **Sumber air data center diperdebatkan.** Wakil BP Batam menyatakan "Duriangkang tidak ada yang masuk ke data center" ([detik](https://www.detik.com/sumut/berita/d-8692975/warga-sambau-batam-sebut-air-mati-sejak-ada-data-center)). Sumber lain menyatakan sebaliknya: Terasbatam melaporkan pasokan ke data center "terus mengalir melalui jalur pemipaan khusus dari Waduk Duriangkang" ketika keran warga mati ([Terasbatam, 24/9/2026](https://www.terasbatam.id/bp-batam-wajibkan-data-center-punya-swro-mandiri/)), dan sumber industri kepada AFP mengatakan kawasan itu memakai air Duriangkang ([VnExpress/AFP](https://e.vnexpress.net/news/news/environment/ai-boom-sparks-water-shortages-and-protests-on-indonesian-island-5143684.html)).
- **Proyeksi resmi.** Menurut data BP Batam yang diolah Katadata, 10 data center pada 2032 butuh **32 juta liter/hari, sekitar 8,4% pasokan Batam**, setara kebutuhan 320.000 orang. NeutraDC-Nxera (56 MW) sendiri butuh hingga 3 juta L/hari. ([Katadata](https://katadata.co.id/data-center-batam/en)) Angka ini sama dengan estimasi WALHI ([WALHI via Indoleft](https://www.indoleft.org/statements/2026-10-01/data-centre-expansion-threatens-water-sources-moratorium-needed.html)).
- **Respons kebijakan.** BP Batam "mewajibkan" data center membangun SWRO, dengan target 750 L/detik dalam 2–3 tahun dan 1.000 L/detik selanjutnya ([Antara](https://www.antaranews.com/berita/5756745/bp-batam-pastikan-data-center-bangun-swro-mandiri-untuk-suplai-air); [Media Center Batam](https://mediacenter.batam.go.id/2026/09/25/jaga-air-waduk-untuk-masyarakat-batam-siapkan-solusi-kebutuhan-air-data-center-lewat-swro/)). Belum ada dasar hukum tertulis yang ditemukan. Beberapa media memakai kata "mendorong", bukan "mewajibkan". SWRO pun memindahkan beban: desalinasi menambah konsumsi listrik dan membuang brine ke pesisir.

### Lahan dan pesisir
- Batam punya sekitar 17.000 ha mangrove yang terus tergerus reklamasi dan arang ([Mongabay, 30/7/2025](https://mongabay.co.id/2025/07/30/benteng-pesisir-hutan-mangrove-batam-terus-tergerus/)). Di pesisir Kabil, reklamasi PT Blue Steel disegel DLHK Kepri pada Februari 2025 ([Mongabay](https://www.mongabay.co.id/2025/02/21/reklamasi-ilegal-di-batam-berlanjut-hutan-mangrove-tergerus/)). Kasus ini tidak terkait data center.
- **Teluk Mata Ikan, Nongsa.** Ada laporan cut-and-fill oleh PT Sri Indah Barelang di area berpapan "Hutan Lindung", dengan isu "puluhan hektare untuk data centre". Laporan yang sama menyebut tujuh kolam ikan patin warga tertimbun, dan BP Batam secara tertulis menyatakan tidak pernah menerbitkan izin kegiatan di lokasi itu ([Sumatera Daily, 21/9/2026](https://sumateradaily.com/2026/09/21/proyek-data-centre-siluman-pt-sri-indah-barelang-di-teluk-mata-ikan-nongsa-batam/)). Proyek EGS AI Data Center senilai US$5 miliar di lahan 30 ha juga berlokasi di Teluk Mata Ikan ([RMOL](https://rmol.id/politik/read/2026/10/14/724887/data-center-rp88-triliun-masuk-batam-iaw-ingatkan-pengalaman-rempang)). **Kaitan kedua hal ini belum terverifikasi**, karena hanya bersumber dari satu media lokal.
- **Rempang.** BP Batam membidik kawasan transmigrasi Barelang (Batam-Rempang-Galang) untuk data center ([Kontan](https://industri.kontan.co.id/news/barelang-dilirik-untuk-data-center-bp-batam-potensi-investasi-rp-500-triliun)). Indonesian Audit Watch memperingatkan agar tata kelola bermasalah Rempang tidak terulang ([RMOL](https://rmol.id/politik/read/2026/10/14/724887/data-center-rp88-triliun-masuk-batam-iaw-ingatkan-pengalaman-rempang)). **Belum ada bukti proyek data center di Pulau Rempang sendiri.** Kaitan yang tepat adalah soal pola tata kelola, bukan soal lokasi.
- **Kepri sebagai frontier PLTU captive.** CREA/GEM mencatat **4,75 GW PLTU captive diumumkan di Kepri**: Gallant Venture 2,25 GW dan Xinyi Group 2,5 GW. Keduanya untuk kawasan industri, **bukan** data center ([CREA/GEM, Jan 2026](https://energyandcleanair.org/wp/wp-content/uploads/2026/02/EN-CREA_GEM_Indonesia-captive-coal-in-2025_REV.pdf)).

### Sosial
- Yang terdampak adalah pelanggan air PDAM di dataran tinggi dan ujung jaringan (Sambau, Mata Ikan), nelayan dan pembudidaya ikan di Teluk Mata Ikan, serta usaha kecil. AFP melaporkan usaha es batu berhenti beroperasi dan air tangki pemerintah "berbau, kekuningan" ([VnExpress/AFP](https://e.vnexpress.net/news/news/environment/ai-boom-sparks-water-shortages-and-protests-on-indonesian-island-5143684.html)).
- **Lapangan kerja.** Saat ditetapkan, KEK Nongsa menargetkan 16.500 tenaga kerja ([GoKepri, 2022](https://gokepri.com/konsumsi-listrik-di-batam-haus-listrik-bisnis-pusat-data/)). Untuk investasi AI senilai Rp88 triliun, kementerian **tidak menyebut angka pekerjaan** ([Antara EN](https://en.antaranews.com/news/417132/ministry-prepares-workforce-for-batam-ai-data-center-investment)). Saya belum menemukan data serapan kerja riil.

---

## 2. Klaster Jabodetabek–Bekasi–Karawang–Purwakarta

- **Energi.** Sekitar 99% dari 159 pelanggan data center PLN (~1.990 MVA) berada di sistem Jawa-Madura-Bali ([Jakarta Globe](https://jakartaglobe.id/tech/data-center-power-demand-to-reach-25297-mw-by-2034-pln-says)). Faktor emisi Jamali yang dipakai dokumen pemerintah sekitar **0,87 tCO2/MWh** (combined margin 2019; [SRN KLHK](https://asset.srnmenlh.id/srn-menlhk/files/3ff4297a-0300-4efd-9572-9eca8eb4ba30.pdf)). Di Cikarang ada pemasok listrik swasta, Cikarang Listrindo: PLTGU 646 MW di Jababeka, dengan data center menyumbang sekitar 6% konsumsi pelanggan industrinya ([Listrindo, 2025](https://www.listrindo.com/uploads/investor_presentation/file__1745997966__b7b91c6cbcca7cd54c794febad4a2b0a.pdf)). Laporan DCD menyebut data center PDG di Cibitung dipasok dari PLTU Babelan (batu bara dengan co-firing biomassa). Halaman DCD tidak bisa saya akses langsung, jadi klaim ini perlu dicek ulang.
- **Air dan tanah.** Badan Geologi mencatat penurunan muka tanah 10–15 cm/tahun di beberapa kawasan industri Bekasi ([Antara, 2025](https://www.antaranews.com/berita/5232397/ai-yang-haus-krisis-air-di-balik-revolusi-digital?page=all)). Saya **tidak menemukan** data publik tentang sumber air (air tanah, PDAM, atau air permukaan) untuk data center tertentu di Cikarang dan Karawang. Data kualitas Citarum dan Cikarang juga belum saya dapatkan.
- **Jatiluhur (BDx CGK4).** Kampus AI 640 MW ini mendapat kontrak 788 MVA dari PLN ([PR Newswire](https://www.prnewswire.com/apac/news-releases/bdx-data-centers-secures-indonesias-largest-data-center-power-commitment-at-1-2-gw-strengthening-strategic-partnership-with-pln-across-national-ai-infrastructure-platform-302789946.html)). Groundbreaking dilakukan 22 September 2026, lalu konstruksi dihentikan 28 September 2026 karena AMDAL dan PBG belum terbit. Kebutuhan airnya 384 L/detik (~33.000 m³/hari), sementara alokasi PDAM Purwakarta 3.000 L/detik dengan pemakaian historis sekitar 380 L/detik ([Katadata](https://katadata.co.id/digital/teknologi/6ac1cc3fd9e4c/kdm-setop-proyek-data-center-bdx-di-jatiluhur-konsumsi-air-jadi-sorotan); [Antara](https://www.antaranews.com/berita/5769159/kdm-hentikan-pembangunan-data-center-ai-jatiluhur-akibat-tanpa-amdal)). WALHI menyetarakannya dengan kebutuhan air harian lebih dari 220.000 orang ([Betahita](https://www.betahita.id/berita/12456/pembangunan-data-center-ai-diminta-ditangguhkan)). Warga juga mengeluhkan kebisingan.
- **Lahan.** Sekitar 1.200 ha sawah Karawang beralih fungsi menjadi kawasan industri dan permukiman pada 2021–2026 ([Bernas](https://bernas.id/nasional/news/karawang-kunci-lumbung-padi-nasional-lewat-perlindungan-lp2b)). Permintaan lahan data center di Karawang sekitar 10 ha dan berada **di dalam kawasan industri yang sudah ada** ([Beritasela](https://beritasela.id/detail/596330/pacu-bisnis-data-center-ssia-targetkan-jual-10-hektare-lahan-karawang)). **Tidak ada bukti data center langsung menggusur sawah.**
- **BSD, Tangerang Selatan.** Unggahan viral (1 November 2026) menyoal kebisingan pendingin dan genset, emisi, air, serta banjir dari proyek data center di BSD. Pemkot hanya menjawab bahwa lokasinya "sesuai tata ruang" ([IDN Times, 13/11/2026](https://banten.idntimes.com/news/banten/viral-warga-khawatirkan-dampak-pembangunan-data-center-di-bsd-00-xwfcr-tfqn3m)).

## 3. Jawa Tengah (Batang/KITB), Kendal, Surabaya

- **KITB Batang.** Ada rencana pusat data AI 240 MW yang masih dikaji, dengan lahan sekitar 100 ha disiapkan ([Kompas](https://regional.kompas.com/read/2026/10/27/094234978/wagub-jateng-tegaskan-proyek-data-center-di-kitb-masih-tahap-kajian); [Republika](https://rejogja.republika.co.id/berita/tniiiq487/sedang-dikembangkan-pusat-data-ai-di-batang-berkapasitas-240-megawatt)). Pemprov mengakui proyek ini butuh "pasokan air cukup melimpah". Klaim di media sosial soal proyek 1 GW belum terverifikasi.
- **Kendal dan Surabaya:** saya tidak menemukan sumber dampak lokal (kuota pencarian habis; lihat bagian metode).

## 4. Kerangka nasional

- **RUPTL 2025–2034.** Rencana ini menambah 69,5 GW: 6,3 GW batu bara, 10,3 GW gas, 42,1 GW EBT, dan 10,3 GW penyimpanan. Lima tahun pertama didominasi fosil (3,4 GW batu bara dan 9,3 GW gas dari 27,9 GW), dan masih ada 2,8 GW PLTU yang masuk pada 2030–2033 ([CREA](https://energyandcleanair.org/wp/wp-content/uploads/2025/09/CREA_EN-IDN-Briefing-Indonesias-RUPTL-2025-2034_-Fossils-first-renewables-later.pdf)). Proyeksi data center di dalam RUPTL sekitar 5.226 MW pada 2034 ([Sirkularium](https://sirkularium.com/en/insight/data-centre-electricity-demand-ruptl-2034)). Namun PLN kini menyebut potensi 13 GW (3.535 MW di antaranya Prioritas 1) ([Ecobiz](https://ecobiz.asia/pln-records-potential-13-gw-data-center-power-demand/)) dan sekitar 20 GW **di luar** 69,5 GW RUPTL ([Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/)). **Artinya, permintaan data center belum sepenuhnya masuk dalam rencana pembangkitan.** Risikonya, tambahan permintaan ini akan ditutup dengan gas dan batu bara yang paling cepat dibangun.
- **Perpres 112/2022.** Moratorium PLTU baru dalam perpres ini mengecualikan PLTU captive untuk industri hilirisasi dan PSN. Pipeline PLTU captive sudah lebih dari 31 GW ([CREA/GEM](https://energyandcleanair.org/wp/wp-content/uploads/2026/02/EN-CREA_GEM_Indonesia-captive-coal-in-2025_REV.pdf)). Data center **saat ini** belum tercatat memakai PLTU captive.
- **REC dan "green as a service".** PLN menyiapkan sekitar 10.000 GWh REC dan skema *dedicated source* (contohnya Microsoft) ([Ecobiz](https://ecobiz.asia/pln-records-potential-13-gw-data-center-power-demand/)). Pelanggan REC naik 117% menjadi 7.354 pada 2024 ([Konstruksi Media](https://konstruksimedia.com/pengguna-renewable-energy-certificate-naik-117-didominasi-sektor-industri-dan-bisnis/)). T-REC per jam baru direncanakan pada 2028 ([Ecobiz](https://ecobiz.asia/pln-develops-time-based-renewable-energy-certificates-to-track-hourly-green-power-use/)). REC tahunan tidak mengubah fakta fisik bahwa elektron yang dipakai di malam hari berasal dari grid fosil.
- **Pembanding Johor.** Johor memberlakukan tarif air khusus data center RM5,33/m³ (1 Agustus 2025), meminta data center berpendingin air menunda tambahan pasokan sekitar 18 bulan, dan mewajibkan air daur ulang ([ArusGrid](https://arusgrid.com/policy/malaysia)). Johor juga berhenti menyetujui data center Tier 1–2 ([Lowyat, 28/11/2025](https://www.lowyat.net/2025/374704/johor-data-centre-approvals/)) dan menolak sekitar 30% aplikasi pada 2024 ([Malay Mail](https://www.malaymail.com/news/malaysia/2024/11/20/official-johor-snubbed-30pc-of-data-centre-bids-for-not-meeting-sustainability-goals/157396)). Indonesia belum punya instrumen setara. Per 8 Oktober 2026 tidak ada moratorium yang berlaku ([Indonesia Business Post](https://indonesiabusinesspost.com/7535/environment/data-center-expansion-sparks-water-crisis-concerns-in-indonesia-as-government-seeks-solutions)).

## 5. Rantai pasok: nikel dan tembaga (penilaian jujur)

Smelter nikel IMIP (3.360 MW PLTU captive) dan IWIP (4.540 MW) adalah pusat PLTU captive terbesar di Indonesia ([CREA/GEM](https://energyandcleanair.org/wp/wp-content/uploads/2026/02/EN-CREA_GEM_Indonesia-captive-coal-in-2025_REV.pdf)). Data center memang memakai tembaga (kabel, busbar, trafo), baja tahan karat, dan baterai (UPS/BESS). Tetapi **saya tidak menemukan satu pun sumber** yang melacak nikel Morowali/Halmahera atau tembaga Grasberg sampai ke data center tertentu, baik di Indonesia maupun di luar negeri.
**Kekuatan kaitan: lemah atau tidak langsung.** Narasi yang bisa dipertanggungjawabkan adalah bahwa "ledakan AI menambah permintaan logam global yang di Indonesia diproduksi dengan PLTU captive". Klaim seperti "server Batam memakai nikel Morowali" tidak bisa dipertanggungjawabkan.

---

## 6. Hitungan ilustratif (bisa diverifikasi)

**Asumsi** (bukan data; diganti bila ada angka resmi):
- Faktor utilisasi rata-rata 80% untuk skenario A dan 70% untuk skenario B. PUE 1,3.
- Konsumsi energi sistem Batam saat ini ≈ beban puncak 780 MW × 8.760 jam × load factor 0,75 ≈ **5.125 GWh/tahun**. Load factor 0,75 adalah asumsi saya.
- Faktor emisi Batam 0,50 tCO2/MWh (asumsi untuk grid dominan gas dengan sedikit PLTU), dibandingkan dengan rata-rata nasional 0,68 ([Ember via OWID](https://sustainabilityreference.com/emission-factors/electricity/id)).
- Intensitas air: (i) rasio BP Batam, yaitu 285 MW IT butuh 29 juta L/hari, sehingga **≈102 m³/MW-IT/hari** ([Katadata](https://katadata.co.id/data-center-batam/en)); (ii) Mytton, 25,5 juta L/MW/tahun ≈ 70 m³/MW/hari (dikutip [Katadata](https://katadata.co.id/data-center-batam/en)).
- Kebutuhan domestik dihitung 100 L/orang/hari (standar yang dipakai Katadata) × 1,3 juta jiwa ≈ 130.000 m³/hari ≈ 47,5 juta m³/tahun.

| Skenario Batam | Listrik (GWh/thn) | vs sistem Batam saat ini | CO2 (Mt/thn, EF 0,50–0,68) | Air (juta m³/thn) | Air (L/detik) | vs kebutuhan domestik 1,3 juta jiwa |
|---|---|---|---|---|---|---|
| **A**: 605 MW (proyeksi PLN 2034 untuk data center Batam, [BMI](https://technode.global/2026/10/26/data-centers-to-strain-power-supply-across-four-asian-hubs-bmi/)) ≈ 465 MW IT | 605×8.760×0,8 ≈ **4.240** | ≈ 83% | 2,1–2,9 | 11,9–17,3 | 376–548 | 25–36% |
| **B**: 1.470 MW IT (pipeline BP Batam) × PUE 1,3 | 1.911×8.760×0,7 ≈ **11.720** | ≈ 2,3× | 5,9–8,0 | 37,5–54,6 | 1.189–1.731 | 79–115% |

Cara membaca: surplus air Batam saat ini hanya sekitar 80 L/detik. Skenario A saja sudah 5–7 kali lipat surplus itu. Target SWRO 1.000 L/detik, dengan rasio BP Batam, hanya cukup untuk sekitar **850 MW IT**, sehingga skenario B melampaui rencana SWRO. Pengecualiannya adalah jika data center beralih ke pendingin udara atau sirkuit tertutup, yang menurunkan air tetapi menaikkan listrik.

**Jatiluhur:** 384 L/detik × 86.400 = 33.178 m³/hari = **12,1 juta m³/tahun**, kira-kira setara seluruh pemakaian historis PDAM Purwakarta dari waduk (380 L/detik).
**Nasional:** 5.226 MW × 8.760 × 0,8 ≈ **36,6 TWh/tahun** pada 2034. Dengan EF 0,68, emisinya ≈ **24,9 MtCO2/tahun**. Ini baru angka RUPTL; dengan angka PLN 20–25 GW, hasilnya bisa 4–5 kali lipat.

## 7. Tabel data untuk grafik

| Seri | Nilai | Sumber |
|---|---|---|
| Batam: beban puncak Okt 2026 / pasokan | 780 / 930 MW | [Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/) |
| Batam: proyeksi beban puncak 2026 → 2035 | 841 → 2.540 MW | [Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/) |
| Batam: kontrak data center (DayOne, Altiva, Nxera) | 511 + 690 + 90 = 1.291 MVA | [Batam Pos](https://news.batampos.co.id/menjaga-daya-di-tengah-ledakan-digital/) |
| Batam: pipeline data center (BP Batam / BMI) | 1.470 MW IT / 70 MW live + 747 MW | [Accura](https://accura.co.id/knowledge/241); [BMI](https://technode.global/2026/10/26/data-centers-to-strain-power-supply-across-four-asian-hubs-bmi/) |
| Batam: air baku per waduk (L/detik) | Duriangkang 3.000; Tembesi 700; Muka Kuning 310; Sei Ladi 240; Sei Harapan 210; Nongsa 60 (kini 25) | [Batam Pos](https://metropolis.batampos.co.id/18-wilayah-batam-masih-jadi-stress-area-bp-batam-siapkan-rp122-t/) |
| Batam: kebutuhan / produksi / surplus air | 3.700 / 4.500 / 80 L/detik | [Batam Pos](https://metropolis.batampos.co.id/air-terjaga-investasi-berdaya/) |
| Data center Batam 2032 (10 unit) | 32 juta L/hari = 8,4% pasokan | [Katadata](https://katadata.co.id/data-center-batam/en) |
| Nasional: proyeksi permintaan data center | 1.098 MW (2025) → 2.122 (2026) → 5.226 (2034, RUPTL); 25.297 MW (PLN 2026) | [Sirkularium](https://sirkularium.com/en/insight/data-centre-electricity-demand-ruptl-2034); [Jakarta Globe](https://jakartaglobe.id/tech/data-center-power-demand-to-reach-25297-mw-by-2034-pln-says) |
| RUPTL 2025–2029 tambahan kapasitas | Batu bara 3,4; gas 9,3; EBT 12,2; storage 3,0 GW | [CREA](https://energyandcleanair.org/wp/wp-content/uploads/2025/09/CREA_EN-IDN-Briefing-Indonesias-RUPTL-2025-2034_-Fossils-first-renewables-later.pdf) |
| Bauran listrik nasional 2024 | Fosil 82%, bersih 18% (surya+angin 0,5%) | [Ember](https://ember-energy.org/countries-and-regions/indonesia/) |
| PLTU captive: batu bara captive vs on-grid 2025 | ≈58% dari 233 TWh on-grid | [Ember](https://ember-energy.org/latest-insights/indonesias-captive-coal-giant-better-data-to-shape-industrial-competitiveness/) |
| Jatiluhur: BDx vs PDAM Purwakarta | 384 vs ~380 L/detik (alokasi 3.000) | [Katadata](https://katadata.co.id/digital/teknologi/6ac1cc3fd9e4c/kdm-setop-proyek-data-center-bdx-di-jatiluhur-konsumsi-air-jadi-sorotan) |

## 8. Cerita lapangan (nyata, bersumber)

1. **Sambau, Nongsa: "Air mati sejak ada data center."** Pada 5 Oktober 2026, sekitar 300 warga RT 03 RW 02 Kavling Sambau berunjuk rasa di depan Nongsa Digital Park sambil membawa galon kosong. Ketua RT Andi Lalang bercerita air mati total selama tiga bulan setelah enam bulan menyala-mati. Ia jujur soal batas klaimnya: "Ada kemungkinan besar. Saya tidak pernah mengatakan 100 persen." BP Batam menyalahkan El Niño, karena produksi IPA Nongsa turun dari 90 ke 25 L/detik. ([detik](https://www.detik.com/sumut/berita/d-8692975/warga-sambau-batam-sebut-air-mati-sejak-ada-data-center); [BatamNow](https://batamnow.com/bp-batam-sebut-data-center-tak-disuplai-waduk-nongsa-dan-duriangkang/)) Dua minggu sebelumnya, 19 September 2026, ratusan warga mendatangi KEK Nongsa ketika air ke rumah berhenti sementara pipa khusus data center tetap mengalir ([Terasbatam](https://www.terasbatam.id/bp-batam-wajibkan-data-center-punya-swro-mandiri/)). Respons HR Director NDP: "Penyediaan air untuk masyarakat warga itu kan bukan di kami."
2. **Mata Ikan: mandi air laut.** Kepada AFP, Rahmat (52) bercerita warga memakai air laut untuk cebok. Sulastri (38) menyebut krisis sudah sekitar setahun dan memburuk enam bulan terakhir, air tangki "berbau, kekuningan", dan usaha es batu berhenti ([VnExpress/AFP, 12/11/2026](https://e.vnexpress.net/news/news/environment/ai-boom-sparks-water-shortages-and-protests-on-indonesian-island-5143684.html)). Muhammad Iwan (40), warga Teluk Mata Ikan, mengingat aksi Desember 2024 di depan fasilitas data center KEK Nongsa: air ke kawasan industri tetap mengalir, sementara rumah warga kering ([Katadata](https://katadata.co.id/data-center-batam/en)).
3. **Jatiluhur: gubernur menghentikan proyek.** Enam hari setelah ikut meresmikan groundbreaking, Gubernur Dedi Mulyadi sidak ke lokasi dan menghentikan konstruksi BDx karena AMDAL dan PBG belum ada. Pernyataannya: "warga Purwakarta yang berkorban untuk kepentingan Jatiluhur harus mendapat akses air. Tidak boleh terganggu." ([Katadata](https://katadata.co.id/digital/teknologi/6ac1cc3fd9e4c/kdm-setop-proyek-data-center-bdx-di-jatiluhur-konsumsi-air-jadi-sorotan)) Asosiasi industri IDPRO lalu menyatakan khawatir soal iklim investasi ([Katadata](https://katadata.co.id/digital/teknologi/6ac49fb70d5e3/proyek-data-center-bdx-di-jatiluhur-disetop-idpro-waswas-soal-minat-investor)).

## 9. Node mind-map hierarkis

```
Dampak lokal data center AI Indonesia
├── Energi
│   ├── Grid fosil: nasional 82% fosil; Jamali ~0,87 tCO2/MWh
│   ├── RUPTL: 3,4 GW batu bara + 9,3 GW gas (2025–29); data center 5,2 GW vs klaim PLN 20–25 GW
│   ├── Batam: grid terisolasi 930 MW; kontrak data center >1,2 GVA; PLTGU baru; PLTU Tj. Kasam
│   ├── Perpres 112/2022: celah PLTU captive (31 GW pipeline; Kepri 4,75 GW diumumkan, belum terkait data center)
│   ├── REC / green-as-a-service: klaim tahunan, belum per jam (T-REC 2028)
│   └── Ekspor surya 3,4 GW ke Singapura: untuk siapa? (ditahan Nov 2026)
├── Air
│   ├── Batam: waduk tadah hujan, surplus ~80 L/detik, 18 stress area
│   │   ├── Konflik Sambau / Mata Ikan (2024, Sep–Okt 2026)
│   │   ├── Sengketa: pipa khusus Duriangkang vs bantahan BP Batam
│   │   └── Kebijakan SWRO 750–1.000 L/detik (dasar hukum belum jelas; brine + listrik)
│   ├── Jatiluhur: BDx 384 L/detik ≈ seluruh pemakaian PDAM Purwakarta
│   ├── Bekasi: subsiden 10–15 cm/thn (sumber air data center belum terbuka)
│   └── Pembanding Johor: tarif RM5,33/m³, jeda pendingin air, wajib air daur ulang
├── Lahan & ruang
│   ├── Mangrove Batam ~17.000 ha tergerus (bukan oleh data center)
│   ├── Teluk Mata Ikan: dugaan cut-and-fill hutan lindung (belum terverifikasi)
│   ├── Barelang/Rempang: pola tata kelola, bukan bukti lokasi
│   └── Karawang: alih fungsi sawah 1.200 ha (data center di kawasan industri)
├── Sosial
│   ├── Pelanggan air ujung jaringan, pembudidaya ikan, usaha es
│   ├── Kebisingan (Jatiluhur, BSD)
│   └── Lapangan kerja: janji tanpa angka
└── Rantai pasok: nikel/tembaga (kaitan lemah, tidak langsung)
```

## 10. Tingkat keyakinan & kritik jujur

| Klaim | Keyakinan | Catatan |
|---|---|---|
| Ada krisis air di Nongsa dan ada protes warga yang menyasar data center | **Tinggi** | Banyak media independen (detik, AFP, Batam Pos, Mongabay) |
| Data center *menyebabkan* air mati di Sambau | **Rendah–sedang** | Kekeringan nyata (Nongsa 90→25 L/detik). Bukti kausal belum ada. Laporan "pipa khusus Duriangkang" penting tetapi dibantah. Tuntut transparansi meter air, jangan klaim kausalitas. |
| Data center akan menekan neraca air Batam secara signifikan | **Tinggi** | Proyeksi resmi BP Batam 8,4% pasokan; surplus hanya ~80 L/detik |
| Data center mendorong pembangkit gas baru di Batam | **Tinggi** | Dokumen PLN Batam dan BMI |
| Data center memicu PLTU baru | **Rendah–sedang** | Belum ada PLTU yang secara eksplisit dibangun untuk data center. Risikonya sistemik (RUPTL, grid Jamali). |
| Data center menggusur sawah Karawang | **Rendah** | Data center berlokasi di kawasan industri yang sudah ada |
| Kaitan dengan Rempang | **Rendah (lokasi) / sedang (pola tata kelola)** | Hanya rencana Barelang dan peringatan IAW |
| Kaitan nikel/tembaga | **Lemah** | Tidak ada pelacakan rantai pasok |
| Hitungan ilustratif | **Sedang** | Sensitif terhadap PUE, utilisasi, dan teknologi pendingin. Kategori pipeline BP Batam (IT vs MVA) tidak jelas. |

**Kritik terhadap posisi advokasi sendiri:** (1) Angka 16–18 proyek dari WALHI berbeda dengan "10 rencana" versi BP Batam, jadi samakan definisinya dulu. (2) SWRO adalah solusi parsial yang sah. Kritik yang tepat menyasar penegakannya, energinya, dan brine, bukan menolak SWRO sebagai konsep. (3) Data center berpendingin udara memakai sedikit air tetapi lebih banyak listrik. Advokasi harus menuntut keduanya sekaligus (WUE dan PUE yang diaudit dan dipublikasikan), bukan hanya air.

**Metode & keterbatasan:** Riset ini memakai pencarian web (Bahasa Indonesia dan Inggris) dan pengambilan langsung halaman sumber per 15 November 2026. Kuota pencarian web bersama habis di tengah riset. Akibatnya beberapa topik **belum tergali**: kualitas Citarum dan Cikarang, sumber air data center Cikarang, klaster Surabaya dan Kendal, pernyataan WALHI Kepri/Riau soal ekspor listrik, faktor emisi resmi sistem Batam, serta data serapan tenaga kerja riil. Beberapa halaman (Kompas.id, walhi.or.id, DCD, jabarprov.go.id) tidak bisa diakses langsung, sehingga isinya diverifikasi lewat liputan media lain.

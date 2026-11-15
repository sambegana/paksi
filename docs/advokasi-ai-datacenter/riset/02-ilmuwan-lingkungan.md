# 02 — Ilmuwan Lingkungan: Mengukur Jejak AI dan Data Center

*Agen riset ber-persona, untuk kampanye WALHI soal AI dan data center. Per 15 November 2026.*

## Pembuka persona

Saya mengambil sudut pandang ilmuwan yang mengukur, bukan yang menebak. Saya memakai empat lensa analitis, karena masing-masing menutup titik buta yang lain:

- **Sasha Luccioni (Hugging Face).** Ia mengukur energi per model dan per jenis tugas (AI Energy Score). Lensanya mengingatkan bahwa "AI" bukan satu benda. Jejaknya bergantung pada jenis tugas, ukuran model, dan mode *reasoning*.
- **Shaolei Ren (UC Riverside).** Ia memecah air menjadi air *on-site* (pendinginan) dan *off-site* (pembangkit listrik). Lensanya paling relevan untuk iklim tropis.
- **Alex de Vries-Gao (Digiconomist).** Ia mengkritik keterbukaan perusahaan dan mengestimasi dari rantai pasok chip. Lensanya berguna untuk membongkar angka "per-prompt" yang dipilih perusahaan.
- **Tim IEA "Energy and AI".** Mereka memberi gambaran tingkat sistem: berapa TWh, dari pembangkit apa, dan di mana.

Prinsip saya: setiap angka memakai tahun dan sumber. Saya tidak memakai kutipan langsung kecuali dari sumber yang sudah saya baca, dan klaim yang lemah saya tandai sebagai lemah.

---

## 1. Listrik

**Global.** Laporan IEA *Key Questions on Energy and AI* (2026) memuat beberapa angka kunci ([PDF IEA 2026](https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf), [ringkasan](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary)):

- Konsumsi listrik data center naik 17% pada 2025 menjadi **485 TWh**.
- Konsumsi data center yang berfokus AI naik **50%** pada tahun yang sama.
- Proyeksinya hampir dua kali lipat menjadi **~945–950 TWh pada 2030**, atau sekitar 3% listrik dunia.
- Data center berfokus AI tumbuh "lebih dari tiga kali lipat" menjadi **~465 TWh pada 2030**. Artinya pada 2025 kelompok ini sekitar 150 TWh (ini angka turunan saya).
- Laporan IEA 2025 sebelumnya mencatat ~415 TWh untuk 2024, sekitar 1,5% listrik dunia ([IEA 2025](https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf)).

**Tabel 1. Konsumsi listrik data center (TWh), IEA 2026, Tabel A.1/A.4** (siap dijadikan grafik)

| Wilayah / skenario | 2023 | 2024 | 2025 | 2030 | 2035* |
|---|---|---|---|---|---|
| Dunia (Base Case) | 360 | 416 | 485 | 945 | 1.193 |
| Amerika Serikat | 154 | 183 | 224 | 426 | – |
| China | 84 | 102 | 117 | 277 | – |
| Eropa | 66 | 68 | 72 | 114 | – |
| Asia Pasifik (termasuk China) | 128 | 150 | 173 | 378 | – |
| Dunia – *Lift-Off* | | | | 1.008 | 1.637 |
| Dunia – *High Efficiency* | | | | 868 | 1.013 |
| Dunia – *Headwinds* | | | | 833 | 942 |

*IEA menyebut angka 2035 sebagai skenario eksploratif.*

**Amerika Serikat.** Laporan LBNL Desember 2024 mencatat 176 TWh pada 2023, atau 4,4% listrik AS. Proyeksinya **325–580 TWh pada 2028**, atau 6,7–12% ([LBNL](https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/)).

**Titik panas.** Dampak sesungguhnya terasa di tingkat lokal:

- **Irlandia:** data center memakai **21,8% listrik bermeteran** pada 2024 (6.969 GWh), naik dari 5% pada 2015 ([CSO](https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2024/keyfindings)).
- **Virginia:** **~25,6%** listrik negara bagian pada 2023 ([EPRI 2024](https://restservice.epri.com/publicdownload/000000003002028905/0/Product)).
- **Singapura:** ~6,5 TWh pada 2024, sedikit di atas sepersepuluh konsumsi nasional, naik dari ~7% pada 2020 ([Eco-Business](https://www.eco-business.com/news/singapore-sets-southeast-asias-first-binding-data-centre-rules-building-demand-for-clean-energy/)).
- **Johor:** menurut data negara bagian, 15 data center yang sudah jadi berkapasitas 1,7 GW, dengan komitmen ~5,1 GW pada 2030 ([w.media](https://w.media/special-report-how-johor-deals-with-thirsty-data-centers/)).
- **Asia Tenggara:** IEA mencatat lebih dari 6 GW proyek diusulkan, dengan Malaysia sebagai motor utama. Pipeline Indonesia juga "signifikan", tetapi banyak proyeknya masih tahap awal ([IEA 2026](https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf)).

**Energi per query: angka resmi dan kritiknya.**

- **Google (Agustus 2025):** median prompt teks Gemini Apps memakai **0,24 Wh**, 0,03 gCO₂e, dan 0,26 mL air. Angka ini turun 33 kali (energi) dan 44 kali (karbon) dalam 12 bulan ([Laporan Lingkungan Google 2026](https://sustainability.google/files/google-2026-environmental-report.pdf)).
- **Sam Altman (Juni 2025):** rata-rata query ChatGPT memakai **0,34 Wh** dan 0,000085 galon air, tanpa penjelasan metodologi ([blog Altman](https://blog.samaltman.com/the-gentle-singularity); [ringkasan](https://simonwillison.net/2025/Jun/10/sam-altman/)).
- **Kritik de Vries-Gao dan Ren** ([Neowin](https://www.neowin.net/news/experts-accuse-google-of-downplaying-ai-water-use-with-5-drops-per-prompt-claim/)):
  - Google memakai **median**, bukan rata-rata.
  - Angka karbonnya **berbasis pasar (market-based)**. Dengan metode berbasis lokasi (location-based), angkanya sekitar 0,09 g, tiga kali lipat.
  - Angka air hanya menghitung air *on-site*, tanpa air pembangkit.
  - Definisi "prompt median" tidak dijelaskan.
- **Variasi antarmodel sangat besar.** AI Energy Score v2 (Desember 2025) menemukan model *reasoning* rata-rata memakai **~30 kali** energi model biasa. Untuk model yang sama, menyalakan mode *reasoning* menaikkan energi **150–700 kali** ([Hugging Face](https://huggingface.co/blog/sasha/ai-energy-score-v2)). Riset Luccioni dkk. (FAccT 2024) menunjukkan model generatif serbaguna "lebih mahal beberapa orde besaran" dibanding model khusus tugas ([arXiv](https://arxiv.org/abs/2311.16863)).
- **Pelatihan vs pemakaian.** Mistral merilis analisis siklus hidup (LCA) untuk Large 2 (Juli 2025) ([Mistral](https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai)):
  - Total jejak setelah 18 bulan: **20,4 ktCO₂e** dan **281.000 m³ air**.
  - Per respons 400 token: 1,14 gCO₂e dan 45 mL air.
  - Pelatihan menyumbang porsi terbesar emisi pada model ini.

## 2. Emisi

**Tabel 2. Emisi perusahaan (juta tCO₂e) dan listrik (TWh), dari laporan perusahaan** (siap dijadikan grafik)

| Tahun | Google, total (*ambition-based*) | Google, Scope 2 lokasi | Google, Scope 2 pasar | Microsoft, total (pasar), FY | Microsoft, Scope 2 lokasi | Microsoft, Scope 2 pasar | Amazon, total | Meta, total lokasi | Meta, total pasar |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 8,00 | 5,17 | 0,79 | – | – | – | 51,17 | – | – |
| 2020 | 7,15 | 5,85 | 0,92 | 13,06 | 4,33 | 0,46 | 60,64 | 8,56 | 5,13 |
| 2021 | 8,46 | 6,50 | 1,77 | 14,91 | 5,01 | 0,43 | 71,54 | 10,16 | 5,83 |
| 2022 | 9,56 | 7,96 | 2,43 | 17,17 | 6,38 | 0,29 | 65,37 | 14,01 | 8,53 |
| 2023 | 10,91 | 9,09 | 3,29 | 17,66 | 8,08 | 0,39 | 65,28 | 14,07 | 7,50 |
| 2024 | 12,23 | 11,07 | 2,90 | 16,69 | 9,96 | 0,26 | 69,55 | 15,63 | 8,20 |
| 2025 | **14,47** | **15,15** | 2,82 | **21,12** | **12,03** | **2,71** | **80,85** | (belum) | (belum) |
| Listrik 2025 | 43,5 TWh | | | 37,0 TWh (FY25) | | | – | 18,1 TWh untuk DC (2024) | |

Sumber: [Google 2026](https://sustainability.google/files/google-2026-environmental-report.pdf); [Microsoft Data Fact Sheet 2026](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf); [Amazon 2025](https://sustainability.aboutamazon.com/2025-amazon-sustainability-report.pdf); [Meta Environmental Data Index 2025](https://sustainability.atmeta.com/wp-content/uploads/2025/10/Meta_2025-Environmental-Data-Index.pdf). Amazon tidak menerbitkan angka berbasis lokasi.

**Bacaan tabel:**

- **Google.** Total emisi naik **+81%** dibanding 2019. Scope 2 berbasis lokasi naik hampir tiga kali lipat (+193%). Konsumsi listrik naik 37% pada 2025 saja.
- **Microsoft.** Emisi naik **+62%** dibanding FY20 menurut tabel 1A. Dengan kriteria manajemen (tabel 1B), naiknya +58%. Listrik naik 3,4 kali lipat.
- **Amazon.** Emisi naik **+58%** dibanding 2019. Pada 2025 total naik 16% dan Scope 2 naik 34%.

**Akuntansi market-based vs location-based.**

- Metode *market-based* mengurangi emisi dengan sertifikat energi terbarukan (REC/EAC), walaupun listrik fisiknya berasal dari jaringan yang sama.
- Contoh paling telanjang: Scope 2 data center Meta tahun 2024 tercatat **135 tCO₂e** dengan metode pasar, tetapi **5.862.614 tCO₂e** dengan metode lokasi. Bedanya sekitar 43.000 kali ([Meta EDI 2025](https://sustainability.atmeta.com/wp-content/uploads/2025/10/Meta_2025-Environmental-Data-Index.pdf)).
- Microsoft berhenti membeli REC "unbundled" yang tidak additional pada Februari 2025. Akibatnya Scope 2 berbasis pasarnya melonjak sekitar 10 kali, dari 0,26 menjadi 2,71 Mt. Menurut ESG Today, Microsoft menyatakan: "While this decision increases our reported emissions in the near term, it enables us to increase the development of new CFE rather than relying on certificates alone" ([ESG Today](https://www.esgtoday.com/microsofts-carbon-footprint-jumps-25-as-ai-buildout-challenges-climate-goals/)). Lonjakan ini menunjukkan seberapa banyak emisi yang selama ini "disembunyikan" oleh sertifikat.
- Analisis The Guardian (September 2024) memperkirakan emisi data center milik Google, Microsoft, Meta, dan Apple pada 2020–2022 sekitar **7,62 kali** lebih tinggi dari yang dilaporkan ([ringkasan Impakter](https://impakter.com/apple-google-meta-and-microsofts-data-centre-emissions-may-be-7-62-times-higher-than-reported/); artikel aslinya tidak berhasil saya akses).

**Pembangkit fosil baru.**

- IEA memperkirakan **gas dan batu bara memasok lebih dari 40%** tambahan permintaan listrik data center sampai 2030 ([IEA 2025](https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf)). Pada 2030 batu bara masih menyumbang **~20%** pasokan listrik data center global, terutama di China ([IEA 2026](https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf)).
- Pembangkit gas *on-site* (dibangun di lokasi data center) diperkirakan mencapai **15–27 GW pada 2030**. Saat ini 5,6 GW sedang dibangun dan lebih dari 70 GW dalam tahap pengembangan (IEA 2026).
- Agar andal, pembangkit gas on-site harus dibangun **30–70% lebih besar** dari beban yang dilayani.
- Regulator Louisiana menyetujui ~2,3 GW pembangkit gas Entergy untuk data center Meta "Hyperion" (Agustus 2025). Pada April 2026 regulator mempercepat proses tujuh pembangkit tambahan ([E&E News](https://www.eenews.net/articles/louisiana-bets-big-on-meta-approving-major-gas-power-expansion); [WWNO](https://www.wwno.org/coastal-desk/2026-04-21/advocates-cite-lack-of-transparency-rising-costs-as-regulators-fast-track-second-meta-data-center)).
- **PLTU batal pensiun.** Di AS, sejumlah unit PLTU ditunda pensiunnya dengan alasan beban data center. Contohnya Southern Company (Georgia/Mississippi), Four Corners (2031 mundur ke 2038), dan Mill Creek ([EESI](https://www.eesi.org/articles/view/data-center-buildout-is-hungry-for-fossil-fuels); [The Register](https://www.theregister.com/on-prem/2026/04/22/datacenter-boom-keeps-dirty-coal-plants-alive-in-the-us/5219820)).
- **Skala global.** Data center menghasilkan ~180 Mt CO₂ tidak langsung (2024), sekitar 0,5% emisi pembakaran dunia. Angka ini diproyeksikan memuncak di ~320 Mt pada 2030 dalam Base Case (IEA 2025).

## 3. Air

**Skala dan rinciannya.**

- IEA memperkirakan konsumsi air data center global **~560 miliar liter per tahun** (2023), naik menjadi **~1.200 miliar liter pada 2030**.
- Sekitar dua pertiga konsumsi itu berasal dari energi dan pembangkit, seperempat dari pendinginan langsung, dan sisanya dari manufaktur chip.
- Satu data center hiperskala 100 MW di AS mengonsumsi ~2 juta liter per hari, setara ~6.500 rumah tangga, dan lebih dari 60% di antaranya air tidak langsung ([IEA 2025](https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf)).

**Ren dkk. ("Making AI Less Thirsty", diterima di *Communications of the ACM*)** ([arXiv](https://arxiv.org/abs/2304.03271)):

- Pelatihan GPT-3 di data center Microsoft AS mengonsumsi **5,4 juta liter air**, termasuk 700.000 liter *on-site*.
- Total penarikan air AI global pada 2027 diproyeksikan **4,2–6,6 miliar m³**.
- Data perusahaan: konsumsi air Google 2025 mencapai **10,87 miliar galon**, 10,52 miliar di antaranya oleh data center. Angka ini naik 34% dari 8,135 miliar galon pada 2024. Sebanyak **13%** air tawar yang ditarik Google berasal dari wilayah dengan risiko kelangkaan tinggi ([Google 2026](https://sustainability.google/files/google-2026-environmental-report.pdf)).

**Iklim tropis lembap: buktinya ada, dan merugikan Indonesia.**

- **Tabel 1 Ren dkk.** memuat data center Microsoft di **Indonesia** (proyeksi Microsoft untuk fasilitas yang saat itu sedang dibangun). WUE *on-site* Indonesia **1,9 L/kWh, tertinggi** dari 18 lokasi. Pembandingnya Irlandia 0,02, Virginia 0,14, dan Arizona 1,63. PUE Indonesia 1,32, juga termasuk yang tertinggi.
- **IEA** mengutip Microsoft: WUE pendinginan langsung di Asia Pasifik **1,65 L/kWh**, lebih dari tiga kali rata-rata global ~0,5. IEA menyebut iklim "hangat dan lembap" membuat pendinginan lebih boros air. Sekitar separuh konsumsi air data center pada 2030 akan terjadi di Asia Pasifik (IEA 2025).
- **Data aktual Microsoft FY25** (tabel 15 Data Fact Sheet 2026) untuk data center **Jakarta**: 22.172 MWh listrik dan 84 megaliter penarikan air. Hasilnya **~3,8 liter per kWh, intensitas tertinggi dari 29 lokasi** yang dilaporkan. Pembandingnya Singapura ~1,25 (99% berasal dari air non-potabel), Kuala Lumpur ~1,15, Phoenix ~1,03, dan Dublin ~0,014 (perhitungan saya dari [Microsoft Data Fact Sheet 2026](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf)). Catatan: angka ini penarikan air fasilitas (bukan konsumsi) dan sebagian bisa berupa estimasi.
- **Singapura.**
  - Studi NTU mencatat rata-rata PUE Singapura 2,07 (data lama) ([NTU](https://dr.ntu.edu.sg/handle/10356/137780)).
  - IMDA menerbitkan standar *Tropical DC* SS 697:2023 yang mengizinkan ruang server beroperasi pada suhu lebih tinggi untuk menghemat pendinginan ([IMDA](https://www.imda.gov.sg/how-we-can-help/green-dc-roadmap/tropical-dc-standard)).
  - PUE Google di Singapura 1,12–1,14, lebih buruk dari rata-rata armadanya 1,09 (Google 2026).
- **Mekanismenya.** Udara panas dan lembap mengurangi jam pendinginan gratis (*free cooling*). Kelembapan tinggi (*wet-bulb* tinggi) juga menurunkan efisiensi menara pendingin evaporatif, sehingga operator memilih antara lebih banyak listrik (chiller) atau lebih banyak air.
- **Johor.** Pada 2024, 101 proyek meminta 808 juta liter per hari (MLD) air, tetapi hanya 142 MLD yang disetujui. Negara bagian meminta ekspansi data center berpendingin air ditunda sampai pertengahan 2027 ([SCMP](https://www.scmp.com/week-asia/health-environment/article/3333109/data-centres-malaysias-johor-told-wait-water-until-mid-2027); [w.media](https://w.media/special-report-how-johor-deals-with-thirsty-data-centers/)).

## 4. Material dan limbah

- **Mineral kritis (IEA 2025).** Pada 2030, permintaan data center diproyeksikan setara dengan porsi berikut dari permintaan total tahun 2024: tembaga ~2% (**512 kt**), silikon ~2%, tanah jarang lebih dari 3%, dan **galium 11%**.
- **Konsentrasi pasokan.** China memasok 98–99% galium olahan. Pada Desember 2024 China membatasi ekspor galium, germanium, dan antimon ke AS (IEA 2025; IEA 2026).
- **Nikel: kaitannya lemah dan tidak langsung.** Analisis IEA soal mineral untuk data center menyebut tembaga, silikon, tanah jarang, dan galium, **tidak menyebut nikel**. Penilaian saya (keyakinan rendah, belum diverifikasi dengan data): nikel masuk lewat baterai UPS/BESS (banyak yang memakai kimia LFP tanpa nikel), baja nirkarat, dan *superalloy* turbin gas. Narasi "nikel Indonesia untuk AI" belum didukung data kuantitatif. Kaitan nikel dengan kendaraan listrik dan baja nirkarat jauh lebih kuat.
- **E-waste.** Wang dkk. (*Nature Computational Science*, 2024) memperkirakan e-waste AI generatif tumbuh dari ~2,6 kt (2023) menjadi **0,4–2,5 juta ton per tahun pada 2030**. Totalnya 1,2–5,0 Mt untuk 2020–2030, dan strategi ekonomi sirkular dapat memangkasnya 16–86% ([Nature](https://www.nature.com/articles/s43588-024-00712-6); [The Register](https://www.theregister.com/2024/10/28/genai_dirty_secret/)).
- **Siklus pakai pendek.** Selama 54 hari pra-pelatihan Llama 3 dengan sampai 16.000 GPU H100, Meta mencatat 419 gangguan tak terduga, **58,7%** di antaranya karena masalah GPU ([arXiv](https://arxiv.org/abs/2407.21783)).
- **Emisi tertanam (embodied).** Scope 3 kini mendominasi: 85,8% dari jejak Microsoft. Kategori "capital goods" Amazon naik 43% pada 2025, dan Google kategori 2 naik dari 4,07 Mt (2023) menjadi 7,63 Mt (2025).

## 5. Dampak lain

- **Udara.** Analisis SELC memperkirakan 35 turbin gas xAI di Memphis berpotensi menghasilkan 1.200–2.100 ton NOx per tahun ([Inside Climate News](https://insideclimatenews.org/news/17072025/elon-musk-xai-data-center-gas-turbines-memphis/); [Earthjustice](https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus)). IEA mencatat lebih dari 400 MW turbin on-site dipasang di Tennessee pada 2024–2025.
- **Kebisingan dan genset diesel.** IEA mencatat bahwa di wilayah dengan batas kebisingan dan polusi udara yang ketat, pengembang beralih ke *fuel cell*. Pasokan gas on-site lewat satu pipa juga bisa membutuhkan cadangan diesel tambahan (IEA 2026). Data jam operasi genset di Indonesia belum tersedia; ini celah transparansi yang perlu dituntut.
- **Lahan.** Dari proyek data center skala gigawatt yang diumumkan, sekitar seperlimanya sudah mulai membuka lahan atau membangun (IEA 2026).
- **Panas buangan.** Hampir semua listrik yang masuk berakhir sebagai panas. Di iklim tropis, panas ini sulit dimanfaatkan (tidak ada kebutuhan pemanas ruangan), jadi argumen "heat reuse" ala Nordik tidak berlaku di Indonesia.

## 6. Metrik yang harus dituntut dari operator

| Metrik | Kenapa | Tuntutan minimum |
|---|---|---|
| **PUE** | Mengukur overhead fasilitas | Dilaporkan per lokasi, per jam/bulan |
| **WUE on-site dan off-site** (L/kWh) | PUE bisa diturunkan dengan pendinginan evaporatif yang justru boros air | Penarikan dan konsumsi, sumber air (potabel/non-potabel), status *water stress* |
| **CUE dan Scope 2 berbasis lokasi** | Metode berbasis pasar bisa menutupi emisi sampai 43.000 kali (kasus Meta) | Wajib disajikan berdampingan dengan angka berbasis pasar |
| **CFE per jam (24/7)** | Pencocokan tahunan 100% "terbarukan" ≠ listrik bersih nyata | Data per jam per grid. Google sendiri hanya mencapai **5% CFE per jam di Singapura** dan 13% di Asia Pasifik (2025) |
| **Additionality** | REC dari pembangkit lama tidak menambah energi bersih | Kontrak PPA baru di grid yang sama |
| **Scope 3 / embodied** | Bagian terbesar jejak perusahaan | Emisi konstruksi dan perangkat keras per MW |
| **Genset, NOx/PM, kebisingan (dB)** | Dampak bagi warga sekitar | Jam operasi, pemantauan berkala |

**Kenapa PUE saja menyesatkan.**

- PUE tidak mengukur air, karbon, efisiensi perangkat IT, atau emisi tertanam.
- Contoh: Google Singapura punya PUE 1,13, yang terlihat "hijau", padahal hanya ~5% listriknya bebas karbon per jam.
- PUE juga bisa turun hanya karena beban IT naik.

---

## Analogi untuk publik Indonesia (perhitungan terbuka)

Data acuan:

- Penjualan listrik PLN: **306,22 TWh (2024)** ([Kompas](https://money.kompas.com/read/2025/03/15/125728226/penjualan-listrik-tahun-2024-tertinggi-dalam-5-tahun-terakhir-pln-ungkap)) dan **317,69 TWh (2025)** ([Republika](https://ekonomi.republika.co.id/berita/t9re7p522/pln-catat-penjualan-31769-twh-di-2025)).
- Konsumsi listrik per kapita: **1.411 kWh (2024)** ([Kontan](https://industri.kontan.co.id/news/masih-jauh-dari-target-konsumsi-listrik-per-kapita-sepanjang-2024-baru-1411-kwh)). Ini angka seluruh sektor dibagi jumlah penduduk.

| Yang dibandingkan | Perhitungan | Hasil |
|---|---|---|
| Data center dunia 2025 (485 TWh) | 485 ÷ 317,69 | **≈1,5 kali seluruh penjualan PLN 2025** |
| Data center dunia 2030 (945 TWh) | 945 ÷ 317,69 | **≈3 kali penjualan PLN** |
| Listrik Google 2025 (43,48 TWh) | 43,48 miliar kWh ÷ 1.411 | ≈ jatah listrik **30,8 juta orang Indonesia** (≈13,7% penjualan PLN) |
| Microsoft FY25 (37,03 TWh) | ÷ 1.411 | ≈ **26,2 juta orang** |
| Satu kampus 1 GW (faktor beban 50–80%) | 1 GW × 8.760 jam × 0,5–0,8 = 4,4–7,0 TWh | ≈ **3,1–5,0 juta orang**, atau 1,4–2,2% penjualan PLN |
| Johor 5,1 GW (2030) | 22–36 TWh | ≈ **7–11% penjualan PLN 2025** |
| Air data center Google 2025 (10,52 miliar galon) | × 3,785 L = 39,8 juta m³ ÷ 2.500 m³ | ≈ **15.900 kolam renang olimpiade** |
| Satu prompt (0,24–0,34 Wh) | ÷ 10 W | Lampu LED 10 W menyala **1,5–2 menit** |

Konteks pasokan: 82% listrik Indonesia pada 2024 berasal dari bahan bakar fosil ([Ember](https://ember-energy.org/countries-and-regions/indonesia/)). Satu GW data center yang menyedot listrik dari grid ini praktis akan berjalan dengan listrik fosil.

## Cerita konkret

1. **Air Jakarta yang paling mahal.** Laporan Microsoft sendiri menunjukkan data center Jakarta menarik ~3,8 liter air per kWh. Itu tertinggi dari 29 lokasi globalnya: 270 kali Dublin, tiga kali Singapura. Hampir semua air Singapura berasal dari sumber non-potabel, sedangkan Jakarta tidak dilaporkan memakai sumber non-potabel. Di kota yang air tanahnya sudah krisis, ini pertanyaan kebijakan, bukan teknis.
2. **Memphis: turbin sebelum izin.** xAI menyalakan turbin gas untuk superkomputer Colossus di Memphis Selatan, komunitas kulit hitam yang sudah lama terbebani polusi, sebelum izinnya lengkap. Akhirnya keluar izin untuk 15 turbin. Perselisihan kemudian pindah ke Mississippi untuk Colossus 2. Kasus ini menunjukkan pola "listrik dulu, izin belakangan" yang harus dicegah di Indonesia.
3. **Johor: tetangga yang mengerem.** Johor menyetujui kurang dari seperlima air yang diminta data center (142 dari 808 MLD) dan menunda ekspansi berpendingin air sampai 2027. Investor yang tertahan di Johor bisa saja melirik Batam atau Jawa. Indonesia perlu syarat WUE dan sumber air sebelum gelombang itu datang.

## Mind-map

- **Jejak lingkungan AI**
  - **Listrik**
    - Global: 485 TWh (2025) → 945 TWh (2030)
    - Data center AI: ~150 TWh → ~465 TWh
    - Titik panas: Irlandia 22%, Virginia 26%, Singapura ~10%, Johor 5,1 GW
    - Per query: 0,24–0,34 Wh (versi perusahaan) vs reasoning 30–700 kali
  - **Emisi**
    - Perusahaan: Google +81%, Microsoft +62%, Amazon +58%
    - Akuntansi: pasar vs lokasi (Meta: 135 t vs 5,86 Mt)
    - Fosil: gas on-site 15–27 GW, Entergy-Meta, PLTU batal pensiun
  - **Air**
    - Langsung vs tidak langsung (dua pertiga dari energi)
    - Tropis: Indonesia WUE 1,9; Jakarta 3,8 L/kWh
    - Johor: moratorium air
  - **Material**
    - Tembaga, galium (11%), germanium
    - Nikel: lemah, tidak langsung
    - E-waste 0,4–2,5 Mt per tahun (2030); kegagalan GPU
  - **Dampak lokal**
    - NOx turbin, genset, kebisingan, lahan, panas
  - **Tuntutan metrik**
    - PUE + WUE + CUE berbasis lokasi + CFE per jam + additionality + Scope 3

## Tingkat keyakinan

| Klaim | Keyakinan | Catatan |
|---|---|---|
| Listrik DC global 2024–2025 | Tinggi | IEA, tetapi tanpa data resmi per perusahaan untuk AI |
| Proyeksi 2030 | Sedang | Rentang skenario 833–1.008 TWh |
| Porsi AI | Rendah–sedang | IEA memakai server akselerator sebagai proksi |
| Emisi perusahaan | Tinggi (sebagai angka laporan) | Batas laporan (boundary) dan metodenya terus berubah |
| Energi per prompt | Rendah | Tidak diaudit, median, tanpa definisi |
| Air Jakarta (Microsoft) | Sedang | Penarikan, bukan konsumsi; mungkin berupa estimasi; fasilitas kecil |
| WUE Indonesia (Ren) | Sedang | Proyeksi Microsoft untuk fasilitas yang belum jadi (2023) |
| E-waste | Rendah–sedang | Estimasi kasar menurut penulisnya sendiri |
| Kaitan nikel | Rendah | Tidak ada data kuantitatif |

Catatan proses: anggaran pencarian web habis sebelum saya sempat memverifikasi data PLN per provinsi dan pangsa LFP di BESS data center. Karena itu analogi memakai angka nasional dan per kapita.

## Kritik jujur: klaim yang sebaiknya tidak dipakai WALHI

1. **"Satu prompt = sebotol air."** Ini keliru. Ren dkk. menyebut 500 mL untuk **10–50 respons** GPT-3, dengan asumsi 4 Wh per permintaan. Asumsi itu lebih dari 10 kali angka yang dilaporkan perusahaan pada 2025. Jika parameter Indonesia dari Ren (WUE 1,9, EWIF 2,27, PUE 1,32) diterapkan pada 0,34 Wh, hasilnya ~1,3 mL per prompt, atau sekitar **400 prompt per botol**.
   **Versi yang bisa dipertahankan:** "Satu kampus 100 MW meminum ~2 juta liter per hari (IEA), dan di iklim tropis efisiensi airnya paling buruk."
2. **"AI menghabiskan listrik dunia."** Data center memakai ~1,5–3% listrik dunia dan kurang dari 1% emisi CO₂ global (IEA).
   **Versi yang bisa dipertahankan:** "Dampaknya terkonsentrasi secara lokal: 22% listrik Irlandia, seperempat listrik Virginia, dan pembangkit fosil baru dibangun khusus untuk data center."
3. **"Data center 100% energi terbarukan."** Klaim ini berbasis sertifikat tahunan. Angka per jam Google di Singapura hanya 5%.
4. **"Efisiensi akan menyelesaikan masalah."** Energi per prompt Google turun 33 kali, tetapi total listriknya naik 37% dalam setahun. Ini efek *rebound*.
5. **"Nikel Indonesia menggerakkan AI."** Belum ada bukti. Jangan dijadikan inti narasi.
6. **"E-waste AI adalah bencana terbesar."** Angka 0,4–2,5 Mt per tahun signifikan, tetapi masih kecil dibanding total e-waste dunia ~62 Mt (2022) ([Global E-waste Monitor](https://ewastemonitor.info/)). Lebih baik dibingkai sebagai pemborosan siklus pakai yang pendek.
7. **Jangan mengutip "7,62 kali lebih tinggi" (The Guardian) sebagai angka hari ini.** Angka itu untuk 2020–2022 dan hanya data center milik sendiri. Pakai angka primer dari laporan perusahaan di Tabel 2.

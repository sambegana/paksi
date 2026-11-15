# 01 — Lensa Orang Dalam: Masalah AI Global dan Akar Menjamurnya Data Center

*Riset persona "orang dalam industri AI yang keluar karena tahu bahayanya". Disusun 15 November 2026 untuk advokasi WALHI. Lingkup: logika industri, peta risiko non-lingkungan, narasi yang perlu dibongkar, dan implikasinya bagi Indonesia. Angka energi/air yang rinci, inventaris data center, dampak lokal, ekonomi politik, dan hukum ditangani agen lain.*

---

## 0. Pembuka persona: siapa, dan kenapa mereka

Ada empat "orang dalam" yang paling sering dikutip. Dari keempatnya, dua paling berguna untuk advokasi lingkungan di Global South.

**Lensa utama: Timnit Gebru (eks-Google, kini DAIR).** Gebru adalah salah satu penulis makalah *"On the Dangers of Stochastic Parrots"* (FAccT 2021). Google memaksanya keluar terkait makalah itu. Makalah ini sejak awal menyambungkan ukuran model dengan keadilan lingkungan dan Global South. Kutipan aslinya (diverifikasi dari teks makalah, https://dl.acm.org/doi/10.1145/3442188.3445922):

> "Is it fair or just to ask, for example, that the residents of the Maldives (likely to be underwater by 2100) or the 800,000 people in Sudan affected by drastic floods pay the environmental price of training and deploying ever larger English LMs, when similar large-scale models aren't being produced for Dhivehi or Sudanese Arabic?"

> "...increasing the environmental and financial costs of these models doubly punishes marginalized communities that are least likely to benefit from the progress achieved by large LMs and most likely to be harmed by negative environmental consequences of its resource consumption."

Lewat institutnya, DAIR, Gebru juga ikut mendirikan *Data Workers' Inquiry* bersama pekerja data di Kenya, Venezuela, dan Suriah (https://www.dair-institute.org/projects/data-workers-inquiry). Jadi lensa ini mencakup dua hal sekaligus: lingkungan dan buruh. Nama Margaret Mitchell muncul sebagai "Shmargaret Shmitchell" di daftar penulis makalah yang sama.

**Lensa kedua: Mrinank Sharma (eks-Anthropic).** Sharma memimpin tim Safeguards Research di Anthropic selama sekitar dua tahun. Ia meneliti sikap AI yang menjilat (*sycophancy*) dan pertahanan terhadap bioterorisme berbantuan AI (https://www.eweek.com/news/ai-safety-leader-resigns-anthropic-global-risks/). Faktanya sudah diverifikasi. Hari terakhirnya 9 Februari 2026, dan surat pengunduran dirinya diterbitkan ulang di Substack-nya (https://mrinank.substack.com/p/why-i-left-anthropic). Kutipan asli dari surat itu:

> "The world is in peril. And not just from AI, or bioweapons, but from a whole series of interconnected crises unfolding in this very moment."

> "...throughout my time here, I've repeatedly seen how hard it is to truly let our values govern our actions."

Ia juga menulis tentang tempat kerja di mana "we constantly face pressures to set aside what matters most".

**Kenapa dua tokoh ini.** Gebru memberi kerangka keadilan: siapa yang menanggung biaya dan siapa yang menikmati hasil. Kerangka ini sejalan dengan bahasa keadilan ekologis WALHI. Sharma memberi kesaksian dari dalam bahwa nilai kalah oleh tekanan. Ia juga menempatkan AI di dalam krisis yang saling terkait (*polycrisis*), bukan sebagai isu teknologi yang berdiri sendiri.

Kokotajlo dan Leike tetap berguna sebagai bukti tekanan komersial (lihat poin 4). Kokotajlo menolak menandatangani perjanjian non-disparagement walau ekuitas dalam jumlah besar dipertaruhkan. Leike menulis bahwa "safety culture and processes have taken a backseat to shiny products" (https://fortune.com/2024/05/17/openai-researcher-resigns-safety/). Namun kerangka mereka berpusat pada risiko AGI. Menurut analisis saya, kerangka itu mudah dipakai untuk membenarkan perlombaan compute: "kita harus menang dulu sebelum pihak lain". Kerangka seperti ini kurang cocok untuk advokasi di tingkat tapak.

---

## 1. Logika "scaling": kenapa data center terus membesar

Saya bicara dengan suara saya sendiri, terinspirasi lensa orang dalam. Di dalam lab, keyakinan dasarnya adalah *scaling laws*: kemampuan model naik secara terprediksi jika compute, data, dan parameter ditambah. Selama keyakinan itu dipegang, setiap lab merasa tertinggal jika berhenti membangun.

- **Pertumbuhan compute.** Compute untuk melatih model frontier tumbuh sekitar **4–5x per tahun**. Untuk model bahasa frontier angkanya sekitar 5x per tahun, dengan data 2010–Mei 2024 (Epoch AI, https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year).
- **Capex hyperscaler 2026.** Panduan gabungan empat perusahaan sekitar **US$720–745 miliar**. Rinciannya: Amazon ±US$220 miliar (ditegaskan ulang 29 Oktober 2026), Alphabet US$195–205 miliar, Microsoft ±US$170–175 miliar (angka paling tidak pasti karena reklasifikasi sewa), dan Meta US$135–145 miliar (https://www.datacentres.com/guides/hyperscaler-capex-trends). Sebagai pembanding, beberapa pelacak menyebut angka 2025 sekitar US$410 miliar. *Keyakinan sedang:* angka ini berasal dari pelacak sekunder yang merangkum laporan keuangan, dan tidak semua capex khusus untuk AI.
- **Stargate (OpenAI).** Proyek ini diumumkan dengan nilai US$500 miliar. Per September–Oktober 2026, hanya Abilene, Texas, yang beroperasi dalam skala nyata, sekitar 618 MW dari rencana 1,2 GW. Situs lain masih dibangun atau baru dikontrak. Situs Inggris dihentikan sementara pada April 2026 dengan alasan biaya energi (https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand; https://en.wikipedia.org/wiki/Stargate_LLC). Klaim "10 GW tercapai" sebagian besar berupa kapasitas yang dikontrak, bukan yang sudah dibangun.
- **Akibatnya pada listrik.** Data center memakai sekitar **415 TWh pada 2024** (±1,5% listrik dunia). Dalam Base Case, angka ini diproyeksikan menjadi **±945 TWh pada 2030** (IEA, *Energy and AI*, 2025, https://www.iea.org/reports/energy-and-ai/executive-summary).

**Inti dari dalam.** Ekspansi ini tidak didorong permintaan masyarakat. Ia didorong oleh taruhan bahwa skala adalah jalan menuju dominasi. AI Now Institute menyebut skala compute dan data sebagai "proxy" performa. Proxy itu kebetulan menguntungkan pemilik cloud (laporan *Artificial Power*, Juni 2025, https://ainowinstitute.org/publications/research/executive-summary-artificial-power).

---

## 2. Peta risiko AI di luar lingkungan

**a. Konsentrasi kekuasaan.** Compute, cloud, dan chip dikuasai segelintir perusahaan. Menurut AI Now (2025), jalan tercepat menuju laba AI adalah permintaan cloud, sehingga hyperscaler untung baik ketika model berhasil maupun gagal ("Heads I Win, Tails You Lose").

**b. Keselamatan dan kontrol.** Kesaksian Leike (2024) dan Sharma (2026) menunjukkan pola yang sama: tim keselamatan bekerja di bawah tekanan produk. Pada Juni 2024, 13 pegawai dan mantan pegawai OpenAI dan Google DeepMind menandatangani surat *"A Right to Warn about Advanced Artificial Intelligence"*. Mereka meminta perlindungan bagi pelapor (https://www.lesswrong.com/posts/q3zs7E7rktHsESXaF/openai-8-the-right-to-warn).

**c. Disinformasi dan demokrasi, dengan contoh Indonesia.** Pada Januari 2024, Wakil Ketua Umum Golkar Erwin Aksa mengunggah video deepfake Soeharto yang mengajak orang memilih Golkar (https://www.benarnews.org/english/news/indonesian/suharto-deepfake-used-in-election-campaign-01122024135217.html; OECD AI Incidents, https://oecd.ai/en/incidents/2024-01-09-2d3c). NPR mencatat bahwa gelombang deepfake yang ditakutkan pada pemilu 2024 secara global ternyata tidak sebesar perkiraan (https://www.npr.org/2024/12/21/nx-s1-5220301/deepfakes-memes-artificial-intelligence-elections). Karena itu, jangan membesar-besarkan isu ini.

**d. Pengawasan.** AI menurunkan biaya pengenalan wajah, analisis media sosial, dan profiling. *Catatan:* dalam riset ini saya tidak memverifikasi kasus spesifik di Indonesia. Agen hukum atau dampak lokal sebaiknya mengecek.

**e. Tenaga kerja tersembunyi: pelabel data di Global South.**
- **Kenya:** Melalui Sama, OpenAI mempekerjakan pelabel dengan upah bersih sekitar **US$1,32–2 per jam** untuk menyaring konten kekerasan seksual dan penyiksaan demi ChatGPT. Pada saat yang sama, OpenAI membayar Sama US$12,50 per jam per pekerja (TIME, Januari 2023, dirangkum di https://www.business-humanrights.org/en/latest-news/openai-and-sama-hired-underpaid-workers-in-kenia-to-filter-toxic-content-for-chatgpt).
- **Filipina:** Pekerja Remotasks (Scale AI) sering dibayar di bawah upah minimum daerah, dan pembayaran mereka kerap ditahan (Washington Post, 28 Agustus 2023, https://www.washingtonpost.com/world/2023/08/28/scale-ai-remotasks-philippines-artificial-intelligence/).
- **Indonesia:** Ada indikasi, tetapi datanya tipis. Riset Tech Global Institute yang dilaporkan Kompas menggambarkan moderator konten dan pelabel data Indonesia sebagai pekerja berupah rendah tanpa jaminan sosial. Serikat Sindikasi mengakui ada anggotanya yang bekerja lepas sebagai pelabel, tetapi tidak punya data jumlahnya (https://www.kompas.id/artikel/en-pekerja-bayangan-di-balik-platform-digital-kerja-berat-upah-rendah-dan-minim-jamsos). Pemetaan Brown University (Oktober 2026) juga menyebut Indonesia sebagai salah satu lokasi alih daya (https://www.brown.edu/news/2026-10-26/ai-data-workers). *Keyakinan rendah–sedang:* belum ada studi upah yang khusus tentang Indonesia.

**f. Hak cipta dan data.** Kasus *Bartz v. Anthropic* berakhir dengan penyelesaian **US$1,5 miliar** atas buku bajakan yang dipakai untuk pelatihan. Persetujuan final keluar pada 20 Juli 2026, dengan kompensasi sekitar US$3.000 per buku (https://news.bloomberglaw.com/ip-law/anthropic-authors-1-5-billion-deal-receives-final-approval). Anthropic tidak mengakui kesalahan, dan putusan 2025 bahwa pelatihan pada buku termasuk *fair use* tetap berlaku.

**g. Bias.** *Stochastic Parrots* (2021) mencatat model besar menyerap bias hegemonik dari data internet, dan kerugiannya jatuh pada kelompok marginal. Bahasa daerah dan lokal juga kurang terwakili.

**h. Pekerjaan.** IMF (Januari 2024) memperkirakan AI memengaruhi hampir **40% pekerjaan global**: 60% di negara maju, 40% di negara berkembang, dan 26% di negara berpendapatan rendah. Negara berkembang juga dinilai "kurang mungkin" menikmati manfaatnya (https://www.cnbc.com/2024/01/15/imf-warns-ai-to-hit-almost-40percent-of-global-employment-worsen-inequality.html).

---

## 3. Narasi industri yang perlu dibongkar

**"AI akan menyelesaikan krisis iklim."**
- Eric Schmidt (eks-CEO Google), Oktober 2024: *"we're not going to hit the climate goals anyway because we're not organized to do it"*. Ia menyarankan agar kita "bet on AI solving the problem" (https://www.theregister.com/2024/10/08/eric_schmidt_speech/).
- Bantahannya datang dari IEA sendiri. Skenario pengurangan 1.400 Mt CO₂ pada 2035 berlaku bersyarat, dan IEA menulis: *"there is currently no momentum that could ensure the widespread adoption of these AI applications... their aggregate impact, even in 2035, could be marginal"* (https://www.iea.org/reports/energy-and-ai/ai-and-climate-change).
- Laporan koalisi *The AI Climate Hoax* (Februari 2026, penulis Ketan Joshi) menemukan **74% klaim** manfaat iklim AI dari Big Tech tidak terbukti. Dari klaim yang diperiksa, hanya 26% mengutip riset akademik, dan 36% tidak menyertakan bukti sama sekali. Laporan ini juga menemukan pola "bait-and-switch": manfaat AI "tradisional" yang hemat energi, seperti prakiraan angin, dipakai untuk membela AI generatif yang boros (https://beyondfossilfuels.org/2026/02/17/report-exposes-big-techs-ai-climate-hoax-74-of-industrys-claims-about-ais-climate-benefits-are-unproven/). *Catatan:* laporan ini disusun oleh pihak advokasi, dan "tidak terbukti" di sini berarti tanpa bukti yang dikutip, bukan terbukti salah.

**"Efisiensi akan menyelamatkan" (DeepSeek dan paradoks Jevons).**
- Pada Januari 2025, model DeepSeek-R1 yang jauh lebih murah sempat menjatuhkan saham Nvidia. Respons CEO Microsoft Satya Nadella pada 27 Januari 2025: *"Jevons paradox strikes again!"*, artinya AI yang lebih murah akan dipakai jauh lebih banyak (https://fortune.com/2025/01/27/microsoft-ceo-satya-nadella-deepseek-optimism-jevons-paradox/). Industri sendiri mengakui bahwa efisiensi tidak dimaksudkan untuk mengurangi konsumsi total.
- Buktinya terlihat setahun kemudian: capex 2026 justru naik (lihat poin 1).

**Janji net-zero.**
- Total emisi Microsoft naik **25% dalam setahun**, menjadi 20,29 juta ton CO₂e pada FY2025. Perusahaan sendiri menyebut ekspansi data center untuk AI sebagai pendorong utama (laporan Juli 2026, https://www.esgdive.com/news/microsofts-data-center-expansion-drove-25-emissions-spike-2025-environmental-sustainability-report/825082/). Target "carbon negative 2030" tetap tercantum.
- Untuk Google, angka 2026 masih simpang siur antar-sumber. Satu sumber menyebut total emisi naik 18% secara tahunan, sementara sumber lain menyebut emisi Scope 1+2 turun 2%. Akuntansi berbasis pasar (sertifikat energi terbarukan) bisa membuat angka tampak lebih kecil (https://newtral.io/articles/ai-emissions-accounting-microsoft-google). *Gunakan dengan hati-hati.*

**"Sovereign AI."**
- Di Indonesia, istilah ini dipakai untuk proyek Indosat–Nvidia, AI Center of Excellence Komdigi bersama Indosat, Cisco, dan Nvidia (Juli 2025), serta rencana Indosat "Zankore" berkapasitas hingga 1 GW (https://siliconangle.com/2025/07/16/indonesia-to-establish-ai-center-of-excellence-with-support-from-nvidia-cisco-and-indosat/; https://www.datacenterdynamics.com/en/news/indosat-reinforces-ai-push-with-1gw-data-center-play/).
- Pertanyaan orang dalam: berdaulat atas apa, jika chip, perangkat lunak, dan model dasarnya tetap milik segelintir perusahaan AS? Yang "berdaulat" bisa jadi hanya lokasi beban listrik, air, dan lahannya.

---

## 4. Yang orang dalam tahu tetapi publik tidak

1. **Data energi dan air per model hampir tidak pernah dibuka.** Luccioni dkk. menyebut kekosongan ini *"misinformation by omission"* (arXiv 2506.15572, Juni 2025, https://arxiv.org/abs/2506.15572). Menurut liputan Wired, 84% penggunaan LLM pada Mei 2025 berjalan di model tanpa disclosure lingkungan sama sekali. *Keyakinan sedang:* angka 84% belum saya temukan di teks makalah.
2. **Disclosure yang ada pun bisa dibentuk.** Google (Agustus 2025) menyebut median prompt Gemini menghabiskan 0,24 Wh dan 0,26 mL air, sekitar "lima tetes". Kritik terhadap angka ini: (a) memakai median, bukan rata-rata; (b) akuntansi karbon berbasis pasar; (c) mengabaikan air tidak langsung dari pembangkit listrik. Shaolei Ren memperkirakan angkanya bisa ±50 mL jika air tidak langsung dihitung. Selain itu, data mentahnya tidak dibuka (https://www.neowin.net/news/experts-accuse-google-of-downplaying-ai-water-use-with-5-drops-per-prompt-claim/).
3. **Tekanan komersial mengalahkan keselamatan.** Leike (2024): "shiny products". Sharma (2026): "pressures to set aside what matters most". Kokotajlo (2024) mempertaruhkan ekuitas yang menurut pengakuannya setara ±85% kekayaan bersih keluarganya demi menolak klausul non-disparagement. Belakangan OpenAI mengembalikan ekuitas itu dan mencabut klausulnya (https://venturebeat.com/ai/more-openai-researchers-slam-company-on-safety-call-for-right-to-warn-to-avert-human-extinction).
4. **Banyak angka besar baru berupa pengumuman.** "10 GW Stargate" atau "1 GW Zankore" sering berarti kontrak atau rencana. Pengkampanye perlu membedakan kapasitas yang diumumkan, yang dikontrak, dan yang beroperasi.

---

## 5. Implikasi untuk Indonesia dan Global South: kenapa jadi target

- **Limpahan dari Singapura dan Johor.** Singapura merasionalisasi kapasitas data center sejak moratorium 2019, dan Johor mulai memperketat izin karena kelangkaan air. Akibatnya Batam (Nongsa Digital Park) diposisikan sebagai hub berikutnya. BMI menyebut air sebagai kendala jangka panjang "paling serius", dengan laporan kekurangan air di sekitar 18 lokasi di Batam per Februari 2026 (https://technode.global/2026/08/14/indonesias-data-center-boom-faces-growing-infrastructure-challenges-bmi/). *Detail inventaris dan dampaknya ditangani agen lain.*
- **Investasi besar dan narasi kemajuan.** Microsoft mengumumkan investasi US$1,7 miliar untuk cloud dan AI di Indonesia pada April 2024, termasuk region data center pertamanya (https://news.microsoft.com/apac/2024/04/30/microsoft-announces-us1-7-billion-investment-to-advance-indonesias-cloud-and-ai-ambitions/).
- **Jaringan listrik yang bertumpu pada batu bara.** Batu bara memasok **61,8%** listrik Indonesia pada 2023, dan bahan bakar fosil memenuhi ±82% permintaan listrik pada 2024 (Ember, https://ember-energy.org/countries-and-regions/indonesia/). Artinya, setiap MW data center baru di Indonesia hampir pasti memperpanjang umur batu bara, kecuali ada kewajiban tambahan energi terbarukan yang betul-betul baru.
- **Pola lama dengan wajah baru.** Global South memasok tenaga kerja murah (pelabel data), lahan, air, dan listrik, sedangkan nilai tambah dan kendali model tetap di Utara. Ini persis distribusi yang diperingatkan *Stochastic Parrots*.

---

## 6. Cerita yang bisa dipakai pengkampanye

1. **"Dua dolar per jam untuk membersihkan ChatGPT."** Pekerja di Nairobi membaca 150–250 potongan teks kekerasan seksual dan penyiksaan per shift supaya ChatGPT terasa "aman" bagi pengguna di Utara. OpenAI membayar kontraktor US$12,50 per jam, sementara pekerja menerima kurang dari US$2. Sumber: TIME, 2023 (lihat poin 2e). Kaitan untuk WALHI: rantai pasok AI mengekstraksi tenaga, seperti juga lahan dan air.
2. **"Kepala keselamatan yang memilih puisi."** Pada Februari 2026, pemimpin riset safeguards di salah satu lab yang paling vokal soal keselamatan mundur dan menulis "The world is in peril", sambil menyebut krisis yang saling terkait. Kaitan: bahkan orang dalam melihat AI sebagai bagian dari polycrisis, bukan solusinya.
3. **"Jevons menyerang lagi" dan emisi Microsoft.** Ketika AI menjadi lebih efisien (DeepSeek), CEO Microsoft justru merayakannya karena pemakaian akan naik. Delapan belas bulan kemudian, Microsoft melaporkan emisinya naik 25% dalam setahun karena data center AI. Kaitan: efisiensi tanpa batas absolut tidak menyelamatkan apa pun.
4. *(Cadangan, konteks Indonesia)* **Soeharto "bangkit" lewat AI** untuk berkampanye pada Pemilu 2024.

---

## 7. Node mind-map: masalah AI global menurut lensa orang dalam

- **Akar: logika scaling**
  - Scaling laws → compute tumbuh 4–5x per tahun
  - Perlombaan frontier lab (AS–Tiongkok, antar-lab)
  - Capex hyperscaler ±US$720–745 miliar (2026)
  - Megaproyek (Stargate, "AI factory", sovereign AI)
- **Ekstraksi material**
  - Listrik (415 → 945 TWh) → umur batu bara diperpanjang
  - Air (pendingin + air tidak langsung dari pembangkit)
  - Lahan dan limbah elektronik (wilayah agen lain)
- **Ekstraksi manusia**
  - Pelabel data dan moderator (Kenya, Filipina, Indonesia?)
  - Hak cipta dan data tanpa izin
  - Disrupsi pekerjaan (IMF 40%)
- **Kekuasaan**
  - Konsentrasi compute, cloud, dan chip
  - Ilusi "sovereign AI"
  - Lobi regulasi dan narasi
- **Pengetahuan dan demokrasi**
  - Disinformasi dan deepfake (Soeharto 2024)
  - Bias dan peminggiran bahasa lokal
  - Pengawasan
- **Keselamatan dan tata kelola internal**
  - Tekanan komersial vs keselamatan (Leike, Sharma)
  - Pembungkaman pelapor (non-disparagement, Right to Warn)
- **Opasitas**
  - Tidak ada disclosure energi/air per model
  - Disclosure selektif (median, akuntansi berbasis pasar)
  - Pengumuman vs kapasitas nyata
- **Narasi tandingan yang harus dibongkar**
  - "AI selamatkan iklim" (74% klaim tak terbukti; IEA: "no momentum")
  - "Efisiensi menyelamatkan" (Jevons)
  - "Net-zero" (Microsoft +25%)
  - "Sovereign AI"

---

## 8. Tingkat keyakinan

| Klaim | Keyakinan | Catatan |
|---|---|---|
| Kutipan Gebru dkk. (*Stochastic Parrots*) | Tinggi | Diverifikasi dari teks makalah |
| Kutipan surat Sharma | Tinggi | Diverifikasi dari Substack-nya |
| IEA 415/945 TWh; kutipan "no momentum" | Tinggi | Halaman resmi IEA |
| Capex 2026 ±US$720–745 miliar | Sedang | Pelacak sekunder; definisi tiap perusahaan berbeda; baseline 2025 belum diverifikasi |
| Status Stargate | Sedang | Data satelit/pelacak, bukan angka resmi OpenAI |
| Emisi Microsoft +25% | Tinggi | Laporan perusahaan via ESG Dive |
| Angka emisi Google 2026 | Rendah | Sumber saling bertentangan |
| 84% penggunaan LLM tanpa disclosure | Sedang | Dari Wired, belum ditemukan di makalah |
| Pelabel data di Indonesia | Rendah–sedang | Indikasi ada, tanpa data upah atau jumlah |
| 74% klaim iklim AI tak terbukti | Sedang | Laporan advokasi; sumber lain menyebut 73% |
| Peran Danantara di data center AI | Belum terverifikasi | Tidak dimasukkan sebagai klaim |

---

## 9. Kritik jujur: argumen yang lemah dan bisa diserang balik

1. **"AI = bencana iklim" secara mutlak.** Data center baru menyumbang ±1,5% listrik dunia (2024), dan IEA memang memodelkan potensi pengurangan emisi dari AI. Lebih aman berargumen soal *lokasi, laju, dan siapa yang menanggung*: beban lokal pada air dan jaringan listrik berbasis batu bara.
2. **Angka "per prompt".** Angka seperti "satu botol air per ChatGPT" mudah dipatahkan dengan angka resmi Google (0,26 mL). Fokuskan pada skala agregat dan tuntutan disclosure, bukan angka per kueri yang diperdebatkan.
3. **Menggunakan bahasa "risiko eksistensial/AGI".** Bahasa ini bisa terdengar seperti fiksi ilmiah dan malah memperkuat narasi "harus berlomba". Gunakan kesaksian orang dalam sebagai bukti *budaya korporasi*, bukan ramalan kiamat.
4. **Laporan advokasi sebagai bukti tunggal.** *AI Climate Hoax* bisa dicap bias. Pasangkan dengan IEA dan laporan keberlanjutan perusahaan sendiri.
5. **Menolak semua AI.** Lawan bisa menuding WALHI anti-kemajuan, padahal AI untuk pemantauan deforestasi dan kebakaran juga dipakai gerakan lingkungan. Bedakan AI generatif skala raksasa dari AI terapan berskala kecil.
6. **Pelabel data Indonesia.** Jangan mengklaim angka atau kasus yang belum ada. Lebih baik jadikan ini agenda riset bersama serikat (misalnya Sindikasi).
7. **Deepfake pemilu.** Dampak elektoral deepfake Soeharto sulit dibuktikan, dan gelombang deepfake global 2024 lebih kecil dari perkiraan. Pakai sebagai ilustrasi, bukan bukti kerusakan demokrasi.
8. **"Sovereign AI = penjajahan".** Pemerintah akan membalas dengan argumen kedaulatan data dan lapangan kerja. Lebih kuat bertanya *syarat apa* yang dikenakan: energi terbarukan tambahan yang benar-benar baru, batas air, disclosure, dan persetujuan masyarakat.

---

### Sumber utama
- Bender, Gebru, McMillan-Major, Shmitchell (2021), https://dl.acm.org/doi/10.1145/3442188.3445922
- Sharma (2026), https://mrinank.substack.com/p/why-i-left-anthropic
- IEA (2025), https://www.iea.org/reports/energy-and-ai/executive-summary ; https://www.iea.org/reports/energy-and-ai/ai-and-climate-change
- Epoch AI, https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year
- AI Now (2025), https://ainowinstitute.org/publications/research/executive-summary-artificial-power
- Luccioni dkk. (2025), https://arxiv.org/abs/2506.15572
- Beyond Fossil Fuels dkk. (2026), https://beyondfossilfuels.org/2026/02/17/report-exposes-big-techs-ai-climate-hoax-74-of-industrys-claims-about-ais-climate-benefits-are-unproven/
- DAIR Data Workers' Inquiry, https://www.dair-institute.org/projects/data-workers-inquiry
- Sumber lain tercantum di dalam teks.

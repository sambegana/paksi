# 07 — Hukum & Kebijakan: Pusat Data AI di Indonesia (celah dan tuas hukum)

*Status per 15 November 2026. Disusun dari sudut pandang ahli hukum lingkungan (cara pikir ICEL dan praktisi litigasi). Ini riset awal untuk advokasi, bukan nasihat hukum. Setiap rujukan pasal disertai sumber. Yang belum terverifikasi ditandai **[CEK]**.*

---

## 1. Pembuka persona

Saya membaca pusat data (data center/DC) seperti membaca proyek ekstraktif. Pertanyaan saya: izin apa yang dipakai, siapa yang menilai dampaknya, siapa yang boleh bersuara, dan ke pengadilan mana kita bisa membawanya. Kesimpulan awal saya: **Indonesia belum punya rezim hukum khusus pusat data dari sisi lingkungan.** DC diatur dengan instrumen umum: perizinan berbasis risiko, AMDAL multisektor, izin air, dan izin ketenagalistrikan. WALHI sendiri sudah menyatakan hal yang sama dalam kasus Batam ([Mongabay, 10/10/2026](https://mongabay.co.id/2026/10/10/batam-krisis-air-warga-demo-data-center/)).

Kekosongan ini punya dua sisi. Sisi lemahnya, tidak ada ambang listrik atau air yang khusus untuk DC, dan tidak ada kewajiban keterbukaan. Sisi kuatnya, instrumen umum itu cukup tajam kalau dipakai dengan benar. Buktinya Jatiluhur: Gubernur Jawa Barat menghentikan pembangunan DC AI BDx pada 30 September 2026 karena AMDAL dan PBG belum ada ([jabarprov.go.id](https://jabarprov.go.id/berita/kdm-hentikan-sementara-pusat-data-ai-di-kawasan-jatiluhur-karena-belum-ada-amdal-dan-pbg-26031); [ANTARA](https://www.antaranews.com/berita/5769159/kdm-hentikan-pembangunan-data-center-ai-jatiluhur-akibat-tanpa-amdal)).

---

## 2. Temuan kunci

1. **DC tercantum dalam daftar AMDAL, tetapi tanpa ambang khusus.** Lampiran I Permen LHK 4/2021 mencantumkan KBLI 63111 (Aktivitas pengolahan data) dan 63112 (Aktivitas hosting dan YBDI) pada nomor urut 163–164. Skalanya "sesuai besaran di multisektor", Kategori C. Kriteria multisektor di Lampiran II huruf A wajib AMDAL untuk **luas lahan ≥ 5 ha dan/atau luas bangunan terbangun ≥ 10.000 m²**. UKL-UPL berlaku untuk 5.000–10.000 m², dan SPPL di bawah 5.000 m². **Tidak ada ambang berdasarkan daya listrik (MW).** Ini hasil baca langsung teks Permen ([salinan PDF di bp2sdm KLHK](https://sdmhutkadipaten.bp2sdm.kehutanan.go.id/wp-content/uploads/2022/05/PERMEN-LHK-NO.-4-TAHUN-2021-PERMENHUT-DAFTAR-USAHA-WAJIB-AMDAL-1_2.pdf); [BPK](https://peraturan.bpk.go.id/Download/205143/permen%20LHK%20No.%204%20tahun%202021.pdf)).
2. **Pemicu AMDAL lain dalam Permen yang sama bisa dipakai terhadap DC:**
   - Pengambilan **air tanah dalam untuk tujuan komersial ≥ 50 l/detik**.
   - Pengambilan **air baku dari sungai atau danau ≥ 250 l/detik**.
   - **Pembangkit (PLTU/PLTG/PLTD/PLTMG, termasuk hibrid) ≥ 100 MW dalam satu lokasi**. PLTD 5 sampai kurang dari 100 MW cukup UKL-UPL.

   Contoh penerapan: proyek Jatiluhur diperkirakan menyedot hingga 384 l/detik ([ANTARA](https://www.antaranews.com/berita/5769159/kdm-hentikan-pembangunan-data-center-ai-jatiluhur-akibat-tanpa-amdal)), jauh di atas ambang 250 l/detik. Genset cadangan DC skala hyperscale bisa mencapai ratusan MW. Apakah genset cadangan dihitung sebagai "pembangkit" untuk ambang 100 MW masih bisa diperdebatkan dan perlu diuji **[CEK]**.
3. **Celah terbesar ada di kawasan industri, KEK, dan KPBPB.** Usaha di dalam kawasan yang sudah memiliki AMDAL kawasan dan persetujuan lingkungan kawasan dikecualikan dari AMDAL sendiri. Usaha itu cukup menyusun **RKL-RPL rinci yang diperiksa dan disahkan oleh *pengelola kawasan***, bukan oleh pemerintah dan tanpa konsultasi publik. Dasarnya PP 22/2021 Pasal 10 ayat (1) beserta Penjelasannya, dan kini Pasal 102 ayat (1) PP 28/2025 menurut [Hukumonline](https://www.hukumonline.com/klinik/a/sudah-ada-amdal-kawasan-perlukah-perusahaan-punya-amdal-sendiri-lt61c03b03c52ca). Nomor huruf dan pasal perlu dicek ke naskah resmi **[CEK]**. Akibatnya, DC di Nongsa Digital Park atau Kabil (Batam) dan di kawasan industri Cikarang/Karawang bisa berdiri tanpa AMDAL tersendiri, padahal AMDAL kawasan yang lama tidak memperhitungkan beban air dan listrik DC AI.
4. **PP 5/2021 sudah dicabut.** Penggantinya PP 28/2025 tentang Penyelenggaraan Perizinan Berusaha Berbasis Risiko, yang berlaku 5 Juni 2025 ([JDIH BPK](https://peraturan.bpk.go.id/Details/319773/pp-no-28-tahun-2025); [JDIH Kemenkeu](https://jdih.kemenkeu.go.id/dok/pp-28-tahun-2025/overview)). Dalam KBLI 2025, kode 63111 dan 63112 kabarnya berubah menjadi 63101 dan 63102. Ini baru dari satu sumber sekunder ([LegalMP](https://legalmp.id/artikel/legalitas/izin-usaha-pusat-data-data-center-syarat-kbli-aturan-uu-pdp/)) **[CEK BPS]**. Tingkat risiko DC di lampiran PP 28/2025 belum saya verifikasi **[CEK]**.
5. **Perpres AI belum memuat aspek lingkungan.** Dua rancangan Perpres (Peta Jalan AI 2026–2029 dan Etika AI) belum terbit per akhir Oktober 2026. Isinya berbasis risiko dan fokus pada hak, pelabelan, dan talenta. Tidak ada ketentuan tentang energi, air, atau pusat data ([CNBC, 30/10/2026](https://www.cnbcindonesia.com/tech/20261030162941-37-781009/ri-atur-ai-sesuai-risiko-komdigi-beberkan-isi-regulasinya); [JDIH Komdigi](https://jdih.komdigi.go.id/berita/view/113)). Karena belum terbit, **ini jendela advokasi yang masih terbuka.**

---

## 3. Peta regulasi

| Aspek | Regulasi | Ketentuan kunci | Celah | Sumber |
|---|---|---|---|---|
| Perizinan usaha | PP 28/2025 (mencabut PP 5/2021); UU 6/2023 Cipta Kerja | OSS-RBA; KBLI 63111/63112 (KBLI 2025: 63101/63102 [CEK]); KKPR sebagai syarat dasar | Tingkat risiko DC belum jelas [CEK]; Wamen Komdigi menyatakan perizinan DC ada di kementerian investasi dan industri, bukan Komdigi, sehingga tidak ada regulator sektoral yang menilai dampak | [BPK](https://peraturan.bpk.go.id/Details/319773/pp-no-28-tahun-2025); [Katadata](https://katadata.co.id/ekonomi-hijau/energi-baru/6af3dfd7de313/komdigi-ingatkan-pentingnya-green-data-center-di-tengah-lonjakan-bisnis-ai) |
| AMDAL | UU 32/2009 jo. UU 6/2023; PP 22/2021; Permen LHK 4/2021 | DC = "besaran multisektor": AMDAL jika lahan ≥ 5 ha atau bangunan ≥ 10.000 m²; air tanah ≥ 50 l/dtk; air sungai/danau ≥ 250 l/dtk; pembangkit ≥ 100 MW | Tidak ada ambang MW atau PUE; pengecualian tenant kawasan (cukup RKL-RPL rinci yang disahkan pengelola kawasan); belum pasti apakah Permen LHK 4/2021 sudah diganti peraturan KLH/BPLH 2025 [CEK] | [Permen LHK 4/2021](https://sdmhutkadipaten.bp2sdm.kehutanan.go.id/wp-content/uploads/2022/05/PERMEN-LHK-NO.-4-TAHUN-2021-PERMENHUT-DAFTAR-USAHA-WAJIB-AMDAL-1_2.pdf); [Hukumonline](https://www.hukumonline.com/klinik/a/sudah-ada-amdal-kawasan-perlukah-perusahaan-punya-amdal-sendiri-lt61c03b03c52ca) |
| Partisipasi | UU 6/2023 (mengubah Pasal 26 UU PPLH) | Partisipasi dalam AMDAL dibatasi pada "masyarakat terkena dampak langsung" | Pemerhati lingkungan dan organisasi seperti WALHI tersingkir dari proses AMDAL; uji materi WALHI ke MK (diajukan Juni 2025) belum ditemukan putusannya [CEK] | [Mongabay](https://mongabay.co.id/2025/06/16/walhi-gugat-uu-cipta-kerja-ke-mahkamah-konstitusi/); [IDN Times](https://www.idntimes.com/news/indonesia/walhi-gugat-13-pasal-uu-ciptaker-ke-mk-soroti-izin-lingkungan-dihapus-00-jkxzp-p7h6xp) |
| Gugatan izin | UU 6/2023 menghapus Pasal 93 UU PPLH | Jalur khusus gugatan PTUN atas izin lingkungan dihapus | Jalur PTUN umum masih ada: PTUN Bandung membatalkan izin lingkungan PLTU Tanjung Jati A (13/10/2022) | [Mongabay](https://mongabay.co.id/2025/05/18/menyoal-putusan-gugatan-pltu-tanjung-jati/) |
| Energi: PLTU captive | Perpres 112/2022 Pasal 3 ayat (4) huruf b | PLTU baru dilarang, kecuali yang terintegrasi dengan industri hilirisasi SDA atau PSN, dengan syarat pengurangan emisi dan beroperasi paling lama sampai 2050 (rumusan syarat [CEK teks]) | DC yang masuk PSN atau berada di kawasan PSN berpotensi masuk pengecualian; draf revisi Perpres disebut memperluas pengecualian; status uji materiil di MA belum jelas [CEK] | [WALHI Sulsel](https://walhisulsel.or.id/4914-ahli-hukum-soroti-kontradiksi-perpres-112-2022-dinilai-legitimasi-pltu-industri-di-tengah-krisis-iklim/); [Betahita](https://betahita.id/news/detail/11601/waspada-revisi-perpres-112-2022-legitimasi-pltu-baru.html?v=1764198027) |
| Energi: pasokan dan EBT | UU 30/2009 jo. UU 6/2023; RUPTL PLN; PP 40/2025 (KEN); RUU EBET | Wilayah usaha (mis. PLN Batam, pengelola kawasan); REC PLN; target EBT di KEN | Tidak ada kewajiban EBT khusus DC; power wheeling dicoret dan RUU EBET mandek di Prolegnas 2026; REC bersifat sertifikat, bukan tambahan pembangkit EBT baru (additionality) | [Bloomberg Technoz](https://www.bloombergtechnoz.com/detail-news/69905/esdm-pastikan-power-wheeling-tidak-masuk-ruu-ebet); [Feedberry](https://feedberry.com/artikel/power-wheeling-ditolak-ruu-ebet-masuk-prolegnas-tanpa-arah); [CNN](https://www.cnnindonesia.com/teknologi/20261006113619-192-1412174/polemik-data-center-jatiluhur-iesr-desak-pemerintah-buat-regulasi-ai) |
| Air | UU 17/2019 SDA; PP 30/2024; izin air tanah dari ESDM | Pasal 8: kebutuhan pokok sehari-hari diprioritaskan di atas yang lain saat air terbatas; Pasal 46 ayat (1) huruf e–f: prioritas BUMN/BUMD, izin untuk swasta "dengan syarat tertentu" dan hanya jika air masih tersedia | Tidak ada kewajiban DC memakai air non-konvensional (daur ulang/SWRO); alokasi ditetapkan per wilayah sungai lewat pola dan rencana SDA yang jarang dibuka ke publik | [pasal.id Ps. 8](https://pasal.id/peraturan/uu/uu-no-17-tahun-2019/pasal-8); [Ps. 46](https://pasal.id/peraturan/uu/uu-no-17-tahun-2019/pasal-46); [UNEP LEAP PP 30/2024](https://leap.unep.org/en/countries/id/national-legislation/government-regulation-no-30-2024-concerning-water-resources) |
| Air: Batam | Rezim KPBPB, BP Batam sebagai pengelola SDA dan SPAM (operator: PT Air Batam Hilir) | BP Batam mengklaim DC di Nongsa memakai air dari Kabil Industrial Estate; DC baru didorong memakai SWRO | Data alokasi saling bertentangan: Mongabay mengutip data BP Batam berupa alokasi 160 l/dtk dari kebutuhan 500 l/dtk, sementara BP Batam membantahnya; belum ada keputusan moratorium | [Mongabay 4/10](https://mongabay.co.id/2026/10/04/proyek-data-center-batam-ancam-sumber-air/); [Kompas](https://regional.kompas.com/read/2026/10/05/213227278/bantah-data-center-penyebab-krisis-air-di-nongsa-bp-batam-air-data-center) |
| Digital | PP 71/2019 (PSTE); rancangan Permen Komdigi tentang standar infrastruktur pusat data | Pasal 20: data PSE lingkup publik wajib dikelola di Indonesia; Pasal 21: PSE privat boleh di luar negeri | Lokalisasi data mendorong permintaan DC tanpa syarat lingkungan; rumus PUE ada di rancangan Permen, tetapi belum ada batas PUE wajib [CEK status] | [Hukumonline](https://www.hukumonline.com/berita/a/mengenal-pokok-pokok-aturan-baru-pp-pste-lt5de653d86d627/?page=all); [Rancangan Permen Komdigi](https://web.komdigi.go.id/resource/ZHJ1cGFsL1JQTSBQRURPTUFOIFBVU0FUIERBVEEucGRm) |
| AI | Rancangan Perpres Peta Jalan AI dan Perpres Etika AI | Pendekatan berbasis risiko, pelabelan konten AI, penilaian mandiri | Tidak ada pasal lingkungan, energi, atau air | [CNBC](https://www.cnbcindonesia.com/tech/20261030162941-37-781009/ri-atur-ai-sesuai-risiko-komdigi-beberkan-isi-regulasinya) |
| Anti-SLAPP | UU PPLH Pasal 66; Putusan MK 119/PUU-XXIII/2025 | MK memperluas perlindungan bagi pejuang lingkungan | Perlindungan bergantung pada aparat penegak hukum | [MKRI](https://www.mkri.id/berita/mk-tegaskan-perlindungan-hukum-bagi-aktivis-lingkungan-23697) |

---

## 4. Tuas hukum untuk WALHI, dari yang termurah/tercepat ke yang terberat

1. **Permohonan informasi publik (UU 14/2008 KIP).** Minta dokumen-dokumen berikut ke PPID yang memegangnya:
   - AMDAL, RKL-RPL rinci, dan AMDAL kawasan, ke DLH, KLH, atau BP Batam/pengelola KEK;
   - persetujuan penggunaan SDA dan izin air tanah, ke Kementerian PU/BBWS/ESDM/BP Batam;
   - KKPR dan PBG, ke pemda;
   - kontrak dan kapasitas sambungan PLN, serta pembelian REC, ke PLN dan ESDM.

   Jika ditolak, ajukan keberatan lalu sengketa ke Komisi Informasi. Pemda/BP Batam/PLN dan BUMN wajib tunduk pada UU KIP. Kontrak PLN kemungkinan akan diklaim sebagai rahasia dagang. Siapkan argumen uji konsekuensi dan kepentingan publik, dan cek tenggat prosedural UU KIP bersama LBH **[CEK]**. Penolakan ini sendiri berguna sebagai bahan kampanye.
2. **Pengaduan administratif dan pengawasan.**
   - Laporkan ke DLH/Gakkum KLH bila ada konstruksi tanpa persetujuan lingkungan atau PBG. Preseden Jatiluhur menunjukkan kepala daerah mau menghentikan proyek.
   - Laporkan ke **Ombudsman RI** atas dugaan maladministrasi, misalnya izin terbit tanpa AMDAL atau layanan air BP Batam/ABH yang buruk bagi warga Sambau.
   - Laporkan ke **Komnas HAM** atas hak atas air dan hak atas lingkungan hidup yang baik dan sehat.
3. **Intervensi dalam proses AMDAL.** Ajukan saran, pendapat, dan tanggapan tertulis pada tahap pengumuman dan konsultasi publik. Dampingi warga terdampak langsung sebagai pihak yang masih punya hak partisipasi setelah UU Cipta Kerja. Desak penilai AMDAL menghitung skenario kekeringan, total beban MW, emisi GRK, dan genset. Preseden Tanjung Jati A menunjukkan bahwa AMDAL yang mengabaikan GRK bisa dibatalkan. Untuk DC di kawasan, tuntut **perubahan AMDAL kawasan** karena skala dan dampaknya berubah (dasar pasal **[CEK PP 22/2021]**).
4. **Mekanisme internasional.**
   - **OECD NCP** di negara asal investor atau penyewa, misalnya NCP AS untuk hyperscaler AS atau Nvidia, atau NCP negara asal pemegang saham operator.
   - **IFC CAO, ADB Accountability Mechanism, atau AIIB PPM**, jika lembaga itu membiayai operator DC atau pembangkitnya. Keterlibatannya harus dicek dulu di portal disclosure masing-masing **[CEK]**.
   - Jalur ini murah dari sisi biaya, tetapi lambat dan berbasis reputasi.
5. **Gugatan TUN atas persetujuan lingkungan, PKKPR, atau izin air.** Ajukan dulu upaya administratif (keberatan/banding administratif), lalu gugat ke PTUN dalam tenggat 90 hari. Preseden yang menguntungkan: PTUN Bandung membatalkan izin lingkungan PLTU Tanjung Jati A pada 13 Oktober 2022 karena AMDAL tidak menghitung GRK. Putusan itu inkracht karena tidak dibanding. Nomor perkaranya kemungkinan 52/G/LH/2022/PTUN.BDG ([ELAW](https://elaw.org/system/files/attachments/publicresource/salinan_putusan_52_G_LH_2022_PTUN_BDG.pdf)) **[CEK]**. Risikonya: PTUN Jakarta (455/G/TF/LH/2024/PTUN.JKT, 28/4/2025) menolak legal standing WALHI karena proyek belum dibangun dan belum ada kerugian konkret ([Mongabay](https://mongabay.co.id/2025/05/18/menyoal-putusan-gugatan-pltu-tanjung-jati/)). **Pelajarannya: gugat setelah izin terbit atau konstruksi berjalan, dan sertakan warga terdampak sebagai penggugat bersama.**
6. **Gugatan organisasi lingkungan (Pasal 92 UU PPLH) di PN.** Tuntutannya berupa tindakan tertentu, misalnya pemulihan, penghentian, atau audit air, tanpa ganti rugi kecuali biaya riil. Preseden: PN Poso mengabulkan sebagian gugatan WALHI Sulteng terhadap PT NNI, SEI, dan GNI, termasuk perintah pemulihan, dalam konteks PLTU captive nikel ([Mongabay, 31/12/2025](https://mongabay.co.id/2025/12/31/catatan-2025-kemenangan-warga-gugat-pltu-di-kawasan-industri-nikel/)). Nomor dan status upaya hukumnya **[CEK]**.
7. **Citizen lawsuit (gugatan warga negara) terhadap pemerintah atas kelalaian mengatur.** Contohnya menuntut regulasi DC, prioritas air, atau penetapan daya dukung. Preseden: gugatan polusi udara Jakarta dikabulkan PN Jakarta Pusat (16/9/2021) dan kasasi pemerintah ditolak MA (2560 K/PDT/2023, 13/11/2023) ([Bisnis](https://kabar24.bisnis.com/read/20231117/16/1715355/jokowi-cs-kalah-kasasi-soal-polusi-udara-jakarta)). Karhutla Kalteng menang di tingkat kasasi (3555 K/Pdt/2018), tetapi dianulir lewat PK pemerintah pada 2022 ([Mongabay](https://news.mongabay.com/2022/11/indonesias-supreme-court-rules-president-widodo-not-liable-in-2015-fires/)). Jalur ini lambat dan eksekusinya lemah, tetapi kuat untuk membingkai isu.
8. **Uji materi.**
   - **HUM ke MA** terhadap Permen atau Perpres, misalnya Permen LHK 4/2021 yang tidak punya ambang khusus DC, Pasal 3 ayat (4) Perpres 112/2022 yang uji materiilnya sudah diajukan WALHI Sulsel dan kawan-kawan **[CEK status]**, atau Perpres AI setelah terbit.
   - **PUU ke MK** terhadap UU, dengan memanfaatkan doktrin partisipasi bermakna dari Putusan MK 91/PUU-XVIII/2020: hak untuk didengar, dipertimbangkan, dan mendapat penjelasan. Ikut perkembangan uji materi WALHI atas klaster lingkungan UU 6/2023.
   - Jalur ini paling berat dan lama, tetapi berdampak sistemik.

Untuk semua jalur: lindungi pejuang lingkungan dengan Pasal 66 UU PPLH dan Putusan MK 119/PUU-XXIII/2025.

---

## 5. Usulan kebijakan konkret

1. **Ambang AMDAL khusus DC.** Revisi Permen LHK 4/2021 atau penggantinya dengan memasukkan **ambang berbasis daya IT/fasilitas**. Contoh: wajib AMDAL untuk DC ≥ 20 MW (angka ilustratif, perlu kajian teknis), UKL-UPL di bawahnya. **Kapasitas genset cadangan dihitung kumulatif.** DC AI ≥ ambang tertentu tetap wajib AMDAL sendiri meskipun berada di kawasan industri/KEK, tidak cukup RKL-RPL rinci.
2. **Kewajiban keterbukaan tahunan** sebagai syarat izin: PUE, WUE, konsumsi listrik (MWh), porsi EBT langsung dibanding REC, emisi cakupan 1–2, volume dan sumber air, dan kapasitas genset. Data diumumkan di portal publik. Masukkan ke Perpres AI dan Permen Komdigi tentang standar pusat data.
3. **Standar efisiensi wajib**: PUE < 1,3 dan pendinginan *closed-loop* atau *waterless* di daerah rawan air, sesuai usulan IESR ([CNN](https://www.cnnindonesia.com/teknologi/20261006113619-192-1412174/polemik-data-center-jatiluhur-iesr-desak-pemerintah-buat-regulasi-ai)).
4. **Larangan PLTU captive dan pembangkit fosil baru untuk DC.** Tegaskan dalam revisi Perpres 112/2022 bahwa DC tidak termasuk pengecualian Pasal 3 ayat (4) huruf b, termasuk bila berstatus PSN atau berada di KEK.
5. **Kewajiban EBT tambahan**, yaitu EBT baru dan langsung, bukan sekadar REC: minimal 35% pada 2030 dan 50% pada 2040 (rujukan IESR). Wajib *additionality* melalui PJBL EBT. Selesaikan RUU EBET dengan skema sewa jaringan (PBJT) yang adil.
6. **Prioritas air ditegakkan.** Turunkan Pasal 8 dan Pasal 46 UU SDA menjadi larangan alokasi air baku PDAM/SPAM atau waduk irigasi untuk pendinginan DC saat neraca air defisit. Wajibkan sumber non-konvensional (daur ulang atau SWRO), dengan AMDAL sendiri untuk pembuangan brine.
7. **Moratorium izin DC baru di daerah krisis air** (Batam/Nongsa, DAS Citarum-Jatiluhur) sampai ada kajian daya dukung dan daya tampung atau KLHS. Ini sejalan dengan tuntutan WALHI dan Trend Asia ([Mongabay](https://mongabay.co.id/2026/10/04/proyek-data-center-batam-ancam-sumber-air/)).
8. **Pulihkan partisipasi.** Kembalikan hak pemerhati lingkungan dalam AMDAL dan jadikan FPIC wajib bagi masyarakat adat dan lokal.
9. **Klausul lingkungan dalam Perpres AI.** Sebelum terbit, sisipkan prinsip "AI berkelanjutan", kewajiban pelaporan jejak energi dan air bagi penyedia model atau komputasi skala besar, dan pengadaan pemerintah yang hanya memakai DC yang memenuhi standar hijau.

---

## 6. Node mind-map (hierarkis)

```
Hukum & Kebijakan DC AI Indonesia
├── Perizinan
│   ├── PP 28/2025 (ganti PP 5/2021) → OSS-RBA, KBLI 63111/63112 (→63101/63102?)
│   ├── KKPR / tata ruang → PSN bisa lolos dari RTRW [CEK]
│   └── PBG (kasus Jatiluhur)
├── Lingkungan
│   ├── AMDAL multisektor: ≥5 ha / ≥10.000 m²
│   ├── Pemicu lain: air tanah ≥50 l/dtk, sungai/danau ≥250 l/dtk, pembangkit ≥100 MW
│   ├── CELAH: tenant kawasan/KEK → RKL-RPL rinci oleh pengelola
│   └── Persetujuan teknis: emisi genset, air limbah, limbah B3 (baterai/e-waste) [CEK]
├── Energi
│   ├── Perpres 112/2022 Ps. 3(4)b → celah PLTU captive PSN
│   ├── Wilayah usaha (PLN Batam, kawasan)
│   ├── RUPTL / KEN PP 40/2025
│   └── REC vs EBT langsung; RUU EBET mandek
├── Air
│   ├── UU 17/2019 Ps. 8 (prioritas pokok), Ps. 46 (izin swasta bersyarat)
│   ├── PP 30/2024; izin air tanah ESDM
│   └── Batam: BP Batam/ABH, Kabil, SWRO, krisis Sambau
├── Digital & AI
│   ├── PP 71/2019 lokalisasi data publik → dorong permintaan DC
│   ├── Rancangan Permen standar pusat data (PUE)
│   └── Rancangan Perpres AI → tanpa pasal lingkungan (jendela advokasi)
├── Cipta Kerja & partisipasi
│   ├── Partisipasi dipersempit, Ps. 93 dihapus
│   ├── MK 91/PUU-XVIII/2020: partisipasi bermakna
│   └── Uji materi WALHI UU 6/2023 [status CEK]
└── Tuas WALHI
    ├── KIP → Ombudsman/Komnas HAM → intervensi AMDAL
    ├── OECD NCP / CAO / ADB AM
    ├── PTUN (Tanjung Jati A 2022 ✓; PTUN Jakarta 2025 ✗ standing)
    ├── Ps. 92 hak gugat organisasi (PN Poso ✓)
    ├── Citizen lawsuit (Polusi Jakarta ✓)
    └── HUM MA / PUU MK
```

---

## 7. Tingkat keyakinan & hal yang perlu dicek ke ICEL/LBH

**Keyakinan tinggi** (dibaca dari teks primer atau dari banyak sumber):
- Ambang multisektor dan pemicu air/pembangkit di Permen LHK 4/2021.
- Pencabutan PP 5/2021 oleh PP 28/2025.
- Kasus Jatiluhur dan krisis air Batam.
- Status rancangan Perpres AI.
- Putusan polusi udara Jakarta, Tanjung Jati A, dan PTUN Jakarta 2025.

**Keyakinan sedang:**
- Pengecualian tenant kawasan beserta nomor pasalnya di PP 22/2021 dan PP 28/2025.
- Bunyi persis syarat Pasal 3 ayat (4) huruf b Perpres 112/2022.
- Kode KBLI 2025.
- Isi Pasal 20–21 PP 71/2019 (sumber sekunder).
- Penghapusan Pasal 93 dan penyempitan Pasal 26 UU PPLH (sumber sekunder dan WALHI).

**Perlu dicek:**
1. Apakah Permen LHK 4/2021 sudah diganti atau diubah oleh peraturan KLH/BPLH 2025–2026.
2. Tingkat risiko KBLI DC di lampiran PP 28/2025.
3. Status putusan uji materi WALHI atas UU 6/2023 di MK dan HUM Perpres 112/2022 di MA, serta isi draf revisi Perpres 112/2022.
4. Apakah genset cadangan dihitung sebagai "pembangkit" untuk ambang AMDAL 100 MW, dan apakah DC wajib izin operasi untuk genset (Permen ESDM tentang usaha ketenagalistrikan).
5. Tenggat konsultasi publik AMDAL dan tata cara keberatan dalam PP 22/2021.
6. Status AMDAL kawasan Nongsa/Kabil, dan apakah ada DC yang berstatus PSN.
7. Status rancangan Permen Komdigi tentang standar pusat data (PUE).
8. Keterlibatan IFC, ADB, atau AIIB dalam pendanaan operator DC di Indonesia.
9. Tenggat prosedural UU KIP.

*Catatan metode:* kuota pencarian web habis sebelum semua butir [CEK] dapat diverifikasi. Teks resmi PP 22/2021 dan Perpres 112/2022 tidak dapat diunduh karena portal JDIH memblokir akses otomatis. Butir-butir di atas sebaiknya diverifikasi manual di peraturan.go.id, JDIH KLH, mkri.id, dan putusan3.mahkamahagung.go.id.

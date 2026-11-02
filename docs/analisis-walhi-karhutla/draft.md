---
lang: id
template: sheet
cols: 2
title: WALHI & Karhutla 2026 — Analisis Media dan Respons Pemerintah
subtitle: Uji dua klaim dengan analisis isi berita (1 Jun – 2 Nov 2026)
korpus: Google News RSS, 2.124 judul unik, 9 aktor
status: Studi rintisan — belum diuji antar-pengode
---
Klaim 1 didukung data: WALHI adalah sumber non-negara paling banyak dimuat di judul berita karhutla. Klaim 2 perlu dua angka, bukan satu: sekitar **50%** narasi WALHI dijawab pemerintah, tetapi hanya sekitar **21%** yang dijawab dengan tindakan nyata.

## A Jawaban untuk dua kalimat Anda {span=2}
```callout ok Kalimat 1 — didukung, dengan catatan
WALHI muncul di **347 judul** berita karhutla (tanpa kanal milik WALHI sendiri). Itu **57%** dari semua judul yang menyebut aktor non-negara, dan lebih banyak dari judul yang menyebut KLH (212). Tren menguat: dari 1–3 judul per minggu (Jun–Jul) menjadi 37–70 judul per minggu (Okt).
```
```callout warn Kalimat 2 — isi titik-titiknya dengan dua angka
Usulan rumusan: "Rata-rata **50%** narasi WALHI mendapat respons pemerintah, tetapi hanya **21%** yang berupa tindakan substantif (skor responsivitas tertimbang **27%**)." Rentang sensitivitas: respons 50–58%, substantif 21–25%. Sampel kecil (14 tuntutan), jadi angka ini indikatif.
```

## B Metodologi yang dipakai
```flow LR
(Definisi isu & kata kunci) -> [Kumpulkan korpus: Google News RSS per minggu]
[Kumpulkan korpus: Google News RSS per minggu] -> [Hapus duplikat judul & kanal milik aktor]
[Hapus duplikat judul & kanal milik aktor] -> *[Isu 1: share of voice & tren]
[Hapus duplikat judul & kanal milik aktor] -> [Isu 2: inventaris narasi WALHI]
[Isu 2: inventaris narasi WALHI] -> *[Kode respons pemerintah skala 0–4]
*[Isu 1: share of voice & tren] -> {Uji reliabilitas α ≥ 0,80?}
*[Kode respons pemerintah skala 0–4] -> {Uji reliabilitas α ≥ 0,80?}
{Uji reliabilitas α ≥ 0,80?} --> [Laporan final]
```
| Kerangka | Dipakai untuk |
|---|---|
| Analisis isi kuantitatif (Krippendorff 2018; Neuendorf 2017) | Unit, kategori, reliabilitas antar-pengode |
| Agenda-setting (McCombs & Shaw 1972) | Volume dan tren isu |
| Primary definers (Hall dkk. 1978) | Siapa yang dikutip sebagai sumber |
| Framing (Entman 1993) | Diagnosis, penyebab, solusi dalam narasi WALHI |
| Responsivitas simbolik vs substantif (Walgrave & Van Aelst 2006) | Skala respons 0–4 |

Skala respons: **0** tidak ada respons, **1** ditolak / kontra-narasi, **2** diakui secara retoris, **3** tindakan parsial, **4** diadopsi penuh.

## C Isu 1 — Tren judul berita karhutla per minggu
```chart line
           | WALHI | Greenpeace | KLH | Pantau Gambut
1 Jun      | 3  | 0  | 4  | 0
8 Jun      | 2  | 0  | 4  | 1
15 Jun     | 0  | 0  | 4  | 0
22 Jun     | 1  | 3  | 0  | 0
29 Jun     | 1  | 0  | 8  | 0
6 Jul      | 3  | 0  | 5  | 1
13 Jul     | 3  | 0  | 0  | 0
20 Jul     | 3  | 0  | 4  | 0
27 Jul     | 3  | 0  | 0  | 0
3 Agu      | 2  | 0  | 2  | 1
10 Agu     | 2  | 1  | 5  | 1
17 Agu     | 22 | 4  | 23 | 3
24 Agu     | 13 | 0  | 24 | 1
31 Agu     | 8  | 7  | 23 | 0
7 Sep      | 18 | 2  | 14 | 0
14 Sep     | 25 | 0  | 17 | 1
21 Sep     | 26 | 3  | 6  | 3
28 Sep     | 16 | 4  | 14 | 4
5 Okt      | 51 | 4  | 15 | 0
12 Okt     | 37 | 19 | 16 | 2
19 Okt     | 38 | 92 | 3  | 0
* 26 Okt   | 70 | 9  | 21 | 4
```
Lonjakan pertama 17 Agu: debat WALHI vs Menteri LH di Konsultasi Nasional LH, Pekanbaru. Puncak Greenpeace 19 Okt: isu kabut asap lintas batas. Sejak Sep, WALHI melampaui KLH hampir tiap minggu.

## D Isu 1 — Siapa yang paling banyak muncul di judul
```chart bar horizontal unit=" judul"
BNPB                 | 676
Kemenhut             | 624
* WALHI              | 347
KLH                  | 212
Greenpeace           | 148
Akademisi IPB        | 84
Pantau Gambut        | 22
Madani Berkelanjutan | 9
Auriga               | 2
```
Di antara aktor non-negara (612 judul), WALHI memegang **57%**; tanpa akademisi, **66%**. Jangkauan: 155 media berbeda memuat WALHI di judul, Greenpeace 89.

## E Isu 2 — Narasi WALHI dan respons pemerintah {span=2}
| # | Narasi / tuntutan WALHI (tanggal) | Alamat | Respons pemerintah yang ditemukan | Skor |
|---|---|---|---|---|
| 1 | 1.351 titik api di 15 konsesi (21 Agu) | Menteri LH | Menteri membantah: "kebakaran tidak terjadi pada wilayah konsesi"; Gakkum: "akan kami dalami" | no 1 Ditolak |
| 2 | Verifikasi & sanksi 372 perusahaan (15 Sep) | Kemenhut | Disambut sebagai bahan verifikasi; 5 izin dicabut (4 ada di daftar WALHI); 32 izin dibekukan | ok 3 Parsial |
| 3 | Sama, instrumen UU 32/2009 | KLH | Tidak ada tanggapan publik atas laporan | no 0 |
| 4 | Sama, evaluasi & cabut HGU | ATR/BPN | Tidak ada tanggapan publik atas laporan | no 0 |
| 5 | Data 262 perusahaan ke Presiden (Sep) | Setneg | "Belum ada tanggapan" per 12 Sep | no 0 |
| 6 | Pidana korporasi sampai pemilik manfaat | Polri, Kemenhum | Tersangka korporasi naik 4 → 13 → 20; 23 izin direkomendasikan dicabut; data BO diserahkan ke APH | ok 3 Parsial |
| 7 | Umumkan nama korporasi tersangka (23 Okt, 1 Nov) | Polri | Presiden: nama diumumkan "pada saatnya"; WALHI masih menuntut per 1 Nov | warn 2 Retoris |
| 8 | Tetapkan bencana nasional | Presiden | Menko Polkam: belum berencana | no 1 Ditolak |
| 9 | Kritik label "terorisme ekologi" (19 Sep) | Presiden | Tidak ada tanggapan langsung | no 0 |
| 10 | Layanan kesehatan gratis & evakuasi korban asap | Pusat | Tidak ditemukan di korpus | no 0 |
| 11 | Cabut izin konsesi terbakar berulang | Kemenhut, Presiden | Presiden: cabut setelah 2 pelanggaran; izin dibekukan & dicabut sebagian | ok 3 Parsial |
| 12 | Pulihkan gambut, larang sawit/akasia di bekas terbakar | KLH, Kemenhut | Tidak ditemukan di korpus | no 0 |
| 13 | Gugatan Pasal 72 UU Kehutanan atas 148 PBPH (26 Okt) | Menhut | Belum ada; baru 7 hari | no 0 |
| 14 | Penyebab utama tata kelola, bukan El Niño | Pemerintah | Menhut: "99% kebakaran ulah manusia" | warn 2 Retoris |

Tidak ada narasi dengan skor 4. Tindakan pada narasi 6 dan 11 juga menyusul arahan Presiden, jadi skor 3 berarti **searah**, bukan bukti bahwa WALHI penyebabnya.

## F Isu 2 — Tingkat respons pemerintah
```chart bar horizontal unit=%
                    | Unit 14 tuntutan | Unit 12 narasi
* Ada respons (≥1)  | 50 | 58
Tindakan nyata (≥3) | 21 | 25
Indeks tertimbang   | 27 | 31
```
Indeks tertimbang = jumlah skor ÷ skor maksimum (4 × jumlah unit).
Distribusi 14 tuntutan: skor 0 = 7, skor 1 = 2, skor 2 = 2, skor 3 = 3, skor 4 = 0. "Unit 12 narasi" menggabungkan tuntutan 2–4 menjadi satu laporan.

## G Kelemahan yang harus Anda tutup sebelum dipublikasi {span=2}
```callout err Jangan pakai satu angka tanpa definisi
"Tingkat respons" bisa 21% atau 58% tergantung definisi. Tulis definisi dan unit hitung di catatan kaki, atau angka Anda mudah dipatahkan.
```
- **"Rujukan" ≠ volume.** Data ini membuktikan visibilitas. Untuk "rujukan", tambahkan kode: apakah media memakai data WALHI sebagai fakta, atau hanya mengutip kritiknya?
- **Angka WALHI tidak konsisten di media.** Luas terbakar dikutip 33.837 ha (Kalimantan, Jan–Jul), 107.649 ha (nasional, s.d. 27 Jul), dan 895.000 ha (2026). SiPongi mencatat 202.004 ha untuk Jan–Jul. Periode dan wilayah berbeda, tapi pembaca melihatnya sebagai kontradiksi.
- **Atribusi.** Pemerintah bisa bertindak karena arahan Presiden, Polri, atau tekanan Malaysia–Singapura, bukan karena WALHI. Pisahkan "respons langsung" (menyebut WALHI) dan "konvergensi kebijakan".
- **Korpus belum lengkap.** Google News tidak memuat TV, cetak, dan media sosial. Kueri BNPB (6 minggu) dan Kemenhut (4 minggu) mencapai batas 100 hasil, jadi angka keduanya adalah batas bawah.
- **Satu pengode.** Uji ulang dengan 2 pengode pada ≥ 10% sampel; target α Krippendorff ≥ 0,80.

## H Alat scraping yang cocok untuk tahap berikutnya {span=2}
| Kebutuhan | Alat | Kecocokan | Catatan |
|---|---|---|---|
| Temukan berita per kata kunci & tanggal | Google News RSS (dipakai di sini) | ok Cocok | Gratis, bisa `after:` / `before:`; maks 100 hasil per kueri, jadi pecah per minggu |
| Temukan & hitung tren lintas media | GDELT DOC 2.0 API | ok Cocok | Mendukung bahasa Indonesia, mode timeline volume; standar riset media |
| Ambil isi artikel dari URL | fhamborg/news-please | warn Bisa | Rujukan akademik (Hamborg dkk. 2017), Apache-2.0; repo sudah diarsipkan |
| Ambil isi artikel dari URL | trafilatura (di luar topik GitHub tsb.) | ok Disarankan | Masih dirawat; ekstraksi teks dan tanggal terbaik di uji banding |
| Scraper khusus media Indonesia | nichsedge/indoscraping | no Belum | 6 situs saja; tidak ada filter kata kunci atau tanggal untuk berita |
| Google News berbayar | oxylabs, Decodo | no Tidak perlu | Butuh proxy berbayar; RSS sudah cukup |

Skrip pengumpul dan data mingguan ada di `docs/analisis-walhi-karhutla/` (`collect_gnews.py`, `headline_mentions_weekly.csv`).

Sumber utama:

- [CNN Indonesia 23/10](https://www.cnnindonesia.com/nasional/20261023094532-20-1418680/walhi-greenpeace-desak-pemerintah-buka-data-korporasi-pemicu-karhutla)
- [Betahita 16/9](https://www.betahita.id/berita/12369/372-perusahaan-terduga-karhutla-dilaporkan-ke-3-kementerian)
- [AFU 21/8](https://afu.id/nasional/walhijumhur-ribut-soal-data-karhutla-di-lahan-konsesi-sawit-dan-tambang-gakkum-klh-malah-segel-perusahaan-sawit)
- [Mongabay 21/10](https://mongabay.co.id/2026/10/21/berbagai-kalangan-desak-kabut-asap-dan-karhutla-jadi-bencana-nasional/)
- [NU Online 21/9](https://nu.or.id/nasional/walhi-soroti-narasi-terorisme-ekologi-dalam-penanganan-karhutla-0953D)
- [Wartatrans 14/10](https://wartatrans.com/walhi-ungkap-372-perusahaan-terindikasi-terkait-karhutla-2026-sebanyak-52-berafiliasi-dengan-malaysia-dan-singapura/)
- [Kompas.id](https://www.kompas.id/artikel/walhi-serahkan-data-262-perusahaan-terkait-karhutla-ditunggu-tindakan-presiden)
- [RMOL 29/10](https://rmol.id/read/2026/10/29/726627/20-korporasi-resmi-tersangka-karhutla-empat-perusahaan-asing)
- [Katadata 26/10](https://katadata.co.id/ekonomi-hijau/ekonomi-sirkular/6adf3e14bbd89/walhi-desak-menhut-jalankan-uu-kehutanan-demi-warga-terdampak-kebakaran-hutan)

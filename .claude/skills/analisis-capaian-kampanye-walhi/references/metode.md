# Kerangka Metode Analisis Capaian Kampanye

## Daftar isi
1. Logika dasar
2. Pemberitaan
3. Respons pemerintah
4. Atribusi bidang dan PJ
5. Validasi dan kalibrasi
6. Dasar teori
7. Kalimat metode untuk laporan

## 1. Logika dasar

Kampanye dinilai dari rantai: **rilis (output) → pemberitaan (jangkauan) → respons pemerintah (outcome)**.

- Unit analisis utama adalah **rilis**: satu rilis = satu kasus dengan tuntutan dan lembaga yang dituju.
- Pemberitaan menunjukkan pesan sampai ke publik, tetapi bukan capaian. Jangan menulis "capaian" untuk jumlah berita.
- Capaian kampanye = **respons pemerintah**, terutama **tindakan nyata** yang dapat diverifikasi.
- Bila hasil berbeda karena definisi, tulis angkanya bersama definisi (mis. "79% direspons; 21% berujung tindakan").

## 2. Pemberitaan

Dua lapis, jangan dicampur:

**a. Pemberitaan umum per isu** (gambaran visibilitas WALHI)
- Korpus: semua item Google News yang memuat "walhi" (jendela 2 hari agar tidak kena batas 100 hasil) + kueri per isu.
  Kueri Google mencocokkan judul atau isi, sehingga item dari kueri "walhi …" berarti WALHI disebut di judul/isi.
- Buang item dari kanal WALHI sendiri. Buang akhiran " - Nama Media" sebelum pencocokan kata kunci.
- Pemilahan isu per judul, kata kunci isu + **aturan lokus**: laut, pesisir, perairan, pulau kecil (bukan pulau besar),
  kasus pesisir dari rilis (Batu Beriga, Pantura, Rempang, Kawasi, BOPPJ, Batam) → Pesisir & Laut.
  Multi-label diperbolehkan; laporkan irisan (mis. tambang × pesisir).
- Laporkan: berita (judul atau isi), berita dengan WALHI di judul, jumlah media berbeda.
- **Kliping manual tim bidang** (mis. spreadsheet tim PELA) digabung dengan hasil otomatis untuk bidang itu, tanpa duplikat
  (cocokkan judul ≥ 0,75 dan URL), hanya untuk berita dalam periode. Bersihkan dulu baris ganda dan berita di luar periode.
  Beri tanda di gambar bahwa bidang itu memakai gabungan, karena bidang lain hanya metode otomatis. Laporkan juga recall
  metode otomatis terhadap kliping (Agu–Okt 2026: 27 dari 43 berita PELA tertangkap korpus, 21 terklasifikasi Pesisir).

**b. Pemberitaan per rilis** (jangkauan kampanye)
- Rentang H-1 s.d. H+14 dari tanggal rilis.
- Tiga jalur pencarian: kata kunci kasus + "walhi"; kata kunci kasus saja; nama jejaring + kasus.
  Jalur keempat: nama pengkampanye (termasuk salah ketik), untuk wawancara dan talkshow di luar rilis.
- Isi berita dibaca (trafilatura). Situs yang memblokir pembaca otomatis **tidak ditembus**; pakai tanda indeks Google.
- Kode sikap: memuat pesan WALHI/jejaring · kontra-narasi · konteks · tidak relevan (dibuang).
- Jumlah per rilis bisa tumpang tindih antar-rilis dengan kasus sama; untuk total, pakai berita unik.

## 3. Respons pemerintah

- Jendela: dari tanggal rilis sampai akhir periode + 2 hari. Respons sebelum rilis tidak dihitung.
- Skor = respons **tertinggi** dari lembaga yang dituju atau yang berwenang (skala di `skala_respons.md`).
- Respons kepada **jejaring** yang membawa tuntutan sama dihitung (bentuk "ke_jejaring").
- **Konvergensi**: tindakan searah yang tidak menyebut WALHI tetap dihitung, tetapi ditandai. Di laporan tulis
  "tuntutan WALHI diikuti langkah pemerintah", bukan "dipenuhi karena WALHI".
- **Tindakan unik**: satu tindakan (mis. pencabutan izin) dihitung sekali, lalu dikaitkan ke rilis yang tuntutannya disentuh.
- **Generik**: skor 3 yang buktinya hanya tindakan umum (mis. penyegelan karhutla untuk rilis FOLU) tidak dihitung
  sebagai tindakan nyata isu tersebut.
- Respons pemerintah asing dan rilis berstatus draf dicatat terpisah.
- Kontra-narasi dari pihak ketiga (aktivis pro-proyek, ormas) dicatat sebagai respons tidak langsung, tanpa skor.

Ukuran yang dilaporkan per bidang: jumlah rilis bertuntutan spesifik, % ada respons (skor ≥ 1), % tindakan nyata
(skor ≥ 3, kecocokan inti/sebagian), bentuk respons terbanyak, median hari ke respons, tindakan unik.

## 4. Atribusi bidang dan PJ

- Acuan jumlah rilis: tabel rilis laporan divisi. Rilis publik di luar daftar itu dicatat terpisah.
- Pengkampanye bidang dikutip/narahubung → bidangnya. Hanya pimpinan/Hukum → bidang pemilik topik, tidak dikreditkan.
- Untuk rilis yang penuturnya tidak tercatat, cari penutur di isi berita; kalau tetap tidak jelas, tandai "?" dan tanyakan.
- Nama ditulis sesuai ejaan yang dipakai tim (lihat `roster.md`), bukan sesuai media.

## 5. Validasi dan kalibrasi

- Pemeriksa adversarial: agen kedua per kelompok bidang mencari respons yang terlewat dan membantah skor.
- Penyunting memeriksa semua skor ≥ 3 dan setiap perubahan skor dari pemeriksa.
- Kalibrasi recall: cocokkan hasil dengan kliping tim (mis. PELA) dan hitungan manual nama pengkampanye;
  laporkan persentase yang tertangkap dan sebab utama yang terlewat.
- Reliabilitas: untuk publikasi eksternal, kode ulang ≥ 10% rilis oleh pengode kedua; target α Krippendorff ≥ 0,80.

## 6. Dasar teori

- Analisis isi kuantitatif: Krippendorff (2018), *Content Analysis* (4th ed.); Neuendorf (2017), *The Content Analysis Guidebook*.
- Agenda-setting: McCombs & Shaw (1972). Kapasitas ruang berita yang terbatas: Hilgartner & Bosk (1988).
- Agenda-building dan respons simbolik vs substantif: Cobb & Elder (1972); Walgrave & Van Aelst (2006).
- Ekstraksi teks berita: Barbaresi (2021), trafilatura.

## 7. Kalimat metode untuk laporan (sesuaikan angka)

"Respons pemerintah dihitung dari tanggal tiap rilis sampai [tanggal], dari lembaga yang dituju atau berwenang,
termasuk respons kepada jejaring yang membawa tuntutan yang sama. Setiap respons dinilai pada skala 0–4 dan
diperiksa ulang oleh pemeriksa terpisah. Pemberitaan dicari per rilis (1 hari sebelum sampai 14 hari sesudah rilis)
melalui kata kunci kasus, nama jejaring, dan nama pengkampanye; isi berita dibaca untuk mendeteksi sebutan WALHI
meski tidak ada di judul."

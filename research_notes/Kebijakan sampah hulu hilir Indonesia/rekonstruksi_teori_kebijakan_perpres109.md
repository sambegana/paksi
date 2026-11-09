# Rekonstruksi teori kebijakan Perpres 109/2025 (PSEL)

> Catatan penyusun, 9 November 2026. Bahan untuk bagian analisis policy brief "Hulu Dibiarkan, Hilir Dibakar". Catatan ini tidak menambah data baru. Isinya menyusun ulang data dari catatan lain ke dalam satu kerangka. Label verifikasi mengikuti catatan sumbernya.

## 1. Kerangka: lima tema dan lima metode analisis kebijakan

Sumber: buku Hariadi Kartodihardjo, bab Pendahuluan hlm. 19–20 (foto dari Paksi). Buku itu mengutip Leroy & Nelissen (2000) melalui Runhaar dkk. (2008). Teks Runhaar belum dibaca langsung. Makalah terkait: Runhaar, Dieperink & Driessen (2006), "Policy Analysis for Sustainable Development: the Toolbox for the Environmental Social Scientist", *Int. J. Sustainability in Higher Education* 7: 34–56.

| Tema | Pertanyaan inti | Metode yang menjawab (Tabel 1 buku) |
|---|---|---|
| 1. Isi (content) | Tujuan, definisi masalah, dan kesahihan asumsi | Rekonstruksi teori kebijakan, analisis pemangku kepentingan, analisis wacana |
| 2. Proses | Pengaruh aktor, peran ilmu pengetahuan, kepentingan siapa yang masuk | Analisis pemangku kepentingan, analisis wacana |
| 3. Organisasi | Domain kebijakan yang terlibat, hubungan pusat–daerah | Rekonstruksi teori kebijakan, analisis pemangku kepentingan |
| 4. Dampak | Tercapai atau tidak, efek samping, apakah penilaian pemangku kepentingan berbeda dari pemerintah | Rekonstruksi, pemangku kepentingan, penilaian dampak, analisis wacana |
| 5. Konteks | Pengaruh politik, ekonomi, sosial-budaya, dan kebijakan internasional | Analisis pemangku kepentingan, analisis wacana |

Catatan kritis:
- Baris "analisis biaya-manfaat" di Tabel 1 buku itu kosong. Ini kemungkinan besar salah cetak. Cek sumber asli sebelum mengutip tabelnya.
- **Sutton (1999)**, dikutip di halaman yang sama: masalah pelaksanaan biasanya tidak dianggap bagian dari masalah kebijakan, dan kegagalannya dialamatkan ke "orang-orang di lapangan". Ini mekanisme yang perlu dibongkar dalam isu PSEL. Kegagalan PLTSa dijelaskan "karena sampah warga basah". Padahal yang keliru adalah asumsi desain kebijakannya.
- Kerangka ini netral soal kuasa, jadi pakai sebagai senjata empiris. Bingkai kritisnya (keadilan ekologis, Bacchi WPR, ekologi politik) tetap dari luar kerangka ini.
- Biaya-manfaat konvensional menjumlahkan semua untung dan rugi. Untuk keadilan ekologis, pakai versi **distribusi biaya** (siapa membayar, siapa menanggung), bukan neraca bersih.

## 2. Teori kebijakan versi pemerintah (direkonstruksi)

Teori kebijakan adalah rantai sebab-akibat dan asumsi yang harus benar agar kebijakan mencapai tujuannya. Rantai di bawah disusun dari teks dan pernyataan resmi.

```
[Masalah yang didefinisikan pemerintah]
Sampah menumpuk di TPA; "saldo sampah" harus nol pada 2029; TPA open dumping ditutup.
        │
        ▼
A1  Sampah kota bisa dibakar menjadi listrik secara andal (bahan bakar yang cukup kalori).
        │
        ▼
A2  Pemda mampu menjamin pasokan ≥1.000 t/hari ke satu PSEL (aglomerasi) selama 30 tahun.
        │
        ▼
A3  Harga USD 0,20/kWh + kewajiban beli PLN + Danantara cukup menarik investor
    dan "lebih murah" bagi pemda karena tipping fee (BLPS) dihapus.
        │
        ▼
A4  Persetujuan lingkungan maksimal 2 bulan (otomatis disetujui) tidak mengorbankan
    perlindungan kesehatan dan lingkungan.
        │
        ▼
A5  PSEL mengurangi ±33.000 t/hari (22,48% timbulan nasional, 2029) dan,
    bersama "teknologi lain" (RDF, pirolisis), menuntaskan krisis sampah.
        │
        ▼
[Tujuan] Sampah "terkelola" 100% pada 2029 + energi terbarukan + pemenuhan target iklim (NDC).
```

**Asumsi tersembunyi**, tidak tertulis tetapi diperlukan agar rantai ini masuk akal:
- **H1.** Masalah sampah adalah masalah hilir (volume yang harus dimusnahkan), bukan masalah hulu (desain dan produksi kemasan). Produsen tidak muncul di rantai ini sama sekali.
- **H2.** Pembakaran dihitung sebagai "terkelola" dan "energi terbarukan", sejajar dengan pengurangan.
- **H3.** Wilayah di luar ±60 kab/kota PSEL akan terselesaikan dengan "solusi lain" yang tidak dirinci.

## 3. Uji tiap mata rantai terhadap bukti

| Asumsi | Bukti yang mematahkan | Sumber di repo | Tema |
|---|---|---|---|
| A1 Sampah bisa dibakar andal | Sekitar 40% sampah adalah sisa makanan. Wamen LH: kadar air sampah di Putri Cempo >70%, padahal mesin mensyaratkan <20%. Dari 12 proyek PLTSa, baru 2 yang beroperasi. Putri Cempo hanya mengolah ±80 t/hari dari potensi 380–400 t | `pltsa_pasokan_kalor.md` | Isi, Dampak |
| A2 Pasokan ≥1.000 t/hari selama 30 tahun | Solo hanya memasok 400 t/hari dari kebutuhan 530 t. Putri Cempo menerima sampah dari Bali (kajian WALHI 2024, sekunder). Ps. 17(2)e mewajibkan pemda membayar **kompensasi** bila pasokan kurang. Menteri LH sendiri: bila pemilahan berhasil, PSEL hanya kebagian 15–20% sampah. Artinya kebijakan ini **menghukum daerah yang berhasil memilah** | `pltsa_pasokan_kalor.md`, `putri_cempo_bali_dan_abu.md`, `status_regulasi_dan_pembanding.md` (koreksi denda→kompensasi) | Isi, Organisasi |
| A3 Insentif harga "murah" | Biayanya tidak hilang, hanya pindah dari APBD ke PLN dan APBN (selisih harga di atas BPP selama 30 tahun). Pengurangan dan komposting tetap dibiayai APBD yang hanya rata-rata 0,53% (anjuran 3%). Secara relatif, pembakaran jadi lebih murah bagi pemda daripada pengurangan. Insentifnya keliru | `matriks_celah_kebijakan.md` §15 | Isi, Dampak |
| A4 Izin kilat tetap aman | Amdal 2 bulan dengan persetujuan otomatis (Ps. 18, sekunder). CEMS hanya untuk >1.000 t/hari dan tanpa dioksin. Klasifikasi abu belum jelas. Abu Putri Cempo disimpan di ruang terbuka. PM2.5 di Benowo hingga 8x pedoman WHO | `matriks_celah_kebijakan.md` §8, `putri_cempo_bali_dan_abu.md` | Dampak, Proses |
| A5 PSEL menuntaskan krisis | Target 22,48% timbulan berarti ±78% sisanya tidak tersentuh. Desa hampir tidak terlayani: 5,7% rumah tangga diangkut, 80,8% membakar (SKI 2023). RDF dan pirolisis memindahkan pembakaran ke PLTU dan tanur semen | `data_bakar_sampah_wilayah.md`, `matriks_celah_kebijakan.md` §9 | Dampak, Organisasi |
| H1 Produsen absen | Baru 28 dari 842 produsen melaporkan peta jalan P.75. Pasal 15 UU 18/2008 tidak ditegakkan. Unilever hanya 15% kemasan fleksibel yang dapat dipakai ulang, didaur ulang, atau dikomposkan | `peta_kebijakan.md`, `verifikasi_produsen_global.md` | Isi, Proses |
| H2 Bakar = terkelola = terbarukan | Bertentangan dengan hierarki UU 18/2008 (pengurangan dulu). Pasokan minimal 30 tahun berbenturan dengan target pengurangan. Pembakaran plastik adalah pembakaran bahan bakar fosil | `matriks_celah_kebijakan.md` §19 | Isi, Konteks |
| H3 "Solusi lain" | ±470 kab/kota di luar PSEL tanpa rincian | `status_regulasi_dan_pembanding.md` (Antara, 17 Sep 2026) | Organisasi |

**Simpulan rekonstruksi.** Rantai ini patah di dua titik paling hulu. Pertama, A1: sampahnya tidak cocok untuk dibakar. Kedua, H1: produsen tidak ada di dalam rantai. Karena titik pertama patah, kebijakan ini butuh A2, yaitu memaksa pasokan, dan A3, yaitu memindahkan biaya ke uang publik. Hasilnya, insentif berbalik melawan pengurangan. Menurut Sutton, kegagalan ini nanti akan dialamatkan ke "sampah warga yang tidak dipilah". Padahal sistem pemilahan tidak pernah dibangun negara, dan desain kemasan tidak pernah ditagih ke produsen.

## 4. Peta lima tema untuk isu PSEL: sudah dan belum

| Tema | Sudah ada | Masih kosong |
|---|---|---|
| Isi | Uji asumsi A1–A5 dan H1–H2 (tabel di atas) | Teks resmi Perpres 109 Ps. 18 dan pasal transisi belum terbaca langsung |
| Proses | Danantara, sponsor dan mitra Paviliun COP31, "tanpa partisipasi publik bermakna" (WALHI, Jan 2026) | Siapa yang menyusun Perpres 109 dan draf pengganti P.75. Suara pemulung dan warga sekitar PSEL dalam proses |
| Organisasi | Kompensasi dari pemda, aglomerasi, 7 kementerian/lembaga tanpa sektor pemimpin | Pembagian kewenangan pengangkutan sampai ke desa (kabupaten vs desa vs Dana Desa) |
| Dampak | Putri Cempo, Benowo, data SKI | Data lapangan sendiri. Semuanya masih sekunder |
| Konteks | COP31, Pasal 6 Persetujuan Paris, perjanjian plastik global | Ekonomi politik: kenapa pembakaran menarik bagi negara (proyek investasi, PSN, PLN, Danantara) |

## 5. Pemakaian di policy brief

- Figur utama: diagram rantai A1→A5 dengan tanda "patah" di A1 dan H1. Tiap tanda diberi satu angka bukti.
- Jangan pakai istilah "rekonstruksi teori kebijakan" di brief. Cukup tulis "Logika PSEL dan di mana ia patah".
- Rumusan yang harus dihindari: "sampah kita belum dipilah" (menyalahkan warga). Gantinya: "negara belum membangun sistem pengumpulan terpilah, tetapi sudah membeli mesin yang hanya bekerja bila sampah terpilah".

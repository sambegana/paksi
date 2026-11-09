# Pembanding: Indonesia vs negara berpenduduk setara (untuk wawancara Kontan)

Disusun 9 Nov 2026. Label: **[TERVERIFIKASI]** = dibaca langsung dari dataset atau makalah primer. **[OLAHAN]** = hitungan penyusun dari angka primer; jangan dikutip sebagai angka resmi. **[TIDAK DITEMUKAN]**.

## Sumber
1. **World Bank, *What a Waste 3.0* Country Dataset** (versi 4, diperbarui 11 Mar 2026). Berkas `What_a_Waste_3.0_COUNTRY_Dataset_&_Codebook.xlsx` diunduh dari https://datacatalog.worldbank.org/search/dataset/0039597, lembar "Country dataset" dan "Codebook". [TERVERIFIKASI]
2. **Cottom, Velis dkk. 2024, "A local-to-global emissions inventory of macroplastic pollution", *Nature* 633:101–108**, DOI 10.1038/s41586-024-07758-6. Dibaca dari PDF repositori White Rose (https://eprints.whiterose.ac.uk/id/eprint/225341). Tahun data 2020. [TERVERIFIKASI]

## Tabel 1. World Bank What a Waste 3.0

Tahun data berbeda per negara. Satuan cakupan pengumpulan juga berbeda (% berat, % rumah tangga, % penduduk). **Jangan susun peringkat dari tabel ini.**

| Indikator | Indonesia | Amerika Serikat | Pakistan | Nigeria | Brasil | Bangladesh |
|---|---|---|---|---|---|---|
| Penduduk (tahun data) | 280,0 jt | 333,7 jt | 241,7 jt | 216,3 jt | 209,9 jt | 167,0 jt |
| Kelompok pendapatan | UMIC | HIC | LMIC | LMIC | UMIC | LMIC |
| Tahun data timbulan | 2023 | 2018 | 2022 | 2021 | 2022 | 2021 |
| Timbulan sampah kota (juta t/thn) | 55,4 | 265,3 | 48,5 | 44,5 | 81,8 | 30,5 |
| kg/orang/hari | 0,54 | 2,18 | 0,55 | 0,56 | 1,07 | 0,50 |
| Plastik (% berat) | **19,2%** | 12,2% | 9,7% | 8,4% | 16,8% | 17,6% |
| Sisa makanan (% berat) | 39,7% | 21,6% | 57,0% | 49,8% | 45,3% | 19,3% |
| Plastik per orang/thn [OLAHAN] | ±38 kg | ±97 kg | ±19 kg | ±17 kg | ±65 kg | ±32 kg |
| Cakupan pengumpulan | 62,5% (berat) | 100% (penduduk) | 23,6% (RT) | 20% (berat) | 93% (berat) | 80,6% (berat) |
| Tidak terkumpul (% berat) | 37,5% | – | – | – | 7,0% | 19,4% |
| Daur ulang (% berat sampah kota) | 8,9% | 24,1% | – | – | 1,6% | 3,1% |
| Status EPR menurut World Bank | "Mandatory", "legally-binding" | Mandatory | Mandatory | Mandatory | Mandatory | Voluntary |

Catatan khusus Indonesia (dari Codebook):
- Sumber angka timbulan, cakupan, dan daur ulang adalah **komunikasi email SIPSN ke World Bank (11 Sep 2024)**, data 2023. Angka 55,4 Mt jauh di atas angka SIPSN publik (25–33 Mt, lihat `rantai_hulu_hilir.md`). Selisihnya belum dijelaskan.
- Daur ulang 8,9% terdiri dari **informal 3.908.316 t + formal 1.002.069 t**. Artinya **±80% daur ulang tercatat dikerjakan sektor informal** [OLAHAN]. Ini bukti kuantitatif untuk argumen "subsidi tersembunyi pemulung".
- Rincian sampah tidak terkumpul (73,9% dibakar) memakai **BPS 2014**. Lebih baik pakai SKI 2023 (`data_bakar_sampah_wilayah.md`).
- Status EPR Indonesia dikodekan World Bank sebagai **wajib dan mengikat secara hukum** berdasarkan P.75/2019. Lihat "Jebakan" di bawah.
- Porsi plastik fleksibel Indonesia: [TIDAK DITEMUKAN] di dataset.
- Plastik per orang [OLAHAN] = kg/orang/hari × % plastik × 365. Hasilnya bergantung pada mutu data komposisi tiap negara.

## Tabel 2. Cottom dkk. 2024 (emisi polusi plastik ke lingkungan, 2020)

| Negara | Emisi (Mt/thn) [rentang] | Peringkat absolut |
|---|---|---|
| India | 9,3 [6,5–12,7] | 1 |
| Nigeria | 3,5 [2,6–4,6] | 2 |
| **Indonesia** | **3,4 [2,5–4,3]** | **3** |
| Tiongkok | 2,8 [2,1–3,7] | 4 |

- AS, Pakistan, Brasil, Bangladesh: angka per negara [TIDAK DITEMUKAN] di teks makalah (hanya ada di SD_03 Dryad, 1,45 GB, tidak dibuka).
- Global 52,1 Mt/thn, 57% dibakar terbuka, 43% sampah utuh (debris).
- "Despite high-income countries (HICs) having higher plastic waste generation rates (0.17 kg cap−1 day−1), none are ranked in the top 90 polluters, because most have 100% collection coverage and controlled disposal."
- Penulis **sengaja tidak menghitung ekspor sampah plastik**: "we may have underestimated plastic waste emissions from some HICs because we deliberately excluded plastic waste exports". Ekspor dari 10 eksportir OECD teratas ke negara non-OECD dan Turki turun dari hampir 5,4 Mt/thn (2017) menjadi kurang dari 1,7 Mt/thn (2022).
- **Plastik fleksibel**: "Flexible plastic debris has a higher probability of being emitted into the environment in the Global South compared with rigid debris (mean ratio 56:44) ... In the Global North (for example, Northern America), the opposite is true (mean ratio 33:67)." Ini relevan untuk argumen saset.
- Pengakuan keterbatasan: "notable data gaps on solid waste management in rural communities exist".

## Membaca dengan kerangka risiko BNPB (R = H × V / C)

Kerangka risiko BNPB: Risiko = Ancaman × Kerentanan / Kapasitas. Usulan pemetaan:
- **Ancaman (H)**: volume dan jenis plastik yang masuk ke pasar, terutama kemasan fleksibel/saset. Penentunya keputusan produsen.
- **Kerentanan (V)**: warga tanpa layanan (desa: 80,8% membakar), pemulung, dan pemukiman di sekitar TPA/insinerator.
- **Kapasitas (C)**: layanan pengumpulan dan pengolahan, ditambah regulasi yang ditegakkan (EPR, larangan, guna ulang).

Yang ditunjukkan data:
1. AS memiliki H tertinggi (±97 kg plastik/orang/thn, olahan) tetapi C hampir 100%, sehingga emisi domestiknya rendah. Sebagian kapasitas itu berupa **pengiriman risiko ke negara Selatan lewat ekspor**, yang tidak dihitung Cottom.
2. Brasil adalah pembanding paling jujur: sama-sama UMIC, porsi sisa makanannya mirip (45% vs 40%), tetapi cakupan pengumpulannya 93% vs 62,5% (sama-sama % berat). Kesenjangan C, bukan H.
3. Porsi plastik di sampah Indonesia (19,2%) **tertinggi** di antara enam negara ini. Jadi H Indonesia tidak kecil. Rumuskan sebagai intensitas kemasan, bukan perilaku konsumsi.
4. Indonesia setara Nigeria dalam emisi absolut (3,4 vs 3,5 Mt), padahal pendapatan per kapita dan cakupan pengumpulan Indonesia lebih tinggi.

## Jebakan

- **Kerangka R = H × V / C mengundang solusi "tambah kapasitas"**, artinya tambah infrastruktur hilir. Itu persis argumen PSEL. Pengaman: (a) tegaskan bahwa berbeda dari gempa, **ancamannya diproduksi**, sehingga H bisa dan harus diturunkan di sumbernya; (b) kapasitas dalam kerangka BNPB juga mencakup regulasi dan kelembagaan, bukan hanya fasilitas; (c) tanyakan siapa yang membiayai C. Insinerator juga menaikkan V (abu B3, asap) bagi warga di sekitarnya.
- **World Bank mencatat EPR Indonesia "wajib dan mengikat".** Kalau wartawan mengecek, posisi "Indonesia belum punya EPR wajib" terlihat salah. Rumusan yang tepat: kewajiban ada sejak UU 18/2008 dan P.75/2019, tetapi isinya hanya kewajiban menyusun peta jalan, tanpa iuran dan tanpa sanksi, dan baru 28 dari 842 produsen yang menjalankan dan melaporkannya.
- **Pembanding "penduduk setara" lemah secara analitis.** Yang menentukan adalah pendapatan dan sistem pengelolaan. Pakai paling banyak satu atau dua pembanding, bukan tabel liga.
- Jangan menyebut Indonesia "peringkat 2 dunia" (Jambeck 2015, data 2010). Versi terbaru (Cottom 2024): peringkat 3, dan peringkat model bisa berubah antarversi.

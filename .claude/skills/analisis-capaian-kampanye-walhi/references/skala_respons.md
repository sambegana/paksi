# Skala dan Aturan Pengodean Respons

| Skor | Kategori | Definisi | Contoh (Agu–Okt 2026) |
|---|---|---|---|
| 0 | Tidak ada respons | Tidak ditemukan pernyataan atau tindakan lembaga yang dituju setelah rilis | Gugatan Pasal 72 ke Menhut |
| 1 | Ditolak | Lembaga membantah klaim atau menolak tuntutan secara terbuka ("proyek tetap jalan", "tidak benar") | KKP: PSN tambak Pantura tetap jalan |
| 2 | Diakui/dijanjikan | Mengakui isu, berjanji, "akan dikaji", tanpa tindakan yang bisa diverifikasi | Wamenko Pangan janji perketat pengawasan PSN Merauke |
| 3 | Tindakan parsial | Tindakan terverifikasi, searah dengan tuntutan, tetapi sebagian | Kemenhut cabut 5 izin; 4 ada di daftar WALHI |
| 4 | Dipenuhi | Tuntutan dipenuhi seluruhnya | (belum pernah terjadi) |

## Aturan

1. Catat respons **tertinggi** dari lembaga yang dituju atau atasannya/instansi berwenang.
2. Hanya respons **setelah** tanggal rilis dan sebelum akhir jendela. Tindakan yang sudah berproses sebelum rilis
   (mis. panel Singapura dimulai 23 Okt, rilis 29 Okt) tidak dihitung sebagai respons atas rilis itu.
3. Respons kepada jejaring atas tuntutan yang sama dihitung, bentuk "ke_jejaring".
4. Tindakan searah tanpa menyebut WALHI/jejaring tetap dihitung, `konvergensi = true`.
5. Ragu antara dua skor → pilih yang lebih rendah dan tulis alasannya.
6. Skor 3–4 wajib punya bukti dari sumber resmi (situs lembaga, dokumen, pengumuman pejabat) **atau** dua media berbeda.
   Kalau tidak, turunkan ke 2.
7. Tentukan **kecocokan** untuk skor ≥ 3: inti (menjawab inti tuntutan), sebagian, atau generik (tindakan umum
   yang tidak menyentuh tuntutan). Generik tidak dihitung sebagai tindakan nyata isu itu.
8. Kontra-narasi pihak ketiga: catat di `berita_kontra`, jangan diberi skor.
9. Jangan mengarang. Tidak ditemukan → skor 0, tulis "Tidak ditemukan".
10. Lembaga daerah (mis. DPRD) yang meneken tuntutan bersama WALHI/warga, menjalankan proses revisi regulasi (pansus, revisi perda),
    atau menyampaikan tuntutan itu secara resmi ke kementerian = **tindakan parsial (3)**, bukan sekadar janji. Contoh: DPRD Babel
    untuk Batu Beriga (berita acara 21 Sep, audiensi ke KKP 9 Okt, seluruh fraksi mendukung 22 Okt). Tetap catat bahwa lembaga
    pusat (KKP/ESDM) belum menjawab. Konfirmasi dengan tim bidang; mereka sering tahu perkembangan yang belum diberitakan.

## Bentuk respons (kolom `bentuk`)

`langsung_ke_walhi` (menyebut WALHI atau diucapkan di forum WALHI) · `ke_jejaring` · `umum_tanpa_menyebut` · `tindakan`

## Format keluaran per rilis (JSON)

```json
{"id": "R16", "tuntutan_ringkas": "...", "lembaga_dituju": "KKP", "berita_kasus": 16, "berita_memuat_walhi": 13,
 "berita_jejaring_tanpa_walhi": 0, "berita_kontra": 9, "penutur_terdeteksi": ["Mida Saragih", "Teo Reffelsen"],
 "jejaring_terdeteksi": ["KOMPI"], "respons": [{"lembaga": "KKP", "tanggal": "2026-09-24", "bentuk": "langsung_ke_walhi",
 "isi": "...", "url": "..."}], "skor": 1, "hari_ke_respons": 0, "konvergensi": false, "keyakinan": "tinggi", "catatan": "..."}
```

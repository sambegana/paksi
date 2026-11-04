# Struktur Data Antar-Langkah

## tabel_rilis.json (keluaran ekstrak_tabel_rilis.py)
`{"baris": [["Agustus", "Judul", "Pesisir & Laut", "Mida Saragih"], ...], "kemungkinan_duplikat": [[i, j, "judul"]]}`

## rilis_base.csv (diisi manual/semi-otomatis)
Kolom: `id, tanggal (YYYY-MM-DD atau YYYY-MM), judul_singkat, sumber_daftar, status, bidang_topik, pj_bidang,
pj_penutur, dasar_penentuan (kutipan/narahubung | topik), sifat (isu bidang | momen lembaga), suara_pimpinan,
jenis_tuntutan (spesifik | umum), tuntutan_utama, lembaga_dituju, kueri_kasus (dipisah "|"), jejaring (dipisah koma),
masuk_per_isu (ya | ya (disuarakan pimpinan/Hukum…) | catatan (…) | tunda (…)), daftar_divisi (ya | tidak)`

## kode_respons.json (keluaran agen pengode + pemeriksa)
Daftar objek per rilis seperti di `skala_respons.md`, ditambah `skor_final`, `alasan_verifikasi`, `keyakinan_final`.

## keputusan.json (keputusan penyunting)
```json
{"keluarkan": {"R37": "pemerintah asing"}, "gabung": {"R28": "P10"},
 "kecocokan": {"R07": "inti", "R20": "generik"}, "skor": {"P01": 0}}
```

## tindakan_unik.csv
`kode, tanggal, lembaga, tindakan, jenis, rilis_terkait (dipisah ";"), bukti, atribusi`

## Keluaran gabung_respons.py
- `respons_final.csv` — satu baris per rilis (skor, kecocokan, penutur, berita, bukti, status dihitung/catatan).
- `ringkasan_per_bidang.json` — per bidang: rilis, ada_respons, ditolak, dijanjikan, tindakan_parsial, dipenuhi,
  tindakan_nyata, tindakan_generik, pct_ada_respons, pct_tindakan_nyata, median_hari_ke_respons, berita_memuat_walhi.

## pemberitaan.json (keluaran hitung_pemberitaan.py)
`{"semua": {isu: n}, "judul_walhi": {isu: n}, "media": {isu: n}, "unik_judul_walhi": n, "unik_semua": n, "irisan_pesisir": {...}}`

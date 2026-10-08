# Rencana Penamaan & Penandaan Arsip Foto/Video — Drive Delta Kapuas

Status: **pipeline siap, belum dijalankan terhadap Drive.** Belum ada satu file pun yang diubah.
Kode & petunjuk menjalankan: [`tools/arsip_dk/README.md`](../tools/arsip_dk/README.md).

Keputusan terkini: Delta Kapuas = **Shared Drive**; eksekusi lewat skrip Drive API (opsi B) yang dijalankan di laptop pemilik kredensial.

## 0. Prasyarat yang belum terpenuhi

| Prasyarat | Status | Yang dibutuhkan |
|---|---|---|
| Akses ke Google Drive | Belum ada (connector Google Drive belum tersambung di sesi ini) | Sambungkan connector, **atau** sediakan kredensial Drive API (lihat §5) |
| Ingatan percakapan lama (pemindahan Sampan Kalimantan → Delta Kapuas) | Tidak bisa diakses dari sesi ini | Tempel ringkasan/isi percakapan lama, atau cukup verifikasi langsung isi Drive |
| Kepastian pemindahan sudah terjadi | Belum terverifikasi | Audit isi folder Delta Kapuas (§2 Fase 1) |

## 1. Prinsip desain

Mengikuti praktik standar manajemen aset digital (Library of Congress, *File Naming Best Practices*; IPTC Photo Metadata Standard; Dublin Core):

1. **Nama file = identitas stabil, bukan tempat semua tag.** Nama file hanya memuat elemen yang tidak akan berubah: proyek, tanggal, kategori utama, nomor unik, deskripsi singkat.
2. **Tag lengkap disimpan di kolom *Description* Drive + indeks spreadsheet.** Pencarian Drive (`fullText`) ikut membaca kolom Description, jadi mengetik "mangrove" atau "bekantan" tetap ketemu tanpa nama file sepanjang kalimat.
3. **Kosakata terkendali.** Kode kategori diambil dari daftar tetap (§3), bukan dikarang per file. Tanpa ini, pencarian akan pecah: "mangrove", "bakau", "hutan-bakau".
4. **Tanggal ISO 8601 (YYYYMMDD)** agar urut kronologis otomatis.
5. **Tanpa spasi/karakter khusus**; huruf kecil untuk deskripsi, pemisah `-` di dalam elemen dan `_` antar elemen.
6. **Bisa dibatalkan.** Setiap rename tercatat (file ID, nama lama, nama baru) sehingga bisa di-*rollback*.

## 2. Format nama

```
DK_<YYYYMMDD>_<KAT>_<NNNNN>_<deskripsi-singkat>.<ext>
```

Contoh:

```
DK_20240315_MGV_00042_akar-tunjang-tepi-sungai.jpg
DK_20240316_KGT_00043_penanaman-bibit-mangrove.mp4
DK_00000000_SNG_00044_perahu-di-muara.jpg      ← tanggal tidak diketahui
```

| Elemen | Isi | Sumber |
|---|---|---|
| `DK` | Kode proyek Delta Kapuas | Tetap |
| `YYYYMMDD` | Tanggal pengambilan | EXIF / metadata video Drive; `00000000` jika tidak ada (jangan pakai tanggal upload — menyesatkan) |
| `KAT` | Satu kategori utama (§3) | Analisis visual + review manusia |
| `NNNNN` | Nomor urut unik global, tidak pernah dipakai ulang | Dibuat otomatis |
| `deskripsi` | 2–5 kata, Bahasa Indonesia | Analisis visual + review manusia |

Jenis file (foto/video) sudah terbaca dari ekstensi, tidak perlu kode tambahan.

## 3. Kosakata kategori (usulan awal — wajib dikoreksi pemilik arsip)

| Kode | Kategori | Contoh tag di Description |
|---|---|---|
| MGV | Mangrove / vegetasi pesisir | bakau, nipah, rhizophora, akar-tunjang, bibit |
| SNG | Sungai, muara, perairan | kapuas, anak-sungai, pasang-surut |
| KMP | Kampung, permukiman, infrastruktur | rumah-panggung, dermaga, jalan |
| MSY | Masyarakat / potret orang | warga, nelayan, anak-anak |
| KGT | Kegiatan / acara | rapat, pelatihan, penanaman, survei |
| SWT | Satwa | bekantan, burung, ikan, kepiting |
| PRH | Perahu / transportasi air | sampan, speedboat, kapal |
| UDR | Foto/video udara (drone) | lanskap, tutupan-lahan |
| MTP | Mata pencaharian / ekonomi | perikanan, pertanian, kebun |
| DOK | Dokumen / layar / papan informasi | peta, spanduk, tangkapan-layar |
| LLN | Lain-lain (perlu ditinjau) | — |

Satu file = satu kategori utama di nama; kategori sekunder masuk ke Description.

## 4. Alur kerja

**Fase 1 — Audit (tanpa mengubah apa pun).**
Daftar semua file di Delta Kapuas: ID, nama, ukuran, tipe, tanggal EXIF, checksum MD5. Hasil: jumlah file, porsi foto vs video, file **duplikat** (MD5 sama — mungkin muncul dari proses pemindahan), dan file yang tertinggal di Sampan Kalimantan.

**Fase 2 — Pilot 30–50 file.**
- Foto: dianalisis dari thumbnail resolusi tinggi Drive (tanpa mengunduh file asli).
- Video: ambil 3–5 *keyframe* (ffmpeg) + metadata; isi audio **tidak** dianalisis kecuali diminta transkripsi.
- Hasil: tabel usulan (nama baru + tag + tingkat keyakinan). **Anda meninjau dan mengoreksi**; kosakata §3 disesuaikan.

**Fase 3 — Penandaan penuh (dry-run).**
Seluruh file diproses → spreadsheet indeks `DK_indeks_arsip`. Baris berkeyakinan rendah ditandai untuk ditinjau. Belum ada rename.

**Fase 4 — Eksekusi setelah persetujuan.**
Rename + isi kolom Description via Drive API, per batch. Log rollback disimpan. File ID tidak berubah, jadi tautan berbagi Drive tetap berfungsi.

**Fase 5 — Verifikasi.**
Uji pencarian (mis. "mangrove", "bekantan", "2024") dan cocokkan dengan indeks.

## 5. Opsi teknis akses Drive

| Opsi | Kelebihan | Kekurangan |
|---|---|---|
| **A. Connector Google Drive claude.ai** | Mudah disambungkan | Kemampuan rename/ubah Description dan membaca video belum pasti — harus dicek setelah tersambung |
| **B. Skrip Drive API di container ini** (disarankan untuk eksekusi) | Bisa rename, isi Description, baca metadata EXIF/MD5, ekstrak keyframe video, log rollback; skrip tersimpan di repo ini dan bisa diulang | Butuh kredensial (OAuth token atau *service account* yang diberi akses ke folder) disimpan sebagai *environment secret* |

## 6. Batasan yang harus diterima sejak awal

- **Identifikasi visual tidak sama dengan pengetahuan lapangan.** "Mangrove" dan "sungai" bisa dikenali andal; spesies spesifik, nama desa, nama orang, dan nama kegiatan **tidak bisa** ditebak dari gambar. Tanpa GPS di EXIF, lokasi harus diisi dari Anda (mis. dari nama folder lama).
- **Foto orang:** nama orang tidak akan ditebak. Jika arsip memuat anak-anak atau warga yang tidak memberi izin publikasi, pertimbangkan tag `izin-belum-jelas`.
- **Rename memutus referensi berbasis nama** (mis. proyek Premiere/CapCut, salinan di Drive Desktop yang dipakai aplikasi lain). Tautan Drive tidak terpengaruh.

## 7. Keputusan yang dibutuhkan dari pemilik arsip

1. Delta Kapuas itu *Shared Drive* atau folder di My Drive? Siapa pemiliknya?
2. Perkiraan jumlah file dan total ukuran?
3. Struktur folder sekarang dipertahankan atau ikut ditata ulang?
4. Kosakata §3 sudah sesuai konteks kerja Anda? Kategori apa yang kurang?
5. Opsi akses A atau B?

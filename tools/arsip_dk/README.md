# arsip_dk — penamaan & penandaan foto/video Shared Drive Delta Kapuas

Pipeline 5 tahap. Tahap 1–4 **hanya membaca** Drive. Drive baru berubah di tahap 5,
itu pun hanya untuk baris yang Anda setujui, dan semua perubahan bisa dibatalkan.

```
audit ─► pratinjau ─► analisis (Claude) ─► susun ─► [Anda meninjau CSV] ─► terapkan
                                                                          └► pulihkan (bila perlu)
```

Hasil akhirnya untuk setiap file:

- **Nama baru:** `DK_20240315_MGV_00042_akar-tunjang-tepi-sungai.jpg`
- **Description di Drive** (ikut terbaca oleh kotak pencarian Drive):
  ```
  [arsip-dk]
  kode: DK-00042
  kategori: MGV (Mangrove & vegetasi pesisir)
  kategori lain: SNG
  tag: bakau, mangrove, akar-tunjang, pasang-surut, tepi-sungai
  keterangan: Akar tunjang mangrove di tepi sungai saat air surut.
  tanggal: 20240315 (sumber: exif)
  nama asli: IMG_20240315_101500.jpg
  folder asal: Kegiatan 2024/Survei Maret
  [/arsip-dk]
  ```
  Teks Description lama yang ditulis orang tidak dihapus; blok ini ditambahkan di bawahnya.

Kode kategori ada di `arsip_dk/vocab.json`. Edit file itu **sebelum** tahap analisis
jika ada kategori yang kurang atau tidak cocok dengan pekerjaan Anda.

---

## 1. Persiapan di laptop

Butuh Python 3.10+ dan ffmpeg (untuk video).

```bash
# macOS:   brew install python ffmpeg
# Windows: winget install Python.Python.3.12 Gyan.FFmpeg
cd tools/arsip_dk
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Kredensial — dua kunci yang berbeda

### a. Google (untuk membaca & mengganti nama file di Drive)

**API key Google biasa (berawalan `AIza...`) tidak bisa dipakai**: kunci itu tidak bisa
membuka Shared Drive privat. Yang dibutuhkan salah satu dari:

**Pilihan 1: OAuth desktop (paling sederhana untuk satu orang).**
1. console.cloud.google.com → buat/pilih project → *APIs & Services* → *Enable APIs* → aktifkan **Google Drive API**.
2. *OAuth consent screen*: tipe External, status *Testing*, tambahkan email Anda sebagai *test user*.
3. *Credentials* → *Create credentials* → *OAuth client ID* → tipe **Desktop app** → unduh JSON.
4. Simpan sebagai `tools/arsip_dk/credentials.json`. Saat pertama dijalankan, browser terbuka untuk login.

**Pilihan 2: Service account (cocok jika dijalankan otomatis/di server).**
1. Di project yang sama: *IAM & Admin* → *Service Accounts* → buat → *Keys* → *Add key* → JSON.
2. Buka Shared Drive Delta Kapuas → *Manage members* → tambahkan email service account
   (`...@...iam.gserviceaccount.com`) sebagai **Content manager**. Untuk perbandingan dengan
   Sampan Kalimantan, tambahkan juga di drive itu sebagai **Viewer**.
3. `export GOOGLE_APPLICATION_CREDENTIALS=/path/ke/kunci.json` (Windows: `set GOOGLE_APPLICATION_CREDENTIALS=...`)

### b. Anthropic (untuk analisis gambar oleh Claude)

Buat API key di console.anthropic.com → *API keys*, lalu:
```bash
export ANTHROPIC_API_KEY=sk-ant-...      # Windows: set ANTHROPIC_API_KEY=sk-ant-...
```

Jangan commit file kunci. `.gitignore` sudah mengecualikan `credentials.json`, `token_*.json`,
dan folder `data_arsip/`.

## 3. Menjalankan

```bash
# 1) Audit: hitung file, cari duplikat, dan cek apakah pemindahan dulu sudah lengkap
python -m arsip_dk audit --drive "Delta Kapuas" --bandingkan "Sampan Kalimantan"

# 2–3) PILOT dulu: 50 file
python -m arsip_dk pratinjau --batas 50
python -m arsip_dk analisis --batas 50

# 4) Susun usulan nama
python -m arsip_dk susun
```

Buka `data_arsip/usulan_nama.csv` (sebaiknya impor ke Google Sheets). Periksa kolom
`kategori`, `deskripsi_singkat`, dan `tag`, lalu buka beberapa file lewat kolom `link`. Jika
hasil pilot memuaskan, **sesuaikan `vocab.json` bila perlu**, lalu proses semuanya:

```bash
python -m arsip_dk pratinjau          # lanjut dari yang belum
python -m arsip_dk analisis           # lanjut dari yang belum
python -m arsip_dk susun
```

### Meninjau CSV

| status | Arti | Yang Anda lakukan |
|---|---|---|
| `ok` | Keyakinan tinggi, tanpa catatan | Cek acak beberapa saja |
| `review` | Keyakinan sedang/rendah, kategori LLN, duplikat, atau ada catatan | Periksa; ubah ke `ok` bila benar |
| `belum` | Belum dianalisis (pratinjau/analisis gagal) | Jalankan ulang tahap 2–3 |
| `lewati` | Isi sendiri untuk file yang tidak boleh diubah namanya | — |

Edit kolom `kategori`, `deskripsi_singkat`, `tag`, `keterangan`, `lokasi`, dan `tanggal` sesukanya.
**Jangan edit `nama_baru` atau `nomor`**: nama baru dihitung ulang dari kolom-kolom tadi saat diterapkan.
Simpan sebagai CSV di `data_arsip/usulan_nama.csv` (koma atau titik koma sama-sama terbaca).

### Menerapkan

```bash
python -m arsip_dk terapkan              # simulasi: tampilkan rencana, tidak mengubah apa pun
python -m arsip_dk terapkan --jalankan   # minta konfirmasi "YA", lalu mengubah Drive
```

Setiap perubahan dicatat di `data_arsip/log/terapkan_<waktu>.csv`. Untuk membatalkan:

```bash
python -m arsip_dk pulihkan data_arsip/log/terapkan_<waktu>.csv
```

File yang namanya sudah diubah orang lain sejak audit akan dilewati, tidak ditimpa.

## 4. Biaya & waktu (perkiraan, akan terlihat pasti setelah pilot)

Satu pratinjau ±1568 px ≈ 2.500 token gambar + ±1.300 token konteks; keluaran ±500–1.000 token.

| Model (`--model`) | Perkiraan per 1.000 file |
|---|---|
| `claude-opus-5-5` (default) | ±US$30 |
| `claude-sonnet-5-5` | ±US$15 |
| `claude-haiku-5-5` | ±US$1 |

Tahap analisis mencetak biaya sebenarnya di akhir. Saran: jalankan pilot 50 file dengan Opus
dan Haiku, bandingkan kualitasnya di CSV, baru pilih model untuk sisa arsip. `--ukuran 1092`
memangkas token gambar kira-kira separuh.

## 5. Batasan yang perlu diketahui

- **Privasi:** pratinjau foto/video dikirim ke Anthropic API untuk dianalisis. Kolom `ada_anak`
  menandai file berisi anak-anak supaya izin publikasinya bisa dicek.
- **Isi video:** yang dianalisis hanya 6 cuplikan bingkai; suaranya tidak.
- **Tanggal:** urutan sumbernya EXIF → metadata video → pola nama file. Tanggal upload Drive
  sengaja tidak dipakai karena itu tanggal pemindahan, bukan tanggal pengambilan. Tanpa tanggal: `00000000`.
- **Nama orang, desa, acara, spesies** tidak ditebak dari gambar. Lokasi hanya diisi jika ada di
  nama folder/nama file, GPS, atau tulisan yang terbaca.
- **Rename tidak memutus tautan Drive** (ID file tetap), tetapi proyek editing video
  (Premiere/CapCut/DaVinci) yang memanggil file berdasarkan nama/path bisa kehilangan media.
- Token akses Google untuk video dikirim ke ffmpeg lewat argumen perintah, jadi bisa terlihat
  oleh pengguna lain di komputer yang sama selama proses berjalan. Aman untuk laptop pribadi.

## Uji

```bash
python -m unittest discover -s tests -v
```

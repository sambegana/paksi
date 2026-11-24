---
jenis: panduan
---

# Pengkampanye Urban & Tata Ruang — vault pengetahuan

Knowledge base kerja kampanye urban dan tata ruang berkeadilan, dalam format **vault Obsidian**.
Isinya disaring dari sesi-sesi Claude yang terpisah (data center, sampah, tata ruang, air,
sungai, hutan kota, iklim, advokasi), lalu disambungkan lewat entitas yang sama.

Titik masuk: [[00-indeks]] → [[benang-merah]].

## Membuka di Obsidian

```bash
git clone -b claude/modest-mendel-rfoxrt https://github.com/sambegana/paksi.git
```

Di Obsidian: *Open folder as vault* → pilih `paksi/pengkampanye-urban-tata-ruang`.
Buka **Graph view** untuk melihat sambungan. Filter `path:isu` atau `path:konsep` membantu
saat grafnya terlalu ramai. Plugin *Obsidian Git* bisa dipakai untuk menarik pembaruan.

## Struktur

| Folder / berkas | Isi |
|---|---|
| `benang-merah.md` | Sintesis lintas isu: 8 pola, klaim yang jangan dipakai, celah riset |
| `isu/` | Hub per isu: ringkasan, sambungan ke isu lain, daftar entitas, angka kunci |
| `konsep/` `regulasi/` `aktor/` `tempat/` | Satu entitas per catatan. Bagian `Dari [[sesi]]` menunjukkan sesi mana yang memakainya. Entitas dengan **×N** di hub muncul di N sumber |
| `angka-kunci.md` | Semua angka + sumber + status (`diverifikasi-di-sesi` / `belum-diverifikasi` / `dikoreksi`) |
| `argumen-kampanye.md`, `pertanyaan-terbuka.md` | Bahan kerja per sumber |
| `sesi/` | Log tiap sesi Claude (sumber), ditulis sekali |
| `modul/` | Daftar modul HTML; isinya diimpor setelah final |
| `_meta/` | Catatan tentang sistem vault ini sendiri |
| `_templat/`, `_alat/` | Templat catatan; skrip `periksa.py`, `gabung.py`, `hub.py`, status `sinkron.json` |

## Cara kerja bersama Claude

Skill `/catat-sesi` di repo ini:
- **`/catat-sesi`** di akhir sesi: saring sesi itu ke vault dan sambungkan ke entitas yang ada.
- **`/catat-sesi impor`**: tarik sesi-sesi Claude baru yang belum masuk, cukup sesekali
  (misalnya mingguan). Claude menunjukkan daftar kandidat dulu sebelum membaca.
- **`/catat-sesi modul`**: impor isi modul HTML, hanya setelah kamu bilang modulnya final.
- **`/catat-sesi periksa`**: cek tautan rusak dan catatan yatim.

Agar sesi baru bisa membaca dan menulis vault, sesi itu harus dibuka dengan repo
`sambegana/paksi`, dan perubahan harus di-push.

## Konvensi
- Nama berkas huruf kecil dengan `-`. Tautan memakai nama berkas tanpa `.md`.
- Klaim ditandai: diverifikasi / belum diverifikasi / dikoreksi / kata pengguna.
- Repo ini **publik** atas keputusan pemilik. Tidak ada rahasia (kunci API, kata sandi) dan
  data pribadi warga biasa (no. HP, alamat, NIK). Rekan internal ditulis perannya.

## Keterbatasan yang perlu diketahui
- Catatan entitas adalah **gabungan otomatis** dari beberapa sesi: tiap sesi punya bagian
  sendiri, belum disunting menjadi satu teks utuh. Kontradiksi antarsesi dibiarkan terlihat,
  bukan dipilih diam-diam.
- Sebagian sesi (terutama advokasi iklim urban 5 Nov) berbasis pengetahuan model tanpa sumber
  yang dibuka. Klaimnya ditandai `belum-diverifikasi`.
- Alat pembaca sesi kadang menyisipkan potongan sesi lain saat membaca halaman lama. Agen yang
  menemukannya sudah membuangnya, tetapi kontaminasi kecil di log lain tidak bisa dikesampingkan.

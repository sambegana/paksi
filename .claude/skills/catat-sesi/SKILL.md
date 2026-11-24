---
name: catat-sesi
description: Menyaring sesi kerja saat ini menjadi catatan pengetahuan di vault/ (gaya Obsidian, saling tertaut dengan [[wikilink]]), supaya sesi berikutnya bisa melanjutkan tanpa mengulang konteks. Pakai saat pengguna mengetik /catat-sesi, minta "catat", "simpan pembelajaran", "masukkan ke knowledge", atau di akhir sesi yang menghasilkan keputusan, temuan, atau pekerjaan setengah jadi. Juga untuk "/catat-sesi periksa" (cek tautan rusak & catatan yatim).
---

# catat-sesi

Sesi cloud tidak punya ingatan: container dibuang, transkrip hilang. **Satu-satunya ingatan
lintas sesi adalah `vault/` yang di-commit ke git.** Tugas skill ini: memindahkan yang
penting dari percakapan ke sana — tersaring, bukan disalin.

Baca `vault/README.md` sekali untuk konvensi lengkap. Ringkasnya ada tiga jenis catatan:

| Folder | Jenis | Isinya | Sifat |
|---|---|---|---|
| `vault/sesi/` | Log sesi (episodik) | Apa yang dikerjakan, diputuskan, dan **belum selesai** | Ditulis sekali, tidak diubah |
| `vault/konsep/` | Catatan konsep (permanen) | Satu gagasan yang berlaku lintas proyek, dengan dasar/sumbernya | Diperbarui terus |
| `vault/keputusan/` | Catatan keputusan (ADR) | Konteks → keputusan → konsekuensi → alternatif yang ditolak | Tidak diubah; kalau berubah, buat yang baru dan tandai yang lama `digantikan` |

## Mode default: catat sesi ini

1. **Baca dulu yang sudah ada**: `vault/00-indeks.md`, lalu `ls vault/konsep vault/keputusan`.
   Jangan membuat catatan konsep kedua untuk gagasan yang sudah punya catatan — perbarui yang lama.
2. **Saring percakapan.** Ambil hanya yang lolos uji ini: *"Kalau sesi depan tidak tahu hal ini,
   apakah ia akan salah langkah, mengulang kerja, atau bertanya hal yang sudah dijawab?"*
   Kandidat kuat: keputusan beserta alasannya, preferensi/batasan pengguna, fakta tentang
   sistem/data yang mahal ditemukan ulang, jalan buntu (apa yang dicoba dan kenapa gagal),
   pekerjaan setengah jadi dan langkah berikutnya.
   Buang: obrolan, langkah mekanis yang sudah tercermin di commit, isi file yang bisa dibaca langsung.
3. **Tulis log sesi** di `vault/sesi/YYYY-MM-DD-<topik-singkat>.md` dari `vault/_templat/sesi.md`.
   Tanggal = tanggal hari ini. Bagian **Belum selesai / langkah berikutnya** wajib diisi
   (tulis "tidak ada" bila memang tuntas) — inilah yang paling dibutuhkan sesi berikutnya.
4. **Promosikan** gagasan yang berlaku di luar sesi ini ke `konsep/` (templat `konsep.md`), dan
   keputusan yang mengikat ke `keputusan/` (templat `keputusan.md`). Log sesi menaut ke
   keduanya; jangan menduplikasi isinya di log.
5. **Tautkan.** Setiap catatan baru minimal punya satu `[[tautan]]` keluar dan disebut dari
   `vault/00-indeks.md`. Nama tautan = nama file tanpa `.md`.
6. **Periksa**: `python3 vault/_alat/periksa.py` harus keluar tanpa tautan rusak.
7. **Commit** di branch kerja dengan pesan `vault: catat sesi <topik>`. Push hanya jika
   pengguna meminta atau aturan sesi mewajibkan — tanpa push, catatan hilang bersama container,
   jadi **ingatkan pengguna** bila belum di-push.
8. Laporkan ke pengguna: daftar catatan yang dibuat/diubah, satu baris per catatan.

## Mode `periksa`

Jalankan `python3 vault/_alat/periksa.py`, laporkan tautan rusak, catatan yatim (tidak ditaut
siapa pun), dan catatan tanpa frontmatter. Perbaiki yang jelas; tanyakan yang ambigu.

## Aturan mutu

- **Jujur soal sumber.** Bedakan yang *diverifikasi* (dijalankan, dibaca dari file/data) dari
  yang *diasumsikan* atau *dikatakan pengguna*. Tulis eksplisit bila belum diverifikasi.
- **Jangan menyimpan rahasia**: API key, token, kredensial, isi `.env`, data pribadi pihak ketiga.
- Bahasa Indonesia, kalimat utuh, padat. Catatan konsep harus bisa dipahami tanpa membaca log sesinya.
- Jangan menulis ulang log sesi lama. Koreksi ditulis di log sesi baru yang menaut ke yang lama.

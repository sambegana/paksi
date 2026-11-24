---
jenis: panduan
---

# Vault pengetahuan

Ingatan bersama lintas sesi Claude. Folder ini adalah **vault Obsidian**: buka Obsidian →
*Open folder as vault* → pilih folder `vault/` dari clone repo ini. Graph view dan backlink
langsung jalan karena semua tautan memakai `[[wikilink]]`.

Titik masuk: [[00-indeks]].

## Kenapa ada di repo

Sesi Claude Code di cloud berjalan di container sementara. Saat sesi selesai, container dan
transkripnya hilang; sesi baru tidak bisa membaca percakapan lama. Yang bertahan hanya yang
di-commit ke git. Lihat [[sesi-cloud-tanpa-ingatan]] dan [[vault-pengetahuan-di-repo]].

## Tiga jenis catatan

Diadaptasi dari metode Zettelkasten (Luhmann; Ahrens, *How to Take Smart Notes*, 2017) —
yang memisahkan catatan sementara dari catatan permanen — dan dari *Architecture Decision
Records* (Nygard, 2011).

| Folder | Jenis | Aturan |
|---|---|---|
| `sesi/` | Log sesi: apa yang terjadi, diputuskan, belum selesai | Ditulis sekali. Nama: `YYYY-MM-DD-topik.md` |
| `konsep/` | Satu gagasan yang tahan lama, bisa dipahami berdiri sendiri | Diperbarui terus. Satu gagasan per catatan |
| `keputusan/` | Keputusan + alasan + alternatif yang ditolak | Tidak diubah; keputusan baru menggantikan yang lama |

Log sesi adalah bahan mentah; nilai jangka panjangnya ada di `konsep/` dan `keputusan/`.
Vault yang hanya berisi log sesi akan jadi tumpukan kronologis yang sulit dipakai.

## Konvensi

- Nama file: huruf kecil, pemisah `-`, tanpa spasi. Tautan memakai nama file tanpa `.md`.
- Setiap catatan diawali frontmatter YAML (`jenis`, `tanggal`, `status`, `tag`).
- Setiap catatan baru ditaut dari [[00-indeks]] dan minimal menaut satu catatan lain.
- Tulis sumber setiap klaim: *diverifikasi* (dijalankan/dibaca), *kata pengguna*, atau *asumsi*.
- Jangan simpan rahasia (API key, token, kredensial) atau data pribadi pihak ketiga.
- Templat ada di `_templat/` (bisa dipasang sebagai folder Templates di Obsidian).

## Cara pakai bersama Claude

- **Akhir sesi:** ketik `/catat-sesi`. Claude menyaring sesi menjadi catatan, memeriksa tautan,
  dan commit. Pastikan branch-nya di-push/di-merge — catatan yang belum di-push ikut hilang.
- **Awal sesi:** `CLAUDE.md` di root repo menyuruh Claude membaca [[00-indeks]] lebih dulu.
- **Merawat:** `/catat-sesi periksa` atau `python3 vault/_alat/periksa.py` untuk mencari
  tautan rusak dan catatan yatim.
- **Graf otomatis (opsional):** lihat [[graphify-dan-vault]].

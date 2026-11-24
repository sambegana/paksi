---
jenis: keputusan
tanggal: 2026-11-24
status: berlaku, diperluas oleh [[vault-tematik-lintas-sesi]]
tag: [meta, ingatan]
---

# Ingatan lintas sesi disimpan sebagai vault Markdown di repo dan diisi lewat /catat-sesi

## Konteks
Pengguna ingin sesi-sesi Claude saling terhubung dan menjadi pengetahuan, seperti Obsidian.
Sesi cloud tidak mewarisi apa pun selain isi repo. → [[sesi-cloud-tanpa-ingatan]]

## Keputusan
- `pengkampanye-urban-tata-ruang/` di repo ini, format Markdown + `[[wikilink]]`, bisa dibuka langsung di Obsidian.
- Tiga jenis catatan: log sesi, konsep, keputusan.
- Skill proyek `/catat-sesi` menyaring sesi menjadi catatan; `CLAUDE.md` menyuruh Claude
  membaca `pengkampanye-urban-tata-ruang/00-indeks.md` di awal sesi.
- Pencatatan dipicu manual (atau ditawarkan Claude di akhir sesi), bukan hook otomatis.

## Alternatif yang ditolak
- **Memasang graphify** — memetakan isi folder, bukan menyimpan sesi. → [[graphify-dan-vault]]
- **Simpan transkrip mentah** — besar, berisik, dan bisa memuat rahasia; yang dibutuhkan sesi
  berikutnya adalah keputusan dan langkah lanjutan, bukan seluruh percakapan.
- **Hook otomatis di setiap akhir sesi** — menghasilkan catatan dari sesi remeh dan mengotori
  vault; ditinjau ulang bila pencatatan manual sering terlupa.
- **Layanan memori eksternal/MCP** — menambah ketergantungan dan menaruh data di luar repo
  milik pengguna.

## Konsekuensi
- Pengetahuan bisa ditinjau di diff, di-versioning, dan dibaca manusia di Obsidian.
- Bergantung pada disiplin: tanpa `/catat-sesi` dan push, tidak ada yang tersimpan.
- Vault terikat ke repo `paksi`; perlu dipindah ke repo tersendiri bila proyek bertambah.

## Sumber
[[2026-11-24-sistem-pengetahuan-sesi]]

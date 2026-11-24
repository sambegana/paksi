---
jenis: konsep
tanggal: 2026-11-24
diperbarui: 2026-11-24 (koreksi)
tag: [claude-code, ingatan]
---

# Sesi cloud baru tidak bisa membaca sesi lama; hanya yang di-commit yang bertahan

Setiap sesi Claude Code di cloud berjalan di container baru yang dibuang setelah sesi selesai
atau lama tidak aktif. File sementara dan skill yang dipasang ke `~/.claude` di container ikut
hilang, dan sesi baru **tidak otomatis** membawa konteks sesi lama. Transkrip sesi lama masih
tersimpan di server dan **bisa dibaca** lewat tool sesi (`list_sessions`, `list_events`),
tetapi hanya bila diminta secara eksplisit. Jadi pengetahuan yang ingin dipakai ulang tetap
perlu disaring ke repo: membaca ulang belasan transkrip setiap sesi mahal dan lambat.

> **Koreksi 2026-11-24.** Versi awal catatan ini menyatakan transkrip sesi lama "tidak ada".
> Itu benar untuk disk container, tetapi keliru untuk akun: belasan sesi lama terbaca lewat
> `list_sessions`. Temuan ini yang memungkinkan mode `/catat-sesi impor`.

## Dasar
- (diverifikasi 2026-11-24) `~/.claude/projects/` di container hanya berisi transkrip sesi aktif.
- (diverifikasi 2026-11-24) `list_sessions` mengembalikan ±40 sesi akun sejak Okt 2026, dan
  `list_events` membaca isinya.
- Dokumentasi Claude Code on the web: container bersifat sementara; yang perlu disimpan harus
  di-commit dan di-push.
- Contoh nyata: rencana arsip Delta Kapuas mencatat bahwa percakapan lama soal pemindahan
  drive "tidak bisa diakses dari sesi ini". (log sesinya sudah dipindah keluar dari vault ini; lihat `docs/rencana-penamaan-delta-kapuas.md`)

## Penerapan
- [[vault-pengetahuan-di-repo]]: menulis pengetahuan ke `pengkampanye-urban-tata-ruang/` dan commit di akhir sesi.
- [[vault-tematik-lintas-sesi]]: mengimpor sesi lama ke vault berstruktur isu/entitas.
- Turunannya: skill atau alat yang dipasang global di container harus dipasang ulang setiap
  sesi. Yang ingin permanen dipasang di level proyek (`.claude/skills/` di repo).

## Batasan
- Commit yang tidak di-push atau branch yang tidak di-merge juga hilang atau tidak terlihat
  oleh sesi yang mulai dari branch default.
- Fitur memori bawaan di aplikasi Claude (bila aktif untuk akun) adalah mekanisme terpisah dan
  tidak bisa dibaca atau diatur dari repo ini.

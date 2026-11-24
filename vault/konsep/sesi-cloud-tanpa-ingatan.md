---
jenis: konsep
tanggal: 2026-11-24
diperbarui: 2026-11-24
tag: [claude-code, ingatan]
---

# Sesi cloud baru tidak bisa membaca sesi lama; hanya yang di-commit yang bertahan

Setiap sesi Claude Code di cloud berjalan di container baru yang dibuang setelah sesi selesai
atau lama tidak aktif. Transkrip, file sementara, dan skill yang dipasang ke `~/.claude` di
container ikut hilang. Sesi baru hanya mewarisi isi repo yang di-clone. Akibatnya, konteks
yang tidak ditulis ke repo harus dijelaskan ulang oleh pengguna.

## Dasar
- (diverifikasi 2026-11-24) `~/.claude/projects/` di container hanya berisi transkrip sesi aktif.
- Dokumentasi Claude Code on the web: container bersifat sementara; yang perlu disimpan harus
  di-commit dan di-push.
- Contoh nyata: rencana arsip Delta Kapuas mencatat bahwa percakapan lama soal pemindahan
  drive "tidak bisa diakses dari sesi ini". → [[2026-10-08-arsip-delta-kapuas]]

## Penerapan
- [[vault-pengetahuan-di-repo]]: menulis pengetahuan ke `vault/` dan commit di akhir sesi.
- Turunannya: skill atau alat yang dipasang global di container harus dipasang ulang setiap
  sesi. Yang ingin permanen dipasang di level proyek (`.claude/skills/` di repo).

## Batasan
- Commit yang tidak di-push atau branch yang tidak di-merge juga hilang atau tidak terlihat
  oleh sesi yang mulai dari branch default.
- Fitur memori bawaan di aplikasi Claude (bila aktif untuk akun) adalah mekanisme terpisah dan
  tidak bisa dibaca atau diatur dari repo ini.

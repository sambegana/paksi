---
jenis: konsep
tanggal: 2026-10-08
diperbarui: 2026-11-24
tag: [keamanan-operasi, otomasi]
---

# Perubahan massal: baca dulu, simulasi, persetujuan manusia, log rollback

Operasi yang mengubah banyak data sekaligus (rename ribuan file, migrasi) dipecah menjadi
tahap yang hanya membaca, lalu simulasi yang menampilkan rencana, lalu persetujuan eksplisit
per baris, baru eksekusi per batch. Setiap perubahan dicatat (ID, nilai lama, nilai baru)
supaya bisa dibatalkan. Pilot kecil (30–50 item) dilakukan sebelum proses penuh.

## Dasar
- Praktik umum change management: dry-run, staged rollout, dan rencana rollback sebelum
  eksekusi.

## Penerapan
- `tools/arsip_dk`: tahap audit/pratinjau/analisis/susun hanya membaca; `terapkan` tanpa
  `--jalankan` adalah simulasi; dengan `--jalankan` meminta konfirmasi "YA"; ada perintah
  `pulihkan`. → [[2026-10-08-arsip-delta-kapuas]]

## Batasan
- Log rollback hanya berguna jika disimpan di luar container sementara (di laptop atau Drive),
  lihat [[sesi-cloud-tanpa-ingatan]].

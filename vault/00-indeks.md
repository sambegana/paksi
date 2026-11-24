---
jenis: indeks
diperbarui: 2026-11-24
---

# Indeks

Baca ini dulu di awal sesi. Isinya peta catatan, bukan isi catatan.

## Pekerjaan terbuka
Ringkasan dari bagian *Belum selesai* di log sesi terbaru. Perbarui setiap `/catat-sesi`.

- **Arsip Delta Kapuas** — pipeline `tools/arsip_dk` siap tapi belum pernah dijalankan ke Drive.
  Menunggu: kredensial di laptop pemilik, audit tahap 1, koreksi kosakata kategori oleh
  pemilik arsip. → [[2026-10-08-arsip-delta-kapuas]]
- **Vault pengetahuan** — baru dibuat; perlu diuji di sesi berikutnya (apakah Claude benar
  membaca indeks dan `/catat-sesi` menghasilkan catatan yang berguna). → [[2026-11-24-sistem-pengetahuan-sesi]]

## Proyek
- **Arsip foto/video Delta Kapuas** — penamaan & penandaan media di Shared Drive.
  Rencana: `docs/rencana-penamaan-delta-kapuas.md` · Kode: `tools/arsip_dk/`

## Keputusan
- [[drive-api-skrip-lokal]] — eksekusi rename Drive lewat skrip Drive API di laptop, bukan connector.
- [[vault-pengetahuan-di-repo]] — ingatan lintas sesi disimpan sebagai vault Markdown di repo ini.

## Konsep
- [[sesi-cloud-tanpa-ingatan]] — sesi baru tidak bisa membaca sesi lama; hanya git yang bertahan.
- [[nama-file-identitas-tag-di-metadata]] — nama file memuat identitas stabil; tag di metadata.
- [[kosakata-terkendali]] — tag dari daftar tetap, bukan dikarang per item.
- [[perubahan-massal-bisa-dibatalkan]] — dry-run, persetujuan manusia, log rollback.
- [[graphify-dan-vault]] — kapan graphify berguna dan kenapa ia bukan pengganti vault ini.

## Log sesi (terbaru di atas)
- [[2026-11-24-sistem-pengetahuan-sesi]]
- [[2026-10-08-arsip-delta-kapuas]] *(rekonstruksi dari commit, bukan transkrip)*

---
jenis: keputusan
tanggal: 2026-10-08
status: berlaku
tag: [arsip-delta-kapuas, google-drive]
---

# Rename arsip Delta Kapuas dijalankan lewat skrip Drive API di laptop pemilik kredensial

## Konteks
Butuh rename massal, pengisian Description, pembacaan EXIF/MD5, ekstraksi keyframe video, dan
log rollback di Shared Drive privat. Sesi cloud tidak punya akses Drive saat itu.

## Keputusan
Opsi B: skrip Python (`tools/arsip_dk`) memakai Google Drive API dengan OAuth desktop atau
service account, dijalankan di laptop pemilik kredensial.

## Alternatif yang ditolak
- Opsi A, connector Google Drive claude.ai — kemampuan rename, ubah Description, dan baca video
  belum pasti.

## Konsekuensi
- Bisa diulang dan diaudit; kode tersimpan di repo.
- Pengguna harus menyiapkan dua kredensial (Google + Anthropic) dan menjalankan sendiri.

## Sumber
[[2026-10-08-arsip-delta-kapuas]] · `docs/rencana-penamaan-delta-kapuas.md` §5

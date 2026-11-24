---
jenis: konsep
tanggal: 2026-10-08
diperbarui: 2026-11-24
tag: [arsip-media, penamaan]
---

# Nama file memuat identitas stabil; tag yang bisa berubah disimpan di metadata

Nama file sebaiknya hanya berisi unsur yang tidak akan berubah: kode proyek, tanggal ISO 8601,
satu kategori utama, nomor unik, dan deskripsi pendek. Tag yang lebih kaya dan bisa bertambah
(spesies, lokasi, kegiatan) disimpan di metadata yang bisa dicari, misalnya kolom Description
Google Drive yang ikut terbaca oleh pencarian `fullText`. Nama yang menampung semua tag akan
panjang, rapuh, dan harus diganti setiap kali tag berubah.

## Dasar
- Library of Congress, *File Naming Best Practices*; IPTC Photo Metadata Standard; Dublin Core
  (dirujuk di `docs/rencana-penamaan-delta-kapuas.md` §1).
- Tanggal `YYYYMMDD` membuat urutan abjad sama dengan urutan kronologis.

## Penerapan
- Arsip Delta Kapuas: `DK_20240315_MGV_00042_akar-tunjang-tepi-sungai.jpg` + blok `[arsip-dk]`
  di Description. → [[2026-10-08-arsip-delta-kapuas]]
- Bekerja bersama [[kosakata-terkendali]].

## Batasan
- Rename memutus referensi berbasis nama (proyek editor video, salinan Drive Desktop). Tautan
  Drive berbasis file ID tidak terpengaruh.
- Metadata di Description tidak ikut bila file diunduh lalu diunggah ke tempat lain.

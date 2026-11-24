---
jenis: konsep
tanggal: 2026-10-08
diperbarui: 2026-11-24
tag: [arsip-media, metadata]
---

# Tag diambil dari kosakata terkendali, bukan dikarang per item

Bila setiap item ditandai dengan kata bebas, satu konsep pecah menjadi banyak varian
("mangrove", "bakau", "hutan-bakau") dan pencarian kehilangan sebagian hasil. Kosakata
terkendali — daftar kode/istilah tetap yang disepakati sebelum penandaan — mencegah itu.
Daftar harus dikoreksi oleh orang yang paham konteks lapangan sebelum dipakai massal.

## Dasar
- Praktik standar perpustakaan dan manajemen aset digital (tesaurus/authority list; IPTC
  menyediakan kosakata terkendali untuk metadata foto).

## Penerapan
- `tools/arsip_dk/arsip_dk/vocab.json`: 11 kode kategori (MGV, SNG, KMP, …, LLN).
  Kategori sekunder dan tag bebas masuk ke Description, kategori utama di nama.
  → [[nama-file-identitas-tag-di-metadata]], [[2026-10-08-arsip-delta-kapuas]]
- Vault ini memakai prinsip yang sama secara ringan: nilai `jenis` di frontmatter dibatasi
  ke `sesi | konsep | keputusan | indeks | panduan`.

## Batasan
- Daftar yang terlalu sempit memaksa banyak item ke "lain-lain" (LLN); pantau porsinya saat
  pilot dan tambah kategori bila perlu.

---
jenis: sesi
tanggal: 2026-10-08
proyek: arsip-delta-kapuas
tag: [google-drive, arsip-media, rekonstruksi]
---

# Rencana & pipeline penamaan arsip Delta Kapuas

> **Rekonstruksi.** Transkrip sesi ini sudah tidak ada. Catatan disusun pada 2026-11-24 dari
> commit `2e668f5` dan `f795739` serta isi `docs/rencana-penamaan-delta-kapuas.md` dan
> `tools/arsip_dk/README.md`. Alasan di balik keputusan hanya sejauh yang tertulis di dokumen itu.

## Tujuan
Menamai ulang dan menandai foto/video di Shared Drive Delta Kapuas (sebagian berasal dari
pemindahan dari drive Sampan Kalimantan) supaya bisa dicari.

## Yang dikerjakan
- Rencana: `docs/rencana-penamaan-delta-kapuas.md` (format nama, kosakata kategori, 5 fase).
- Pipeline: `tools/arsip_dk/` — audit → pratinjau → analisis (Claude API) → susun CSV →
  tinjau manusia → terapkan, plus pulihkan.

## Keputusan
- Format nama `DK_<YYYYMMDD>_<KAT>_<NNNNN>_<deskripsi>.<ext>`; tag lengkap di kolom Description
  Drive. → [[nama-file-identitas-tag-di-metadata]], [[kosakata-terkendali]]
- Delta Kapuas adalah Shared Drive (kata pengguna); eksekusi via skrip Drive API. → [[drive-api-skrip-lokal]]
- Tahap 1–4 hanya membaca; perubahan hanya setelah persetujuan, dengan log rollback.
  → [[perubahan-massal-bisa-dibatalkan]]

## Temuan & jalan buntu
- Percakapan lama tentang pemindahan Sampan Kalimantan → Delta Kapuas tidak bisa diakses dari
  sesi itu — contoh nyata dari [[sesi-cloud-tanpa-ingatan]].
- API key Google biasa (`AIza...`) tidak bisa membuka Shared Drive privat; butuh OAuth desktop
  atau service account (tertulis di README pipeline).
- Tanggal upload Drive menyesatkan sebagai tanggal foto; pakai EXIF, atau `00000000` bila tidak ada.

## Belum selesai / langkah berikutnya
- [ ] Siapkan kredensial Google + `ANTHROPIC_API_KEY` di laptop pemilik.
- [ ] Jalankan `audit` (sekaligus bandingkan dengan Sampan Kalimantan) — belum pernah dijalankan.
- [ ] Pemilik arsip mengoreksi `tools/arsip_dk/arsip_dk/vocab.json` sebelum tahap analisis.
- [ ] Pilot 50 file, tinjau CSV, baru proses penuh.
- [ ] Pertanyaan §7 rencana yang belum terjawab: jumlah/ukuran file, struktur folder
      dipertahankan atau ditata ulang, kecocokan kosakata.

## Terkait
- [[00-indeks]]

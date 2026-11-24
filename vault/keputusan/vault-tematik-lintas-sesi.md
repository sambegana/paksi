---
jenis: keputusan
tanggal: 2026-11-24
status: berlaku
tag: [meta, ingatan, kampanye]
---

# Vault disusun per isu dan entitas, diisi dengan mengimpor sesi-sesi Claude lama

## Konteks
Pengguna adalah pengkampanye urban dan tata ruang berkeadilan. Bahan belajarnya tersebar di
sesi Claude yang terpisah (data center, sampah, tata ruang, air, sungai, hutan kota, iklim,
advokasi kebijakan). Mereka ingin pengetahuan itu saling tersambung meski sesinya berbeda.
Struktur vault awal ([[vault-pengetahuan-di-repo]]) masih berorientasi satu proyek.

## Keputusan
- Struktur: `isu/` (hub per isu) + `konsep/`, `regulasi/`, `aktor/`, `tempat/` (satu entitas
  per catatan) + `sesi/` (sumber) + `benang-merah.md` (sintesis lintas isu).
  Sambungan antarsesi terjadi di entitas bersama, bukan di log sesi.
- Sesi lama diimpor lewat API sesi (`list_events`), dibaca paralel oleh agen, lalu digabung
  dengan slug kanonik agar entitas yang sama tidak terpecah.
- Repo tetap **publik** atas keputusan pengguna. Batas yang tetap dipegang: tanpa rahasia
  dan tanpa data pribadi warga biasa.
- Modul HTML belajar diimpor ke `modul/` hanya setelah pengguna menyatakan modulnya final.

## Alternatif yang ditolak
- Satu folder per sesi atau per proyek — pengetahuan tidak bertemu antarisu.
- Repo privat atau vault terpisah — ditawarkan; pengguna memilih tetap publik.
- Hanya memakai graphify — tidak membaca sesi. → [[graphify-dan-vault]]

## Konsekuensi
- Pengetahuan bisa dilihat sebagai graf di Obsidian. Hub isu dan entitas jadi titik masuk
  untuk menulis rilis atau policy brief.
- Strategi kampanye dan peta aktor dapat dibaca publik, termasuk pihak lawan.
- Penggabungan butuh disiplin slug; `periksa.py` dan mode `impor` menjaga konsistensinya.

## Sumber
[[2026-11-24-sistem-pengetahuan-sesi]]

# Jebakan yang Pernah Terjadi (dan Cara Mencegahnya)

1. **Kueri gagal dianggap 0 hasil.** Google News membalas 503 saat banyak permintaan berjalan bersamaan. Skrip di
   skill ini mengulang dengan jeda dan mencatat `kueri_gagal`; laporkan jumlahnya. Jangan menjalankan banyak sapuan
   besar bersamaan.
2. **Nama media ikut tercocokkan.** Judul Google News berakhiran " - Nama Media" ("Terasbatam", "Batam Pos"). Selalu
   buang akhiran itu sebelum mencocokkan kata kunci (`klasifikasi_isu.bersih`).
3. **Substring menipu.** "ikan" cocok di "hentikan"; "kota" di "Kotawaringin". Pakai batas kata dan uji sampel acak 30
   judul per isu untuk mengecek ketepatan.
4. **Pulau besar dikira pulau kecil.** "Pulau Kalimantan/Jawa/Sumatera" dikecualikan dari aturan lokus pesisir.
5. **Satu tindakan, banyak rilis.** Pencabutan izin atau penetapan tersangka sering jadi bukti di banyak rilis karhutla.
   Hitung sekali di tabel tindakan unik.
6. **Salah bulan.** Bulan dari folder sering keliru (rilis 25–29 tercatat bulan berikutnya). Pakai tanggal terbit.
7. **Duplikat di daftar rilis.** Judul sama di dua bulan, atau paket "kesaksian" + rilis. Tanyakan ke pengguna.
8. **Berkas draf.** Berkas "DRAFT" jangan dihitung sebelum terbukti terbit.
9. **Atribusi salah bidang.** Pengkampanye yang dikutip di rilis publik bisa dari bidang lain (mis. Musdalifah di rilis
   transisi energi → Pangan). Bidang mengikuti pengkampanye yang dikutip.
10. **Ejaan nama.** Media lebih sering menulis "Styawan" (sesuai tim) daripada "Setyawan"; ikuti tim.
11. **Proteksi bot.** Situs WALHI dan banyak media memakai Cloudflare. Jangan menembus, jangan memalsukan User-Agent.
12. **Periode berbeda.** Angka korpus lama (mis. 879 judul) mencakup Juni–November; pastikan semua angka satu periode.
13. **Klaim kausal.** Korelasi pemberitaan–respons ada, tetapi isu besar (karhutla) mendorong keduanya. Jangan menulis sebab-akibat.
14. **Respons pemerintah asing** (mis. Singapura) bukan respons pemerintah Indonesia; catat terpisah.

---
jenis: konsep
tanggal: 2026-11-24
diperbarui: 2026-11-24
tag: [alat, graf-pengetahuan]
---

# graphify memetakan isi folder; ia tidak menyimpan atau menghubungkan sesi

graphify (paket PyPI `graphifyy`, CLI `graphify`) membangun graf pengetahuan dari folder kode,
dokumen, PDF, gambar, dan media, lalu menghasilkan `graphify-out/` berisi `graph.html`,
`GRAPH_REPORT.md`, dan `graph.json`. Ia berguna untuk memahami basis kode besar. Ia tidak
membaca transkrip sesi Claude dan tidak menyediakan ingatan lintas sesi — itu tugas vault ini.

## Dasar
- README resmi github.com/safishamsi/graphify (dibaca 2026-11-24). Pasang: `uv tool install graphifyy`,
  lalu `graphify install --project` untuk memasang skill ke `.claude/skills/graphify/` di repo.
- Kode diparse lokal (tree-sitter) tanpa LLM. Dokumen/PDF/gambar melewati tahap semantik yang
  memakai model asisten atau backend LLM yang dikonfigurasi.
- Integrasi Claude Code-nya memasang hook PreToolUse yang aktif sebelum setiap pencarian file.

## Penerapan
- Belum dipasang. Repo `paksi` masih kecil (satu paket Python + satu dokumen), jadi graf
  otomatis belum memberi nilai lebih dari membaca langsung, sementara hook-nya menambah
  langkah di setiap pencarian. → [[2026-11-24-sistem-pengetahuan-sesi]]
- Pemakaian yang masuk akal nanti: `/graphify vault` untuk melihat hubungan antarcatatan yang
  belum ditaut manual, atau `/graphify .` ketika kode sudah besar.

## Batasan
- Graf hasil inferensi LLM bisa memuat hubungan yang keliru (graphify menandai edge
  `INFERRED`); jangan menyalinnya ke vault tanpa diperiksa.
- Bila dipasang global di container cloud, ia hilang di sesi berikutnya; pasang dengan
  `--project` dan commit bila ingin permanen.

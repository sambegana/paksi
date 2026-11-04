// Template alur multi-agen: pengode respons per kelompok bidang + pemeriksa adversarial.
// Pakai dengan tool Workflow (hanya bila pengguna setuju multi-agen). args:
//   {"folder": "/abs/path/docs/capaian-walhi-<yyyy-mm>", "skill": "/abs/path/.claude/skills/analisis-capaian-kampanye-walhi",
//    "mulai": "2026-11-01", "akhir_respons": "2026-12-02",
//    "kelompok": [{"nama": "Hutan & Kebun", "ids": ["R01", "R02"]}, ...]}
// Batasi ±5 kelompok (10 agen). Kelompokkan rilis agar tiap agen menangani <= 10 rilis.
export const meta = {
  name: 'respons-rilis-walhi',
  description: 'Per bidang kampanye: ukur pemuatan tiap rilis WALHI dan kode respons pemerintah, lalu verifikasi adversarial',
  phases: [
    { title: 'Kode', detail: 'satu agen per kelompok bidang: jalankan skrip pemuatan per rilis, cari dan kode respons pemerintah' },
    { title: 'Verifikasi', detail: 'satu agen per kelompok: coba bantah setiap skor' },
  ],
}

const REPO = args.folder
const SKILL = args.skill

const RESPON = {
  type: 'object',
  properties: {
    lembaga: { type: 'string' }, tanggal: { type: 'string' },
    bentuk: { type: 'string', enum: ['langsung_ke_walhi', 'ke_jejaring', 'umum_tanpa_menyebut', 'tindakan'] },
    isi: { type: 'string' }, url: { type: 'string' },
  },
  required: ['lembaga', 'tanggal', 'bentuk', 'isi', 'url'],
}
const RILIS = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    tuntutan_ringkas: { type: 'string' },
    lembaga_dituju: { type: 'string' },
    berita_kasus: { type: 'integer' },
    berita_memuat_walhi: { type: 'integer' },
    berita_jejaring_tanpa_walhi: { type: 'integer' },
    berita_kontra: { type: 'integer' },
    penutur_terdeteksi: { type: 'array', items: { type: 'string' } },
    jejaring_terdeteksi: { type: 'array', items: { type: 'string' } },
    respons: { type: 'array', items: RESPON },
    skor: { type: 'integer', minimum: 0, maximum: 4 },
    hari_ke_respons: { type: 'integer', description: 'hari dari rilis ke respons pertama; -1 bila tidak ada' },
    konvergensi: { type: 'boolean', description: 'tindakan searah tapi tidak menyebut WALHI/jejaring' },
    keyakinan: { type: 'string', enum: ['tinggi', 'sedang', 'rendah'] },
    catatan: { type: 'string' },
  },
  required: ['id', 'tuntutan_ringkas', 'lembaga_dituju', 'berita_kasus', 'berita_memuat_walhi', 'berita_jejaring_tanpa_walhi', 'berita_kontra', 'penutur_terdeteksi', 'jejaring_terdeteksi', 'respons', 'skor', 'hari_ke_respons', 'konvergensi', 'keyakinan', 'catatan'],
}
const OUT = { type: 'object', properties: { rilis: { type: 'array', items: RILIS } }, required: ['rilis'] }
const VOUT = {
  type: 'object',
  properties: {
    rilis: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' }, skor_awal: { type: 'integer' }, skor_final: { type: 'integer', minimum: 0, maximum: 4 },
          respons_tambahan: { type: 'array', items: RESPON },
          alasan: { type: 'string' }, keyakinan: { type: 'string', enum: ['tinggi', 'sedang', 'rendah'] },
        },
        required: ['id', 'skor_awal', 'skor_final', 'respons_tambahan', 'alasan', 'keyakinan'],
      },
    },
  },
  required: ['rilis'],
}

const ATURAN = `
ATURAN PENGODEAN (wajib):
- Respons dihitung dari tanggal rilis sampai ${args.akhir_respons}. Respons sebelum tanggal rilis TIDAK dihitung.
- Skala skor (respons TERTINGGI dari lembaga yang dituju, atau atasan/instansi yang berwenang atas tuntutan itu):
  0 tidak ada respons; 1 menolak/membantah secara terbuka (mis. "proyek tetap jalan", "tidak benar"); 2 diakui/berjanji/"akan dikaji" tanpa tindakan terverifikasi;
  3 tindakan terverifikasi yang searah tetapi sebagian; 4 tuntutan dipenuhi.
- Respons kepada JEJARING (koalisi/kelompok warga yang membawa tuntutan yang sama, mis. KOMPI, KIARA, Maleh Dadi Segoro, JATAM, AMAN, Greenpeace) DIHITUNG; tandai bentuk "ke_jejaring".
- Tindakan searah yang tidak menyebut WALHI/jejaring tetap dihitung, set konvergensi=true.
- Kontra-narasi dari pihak ketiga (aktivis/koalisi pro-proyek, ormas) BUKAN respons resmi: jangan diberi skor, hitung di berita_kontra dan sebut di catatan.
- Bila ragu antara dua skor, pakai yang LEBIH RENDAH dan jelaskan. Jangan mengarang; kalau tidak ditemukan tulis "tidak ditemukan" dan skor 0.
- URL harus halaman yang benar-benar kamu lihat (hasil WebSearch/WebFetch atau keluaran skrip).
ETIKA AKSES: jangan menembus proteksi bot, jangan memalsukan User-Agent, jangan memakai curl dengan header peramban. Situs yang memblokir dibiarkan; pakai tanda indeks Google (indeks_walhi) dari skrip, atau WebFetch biasa.
`

const CARA = `
CARA KERJA untuk setiap id rilis:
1. Baca barisnya di ${REPO}/rilis_base.csv (kolom: tanggal, judul_singkat, status, bidang_topik, pj_penutur, jenis_tuntutan, tuntutan_utama, lembaga_dituju, kueri_kasus dipisah "|", jejaring dipisah koma).
   Untuk tanggal yang hanya berisi bulan (mis. "2026-09"), cari dulu tanggal terbit pastinya lewat WebSearch; kalau tidak ketemu pakai tanggal 15.
   Rilis berstatus DRAFT atau "perlu cek isi": cari apakah benar terbit; kalau tidak ditemukan bukti terbit, skor 0, keyakinan rendah, catatan "tidak ditemukan bukti terbit".
2. Ukur pemuatan dengan skrip (sudah terpasang, jalankan dari /home/user/paksi):
   python3 -I ${SKILL}/scripts/pemuatan_rilis.py --id <ID> --tanggal <YYYY-MM-DD> --out ${REPO}/hasil/<ID>.json --kueri '<kueri1>' --kueri '<kueri2>' ... --jejaring '<nama1>' --jejaring '<nama2>'
   Pakai semua kueri_kasus, TAMBAHKAN versi kasus tanpa kata walhi (mis. '"revitalisasi tambak" pantura') dan 1–2 kueri jejaring+kasus (mis. 'KOMPI tambak'). Maksimal 7 kueri.
   Lalu baca file JSON hasilnya. Buang berita yang tidak relevan dengan kasus. Hitung: berita_kasus (relevan), berita_memuat_walhi (walhi_di_isi>0 atau indeks_walhi atau walhi_di_judul),
   berita_jejaring_tanpa_walhi, berita_kontra (menyerang/membantah tuntutan WALHI-jejaring). penutur_terdeteksi dari penutur_walhi; jejaring_terdeteksi dari jejaring_di_isi dan judul.
3. Cari respons pemerintah: periksa kalimat_pemerintah di hasil skrip, lalu WebSearch (Indonesia) nama lembaga + kasus + "tanggapi/respons/bantah/dikaji/dicabut/dihentikan", juga situs resmi (kkp.go.id, kemenlh.go.id, esdm.go.id, polri.go.id, menlhk/kemenhut, setneg, pemda).
   Periksa juga respons kepada jejaring atas tuntutan yang sama.
4. Aturan lengkap skala: ${SKILL}/references/skala_respons.md. Orang dan jejaring: ${SKILL}/references/roster.md.
`

const groups = args.kelompok
phase('Kode')
const hasil = await pipeline(
  groups,
  g => agent(`Kamu pengode respons pemerintah untuk tim KAMPANYE WALHI (fokus: apakah pemerintah merespons tuntutan, bukan sekadar jumlah berita).
Kelompok: ${g.nama}. Kerjakan SEMUA id ini, satu per satu: ${g.ids.join(', ')}.
${CARA}
${ATURAN}
Kembalikan satu objek per id, urut sesuai daftar.`, { label: `kode:${g.nama}`, phase: 'Kode', schema: OUT }),
  (kode, g) => agent(`Kamu pemeriksa skeptis. Tugasmu MEMBANTAH skor respons pemerintah berikut untuk kelompok ${g.nama}.
Untuk setiap rilis: (a) cari respons yang TERLEWAT dari lembaga yang dituju atau kepada jejaring (bisa menaikkan skor); (b) periksa apakah respons yang diklaim benar-benar dari lembaga itu, terjadi SETELAH tanggal rilis dan paling lambat ${args.akhir_respons}, dan sesuai skala (bisa menurunkan skor). Buka URL bukti yang diklaim (WebFetch) bila bisa.
Baris rilis ada di ${REPO}/rilis_base.csv; hasil skrip pemuatan ada di ${REPO}/hasil/<ID>.json.
${ATURAN}
Hasil pengodean yang harus diperiksa:
${JSON.stringify(kode && kode.rilis ? kode.rilis : [], null, 1)}
Kembalikan skor_awal, skor_final, respons_tambahan (kosongkan bila tidak ada), alasan singkat, dan keyakinan untuk setiap id.`, { label: `verifikasi:${g.nama}`, phase: 'Verifikasi', schema: VOUT })
    .then(v => ({ kelompok: g.nama, kode, verifikasi: v })),
)
return hasil.filter(Boolean)

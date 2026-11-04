// Laporan capaian kampanye WALHI Agu–Okt 2026.
// Jalankan: python3 final_respons.py && python3 make_figures_respons.py && python3 produksi_rilis.py && node build_laporan_capaian.js
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, AlignmentType, HeadingLevel,
  BorderStyle, ShadingType, LevelFormat, Footer, PageNumber, ExternalHyperlink, TableLayoutType, PageBreak,
} = require("docx");

const HERE = __dirname, FIG = path.join(HERE, "figures_respons");
function parseCSV(file) {
  const txt = fs.readFileSync(path.join(HERE, file), "utf8").trim();
  const rows = []; let row = [], cur = "", q = false;
  for (let i = 0; i < txt.length; i++) {
    const c = txt[i];
    if (q) { if (c === '"' && txt[i + 1] === '"') { cur += '"'; i++; } else if (c === '"') q = false; else cur += c; }
    else if (c === '"') q = true; else if (c === ",") { row.push(cur); cur = ""; }
    else if (c === "\n") { row.push(cur); rows.push(row); row = []; cur = ""; } else if (c !== "\r") cur += c;
  }
  row.push(cur); rows.push(row);
  const h = rows.shift();
  return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]])));
}
const S = JSON.parse(fs.readFileSync(path.join(HERE, "ringkasan_per_isu.json"), "utf8"));
const R = parseCSV("respons_final.csv");
const RING = Object.fromEntries(parseCSV("ringkas_respons.csv").map(r => [r.id, r]));
const T = parseCSV("tindakan_unik.csv");
const BELUM = parseCSV("rilis_belum_dikode.csv");
const ISU = ["Hutan & Kebun", "Pesisir & Laut", "Urban", "Pangan & Ekosistem Esensial", "Iklim & Isu Global", "Tambang & Energi"];
const NAMA_ISU = { "Hutan & Kebun": "Hutan dan Kebun", "Pesisir & Laut": "Perlindungan Pesisir dan Laut", "Urban": "Urban dan Tata Ruang",
  "Pangan & Ekosistem Esensial": "Ekosistem Esensial dan Pangan", "Iklim & Isu Global": "Iklim dan Isu Global", "Tambang & Energi": "Tambang dan Energi Berkeadilan" };
const LABEL = { 0: "0 · tidak ada", 1: "1 · ditolak", 2: "2 · dijanjikan", 3: "3 · tindakan", 4: "4 · dipenuhi" };
const BUL = ["", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"];
const tgl = s => { const p = s.split("-"); return p.length === 3 ? `${+p[2]} ${BUL[+p[1]]}` : BUL[+p[1]]; };
const pct = x => `${Math.round(x)}%`;

const FONT = "Calibri", CW = 9072;
const bd = { style: BorderStyle.SINGLE, size: 4, color: "808080" };
const borders = { top: bd, bottom: bd, left: bd, right: bd };
const run = (x, o = {}) => (Array.isArray(x) ? x : [x]).map(r => typeof r === "string" ? new TextRun({ text: r, ...o })
  : r.link ? new ExternalHyperlink({ link: r.link, children: [new TextRun({ text: r.t, style: "Hyperlink", ...o })] })
    : new TextRun({ text: r.t, bold: r.b, italics: r.i, ...o }));
const P = (x, o = {}) => new Paragraph({ children: run(x), spacing: { after: 110, line: 276 }, ...o });
const H1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const H2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const B = x => new Paragraph({ numbering: { reference: "b", level: 0 }, children: run(x), spacing: { after: 60, line: 276 } });
let fN = 0, tN = 0;
function fig(file, cap, src) {
  fN++;
  const b = fs.readFileSync(path.join(FIG, file)), w = b.readUInt32BE(16), h = b.readUInt32BE(20);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 100, after: 40 },
      children: [new ImageRun({ type: "png", data: b, transformation: { width: 600, height: Math.round(600 * h / w) }, altText: { title: `Gambar ${fN}`, description: cap, name: file } })] }),
    new Paragraph({ style: "Caption", keepNext: true, children: [new TextRun({ text: `Gambar ${fN}. `, bold: true }), new TextRun(cap)] }),
    new Paragraph({ style: "Src", children: [new TextRun(`Sumber: ${src}`)] }),
  ];
}
function table(cap, widths, head, body, o = {}) {
  tN++;
  const size = o.size || 18;
  const cell = (t, w, hd, fill) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA }, margins: { top: 40, bottom: 40, left: 70, right: 70 },
    shading: hd ? { fill: "D9D9D9", type: ShadingType.CLEAR, color: "auto" } : fill ? { fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    children: [new Paragraph({ children: run(t, { size, bold: hd || undefined }) })],
  });
  return [
    new Paragraph({ style: "Caption", keepNext: true, spacing: { before: 140, after: 60 }, children: [new TextRun({ text: `Tabel ${tN}. `, bold: true }), new TextRun(cap)] }),
    new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: [
      new TableRow({ tableHeader: true, children: head.map((t, i) => cell(t, widths[i], true)) }),
      ...body.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, widths[i], false, o.fills && o.fills[ri])) })),
    ] }),
    new Paragraph({ spacing: { after: 100 }, children: [] }),
  ];
}

const tot = S._total;
const hitung = R.filter(r => r.status === "dihitung");
const nyataRilis = hitung.filter(r => +r.skor >= 3 && ["inti", "sebagian"].includes(r.kecocokan_tindakan));
const PROD = JSON.parse(fs.readFileSync(path.join(HERE, "produksi_rilis.json"), "utf8"));
const PRODTOT = Object.values(PROD.produksi).reduce((a, p) => a + p.total, 0) + 2; // + 2 rilis lintas bidang
const LUAR = R.filter(r => r.status === "catatan: di luar daftar divisi");
const fill0 = { 3: "DEEAF6", 2: "F2F2F2" };
const C = [];
C.push(
  new Paragraph({ children: [new TextRun({ text: "LAPORAN CAPAIAN KAMPANYE", bold: true, size: 20, color: "595959" })], spacing: { after: 60 } }),
  new Paragraph({ style: "Title", children: [new TextRun("Capaian Kampanye WALHI Eksekutif Nasional, Agustus–Oktober 2026")] }),
  new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: "Respons pemerintah atas rilis kampanye, produksi rilis per bidang, dan pemberitaan · respons dihitung sampai 2 November 2026 · draf untuk dicek tim", italics: true, color: "404040" })] }),
);

// 1. Ringkasan
C.push(H1("1. Ringkasan Capaian"));
C.push(
  B([{ t: "Produksi. ", b: true }, `Divisi Kampanye memproduksi ${PRODTOT} rilis (43 baris di rekap divisi; satu rilis tercatat dua kali). Hutan & Kebun paling banyak (${PROD.produksi["Hutan & Kebun"].total}), disusul Pesisir & Laut (${PROD.produksi["Pesisir & Laut"].total}); Tambang & Energi paling sedikit (${PROD.produksi["Tambang & Energi"].total}). ${tot.rilis} rilis berisi tuntutan spesifik kepada pemerintah dan dikode responsnya.`]),
  B([{ t: "Respons. ", b: true }, `${tot.ada_respons} rilis (${pct(tot.pct_ada_respons)}) mendapat respons pemerintah, tetapi hanya ${tot.tindakan_nyata} (${pct(tot.pct_tindakan_nyata)}) yang berujung tindakan nyata. Tidak ada tuntutan yang dipenuhi penuh.`]),
  B([{ t: "Capaian utama ada di karhutla. ", b: true }, `Ada ${T.length} tindakan unik: pembekuan dan pencabutan izin, penyegelan konsesi, penetapan 20 korporasi tersangka, penyerahan data pemilik manfaat, penyidikan laporan WALHI Kalsel, dan rumah oksigen gratis bagi korban asap. Dua di antaranya terkait langsung dengan WALHI: 4 dari 5 izin yang dicabut ada di daftar laporan WALHI, dan Kapolda Kalsel menyebut laporan WALHI Kalsel naik ke penyidikan.`]),
  B([{ t: "Isu lain baru sampai respons. ", b: true }, `Urban direspons di semua rilis, tetapi dengan penolakan atau janji. Pesisir & Laut (${pct(S["Pesisir & Laut"].pct_ada_respons)}), Iklim (${pct(S["Iklim & Isu Global"].pct_ada_respons)}) dan Tambang & Energi (${pct(S["Tambang & Energi"].pct_ada_respons)}) paling jarang direspons.`]),
  B([{ t: "Pemberitaan. ", b: true }, `${tot.berita_memuat_walhi} berita yang memuat WALHI terkait langsung dengan rilis-rilis ini, ditambah ${tot.berita_jejaring} berita dari jejaring. Median berita yang memuat WALHI: ${tot.median_walhi_per_skor["3"] ?? tot.median_walhi_per_skor[3]} per rilis yang berujung tindakan, ${tot.median_walhi_per_skor["0"] ?? tot.median_walhi_per_skor[0]} per rilis tanpa respons.`]),
);
C.push(...table("Capaian per isu kampanye", [2250, 1700, 750, 1100, 1150, 1072, 1050],
  ["Isu", "PJ bidang", "Rilis", "Ada respons", "Tindakan nyata", "Berita memuat WALHI", "Median hari ke respons"],
  [...ISU.map(k => { const s = S[k]; return [NAMA_ISU[k], PROD.produksi[k].pj, String(s.rilis), `${s.ada_respons} (${pct(s.pct_ada_respons)})`, `${s.tindakan_nyata} (${pct(s.pct_tindakan_nyata)})`, String(s.berita_memuat_walhi), s.median_hari_ke_respons == null ? "–" : String(s.median_hari_ke_respons)]; }),
   [{ t: "Semua isu", b: true }, "", { t: String(tot.rilis), b: true }, { t: `${tot.ada_respons} (${pct(tot.pct_ada_respons)})`, b: true }, { t: `${tot.tindakan_nyata} (${pct(tot.pct_tindakan_nyata)})`, b: true }, { t: String(tot.berita_memuat_walhi), b: true }, ""]]));
C.push(P([{ t: "Cara membaca: ", b: true }, "skor respons 0 tidak ada; 1 ditolak; 2 diakui atau dijanjikan tanpa tindakan; 3 tindakan terverifikasi yang searah tetapi sebagian; 4 tuntutan dipenuhi. \"Tindakan nyata\" hanya menghitung skor 3 yang menyentuh inti atau sebagian tuntutan, tidak termasuk tindakan karhutla umum yang dipakai sebagai bukti di rilis lain (\"tindakan generik\")."]));

// 2. Capaian utama
C.push(new Paragraph({ children: [new PageBreak()] }));
C.push(H1("2. Capaian Utama: Tindakan Nyata Pemerintah"));
C.push(P(`Satu tindakan pemerintah sering menjawab beberapa rilis sekaligus, jadi tindakan dihitung sekali (${T.length} tindakan unik) lalu dikaitkan ke rilis yang tuntutannya disentuh.`));
const urut = [...T].sort((a, b) => a.tanggal.localeCompare(b.tanggal));
C.push(...table("Tindakan nyata pemerintah setelah rilis WALHI", [800, 1500, 3372, 1500, 1900],
  ["Tanggal", "Lembaga", "Tindakan", "Rilis terkait", "Atribusi ke WALHI"],
  urut.map(t => [tgl(t.tanggal), t.lembaga, t.bukti ? [t.tindakan + " ", { t: "[sumber]", link: t.bukti }] : t.tindakan, t.rilis_terkait.split(";").join(", "), t.atribusi]),
  { fills: urut.map(t => /WALHI/.test(t.atribusi) ? "DEEAF6" : undefined) }));
C.push(P([{ t: "Baris berwarna", b: true }, " = terkait langsung dengan WALHI. Baris lain searah dengan tuntutan WALHI tetapi tidak menyebut WALHI (konvergensi), dan sebagian menyusul arahan Presiden pada ratas 16 September. Karena itu capaian ini paling tepat ditulis sebagai \"tuntutan WALHI diikuti langkah pemerintah\", bukan \"dipenuhi karena WALHI\"."]));

// 3. Respons per isu
C.push(H1("3. Respons Pemerintah per Isu"));
C.push(...fig("gambar-1-tangga-respons-per-isu.png", "Respons tertinggi pemerintah atas tiap rilis, per isu", "pengodean penulis (diverifikasi agen pemeriksa), Agu–Okt 2026."));
C.push(P("Hutan & Kebun satu-satunya isu dengan banyak tindakan nyata (8 dari 15 rilis). Pesisir & Laut dan Tambang & Energi didominasi \"tidak ada respons\". Urban tidak punya rilis yang diabaikan, tetapi semua responsnya berhenti di penolakan atau janji."));
C.push(...fig("gambar-2-respons-vs-tindakan.png", "Persentase rilis yang direspons dan yang berujung tindakan nyata", "pengodean penulis."));

// 4. Produksi rilis
C.push(H1("4. Produksi Rilis per Bidang"));
C.push(P("Jumlah rilis mengikuti daftar rilis Laporan Divisi Kampanye Juli–Oktober 2026. Rilis yang hanya disuarakan pimpinan atau Hukum tetap masuk bidang pemilik topiknya, tetapi tidak dikreditkan ke pengkampanye."));
C.push(...table("Rilis kampanye per bidang dan bulan (daftar divisi)", [2100, 1700, 700, 900, 900, 900, 600, 600, 672],
  ["Bidang", "PJ", "Total", "Dibawakan PJ", "Pimpinan/ Hukum", "Momen lembaga", "Agu", "Sep", "Okt"],
  [...ISU.map(k => { const p = PROD.produksi[k]; return [NAMA_ISU[k], p.pj, String(p.total), String(p.dibawakan_pj), String(p.total - p.dibawakan_pj - p.tidak_diketahui), String(p.momen_lembaga), String(p.agu), String(p.sep), String(p.okt)]; }),
   ["Lintas bidang (lembaga)", "–", "2", "–", "2", "2", "1", "1", "0"],
   [{ t: "Total", b: true }, "", { t: String(PRODTOT), b: true }, "", "", "", "", "", ""]]));
C.push(P("Pesisir & Laut tercatat 11 baris di daftar divisi. Satu di antaranya, Ketahanan Pangan Jangan Rampas Ruang Petambak, tercantum dua kali (September dan Oktober), jadi dihitung 10 rilis. Di Hutan & Kebun, sebagian besar rilis hanya mengutip pimpinan atau Hukum; Pesisir & Laut, Urban, dan Pangan hampir seluruhnya dibawakan pengkampanyenya sendiri."));

// 5. Pemberitaan
C.push(H1("5. Pemberitaan (Konteks)"));
C.push(P("Untuk tiap rilis, berita dicari dalam rentang 1 hari sebelum sampai 14 hari sesudah rilis, lewat kata kunci kasus, nama jejaring, dan nama pengkampanye. Isi berita dibaca untuk mengecek sebutan WALHI, meski tidak ada di judul."));
C.push(...table("Pemberitaan terkait rilis per isu", [2350, 800, 1300, 1300, 1300, 1000, 1022],
  ["Isu", "Rilis", "Berita kasus", "Memuat WALHI", "Rata-rata per rilis", "Jejaring tanpa WALHI", "Kontra-narasi"],
  [...ISU.map(k => { const s = S[k]; return [NAMA_ISU[k], String(s.rilis), String(s.berita_kasus), String(s.berita_memuat_walhi), String(s.rata_walhi_per_rilis).replace(".", ","), String(s.berita_jejaring), String(s.berita_kontra)]; }),
   [{ t: "Semua isu", b: true }, { t: String(tot.rilis), b: true }, { t: String(tot.berita_kasus), b: true }, { t: String(tot.berita_memuat_walhi), b: true }, "", { t: String(tot.berita_jejaring), b: true }, { t: String(tot.berita_kontra), b: true }]]));
C.push(...fig("gambar-3-pemberitaan-vs-respons.png", "Median berita yang memuat WALHI per rilis, menurut respons tertinggi pemerintah", "pengodean dan pengumpulan berita penulis."));
C.push(P("Rilis yang banyak dimuat media cenderung lebih sering berujung tindakan; pola ini juga terlihat di dalam isu Hutan & Kebun saja. Ini bukan bukti sebab-akibat: isu karhutla memang besar, dan tindakan pemerintah sendiri ikut menambah berita."));
const top = [...hitung].sort((a, b) => b.berita_memuat_walhi - a.berita_memuat_walhi).slice(0, 8);
C.push(...table("Delapan rilis dengan berita memuat WALHI terbanyak", [1100, 3672, 1400, 1500, 1400],
  ["Rilis", "Narasi", "Memuat WALHI", "Berita kasus", "Skor respons"],
  top.map(r => [`${r.id} · ${tgl(r.tanggal)}`, (RING[r.id] || {}).narasi_singkat || r.tuntutan, r.berita_memuat_walhi, r.berita_kasus, LABEL[r.skor]])));

// 5b. Rilis publik di luar daftar divisi
C.push(H2("Rilis publik di luar daftar divisi"));
C.push(P(`${LUAR.length} rilis berikut terbit di situs atau kanal WALHI pada periode yang sama tetapi tidak ada di daftar divisi. Respons atas rilis-rilis ini tidak masuk statistik bidang, tetapi dicatat karena sebagian berujung tindakan.`));
C.push(...table("Rilis publik di luar daftar divisi dan respons pemerintah", [1150, 1400, 2500, 2822, 1200],
  ["Rilis", "Isu dugaan", "Tuntutan", "Respons pemerintah", "Skor"],
  LUAR.sort((a, b) => a.tanggal.localeCompare(b.tanggal)).map(r => [`${r.id} · ${tgl(r.tanggal)}`, NAMA_ISU[r.isu] || r.isu, (RING[r.id] || {}).narasi_singkat || r.tuntutan, (RING[r.id] || {}).respons_singkat || "", LABEL[r.skor] + (r.kecocokan_tindakan === "generik" ? " (generik)" : "")]),
  { fills: LUAR.map(r => fill0[r.skor]) }));

// 6. Rincian per isu
C.push(new Paragraph({ children: [new PageBreak()] }));
C.push(H1("6. Rincian per Isu"));
const fill = { 3: "DEEAF6", 2: "F2F2F2" };
ISU.forEach((k, i) => {
  const s = S[k]; const rs = hitung.filter(r => r.isu === k).sort((a, b) => b.skor - a.skor || a.tanggal.localeCompare(b.tanggal));
  C.push(H2(`6.${i + 1} ${NAMA_ISU[k]}`));
  C.push(P([{ t: `${s.rilis} rilis · ${s.ada_respons} direspons · ${s.tindakan_nyata} tindakan nyata · ${s.berita_memuat_walhi} berita memuat WALHI`, b: true }, ` · PJ ${PROD.produksi[k].pj}`], { keepNext: true }));
  C.push(...table(`Rilis, respons pemerintah, dan pemberitaan — ${NAMA_ISU[k]}`, [1450, 2000, 3622, 800, 1200],
    ["Rilis", "Tuntutan", "Respons pemerintah", "Berita (WALHI)", "Skor"],
    rs.map(r => {
      const pen = r.penutur.startsWith("pengkampanye") ? (r.pj_pengkampanye || "pengkampanye") : r.penutur.startsWith("pimpinan") ? "pimpinan/Hukum" : "penutur ?";
      return [`${r.id} · ${tgl(r.tanggal)} · ${pen}`, (RING[r.id] || {}).narasi_singkat || r.tuntutan, (RING[r.id] || {}).respons_singkat || "",
        `${r.berita_kasus} (${r.berita_memuat_walhi})`, LABEL[r.skor] + (r.kecocokan_tindakan === "generik" ? " (generik)" : "")];
    }), { fills: rs.map(r => fill[r.skor]) }));
});

// 7. Catatan
C.push(H1("7. Catatan"));
const SP = PROD.suara_pimpinan;
C.push(B([{ t: "Suara pimpinan dan Hukum (catatan, bukan capaian bidang). ", b: true }, Object.entries(SP).sort((a, b) => b[1].rilis - a[1].rilis).map(([n, v]) => `${n} (${v.peran}) dikutip di ${v.rilis} rilis`).join("; ") + "."]));
C.push(B([{ t: "Momen lembaga. ", b: true }, "Rilis dengan tuntutan umum (81 Tahun Merdeka, pidato kenegaraan, hak alam, Hari Keadilan Ekologis, Dua Tahun Prabowo) dan rilis Rempang (Hukum) tidak dikode per isu. Untuk Rempang tidak ditemukan tanggapan BP Batam atau Polda Kepri setelah 22 Sep."]));
C.push(B([{ t: "Respons pemerintah asing. ", b: true }, RING.R37.respons_singkat.replace("(Pemerintah asing) ", "")]));
C.push(B([{ t: "Kontra-narasi. ", b: true }, "Rilis tambak Pantura (24 Sep) diikuti 9 berita kontra-narasi pro-PSN pada hari yang sama, 6 di antaranya menyebut WALHI. Ini dicatat sebagai respons tidak langsung, tidak diberi skor."]));
C.push(B([{ t: "Rilis belum dikode. ", b: true }, `${BELUM.length} rilis publik Agu–Okt belum masuk daftar, kebanyakan dugaan rilis WALHI daerah (Tabel ${tN + 1}).`]));
C.push(...table("Rilis publik Agu–Okt yang belum dikode", [1000, 4772, 1700, 1600], ["Tanggal", "Judul", "Isu dugaan", "Asal dugaan"],
  BELUM.map(b => [tgl(b.tanggal), b.judul, b.isu_dugaan, b.asal_dugaan])));

// 8. Metode
C.push(H1("8. Metode Singkat"));
C.push(
  B("Daftar rilis: tabel rilis Laporan Divisi Kampanye Juli–Oktober 2026 (43 baris, 42 rilis unik). Rilis publik WALHI di luar daftar itu dicatat terpisah."),
  B("Atribusi bidang: rilis masuk bidang pengkampanye yang dikutip atau menjadi narahubung; bila hanya pimpinan atau Hukum yang bicara, rilis masuk isu pemilik topik tanpa dikreditkan ke pengkampanye."),
  B("Respons: dicari dari tanggal rilis sampai 2 Nov 2026, dari lembaga yang dituju atau yang berwenang, termasuk respons kepada jejaring yang membawa tuntutan sama. Respons sebelum tanggal rilis tidak dihitung."),
  B("Pemeriksaan: tiap rilis dikode satu agen dan diperiksa agen kedua yang bertugas membantah skor. Klaim tindakan nyata diperiksa ulang penyunting: satu dikeluarkan (Singapura) dan dua ditandai generik."),
  B("Berita: kata kunci kasus, nama jejaring, dan nama pengkampanye (termasuk salah ketik); isi berita dibaca otomatis. Situs yang memblokir pembaca otomatis tidak ditembus; untuk situs itu dipakai indeks Google."),
  B("Keterbatasan: jumlah rilis per isu kecil, satu skor menggeser persentase 17–50 poin; sebagian bukti hanya dari satu media; kalibrasi terhadap kliping PELA dan hitungan manual nama pengkampanye belum selesai. Data lengkap: respons_final.csv, tindakan_unik.csv, produksi_rilis.json."),
);

const doc = new Document({
  creator: "Tim kampanye", title: "Capaian Kampanye WALHI Agu–Okt 2026",
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", run: { size: 36, bold: true, font: FONT, color: "1F3864" }, paragraph: { spacing: { after: 80 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 28, bold: true, font: FONT, color: "1F3864" }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 0, keepNext: true } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: FONT, color: "2E5496" }, paragraph: { spacing: { before: 220, after: 80 }, outlineLevel: 1, keepNext: true } },
      { id: "Caption", name: "Caption", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 19, font: FONT }, paragraph: { spacing: { before: 40, after: 20 } } },
      { id: "Src", name: "Source Note", basedOn: "Normal", next: "Normal", run: { size: 17, italics: true, color: "595959", font: FONT }, paragraph: { spacing: { after: 100 } } },
    ],
  },
  numbering: { config: [{ reference: "b", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 283 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18 })] })] }) },
    children: C,
  }],
});
const out = path.join(HERE, "laporan-capaian-kampanye-walhi-agu-okt-2026.docx");
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log("ok", out); });

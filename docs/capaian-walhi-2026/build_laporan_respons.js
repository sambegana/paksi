// Laporan respons pemerintah atas rilis kampanye WALHI Agu–Okt 2026.
// Jalankan: python3 final_respons.py && python3 make_figures_respons.py && node build_laporan_respons.js
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
const C = [];
C.push(
  new Paragraph({ children: [new TextRun({ text: "LAPORAN KAMPANYE", bold: true, size: 20, color: "595959" })], spacing: { after: 60 } }),
  new Paragraph({ style: "Title", children: [new TextRun("Respons Pemerintah atas Rilis Kampanye WALHI")] }),
  new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: "Rilis 1 Agustus – 31 Oktober 2026 · respons dihitung sampai 2 November 2026 · draf untuk dicek tim", italics: true, color: "404040" })] }),
);

// 1. Ringkasan
C.push(H1("1. Ringkasan"));
C.push(
  B([{ t: "Respons. ", b: true }, `Dari ${tot.rilis} rilis kampanye, ${tot.ada_respons} (${pct(tot.pct_ada_respons)}) mendapat respons pemerintah. Tetapi hanya ${tot.tindakan_nyata} (${pct(tot.pct_tindakan_nyata)}) yang berujung tindakan nyata. Tidak ada tuntutan yang dipenuhi penuh.`]),
  B([{ t: "Tindakan nyata hanya ada di karhutla. ", b: true }, `Ada ${T.length} tindakan unik: pembekuan dan pencabutan izin, penyegelan, penetapan korporasi tersangka, penyerahan data pemilik manfaat, penyidikan laporan WALHI Kalsel, dan rumah oksigen gratis bagi korban asap. Semuanya terkait karhutla.`]),
  B([{ t: "Atribusi langsung ke WALHI hanya dua. ", b: true }, "4 dari 5 izin yang dicabut Kemenhut (21 Sep) ada di daftar laporan WALHI, dan Kapolda Kalsel menyebut laporan WALHI Kalsel naik ke penyidikan. Tindakan lain searah tetapi tidak menyebut WALHI, dan sebagian menyusul arahan Presiden."]),
  B([{ t: "Isu lain direspons tanpa tindakan. ", b: true }, `Urban direspons di semua rilis (${S["Urban"].rilis}), tetapi responsnya penolakan atau janji. Pesisir & Laut (${pct(S["Pesisir & Laut"].pct_ada_respons)}), Iklim (${pct(S["Iklim & Isu Global"].pct_ada_respons)}) dan Tambang & Energi (${pct(S["Tambang & Energi"].pct_ada_respons)}) paling jarang direspons, tanpa satu pun tindakan nyata.`]),
);
C.push(...table("Respons pemerintah per isu kampanye", [2300, 900, 1250, 1100, 1150, 1222, 1150],
  ["Isu", "Rilis", "Dibawakan pengkampanye", "Ada respons", "Tindakan nyata", "Bentuk respons terbanyak", "Median hari ke respons"],
  [...ISU.map(k => { const s = S[k]; const bent = [["ditolak", s.ditolak], ["dijanjikan", s.dijanjikan], ["tindakan", s.tindakan_parsial], ["tidak ada", s.rilis - s.ada_respons]].sort((a, b) => b[1] - a[1])[0][0];
    return [NAMA_ISU[k], String(s.rilis), String(s.oleh_pengkampanye), `${s.ada_respons} (${pct(s.pct_ada_respons)})`, `${s.tindakan_nyata} (${pct(s.pct_tindakan_nyata)})`, bent, s.median_hari_ke_respons == null ? "–" : String(s.median_hari_ke_respons)]; }),
   [{ t: "Semua isu", b: true }, { t: String(tot.rilis), b: true }, "", { t: `${tot.ada_respons} (${pct(tot.pct_ada_respons)})`, b: true }, { t: `${tot.tindakan_nyata} (${pct(tot.pct_tindakan_nyata)})`, b: true }, "", ""]]));
C.push(P([{ t: "Cara membaca: ", b: true }, "skor 0 tidak ada respons; 1 ditolak; 2 diakui atau dijanjikan tanpa tindakan; 3 tindakan terverifikasi yang searah tetapi sebagian; 4 tuntutan dipenuhi. \"Tindakan nyata\" hanya menghitung skor 3 yang menyentuh inti atau sebagian tuntutan, tidak termasuk tindakan karhutla umum yang dipakai sebagai bukti di rilis lain (\"tindakan generik\")."]));
C.push(...fig("gambar-1-tangga-respons-per-isu.png", "Respons tertinggi pemerintah atas tiap rilis, per isu", "pengodean penulis (verifikasi adversarial), Agu–Okt 2026."));
C.push(P("Hutan & Kebun adalah satu-satunya isu dengan banyak tindakan nyata (8 dari 15 rilis). Pesisir & Laut dan Tambang & Energi didominasi \"tidak ada respons\". Urban tidak punya rilis yang diabaikan, tetapi semua responsnya berhenti di penolakan atau janji."));
C.push(...fig("gambar-2-respons-vs-tindakan.png", "Persentase rilis yang direspons dan yang berujung tindakan nyata", "pengodean penulis."));

// 2. Tindakan nyata
C.push(new Paragraph({ children: [new PageBreak()] }));
C.push(H1("2. Tindakan Nyata (Outcome)"));
C.push(P(`Satu tindakan pemerintah sering menjawab beberapa rilis sekaligus. Karena itu tindakan dihitung sekali di tabel ini (${T.length} tindakan unik), lalu dikaitkan ke rilis yang tuntutannya disentuh.`));
const urut = [...T].sort((a, b) => a.tanggal.localeCompare(b.tanggal));
C.push(...table("Tindakan nyata pemerintah setelah rilis WALHI", [800, 1500, 3372, 1500, 1900],
  ["Tanggal", "Lembaga", "Tindakan", "Rilis terkait", "Atribusi ke WALHI"],
  urut.map(t => [tgl(t.tanggal), t.lembaga, t.bukti ? [t.tindakan + " ", { t: "[sumber]", link: t.bukti }] : t.tindakan, t.rilis_terkait.split(";").join(", "), t.atribusi]),
  { fills: urut.map(t => /WALHI/.test(t.atribusi) ? "DEEAF6" : undefined) }));
C.push(P([{ t: "Baris berwarna", b: true }, " = tindakan yang terkait langsung dengan WALHI. Baris lain searah dengan tuntutan WALHI tetapi tidak menyebut WALHI (konvergensi). Sebagian menyusul arahan Presiden pada ratas 16 September, jadi tidak bisa diklaim sebagai hasil kampanye semata."]));

// 3. Per isu
C.push(H1("3. Rincian per Isu"));
const fill = { 3: "DEEAF6", 2: "F2F2F2" };
ISU.forEach((k, i) => {
  const s = S[k]; const rs = hitung.filter(r => r.isu === k).sort((a, b) => b.skor - a.skor || a.tanggal.localeCompare(b.tanggal));
  C.push(H2(`3.${i + 1} ${NAMA_ISU[k]}`));
  C.push(P([{ t: `${s.rilis} rilis · ${s.ada_respons} direspons · ${s.tindakan_nyata} tindakan nyata`, b: true }, ` · dibawakan pengkampanye ${s.oleh_pengkampanye}, pimpinan/Hukum ${s.oleh_pimpinan_hukum}${s.penutur_tidak_diketahui ? `, penutur belum diketahui ${s.penutur_tidak_diketahui}` : ""}`], { keepNext: true }));
  C.push(...table(`Rilis dan respons pemerintah — ${NAMA_ISU[k]}`, [1550, 2200, 4022, 1300],
    ["Rilis", "Tuntutan", "Respons pemerintah", "Skor"],
    rs.map(r => {
      const pen = r.penutur.startsWith("pengkampanye") ? (r.pj_pengkampanye || "pengkampanye") : r.penutur.startsWith("pimpinan") ? "pimpinan/Hukum" : "penutur ?";
      const lab = LABEL[r.skor] + (r.kecocokan_tindakan === "generik" ? " (generik)" : "");
      return [`${r.id} · ${tgl(r.tanggal)} · ${pen}`, (RING[r.id] || {}).narasi_singkat || r.tuntutan, (RING[r.id] || {}).respons_singkat || "", lab];
    }), { fills: rs.map(r => fill[r.skor]) }));
});

// 4. Catatan
C.push(H1("4. Catatan"));
C.push(B([{ t: "Suara lembaga di luar statistik isu. ", b: true }, "Rilis momen lembaga dengan tuntutan umum (81 Tahun Merdeka, pidato kenegaraan, hak alam, Hari Keadilan Ekologis, Dua Tahun Prabowo) dan rilis Rempang (Hukum) tidak dikode per isu. Untuk Rempang tidak ditemukan tanggapan BP Batam atau Polda Kepri setelah 22 Sep."]));
C.push(B([{ t: "Respons pemerintah asing. ", b: true }, RING.R37.respons_singkat.replace("(Pemerintah asing) ", "")]));
C.push(B([{ t: "Kontra-narasi. ", b: true }, "Rilis tambak Pantura (24 Sep) diikuti 9 berita kontra-narasi pro-PSN pada hari yang sama, 6 di antaranya menyebut WALHI. Ini dicatat sebagai respons tidak langsung dan tidak diberi skor."]));
C.push(B([{ t: "Rilis belum dikode. ", b: true }, `${BELUM.length} rilis publik Agu–Okt belum masuk daftar dan perlu dipastikan apakah termasuk rilis Eknas (Tabel ${tN + 1}).`]));
C.push(...table("Rilis publik Agu–Okt yang belum dikode", [1000, 4772, 1700, 1600], ["Tanggal", "Judul", "Isu dugaan", "Asal dugaan"],
  BELUM.map(b => [tgl(b.tanggal), b.judul, b.isu_dugaan, b.asal_dugaan])));

// 5. Metode
C.push(H1("5. Metode Singkat"));
C.push(
  B("Daftar rilis: 37 rilis folder RILIS/2026 (rekap tim), ditambah rilis publik WALHI yang tidak ada di folder dan daftar siaran pers tim PELA."),
  B("Atribusi: rilis masuk isu pemilik topik. Bila hanya pimpinan atau Hukum yang bicara (Boy, Uli, Dana, Teo, Christine, Melva, Tubagus), rilis tetap dihitung di isu itu tetapi tidak dikreditkan ke pengkampanye."),
  B("Respons: dicari dari tanggal rilis sampai 2 Nov 2026, dari lembaga yang dituju atau yang berwenang, termasuk respons kepada jejaring yang membawa tuntutan sama (mis. KOMPI, KIARA, Greenpeace). Respons sebelum tanggal rilis tidak dihitung."),
  B("Pemeriksaan: setiap rilis dikode satu agen dan diperiksa agen kedua yang bertugas membantah skor. Klaim tindakan nyata diperiksa ulang penyunting; satu dikeluarkan (Singapura) dan dua ditandai generik."),
  B("Berita: dicari per kasus (H-1 s.d. H+14) dengan kata kunci kasus, nama jejaring, dan nama pengkampanye; isi berita dibaca untuk mendeteksi sebutan WALHI dan penutur. Situs yang memblokir pembaca otomatis tidak ditembus."),
  B("Keterbatasan: satu skor menggeser persentase isu kecil sebesar 20–33 poin; sebagian bukti hanya dari satu media; kalibrasi terhadap kliping PELA dan hitungan manual nama pengkampanye belum selesai."),
  B("Data lengkap per rilis, termasuk kutipan respons dan alasan skor: respons_final.csv; tindakan unik: tindakan_unik.csv."),
);

const doc = new Document({
  creator: "Tim kampanye", title: "Respons Pemerintah atas Rilis Kampanye WALHI Agu–Okt 2026",
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
const out = path.join(HERE, "laporan-respons-rilis-agu-okt-2026.docx");
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log("ok", out); });

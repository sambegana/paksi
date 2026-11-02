// Laporan ringkas Capaian WALHI per isu: node build_docx.js (jalankan make_figures.py dulu)
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, AlignmentType,
  HeadingLevel, BorderStyle, ShadingType, LevelFormat, Footer, PageNumber, ExternalHyperlink, TableLayoutType,
} = require("docx");

const HERE = __dirname, FIG = path.join(HERE, "figures");
const S = JSON.parse(fs.readFileSync(path.join(FIG, "ringkasan.json"), "utf8"));
const PJ = JSON.parse(fs.readFileSync(path.join(HERE, "penjelasan.json"), "utf8"));

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
const rows = parseCSV("narasi_respons.csv");
const ISU = ["Pesisir & Laut", "Hutan & Kebun", "Tambang & Energi", "Perkotaan & Tata Ruang", "Iklim & Global", "Ekosistem Esensial & Pangan"];
const JUDUL = {
  "Pesisir & Laut": "Perlindungan Pesisir dan Laut", "Hutan & Kebun": "Hutan dan Kebun",
  "Tambang & Energi": "Tambang dan Energi Berkeadilan", "Perkotaan & Tata Ruang": "Isu Perkotaan dan Kebijakan Tata Ruang",
  "Iklim & Global": "Iklim dan Isu Global", "Ekosistem Esensial & Pangan": "Ekosistem Esensial dan Pangan",
};
const SKOR = { 0: "Tidak ada respons", 1: "Ditolak", 2: "Diakui retoris", 3: "Tindakan parsial", 4: "Diadopsi penuh" };
const pct = x => `${Math.round(x)}%`;
const FONT = "Calibri", CW = 9072;
const bd = { style: BorderStyle.SINGLE, size: 4, color: "808080" };
const borders = { top: bd, bottom: bd, left: bd, right: bd };

const run = (x, o = {}) => (Array.isArray(x) ? x : [x]).map(r => typeof r === "string" ? new TextRun({ text: r, ...o })
  : r.link ? new ExternalHyperlink({ link: r.link, children: [new TextRun({ text: r.t, style: "Hyperlink", ...o })] })
    : new TextRun({ text: r.t, bold: r.b, italics: r.i, ...o }));
const P = (x, o = {}) => new Paragraph({ children: run(x), spacing: { after: 120, line: 276 }, ...o });
const H1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const H2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const B = x => new Paragraph({ numbering: { reference: "b", level: 0 }, children: run(x), spacing: { after: 60, line: 276 } });

let fN = 0, tN = 0;
function fig(file, cap, src = "Google News RSS dan pengodean penulis.") {
  fN++;
  const f = path.join(FIG, file), b = fs.readFileSync(f), w = b.readUInt32BE(16), h = b.readUInt32BE(20);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 120, after: 40 },
      children: [new ImageRun({ type: "png", data: b, transformation: { width: 600, height: Math.round(600 * h / w) }, altText: { title: `Gambar ${fN}`, description: cap, name: file } })] }),
    new Paragraph({ style: "Caption", keepNext: true, children: [new TextRun({ text: `Gambar ${fN}. `, bold: true }), new TextRun(cap)] }),
    new Paragraph({ style: "Src", children: [new TextRun(`Sumber: ${src}`)] }),
  ];
}
function table(cap, widths, head, body, o = {}) {
  tN++;
  const size = o.size || 19;
  const cell = (t, w, hd, al, fill) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA }, margins: { top: 40, bottom: 40, left: 80, right: 80 },
    shading: hd ? { fill: "D9D9D9", type: ShadingType.CLEAR, color: "auto" } : fill ? { fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    children: [new Paragraph({ alignment: al || AlignmentType.LEFT, children: run(t, { size, bold: hd || undefined }) })],
  });
  const al = o.aligns || [];
  return [
    new Paragraph({ style: "Caption", keepNext: true, spacing: { before: 160, after: 60 }, children: [new TextRun({ text: `Tabel ${tN}. `, bold: true }), new TextRun(cap)] }),
    new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: [
      new TableRow({ tableHeader: true, children: head.map((t, i) => cell(t, widths[i], true, al[i])) }),
      ...body.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, widths[i], false, al[i], o.fills && o.fills[ri])) })),
    ] }),
    new Paragraph({ spacing: { after: 120 }, children: [] }),
  ];
}

const R = S.R, A = S.all, C = [];
C.push(
  new Paragraph({ children: [new TextRun({ text: "LAPORAN RINGKAS", bold: true, size: 20, color: "595959" })], spacing: { after: 60 } }),
  new Paragraph({ style: "Title", children: [new TextRun("Capaian WALHI per Isu Kampanye: Pemberitaan dan Respons Pemerintah")] }),
  new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: "Periode 1 Juni – 2 November 2026", italics: true, color: "404040" })] }),
);

// 1. Ringkasan
C.push(H1("1. Ringkasan"));
const hi = [...ISU].sort((a, b) => R[b].respons - R[a].respons);
C.push(
  B([{ t: "Pemberitaan. ", b: true }, `WALHI muncul di ${S.total_judul} judul berita. ${PJ._ringkasan.pemberitaan}`]),
  B([{ t: "Respons pemerintah. ", b: true }, `Rata-rata ${pct(A.respons)} narasi WALHI mendapat respons pemerintah, tetapi hanya ${pct(A.tindakan)} yang berupa tindakan nyata (n = ${A.n} narasi, 6 isu).`]),
  B([{ t: "Per isu. ", b: true }, PJ._ringkasan.per_isu]),
);
C.push(...table("Pemberitaan dan respons pemerintah per isu kampanye", [2772, 1100, 1000, 1000, 1600, 1600],
  ["Isu kampanye", "Judul berita", "Media", "Narasi dikode", "Ada respons", "Tindakan nyata"],
  [...ISU.map(k => [JUDUL[k], String(S.judul[k]), String(S.media[k]), String(R[k].n), pct(R[k].respons), pct(R[k].tindakan)]),
   [{ t: "Semua isu", b: true }, { t: String(S.total_judul), b: true }, "", { t: String(A.n), b: true }, { t: pct(A.respons), b: true }, { t: pct(A.tindakan), b: true }]],
  { aligns: [AlignmentType.LEFT, ...Array(5).fill(AlignmentType.CENTER)] }));
C.push(P([{ t: "Cara membaca: ", b: true }, "“Ada respons” = pemerintah menanggapi dalam bentuk apa pun (skor ≥ 1). “Tindakan nyata” = ada tindakan yang bisa diverifikasi (skor ≥ 3). Skala skor: 0 tidak ada respons, 1 ditolak, 2 diakui secara retoris, 3 tindakan parsial, 4 diadopsi penuh."]));
C.push(...fig("gambar-1-berita-per-isu.png", "Jumlah judul berita yang memuat WALHI per isu kampanye"));
C.push(P(PJ._gambar1));
C.push(...fig("gambar-2-respons-per-isu.png", "Tingkat respons pemerintah atas narasi WALHI per isu kampanye"));
C.push(P(PJ._gambar2));

// 2. Per isu
C.push(H1("2. Capaian per Isu"));
const fills = { 3: "DEEAF6", 4: "BDD7EE" };
ISU.forEach((k, i) => {
  C.push(H2(`2.${i + 1} ${JUDUL[k]}`));
  C.push(P([{ t: `${S.judul[k]} judul berita · ${S.media[k]} media · respons ${pct(R[k].respons)} · tindakan nyata ${pct(R[k].tindakan)}`, b: true }]));
  C.push(P(PJ[k]));
  C.push(...fig(`gambar-${i + 3}-${S.slug[k]}.png`, `Skor respons pemerintah per narasi WALHI — ${JUDUL[k]}`));
  const rs = rows.filter(r => r.isu === k);
  C.push(...table(`Narasi WALHI dan respons pemerintah — ${JUDUL[k]}`, [3100, 4572, 1400],
    ["Narasi WALHI (tanggal · lembaga dituju)", "Respons pemerintah", "Skor"],
    rs.map(r => [`${r.narasi_walhi} (${r.tanggal} · ${r.alamat})`, r.url_respons ? [r.respons_pemerintah + " ", { t: "[sumber]", link: r.url_respons }] : r.respons_pemerintah, `${r.skor} – ${SKOR[r.skor]}`]),
    { size: 18, fills: rs.map(r => fills[r.skor]) }));
});

// 3. Catatan
C.push(H1("3. Catatan Metode"));
C.push(
  B(`Data pemberitaan: semua judul berita Google News yang memuat “WALHI”, diambil per 2 hari selama 1 Juni – 2 November 2026. Judul ganda dan berita dari kanal milik WALHI dibuang (${S.kanal_sendiri} judul). Judul dipilah ke isu dengan kata kunci; ${S.lainnya} judul tidak masuk isu mana pun (umumnya kebencanaan dan kegiatan organisasi).`),
  B("Narasi yang dikode: per isu, tuntutan WALHI dikelompokkan, lalu diambil kelompok dengan judul terbanyak (maksimal 6). Pemilihan tidak melihat ada atau tidaknya respons."),
  B("Skor = respons tertinggi dari lembaga yang dituju setelah narasi muncul. Tindakan yang searah tetapi tidak menyebut WALHI tetap dihitung; artinya searah, belum tentu karena WALHI."),
  B("Keterbatasan: Google News tidak mencakup TV, cetak, dan media sosial; jumlah narasi per isu kecil (satu skor menggeser persentase ±17 poin); dikode satu orang tanpa uji antar-pengode."),
);

const doc = new Document({
  creator: "Analisis media", title: "Capaian WALHI per Isu Kampanye 2026",
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", run: { size: 36, bold: true, font: FONT, color: "1F3864" }, paragraph: { spacing: { after: 80 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 28, bold: true, font: FONT, color: "1F3864" }, paragraph: { spacing: { before: 300, after: 120 }, outlineLevel: 0, keepNext: true } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: FONT, color: "2E5496" }, paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1, keepNext: true } },
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
const out = path.join(HERE, "capaian-walhi-per-isu-2026.docx");
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log("ok", out); });

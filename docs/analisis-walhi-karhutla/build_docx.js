// Susun laporan Word: node build_docx.js  (jalankan make_figures.py lebih dulu)
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, BorderStyle, ShadingType, LevelFormat, Footer, Header, PageNumber,
  ExternalHyperlink, PageBreak, TableLayoutType, VerticalAlign,
} = require("docx");

const HERE = __dirname;
const FIG = path.join(HERE, "figures");
const S = JSON.parse(fs.readFileSync(path.join(FIG, "ringkasan.json"), "utf8"));

// ---------- util ----------
function parseCSV(file) {
  const txt = fs.readFileSync(path.join(HERE, file), "utf8").trim();
  const rows = [];
  let row = [], cur = "", q = false;
  for (let i = 0; i < txt.length; i++) {
    const c = txt[i];
    if (q) {
      if (c === '"' && txt[i + 1] === '"') { cur += '"'; i++; }
      else if (c === '"') q = false;
      else cur += c;
    } else if (c === '"') q = true;
    else if (c === ",") { row.push(cur); cur = ""; }
    else if (c === "\n") { row.push(cur); rows.push(row); row = []; cur = ""; }
    else if (c !== "\r") cur += c;
  }
  row.push(cur); rows.push(row);
  const h = rows.shift();
  return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]])));
}
const coding = parseCSV("coding_respons.csv");
const weekly = parseCSV("headline_mentions_weekly.csv");

const id = (x, d = 0) => Number(x).toLocaleString("id-ID", { minimumFractionDigits: d, maximumFractionDigits: d });
const pct = (x, d = 0) => id(x, d) + "%";

function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

const FONT = "Calibri";
const CONTENT_W = 9072; // A4 11906 − 2 × 1417 (2,5 cm)
const border = { style: BorderStyle.SINGLE, size: 4, color: "808080" };
const borders = { top: border, bottom: border, left: border, right: border };

// runs: string atau array berisi string / {t, b, i}
function runs(x, base = {}) {
  const arr = Array.isArray(x) ? x : [x];
  return arr.map(r => typeof r === "string"
    ? new TextRun({ text: r, ...base })
    : r.link ? new ExternalHyperlink({ link: r.link, children: [new TextRun({ text: r.t, style: "Hyperlink", ...base })] })
      : new TextRun({ text: r.t, bold: r.b, italics: r.i, ...base }));
}
const P = (x, opt = {}) => new Paragraph({ children: runs(x), spacing: { after: 120, line: 276 }, alignment: AlignmentType.JUSTIFIED, ...opt });
const H1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const H2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const B = (x, level = 0) => new Paragraph({ numbering: { reference: "bullets", level }, children: runs(x), spacing: { after: 60, line: 276 } });
let listInst = 0;
const newList = () => { listInst++; };
const N = (x) => new Paragraph({ numbering: { reference: "numbers", level: 0, instance: listInst }, children: runs(x), spacing: { after: 60, line: 276 } });

let figNo = 0, tabNo = 0;
function figure(file, caption, source, explanation) {
  figNo++;
  const f = path.join(FIG, file);
  const { w, h } = pngSize(f);
  const width = 600;
  const out = [
    new Paragraph({ keepNext: true, spacing: { before: 120, after: 60 }, alignment: AlignmentType.CENTER,
      children: [new ImageRun({ type: "png", data: fs.readFileSync(f), transformation: { width, height: Math.round(width * h / w) },
        altText: { title: `Gambar ${figNo}`, description: caption, name: file } })] }),
    new Paragraph({ style: "Caption", keepNext: true, children: [new TextRun({ text: `Gambar ${figNo}. `, bold: true }), ...runs(caption)] }),
    new Paragraph({ style: "SourceNote", children: runs(["Sumber: ", ...[].concat(source)]) }),
  ];
  if (explanation) {
    out.push(new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun({ text: `Penjelasan Gambar ${figNo}`, bold: true })] }));
    for (const e of explanation) out.push(typeof e === "string" || Array.isArray(e) ? P(e) : e);
  }
  return out;
}

function table(caption, widths, header, rows, opt = {}) {
  tabNo++;
  const size = opt.size || 20;
  const cell = (txt, w, isHead, align, fill) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA }, verticalAlign: VerticalAlign.TOP,
    shading: isHead ? { fill: "D9D9D9", type: ShadingType.CLEAR, color: "auto" } : fill ? { fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 50, bottom: 50, left: 90, right: 90 },
    children: [new Paragraph({ alignment: align || AlignmentType.LEFT, children: runs(txt, { size, bold: isHead || undefined }) })],
  });
  const aligns = opt.aligns || [];
  return [
    new Paragraph({ style: "Caption", keepNext: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: `Tabel ${tabNo}. `, bold: true }), ...runs(caption)] }),
    new Table({
      width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED,
      rows: [
        new TableRow({ tableHeader: true, children: header.map((t, i) => cell(t, widths[i], true, aligns[i])) }),
        ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, widths[i], false, aligns[i], opt.fills && opt.fills[ri])) })),
      ],
    }),
    ...(opt.note ? [new Paragraph({ style: "SourceNote", spacing: { before: 60, after: 160 }, children: runs(opt.note) })] : [new Paragraph({ spacing: { after: 120 }, children: [] })]),
  ];
}

// ---------- angka ----------
const T = S.tot;
const [r14any, r14sub, r14idx] = S.rates14;
const [r12any, r12sub, r12idx] = S.rates12;
const wk = S.weekly.WALHI;
const weeks = Object.keys(wk);
const sumW = ks => ks.reduce((a, k) => a + wk[k], 0);
const junjul = weeks.filter(w => w < "2026-08-01");
const okt = weeks.filter(w => w >= "2026-10-01");
const walhiGtKlh = weeks.filter(w => w >= "2026-09-01" && S.weekly.WALHI[w] > S.weekly.KLH[w]).length;
const sepWeeks = weeks.filter(w => w >= "2026-09-01").length;
const SKOR = { 0: "Tidak ada respons", 1: "Ditolak / kontra-narasi", 2: "Diakui secara retoris", 3: "Tindakan parsial", 4: "Diadopsi penuh" };

// ---------- isi ----------
const children = [];

// Judul
children.push(
  new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 80 }, children: [new TextRun({ text: "LAPORAN ANALISIS MEDIA", bold: true, size: 20, color: "595959" })] }),
  new Paragraph({ style: "Title", children: [new TextRun("WALHI sebagai Rujukan Isu Karhutla dan Tingkat Respons Pemerintah terhadap Narasinya")] }),
  new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: "Periode pemberitaan 1 Juni – 2 November 2026 · Studi rintisan (draf untuk disunting)", italics: true, color: "404040" })] }),
);
children.push(...table("Identitas laporan", [2600, 6472], ["Unsur", "Keterangan"], [
  ["Periode data", "1 Juni – 2 November 2026 (22 minggu)"],
  ["Sumber korpus", "Google News RSS (bahasa Indonesia, wilayah ID), kueri mingguan per aktor"],
  ["Ukuran korpus", `${id(3406)} judul unik terambil; ${id(2114)} judul unik menyebut minimal satu aktor; ${id(S.all_total)} penyebutan aktor di judul`],
  ["Unit analisis", "Isu 1: judul berita. Isu 2: narasi/tuntutan WALHI yang dialamatkan ke lembaga pemerintah (n = 14)"],
  ["Status", "Dikode oleh satu pengode; uji reliabilitas antar-pengode belum dilakukan"],
  ["Berkas pendukung", "docs/analisis-walhi-karhutla/ (skrip, data mentah, CSV pengodean, gambar PNG/SVG)"],
]));

// Ringkasan eksekutif
children.push(H1("Ringkasan Eksekutif"));
children.push(
  B([{ t: "Isu 1 — didukung, dengan catatan. ", b: true }, `WALHI muncul di ${id(T.WALHI)} judul berita karhutla, tidak termasuk kanal milik WALHI sendiri. Angka ini setara ${pct(S.walhi_share_nonstate, 1)} dari judul yang menyebut aktor non-pemerintah, dan lebih tinggi dari KLH (${id(T.KLH)} judul). Hanya BNPB dan Kemenhut yang lebih sering muncul.`]),
  B([{ t: "Isu 1 — tren menguat. ", b: true }, `Rata-rata judul WALHI naik dari ${id(sumW(junjul) / junjul.length, 1)} per minggu (Juni–Juli) menjadi ${id(sumW(okt) / okt.length, 1)} per minggu (Oktober).`]),
  B([{ t: "Isu 2 — respons ada, tindakan sedikit. ", b: true }, `Dari ${S.n14} tuntutan WALHI, ${pct(r14any)} mendapat respons dalam bentuk apa pun. Hanya ${pct(r14sub)} yang dijawab dengan tindakan nyata. Tidak ada tuntutan yang diadopsi penuh. Indeks responsivitas tertimbang ${pct(r14idx)}.`]),
  B([{ t: "Catatan metodologis. ", b: true }, `Angka Isu 2 bergantung pada definisi. Dengan unit hitung ${S.n12} narasi, hasilnya ${pct(r12any)} (ada respons) dan ${pct(r12sub)} (tindakan nyata). Laporan ini menyarankan kedua angka ditulis berdampingan dengan definisinya.`]),
);
children.push(P([{ t: "Usulan rumusan kalimat:", b: true }]));
newList();
children.push(
  N([`“WALHI menjadi rujukan utama masyarakat sipil dalam pemberitaan karhutla 2026: ${pct(S.walhi_share_nonstate)} judul berita yang menyebut aktor non-pemerintah memuat WALHI, dan jumlahnya meningkat tajam sejak Agustus.”`]),
  N([`“Rata-rata ${pct(r14any)} narasi WALHI mendapat respons pemerintah, tetapi hanya ${pct(r14sub)} yang berupa tindakan substantif.”`]),
);

// 1 Pendahuluan
children.push(H1("1. Pendahuluan"));
children.push(H2("1.1 Latar belakang"));
children.push(P("Kebakaran hutan dan lahan (karhutla) 2026 meluas. Data SiPongi Kementerian Kehutanan mencatat 202.004 ha terbakar pada Januari–Juli 2026, naik 69% dibanding periode yang sama tahun 2025. Kalimantan dan Papua menjadi episentrum. Selama periode ini WALHI aktif merilis data titik panas di konsesi, daftar perusahaan, dan tuntutan penegakan hukum."));
children.push(H2("1.2 Pertanyaan analisis"));
children.push(P("Laporan ini menguji dua pernyataan sebagai hipotesis:"));
children.push(
  B([{ t: "P1. ", b: true }, "WALHI menjadi rujukan isu lingkungan di Indonesia, khususnya isu karhutla yang sedang menguat."]),
  B([{ t: "P2. ", b: true }, "Berapa rata-rata tingkat respons pemerintah atas narasi yang disampaikan WALHI?"]),
);

// 2 Metodologi
children.push(H1("2. Metodologi"));
children.push(H2("2.1 Kerangka yang dipakai"));
children.push(P("Desain analisis memakai analisis isi kuantitatif sebagai metode inti. Teori agenda-setting dan konsep primary definers dipakai untuk Isu 1. Teori agenda-building dan pembedaan respons simbolik–substantif dipakai untuk Isu 2."));
children.push(...table("Kerangka teori dan metode", [2700, 2900, 3472], ["Kerangka", "Rujukan", "Dipakai untuk"], [
  ["Analisis isi kuantitatif", "Krippendorff (2018); Neuendorf (2017)", "Unit analisis, kategori, aturan pengodean, reliabilitas antar-pengode"],
  ["Agenda-setting", "McCombs & Shaw (1972)", "Volume dan tren pemberitaan sebagai ukuran arti penting isu"],
  ["Primary definers", "Hall dkk. (1978)", "Siapa yang dimuat sebagai sumber yang mendefinisikan isu"],
  ["Framing", "Entman (1993)", "Membaca diagnosis, penyebab, dan solusi dalam narasi WALHI"],
  ["Agenda-building; respons simbolik vs substantif", "Cobb & Elder (1972); Walgrave & Van Aelst (2006)", "Skala respons pemerintah 0–4"],
]));
children.push(...figure("gambar-1-alur-metodologi.png", "Alur metodologi analisis", "disusun penulis.", [
  "Alur dimulai dari definisi aktor dan kata kunci, lalu pengumpulan korpus mingguan. Setelah pembersihan, analisis bercabang. Cabang kiri (Isu 1) menghitung penyebutan aktor di judul. Cabang kanan (Isu 2) menginventaris tuntutan WALHI dan mengode respons pemerintah. Kotak bergaris putus menandai langkah yang belum dilakukan: uji reliabilitas antar-pengode.",
]));
children.push(H2("2.2 Pengumpulan korpus"));
newList();
children.push(
  N(["Untuk tiap aktor, kueri berbentuk “<aktor> karhutla after:<tanggal> before:<tanggal+7>” dikirim ke Google News RSS (hl=id, gl=ID)."]),
  N(["Kueri diulang untuk 22 jendela mingguan, 1 Juni – 2 November 2026. Jendela mingguan dipakai karena RSS membatasi 100 hasil per kueri."]),
  N(["Judul yang sama dalam satu aktor dihitung sekali (deduplikasi judul)."]),
  N([`Berita dari kanal milik aktor sendiri dibuang: ${25} judul dari situs WALHI dan ${8} judul dari situs Greenpeace.`]),
);
children.push(P(`Hasil: ${id(3406)} judul unik terambil. Sebanyak ${id(2114)} judul unik memuat nama minimal satu aktor, dengan total ${id(S.all_total)} penyebutan (satu judul dapat menyebut lebih dari satu aktor). Kata kunci per aktor ada di Lampiran B.`));
children.push(H2("2.3 Pengodean Isu 1"));
children.push(P("Unit analisis Isu 1 adalah judul berita. Judul dipilih karena mencerminkan arti penting (salience) yang diberikan redaksi, dan karena penyebutan di judul adalah kriteria yang lebih ketat daripada penyebutan di badan berita. Aktor dihitung bila namanya muncul di judul. Ukuran yang dilaporkan: jumlah judul per aktor, pangsa di antara aktor non-pemerintah, dan tren mingguan."));
children.push(H2("2.4 Pengodean Isu 2"));
children.push(P("Narasi WALHI diinventaris dari berita dalam korpus. Kriteria inklusi: klaim atau tuntutan spesifik, dialamatkan ke lembaga pemerintah tertentu, dan dimuat media dalam periode data. Tuntutan yang sama ke lembaga berbeda dihitung terpisah (unit 14 tuntutan). Sebagai uji sensitivitas, tiga tuntutan dari satu laporan 15 September digabung (unit 12 narasi, mengambil skor tertinggi)."));
children.push(P("Aturan pengodean: skor yang dicatat adalah respons tertinggi dari lembaga yang dituju, yang terjadi setelah narasi muncul. Tindakan yang searah tetapi tidak menyebut WALHI dicatat sebagai konvergensi kebijakan, bukan bukti pengaruh."));
children.push(...table("Skala respons pemerintah", [900, 2300, 5872], ["Skor", "Kategori", "Definisi operasional"], [
  ["0", SKOR[0], "Tidak ditemukan pernyataan atau tindakan lembaga yang dituju dalam korpus"],
  ["1", SKOR[1], "Lembaga membantah klaim atau menolak tuntutan secara terbuka"],
  ["2", SKOR[2], "Lembaga mengakui isu atau berjanji, tanpa tindakan yang dapat diverifikasi"],
  ["3", SKOR[3], "Ada tindakan yang dapat diverifikasi dan searah dengan tuntutan, tetapi hanya sebagian"],
  ["4", SKOR[4], "Tuntutan dipenuhi seluruhnya"],
], { aligns: [AlignmentType.CENTER] }));
children.push(P("Tiga ukuran dihitung dari skor:"));
children.push(
  B([{ t: "Tingkat respons", b: true }, " = jumlah unit dengan skor ≥ 1 ÷ jumlah unit."]),
  B([{ t: "Tingkat tindakan nyata", b: true }, " = jumlah unit dengan skor ≥ 3 ÷ jumlah unit."]),
  B([{ t: "Indeks tertimbang", b: true }, " = jumlah skor ÷ (4 × jumlah unit)."]),
);
children.push(H2("2.5 Reliabilitas"));
children.push(P("Seluruh pengodean dilakukan oleh satu pengode. Sebelum publikasi, minimal 10% sampel perlu dikode ulang oleh pengode kedua secara independen. Target reliabilitas adalah α Krippendorff ≥ 0,80; nilai 0,667–0,80 hanya layak untuk kesimpulan tentatif (Krippendorff, 2018)."));

// 3 Temuan Isu 1
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("3. Temuan Isu 1: WALHI sebagai Rujukan Karhutla"));
children.push(...figure("gambar-2-tren-mingguan.png", "Jumlah judul berita karhutla per minggu yang menyebut WALHI, Greenpeace, KLH, dan Pantau Gambut, 1 Juni – 2 November 2026",
  "Google News RSS, diolah penulis (Lampiran A).", [
    `Pemberitaan WALHI rendah pada Juni–Juli, rata-rata ${id(sumW(junjul) / junjul.length, 1)} judul per minggu. Lonjakan pertama terjadi pada minggu 17 Agustus (${wk["2026-08-17"]} judul). Pemicunya adalah debat terbuka WALHI dengan Menteri LH di Konsultasi Nasional Lingkungan Hidup, Pekanbaru, 21 Agustus 2026.`,
    `Sejak September, judul WALHI melampaui KLH setiap minggu (${walhiGtKlh} dari ${sepWeeks} minggu). Puncaknya minggu 26 Oktober (${wk["2026-10-26"]} judul), bersamaan dengan penetapan 20 korporasi tersangka oleh Polri dan tuntutan WALHI agar nama korporasi diumumkan.`,
    `Puncak Greenpeace pada minggu 19 Oktober (${S.weekly.Greenpeace["2026-10-19"]} judul) bersifat sesaat. Puncak itu terkait isu kabut asap lintas batas dan perusahaan Malaysia–Singapura. Pola WALHI lebih stabil: sejak 17 Agustus, WALHI bertahan minimal 8 judul per minggu selama 11 minggu berturut-turut.`,
  ]));
children.push(...figure("gambar-3-judul-per-aktor.png", "Jumlah judul berita karhutla yang menyebut tiap aktor, 1 Juni – 2 November 2026",
  "Google News RSS, diolah penulis.", [
    `WALHI menempati posisi ketiga dari sembilan aktor, di bawah dua lembaga pelaksana utama penanganan karhutla: BNPB (${id(T.BNPB)}) dan Kemenhut (${id(T.Kemenhut)}). WALHI muncul lebih sering daripada KLH (${id(T.KLH)}), lembaga yang secara formal memegang urusan lingkungan hidup.`,
    "Angka BNPB dan Kemenhut adalah batas bawah: kueri BNPB mencapai batas 100 hasil pada 6 minggu, dan Kemenhut pada 4 minggu. Urutan aktor tidak berubah karena batas ini.",
  ]));
children.push(...figure("gambar-4-pangsa-nonpemerintah.png", "Pangsa judul berita karhutla di antara aktor non-pemerintah",
  "Google News RSS, diolah penulis.", [
    `Di antara aktor non-pemerintah, WALHI memegang ${pct(S.walhi_share_nonstate, 1)} judul (${id(T.WALHI)} dari ${id(S.nonstate_total)}). Angka ini lebih dari dua kali Greenpeace (${pct(100 * T.Greenpeace / S.nonstate_total, 1)}). Bila akademisi dikeluarkan sehingga hanya organisasi masyarakat sipil yang dibandingkan, pangsa WALHI menjadi ${pct(S.walhi_share_nonstate_no_academia, 1)}.`,
    "Jangkauan WALHI juga lebih luas: judul yang menyebut WALHI dimuat oleh 155 media berbeda, dibanding 89 media untuk Greenpeace. Sebagian berasal dari cabang daerah (WALHI Kalimantan, Papua, Riau), sehingga WALHI hadir di media nasional dan lokal.",
  ]));
children.push(H2("3.1 Interpretasi"));
children.push(P("Data mendukung bahwa WALHI adalah sumber non-pemerintah paling menonjol dalam pemberitaan karhutla 2026. Ada tiga indikasi bahwa WALHI juga diperlakukan sebagai rujukan, bukan hanya sering disebut:"));
children.push(
  B("Kemenhut menanggapi laporan 372 perusahaan dari WALHI sebagai “bahan verifikasi”, dan 4 dari 5 izin yang dicabut pada September ada di daftar WALHI."),
  B("Menteri LH berdebat langsung dengan data WALHI tentang titik api di konsesi dalam forum resmi."),
  B("Media mengutip angka WALHI (jumlah perusahaan, titik panas di konsesi, emisi) sebagai data, bukan hanya sebagai opini."),
);
children.push(P([{ t: "Batas temuan: ", b: true }, "penyebutan di judul mengukur visibilitas. Untuk menyatakan “rujukan” secara kuat, perlu kode tambahan pada badan berita: apakah data WALHI dipakai sebagai fakta, atau WALHI hanya dikutip sebagai pengkritik. Selain itu, angka luas terbakar dari WALHI dikutip berbeda di media (33.837 ha untuk Kalimantan Januari–Juli; 107.649 ha nasional hingga 27 Juli; 895.000 ha untuk 2026). Periode dan wilayahnya berbeda, tetapi perbedaan ini dapat melemahkan kredibilitas WALHI sebagai rujukan data."]));

// 4 Temuan Isu 2
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("4. Temuan Isu 2: Tingkat Respons Pemerintah"));
children.push(P(`Tabel 4 memuat ${S.n14} tuntutan WALHI beserta respons yang ditemukan dan skornya. Kolom skor dapat disunting di berkas coding_respons.csv; jalankan ulang make_figures.py dan build_docx.js untuk memperbarui gambar dan angka.`));
const fills = { 0: undefined, 1: "F2F2F2", 2: "E7E6E6", 3: "DEEAF6", 4: "BDD7EE" };
children.push(...table("Matriks narasi WALHI dan respons pemerintah", [450, 2500, 1300, 3322, 1500],
  ["No", "Narasi / tuntutan WALHI (tanggal)", "Lembaga yang dituju", "Respons pemerintah yang ditemukan", "Skor"],
  coding.map(r => [r.no, `${r.narasi_walhi} (${r.tanggal})`, r.alamat, r.respons_pemerintah, `${r.skor} – ${SKOR[r.skor]}`]),
  { size: 18, aligns: [AlignmentType.CENTER], fills: coding.map(r => fills[r.skor]),
    note: "Sumber: CNN Indonesia (23/10), Betahita (16/9), AFU (21/8), Mongabay (21/10), NU Online (21/9), Wartatrans (14/10), Kompas.id, RMOL (29/10), Katadata (26/10); lengkapnya di Lampiran C." }));
children.push(...figure("gambar-5-skor-per-narasi.png", "Skor respons pemerintah per narasi WALHI (skala 0–4)",
  "Tabel 4, diolah penulis.", [
    "Tiga narasi mendapat skor 3 (tindakan parsial): verifikasi dan sanksi atas 372 perusahaan oleh Kemenhut, pidana korporasi hingga pemilik manfaat, dan pencabutan izin konsesi yang terbakar berulang. Ketiganya berada di ranah penegakan hukum dan perizinan.",
    "Narasi dengan skor 0 berada di ranah struktural dan korban: pemulihan gambut, layanan kesehatan dan evakuasi korban asap, kritik atas label “terorisme ekologi”, serta laporan yang sama kepada KLH dan ATR/BPN.",
    "Narasi 13 (gugatan Pasal 72) baru berumur 7 hari saat data ditutup. Skor 0 untuk narasi ini belum final.",
  ]));
children.push(...figure("gambar-6-distribusi-skor.png", `Distribusi skor respons pemerintah (n = ${S.n14} tuntutan)`,
  "Tabel 4, diolah penulis.", [
    `Separuh tuntutan (${S.dist["0"]} dari ${S.n14}) tidak mendapat respons. Respons yang ada tersebar merata: ${S.dist["1"]} ditolak, ${S.dist["2"]} diakui secara retoris, dan ${S.dist["3"]} dijawab dengan tindakan parsial. Tidak ada tuntutan yang diadopsi penuh.`,
  ]));
children.push(...figure("gambar-7-tingkat-respons.png", "Tingkat respons pemerintah menurut tiga ukuran dan dua unit hitung",
  "Tabel 4, diolah penulis.", [
    `Dengan unit ${S.n14} tuntutan, tingkat respons ${pct(r14any)}, tingkat tindakan nyata ${pct(r14sub)}, dan indeks tertimbang ${pct(r14idx)}. Dengan unit ${S.n12} narasi, ketiganya naik menjadi ${pct(r12any)}, ${pct(r12sub)}, dan ${pct(r12idx)}.`,
    "Selisih antar-unit hitung (8 poin persen untuk tingkat respons) lebih kecil daripada selisih antar-ukuran (29 poin persen antara “ada respons” dan “tindakan nyata”). Artinya, pilihan ukuran lebih menentukan hasil daripada pilihan unit.",
  ]));
children.push(...table("Ringkasan tingkat respons pemerintah", [2500, 3372, 1600, 1600], ["Ukuran", "Rumus", `Unit ${S.n14} tuntutan`, `Unit ${S.n12} narasi`], [
  ["Tingkat respons", "skor ≥ 1 ÷ n", pct(r14any, 1), pct(r12any, 1)],
  ["Tingkat tindakan nyata", "skor ≥ 3 ÷ n", pct(r14sub, 1), pct(r12sub, 1)],
  ["Indeks tertimbang", "Σ skor ÷ (4 × n)", pct(r14idx, 1), pct(r12idx, 1)],
], { aligns: [AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.CENTER] }));
children.push(H2("4.1 Interpretasi"));
children.push(P("Pemerintah cenderung merespons narasi WALHI yang searah dengan agenda pemerintah sendiri, yaitu penegakan hukum terhadap korporasi (termasuk korporasi asing) dan pembekuan izin. Narasi yang menuntut perubahan struktural, pemulihan ekosistem, atau layanan bagi korban hampir tidak direspons."));
children.push(P([{ t: "Batas temuan: ", b: true }, "pola ini adalah hipotesis, bukan bukti sebab-akibat. Tindakan pada narasi 6 dan 11 juga menyusul arahan Presiden pada September 2026. Karena itu skor 3 berarti tindakan pemerintah searah dengan tuntutan WALHI, bukan bahwa tuntutan WALHI menyebabkan tindakan tersebut."]));

// 5 Keterbatasan
children.push(H1("5. Keterbatasan"));
children.push(
  B([{ t: "Cakupan korpus. ", b: true }, "Google News tidak mencakup televisi, media cetak, dan media sosial, dan tidak menjamin semua berita daring terindeks."]),
  B([{ t: "Batas hasil kueri. ", b: true }, "Kueri BNPB (6 minggu) dan Kemenhut (4 minggu) mencapai batas 100 hasil; angka keduanya adalah batas bawah."]),
  B([{ t: "Pencocokan kata kunci. ", b: true }, "Penyebutan aktor dideteksi dengan pola teks pada judul. Singkatan seperti “KLH” dan “IPB” dapat menghasilkan salah hitung kecil."]),
  B([{ t: "Ukuran sampel Isu 2. ", b: true }, `Dengan ${S.n14} tuntutan, perubahan satu skor menggeser tingkat respons sekitar 7 poin persen.`]),
  B([{ t: "Satu pengode. ", b: true }, "Reliabilitas pengodean belum diuji."]),
  B([{ t: "Sensor kanan. ", b: true }, "Tuntutan yang muncul menjelang 2 November belum sempat direspons."]),
);

// 6 Rekomendasi
children.push(H1("6. Rekomendasi"));
children.push(H2("6.1 Penulisan angka dalam laporan"));
children.push(P(`Tuliskan tingkat respons bersama definisinya, misalnya: “${pct(r14any)} narasi mendapat respons pemerintah (skor ≥ 1), ${pct(r14sub)} berupa tindakan nyata (skor ≥ 3); n = ${S.n14} tuntutan, Juni–November 2026.” Angka tunggal tanpa definisi mudah dibantah karena hasilnya berkisar ${pct(r14sub)}–${pct(r12any)}.`));
children.push(H2("6.2 Langkah lanjutan"));
newList();
children.push(
  N("Perluas korpus dengan GDELT DOC 2.0 API atau Media Cloud untuk volume lintas media."),
  N("Ambil isi artikel (bukan hanya judul) dengan trafilatura, lalu kode apakah data WALHI dipakai sebagai fakta atau sebagai kritik."),
  N("Kode ulang 10% sampel oleh pengode kedua dan laporkan α Krippendorff."),
  N("Pisahkan respons langsung (lembaga menyebut WALHI) dari konvergensi kebijakan."),
  N("Ukur jeda waktu antara narasi WALHI dan respons pemerintah."),
);
children.push(...table("Alat pengumpulan berita yang dinilai", [2000, 2300, 1300, 3472], ["Kebutuhan", "Alat", "Kecocokan", "Catatan"], [
  ["Mencari berita per kata kunci dan tanggal", "Google News RSS (dipakai di laporan ini)", "Cocok", "Gratis; mendukung after:/before:; maksimal 100 hasil per kueri"],
  ["Volume dan tren lintas media", "GDELT DOC 2.0 API", "Cocok", "Mendukung bahasa Indonesia; mode timeline volume; banyak dipakai dalam riset media"],
  ["Mengambil isi artikel dari URL", "fhamborg/news-please", "Bisa", "Rujukan akademik (Hamborg dkk., 2017), Apache-2.0; repositori sudah diarsipkan"],
  ["Mengambil isi artikel dari URL", "trafilatura", "Disarankan", "Masih dirawat; unggul pada uji banding ekstraksi teks dan tanggal (Barbaresi, 2021)"],
  ["Scraper khusus media Indonesia", "nichsedge/indoscraping", "Belum cocok", "Hanya 6 situs; tidak ada filter kata kunci atau tanggal untuk berita"],
  ["Google News berbayar", "oxylabs, Decodo", "Tidak perlu", "Membutuhkan proxy berbayar; RSS sudah memadai untuk skala ini"],
]));

// Daftar pustaka
children.push(H1("Daftar Pustaka"));
[
  "Barbaresi, A. (2021). Trafilatura: A web scraping library and command-line tool for text discovery and extraction. Proceedings of ACL-IJCNLP 2021: System Demonstrations, 122–131.",
  "Cobb, R. W., & Elder, C. D. (1972). Participation in American politics: The dynamics of agenda-building. Allyn and Bacon.",
  "Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51–58.",
  "Hall, S., Critcher, C., Jefferson, T., Clarke, J., & Roberts, B. (1978). Policing the crisis: Mugging, the state, and law and order. Macmillan.",
  "Hamborg, F., Meuschke, N., Breitinger, C., & Gipp, B. (2017). news-please: A generic news crawler and extractor. Proceedings of the 15th International Symposium of Information Science, 218–223.",
  "Krippendorff, K. (2018). Content analysis: An introduction to its methodology (4th ed.). SAGE.",
  "McCombs, M. E., & Shaw, D. L. (1972). The agenda-setting function of mass media. Public Opinion Quarterly, 36(2), 176–187.",
  "Neuendorf, K. A. (2017). The content analysis guidebook (2nd ed.). SAGE.",
  "Walgrave, S., & Van Aelst, P. (2006). The contingency of the mass media's political agenda setting power: Toward a preliminary theory. Journal of Communication, 56(1), 88–109.",
].forEach(t => children.push(new Paragraph({ children: [new TextRun(t)], indent: { left: 567, hanging: 567 }, spacing: { after: 100 } })));

// Lampiran
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("Lampiran A. Data Mingguan Judul per Aktor"));
const ACT = ["WALHI", "Greenpeace", "Pantau Gambut", "Auriga", "Madani", "BRGM/Akademisi IPB", "Kemenhut", "KLH", "BNPB"];
const ACTL = ["WALHI", "Green-peace", "Pantau Gambut", "Auriga", "Madani", "Akad. IPB", "Kemen-hut", "KLH", "BNPB"];
const byWeek = {};
weekly.forEach(r => { (byWeek[r.minggu_mulai] ||= {})[r.aktor] = r.judul_menyebut_tanpa_kanal_sendiri; });
const BUL = ["", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"];
const tgl = s => { const [y, m, d] = s.split("-"); return `${+d} ${BUL[+m]}`; };
const wrows = Object.keys(byWeek).sort().map(w => [tgl(w), ...ACT.map(a => byWeek[w][a])]);
wrows.push([{ t: "Total", b: true }, ...ACT.map(a => ({ t: String(T[a]), b: true }))]);
children.push(...table("Jumlah judul yang menyebut aktor per minggu (tanpa kanal milik aktor sendiri)", [1269, ...Array(9).fill(867)],
  ["Minggu mulai", ...ACTL], wrows, { size: 17, aligns: [AlignmentType.LEFT, ...Array(9).fill(AlignmentType.CENTER)],
    note: "Berkas: headline_mentions_weekly.csv. Minggu terakhir (26 Okt) mencakup 26 Oktober – 2 November 2026." }));
children.push(H1("Lampiran B. Kata Kunci per Aktor"));
children.push(...table("Kueri pencarian dan pola pencocokan judul", [2200, 3000, 3872], ["Aktor", "Kueri Google News", "Pola di judul (tidak peka huruf besar/kecil)"], [
  ["WALHI", "walhi karhutla", "walhi"],
  ["Greenpeace", "greenpeace karhutla", "greenpeace"],
  ["Pantau Gambut", "\"pantau gambut\" karhutla", "pantau gambut"],
  ["Auriga", "auriga karhutla", "auriga"],
  ["Madani Berkelanjutan", "\"madani berkelanjutan\" karhutla", "madani"],
  ["Akademisi IPB", "\"ipb\" karhutla", "ipb (kata utuh)"],
  ["Kemenhut", "\"kementerian kehutanan\" OR kemenhut karhutla", "kemenhut | kementerian kehutanan | menhut | raja juli"],
  ["KLH", "\"kementerian lingkungan hidup\" OR KLH karhutla", "klh (kata utuh) | kementerian lingkungan hidup | jumhur | menteri lh"],
  ["BNPB", "bnpb karhutla", "bnpb"],
], { size: 18 }));
children.push(H1("Lampiran C. Sumber Berita Utama untuk Pengodean Isu 2"));
[
  ["CNN Indonesia, 23 Okt 2026 — Walhi-Greenpeace desak pemerintah buka data korporasi pemicu karhutla", "https://www.cnnindonesia.com/nasional/20261023094532-20-1418680/walhi-greenpeace-desak-pemerintah-buka-data-korporasi-pemicu-karhutla"],
  ["Betahita, 16 Sep 2026 — 372 perusahaan terduga karhutla dilaporkan ke 3 kementerian", "https://www.betahita.id/berita/12369/372-perusahaan-terduga-karhutla-dilaporkan-ke-3-kementerian"],
  ["AFU, 21 Agu 2026 — Walhi-Jumhur ribut soal data karhutla di lahan konsesi", "https://afu.id/nasional/walhijumhur-ribut-soal-data-karhutla-di-lahan-konsesi-sawit-dan-tambang-gakkum-klh-malah-segel-perusahaan-sawit"],
  ["Mongabay, 21 Okt 2026 — Berbagai kalangan desak kabut asap dan karhutla jadi bencana nasional", "https://mongabay.co.id/2026/10/21/berbagai-kalangan-desak-kabut-asap-dan-karhutla-jadi-bencana-nasional/"],
  ["NU Online, 21 Sep 2026 — Walhi soroti narasi ‘terorisme ekologi’", "https://nu.or.id/nasional/walhi-soroti-narasi-terorisme-ekologi-dalam-penanganan-karhutla-0953D"],
  ["Wartatrans, 14 Okt 2026 — WALHI ungkap 372 perusahaan, 52 berafiliasi Malaysia dan Singapura", "https://wartatrans.com/walhi-ungkap-372-perusahaan-terindikasi-terkait-karhutla-2026-sebanyak-52-berafiliasi-dengan-malaysia-dan-singapura/"],
  ["Kompas.id — Walhi serahkan data 262 perusahaan terkait karhutla", "https://www.kompas.id/artikel/walhi-serahkan-data-262-perusahaan-terkait-karhutla-ditunggu-tindakan-presiden"],
  ["RMOL, 29 Okt 2026 — 20 korporasi resmi tersangka karhutla", "https://rmol.id/read/2026/10/29/726627/20-korporasi-resmi-tersangka-karhutla-empat-perusahaan-asing"],
  ["Katadata, 26 Okt 2026 — Walhi desak Menhut jalankan UU Kehutanan", "https://katadata.co.id/ekonomi-hijau/ekonomi-sirkular/6adf3e14bbd89/walhi-desak-menhut-jalankan-uu-kehutanan-demi-warga-terdampak-kebakaran-hutan"],
  ["Media Indonesia — Walhi: Kalimantan jadi episentrum karhutla 2026", "https://mediaindonesia.com/nusantara/915941/walhi-kalimantan-jadi-episentrum-karhutla-2026"],
].forEach(([t, u]) => children.push(B([{ t, link: u }])));
children.push(H1("Lampiran D. Berkas Pendukung"));
children.push(...table("Berkas di folder docs/analisis-walhi-karhutla/", [3200, 5872], ["Berkas", "Isi"], [
  ["collect_gnews.py", "Skrip pengumpul korpus dari Google News RSS"],
  ["korpus_gnews_raw.json", "Data mentah: judul, tanggal, dan media per aktor per minggu"],
  ["headline_mentions_weekly.csv", "Jumlah judul per aktor per minggu (Lampiran A)"],
  ["coding_respons.csv", "Matriks pengodean Isu 2 (Tabel 4); sunting skor di sini"],
  ["make_figures.py", "Membuat Gambar 1–7 (PNG 300 dpi dan SVG) di folder figures/"],
  ["build_docx.js", "Menyusun laporan Word ini dari CSV dan gambar"],
], { size: 18 }));

// ---------- dokumen ----------
const doc = new Document({
  creator: "Analisis media",
  title: "WALHI sebagai Rujukan Isu Karhutla dan Tingkat Respons Pemerintah",
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", run: { size: 40, bold: true, font: FONT, color: "1F3864" }, paragraph: { spacing: { after: 120 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 30, bold: true, font: FONT, color: "1F3864" }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0, keepNext: true } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 25, bold: true, font: FONT, color: "2E5496" }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1, keepNext: true } },
      { id: "Caption", name: "Caption", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 20, font: FONT }, paragraph: { spacing: { before: 60, after: 40 } } },
      { id: "SourceNote", name: "Source Note", basedOn: "Normal", next: "Normal", run: { size: 18, italics: true, color: "595959", font: FONT }, paragraph: { spacing: { after: 120 } } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 283 } } } }] },
      { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 283 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: "Analisis Media WALHI & Karhutla 2026 — draf", size: 16, color: "808080" })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18 })] })] }) },
    children,
  }],
});

const out = path.join(HERE, "laporan-analisis-walhi-karhutla-2026.docx");
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log("ok", out, b.length); });

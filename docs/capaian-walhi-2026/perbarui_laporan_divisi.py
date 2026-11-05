"""Perbarui Laporan Divisi Kampanye Juli–Oktober 2026: data pemberitaan, respons, dan gambar.

Pakai: python3 -I perbarui_laporan_divisi.py <folder_docx_terurai> <folder_gambar>
Hanya paragraf berikut yang diubah (indeks paragraf di document.xml asli):
  105, 609, 614  : angka rilis 37 -> 43 (mengikuti tabel rilis di laporan yang sama)
  290, 291       : caption + penjelasan Gambar 1 (rilis per bidang)
  294, 295       : caption + penjelasan Gambar 2 (rilis per bulan)
  296, 297       : paragraf pemberitaan dan respons; disisipkan daftar tindakan nyata
  300, 302       : caption + penjelasan Gambar 3 (pemberitaan); komentar Mida dipertahankan
  304            : caption Gambar 4 (respons)
  307            : kalimat soal isu perkotaan diperbarui
Gambar word/media/image1..4.png diganti; ukuran tinggi (cy) disesuaikan dengan rasio gambar baru.
"""
import os, re, struct, sys
from xml.sax.saxutils import escape

D, FIG = sys.argv[1], sys.argv[2]
P = os.path.join(D, "word", "document.xml")
x = open(P, encoding="utf8").read()
paras = re.findall(r"<w:p[ >].*?</w:p>", x, re.S)
ORIG = {i: paras[i] for i in (105, 290, 291, 294, 295, 296, 297, 300, 302, 304, 307, 609, 614)}


def ppr(p):
    m = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    return m.group(0) if m else ""


def rprs(p):
    return [m.group(1) or "" for m in re.finditer(r"<w:r(?: [^>]*)?>(?:(<w:rPr>.*?</w:rPr>|<w:rPr ?/>))?(?:(?!</w:r>).)*?<w:t", p, re.S)]


def run(text, rpr):
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def para(p_open, pp, runs):
    return f"{p_open}{pp}{''.join(runs)}</w:p>"


def p_open(p):
    return re.match(r"<w:p[^>]*>", p).group(0)


def body(i, text):
    p = ORIG[i]; r = rprs(p)
    return para(p_open(p), ppr(p), [run(text, r[0] if r else "")])


def caption(i, nomor, text):
    p = ORIG[i]; r = rprs(p)
    return para(p_open(p), ppr(p), [run(f"Gambar {nomor}. ", r[0]), run(text, r[1] if len(r) > 1 else "")])


NEW = {}
for i in (105, 609, 614):
    NEW[i] = re.sub(r"(<w:t[^>]*>[^<]*?)37( rilis)", r"\g<1>43\2", ORIG[i])
NEW[290] = caption(290, 1, "Jumlah rilis per bidang, Agustus–Oktober 2026 (43 rilis dalam daftar rilis Divisi Kampanye).")
NEW[291] = body(291, "Hutan & Kebun mendominasi karena musim karhutla. Dari 43 rilis, 12 masuk bidang ini. Pesisir & Laut di urutan kedua "
                "dengan 11 rilis, lalu Urban (7) dan Pangan & Ekosistem (6). Iklim & Isu Global punya 4 rilis, sedangkan Tambang & Energi "
                "hanya 1: aksi warga Jawa soal transisi energi pada Oktober.")
NEW[294] = caption(294, 2, "Rilis per bulan untuk setiap bidang.")
NEW[295] = body(295, "Oktober menjadi puncak dengan 18 rilis. Rilis Hutan & Kebun naik dua kali lipat dari bulan sebelumnya, dan Pangan naik "
                "menjadi 4. Pemicunya kajian aktor karhutla, desakan ke Singapura, isu data center AI, Dua Tahun Prabowo, dan respons "
                "pangan-energi. Pesisir & Laut stabil sepanjang tiga bulan (4, 4, dan 3 rilis) dengan isu RUU Daerah Kepulauan, PSN tambak "
                "Pantura, Giant Sea Wall, dan Batu Beriga. Iklim & Isu Global memuncak pada September, saat emisi karhutla, proyek karbon, "
                "dan pidato BRICS. Pangan kosong di September.")
NEW[296] = body(296, "Bukan hanya itu, WALHI juga menjadi pusat pemberitaan pada media-media mainstream. Sepanjang Agustus–Oktober 2026, "
                "WALHI disebut dalam 1.267 berita di Google News, 843 di antaranya memuat WALHI di judul. Isu Hutan dan Kebun mendominasi "
                "dengan 661 berita dari 259 media, terutama karena momentum karhutla. Isu Pesisir dan Laut tercatat 94 berita dari 64 media "
                "(gabungan pemantauan otomatis dan kliping tim PELA), "
                "termasuk berita tambang, PSN, dan data center yang berlokasi di laut, pesisir, atau pulau kecil. Dari sisi respons "
                "pemerintah, 79% rilis kampanye yang memuat tuntutan spesifik mendapat respons, tetapi hanya 24% yang berujung tindakan nyata.")
NEW[297] = body(297, "Temuan ini didasarkan pada pengodean 33 rilis yang memuat tuntutan spesifik kepada pemerintah; rilis momen lembaga, "
                "rilis berstatus draf, dan desakan kepada pemerintah Singapura tidak dihitung. Respons dicari dari tanggal rilis sampai "
                "2 November 2026, termasuk respons kepada jejaring yang membawa tuntutan yang sama, lalu diperiksa ulang. Hutan & Kebun "
                "mencatat capaian tertinggi: seluruh 10 rilis direspons dan 6 berujung tindakan nyata. Urban direspons di seluruh 5 rilis, "
                "tetapi responsnya berupa penolakan atau janji. Pesisir & Laut direspons di 5 dari 9 rilis (56%) dengan satu tindakan nyata: "
                "DPRD Babel berpihak pada warga nelayan dan WALHI serta menjalankan revisi Perda RZWP3K agar Batu Beriga keluar dari zona "
                "tambang. Respons lain masih berupa penolakan atau janji, misalnya KKP tetap menjalankan PSN tambak Pantura. Pangan & Ekosistem Esensial direspons di 4 dari 5 rilis dengan satu tindakan nyata, sedangkan Iklim & Isu Global "
                "(1 dari 3 rilis) dan Tambang & Energi (1 rilis, ditolak) paling rendah. Hal ini menunjukkan bahwa tingginya respons "
                "pemerintah terhadap narasi dan advokasi WALHI belum sepenuhnya berbanding lurus dengan tindakan konkret dalam penyelesaian "
                "persoalan lingkungan hidup.")
TINDAKAN = [
    "Tindakan nyata pemerintah yang tercatat setelah rilis WALHI (Agustus–Oktober 2026):",
    "1) 1 September – Pemprov Kalteng dan Pemkot Palangka Raya membuka rumah oksigen gratis bagi korban asap.",
    "2) 3 September – Kemenhut membekukan izin 5 PBPH di Kalimantan Barat (371.560 ha).",
    "3) 13 September – KLH menyegel 50 badan usaha terkait karhutla, berlanjut hingga 68 konsesi per Oktober.",
    "4) 21 September – Kemenhut mencabut izin 5 perusahaan; 4 di antaranya ada di daftar laporan WALHI.",
    "5) 15–20 Oktober – Polda Kalsel menaikkan laporan WALHI Kalsel ke penyidikan; 4 korporasi ditetapkan tersangka.",
    "6) 21 Oktober – Kemenhut membekukan izin 6 PBPH lagi disertai paksaan pemulihan.",
    "7) 9–22 Oktober – DPRD Babel bersama warga nelayan dan WALHI menuntut KKP merevisi zonasi agar Batu Beriga dan perairan "
    "sekitarnya keluar dari zona tambang (penghapusan Pasal 24 huruf d); seluruh fraksi mendukung revisi Perda RZWP3K, paripurna "
    "ditargetkan 20 November. IUP PT Timah belum dicabut.",
    "8) 23 Oktober – Kementerian Hukum menyerahkan data pemilik manfaat korporasi terduga karhutla kepada aparat penegak hukum.",
    "9) 14–29 Oktober – Bareskrim menetapkan 20 korporasi tersangka karhutla (4 PMA) dan mengusulkan pencabutan 23 izin.",
    "Tiga tindakan (nomor 4, 5, dan 7) terkait langsung dengan WALHI. Tindakan lain searah dengan tuntutan WALHI tetapi tidak menyebut WALHI, "
    "dan sebagian menyusul arahan Presiden pada 16 September. Tidak ada tuntutan yang dipenuhi penuh.",
]
p297 = ORIG[297]; r297 = rprs(p297)[0]
NEW[297] += "".join(para("<w:p>", ppr(p297), [run(t, r297)]) for t in TINDAKAN)
NEW[300] = caption(300, 3, "Jumlah berita yang memuat WALHI per isu kampanye, Agustus–Oktober 2026")
# P302: pertahankan komentar Mida pada kalimat Pesisir
p = ORIG[302]; r = rprs(p)[0]
m_start = re.search(r'<w:commentRangeStart w:id="\d+" ?/>', p).group(0)
m_end = re.search(r'<w:commentRangeEnd w:id="\d+" ?/>', p).group(0)
m_ref = re.search(r'<w:r>(?:(?!</w:r>).)*?<w:commentReference w:id="\d+" ?/></w:r>', p, re.S).group(0)
NEW[302] = para(p_open(p), ppr(p), [
    run("Hutan & Kebun menyumbang lebih dari separuh pemberitaan WALHI (661 berita), terutama bersamaan dengan karhutla. Tambang & Energi "
        "(198) dan Urban & Tata Ruang (187) menyusul; sebagian besar pemberitaan tambang berasal dari WALHI daerah. ", r),
    m_start,
    run("Pesisir & Laut tercatat 94 berita dari 64 media: gabungan pemantauan otomatis (72 berita) dan kliping tim PELA (22 berita "
        "tambahan, kebanyakan media alternatif dan daerah yang tidak terindeks Google News). Angka ini sudah mencakup berita tambang, "
        "PSN, dan data center di laut, pesisir, dan pulau kecil.", r),
    m_end, m_ref,
    run(" Berita yang terkait langsung dengan rilis Divisi Kampanye (dicari per rilis, 1 hari sebelum sampai 14 hari sesudah rilis) "
        "tercatat 382 berita yang memuat WALHI: Hutan & Kebun 183, Urban 84, Pesisir & Laut 46, Pangan 41, Iklim 19, dan Tambang & Energi 3.", r),
])
NEW[304] = caption(304, 4, "Respons tertinggi pemerintah atas rilis WALHI per bidang kampanye")
NEW[307] = body(307, "Analisa data pemberitaan ini juga mencakup pemberitaan WALHI secara umum, sehingga beberapa pemberitaan isu daerah juga "
                "termasuk di dalamnya. Untuk beberapa isu dan respon dibantu oleh kampanye WALHI daerah. Misalnya untuk isu tambang dan "
                "energi, secara dominan adalah cover pemberitaan dari WALHI daerah serta respon pemerintah terhadap pemberitaan tersebut. "
                "Untuk isu perkotaan dan tata ruang, seluruh rilis direspons, umumnya oleh kementerian dan pemerintah daerah, tetapi belum "
                "ada tindakan nyata: Menkomdigi mengakui masalah air data center tanpa moratorium, Menko Pangan dan Danantara justru "
                "mempercepat PSEL, dan Wali Kota Solo baru berjanji menghentikan open dumping di TPA Putri Cempo.")
for i, new in NEW.items():
    assert x.count(ORIG[i]) == 1, i
    x = x.replace(ORIG[i], new, 1)

# gambar: ganti file dan sesuaikan tinggi
ext = list(re.finditer(r'<wp:extent cx="(\d+)" cy="(\d+)" ?/>', x))
FILES = ["gambar-1-rilis-per-bidang.png", "gambar-2-rilis-per-bulan.png", "gambar-3-pemberitaan-per-isu.png", "gambar-4-respons-per-bidang.png"]
rels = open(os.path.join(D, "word", "_rels", "document.xml.rels"), encoding="utf8").read()
embeds = re.findall(r'r:embed="(rId\d+)"', x)
for k, (m, f, rid) in enumerate(zip(ext, FILES, embeds)):
    target = re.search(r'Target="(media/[^"]+)" Id="%s"' % rid, rels) or re.search(r'Id="%s"[^>]*Target="(media/[^"]+)"' % rid, rels)
    data = open(os.path.join(FIG, f), "rb").read()
    open(os.path.join(D, "word", target.group(1)), "wb").write(data)
    w, h = struct.unpack(">II", data[16:24]); cx = int(m.group(1)); cy = round(cx * h / w)
    x = x.replace(m.group(0), f'<wp:extent cx="{cx}" cy="{cy}" />', 1)
    # a:ext di dalam pic untuk gambar yang sama
    x = re.sub(r'(<a:ext cx="%d" cy=")\d+(")' % cx, lambda mm: f"{mm.group(1)}{cy}{mm.group(2)}", x, count=1) if False else x
    print(f"gambar {k+1}: {target.group(1)} <- {f} ({cx}x{cy})")
# sesuaikan a:ext (xfrm) yang mengikuti setiap extent
def fix_xfrm(doc):
    out = []; pos = 0
    for m in re.finditer(r"<w:drawing>.*?</w:drawing>", doc, re.S):
        blk = m.group(0)
        e = re.search(r'<wp:extent cx="(\d+)" cy="(\d+)"', blk)
        blk2 = re.sub(r'(<a:ext cx=")\d+(" cy=")\d+(")', lambda mm: f"{mm.group(1)}{e.group(1)}{mm.group(2)}{e.group(2)}{mm.group(3)}", blk)
        out.append(doc[pos:m.start()]); out.append(blk2); pos = m.end()
    out.append(doc[pos:]); return "".join(out)
x = fix_xfrm(x)
# baris sumber di bawah Gambar 3: tambahkan kliping tim PELA
_ps = re.findall(r"<w:p[ >].*?</w:p>", x, re.S)
_t = lambda q: "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", q))
_i = [i for i, q in enumerate(_ps) if _t(q).startswith("Gambar 3.")][0]
_src = _ps[_i + 1]
if _t(_src).startswith("Sumber:") and "PELA" not in _t(_src):
    _m = list(re.finditer(r"(<w:t)[^>]*(>)\.(</w:t>)", _src))[-1]
    _new = _src[:_m.start()] + '<w:t xml:space="preserve">; kliping tim PELA (Pesisir &amp; Laut).</w:t>' + _src[_m.end():]
    x = x.replace(_src, _new, 1)
open(P, "w", encoding="utf8").write(x)
print("paragraf diubah:", sorted(NEW))

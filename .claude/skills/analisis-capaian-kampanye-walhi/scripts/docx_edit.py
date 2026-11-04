"""Edit laporan divisi (.docx) di tempat berdasarkan berkas spesifikasi JSON.

Pakai:
  python3 -I docx_edit.py laporan.docx spesifikasi.json laporan_diperbarui.docx

Paragraf dicari lewat potongan teks yang unik ("cari"), bukan nomor, sehingga bisa dipakai untuk laporan bulan apa pun.
Format paragraf (pPr) dan format run pertama dipertahankan. Komentar yang menempel di paragraf yang diganti
dipertahankan dan dipasang di sekeliling teks baru. Setiap "cari" harus cocok dengan tepat satu paragraf.

Contoh spesifikasi:
{
  "ganti_teks": [{"dari": "37 rilis", "ke": "43 rilis"}],
  "paragraf": [{"cari": "WALHI juga menjadi center pemberitaan", "teks": "Paragraf baru ..."}],
  "caption": [{"cari": "Jumlah rilis per bidang", "nomor": 1, "teks": "Jumlah rilis per bidang, November 2026."}],
  "sisip_setelah": [{"cari": "Temuan ini didasarkan pada", "paragraf": ["Tindakan nyata ...:", "1) ...", "2) ..."]}],
  "gambar": [{"urutan": 1, "file": "figures/gambar-1-rilis-per-bidang.png"}]
}
"gambar.urutan" = urutan gambar di dokumen (1 = gambar pertama). Tinggi gambar disesuaikan dengan rasio gambar baru.
Setelah itu validasi (skill docx: scripts/office/validate.py --original) dan render halaman yang berubah untuk dicek.
Untuk membalas komentar yang ada, pakai skill docx: scripts/comment.py <folder> "teks" --parent <id> --author "...".
"""
import json, os, re, shutil, struct, sys, tempfile, zipfile
from xml.sax.saxutils import escape

PARA = re.compile(r"<w:p[ >].*?</w:p>", re.S)


def teks(p):
    import html
    return html.unescape("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)))


def cari_satu(x, potongan):
    hit = [p for p in PARA.findall(x) if potongan in teks(p)]
    if len(hit) != 1:
        sys.exit(f"'{potongan[:50]}' cocok dengan {len(hit)} paragraf (harus tepat 1). Perpanjang potongan teksnya.")
    return hit[0]


def ppr(p):
    m = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    return m.group(0) if m else ""


def rprs(p):
    return [m.group(1) or "" for m in re.finditer(r"<w:r(?: [^>]*)?>(<w:rPr>.*?</w:rPr>|<w:rPr ?/>)?(?:(?!</w:r>).)*?<w:t", p, re.S)]


def run(t, rpr):
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(t)}</w:t></w:r>'


def komentar(p):
    s = re.findall(r'<w:commentRangeStart w:id="\d+" ?/>', p)
    e = re.findall(r'<w:commentRangeEnd w:id="\d+" ?/>', p)
    r = re.findall(r'<w:r>(?:(?!</w:r>).)*?<w:commentReference w:id="\d+" ?/></w:r>', p, re.S)
    return s, e, r


def paragraf_baru(p, potongan_runs):
    buka = re.match(r"<w:p[^>]*>", p).group(0)
    s, e, r = komentar(p)
    return buka + ppr(p) + "".join(s) + "".join(potongan_runs) + "".join(e) + "".join(r) + "</w:p>"


def main(src, spec_path, out):
    spec = json.load(open(spec_path))
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(src) as z:
        z.extractall(tmp)
    for root, _, files in os.walk(tmp):  # buang symlink dari arsip luar
        for f in files:
            if os.path.islink(os.path.join(root, f)):
                os.remove(os.path.join(root, f))
    P = os.path.join(tmp, "word", "document.xml")
    x = open(P, encoding="utf8").read()
    for g in spec.get("ganti_teks", []):
        n = len(re.findall(r"(<w:t[^>]*>[^<]*?)" + re.escape(g["dari"]), x))
        x = re.sub(r"(<w:t[^>]*>[^<]*?)" + re.escape(g["dari"]), lambda m: m.group(1) + escape(g["ke"]), x)
        print(f"ganti_teks '{g['dari']}' -> '{g['ke']}': {n} tempat")
    for c in spec.get("paragraf", []):
        p = cari_satu(x, c["cari"]); r = rprs(p)
        x = x.replace(p, paragraf_baru(p, [run(c["teks"], r[0] if r else "")]), 1)
    for c in spec.get("caption", []):
        p = cari_satu(x, c["cari"]); r = rprs(p)
        x = x.replace(p, paragraf_baru(p, [run(f"Gambar {c['nomor']}. ", r[0] if r else ""), run(c["teks"], r[1] if len(r) > 1 else "")]), 1)
    for c in spec.get("sisip_setelah", []):
        p = cari_satu(x, c["cari"]); r = rprs(p)
        tambahan = "".join(f"<w:p>{ppr(p)}{run(t, r[0] if r else '')}</w:p>" for t in c["paragraf"])
        x = x.replace(p, p + tambahan, 1)
    if spec.get("gambar"):
        rels = open(os.path.join(tmp, "word", "_rels", "document.xml.rels"), encoding="utf8").read()
        blok = list(re.finditer(r"<w:drawing>.*?</w:drawing>", x, re.S))
        ganti = {}
        for g in spec["gambar"]:
            b = blok[g["urutan"] - 1].group(0)
            rid = re.search(r'r:embed="(rId\d+)"', b).group(1)
            tgt = (re.search(r'Target="(media/[^"]+)"[^>]*Id="%s"' % rid, rels) or re.search(r'Id="%s"[^>]*Target="(media/[^"]+)"' % rid, rels)).group(1)
            data = open(g["file"], "rb").read()
            if not data.startswith(b"\x89PNG"):
                sys.exit(f"{g['file']} harus PNG")
            open(os.path.join(tmp, "word", tgt), "wb").write(data)
            w, h = struct.unpack(">II", data[16:24])
            cx = int(re.search(r'<wp:extent cx="(\d+)"', b).group(1)); cy = round(cx * h / w)
            b2 = re.sub(r'<wp:extent cx="\d+" cy="\d+"', f'<wp:extent cx="{cx}" cy="{cy}"', b)
            b2 = re.sub(r'<a:ext cx="\d+" cy="\d+"', f'<a:ext cx="{cx}" cy="{cy}"', b2)
            ganti[b] = b2
            print(f"gambar {g['urutan']}: {tgt} <- {g['file']}")
        for lama, baru in ganti.items():
            x = x.replace(lama, baru, 1)
    open(P, "w", encoding="utf8").write(x)
    if os.path.exists(out):
        os.remove(out)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, tmp))
    shutil.rmtree(tmp)
    print("tersimpan:", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

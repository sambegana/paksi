"""Ambil tabel rilis dari laporan divisi kampanye (.docx) dan tandai kemungkinan duplikat.

Pakai: python3 -I ekstrak_tabel_rilis.py laporan_divisi.docx tabel_rilis.json

Mencari tabel yang baris pertamanya memuat kolom Bulan, Judul, Bidang (dan Pengkampanye/PJ).
Keluaran: {"baris": [[bulan, judul, bidang, pengkampanye], ...], "per_bidang": {...},
           "per_bidang_bulan": {...}, "kemungkinan_duplikat": [[i, j, alasan]]}
Duplikat ditandai bila judul yang dinormalkan sama, kemiripan >= 0,8, atau judul pendek (>= 25 huruf) terkandung di judul lain. Keputusan tetap di pengguna.
"""
import collections, difflib, html, json, re, sys, zipfile


def tabel_docx(path):
    x = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
    for t in re.findall(r"<w:tbl>.*?</w:tbl>", x, re.S):
        rows = []
        for tr in re.findall(r"<w:tr[ >].*?</w:tr>", t, re.S):
            cells = [re.sub(r"\s+", " ", html.unescape("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", tc)))).strip()
                     for tc in re.findall(r"<w:tc>.*?</w:tc>", tr, re.S)]
            rows.append(cells)
        yield rows


def norm(s):
    s = re.sub(r"[_\-]+", " ", s.lower())
    s = re.sub(r"\b(rilis|siaran pers|sipers|press release|media|walhi|draft)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def main(src, out):
    for rows in tabel_docx(src):
        if not rows:
            continue
        h = [c.lower() for c in rows[0]]
        if {"bulan", "judul", "bidang"} <= set(h):
            ib, ij, ibd = h.index("bulan"), h.index("judul"), h.index("bidang")
            ip = next((h.index(k) for k in ("pengkampanye", "pj", "pengkampanye pj") if k in h), None)
            data = [[r[ib], r[ij], r[ibd], r[ip] if ip is not None and ip < len(r) else ""] for r in rows[1:] if len(r) > max(ib, ij, ibd)]
            dup = []
            for i in range(len(data)):
                for j in range(i + 1, len(data)):
                    a, b = norm(data[i][1]), norm(data[j][1])
                    pendek, panjang = sorted((a, b), key=len)
                    if a and (a == b or difflib.SequenceMatcher(None, a, b).ratio() >= 0.8
                              or (len(pendek) >= 25 and pendek in panjang)):
                        dup.append([i, j, f"judul mirip: '{data[i][1][:60]}' ({data[i][0]}) ~ '{data[j][1][:60]}' ({data[j][0]})"])
            pb = collections.Counter(r[2] for r in data)
            pbb = collections.defaultdict(collections.Counter)
            for r in data:
                pbb[r[2]][r[0].split()[0] if r[0] else "?"] += 1
            res = {"sumber": src, "baris": data, "per_bidang": dict(pb), "per_bidang_bulan": {k: dict(v) for k, v in pbb.items()},
                   "kemungkinan_duplikat": dup}
            json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
            print(f"{len(data)} baris | per bidang: {dict(pb)}")
            for d in dup:
                print("  KEMUNGKINAN DUPLIKAT:", d[2])
            return
    sys.exit("Tabel dengan kolom Bulan/Judul/Bidang tidak ditemukan.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

"""Tahap 4 — susun usulan nama untuk ditinjau manusia. Belum ada perubahan di Drive.

Nomor urut disimpan di nomor.json dan tidak pernah dipakai ulang, sehingga
menjalankan ulang tahap ini (misalnya setelah file baru ditambahkan) tidak
mengubah nomor file yang sudah ada.
"""

import json
import re

from . import config
from .names import (TANGGAL_TIDAK_DIKETAHUI, ekstensi, muat_vocab, slug, susun_nama,
                    tag_bersih, tentukan_tanggal)

KOLOM = [
    "status", "nomor", "nama_lama", "nama_baru", "kategori", "kategori_lain",
    "deskripsi_singkat", "tag", "keterangan", "lokasi", "tanggal", "sumber_tanggal",
    "keyakinan", "ada_anak", "duplikat_dari", "catatan_review", "folder", "jenis",
    "file_id", "link",
]

_NAMA_ASLI = re.compile(r"^nama asli: (.+)$", re.M)


def nama_asli(m):
    """Setelah rename, nama asli tetap diambil dari blok Description yang kita tulis."""
    t = _NAMA_ASLI.search(m.get("deskripsi_lama") or "")
    return t.group(1).strip() if t else m["nama"]


def _muat_nomor():
    return json.loads(config.NOMOR.read_text()) if config.NOMOR.exists() else {}


def _beri_nomor(inventaris, tanggal_per_id, nomor):
    berikut = max(nomor.values(), default=0) + 1
    baru = [m for m in inventaris if m["id"] not in nomor]
    # Urut kronologis; yang tanggalnya tidak diketahui di belakang.
    baru.sort(key=lambda m: (tanggal_per_id[m["id"]] == TANGGAL_TIDAK_DIKETAHUI,
                             tanggal_per_id[m["id"]], m["folder"], m["nama"]))
    for m in baru:
        nomor[m["id"]] = berikut
        berikut += 1
    return nomor


def jalankan(args):
    config.siapkan()
    vocab = muat_vocab()
    inventaris = config.baca_jsonl(config.INVENTARIS)
    if not inventaris:
        raise SystemExit("Inventaris kosong. Jalankan tahap 'audit' dulu.")
    meta_video = {v["id"]: v for v in config.baca_jsonl(config.META_VIDEO)}
    klas = {}
    for k in config.baca_jsonl(config.KLASIFIKASI):
        klas[k["md5"] or k["id"]] = k

    tanggal = {}
    for m in inventaris:
        asli = nama_asli(m)
        tanggal[m["id"]] = tentukan_tanggal(
            exif=m["waktu_exif"],
            meta_video=(meta_video.get(m["id"]) or {}).get("creation_time"),
            nama_file=asli,
        )
    nomor = _beri_nomor(inventaris, {i: t for i, (t, _) in tanggal.items()}, _muat_nomor())
    config.NOMOR.write_text(json.dumps(nomor, indent=0))

    asli_per_md5 = {}
    baris_baris = []
    for m in sorted(inventaris, key=lambda m: nomor[m["id"]]):
        tgl, sumber = tanggal[m["id"]]
        asli = nama_asli(m)
        k = klas.get(m["md5"] or m["id"])
        dup = ""
        if m["md5"]:
            if m["md5"] in asli_per_md5:
                dup = asli_per_md5[m["md5"]]
            else:
                asli_per_md5[m["md5"]] = f"{nomor[m['id']]:05d} ({m['folder']}/{asli})"
        b = {"nomor": nomor[m["id"]], "nama_lama": m["nama"], "tanggal": tgl,
             "sumber_tanggal": sumber, "duplikat_dari": dup, "folder": m["folder"],
             "jenis": m["jenis"], "file_id": m["id"], "link": m["link"]}
        if not k:
            b.update(status="belum", nama_baru="", catatan_review="belum dianalisis")
            baris_baris.append(b)
            continue
        kat = k["kategori_utama"] if k["kategori_utama"] in vocab else "LLN"
        desk = slug(k["deskripsi_singkat"])
        b.update(
            kategori=kat,
            kategori_lain=", ".join(x for x in k["kategori_lain"] if x != kat),
            deskripsi_singkat=desk,
            tag=", ".join(tag_bersih(k["tag"])),
            keterangan=k["keterangan"],
            lokasi=k["lokasi"],
            keyakinan=k["keyakinan"],
            ada_anak="ya" if k["ada_anak"] else "",
            catatan_review=k["catatan_review"],
            nama_baru=susun_nama(tgl, kat, nomor[m["id"]], desk, ekstensi(asli, m["mime"])),
        )
        perlu_review = (k["keyakinan"] != "tinggi" or kat == "LLN" or dup or k["catatan_review"].strip())
        b["status"] = "review" if perlu_review else "ok"
        baris_baris.append(b)

    config.tulis_csv(config.USULAN, KOLOM, baris_baris)
    hitung = {s: sum(1 for b in baris_baris if b["status"] == s) for s in ("ok", "review", "belum")}
    print(f"Usulan ditulis ke {config.USULAN}")
    print(f"  ok={hitung['ok']}  review={hitung['review']}  belum dianalisis={hitung['belum']}")
    print("Tinjau file itu (Google Sheets/Excel). Ubah status menjadi 'ok' untuk yang disetujui,")
    print("'lewati' untuk yang tidak boleh diubah. Edit kolom kategori/deskripsi_singkat/tag/")
    print("keterangan/lokasi/tanggal bila perlu — kolom nama_baru dihitung ulang saat diterapkan.")

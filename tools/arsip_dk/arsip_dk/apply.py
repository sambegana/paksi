"""Tahap 5 — terapkan rename + Description ke Drive, dan pulihkan bila perlu.

Default-nya simulasi (dry-run). Perubahan hanya terjadi dengan --jalankan.
Setiap perubahan dicatat di log/terapkan_<waktu>.csv sebelum lanjut ke file
berikutnya, sehingga bisa dibatalkan dengan perintah 'pulihkan'.
"""

import csv
import time

from . import config, drive
from .names import (ekstensi, gabung_description, muat_vocab, render_blok, stempel_waktu,
                    susun_nama, tag_bersih)
from .propose import nama_asli

JEDA_DETIK = 0.4  # batas tulis Drive kira-kira 3 permintaan/detik per pengguna
KOLOM_LOG = ["file_id", "nama_sebelum", "nama_sesudah", "description_sebelum", "waktu"]


def _path_log_baru():
    """Log pemulihan tidak boleh pernah tertimpa, walau dua proses jalan di detik yang sama."""
    dasar = config.LOG_DIR / f"terapkan_{stempel_waktu()}"
    path, n = dasar.with_suffix(".csv"), 1
    while path.exists():
        n += 1
        path = config.LOG_DIR / f"{dasar.name}_{n}.csv"
    return path


def _rencana(baris_baris, vocab, inventaris):
    per_id = {m["id"]: m for m in inventaris}
    rencana, masalah = [], []
    for b in baris_baris:
        if b.get("status", "").strip().lower() != "ok":
            continue
        m = per_id.get(b["file_id"])
        if not m:
            masalah.append(f"{b['file_id']}: tidak ada di inventaris (jalankan audit ulang)")
            continue
        kat = b["kategori"].strip().upper()
        if kat not in vocab:
            masalah.append(f"{b['nama_lama']}: kategori {kat!r} tidak ada di vocab.json")
            continue
        # Excel membuang nol di depan: "00000000" kembali sebagai "0".
        tgl = b["tanggal"].strip()
        b["tanggal"] = tgl.zfill(8) if tgl.isdigit() and int(tgl) == 0 else tgl
        try:
            asli = nama_asli(m)
            baru = susun_nama(b["tanggal"], kat, b["nomor"], b["deskripsi_singkat"],
                              ekstensi(asli, m["mime"]))
        except ValueError as e:
            masalah.append(f"{b['nama_lama']}: {e}")
            continue
        lain = [k.strip().upper() for k in b["kategori_lain"].split(",") if k.strip().upper() in vocab]
        blok = render_blok(
            kode_arsip=f"DK-{int(b['nomor']):05d}", kategori=kat, nama_kategori=vocab[kat]["nama"],
            kategori_lain=lain, tags=tag_bersih(b["tag"].split(",")), keterangan=b["keterangan"].strip(),
            lokasi=b["lokasi"].strip(), tanggal=b["tanggal"], sumber_tanggal=b["sumber_tanggal"],
            nama_lama=asli, folder_lama=m["folder"],
        )
        rencana.append({"file_id": m["id"], "nama_sekarang": m["nama"], "nama_baru": baru, "blok": blok})

    dobel = {}
    for r in rencana:
        dobel.setdefault(r["nama_baru"], []).append(r["file_id"])
    for nama, ids in dobel.items():
        if len(ids) > 1:
            masalah.append(f"nama {nama} dipakai {len(ids)} file — cek kolom nomor")
    return rencana, masalah


def terapkan(args):
    config.siapkan()
    vocab = muat_vocab()
    if not config.USULAN.exists():
        raise SystemExit("usulan_nama.csv belum ada. Jalankan tahap 'susun' dulu.")
    rencana, masalah = _rencana(config.baca_csv(config.USULAN), vocab, config.baca_jsonl(config.INVENTARIS))
    if masalah:
        print("Masalah yang harus dibereskan dulu:")
        print("\n".join(f"  - {x}" for x in masalah))
        raise SystemExit(1)

    config.tulis_csv(config.RENCANA, ["file_id", "nama_sekarang", "nama_baru", "blok"], rencana)
    print(f"{len(rencana)} file berstatus ok. Rencana lengkap: {config.RENCANA}")
    for r in rencana[:15]:
        print(f"  {r['nama_sekarang']}  ->  {r['nama_baru']}")
    if not args.jalankan:
        print("\nINI SIMULASI. Tidak ada yang diubah. Tambahkan --jalankan untuk menerapkan.")
        return
    if not args.ya and input(f"\nUbah {len(rencana)} file di Drive? Ketik YA: ").strip() != "YA":
        print("Dibatalkan.")
        return

    svc = drive.layanan(drive.kredensial(tulis=True))
    path_log = _path_log_baru()
    diubah = dilewati = 0
    with open(path_log, "x", encoding="utf-8-sig", newline="") as f:
        log = csv.DictWriter(f, fieldnames=KOLOM_LOG)
        log.writeheader()
        for i, r in enumerate(rencana, 1):
            kini = svc.files().get(fileId=r["file_id"], fields="name,description",
                                   supportsAllDrives=True).execute(num_retries=5)
            desk_baru = gabung_description(kini.get("description"), r["blok"])
            if kini["name"] not in (r["nama_sekarang"], r["nama_baru"]):
                print(f"  LEWATI {kini['name']}: nama berubah sejak audit")
                dilewati += 1
                continue
            if kini["name"] == r["nama_baru"] and kini.get("description") == desk_baru:
                dilewati += 1
                continue
            svc.files().update(fileId=r["file_id"], supportsAllDrives=True,
                               body={"name": r["nama_baru"], "description": desk_baru},
                               fields="id").execute(num_retries=5)
            log.writerow({"file_id": r["file_id"], "nama_sebelum": kini["name"],
                          "nama_sesudah": r["nama_baru"],
                          "description_sebelum": kini.get("description", ""),
                          "waktu": stempel_waktu()})
            f.flush()
            diubah += 1
            if i % 50 == 0:
                print(f"  {i}/{len(rencana)}")
            time.sleep(JEDA_DETIK)
    print(f"Selesai: {diubah} diubah, {dilewati} dilewati. Log pemulihan: {path_log}")


def pulihkan(args):
    baris_baris = config.baca_csv(args.log)
    print(f"{len(baris_baris)} perubahan di {args.log}.")
    if not args.ya and input("Kembalikan nama & Description semuanya? Ketik YA: ").strip() != "YA":
        print("Dibatalkan.")
        return
    svc = drive.layanan(drive.kredensial(tulis=True))
    pulih = lewat = 0
    for b in reversed(baris_baris):
        kini = svc.files().get(fileId=b["file_id"], fields="name", supportsAllDrives=True).execute(num_retries=5)
        if kini["name"] != b["nama_sesudah"]:
            print(f"  LEWATI {kini['name']}: sudah diubah lagi setelah diterapkan")
            lewat += 1
            continue
        svc.files().update(fileId=b["file_id"], supportsAllDrives=True, fields="id",
                           body={"name": b["nama_sebelum"], "description": b["description_sebelum"]},
                           ).execute(num_retries=5)
        pulih += 1
        time.sleep(JEDA_DETIK)
    print(f"Dipulihkan: {pulih}, dilewati: {lewat}.")

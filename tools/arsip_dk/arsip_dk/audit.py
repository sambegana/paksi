"""Tahap 1 — audit (hanya membaca). Tidak ada file di Drive yang diubah."""

from collections import Counter, defaultdict

from . import config, drive
from .names import tentukan_tanggal


def _media(item):
    return item["mimeType"].startswith(("image/", "video/"))


def _ukuran(n):
    n = float(n or 0)
    for satuan in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {satuan}"
        n /= 1024
    return f"{n:.1f} PB"


def _rapikan(item, folder_by_id, drive_id):
    img = item.get("imageMediaMetadata") or {}
    vid = item.get("videoMediaMetadata") or {}
    loc = img.get("location") or {}
    tanggal, sumber = tentukan_tanggal(exif=img.get("time"), nama_file=item["name"])
    return {
        "id": item["id"],
        "nama": item["name"],
        "folder": drive.path_folder(item, folder_by_id, drive_id),
        "mime": item["mimeType"],
        "jenis": "video" if item["mimeType"].startswith("video/") else "foto",
        "ukuran": int(item.get("size") or 0),
        "md5": item.get("md5Checksum", ""),
        "waktu_exif": img.get("time", ""),
        "tanggal": tanggal,
        "sumber_tanggal": sumber,
        "durasi_ms": int(vid.get("durationMillis") or 0),
        "lebar": img.get("width") or vid.get("width") or "",
        "tinggi": img.get("height") or vid.get("height") or "",
        "gps_lat": loc.get("latitude", ""),
        "gps_lon": loc.get("longitude", ""),
        "kamera": " ".join(filter(None, [img.get("cameraMake"), img.get("cameraModel")])),
        "deskripsi_lama": item.get("description", ""),
        "ada_thumbnail": bool(item.get("hasThumbnail")),
        "dibuat_di_drive": item.get("createdTime", ""),
        "link": item.get("webViewLink", ""),
    }


def jalankan(args):
    config.siapkan()
    cred = drive.kredensial(tulis=False)
    svc = drive.layanan(cred)
    drive_id = args.drive_id or drive.cari_shared_drive(svc, args.drive)
    print(f"Membaca isi Shared Drive {args.drive_id or args.drive!r} ({drive_id}) ...")

    semua = drive.daftar_semua(svc, drive_id)
    folder_by_id = {f["id"]: f for f in semua if f["mimeType"] == drive.MIME_FOLDER}
    media = [_rapikan(f, folder_by_id, drive_id) for f in semua if _media(f)]
    lain = [f for f in semua if f["mimeType"] != drive.MIME_FOLDER and not _media(f)]
    media.sort(key=lambda m: (m["folder"], m["nama"]))

    config.tulis_jsonl(config.INVENTARIS, media)
    config.tulis_csv(config.INVENTARIS_CSV, list(media[0].keys()) if media else ["id"], media)

    # Duplikat persis (isi byte identik) — sering muncul dari proses salin/pindah.
    per_md5 = defaultdict(list)
    for m in media:
        if m["md5"]:
            per_md5[m["md5"]].append(m)
    grup_duplikat = [g for g in per_md5.values() if len(g) > 1]
    file_berlebih = sum(len(g) - 1 for g in grup_duplikat)
    byte_berlebih = sum(g[0]["ukuran"] * (len(g) - 1) for g in grup_duplikat)

    jenis = Counter(m["jenis"] for m in media)
    ext = Counter((m["nama"].rsplit(".", 1)[-1].lower() if "." in m["nama"] else "(tanpa)") for m in media)
    sumber_tgl = Counter(m["sumber_tanggal"] for m in media)
    per_folder = Counter(m["folder"] or "(akar drive)" for m in media)
    ber_gps = sum(1 for m in media if m["gps_lat"] != "")

    L = [f"# Laporan audit — {args.drive_id or args.drive}", ""]
    L += [f"- Total item (tanpa folder): {len(semua) - len(folder_by_id)}",
          f"- Folder: {len(folder_by_id)}",
          f"- Foto: {jenis['foto']}  ·  Video: {jenis['video']}  ·  Bukan media: {len(lain)}",
          f"- Total ukuran media: {_ukuran(sum(m['ukuran'] for m in media))}",
          f"- Duplikat persis: {len(grup_duplikat)} grup, {file_berlebih} salinan berlebih "
          f"({_ukuran(byte_berlebih)})",
          f"- Punya koordinat GPS: {ber_gps}", ""]
    L += ["## Sumber tanggal", ""] + [f"- {k}: {v}" for k, v in sumber_tgl.most_common()] + [""]
    L += ["## Ekstensi", ""] + [f"- {k}: {v}" for k, v in ext.most_common()] + [""]
    L += ["## Folder terbanyak (30 teratas)", ""] + [f"- {k}: {v}" for k, v in per_folder.most_common(30)] + [""]
    if lain:
        L += ["## Contoh file bukan media (tidak diproses)", ""]
        L += [f"- {f['name']} ({f['mimeType']})" for f in lain[:30]] + [""]
    if grup_duplikat:
        L += ["## Contoh duplikat (20 grup pertama)", ""]
        for g in grup_duplikat[:20]:
            L.append("- " + "  |  ".join(f"{m['folder']}/{m['nama']}" for m in g))
        L.append("")

    if args.bandingkan:
        L += _bandingkan(svc, args.bandingkan, per_md5)

    config.LAPORAN_AUDIT.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L))
    print(f"\nInventaris: {config.INVENTARIS_CSV}\nLaporan: {config.LAPORAN_AUDIT}")


def _bandingkan(svc, nama_sumber, md5_tujuan):
    """Cek apakah semua media di drive sumber sudah ada (isi identik) di drive tujuan."""
    sumber_id = drive.cari_shared_drive(svc, nama_sumber)
    semua = drive.daftar_semua(svc, sumber_id)
    folder_by_id = {f["id"]: f for f in semua if f["mimeType"] == drive.MIME_FOLDER}
    media = [f for f in semua if _media(f)]
    tertinggal = [f for f in media if f.get("md5Checksum") and f["md5Checksum"] not in md5_tujuan]
    tanpa_md5 = [f for f in media if not f.get("md5Checksum")]
    L = [f"## Perbandingan dengan {nama_sumber!r}", "",
         f"- Media di sumber: {len(media)}",
         f"- Sudah ada di tujuan (isi identik): {len(media) - len(tertinggal) - len(tanpa_md5)}",
         f"- **Belum ada di tujuan: {len(tertinggal)}**",
         f"- Tidak bisa dicek (tanpa checksum): {len(tanpa_md5)}", ""]
    for f in tertinggal[:50]:
        L.append(f"- {drive.path_folder(f, folder_by_id, sumber_id)}/{f['name']}")
    if len(tertinggal) > 50:
        L.append(f"- ... dan {len(tertinggal) - 50} lainnya")
    return L + [""]

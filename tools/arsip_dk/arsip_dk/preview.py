"""Tahap 2 — pratinjau (hanya membaca).

Foto: thumbnail Drive resolusi tinggi; kalau tidak ada, unduh file asli lalu diperkecil.
Video: 6 cuplikan bingkai diambil lewat HTTP range request (tanpa mengunduh seluruh
video), disusun jadi satu lembar kontak 3x2. Satu pratinjau per isi file unik (md5),
jadi duplikat tidak dianalisis dua kali.
"""

import io
import json
import shutil
import subprocess
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from PIL import Image, ImageDraw

from . import config, drive

POSISI_BINGKAI = (0.05, 0.2, 0.4, 0.6, 0.8, 0.95)
BATAS_UNDUH_FOTO = 80 * 1024 * 1024

_lokal = threading.local()
_kunci_tulis = threading.Lock()


def wakil_per_isi(inventaris):
    """Satu file mewakili setiap isi unik; file tanpa md5 mewakili dirinya sendiri."""
    terlihat, wakil = set(), []
    for m in inventaris:
        kunci = m["md5"] or m["id"]
        if kunci not in terlihat:
            terlihat.add(kunci)
            wakil.append(m)
    return wakil


def path_pratinjau(file_id):
    return config.PRATINJAU_DIR / f"{file_id}.jpg"


def _perkecil(img, sisi):
    img = img.convert("RGB")
    img.thumbnail((sisi, sisi))
    return img


def _sesi(cred):
    if not hasattr(_lokal, "sesi"):
        _lokal.sesi = drive.sesi_http(cred)
        _lokal.svc = drive.layanan(cred)
    return _lokal.sesi, _lokal.svc


def _foto(m, cred, sisi):
    sesi, svc = _sesi(cred)
    link = drive.link_thumbnail(svc, m["id"], sisi) if m["ada_thumbnail"] else None
    if link:
        r = sesi.get(link, timeout=60)
        if r.ok and r.headers.get("content-type", "").startswith("image/"):
            return _perkecil(Image.open(io.BytesIO(r.content)), sisi), "thumbnail"
    if m["ukuran"] > BATAS_UNDUH_FOTO:
        raise RuntimeError("tidak ada thumbnail dan file terlalu besar untuk diunduh")
    r = sesi.get(drive.url_media(m["id"]), timeout=300)
    r.raise_for_status()
    return _perkecil(Image.open(io.BytesIO(r.content)), sisi), "file_asli"


def _ffprobe(url, header):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-headers", header,
         "-show_entries", "format=duration:format_tags=creation_time", "-of", "json", url],
        capture_output=True, text=True, timeout=180,
    )
    fmt = json.loads(out.stdout or "{}").get("format", {})
    return float(fmt.get("duration") or 0), (fmt.get("tags") or {}).get("creation_time", "")


def _bingkai(url, header, detik, tujuan, sisi):
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-rw_timeout", "60000000", "-headers", header,
         "-ss", f"{detik:.2f}", "-i", url, "-frames:v", "1",
         "-vf", f"scale='min({sisi},iw)':-2", "-q:v", "3", str(tujuan)],
        capture_output=True, timeout=300, check=True,
    )


def _lembar_kontak(gambar, sisi, label):
    kolom, baris = 3, 2
    sel = sisi // kolom
    # Sel mengikuti rasio video (video HP umumnya tegak) agar bingkai tidak mengecil.
    tinggi_sel = int(sel * gambar[0].height / gambar[0].width)
    hasil = Image.new("RGB", (sel * kolom, tinggi_sel * baris + 24), "black")
    for i, img in enumerate(gambar[: kolom * baris]):
        img = img.convert("RGB")
        img.thumbnail((sel, tinggi_sel))
        x = (i % kolom) * sel + (sel - img.width) // 2
        y = (i // kolom) * tinggi_sel + (tinggi_sel - img.height) // 2
        hasil.paste(img, (x, y))
    ImageDraw.Draw(hasil).text((6, hasil.height - 20), label, fill="white")
    hasil.thumbnail((sisi, sisi))
    return hasil


def _video(m, cred, sisi):
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg tidak terpasang")
    header = f"Authorization: Bearer {drive.token_segar(cred)}\r\n"
    url = drive.url_media(m["id"])
    durasi, waktu_buat = _ffprobe(url, header)
    durasi = durasi or m["durasi_ms"] / 1000
    gambar = []
    with tempfile.TemporaryDirectory() as tmp:
        titik = [p * durasi for p in POSISI_BINGKAI] if durasi > 2 else [0]
        for i, detik in enumerate(titik):
            out = Path(tmp) / f"{i}.jpg"
            try:
                _bingkai(url, header, detik, out, sisi)
                gambar.append(Image.open(out).copy())
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                continue
    if not gambar:
        sesi, svc = _sesi(cred)
        link = drive.link_thumbnail(svc, m["id"], sisi)
        if not link:
            raise RuntimeError("gagal mengambil bingkai video dan tidak ada thumbnail")
        r = sesi.get(link, timeout=60)
        r.raise_for_status()
        return _perkecil(Image.open(io.BytesIO(r.content)), sisi), "thumbnail", waktu_buat, durasi
    label = f"{len(gambar)} cuplikan dari video {durasi:.0f} detik"
    return _lembar_kontak(gambar, sisi, label), "bingkai_video", waktu_buat, durasi


def _proses(m, cred, sisi):
    if m["jenis"] == "video":
        img, cara, waktu_buat, durasi = _video(m, cred, sisi)
        meta = {"id": m["id"], "creation_time": waktu_buat, "durasi_detik": durasi}
    else:
        img, cara = _foto(m, cred, sisi)
        meta = None
    img.save(path_pratinjau(m["id"]), "JPEG", quality=85)
    return cara, meta


def jalankan(args):
    config.siapkan()
    inventaris = config.baca_jsonl(config.INVENTARIS)
    if not inventaris:
        raise SystemExit("Inventaris kosong. Jalankan tahap 'audit' dulu.")
    target = [m for m in wakil_per_isi(inventaris) if not path_pratinjau(m["id"]).exists()]
    if args.batas:
        target = target[: args.batas]
    print(f"{len(target)} pratinjau akan dibuat ({args.paralel} paralel).")

    cred = drive.kredensial(tulis=False)
    ok, gagal = 0, []
    with ThreadPoolExecutor(max_workers=args.paralel) as ex:
        tugas = {ex.submit(_proses, m, cred, args.ukuran): m for m in target}
        for i, t in enumerate(as_completed(tugas), 1):
            m = tugas[t]
            try:
                cara, meta = t.result()
                ok += 1
                if meta:
                    with _kunci_tulis, open(config.META_VIDEO, "a", encoding="utf-8") as f:
                        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
            except Exception as e:  # satu file gagal tidak boleh menghentikan ribuan lainnya
                gagal.append((m, str(e)))
            if i % 25 == 0 or i == len(target):
                print(f"  {i}/{len(target)}  berhasil={ok} gagal={len(gagal)}")

    if gagal:
        path = config.LOG_DIR / "pratinjau_gagal.csv"
        config.tulis_csv(path, ["id", "folder", "nama", "galat"],
                         [{"id": m["id"], "folder": m["folder"], "nama": m["nama"], "galat": e}
                          for m, e in gagal])
        print(f"Daftar yang gagal: {path} (jalankan ulang tahap ini untuk mencoba lagi)")

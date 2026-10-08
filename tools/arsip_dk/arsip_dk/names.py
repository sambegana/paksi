"""Fungsi murni untuk tanggal, nama file baru, dan blok Description Drive.

Tidak ada akses jaringan di sini supaya mudah diuji.
"""

import json
import os
import re
import unicodedata
from datetime import date, datetime
from pathlib import Path

PREFIX = "DK"
TANGGAL_TIDAK_DIKETAHUI = "00000000"
MAKS_KATA_DESKRIPSI = 5

BLOK_AWAL = "[arsip-dk]"
BLOK_AKHIR = "[/arsip-dk]"

_VOCAB_PATH = Path(__file__).with_name("vocab.json")

# 2024:03:15 10:22:11 (EXIF) atau 2024-03-15T10:22:11Z (ISO / ffprobe)
_ISO_ATAU_EXIF = re.compile(r"^(\d{4})[:\-](\d{2})[:\-](\d{2})")
# IMG_20240315_..., VID-20240315-WA0001, PXL_20240315..., 2024-03-15 ...
_TANGGAL_DI_NAMA = re.compile(
    r"(?<!\d)((?:19|20)\d{2})[-_.]?(0[1-9]|1[0-2])[-_.]?(0[1-9]|[12]\d|3[01])(?!\d)"
)

_EKSTENSI_DARI_MIME = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/heic": ".heic",
    "image/heif": ".heif",
    "image/webp": ".webp",
    "video/mp4": ".mp4",
    "video/quicktime": ".mov",
    "video/x-msvideo": ".avi",
    "video/3gpp": ".3gp",
}


def muat_vocab():
    with open(_VOCAB_PATH, encoding="utf-8") as f:
        return json.load(f)


def _tanggal_valid(y, m, d):
    try:
        t = date(int(y), int(m), int(d))
    except ValueError:
        return None
    # Kamera yang jamnya belum diatur sering menulis 1970/1980/2000-01-01.
    if t.year < 1995 or t > date.today():
        return None
    if (t.month, t.day) == (1, 1) and t.year in (1970, 1980, 2000):
        return None
    return t.strftime("%Y%m%d")


def tanggal_dari_metadata(teks):
    """EXIF ('2024:03:15 10:22:11') atau ISO ('2024-03-15T...') -> 'YYYYMMDD'."""
    if not teks:
        return None
    m = _ISO_ATAU_EXIF.match(teks.strip())
    return _tanggal_valid(*m.groups()) if m else None


def tanggal_dari_nama(nama):
    """Ambil tanggal dari pola nama file kamera/WhatsApp. Hanya perkiraan."""
    if not nama:
        return None
    for m in _TANGGAL_DI_NAMA.finditer(nama):
        t = _tanggal_valid(*m.groups())
        if t:
            return t
    return None


def tentukan_tanggal(exif=None, meta_video=None, nama_file=None):
    """Kembalikan (YYYYMMDD, sumber). Tanggal upload/modifikasi sengaja tidak dipakai:
    itu tanggal file dipindahkan, bukan tanggal pengambilan, dan akan menyesatkan."""
    for nilai, sumber in (
        (tanggal_dari_metadata(exif), "exif"),
        (tanggal_dari_metadata(meta_video), "metadata_video"),
        (tanggal_dari_nama(nama_file), "nama_file"),
    ):
        if nilai:
            return nilai, sumber
    return TANGGAL_TIDAK_DIKETAHUI, "tidak_diketahui"


def slug(teks, maks_kata=MAKS_KATA_DESKRIPSI):
    """'Akar Tunjang di Tepi Sungai!' -> 'akar-tunjang-di-tepi-sungai'."""
    ascii_ = unicodedata.normalize("NFKD", teks or "").encode("ascii", "ignore").decode()
    kata = re.findall(r"[a-z0-9]+", ascii_.lower())
    return "-".join(kata[:maks_kata])


def ekstensi(nama_lama, mime=None):
    ext = os.path.splitext(nama_lama or "")[1].lower()
    if ext and len(ext) <= 6 and ext[1:].isalnum():
        return ext
    return _EKSTENSI_DARI_MIME.get(mime or "", "")


def susun_nama(tanggal, kategori, nomor, deskripsi, ext):
    """DK_<YYYYMMDD>_<KAT>_<NNNNN>_<deskripsi>.<ext>"""
    if not re.fullmatch(r"\d{8}", tanggal or ""):
        raise ValueError(f"tanggal harus 8 digit YYYYMMDD, dapat {tanggal!r}")
    if not re.fullmatch(r"[A-Z]{3}", kategori or ""):
        raise ValueError(f"kode kategori harus 3 huruf kapital, dapat {kategori!r}")
    nomor = int(nomor)
    if not 0 < nomor < 100000:
        raise ValueError(f"nomor di luar rentang 1-99999: {nomor}")
    bagian = [PREFIX, tanggal, kategori, f"{nomor:05d}"]
    s = slug(deskripsi)
    if s:
        bagian.append(s)
    return "_".join(bagian) + ext


def tag_bersih(tags):
    """Normalisasi, buang duplikat, pertahankan urutan."""
    hasil = []
    for t in tags or []:
        s = slug(t, maks_kata=4)
        if s and s not in hasil:
            hasil.append(s)
    return hasil


def render_blok(kode_arsip, kategori, nama_kategori, kategori_lain, tags, keterangan,
                lokasi, tanggal, sumber_tanggal, nama_lama, folder_lama):
    baris = [
        BLOK_AWAL,
        f"kode: {kode_arsip}",
        f"kategori: {kategori} ({nama_kategori})",
    ]
    if kategori_lain:
        baris.append("kategori lain: " + ", ".join(kategori_lain))
    if tags:
        baris.append("tag: " + ", ".join(tags))
    if keterangan:
        baris.append(f"keterangan: {keterangan}")
    if lokasi:
        baris.append(f"lokasi: {lokasi}")
    baris.append(f"tanggal: {tanggal} (sumber: {sumber_tanggal})")
    baris.append(f"nama asli: {nama_lama}")
    if folder_lama:
        baris.append(f"folder asal: {folder_lama}")
    baris.append(BLOK_AKHIR)
    return "\n".join(baris)


def gabung_description(lama, blok):
    """Ganti blok [arsip-dk] lama bila ada; kalau tidak, tambahkan di akhir.
    Teks Description lain yang ditulis manusia tidak disentuh."""
    lama = lama or ""
    pola = re.compile(re.escape(BLOK_AWAL) + r".*?" + re.escape(BLOK_AKHIR), re.S)
    if pola.search(lama):
        return pola.sub(lambda _: blok, lama, count=1)
    return f"{lama.rstrip()}\n\n{blok}" if lama.strip() else blok


def stempel_waktu():
    return datetime.now().strftime("%Y%m%d-%H%M%S")

"""Lokasi file kerja. Semua hasil disimpan di satu folder data (default ./data_arsip)."""

import csv
import json
import os
from pathlib import Path

DATA = Path(os.environ.get("DK_DATA_DIR", "data_arsip"))

INVENTARIS = DATA / "inventaris.jsonl"
INVENTARIS_CSV = DATA / "inventaris.csv"
LAPORAN_AUDIT = DATA / "laporan_audit.md"
PRATINJAU_DIR = DATA / "pratinjau"
META_VIDEO = DATA / "meta_video.jsonl"
KLASIFIKASI = DATA / "klasifikasi.jsonl"
NOMOR = DATA / "nomor.json"
USULAN = DATA / "usulan_nama.csv"
RENCANA = DATA / "rencana_terapkan.csv"
LOG_DIR = DATA / "log"


def siapkan():
    for d in (DATA, PRATINJAU_DIR, LOG_DIR):
        d.mkdir(parents=True, exist_ok=True)


def baca_jsonl(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(baris) for baris in f if baris.strip()]


def tulis_jsonl(path, baris_baris):
    with open(path, "w", encoding="utf-8") as f:
        for b in baris_baris:
            f.write(json.dumps(b, ensure_ascii=False) + "\n")


def tulis_csv(path, kolom, baris_baris):
    # utf-8-sig agar Excel membaca huruf non-ASCII dengan benar.
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=kolom, extrasaction="ignore")
        w.writeheader()
        w.writerows(baris_baris)


def baca_csv(path):
    """Terima CSV dari Google Sheets (koma) maupun Excel lokal Indonesia (titik koma)."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        contoh = f.read(8192)
        f.seek(0)
        try:
            dialek = csv.Sniffer().sniff(contoh, delimiters=",;\t")
        except csv.Error:
            dialek = csv.excel
        return list(csv.DictReader(f, dialect=dialek))

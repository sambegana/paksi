#!/usr/bin/env python3
"""Gabungkan file ekstraksi agen (format references/brief-ekstraksi.md) ke catatan entitas vault.

Pemakaian:
  python3 vault/_alat/gabung.py <dir-ekstrak> [--tulis]

Tanpa --tulis hanya mencetak ringkasan (dry-run). Dengan --tulis:
  - membuat/menambah catatan di vault/{konsep,regulasi,aktor,tempat}/<slug>.md
    (catatan yang sudah ada TIDAK ditimpa: bagian sumber baru ditambahkan di bawah penanda)
  - menulis <dir-ekstrak>/_kumpulan.md berisi angka, argumen, keterkaitan lintas isu, dan
    pertanyaan terbuka dari semua agen — bahan untuk hub isu & benang-merah (disunting manusia).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
JENIS = {"konsep": "konsep", "regulasi": "regulasi", "aktor": "aktor", "tempat": "tempat"}
FIELD = re.compile(r"^\s*-\s*([a-z][a-z\-/ ]*?)\s*:\s*(.*)$")
PENANDA = "<!-- gabung.py: sumber tambahan di bawah -->"
HARI_INI = date.today().isoformat()

ISU = {"data-center": "isu-data-center", "sampah": "isu-sampah", "tata-ruang": "isu-tata-ruang",
       "air": "isu-air", "sungai": "isu-sungai", "hutan-kota": "isu-hutan-kota",
       "iklim": "isu-iklim-kota", "iklim-kota": "isu-iklim-kota",
       "advokasi": "isu-advokasi-kebijakan", "advokasi-kebijakan": "isu-advokasi-kebijakan"}

# Slug ganda -> slug kanonik. Diterapkan pada judul entitas DAN pada setiap [[tautan]].
ALIAS = {
    "additionality-ebt": "additionality",
    "moratorium-berambang": "moratorium-bersyarat",
    "lock-in-pasokan": "lock-in-psel",
    "penurunan-muka-tanah-antropogenik": "penurunan-muka-tanah",
    "pulau-panas-perkotaan": "panas-kota",
    "akumulasi-lewat-perampasan": "perampasan-ruang",
    "saset-multilapis": "ekonomi-saset",
    "instrumen-asing-pembanding-semua-diverifikasi-di-sesi-lewat-sumber-hukum-berita-yang-dikutip":
        "instrumen-asing-data-center",
    "jakstranas-perpres-97-2017": "jakstranas-sampah",
    "perpres-jakstranas": "jakstranas-sampah",
    "pp-27-2020": "pp-27-2020-sampah-spesifik",
    "pp-28-2025": "pp-28-2025-perizinan-berbasis-risiko",
    "se-menlh-2-2026": "se-menlh-2-2026-plastik-sekali-pakai",
    "second-ndc-indonesia": "sndc-indonesia",
    "uu-keterbukaan-informasi-publik": "uu-kip",
    "uu-23-2014-pemda": "uu-pemerintahan-daerah",
    "uu-24-2007-penanggulangan-bencana": "uu-penanggulangan-bencana",
    "pergub-zona-bebas-air-tanah": "pergub-dki-zona-bebas-air-tanah",
    "regulasi-lain-disebut-s-adv-semua-belum-diverifikasi": "regulasi-lain-belum-diverifikasi",
    "tempat-lain-disebut-s-adv": "tempat-lain-belum-diverifikasi",
    "bdx": "bdx-indonesia",
    "operator-dc-lain": "operator-lain-data-center",
    "bekasi-karawang": "bekasi-cikarang-karawang",
    "kit-batang": "batang-kitb",
    "johor": "singapura-johor",
    "isu-iklim": "isu-iklim-kota",
    "isu-advokasi": "isu-advokasi-kebijakan",
}
_LINK = re.compile(r"\[\[([^\]|#]+)([^\]]*)\]\]")


def ganti_alias(teks: str) -> str:
    return _LINK.sub(lambda m: f"[[{ALIAS.get(m.group(1).strip(), m.group(1).strip())}{m.group(2)}]]", teks)


def slugify(s: str) -> str:
    s = s.strip().strip("`[]").lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def norm_isu(raw: str) -> list[str]:
    items = re.split(r"[,\s;·—]+", raw.replace("[", " ").replace("]", " "))
    out = []
    for it in items:
        it = slugify(it).removeprefix("isu-")
        if it in ISU and ISU[it] not in out:
            out.append(ISU[it])
    return out


def parse(path: Path):
    """-> (entitas: list[(jenis, slug, fields)], bebas: dict[section -> text])"""
    entitas, bebas = [], defaultdict(str)
    section = sub = None
    fields: dict[str, str] = {}
    last_key = None

    def flush():
        if section in JENIS and sub:
            entitas.append((JENIS[section], sub, dict(fields)))

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            flush()
            section = slugify(line[3:]).split("-")[0] if slugify(line[3:]).split("-")[0] in JENIS \
                else slugify(line[3:])
            sub, fields, last_key = None, {}, None
            continue
        if section in JENIS:
            if line.startswith("### "):
                flush()
                sub = slugify(line[4:].split("—")[0].split(" - ")[0])
                sub, fields, last_key = ALIAS.get(sub, sub), {}, None
                continue
            if sub is None:
                continue
            m = FIELD.match(line)
            if m:
                last_key = m.group(1).strip().replace(" ", "-")
                val = m.group(2).strip()
                if last_key == "isu" and "sumber-sesi" in val:  # isu & sumber-sesi satu baris
                    val, _, rest = val.partition("sumber-sesi")
                    fields["sumber-sesi"] = rest.lstrip(" :")
                fields[last_key] = val
            elif last_key and line.strip():
                fields[last_key] += "\n" + line.rstrip()
        elif section:
            bebas[section] += line + "\n"
    flush()
    return entitas, bebas


def sesi_links(v: str) -> list[str]:
    found = re.findall(r"\[\[([^\]|#]+)", v)
    if found:
        return [f.strip() for f in found]
    return re.findall(r"\d{4}-\d{2}-\d{2}-[a-z0-9\-]+", v)


BIDANG = {
    "konsep": [("definisi", None), ("dasar", "Dasar"), ("dipakai-untuk", "Dipakai untuk")],
    "regulasi": [("pokok", "Pokok"), ("masalah/celah", "Masalah / celah"), ("status", "Status")],
    "aktor": [("jenis", "Jenis"), ("peran", "Peran"), ("kepentingan/posisi", "Kepentingan / posisi")],
    "tempat": [("apa-yang-terjadi", "Kasus"), ("kasus", "Kasus")],
}


def blok_sumber(jenis: str, f: dict[str, str]) -> str:
    sesi = ", ".join(f"[[{s}]]" for s in sesi_links(f.get("sumber-sesi", "")))
    isu = ", ".join(f"[[{i}]]" for i in norm_isu(f.get("isu", "")))
    lines = [f"### Dari {sesi or 'sumber tak disebut'}", f"Isu: {isu or '—'}", ""]
    dipakai = set()
    for key, label in BIDANG[jenis]:
        val = f.get(key)
        if val and key not in dipakai:
            dipakai.add(key)
            lines.append(f"**{label or key.capitalize()}.** {val}" if label else val)
            lines.append("")
    for key, val in f.items():  # bidang lain yang tidak dikenal tetap disimpan
        if key in {"judul", "isu", "sumber-sesi"} | dipakai or not val:
            continue
        lines.append(f"**{key}.** {val}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def tulis_entitas(jenis: str, slug: str, sumber: list[dict[str, str]], tulis: bool) -> str:
    path = VAULT / jenis / f"{slug}.md"
    judul = max((s.get("judul", "") for s in sumber), key=len) or slug.replace("-", " ").title()
    isu = sorted({i for s in sumber for i in norm_isu(s.get("isu", ""))})
    blok = "\n".join(blok_sumber(jenis, s) for s in sumber)
    if path.exists():
        teks = path.read_text(encoding="utf-8")
        if PENANDA not in teks:
            teks = teks.rstrip() + f"\n\n## Sumber\n{PENANDA}\n"
        teks = teks.rstrip() + "\n\n" + blok
        status = "tambah"
    else:
        teks = (f"---\njenis: {jenis}\ndiperbarui: {HARI_INI}\nisu: [{', '.join(isu)}]\n"
                f"tag: []\n---\n\n# {judul}\n\n"
                f"Terkait: {', '.join(f'[[{i}]]' for i in isu) or '—'}\n\n"
                f"## Sumber\n{PENANDA}\n\n{blok}")
        status = "baru"
    if tulis:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(ganti_alias(teks), encoding="utf-8")
    return status


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1])
    tulis = "--tulis" in sys.argv
    kumpul: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    bebas_semua: dict[str, list[str]] = defaultdict(list)
    for f in sorted(src.glob("*.md")):
        if f.name.startswith("_"):
            continue
        ent, bebas = parse(f)
        for jenis, slug, fields in ent:
            kumpul[(jenis, slug)].append(fields)
        for sec, txt in bebas.items():
            if txt.strip():
                bebas_semua[sec].append(f"<!-- {f.stem} -->\n{txt.strip()}\n")
        print(f"{f.name}: {len(ent)} entitas, bagian bebas: {', '.join(k for k in bebas if bebas[k].strip())}")

    hitung = defaultdict(lambda: defaultdict(int))
    for (jenis, slug), sumber in sorted(kumpul.items()):
        st = tulis_entitas(jenis, slug, sumber, tulis)
        hitung[jenis][st] += 1
        if len(sumber) > 1:
            print(f"  SAMBUNG {jenis}/{slug}: {len(sumber)} sumber")
    for jenis, d in hitung.items():
        print(f"{jenis}: {dict(d)}")
    if tulis:
        out = src / "_kumpulan.md"
        out.write_text(ganti_alias("\n".join(f"# {sec}\n\n" + "\n".join(v)
                                             for sec, v in bebas_semua.items())), encoding="utf-8")
        print(f"bahan bebas -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

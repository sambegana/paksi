#!/usr/bin/env python3
"""Periksa kesehatan vault: tautan rusak, catatan yatim, frontmatter hilang.

Pemakaian:  python3 vault/_alat/periksa.py
Keluar dengan kode 1 jika ada tautan rusak (catatan yatim hanya peringatan).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
LEWATI = {"_templat", "_alat", ".obsidian"}
# [[nama]], [[nama|alias]], [[nama#judul]] — abaikan isi blok kode.
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
BLOK_KODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
# Catatan yang memang titik masuk, tidak perlu ditaut balik.
AKAR = {"00-indeks", "README"}


def catatan() -> dict[str, Path]:
    hasil: dict[str, Path] = {}
    for p in VAULT.rglob("*.md"):
        if LEWATI & set(p.relative_to(VAULT).parts):
            continue
        if p.stem in hasil:
            print(f"GANDA   nama sama: {p.relative_to(VAULT)} dan {hasil[p.stem].relative_to(VAULT)}")
        hasil[p.stem] = p
    return hasil


def main() -> int:
    semua = catatan()
    ditaut: set[str] = set()
    rusak = tanpa_frontmatter = 0

    for nama, path in sorted(semua.items()):
        teks = path.read_text(encoding="utf-8")
        if not teks.startswith("---\n"):
            tanpa_frontmatter += 1
            print(f"FRONT   {path.relative_to(VAULT)}: tidak ada frontmatter YAML")
        for target in WIKILINK.findall(BLOK_KODE.sub("", teks)):
            target = target.strip()
            if target in semua:
                if target != nama:
                    ditaut.add(target)
            else:
                rusak += 1
                print(f"RUSAK   {path.relative_to(VAULT)} -> [[{target}]]")

    yatim = sorted(set(semua) - ditaut - AKAR)
    for nama in yatim:
        print(f"YATIM   {semua[nama].relative_to(VAULT)}: tidak ditaut catatan mana pun")

    print(f"\n{len(semua)} catatan · {rusak} tautan rusak · {len(yatim)} yatim · "
          f"{tanpa_frontmatter} tanpa frontmatter")
    return 1 if rusak else 0


if __name__ == "__main__":
    sys.exit(main())

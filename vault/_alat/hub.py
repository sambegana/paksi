#!/usr/bin/env python3
"""Bangun bagian otomatis hub isu (vault/isu/isu-*.md) dan kartu angka (vault/angka-kunci.md).

Pemakaian:
  python3 vault/_alat/hub.py [--angka-dari <dir-ekstrak>]

--angka-dari: tambahkan baris tabel `## angka` dari file ekstraksi agen ke vault/angka-kunci.md
              (baris yang persis sama tidak digandakan).
Lalu untuk tiap isu: daftar konsep/regulasi/aktor/tempat bertag isu itu (urut jumlah sumber),
baris angka bertag isu itu, dan log sesinya ditulis di antara penanda AUTO di hub. Teks di luar
penanda (ringkasan, sambungan lintas isu, argumen) ditulis manusia dan tidak disentuh.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gabung import ISU, ganti_alias, norm_isu  # noqa: E402

VAULT = Path(__file__).resolve().parent.parent
ANGKA = VAULT / "angka-kunci.md"
MULAI, SELESAI = "<!-- AUTO:mulai — dibuat hub.py, jangan disunting -->", "<!-- AUTO:selesai -->"
JUDUL = {
    "isu-data-center": "Data center", "isu-sampah": "Sampah", "isu-tata-ruang": "Tata ruang",
    "isu-air": "Air", "isu-sungai": "Sungai & DAS urban", "isu-hutan-kota": "Hutan kota & RTH",
    "isu-iklim-kota": "Iklim kota", "isu-advokasi-kebijakan": "Advokasi kebijakan",
}
KOLOM = "| Angka | Konteks | Sumber | Status | Isu | Sesi |"


def frontmatter(teks: str) -> dict[str, str]:
    if not teks.startswith("---\n"):
        return {}
    blok = teks[4:].split("\n---", 1)[0]
    return dict(l.split(":", 1) for l in blok.splitlines() if ":" in l and not l.startswith(" "))


def baris_angka_dari(src: Path) -> list[str]:
    out = []
    for f in sorted(src.glob("*.md")):
        if f.name.startswith("_"):
            continue
        dalam, sesi_lalu = False, ""
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                dalam = line[3:].strip().lower().startswith("angka")
                continue
            if not dalam or not line.startswith("|") or set(line) <= set("|-: "):
                continue
            sel = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(sel) < 6 or sel[0].lower() == "angka":
                continue
            sel = sel[:5] + [" ".join(sel[5:])]
            if sel[5].lower() in {"idem", "sda", "\"", "〃"}:
                sel[5] = sesi_lalu
            else:
                if not sel[5].startswith("[["):
                    sel[5] = " ".join(f"[[{s}]]" for s in re.findall(r"\d{4}-\d{2}-\d{2}-[a-z0-9\-]+", sel[5])) or sel[5]
                sesi_lalu = sel[5]
            sel[4] = ", ".join(i.removeprefix("isu-") for i in norm_isu(sel[4])) or sel[4]
            out.append("| " + " | ".join(sel) + " |")
    return out


def muat_angka() -> list[str]:
    if not ANGKA.exists():
        return []
    return [l for l in ANGKA.read_text(encoding="utf-8").splitlines()
            if l.startswith("| ") and not l.startswith(KOLOM[:8]) and not set(l) <= set("|-: ")]


def simpan_angka(baris: list[str]) -> None:
    ANGKA.write_text(
        f"---\njenis: data\ndiperbarui: {date.today().isoformat()}\n---\n\n# Angka kunci\n\n"
        "Semua angka dari sesi, dengan sumber dan status. **Cek status sebelum dikutip**: "
        "`belum-diverifikasi` dan `dikoreksi` jangan dipakai di rilis tanpa membuka sumber primer.\n"
        "Hub tiap isu menampilkan potongan tabel ini.\n\n"
        f"{KOLOM}\n|---|---|---|---|---|---|\n" + "\n".join(baris) + "\n", encoding="utf-8")


def entitas_per_isu() -> dict[str, dict[str, list[tuple[int, str, str]]]]:
    hasil: dict[str, dict[str, list]] = {i: {} for i in JUDUL}
    for jenis in ("konsep", "regulasi", "aktor", "tempat"):
        for p in (VAULT / jenis).glob("*.md"):
            teks = p.read_text(encoding="utf-8")
            fm = frontmatter(teks)
            n = max(1, teks.count("### Dari "))
            m = re.search(r"^# (.+)$", teks, re.M)
            judul = m.group(1).strip() if m else p.stem
            for isu in norm_isu(fm.get("isu", "")):
                hasil[isu].setdefault(jenis, []).append((n, p.stem, judul))
    return hasil


def sesi_per_isu() -> dict[str, list[str]]:
    hasil: dict[str, list[str]] = {i: [] for i in JUDUL}
    for p in sorted((VAULT / "sesi").glob("*.md"), reverse=True):
        for isu in norm_isu(frontmatter(p.read_text(encoding="utf-8")).get("isu", "")):
            hasil[isu].append(p.stem)
    return hasil


def blok_auto(isu: str, ent, sesi, angka) -> str:
    lines = [MULAI, ""]
    label = {"konsep": "Konsep", "regulasi": "Regulasi", "aktor": "Aktor", "tempat": "Tempat & kasus"}
    for jenis in ("konsep", "regulasi", "aktor", "tempat"):
        daftar = sorted(ent.get(jenis, []), key=lambda x: (-x[0], x[1]))
        if not daftar:
            continue
        lines.append(f"## {label[jenis]} ({len(daftar)})")
        lines.append(" · ".join(f"[[{s}|{j[:60]}]]" + (f" **×{n}**" if n > 1 else "") for n, s, j in daftar))
        lines.append("")
    kunci = isu.removeprefix("isu-")
    if kunci == "iklim-kota":
        kunci = "iklim"
    rows = [r for r in angka if re.search(rf"\|\s*[^|]*\b{re.escape(kunci)}\b[^|]*\|[^|]*\|\s*$", r)]
    if rows:
        lines += [f"## Angka kunci ({len(rows)}) — lengkapnya di [[angka-kunci]]", "", KOLOM,
                  "|---|---|---|---|---|---|", *rows, ""]
    if sesi.get(isu):
        lines += ["## Sumber sesi", *[f"- [[{s}]]" for s in sesi[isu]], ""]
    lines.append(SELESAI)
    return "\n".join(lines)


def main() -> int:
    angka = muat_angka()
    if "--angka-dari" in sys.argv:
        src = Path(sys.argv[sys.argv.index("--angka-dari") + 1])
        ada = set(angka)
        baru = [ganti_alias(b) for b in baris_angka_dari(src)]
        angka += [b for b in baru if b not in ada]
        simpan_angka(angka)
        print(f"angka-kunci: {len(angka)} baris")
    ent, sesi = entitas_per_isu(), sesi_per_isu()
    for isu, judul in JUDUL.items():
        p = VAULT / "isu" / f"{isu}.md"
        auto = blok_auto(isu, ent[isu], sesi, angka)
        if p.exists():
            teks = p.read_text(encoding="utf-8")
            if MULAI in teks:
                teks = teks.split(MULAI)[0] + auto + teks.split(SELESAI, 1)[1]
            else:
                teks = teks.rstrip() + "\n\n" + auto + "\n"
        else:
            teks = (f"---\njenis: isu\ndiperbarui: {date.today().isoformat()}\ntag: []\n---\n\n"
                    f"# {judul}\n\n_Ringkasan isu belum ditulis._\n\n{auto}\n")
        p.parent.mkdir(exist_ok=True)
        p.write_text(teks, encoding="utf-8")
        print(f"{isu}: " + ", ".join(f"{k} {len(v)}" for k, v in ent[isu].items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Buat gambar laporan analisis WALHI & karhutla 2026.

Membaca:
  headline_mentions_weekly.csv  (hasil collect_gnews.py)
  coding_respons.csv            (matriks pengodean respons, bisa diedit)
Menulis:
  figures/gambar-N-*.png (300 dpi) dan .svg
  figures/ringkasan.json        (angka yang dipakai di laporan)

Jalankan:  python3 make_figures.py
"""
import csv
import json
import os
from collections import Counter, defaultdict, OrderedDict

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": ["Carlito", "DejaVu Sans"],
    "font.size": 10,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 11,
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "legend.frameon": False,
    "svg.fonttype": "path",
})
INK = "#1a1a1a"
ACCENT = "#1f4e79"   # WALHI / seri utama
GREY = "#9e9e9e"
LIGHT = "#d0d0d0"
W = 6.3  # inci, lebar isi halaman A4 dengan margin 2,5 cm


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------- data ----------
weekly = list(csv.DictReader(open(os.path.join(HERE, "headline_mentions_weekly.csv"))))
coding = list(csv.DictReader(open(os.path.join(HERE, "coding_respons.csv"))))

tot = Counter()
series = defaultdict(OrderedDict)
for r in weekly:
    n = int(r["judul_menyebut_tanpa_kanal_sendiri"])
    tot[r["aktor"]] += n
    series[r["aktor"]][r["minggu_mulai"]] = n

LABEL = {"BRGM/Akademisi IPB": "Akademisi IPB", "Madani": "Madani Berkelanjutan"}
STATE = ["BNPB", "Kemenhut", "KLH"]
NONSTATE = ["WALHI", "Greenpeace", "BRGM/Akademisi IPB", "Pantau Gambut", "Madani", "Auriga"]
nonstate_total = sum(tot[a] for a in NONSTATE)
all_total = sum(tot.values())

BULAN = ["", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


def tgl(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {BULAN[int(m)]}"


# ---------- Gambar 1: alur metodologi ----------
fig, ax = plt.subplots(figsize=(W, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")


def box(x, y, w, h, text, dashed=False, bold=False):
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                       linewidth=0.9, edgecolor=INK, facecolor="white",
                       linestyle="--" if dashed else "-")
    ax.add_patch(p)
    ax.text(x, y, text, ha="center", va="center", fontsize=8.8, color=INK,
            fontweight="bold" if bold else "normal", wrap=True)


def arrow(x1, y1, x2, y2, dashed=False):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9, linestyle="--" if dashed else "-",
                                shrinkA=0, shrinkB=0))


box(5, 9.3, 6.4, 0.8, "1. Definisi isu dan kata kunci\n(aktor + \"karhutla\")")
box(5, 7.9, 6.4, 0.9, "2. Pengumpulan korpus: Google News RSS per minggu\n1 Jun – 2 Nov 2026, 9 aktor")
box(5, 6.45, 6.4, 0.9, "3. Pembersihan: hapus judul ganda dan\nberita dari kanal milik aktor sendiri")
box(2.5, 4.8, 4.2, 1.0, "4a. ISU 1 — hitung judul yang\nmenyebut tiap aktor", bold=True)
box(7.5, 4.8, 4.2, 1.0, "4b. ISU 2 — inventaris narasi/\ntuntutan WALHI (n = 14)", bold=True)
box(2.5, 3.2, 4.2, 1.0, "5a. Pangsa pemberitaan\n(share of voice) dan tren mingguan")
box(7.5, 3.2, 4.2, 1.0, "5b. Kode respons pemerintah\nskala 0–4 → tingkat respons")
box(5, 1.6, 6.4, 0.9, "6. Uji reliabilitas antar-pengode\n(α Krippendorff ≥ 0,80) — belum dilakukan", dashed=True)
box(5, 0.35, 3.0, 0.6, "7. Laporan")
arrow(5, 8.9, 5, 8.35)
arrow(5, 7.45, 5, 6.9)
arrow(4.0, 6.0, 2.8, 5.3)
arrow(6.0, 6.0, 7.2, 5.3)
arrow(2.5, 4.3, 2.5, 3.7)
arrow(7.5, 4.3, 7.5, 3.7)
arrow(2.8, 2.7, 4.0, 2.05)
arrow(7.2, 2.7, 6.0, 2.05)
arrow(5, 1.15, 5, 0.65, dashed=True)
save(fig, "gambar-1-alur-metodologi")

# ---------- Gambar 2: tren mingguan ----------
weeks = list(series["WALHI"].keys())
fig, ax = plt.subplots(figsize=(W, 3.3))
styles = [("WALHI", ACCENT, "-", 2.0, "o"), ("Greenpeace", "#7f7f7f", "--", 1.3, "s"),
          ("KLH", INK, ":", 1.4, "^"), ("Pantau Gambut", "#b0b0b0", "-", 1.1, None)]
x = range(len(weeks))
for a, c, ls, lw, mk in styles:
    ax.plot(x, [series[a][w] for w in weeks], color=c, linestyle=ls, linewidth=lw, marker=mk,
            markersize=3, label=a)
ax.set_xticks(list(x))
ax.set_xticklabels([tgl(w) for w in weeks], rotation=60, ha="right", fontsize=8)
ax.set_ylabel("Jumlah judul per minggu")
ax.set_xlabel("Minggu mulai (2026)")
ax.grid(axis="y", color="#e5e5e5", linewidth=0.6)
ax.set_axisbelow(True)
ax.legend(ncol=2, loc="upper left", fontsize=8.5)
i17 = weeks.index("2026-08-17")
ax.annotate("Debat WALHI–Menteri LH\n(KNLH, 21 Agu)", xy=(i17, series["WALHI"]["2026-08-17"]),
            xytext=(i17 - 6.5, 45), fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
i19 = weeks.index("2026-10-19")
ax.annotate("Kabut asap lintas\nbatas (Greenpeace)", xy=(i19, series["Greenpeace"]["2026-10-19"]),
            xytext=(i19 - 7.5, 72), fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
save(fig, "gambar-2-tren-mingguan")

# ---------- Gambar 3: jumlah judul per aktor ----------
order = sorted(tot, key=lambda a: tot[a])
fig, ax = plt.subplots(figsize=(W, 3.2))
cols = [ACCENT if a == "WALHI" else (GREY if a in STATE else LIGHT) for a in order]
bars = ax.barh([LABEL.get(a, a) for a in order], [tot[a] for a in order], color=cols, edgecolor=INK, linewidth=0.4)
for b, a in zip(bars, order):
    ax.text(b.get_width() + 8, b.get_y() + b.get_height() / 2, str(tot[a]), va="center", fontsize=8.5)
ax.set_xlabel("Jumlah judul berita yang menyebut aktor (1 Jun – 2 Nov 2026)")
ax.set_xlim(0, max(tot.values()) * 1.12)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(facecolor=GREY, edgecolor=INK, lw=0.4, label="Lembaga pemerintah"),
                   Patch(facecolor=LIGHT, edgecolor=INK, lw=0.4, label="Non-pemerintah"),
                   Patch(facecolor=ACCENT, label="WALHI")], loc="lower right", fontsize=8.5)
save(fig, "gambar-3-judul-per-aktor")

# ---------- Gambar 4: pangsa non-pemerintah ----------
ns = sorted(NONSTATE, key=lambda a: tot[a])
fig, ax = plt.subplots(figsize=(W, 2.6))
pct = [100 * tot[a] / nonstate_total for a in ns]
bars = ax.barh([LABEL.get(a, a) for a in ns], pct, color=[ACCENT if a == "WALHI" else LIGHT for a in ns],
               edgecolor=INK, linewidth=0.4)
for b, p, a in zip(bars, pct, ns):
    ax.text(b.get_width() + 0.8, b.get_y() + b.get_height() / 2, f"{p:.1f}".replace(".", ",") + f"% ({tot[a]})", va="center", fontsize=8.5)
ax.set_xlim(0, 70)
ax.set_xlabel(f"Pangsa judul di antara aktor non-pemerintah (%, n = {nonstate_total} judul)")
save(fig, "gambar-4-pangsa-nonpemerintah")

# ---------- Isu 2 ----------
skor = [int(r["skor"]) for r in coding]
n14 = len(coding)
grp = defaultdict(int)
for r in coding:
    grp[r["unit12_kelompok"]] = max(grp[r["unit12_kelompok"]], int(r["skor"]))
g = list(grp.values())
n12 = len(g)


def rates(vals):
    n = len(vals)
    return (100 * sum(v >= 1 for v in vals) / n, 100 * sum(v >= 3 for v in vals) / n, 100 * sum(vals) / (4 * n))


r14, r12 = rates(skor), rates(g)
SK = {0: "0 Tidak ada respons", 1: "1 Ditolak", 2: "2 Diakui retoris", 3: "3 Tindakan parsial", 4: "4 Diadopsi penuh"}
SC = {0: "#ffffff", 1: "#d0d0d0", 2: "#9e9e9e", 3: ACCENT, 4: "#0b2740"}

# Gambar 5: skor per narasi
fig, ax = plt.subplots(figsize=(W, 4.3))
rows = list(reversed(coding))
labels = [f"{r['no']}. {r['label_pendek']}" for r in rows]
vals = [int(r["skor"]) for r in rows]
ax.barh(labels, [max(v, 0.04) for v in vals], color=[SC[v] for v in vals], edgecolor=INK, linewidth=0.5)
for i, v in enumerate(vals):
    ax.text(max(v, 0.04) + 0.06, i, str(v), va="center", fontsize=8.5)
ax.set_xlim(0, 4.3)
ax.set_xticks(range(5))
ax.set_xticklabels([SK[k].replace(" ", "\n", 1) for k in range(5)], fontsize=8)
ax.grid(axis="x", color="#e5e5e5", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(axis="y", labelsize=8.5)
save(fig, "gambar-5-skor-per-narasi")

# Gambar 6: distribusi skor
dist = Counter(skor)
fig, ax = plt.subplots(figsize=(W, 2.6))
ks = list(range(5))
bars = ax.bar([SK[k].replace(" ", "\n", 1) for k in ks], [dist[k] for k in ks], color=[SC[k] for k in ks],
              edgecolor=INK, linewidth=0.6)
for b, k in zip(bars, ks):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.12, f"{dist[k]} ({100 * dist[k] / n14:.0f}%)",
            ha="center", fontsize=8.5)
ax.set_ylabel(f"Jumlah tuntutan (n = {n14})")
ax.set_ylim(0, max(dist.values()) + 1.5)
ax.tick_params(axis="x", labelsize=8.5)
save(fig, "gambar-6-distribusi-skor")

# Gambar 7: tingkat respons, dua unit hitung
fig, ax = plt.subplots(figsize=(W, 2.9))
cats = ["Ada respons\n(skor ≥ 1)", "Tindakan nyata\n(skor ≥ 3)", "Indeks tertimbang\n(Σ skor ÷ 4n)"]
import numpy as np
xx = np.arange(3)
b1 = ax.bar(xx - 0.19, r14, 0.38, color=ACCENT, edgecolor=INK, linewidth=0.5, label=f"Unit {n14} tuntutan")
b2 = ax.bar(xx + 0.19, r12, 0.38, color=LIGHT, edgecolor=INK, linewidth=0.5, label=f"Unit {n12} narasi")
for bs in (b1, b2):
    for b in bs:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1, f"{b.get_height():.0f}%", ha="center", fontsize=8.5)
ax.set_xticks(xx)
ax.set_xticklabels(cats, fontsize=8.5)
ax.set_ylabel("Persen")
ax.set_ylim(0, 70)
ax.legend(loc="upper right", fontsize=8.5)
save(fig, "gambar-7-tingkat-respons")

summary = {
    "tot": dict(tot), "nonstate_total": nonstate_total, "all_total": all_total,
    "walhi_share_nonstate": 100 * tot["WALHI"] / nonstate_total,
    "walhi_share_nonstate_no_academia": 100 * tot["WALHI"] / (nonstate_total - tot["BRGM/Akademisi IPB"]),
    "walhi_share_all": 100 * tot["WALHI"] / all_total,
    "rates14": r14, "rates12": r12, "dist": {k: dist[k] for k in ks}, "n14": n14, "n12": n12,
    "weekly": {a: dict(series[a]) for a in ["WALHI", "Greenpeace", "KLH", "Pantau Gambut"]},
}
json.dump(summary, open(os.path.join(OUT, "ringkasan.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in summary.items() if k != "weekly"}, indent=1, ensure_ascii=False))

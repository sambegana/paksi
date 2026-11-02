"""Gambar laporan Capaian WALHI per isu kampanye (1 Jun – 2 Nov 2026).

Membaca korpus_walhi_raw.json (lewat classify.py) dan narasi_respons.csv.
Menulis figures/*.png (300 dpi), figures/*.svg, figures/ringkasan.json.
Jalankan: python3 make_figures.py
"""
import csv, json, os, sys, email.utils
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import classify  # noqa: E402

OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({
    "font.family": ["Carlito", "DejaVu Sans"], "font.size": 10,
    "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#333333",
    "legend.frameon": False, "svg.fonttype": "path",
})
INK, ACCENT, MID, LIGHT = "#1a1a1a", "#1f4e79", "#9e9e9e", "#d0d0d0"
W = 6.3
ISU = list(classify.ISU.keys())
SK = {0: "Tidak ada\nrespons", 1: "Ditolak", 2: "Diakui\nretoris", 3: "Tindakan\nparsial", 4: "Diadopsi\npenuh"}
SC = {0: "#ffffff", 1: LIGHT, 2: MID, 3: ACCENT, 4: "#0b2740"}


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def pct_id(x):
    return f"{x:.0f}%"


# ---- data ----
items, own = classify.load(os.path.join(HERE, "korpus_walhi_raw.json"))
judul = Counter(); media = defaultdict(set); bulan = defaultdict(Counter); lain = 0
for i in items:
    tg = classify.tag(i["title"])
    if not tg:
        lain += 1
    m = email.utils.parsedate_to_datetime(i["date"]).strftime("%Y-%m")
    for k in tg:
        judul[k] += 1; media[k].add(i["src"]); bulan[k][m] += 1

rows = list(csv.DictReader(open(os.path.join(HERE, "narasi_respons.csv"))))
by = defaultdict(list)
for r in rows:
    by[r["isu"]].append(r)


def rates(rs):
    s = [int(r["skor"]) for r in rs]
    n = len(s)
    return {"n": n, "respons": 100 * sum(v >= 1 for v in s) / n, "tindakan": 100 * sum(v >= 3 for v in s) / n,
            "indeks": 100 * sum(s) / (4 * n), "dist": {k: s.count(k) for k in range(5)}}


R = {k: rates(by[k]) for k in ISU}
allr = rates(rows)

# ---- Gambar 1: jumlah judul WALHI per isu ----
order = sorted(ISU, key=lambda k: judul[k])
fig, ax = plt.subplots(figsize=(W, 2.7))
bars = ax.barh(order, [judul[k] for k in order], color=ACCENT, edgecolor=INK, linewidth=0.4)
for b, k in zip(bars, order):
    ax.text(b.get_width() + 6, b.get_y() + b.get_height() / 2, f"{judul[k]} judul · {len(media[k])} media", va="center", fontsize=8.5)
ax.set_xlim(0, max(judul.values()) * 1.35)
ax.set_xlabel(f"Jumlah judul berita yang memuat WALHI (n = {len(items)} judul; satu judul bisa masuk >1 isu)")
save(fig, "gambar-1-berita-per-isu")

# ---- Gambar 2: tingkat respons per isu ----
order2 = ISU
fig, ax = plt.subplots(figsize=(W, 3.0))
x = np.arange(len(order2))
b1 = ax.bar(x - 0.19, [R[k]["respons"] for k in order2], 0.38, color=LIGHT, edgecolor=INK, linewidth=0.5, label="Ada respons (skor ≥ 1)")
b2 = ax.bar(x + 0.19, [R[k]["tindakan"] for k in order2], 0.38, color=ACCENT, edgecolor=INK, linewidth=0.5, label="Tindakan nyata (skor ≥ 3)")
for bs in (b1, b2):
    for b in bs:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, pct_id(b.get_height()), ha="center", fontsize=8)
ax.axhline(allr["respons"], color=INK, lw=0.7, ls="--")
ax.text(len(order2) - 0.5, allr["respons"] + 1.5, f"rata-rata respons {pct_id(allr['respons'])}", ha="right", fontsize=7.5)
ax.set_xticks(x)
ax.set_xticklabels([k.replace(" & ", " &\n") for k in order2], fontsize=8.3)
ax.set_ylabel("Persen narasi")
ax.set_ylim(0, 105)
ax.legend(loc="upper left", fontsize=8.3, ncol=2)
save(fig, "gambar-2-respons-per-isu")

# ---- Gambar 3–8: per isu ----
slug = {k: classify.re.sub("[^a-z]+", "-", k.lower()).strip("-") for k in ISU}
for n, k in enumerate(ISU, start=3):
    rs = list(reversed(by[k]))
    fig, ax = plt.subplots(figsize=(W, 0.42 * len(rs) + 0.9))
    vals = [int(r["skor"]) for r in rs]
    ax.barh([r["label_pendek"] for r in rs], [max(v, 0.04) for v in vals], color=[SC[v] for v in vals], edgecolor=INK, linewidth=0.5)
    for i, v in enumerate(vals):
        ax.text(max(v, 0.04) + 0.07, i, str(v), va="center", fontsize=8.5)
    ax.set_xlim(0, 4.3)
    ax.set_xticks(range(5))
    ax.set_xticklabels([SK[s] for s in range(5)], fontsize=7.8)
    ax.grid(axis="x", color="#e5e5e5", lw=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", labelsize=8.5)
    ax.set_title(f"{k}: respons {pct_id(R[k]['respons'])} · tindakan nyata {pct_id(R[k]['tindakan'])} (n = {R[k]['n']} narasi)",
                 fontsize=9.5, loc="left")
    save(fig, f"gambar-{n}-{slug[k]}")

json.dump({"judul": judul, "media": {k: len(v) for k, v in media.items()}, "total_judul": len(items), "kanal_sendiri": own,
           "lainnya": lain, "R": R, "all": allr, "bulan": {k: dict(v) for k, v in bulan.items()}, "slug": slug},
          open(os.path.join(OUT, "ringkasan.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps({"judul": judul, "R": {k: (v["n"], round(v["respons"]), round(v["tindakan"])) for k, v in R.items()},
                  "all": (allr["n"], round(allr["respons"]), round(allr["tindakan"]), round(allr["indeks"]))}, ensure_ascii=False))

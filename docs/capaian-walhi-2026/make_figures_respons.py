"""Gambar laporan respons pemerintah atas rilis WALHI Agu–Okt 2026. Jalankan setelah final_respons.py."""
import csv, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures_respons"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": ["Carlito", "DejaVu Sans"], "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "legend.frameon": False, "svg.fonttype": "path"})
INK, ACCENT = "#1a1a1a", "#1f4e79"
S = json.load(open(os.path.join(HERE, "ringkasan_per_isu.json")))
ISU = ["Hutan & Kebun", "Pesisir & Laut", "Urban", "Pangan & Ekosistem Esensial", "Iklim & Isu Global", "Tambang & Energi"]
W = 6.3


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# Gambar 1: tangga respons per isu (jumlah rilis)
lv = [("tidak ada respons", lambda s: s["rilis"] - s["ada_respons"], "#ffffff"), ("ditolak", lambda s: s["ditolak"], "#d0d0d0"),
      ("dijanjikan/diakui", lambda s: s["dijanjikan"], "#9e9e9e"), ("tindakan generik", lambda s: s["tindakan_generik"], "#9db7d1"),
      ("tindakan nyata", lambda s: s["tindakan_nyata"], ACCENT)]
fig, ax = plt.subplots(figsize=(W, 3.0))
y = np.arange(len(ISU))[::-1]; left = np.zeros(len(ISU))
for lab, f, c in lv:
    v = np.array([f(S[k]) for k in ISU])
    ax.barh(y, v, left=left, color=c, edgecolor=INK, linewidth=0.5, label=lab)
    for yi, l, vi in zip(y, left, v):
        if vi:
            ax.text(l + vi / 2, yi, str(vi), ha="center", va="center", fontsize=8, color="white" if c == ACCENT else INK)
    left += v
ax.set_yticks(y); ax.set_yticklabels([f"{k} (n={S[k]['rilis']})" for k in ISU], fontsize=8.5)
ax.set_xlabel("Jumlah rilis menurut respons tertinggi pemerintah (1 Agu – 2 Nov 2026)")
ax.legend(ncol=3, fontsize=7.8, loc="lower left", bbox_to_anchor=(0, 1.0))
save(fig, "gambar-1-tangga-respons-per-isu")

# Gambar 2: % ada respons vs % tindakan nyata
fig, ax = plt.subplots(figsize=(W, 2.8))
x = np.arange(len(ISU))
a = [S[k]["pct_ada_respons"] for k in ISU]; t = [S[k]["pct_tindakan_nyata"] for k in ISU]
b1 = ax.bar(x - 0.19, a, 0.38, color="#d0d0d0", edgecolor=INK, linewidth=0.5, label="Ada respons (skor ≥ 1)")
b2 = ax.bar(x + 0.19, t, 0.38, color=ACCENT, edgecolor=INK, linewidth=0.5, label="Tindakan nyata (skor ≥ 3, sesuai tuntutan)")
for bs in (b1, b2):
    for bb in bs:
        ax.text(bb.get_x() + bb.get_width() / 2, bb.get_height() + 1.5, f"{bb.get_height():.0f}%", ha="center", fontsize=8)
tot = S["_total"]
ax.axhline(tot["pct_ada_respons"], color=INK, ls="--", lw=0.7)
ax.text(len(ISU) - 0.5, tot["pct_ada_respons"] + 2, f"rata-rata respons {tot['pct_ada_respons']}%", ha="right", fontsize=7.5)
ax.set_xticks(x); ax.set_xticklabels([k.replace(" & ", " &\n") for k in ISU], fontsize=8.2)
ax.set_ylim(0, 112); ax.set_ylabel("Persen rilis")
ax.legend(fontsize=8, ncol=2, loc="lower left", bbox_to_anchor=(0, 1.0))
save(fig, "gambar-2-respons-vs-tindakan")
print("ok")

"""Buat 4 gambar laporan capaian kampanye.

Pakai: python3 -I buat_gambar.py --tabel tabel_rilis.json --pemberitaan pemberitaan.json \
           --ringkasan ringkasan_per_bidang.json --out figures/ [--judul-periode "Agustus–Oktober 2026"]

Gambar 1–2 dari tabel rilis laporan divisi (ekstrak_tabel_rilis.py), Gambar 3 dari hitung_pemberitaan.py,
Gambar 4 dari gabung_respons.py. Nama bidang mengikuti laporan divisi.
"""
import collections, json, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--tabel", required=True); ap.add_argument("--pemberitaan", required=True); ap.add_argument("--ringkasan", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--judul-periode", default="")
A = ap.parse_args()
OUT = A.out; os.makedirs(OUT, exist_ok=True)
PER = A.judul_periode
plt.rcParams.update({"font.family": ["Carlito", "DejaVu Sans"], "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "legend.frameon": False, "svg.fonttype": "path"})
INK, ACCENT, MID, LIGHT = "#1a1a1a", "#1f4e79", "#9e9e9e", "#d0d0d0"
W = 6.3
T = json.load(open(A.tabel)); tabel = T["baris"] if isinstance(T, dict) else T
PB = json.load(open(A.pemberitaan))
S = json.load(open(A.ringkasan))


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=250, bbox_inches="tight", facecolor="white")
    plt.close(fig)


ORDER0 = ["Hutan & Kebun", "Pesisir & Laut", "Urban", "Pangan & Ekosistem Esensial", "Iklim & Isu Global", "Lintas bidang (lembaga)", "Tambang & Energi"]
PJ = {"Hutan & Kebun": "Umi", "Pesisir & Laut": "Mida", "Urban": "Wahyu", "Pangan & Ekosistem Esensial": "Ifa", "Iklim & Isu Global": "Patria", "Tambang & Energi": "Faisal"}
SHORT = {"Pangan & Ekosistem Esensial": "Pangan & Ekosistem", "Lintas bidang (lembaga)": "Lintas bidang"}
cnt = collections.Counter(r[2] for r in tabel)
ORDER = [k for k in ORDER0 if cnt[k]] + [k for k in cnt if k not in ORDER0]
bln = collections.defaultdict(collections.Counter)
for r in tabel:
    bln[r[2]][r[0].split()[0]] += 1

# Gambar 1: rilis per bidang
order = sorted(ORDER, key=lambda k: cnt[k])
fig, ax = plt.subplots(figsize=(W, 2.9))
lab = [f"{SHORT.get(k, k)} ({PJ[k]})" if k in PJ else SHORT.get(k, k) for k in order]
bars = ax.barh(lab, [cnt[k] for k in order], color=[ACCENT if k == "Hutan & Kebun" else LIGHT for k in order], edgecolor=INK, linewidth=0.4)
for b, k in zip(bars, order):
    ax.text(b.get_width() + 0.15, b.get_y() + b.get_height() / 2, str(cnt[k]), va="center", fontsize=9)
ax.set_xlabel(f"Jumlah rilis{(", " + PER) if PER else ""} (n = {len(tabel)} baris di daftar rilis divisi)")
ax.set_xlim(0, max(cnt.values()) * 1.12)
ax.grid(axis="x", color="#e5e5e5", lw=0.6); ax.set_axisbelow(True)
save(fig, "gambar-1-rilis-per-bidang")

# Gambar 2: rilis per bulan per bidang
fig, ax = plt.subplots(figsize=(W, 2.9))
x = np.arange(len(ORDER)); w = 0.26
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
ada = [b for b in BULAN if any(bln[k][b] for k in bln)]
WARNA = [INK, MID, LIGHT, "#5b7fa6", "#bfcfe0", "#666666"]
w = 0.8 / max(len(ada), 1)
for j, (m, c) in enumerate(zip(ada, WARNA)):
    v = [bln[k][m] for k in ORDER]
    bb = ax.bar(x + (j - (len(ada) - 1) / 2) * w, v, w, color=c, edgecolor=INK, linewidth=0.4, label=m)
    for b, vi in zip(bb, v):
        if vi:
            ax.text(b.get_x() + b.get_width() / 2, vi + 0.08, str(vi), ha="center", fontsize=7.5)
ax.set_xticks(x); ax.set_xticklabels([SHORT.get(k, k).replace(" & ", " &\n") for k in ORDER], fontsize=8.2)
ax.set_ylabel("Jumlah rilis"); ax.legend(ncol=len(ada), fontsize=8.3, loc="upper right")
ax.grid(axis="y", color="#e5e5e5", lw=0.6); ax.set_axisbelow(True)
save(fig, "gambar-2-rilis-per-bulan")

# Gambar 3: pemberitaan per isu (Agu–Okt)
ISU = {k: k for k in ["Hutan & Kebun", "Urban", "Tambang & Energi", "Pangan & Ekosistem Esensial", "Iklim & Isu Global", "Pesisir & Laut"]}
semua, judul, media = PB["semua"], PB["judul_walhi"], PB["media"]
order3 = sorted(ISU, key=lambda k: semua[k])
fig, ax = plt.subplots(figsize=(W, 2.8))
y = np.arange(len(order3))
ax.barh(y, [semua[k] for k in order3], color=LIGHT, edgecolor=INK, linewidth=0.4, label="WALHI disebut di judul atau isi")
ax.barh(y, [judul[k] for k in order3], height=0.45, color=ACCENT, label="WALHI disebut di judul")
for yi, k in zip(y, order3):
    ax.text(semua[k] + 8, yi, f"{semua[k]} berita · {media[k]} media", va="center", fontsize=8.3)
ax.set_yticks(y); ax.set_yticklabels([ISU[k] for k in order3], fontsize=9)
ax.set_xlim(0, max(semua.values()) * 1.35)
ax.set_xlabel(f"Jumlah berita {PER} (n = {PB['unik_judul_walhi']} judul memuat WALHI; satu berita bisa masuk >1 isu)", fontsize=8.5)
ax.legend(fontsize=8, loc="lower right")
save(fig, "gambar-3-pemberitaan-per-isu")

# Gambar 4: respons tertinggi per bidang
B4 = [k for k in ["Hutan & Kebun", "Pesisir & Laut", "Urban", "Pangan & Ekosistem Esensial", "Iklim & Isu Global", "Tambang & Energi"] if k in S]
lv = [("tidak ada respons", lambda s: s["rilis"] - s["ada_respons"], "#ffffff"), ("ditolak", lambda s: s["ditolak"], LIGHT),
      ("dijanjikan/diakui", lambda s: s["dijanjikan"], MID), ("tindakan generik", lambda s: s["tindakan_generik"], "#9db7d1"),
      ("tindakan nyata", lambda s: s["tindakan_nyata"], ACCENT)]
fig, ax = plt.subplots(figsize=(W, 3.0))
y = np.arange(len(B4))[::-1]; left = np.zeros(len(B4))
for labl, f, c in lv:
    v = np.array([f(S[k]) for k in B4])
    ax.barh(y, v, left=left, color=c, edgecolor=INK, linewidth=0.5, label=labl)
    for yi, l, vi in zip(y, left, v):
        if vi:
            ax.text(l + vi / 2, yi, str(vi), ha="center", va="center", fontsize=8, color="white" if c == ACCENT else INK)
    left += v
for yi, k in zip(y, B4):
    s = S[k]
    ax.text(s["rilis"] + 0.2, yi, f"respons {s['pct_ada_respons']}% · tindakan {s['pct_tindakan_nyata']}%", va="center", fontsize=7.8)
ax.set_yticks(y); ax.set_yticklabels([f"{SHORT.get(k, k)} (n={S[k]['rilis']})" for k in B4], fontsize=8.6)
ax.set_xlim(0, max(S[k]["rilis"] for k in B4) * 1.55)
ax.set_xlabel("Jumlah rilis bertuntutan spesifik menurut respons tertinggi pemerintah", fontsize=8.5)
ax.legend(ncol=3, fontsize=7.6, loc="lower left", bbox_to_anchor=(0, 1.0))
save(fig, "gambar-4-respons-per-bidang")
print("ok:", sorted(os.listdir(OUT)))

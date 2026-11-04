"""Hitung pemberitaan WALHI per isu dari korpus_walhi.py.

Pakai: python3 -I hitung_pemberitaan.py --korpus korpus.json --mulai 2026-11-01 --selesai 2026-11-30 --out pemberitaan.json [--sampel 30]

Aturan:
- Item dari kanal WALHI dibuang; judul ganda dihitung sekali.
- Isu ditentukan dari judul (setelah akhiran nama media dibuang) dengan kata kunci isu + aturan lokus pesisir.
- "semua" = WALHI disebut di judul atau isi (semua item korpus berasal dari kueri yang memuat "walhi").
- "judul_walhi" = WALHI tertulis di judul.
--sampel N mencetak N judul acak per isu untuk dicek ketepatannya.
"""
import argparse, collections, datetime as dt, email.utils, json, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import klasifikasi_isu as K  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--korpus", required=True); ap.add_argument("--mulai", required=True); ap.add_argument("--selesai", required=True)
    ap.add_argument("--out", required=True); ap.add_argument("--sampel", type=int, default=0)
    a = ap.parse_args()
    m, s = dt.date.fromisoformat(a.mulai), dt.date.fromisoformat(a.selesai)
    k = json.load(open(a.korpus))
    items = {}
    for w in k["umum"] + [w for ws in k["per_isu"].values() for w in ws]:
        for i in w["items"]:
            src = (i.get("src") or "").strip()
            if src.upper() == "WALHI":
                continue
            d = email.utils.parsedate_to_datetime(i["date"]).date()
            if m <= d <= s and i["title"] not in items:
                items[i["title"]] = {"judul": i["title"], "media": src, "tanggal": str(d)}
    semua, judul, media, irisan = collections.Counter(), collections.Counter(), collections.defaultdict(set), collections.Counter()
    per_isu = collections.defaultdict(list)
    for it in items.values():
        isu = K.tag(it["judul"], it["media"])
        di_judul = bool(re.search("walhi", K.bersih(it["judul"], it["media"]), re.I))
        for x in isu:
            semua[x] += 1; media[x].add(it["media"]); per_isu[x].append(it["judul"])
            if di_judul:
                judul[x] += 1
        if "Pesisir & Laut" in isu:
            for x in isu:
                if x != "Pesisir & Laut":
                    irisan[x] += 1
    out = {"periode": [a.mulai, a.selesai], "unik_semua": len(items),
           "unik_judul_walhi": sum(bool(re.search("walhi", K.bersih(i["judul"], i["media"]), re.I)) for i in items.values()),
           "semua": dict(semua), "judul_walhi": dict(judul), "media": {x: len(v) for x, v in media.items()},
           "irisan_pesisir": dict(irisan), "kueri_gagal_korpus": len(k.get("kueri_gagal", []))}
    json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if a.sampel:
        random.seed(7)
        for x, js in per_isu.items():
            print(f"\n== sampel {x}")
            for j in random.sample(js, min(a.sampel, len(js))):
                print(" -", j[:120])


if __name__ == "__main__":
    main()

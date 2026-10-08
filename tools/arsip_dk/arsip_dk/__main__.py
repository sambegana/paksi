"""python -m arsip_dk <tahap> ...  — lihat README.md untuk urutan lengkap."""

import argparse

from . import apply, audit, classify, preview, propose


def main():
    p = argparse.ArgumentParser(prog="python -m arsip_dk")
    sub = p.add_subparsers(dest="tahap", required=True)

    a = sub.add_parser("audit", help="1. daftar semua media, duplikat, sumber tanggal (hanya baca)")
    a.add_argument("--drive", default="Delta Kapuas", help="nama Shared Drive")
    a.add_argument("--drive-id", help="ID Shared Drive (jika nama tidak unik)")
    a.add_argument("--bandingkan", metavar="NAMA_DRIVE",
                   help="cek file mana di drive ini (mis. 'Sampan Kalimantan') yang belum ada di tujuan")
    a.set_defaults(fungsi=audit.jalankan)

    v = sub.add_parser("pratinjau", help="2. ambil thumbnail foto & cuplikan video (hanya baca)")
    v.add_argument("--batas", type=int, help="proses N file saja (untuk pilot)")
    v.add_argument("--paralel", type=int, default=4)
    v.add_argument("--ukuran", type=int, default=1568, help="sisi terpanjang pratinjau (px)")
    v.set_defaults(fungsi=preview.jalankan)

    k = sub.add_parser("analisis", help="3. analisis visual dengan Claude")
    k.add_argument("--batas", type=int, help="proses N file saja (untuk pilot)")
    k.add_argument("--paralel", type=int, default=4)
    k.add_argument("--model", default="claude-opus-5-5")
    k.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    k.set_defaults(fungsi=classify.jalankan)

    s = sub.add_parser("susun", help="4. buat usulan_nama.csv untuk ditinjau")
    s.set_defaults(fungsi=propose.jalankan)

    t = sub.add_parser("terapkan", help="5. rename + isi Description (default simulasi)")
    t.add_argument("--jalankan", action="store_true", help="benar-benar ubah Drive")
    t.add_argument("--ya", action="store_true", help="lewati konfirmasi ketik YA")
    t.set_defaults(fungsi=apply.terapkan)

    r = sub.add_parser("pulihkan", help="batalkan perubahan dari satu file log terapkan")
    r.add_argument("log", help="path log/terapkan_<waktu>.csv")
    r.add_argument("--ya", action="store_true")
    r.set_defaults(fungsi=apply.pulihkan)

    args = p.parse_args()
    args.fungsi(args)


if __name__ == "__main__":
    main()

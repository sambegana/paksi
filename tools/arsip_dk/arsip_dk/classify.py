"""Tahap 3 — analisis visual dengan Claude. Belum ada perubahan di Drive.

Setiap pratinjau dikirim ke Claude API beserta konteks (nama asli, folder asal,
tanggal, GPS). Hasil terstruktur (JSON schema) disimpan per baris di klasifikasi.jsonl;
menjalankan ulang tahap ini hanya memproses yang belum ada (bisa dilanjutkan).
"""

import base64
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

import anthropic

from . import config
from .names import muat_vocab
from .preview import path_pratinjau, wakil_per_isi

# Harga per juta token (USD) untuk estimasi biaya di akhir proses.
HARGA = {
    "claude-opus-5-5": (4.00, 20.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-haiku-5-5": (0.10, 0.50),
}

_kunci = threading.Lock()


def skema(vocab):
    kode = list(vocab)
    return {
        "type": "object",
        "properties": {
            "kategori_utama": {"type": "string", "enum": kode},
            "kategori_lain": {"type": "array", "items": {"type": "string", "enum": kode}},
            "deskripsi_singkat": {"type": "string"},
            "tag": {"type": "array", "items": {"type": "string"}},
            "keterangan": {"type": "string"},
            "lokasi": {"type": "string"},
            "sumber_lokasi": {"type": "string", "enum": ["tidak_ada", "folder_atau_nama_file", "gps", "tulisan_di_gambar"]},
            "ada_orang": {"type": "boolean"},
            "ada_anak": {"type": "boolean"},
            "keyakinan": {"type": "string", "enum": ["tinggi", "sedang", "rendah"]},
            "catatan_review": {"type": "string"},
        },
        "required": ["kategori_utama", "kategori_lain", "deskripsi_singkat", "tag", "keterangan",
                     "lokasi", "sumber_lokasi", "ada_orang", "ada_anak", "keyakinan", "catatan_review"],
        "additionalProperties": False,
    }


def prompt_sistem(vocab):
    daftar = "\n".join(f"- {k}: {v['nama']} — {v['panduan']}" for k, v in vocab.items())
    return f"""Anda mengkatalogkan arsip foto dan video lapangan sebuah organisasi yang bekerja di Delta Kapuas, Kalimantan Barat (pesisir, mangrove, sungai, kampung nelayan). Tujuannya: setiap file mudah ditemukan lewat pencarian Google Drive bertahun-tahun kemudian. Semua isian ditulis dalam Bahasa Indonesia.

Kategori (pilih tepat satu kategori_utama = subjek yang paling menonjol; kategori lain yang juga jelas terlihat masuk kategori_lain):
{daftar}

Aturan isian:
- deskripsi_singkat: 2–5 kata, huruf kecil, menggambarkan isi visual yang membedakan file ini dari file lain dalam kategori yang sama (contoh: "akar tunjang tepi sungai", "warga menanam bibit"). Jangan mengulang nama kategori saja.
- tag: 5–12 kata kunci yang kemungkinan diketik orang saat mencari (benda, kegiatan, suasana, jenis lanskap; sertakan sinonim lokal yang umum seperti "bakau" untuk mangrove).
- keterangan: 1–2 kalimat faktual tentang apa yang terlihat.
- lokasi: isi HANYA jika didukung nama folder/nama file, koordinat GPS, atau tulisan yang terbaca di gambar; sebutkan sumbernya di sumber_lokasi. Selain itu kosongkan dan pilih "tidak_ada".
- Jangan menebak nama orang, nama desa, nama acara, atau spesies tertentu dari penampilan saja. Spesies boleh disebut hanya jika ciri pembedanya jelas terlihat; kalau ragu, pakai nama umum ("mangrove", "burung") dan catat keraguan di catatan_review.
- Folder asal dan nama file asli sering memuat konteks berharga (nama kegiatan, desa, tahun). Pakai itu untuk lokasi/tag, tetapi jika bertentangan dengan isi gambar, ikuti gambar dan catat konfliknya di catatan_review.
- ada_anak: true jika tampak orang yang kemungkinan berusia di bawah 18 tahun.
- keyakinan: "tinggi" jika kategori dan deskripsi jelas dari gambar; "sedang" jika ada ambiguitas kecil; "rendah" jika gambar buram/gelap/terpotong atau kategori sulit ditentukan.
- catatan_review: hal yang perlu dicek manusia; kosongkan jika tidak ada.
- Untuk video Anda melihat lembar kontak berisi beberapa cuplikan bingkai dari sepanjang video; deskripsikan video secara keseluruhan."""


def _konteks(m, meta_video):
    baris = [f"Jenis: {m['jenis']}", f"Nama file asli: {m['nama']}",
             f"Folder asal: {m['folder'] or '(akar drive)'}"]
    if m["tanggal"] != "00000000":
        baris.append(f"Tanggal (dari {m['sumber_tanggal']}): {m['tanggal']}")
    if m["gps_lat"] != "":
        baris.append(f"GPS: {m['gps_lat']}, {m['gps_lon']}")
    if m["jenis"] == "video" and meta_video.get(m["id"]):
        baris.append(f"Durasi: {meta_video[m['id']].get('durasi_detik', 0):.0f} detik")
    if m["deskripsi_lama"]:
        baris.append(f"Description yang sudah ada di Drive: {m['deskripsi_lama'][:500]}")
    return "\n".join(baris)


def _panggil(client, model, effort, sistem, sch, m, meta_video):
    data = base64.standard_b64encode(path_pratinjau(m["id"]).read_bytes()).decode()
    resp = client.beta.messages.create(
        model=model,
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        system=sistem,
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": sch}},
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data}},
            {"type": "text", "text": _konteks(m, meta_video)},
        ]}],
    )
    if resp.stop_reason == "refusal":
        kategori = resp.stop_details.category if resp.stop_details else None
        raise RuntimeError(f"ditolak oleh model (kategori: {kategori})")
    if resp.stop_reason == "max_tokens":
        raise RuntimeError("keluaran terpotong (max_tokens)")
    teks = next(b.text for b in resp.content if b.type == "text")
    return json.loads(teks), resp.usage, resp.model


def jalankan(args):
    config.siapkan()
    vocab = muat_vocab()
    sistem, sch = prompt_sistem(vocab), skema(vocab)
    inventaris = config.baca_jsonl(config.INVENTARIS)
    meta_video = {v["id"]: v for v in config.baca_jsonl(config.META_VIDEO)}
    sudah = {k["id"] for k in config.baca_jsonl(config.KLASIFIKASI)}
    target = [m for m in wakil_per_isi(inventaris)
              if m["id"] not in sudah and path_pratinjau(m["id"]).exists()]
    if args.batas:
        target = target[: args.batas]
    print(f"{len(target)} file akan dianalisis dengan {args.model} (effort {args.effort}).")

    client = anthropic.Anthropic(max_retries=5)
    tok_in = tok_out = 0
    gagal = []
    with ThreadPoolExecutor(max_workers=args.paralel) as ex:
        tugas = {ex.submit(_panggil, client, args.model, args.effort, sistem, sch, m, meta_video): m
                 for m in target}
        for i, t in enumerate(as_completed(tugas), 1):
            m = tugas[t]
            try:
                hasil, usage, dilayani = t.result()
            except anthropic.AuthenticationError:
                raise SystemExit("ANTHROPIC_API_KEY tidak valid atau belum di-set.")
            except anthropic.BadRequestError as e:
                gagal.append((m, f"permintaan ditolak API: {e.message}"))
                continue
            except anthropic.APIStatusError as e:
                gagal.append((m, f"galat API {e.status_code}: {e.message}"))
                continue
            except anthropic.APIConnectionError:
                gagal.append((m, "koneksi gagal"))
                continue
            except (RuntimeError, ValueError, StopIteration) as e:
                gagal.append((m, str(e) or type(e).__name__))
                continue
            tok_in += usage.input_tokens
            tok_out += usage.output_tokens
            baris = {"id": m["id"], "md5": m["md5"], "model": dilayani, **hasil}
            with _kunci, open(config.KLASIFIKASI, "a", encoding="utf-8") as f:
                f.write(json.dumps(baris, ensure_ascii=False) + "\n")
            if i % 10 == 0 or i == len(target):
                print(f"  {i}/{len(target)}  gagal={len(gagal)}  token masuk={tok_in:,} keluar={tok_out:,}")

    if args.model in HARGA:
        p_in, p_out = HARGA[args.model]
        print(f"Perkiraan biaya sesi ini: ${tok_in / 1e6 * p_in + tok_out / 1e6 * p_out:.2f}")
    if gagal:
        path = config.LOG_DIR / "klasifikasi_gagal.csv"
        config.tulis_csv(path, ["id", "folder", "nama", "galat"],
                         [{"id": m["id"], "folder": m["folder"], "nama": m["nama"], "galat": e}
                          for m, e in gagal])
        print(f"{len(gagal)} gagal, lihat {path}. Jalankan ulang tahap ini untuk mencoba lagi.")

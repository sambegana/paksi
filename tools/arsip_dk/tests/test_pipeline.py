import argparse
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from arsip_dk import apply, config, names, propose


class TestNama(unittest.TestCase):
    def test_tanggal_exif_dan_iso(self):
        self.assertEqual(names.tanggal_dari_metadata("2024:03:15 10:22:11"), "20240315")
        self.assertEqual(names.tanggal_dari_metadata("2024-03-15T10:22:11.000000Z"), "20240315")

    def test_tanggal_kamera_belum_diatur_ditolak(self):
        self.assertIsNone(names.tanggal_dari_metadata("1970:01:01 00:00:00"))
        self.assertIsNone(names.tanggal_dari_metadata("2000:01:01 00:00:00"))
        self.assertIsNone(names.tanggal_dari_metadata("2024:13:40 00:00:00"))

    def test_tanggal_dari_nama_file(self):
        self.assertEqual(names.tanggal_dari_nama("IMG_20230812_101500.jpg"), "20230812")
        self.assertEqual(names.tanggal_dari_nama("VID-20240105-WA0007.mp4"), "20240105")
        self.assertEqual(names.tanggal_dari_nama("Penanaman 2023-11-02.jpg"), "20231102")
        self.assertIsNone(names.tanggal_dari_nama("DSC_4821.JPG"))
        # Nomor panjang yang kebetulan berisi angka mirip tanggal tidak boleh terbaca.
        self.assertIsNone(names.tanggal_dari_nama("1202403150001.jpg"))

    def test_prioritas_sumber_tanggal(self):
        self.assertEqual(names.tentukan_tanggal("2022:01:02 00:00:00", None, "IMG_20240101.jpg"),
                         ("20220102", "exif"))
        self.assertEqual(names.tentukan_tanggal(None, None, "IMG_20240101.jpg"), ("20240101", "nama_file"))
        self.assertEqual(names.tentukan_tanggal(None, None, "x.jpg"), ("00000000", "tidak_diketahui"))

    def test_slug(self):
        self.assertEqual(names.slug("Akar Tunjang di Tepi Sungai!"), "akar-tunjang-di-tepi-sungai")
        self.assertEqual(names.slug("Pembibitan  Mangrove — Desa Sungai Kakap Barat"),
                         "pembibitan-mangrove-desa-sungai-kakap")
        self.assertEqual(names.slug("Rumah Ibu Siti é"), "rumah-ibu-siti-e")

    def test_susun_nama(self):
        self.assertEqual(names.susun_nama("20240315", "MGV", 42, "akar tunjang", ".jpg"),
                         "DK_20240315_MGV_00042_akar-tunjang.jpg")
        self.assertEqual(names.susun_nama("00000000", "LLN", 7, "", ".mp4"), "DK_00000000_LLN_00007.mp4")
        with self.assertRaises(ValueError):
            names.susun_nama("2024315", "MGV", 1, "x", ".jpg")
        with self.assertRaises(ValueError):
            names.susun_nama("20240315", "mangrove", 1, "x", ".jpg")

    def test_ekstensi(self):
        self.assertEqual(names.ekstensi("IMG_1.JPG"), ".jpg")
        self.assertEqual(names.ekstensi("tanpa ekstensi", "video/mp4"), ".mp4")
        self.assertEqual(names.ekstensi("Laporan v1.2 final", "image/jpeg"), ".jpg")

    def test_description_mempertahankan_teks_manusia(self):
        blok1 = "[arsip-dk]\nkode: DK-00001\n[/arsip-dk]"
        blok2 = "[arsip-dk]\nkode: DK-00001\ntag: bakau\n[/arsip-dk]"
        d = names.gabung_description("Foto oleh Pak Budi", blok1)
        self.assertEqual(d, "Foto oleh Pak Budi\n\n" + blok1)
        d2 = names.gabung_description(d, blok2)
        self.assertEqual(d2, "Foto oleh Pak Budi\n\n" + blok2)
        self.assertEqual(names.gabung_description("", blok1), blok1)

    def test_vocab_valid(self):
        vocab = names.muat_vocab()
        self.assertIn("LLN", vocab)
        for kode, isi in vocab.items():
            self.assertRegex(kode, r"^[A-Z]{3}$")
            self.assertTrue(isi["nama"] and isi["panduan"])


def _media(id_, nama, md5, folder="Kegiatan 2023", exif="", jenis="foto"):
    return {"id": id_, "nama": nama, "folder": folder, "mime": "image/jpeg", "jenis": jenis,
            "ukuran": 1000, "md5": md5, "waktu_exif": exif, "tanggal": "", "sumber_tanggal": "",
            "durasi_ms": 0, "lebar": "", "tinggi": "", "gps_lat": "", "gps_lon": "", "kamera": "",
            "deskripsi_lama": "", "ada_thumbnail": True, "dibuat_di_drive": "", "link": ""}


def _klas(id_, md5, kat="MGV", yakin="tinggi", catatan=""):
    return {"id": id_, "md5": md5, "model": "x", "kategori_utama": kat, "kategori_lain": ["SNG"],
            "deskripsi_singkat": "Akar Tunjang Tepi Sungai", "tag": ["Bakau", "mangrove", "bakau"],
            "keterangan": "Akar mangrove di tepi sungai.", "lokasi": "", "sumber_lokasi": "tidak_ada",
            "ada_orang": False, "ada_anak": False, "keyakinan": yakin, "catatan_review": catatan}


class DriveTiruan:
    """Cukup untuk files().get(...).execute() dan files().update(...).execute()."""

    def __init__(self, isi):
        self.isi = isi  # id -> {"name", "description"}

    def files(self):
        return self

    def get(self, fileId, **_):
        return mock.Mock(execute=lambda **__: dict(self.isi[fileId]))

    def update(self, fileId, body, **_):
        def jalan(**__):
            self.isi[fileId].update(body)
            return {"id": fileId}
        return mock.Mock(execute=jalan)


class TestAlurOffline(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.patch = mock.patch.multiple(
            config, DATA=d, INVENTARIS=d / "inv.jsonl", META_VIDEO=d / "mv.jsonl",
            KLASIFIKASI=d / "k.jsonl", NOMOR=d / "nomor.json", USULAN=d / "usulan.csv",
            RENCANA=d / "rencana.csv", LOG_DIR=d / "log", PRATINJAU_DIR=d / "p",
        )
        self.patch.start()
        self.inv = [
            _media("a", "IMG_20240315_1.jpg", "m1", exif="2024:03:15 08:00:00"),
            _media("b", "salinan.jpg", "m1", folder="Duplikat"),
            _media("c", "DSC_9.JPG", "m2"),
            _media("d", "buram.jpg", "m3"),
        ]
        config.tulis_jsonl(config.INVENTARIS, self.inv)
        config.tulis_jsonl(config.KLASIFIKASI, [
            _klas("a", "m1"), _klas("c", "m2", kat="KGT"), _klas("d", "m3", kat="LLN", yakin="rendah"),
        ])

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def test_susun_terapkan_pulihkan(self):
        with mock.patch("builtins.print"):
            propose.jalankan(argparse.Namespace())
        usulan = {b["file_id"]: b for b in config.baca_csv(config.USULAN)}

        # Bertanggal lebih dulu, yang tanpa tanggal di belakang.
        self.assertEqual(usulan["a"]["nama_baru"], "DK_20240315_MGV_00001_akar-tunjang-tepi-sungai.jpg")
        self.assertEqual(usulan["a"]["status"], "ok")
        self.assertEqual(usulan["a"]["tag"], "bakau, mangrove")
        self.assertEqual(usulan["b"]["status"], "review")
        self.assertTrue(usulan["b"]["duplikat_dari"].startswith("00001"))
        self.assertEqual(usulan["c"]["nama_baru"], "DK_00000000_KGT_00003_akar-tunjang-tepi-sungai.jpg")
        self.assertEqual(usulan["d"]["status"], "review")

        # Nomor stabil saat dijalankan ulang.
        with mock.patch("builtins.print"):
            propose.jalankan(argparse.Namespace())
        self.assertEqual(json.loads(config.NOMOR.read_text()), {"a": 1, "b": 2, "c": 3, "d": 4})

        # Peninjau: koreksi deskripsi c dan simulasikan Excel membuang nol tanggal.
        baris = config.baca_csv(config.USULAN)
        for b in baris:
            if b["file_id"] == "c":
                b["deskripsi_singkat"] = "rapat warga di balai desa"
                b["tanggal"] = "0"
        config.tulis_csv(config.USULAN, propose.KOLOM, baris)

        drive_tiruan = DriveTiruan({m["id"]: {"name": m["nama"], "description": ""} for m in self.inv})
        drive_tiruan.isi["a"]["description"] = "Foto oleh tim lapangan"
        with mock.patch.object(apply.drive, "layanan", return_value=drive_tiruan), \
             mock.patch.object(apply.drive, "kredensial"), mock.patch.object(apply, "JEDA_DETIK", 0), \
             mock.patch("builtins.print"):
            # Simulasi tidak mengubah apa pun.
            apply.terapkan(argparse.Namespace(jalankan=False, ya=True))
            self.assertEqual(drive_tiruan.isi["a"]["name"], "IMG_20240315_1.jpg")

            apply.terapkan(argparse.Namespace(jalankan=True, ya=True))
            self.assertEqual(drive_tiruan.isi["a"]["name"], "DK_20240315_MGV_00001_akar-tunjang-tepi-sungai.jpg")
            self.assertEqual(drive_tiruan.isi["c"]["name"], "DK_00000000_KGT_00003_rapat-warga-di-balai-desa.jpg")
            self.assertEqual(drive_tiruan.isi["b"]["name"], "salinan.jpg")  # status review, tidak disentuh
            desk = drive_tiruan.isi["a"]["description"]
            self.assertTrue(desk.startswith("Foto oleh tim lapangan\n\n[arsip-dk]"))
            self.assertIn("nama asli: IMG_20240315_1.jpg", desk)
            self.assertIn("tag: bakau, mangrove", desk)

            # Menjalankan ulang tidak menulis apa pun (idempoten).
            log_sebelum = set(config.LOG_DIR.iterdir())
            apply.terapkan(argparse.Namespace(jalankan=True, ya=True))
            log_baru = (set(config.LOG_DIR.iterdir()) - log_sebelum).pop()
            self.assertEqual(len(config.baca_csv(log_baru)), 0)

            log_pertama = sorted(log_sebelum)[0]
            apply.pulihkan(argparse.Namespace(log=log_pertama, ya=True))
        self.assertEqual(drive_tiruan.isi["a"], {"name": "IMG_20240315_1.jpg", "description": "Foto oleh tim lapangan"})
        self.assertEqual(drive_tiruan.isi["c"]["name"], "DSC_9.JPG")

    def test_nama_asli_bertahan_setelah_rename(self):
        m = _media("a", "DK_20240315_MGV_00001_x.jpg", "m1")
        m["deskripsi_lama"] = "[arsip-dk]\nnama asli: IMG_20240315_1.jpg\n[/arsip-dk]"
        self.assertEqual(propose.nama_asli(m), "IMG_20240315_1.jpg")

    def test_kategori_tak_dikenal_menghentikan_terapkan(self):
        with mock.patch("builtins.print"):
            propose.jalankan(argparse.Namespace())
        baris = config.baca_csv(config.USULAN)
        baris[0]["kategori"] = "XYZ"
        config.tulis_csv(config.USULAN, propose.KOLOM, baris)
        with mock.patch("builtins.print"), self.assertRaises(SystemExit):
            apply.terapkan(argparse.Namespace(jalankan=True, ya=True))


class TestPanggilClaude(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.patch = mock.patch.object(config, "PRATINJAU_DIR", Path(self.tmp.name))
        self.patch.start()
        (Path(self.tmp.name) / "a.jpg").write_bytes(b"\xff\xd8gambar")
        self.vocab = names.muat_vocab()

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def _respons(self, stop="end_turn", teks=None):
        isi = [mock.Mock(type="thinking"), mock.Mock(type="text", text=teks or json.dumps(_klas("a", "m1")))]
        return mock.Mock(stop_reason=stop, content=isi, model="claude-opus-5-5", stop_details=None,
                         usage=mock.Mock(input_tokens=10, output_tokens=5))

    def test_permintaan_dan_parsing(self):
        from arsip_dk import classify
        client = mock.Mock()
        client.beta.messages.create.return_value = self._respons()
        m = _media("a", "IMG_20240315_1.jpg", "m1", exif="2024:03:15 08:00:00")
        m.update(tanggal="20240315", sumber_tanggal="exif", gps_lat=-0.1, gps_lon=109.2)
        hasil, _, _ = classify._panggil(client, "claude-opus-5-5", "medium",
                                        classify.prompt_sistem(self.vocab), classify.skema(self.vocab), m, {})
        self.assertEqual(hasil["kategori_utama"], "MGV")
        kw = client.beta.messages.create.call_args.kwargs
        self.assertEqual(kw["fallbacks"], "default")
        self.assertEqual(kw["betas"], ["server-side-fallback-2026-07-01"])
        self.assertEqual(kw["output_config"]["format"]["schema"]["properties"]["kategori_utama"]["enum"],
                         list(self.vocab))
        teks = kw["messages"][0]["content"][1]["text"]
        self.assertIn("Folder asal: Kegiatan 2023", teks)
        self.assertIn("GPS: -0.1, 109.2", teks)

    def test_penolakan_menjadi_galat(self):
        from arsip_dk import classify
        client = mock.Mock()
        client.beta.messages.create.return_value = self._respons(stop="refusal")
        with self.assertRaises(RuntimeError):
            classify._panggil(client, "claude-opus-5-5", "medium", "", {}, _media("a", "x.jpg", "m1"), {})


if __name__ == "__main__":
    unittest.main()

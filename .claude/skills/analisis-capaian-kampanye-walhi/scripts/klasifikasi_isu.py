"""Kata kunci isu kampanye WALHI dan aturan lokus pesisir. Dipakai sebagai modul.

Nama isu mengikuti nama bidang di laporan divisi. Satu judul boleh masuk lebih dari satu isu.
Selalu panggil bersih() dulu supaya akhiran " - Nama Media" tidak ikut tercocokkan.
"""
import re

ISU = {
    "Pesisir & Laut": r"coastal|\bsea\b|fisher|pesisir|\blaut|reklamasi|nelayan|pagar laut|mangrove|pulau kecil|pulau-pulau|abrasi|"
                      r"tambak|pantai|sedimentasi|terumbu|kelautan|\bkkp\b|perikanan|teluk|\brob\b",
    "Hutan & Kebun": r"forest|\bfire|haze|ispa|\btpl\b|toba pulp|kebun|way kambas|tnwk|tnks|pembalakan|peladang|orangutan|satwa|"
                     r"karhutla|kebakaran hutan|kebakaran lahan|\bhutan|sawit|deforestasi|perkebunan|\bhgu\b|kayu|pbph|\bhti\b|akasia|"
                     r"konsesi|kabut asap|asap|titik panas|hotspot|taman nasional|kemenhut|menhut|satgas pkh|masyarakat adat|"
                     r"tanah adat|ulayat|agraria|konflik lahan",
    "Tambang & Energi": r"geothermal|plta|thorcon|timah|\bpeti\b|iwip|mining|nickel|coal|tambang|pertambangan|nikel|batu ?bara|"
                        r"smelter|pltu|\bpltn|nuklir|energi|geotermal|panas bumi|\bpltp|minerba|\biup\b|galian|\bemas\b|pasir|"
                        r"hilirisasi|listrik|transisi energi|biomassa|co-?firing|migas|pertamina",
    "Urban": r"pemkot|data center|pusat data|alih fungsi|markas|\bcity\b|\bkota\b|perkotaan|tata ruang|\brtrw|\brdtr|banjir|sampah|"
             r"\bpsn\b|proyek strategis|\bikn\b|ibu kota nusantara|polusi udara|kualitas udara|air bersih|limbah|\btpa\b|penggusuran|"
             r"omnibus|cipta kerja|amdal|perizinan|kawasan industri|tanggul",
    "Iklim & Isu Global": r"climate|iklim|\bcop\s?3\d|cop-?3\d|emisi|karbon|net zero|\bndc\b|el ?nino|la ?nina|pemanasan global|"
                          r"krisis iklim|perdagangan karbon|\bjetp\b|internasional|global|uni eropa|eudr|malaysia|singapura|asean|"
                          r"lintas batas|\bpbb\b|\bun\b|brics",
    "Pangan & Ekosistem Esensial": r"mata air|krisis air|lahan kritis|\bfood\b|pangan|food estate|lumbung|sawah|cetak sawah|petani|"
                                   r"pertanian|gambut|karst|\bdas\b|danau|sungai|rawa|lahan basah|ekosistem esensial|kekeringan|"
                                   r"benih|merauke|swasembada|kedaulatan pangan|\bmbg\b|makan bergizi",
}
# Lokus pesisir: berita tambang/PSN/data center di laut, pesisir, perairan, pulau kecil ikut Pesisir & Laut.
# Pulau besar dikecualikan. Tambahkan nama kasus pesisir periode berjalan ke KASUS_PESISIR.
KASUS_PESISIR = ["rempang", r"\bobi\b", "kawasi", "gelasa", "batu beriga", "pantura", "giant sea wall", "tanggul laut",
                 "wilayah tangkap", "petambak", "pasir laut", r"\bbopp", "otorita pantai", "batam", "teluk kelabat", "pulau pari"]
PESISIR_LOKUS = (r"perairan|pulau-pulau kecil|pulau kecil|daerah kepulauan|"
                 r"pulau(?!\s+(jawa|sumatera|sumatra|kalimantan|sulawesi|papua|bali|borneo)\b)\s+[a-z]|" + "|".join(KASUS_PESISIR))
ISU_LOKUS = dict(ISU)
ISU_LOKUS["Pesisir & Laut"] = ISU["Pesisir & Laut"] + "|" + PESISIR_LOKUS


def bersih(judul, media=None):
    """Buang akhiran ' - Nama Media' dari judul Google News."""
    if media and judul.endswith(" - " + media):
        return judul[: -len(media) - 3]
    return judul.rsplit(" - ", 1)[0] if " - " in judul else judul


def tag(judul, media=None, lokus=True):
    t = bersih(judul, media)
    pola = ISU_LOKUS if lokus else ISU
    return [k for k, p in pola.items() if re.search(p, t, re.I)]

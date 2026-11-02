import json, re, sys, collections
ISU = {
 "Pesisir & Laut": r"coastal|\bsea\b|fisher|pesisir|\blaut|reklamasi|nelayan|pagar laut|mangrove|pulau kecil|pulau-pulau|abrasi|tambak|pantai|sedimentasi|terumbu|kelautan|\bkkp\b|perikanan|teluk|rob\b",
 "Hutan & Kebun": r"forest|fire|haze|ispa|\btpl\b|toba pulp|kebun|way kambas|tnwk|tnks|pembalakan|peladang|orangutan|satwa|karhutla|kebakaran hutan|kebakaran lahan|\bhutan|sawit|deforestasi|perkebunan|\bhgu\b|kayu|pbph|\bhti\b|akasia|konsesi|kabut asap|asap|titik panas|hotspot|taman nasional|kemenhut|menhut|satgas pkh|masyarakat adat|tanah adat|ulayat|agraria|konflik lahan",
 "Tambang & Energi": r"geothermal|plta|thorcon|timah|\bpeti\b|iwip|mining|nickel|coal|tambang|pertambangan|nikel|batu ?bara|smelter|pltu|\bpltn|nuklir|energi|geotermal|panas bumi|\bpltp|minerba|\biup\b|galian|emas|pasir|hilirisasi|listrik|transisi energi|biomassa|co-?firing|migas|pertamina",
 "Perkotaan & Tata Ruang": r"pemkot|data center|pusat data|alih fungsi|markas|\bcity\b|kota|perkotaan|tata ruang|\brtrw|\brdtr|banjir|sampah|\bpsn\b|proyek strategis|ikn|ibu kota nusantara|polusi udara|kualitas udara|air bersih|limbah|tpa\b|penggusuran|omnibus|cipta kerja|amdal|perizinan|kawasan industri|tanggul",
 "Iklim & Global": r"climate|iklim|\bcop\s?3\d|cop30|cop31|emisi|karbon|net zero|\bndc\b|el ?nino|la ?nina|pemanasan global|krisis iklim|perdagangan karbon|\bjetp\b|internasional|global|uni eropa|eudr|malaysia|singapura|asean|lintas batas|\bpbb\b|\bun\b",
 "Ekosistem Esensial & Pangan": r"mata air|krisis air|lahan kritis|\bfood\b|pangan|food estate|lumbung|sawah|cetak sawah|petani|pertanian|gambut|karst|\bdas\b|danau|sungai|rawa|lahan basah|ekosistem esensial|kekeringan|benih|merauke|swasembada|kedaulatan pangan|mbg|makan bergizi",
}
def load(path):
    r = json.load(open(path)); seen = {}; own = 0
    for w in r:
        for i in w["items"]:
            t = i["title"]
            if not re.search(r"walhi", t, re.I):  # hanya judul yang memuat WALHI
                continue
            if (i["src"] or "").strip().upper() == "WALHI":
                own += 1; continue
            if t not in seen: seen[t] = i
    return list(seen.values()), own
def tag(t):
    return [k for k, p in ISU.items() if re.search(p, t, re.I)]
if __name__ == "__main__":
    items, own = load("korpus_walhi_raw.json")
    c = collections.Counter(); multi = 0; none = []
    for i in items:
        tg = tag(i["title"]); c.update(tg)
        multi += len(tg) > 1
        if not tg: none.append(i["title"])
    print("judul unik memuat WALHI (tanpa kanal sendiri):", len(items), "kanal sendiri dibuang:", own)
    print(c, "multi:", multi, "tak terklasifikasi:", len(none))
    import random; random.seed(1)
    for t in random.sample(none, min(60, len(none))): print(" -", t)

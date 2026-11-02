import sys, re, email.utils, collections
sys.path.insert(0, ".")
import classify
items, _ = classify.load("korpus_walhi_raw.json")
dem = r"desak|minta|tuntut|tolak|gugat|cabut|hentikan|tagih|lapor|kritik|soroti|tantang|dorong|batalkan|evaluasi|audit|usut"
by = collections.defaultdict(list)
for i in items:
    for k in classify.tag(i["title"]):
        if re.search(dem, i["title"], re.I):
            d = email.utils.parsedate_to_datetime(i["date"]).strftime("%Y-%m-%d")
            by[k].append(f'{d} | {i["title"]}')
for k in classify.ISU:
    L = sorted(by[k])
    with open(f"tuntutan_{re.sub('[^a-z]+','_',k.lower()).strip('_')}.txt", "w") as f:
        f.write("\n".join(L))
    print(k, len(L))

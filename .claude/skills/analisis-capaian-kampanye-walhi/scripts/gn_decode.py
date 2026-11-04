import urllib.request, urllib.parse, re, json, sys
UA = {"User-Agent": "walhi-media-monitor/0.1 (riset pemberitaan; non-komersial)"}
def decode(link):
    gid = link.split("/articles/")[1].split("?")[0]
    html = urllib.request.urlopen(urllib.request.Request(f"https://news.google.com/rss/articles/{gid}", headers=UA), timeout=30).read().decode("utf8", "ignore")
    sg = re.search(r'data-n-a-sg="([^"]+)"', html).group(1); ts = re.search(r'data-n-a-ts="([^"]+)"', html).group(1)
    inner = json.dumps(["garturlreq", [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1, None, None, None, None, None, 0, 1], "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0], gid, int(ts), sg])
    body = "f.req=" + urllib.parse.quote(json.dumps([[["Fbv4je", inner, None, "generic"]]]))
    req = urllib.request.Request("https://news.google.com/_/DotsSplashUi/data/batchexecute", data=body.encode(),
                                 headers={**UA, "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
    r = urllib.request.urlopen(req, timeout=30).read().decode("utf8", "ignore")
    arr = json.loads(r.split("\n\n", 1)[1])
    return json.loads(arr[0][2])[1]
if __name__ == "__main__":
    for line in open(sys.argv[1]).read().splitlines()[:4]:
        t, l = line.split("\t")
        try: print(decode(l), "|", t[:60])
        except Exception as e: print("ERR", e, "|", t[:60])

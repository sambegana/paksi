import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, datetime as dt, time, sys, os
OUT=sys.argv[1]
actors={"WALHI":'walhi',"Greenpeace":'greenpeace',"Pantau Gambut":'"pantau gambut"',"Auriga":'auriga',"Madani":'"madani berkelanjutan"',"BRGM/Akademisi IPB":'"ipb" ',"Kemenhut":'"kementerian kehutanan" OR kemenhut',"KLH":'"kementerian lingkungan hidup" OR KLH',"BNPB":'bnpb'}
start=dt.date(2026,6,1); end=dt.date(2026,11,2)
res={}
for name,q in actors.items():
    d=start
    while d<end:
        e=min(d+dt.timedelta(days=7),end)
        query=f'{q} karhutla after:{d} before:{e}'
        url="https://news.google.com/rss/search?"+urllib.parse.urlencode({"q":query,"hl":"id","gl":"ID","ceid":"ID:id"})
        for attempt in range(3):
            try:
                x=urllib.request.urlopen(url,timeout=30).read(); break
            except Exception as ex:
                time.sleep(3)
        root=ET.fromstring(x)
        items=[{"title":i.findtext("title"),"date":i.findtext("pubDate"),"src":i.findtext("source")} for i in root.iter("item")]
        res.setdefault(name,{})[str(d)]=items
        time.sleep(0.5)
        d=e
    print(name, sum(len(v) for v in res[name].values()), flush=True)
json.dump(res,open(OUT,"w"),ensure_ascii=False)

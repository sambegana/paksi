import re,sys,shutil
D=sys.argv[1]; FIG=sys.argv[2]
P=D+'/word/document.xml'; x=open(P,encoding='utf8').read()
R=[("94 berita dari 64 media (gabungan pemantauan otomatis dan kliping tim PELA), termasuk berita tambang, PSN, dan data center yang berlokasi di laut, pesisir, atau pulau kecil.",
    "45 berita dari 30 media berdasarkan kliping tim PELA, termasuk berita tambang, PSN, dan data center yang berlokasi di laut, pesisir, atau pulau kecil."),
   ("94 berita dari 64 media: gabungan pemantauan otomatis (72 berita) dan kliping tim PELA (22 berita tambahan, kebanyakan media alternatif dan daerah yang tidak terindeks Google News). Angka ini sudah mencakup berita tambang, PSN, dan data center di laut, pesisir, dan pulau kecil.",
    "45 berita dari 30 media, dihitung dari kliping tim PELA (Agustus–Oktober; baris ganda dan berita Juli tidak dihitung). Sebagian besar berasal dari media alternatif dan daerah, dengan isu utama PSN tambak Pantura, Giant Sea Wall, RUU Daerah Kepulauan, dan data center di pulau kecil."),
   ("tercatat 382 berita yang memuat WALHI: Hutan &amp; Kebun 183, Urban 84, Pesisir &amp; Laut 46, Pangan 41, Iklim 19, dan Tambang &amp; Energi 3.",
    "tercatat 336 berita yang memuat WALHI untuk bidang selain Pesisir &amp; Laut: Hutan &amp; Kebun 183, Urban 84, Pangan 41, Iklim 19, dan Tambang &amp; Energi 3. Pemberitaan Pesisir &amp; Laut mengikuti kliping tim PELA di atas.")]
for a,b in R:
    assert x.count(a)==1,a[:40]; x=x.replace(a,b)
# gambar 3: cari rId image3, sesuaikan cy
rels=open(D+'/word/_rels/document.xml.rels').read()
rid=re.search(r'Id="(rId\d+)"[^>]*Target="media/image3.png"',rels) or re.search(r'Target="media/image3.png"[^>]*Id="(rId\d+)"',rels)
rid=rid.group(1)
import struct
w,h=struct.unpack('>II',open(FIG,'rb').read()[16:24])
m=re.search(r'<w:drawing>(?:(?!</w:drawing>).)*?r:embed="%s"(?:(?!</w:drawing>).)*?</w:drawing>'%rid,x,re.S); dr=m.group(0)
cx=int(re.search(r'<wp:extent cx="(\d+)"',dr).group(1)); cy=round(cx*h/w)
dr2=re.sub(r'(<wp:extent cx="\d+" cy=")\d+',r'\g<1>%d'%cy,dr); dr2=re.sub(r'(<a:ext cx="\d+" cy=")\d+',r'\g<1>%d'%cy,dr2)
x=x.replace(dr,dr2); open(P,'w',encoding='utf8').write(x)
shutil.copy(FIG,D+'/word/media/image3.png')
C=D+'/word/comments.xml'; c=open(C,encoding='utf8').read()
a="Angka baru 94 berita dari 64 media adalah gabungan pemantauan otomatis (berita yang menyebut WALHI di judul atau isi, termasuk tambang/PSN/data center di laut, pesisir, dan pulau kecil: 72) dan kliping tim PELA (22 berita tambahan), tanpa duplikat."
b="Angka baru 45 berita dari 30 media dihitung dari kliping tim PELA (Agustus–Oktober; baris ganda dan berita Juli tidak dihitung)."
assert c.count(a)==1; open(C,'w',encoding='utf8').write(c.replace(a,b)); print('ok',rid,cx,cy)

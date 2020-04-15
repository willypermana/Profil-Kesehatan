import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'Indonesian_indonesia.1252')

berkasData = r'D:\path\ke\direktori\bab_04\bab_04_03_dataAnggaran.csv'
judulDiagram = 'Anggaran Kesehatan'
berkasSimpan = r'D:\path\ke\direktori\bab_04\bab_04_03_anggaranKesehatan.pdf'

# read data file
colnames = ['jenisJaminan','jumlahPeserta']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
labelJenis = data.jenisJaminan.tolist()
listJumlah = data.jumlahPeserta.tolist()
sliceJumlah = np.array(data.jumlahPeserta.tolist())
porcent = 100.*sliceJumlah/sliceJumlah.sum()

fig1, ax1 = plt.subplots()
# explodeTuple = (0.05, 0, 0.1, 0.0, 0.1, 0.3)
# patches, texts, autotexts = ax1.pie(listPagu, autopct='%.2f%%', pctdistance=0.85, explode=explodeTuple, startangle=80)
explodeTuple = (0.05, 0, 0.1, 0.0, 0.2, 0.1)
patches, texts, autotexts = ax1.pie(listJumlah[0:6], autopct='%.2f%%', pctdistance=1.15, explode=explodeTuple, startangle=80)

for t in autotexts:
    t.set_size(9)
# for i, a in enumerate(autotexts):
    # a.set_text("Rp {0:n}".format(listPagu[i]))
#autotexts[0].set_color('y')

centre_circle = plt.Circle((0,0),0.65,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

#labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labelJenis, slicePagu)]
labels = ['{0} - Rp {1:n}'.format(i,j) for i,j in zip(labelJenis, sliceJumlah)]

sort_legend = False
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, slicePagu),
                                          key=lambda labelJenis: labelJenis[2],
                                          reverse=True))


box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
plt.legend(patches, labels, loc='center', bbox_to_anchor=(0.5, -0.1),fontsize=8, fancybox=True, shadow=True, ncol=2)
		   
plt.axis('equal')

pyrfig = plt.figure(1)
pyrfig.suptitle(judulDiagram)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
#plt.show()

# Exploded doughnut chart. Visually more pleasing than pie chart, IMO
import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'Indonesian_indonesia.1252')

berkasData = r'D:\path\ke\direktori\data\bab_01_3_dataDistribusiPendidikan.csv'
judulDiagram = 'Tingkat Pendidikan'
berkasSimpan = r'D:\path\ke\direktori\bab_01\bab_01_3_distribusiPendidikan.pdf'

# read data file
colnames = ['tingkatDidik','jumlahDidik']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
labelJenis = data.tingkatDidik.tolist()
listJumlah = data.jumlahDidik.tolist()
sliceJumlah = np.array(data.jumlahDidik.tolist())
porcent = 100.*sliceJumlah/sliceJumlah.sum()

fig1, ax1 = plt.subplots()
explodeTuple = (0.05, 0, 0.1, 0.0, 0.15, -0.05, 0.2,0.05)
patches, texts, autotexts = ax1.pie(listJumlah[0:8], autopct='%.2f%%', pctdistance=1.2, explode=explodeTuple, startangle=80)

for t in autotexts:
    t.set_size(9)
    
centre_circle = plt.Circle((0,0),0.65,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

labels = ['{0}'.format(i,j) for i,j in zip(labelJenis, sliceJumlah[0:8])]

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
#fig.savefig(berkasSimpan, bbox_inches='tight')
#plt.close(pyrfig)
plt.show()

# I'm using horizontal bars as I think it's more space efficient than the vertical one
# It's also seem easier to draw vertical comparison between bars
import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')

berkasData = r'D:\path\ke\direktori\profil_kesehatan\bab_05\bab_05_14_dataKN1KN3.csv'
judulDiagram = 'Kunjungan Neonatal'
sumbuX = 'Cakupan'
sumbuY = 'Puskesmas'
berkasSimpan = r'D:\path\ke\direktori\profil_kesehatan\bab_05\bab_05_14_KN1KN3.pdf'

# read data file
colnames = ['puskesmas','KN1','KN3']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
puskesmas = data.puskesmas.tolist()
bar1 = data.KN1.tolist()
bar2 = data.KN3.tolist()

ind = np.arange(len(puskesmas))  # the x locations for the groups
width = 0.35       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label='KN1')
rects2 = ax.barh(ind + width, bar2, width, color='orangered', label = 'KN3')

# add some text for labels, title and axes ticks
ax.set_title(judulDiagram)
ax.set_xlim(0,110,20)
ax.set_xlabel(sumbuX)
ax.set_ylabel(sumbuY)
formatter = FuncFormatter(lambda x, pos: "{:n}%".format(x))
ax.xaxis.set_major_formatter(formatter)

ax.set_yticks(ind+0.5*width)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in puskesmas ]))
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# add data label
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v+0.5, i+0.3, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
# plt.show()

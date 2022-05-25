# plotting two line diagrams on the same x-axis but different y-axis
# especially useful when you want to superimpose ratio/ percentage against absolute numbers
import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')
## force matplotlib to use TrueType fonts
plt.rcParams['pdf.fonttype'] = 42

# necessary if you want to use relative path but your project isn't in Python $PATH
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

berkasData = currentdir +'\\bab_05_02_dataPlotAKI.csv'
judulDiagram = 'Angka Kematian Ibu'
sumbuY = 'Jumlah'
tickerSumbuY = np.arange(0,510,100)
tickerSumbuY2 = np.arange(0,21,5)
sumbuX = 'Tahun'
berkasSimpan = currentdir +'\\bab_05_02_plotAKI.pdf'

# read data file
colnames = ['tahun','aki', 'kematian']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
tahun = data.tahun.tolist()
aki = data.aki.tolist()
kematian = data.kematian.tolist()
 
# setting up x locations for the groups and width of the bars
ind = np.arange(len(tahun))
# actually just remnant from other bar diagrams, you can safely ignore this
#width = 0.25

# make the plots
fig, ax = plt.subplots()
garis1 = ax.plot(ind, aki, marker='.', color='royalblue', label='AKI')
ax2 = ax.twinx()
garis2 = ax2.plot(ind, kematian, marker='.', color='#cc0000', label='Jumlah Kematian')

# add some text for labels, title and axes ticks
ax.set_title(judulDiagram)
ax.set_yticks(tickerSumbuY) 
# yticks can be set to auto
ax.set_ylabel('AKI per 100.000 kelahiran')
formatter = FuncFormatter(lambda y, pos: "{:n}".format(y))
# use round to get significant decimal
#formatter = FuncFormatter(lambda y, pos: "{:n}".format(round(y,2)))
ax.yaxis.set_major_formatter(formatter)

# set secondary yticks
ax2.set_yticks(tickerSumbuY2) 
ax2.set_ylabel('Jumlah kematian')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

ax.set_xticks(ind)
ax.set_xticklabels(list(tahun), fontsize='small', ha='center')
ax.set_xlabel(sumbuX)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
# legend workaround for 2-vert axis line diagram
kolomLegen = ['AKI','Jumlah Kematian']
ax.legend((garis1[0], garis2[0]), kolomLegen, fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# make labels for plots
for i, txt in enumerate(aki):
		ax.annotate('{:n}'.format(txt), (ind[i],aki[i]+0.5))
for i, txt in enumerate(kematian):
		ax2.annotate(txt, (ind[i],kematian[i]))

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
# uncomment following two lines to save figures
plt.savefig(berkasSimpan)
plt.close(pyrfig)
# uncomment following lines to generate figures on screen
# plt.show()

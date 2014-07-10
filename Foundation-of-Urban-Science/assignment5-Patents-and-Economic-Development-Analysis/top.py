
import pylab
import scipy
import csv
import sys
import scipy
import array
from matplotlib import *
from pylab import *
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


g=open('top10.csv', 'r')
reader=csv.reader(g,delimiter=',')
i=0
cons = []
lass = []
index = []
number = [0 for i in range(0,61)]
newb = []
for x in reader:
    cons.append(x)
for x in range (1, 61):
    lass.append(cons[x][0])
    if cons[x][0] not in index:
        index.append(cons[x][0])
        newb.append(x)
order = [i for i in range(0, len(newb))]

nyx = []
sjx = []
bsx = []
rox = []
cox = []
box = []

nyy = [1 for i in range(0,10)]
sjy = [2 for i in range(0,10)]
bsy = [3 for i in range(0,10)]
roy = [4 for i in range(0,10)]
coy = [5 for i in range(0,10)]
boy = [6 for i in range(0,10)]

for x in range(1,11):
    for y in range (0, len(index)):
        if cons[x][0]==index[y]:
            nyx.append(y)

for x in range(11,21):
    for y in range (0, len(index)):
        if cons[x][0]==index[y]:
            sjx.append(y)

for x in range(21,31):
    for y in range (0, len(index)):
        if cons[x][0]==index[y]:
            bsx.append(y)

for x in range(31,41):
    for y in range (0, len(index)):
        if cons[x][0]==index[y]:
            rox.append(y)

for x in range(41,51):
    for y in range (0, len(index)):
        if cons[x][0]==index[y]:
            cox.append(y)

for x in range(51,61):
    for y in range (0, len(index)):
        if cons[x][0]==index[y]:
            box.append(y)
ax = plt.subplot(1,1,1)
plt.plot(box,boy, marker='o', linestyle = '' )
plt.plot(cox,coy, marker='o', linestyle = '' )
plt.plot(rox,roy, marker='o', linestyle = '' )
plt.plot(bsx,bsy, marker='o', linestyle = '' )
plt.plot(sjx,sjy, marker='o', linestyle = '' )
plt.plot(nyx,nyy, marker='o', linestyle = '' )
ll = ['New York','San Jose','Burlington','Rochester','Corvallis','Boulder']
plt.yticks(range(1,7),ll)


plt.xticks(range(0,32),index)
plt.ylim((0.5,6.5))
plt.xlim((-2,34))
ax.tick_params(axis='x', direction='out', labelsize=6)
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.grid(True,'minor')
plt.title('Top 10 patent of six MSAs')
plt.show()

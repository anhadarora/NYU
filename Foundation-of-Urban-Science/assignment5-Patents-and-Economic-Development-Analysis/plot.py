
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



params = {'axes.labelsize': 14,
          'text.fontsize': 20,
          'legend.fontsize': 20,
          'xtick.labelsize': 14,
          'ytick.labelsize': 14,
          'text.usetex': True}

pylab.rcParams.update(params)



gcon = []
g=open('plot.csv', 'r')
reader=csv.reader(g,delimiter=',')
i=0
patents = []
for x in reader:
    patents.append(x)
patent = []
pop= []
poplog = []
patentlog =[]

for x in patents:
    patent.append(float(x[1]))
    pop.append(float(x[2]))

poplog = log10(pop)
patentlog = log10(patent)

#xy = [0, 0.5, 1]
plot(poplog,patentlog,color='green',marker='o',ls='None', alpha=0.5 )

#p = np.poly1d(np.polyfit(poplog,patentlog,5))
#plot(xy, p(xy), color = 'r')
   
wgradient, wintercept, wr_value, wp_value, std_err = stats.linregress(poplog,patentlog)


#print "Gradient and intercept, wages", wgradient, wintercept
#print "R-squared", wr_value**2
#print "p-value", wp_value

tt=poplog
tt.sort()
fitxx=arange(float(tt[0])-0.5,float(tt[-1])+0.5,0.1,dtype=float)
fityy=wintercept + fitxx*wgradient
str=r'$\beta='+repr(round(wgradient,3))+'$, intercep $='+repr(round(wintercept,3))+'$, $r^2='+repr(round(wr_value**2,2))+'$'
plot(fitxx,fityy,'r-', linewidth=3, alpha=0.5,label=str)
#m = str(float(wintercept))
#n = str(float(wgradient))

plt.ylabel('Log10 patent intensity, 2001-2005')
plt.xlabel('Log10 GDP per capita, 2008-2012'+'  '+'y='+repr(round(wintercept,3))+'+'+repr(round(wgradient,3))+'*x'+ ' '+ 'R^2='+repr(round(wr_value**2,2)) )
plt.title('LN GDP per capita VS LN patent intensity')
#plt.subplots_adjust(left =0.2)
plt.axis([4.0,5.2,-0.5,3.0])
plt.show()

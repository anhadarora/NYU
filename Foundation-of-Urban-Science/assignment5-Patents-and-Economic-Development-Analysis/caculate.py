
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


gcon = []
g=open('intensity.csv', 'r')
reader=csv.reader(g,delimiter=',')
i=0
patents = []
for x in reader:
    patents.append(x)
avg = []
for x in range(0, 362):
    i =(float( patents[x][49])/float(patents[x][36])*100000 +float( patents[x][50])/float(patents[x][37])*100000 +float( patents[x][51])/float(patents[x][38])*100000+float( patents[x][52])/float(patents[x][39])*100000+ float( patents[x][53])/float(patents[x][40])*100000)/5
    avg.append(i)

ff = open('patentin.csv','w')
for x in range(0, 362):
    ff.write(patents[x][1]+','+patents[x][2]+','+patents[x][44]+','+patents[x][45]+','+patents[x][46]+','+patents[x][47]+',')
    ff.write(str(avg[x])+'\n')



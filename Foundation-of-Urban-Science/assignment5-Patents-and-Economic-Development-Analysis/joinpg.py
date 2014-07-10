
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
g=open('patentin.csv', 'r')
reader=csv.reader(g,delimiter=',')
i=0
patents = []
for x in reader:
    patents.append(x)


ggcon = []
gg=open('GDPpercapp.csv', 'r')
readerg=csv.reader(gg,delimiter=',')
i=0
gdp = []
for x in readerg:
    gdp.append(x)


ff = open('plot.csv','w')
for x in range(0, len(patents)):
    for y in range(0, len(gdp)):
        if patents[x][0]== gdp[y][0]:
            ff.write(patents[x][0]+','+patents[x][6]+','+gdp[y][14]+'\n')


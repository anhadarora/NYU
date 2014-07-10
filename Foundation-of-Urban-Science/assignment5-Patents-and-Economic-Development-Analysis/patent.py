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


gcon = []
g=open('patents.csv', 'r')
reader=csv.reader(g,delimiter=',')

gg = open('pop_all.csv', 'r')
readerg = csv.reader(gg, delimiter= ',')

xxx = open('intensity.csv','w')
i=0
patents = []
for x in reader:
    patents.append(x)
for x in readerg:
    for y in range (0, 951):
        if patents[y][1] in x[2]:
            if patents[y][2]=='Metropolitan Statistical Area':
                for n in range(0, 43):
                    xxx.write(str(x[n])+',')
                for m in range(0, 16):
                    xxx.write(patents[y][m]+',')
                xxx.write('\n')

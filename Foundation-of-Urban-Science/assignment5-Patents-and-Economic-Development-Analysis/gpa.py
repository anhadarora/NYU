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

g=open('GDPpercap.csv', 'r')
gcon = []
i = 0
for x in g:
    if i == 0:
        i+=1
        continue
    gcon.append(x.split(','))
gg = open('GDPpercapp.csv','w')
for x in range(0, 381):
    b =float( (float(gcon[x][10])+float(gcon[x][11])+float(gcon[x][12])+float(gcon[x][13])+float(gcon[x][14]))/5)
    print gcon[x][10]
    gcon[x][14] = gcon[x][14].strip()
    for n in gcon[x]:
        gg.write(str(n)+',')
    gg.write(str(b))
    gg.write('\n')





 #   for y in range(0, 23):
  #      m = gcon[x][y].strip('"')
   #     m = m.strip('\n')
    #    m = m.strip('"')
    #    outputFile.write(m +',')
   # outputFile.write('Bronx'+','+'\n')
#print m

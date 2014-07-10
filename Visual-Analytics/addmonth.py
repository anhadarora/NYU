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

g=open('done.csv', 'r')
gcon = g.readlines()
con = []
for x in gcon:
    con.append(x.split(','))
count = [0 for i in range (0, 18)]
outputFile = open('newdone.csv','w')
i = 0
j = 1
for x in range (2, len(con)):
    if i < 7:
        for y in range(0, 18):
            print con[x][0]
            count[y] += float(con[x][1+y])
        i += 1
    if i == 7:
        for y in range(0, 18):
            print count[y]
            count[y]= count[y]/7 
            print count[y]
            outputFile.write(str(count[y])+',')
        outputFile.write('Bronx'+','+str(j)+','+'\n')
        count = [0 for i in range (0, 18)]
        i = 0
        j += 1
    






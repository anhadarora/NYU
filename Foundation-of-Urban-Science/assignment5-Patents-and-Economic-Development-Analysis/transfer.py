
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
import pylab

class Patentclass:
    name = None
    number = None

    def __init__(self, name):
        self.name = name
        self.number = []
        
    def addnumber(self, zip):
        self.number.append(zip)

g=open('new.csv', 'r')
reader=csv.reader(g,delimiter=',')
i=0
cons = []
count = [0 for i in range(0, 376)]
for x in reader:
    cons.append(x)
for x in range(2, 401):
    for y in range(2, 376):
        if int(cons[x][y]) ==0:
            cons[x][y]='N'
        else:
            cons[x][y]='Y'
            count[y]+=1

hhh = open('heatmap.csv','w')
for x in range(0,401):
    for y in range(0, 376):
        mmm = cons[x][y].replace(","," ")
        hhh.write(mmm+',')
    hhh.write('\n')

for x in range(0, 376):
    hhh.write(str(count[x])+',')

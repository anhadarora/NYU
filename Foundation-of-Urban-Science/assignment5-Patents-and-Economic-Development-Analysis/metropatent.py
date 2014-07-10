
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
i=0
patents = []
for x in reader:
    patents.append(x)
patent = []
pop= []

ff = open('metropatent.csv','w')
for x in range(0, 951):
    if patents[x][2]=='Metropolitan Statistical Area':
        for y in range(0,15 ):
            ff.write(patents[x][y]+',')
        ff.write('\n')

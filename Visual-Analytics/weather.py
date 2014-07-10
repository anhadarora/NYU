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

g=open('Bronxweather.csv', 'r')
gcon = []
for x in g:
    gcon.append(x.split(','))
print gcon[0]
outputFile = open('bronweather.csv','w')
for x in range(0, 367):
    for y in range(0, 23):
        m = gcon[x][y].strip('"')
        m = m.strip('\n')
        m = m.strip('"')
        outputFile.write(m +',')
    outputFile.write('Bronx'+','+'\n')
print m

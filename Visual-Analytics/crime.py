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
g=open('nyct.csv', 'r')
reader=csv.reader(g,delimiter=',')

gg = open('Policebor.csv', 'r')
readerg = csv.reader(gg, delimiter= ',')

m = []
bro = []
bron = []
qu = []
st = []

for x in readerg:
    if x[0]=='Manhattan':
        m.append(x[1])
    if x[0]=='Bronx':
        bron.append(x[1])
    if x[0]=='Brooklyn':
        bro.append(x[1])
    if x[0]=='Queens':
        qu.append(x[1])
    if x[0]=='Staten':
        st.append(x[1])
    
        


outputFile = open('newone.csv','w')

for x in reader:
    a = x[0][20:]
    for i in range(0 , len(x)):
        outputFile.write(x[i] +',')
    outputFile.write('2012'+','+a+',')
    if x[16] in m:
        outputFile.write('Manhattan'+',')
    if x[16] in bro:
        outputFile.write('Brooklyn'+',')
    if x[16] in bron:
        outputFile.write('Bronx'+',')
    if x[16] in qu:
        outputFile.write('Queens'+',')
    if x[16] in st:
        outputFile.write('Staten'+',')
    outputFile.write('\n')

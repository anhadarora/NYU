
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

class Patentclass:
    name = None
    number = None

    def __init__(self, name):
        self.name = name
        self.number = []
        
    def addnumber(self, zip):
        self.number.append(zip)

patentclas = {}
newpatent = {}
gcon = []
x = 100000
y = '.csv'
z = str(x)+str(y)
g=open(z, 'r')
reader=csv.reader(g,delimiter=',')
i=0
patents = []
for x in reader:
    patents.append(x)
patentnum = []
for x in range(1, 400):
    patentnum.append(patents[x][0])
nnn = []
for x in patentnum:
    patentclas[x] = Patentclass(x)
    newpatent[x]= Patentclass(x)
    newpatent[x].addnumber(0)
m =  len(newpatent.keys())
gg = open('metropatent.csv','r')
readerg = csv.reader(gg,delimiter=',')
area = []
for x in readerg:
    area.append(x[0]+'.csv')
    nnn.append(x[0])
total = []
con = []
numb = []


for n in range(48, 100):
    ggg = open(area[n],'r')
    readergg = csv.reader(ggg, delimiter=',')
    for x in readergg:
        con.append(x)
    for x in range(1, len(con)):
        numb.append(con[x][0])
        total.append(int(con[x][14])-int(con[x][2]))
    for x in range(0, len(numb)):
        if numb[x] in newpatent.keys():
            newpatent[numb[x]].number[0]= total[x]
    for x in patentnum:
        patentclas[x].addnumber(newpatent[x].number[0])
    con = []
    ggg.close()

ff = open('one2.csv','w')
ff.write('Class'+',')
for x in range(48, 100):
    ff.write(nnn[x] +',')
ff.write('\n')
for x in patentclas.keys():
    ff.write(x+',')
    for y in range(0, 52):
        ff.write(str(patentclas[x].number[y])+',')
    ff.write('\n')
    

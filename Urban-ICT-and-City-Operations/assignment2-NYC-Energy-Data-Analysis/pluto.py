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
import re

conn= []
before = open('join11.csv','r')
beforecon = before.readlines()
for x in beforecon:
    a=x.strip('\n')
    conn.append(a.split(','))

outputFile = open('bxpluto.csv','w')

p = re.compile('\s+')
m = []
n = []
q = []

for x in conn:
    a = re.sub(p,'',x[1])
    b = re.sub(p,'',x[2])
    c = a+b
    m.append(c)

after = open('bx13v1.csv','r')
aftercon = after.readlines()
for x in aftercon:
    a = x.strip('\n')
    q.append(a.split(','))

for x in q:
    a = re.sub(p,'',x[11])
    n.append(a)


for i in range(0, 90004):
    for j in range(0,823):
        if n[i] == m[j]:
            for e in range(0, 31):
                outputFile.write(conn[j][e]+',')
            for f in range(0, 82):
                outputFile.write(q[i][f]+',')
            outputFile.write('\n')
            







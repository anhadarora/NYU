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
g=open('newone.csv', 'r')
reader=csv.reader(g,delimiter=',')

gg = open('bronxweatheravg.csv', 'r')
readerg = csv.reader(gg, delimiter= ',')

weather = []

outputFile = open('Bronx.csv','w')
i = 0
for x in readerg:
    weather.append(x)
for x in reader:
    for y in range (0,52):
        if x[18] == weather[y][19]:
            if x[19] == weather[y][18]:
                for m in range (0,20):
                    outputFile.write(x[m] +',')   
                for n in range (0,20):
                    outputFile.write(weather[y][n])  
                    outputFile.write(',')
                outputFile.write('\n')  

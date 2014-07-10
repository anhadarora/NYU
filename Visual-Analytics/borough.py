import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny
from pylab import *
import csv
from sklearn import cross_validation, linear_model, datasets
from random import shuffle
from scipy import stats
import csv
import sys
import time
import datetime as dt
from matplotlib.dates import date2num
import matplotlib.dates as date
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

actions = open('final.csv','r')
actioncon = csv.reader(actions, delimiter = ',')
final = []
i = 0
j = 0

for x in actioncon:
    if i == 0 :
        i += 1
        final.append(x)
        continue
    for y in final:
        if x[22]==y[22]:
            # and x [19]==y[19] and x[21]== y[21] and x[23]= = y[23] and x [25]== y[25]:
            y[4] = int(y[4])+int(x[4])
            y[5] = int(y[5])+int(x[5])
            y[6] = int(y[6])+int(x[6])
            y[7] = int(y[7])+int(x[7])
            y[8] = int(y[8])+int(x[8])
            y[9] = int(y[9])+int(x[9])
            y[10]= int(y[10])+int(x[10])
            y[11] = int(y[11])+int(x[11])
        else:
            final.append(x)
            print i
            i+=1

ddd = open('citywide.csv','w')
for x in final:
    for i in range(0, len(x)):
        ddd.write(str(x[i])+',')
    ddd.write('\n')

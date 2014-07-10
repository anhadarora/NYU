import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny
from pylab import *
import csv
from sklearn import cross_validation, linear_model, datasets
from random import shuffle

action = []
actions = open('labeled_data.csv','r')
for x in actions:
    action.append(x)
del action[0]

# parse the data
action2 = []
for x in action:
    action2.append(x.split(','))

population = []
incidents = []

for x in action2:
    population.append(float(x[1]))
    incidents.append(float(x[2]))
population1 = np.array(population, np.float)
incidents1 = np.array(incidents, np.float)

# practice 10-fold cross validation
km = cross_validation.KFold(len(incidents), n_folds = 10, shuffle = True) # every time the outcome would be different
rmse = []
r2 = []
rmsestd = []

for x in range(1, 6):
    rmseord = []
    r2ord = []
    for y, z in km:
        poly1 = np.polyfit(population1[y] ,incidents1[y] ,x )
        polyval = np.polyval(poly1, population1[z])
        rm = (((polyval - incidents1[z])**2).mean(axis = None))**.5
        rmseord.append(rm)
        testavg = sum(incidents1[z])/len(incidents1)
        avg = []
        for i in range(0, len(incidents1[z])):
            avg.append(testavg)
        residential = sum((polyval - incidents1[z])**2)
        total = sum((incidents1[z] - avg)**2)
        r2ord.append(1-(residential/total))
    rmse.append(sum(rmseord)/len(rmseord))
    r2.append(sum(r2ord)/len(r2ord))
print rmse, r2

# Mainly learned from Ravi's code. Thx.

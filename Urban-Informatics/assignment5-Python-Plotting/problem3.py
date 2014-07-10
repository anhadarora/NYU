# Gang Zhao, Assignment 5, Problem3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny

# read the file and deal with the data 
action = []
actions = open('microprocessors.dat','r')
for x in actions:
    action.append(x)
del action[0]

# parse the data
action2 = []
for x in action:
    action2.append(x.split(','))
prolist = []
yearlist = []
translist = []
for x in action2:
    prolist.append(x[0])
    yearlist.append(x[1])
    translist.append(ny.log10(float(x[2].strip())))
yearlist = sorted(yearlist)

for x in range(0, len(yearlist)):
    for y in action2:
        if yearlist[x] == y[1]:
            prolist[x] = y[0]
            translist[x] = ny.log10(float((y[2])))
count = [i for i in range(0,len(yearlist))]
count1 = [' ' for i in range(0,len(yearlist))]

# plot the figure 1
chart = plt.figure()
chart.patch.set_facecolor('white')
ax1 = plt.subplot(1, 2, 1)
ax1.plot( yearlist, count, 'bo', color = 'k')
ax1.set_xlabel('Year of Introduction')
plt.yticks(range(len(prolist)), prolist)
ax1.yaxis.grid()
ax1.tick_params(axis='both', direction='out', labelsize=8)
ax1.axis([1965, 2010, -1, 13])

#plot the figure 2
ax2 = plt.subplot(1, 2, 2)
ax2.plot(translist, count, 'bo', color = 'k')
ax2.set_xlabel('Number of Transistors (log 10)')
plt.yticks(range(len(count1)), count1)
ax2.tick_params(axis='both', direction='out', labelsize=8)
ax2.yaxis.grid()
ax2.axis([2.5, 9.5, -1, 13])
plt.subplots_adjust(left =0.2)
chart.suptitle('Microprocessors')
plt.savefig("Problem 3.png")

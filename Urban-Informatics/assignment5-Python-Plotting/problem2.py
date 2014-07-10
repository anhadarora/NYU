# Gang Zhao, Assignment 5, Problem2

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as date
from matplotlib.dates import date2num, MonthLocator, DateFormatter

# read the file and deal with the data 
action = []
actions = open('actions-fall-2007.dat','r')
for x in actions:
    action.append(x)
del action[0]

# change the calendar time to days
daytime = []
for x in action:
    a = dt.datetime.strptime(x.strip(),'%Y-%m-%d %H:%M:%S')
    b = date.date2num(a)
    daytime.append(b)
# Find the number of bins
a = max(daytime)-min(daytime)
binnum = int(a)+1

# plot histogram
begin = date.date2num(dt.datetime.strptime('2007-09-10 12:00:00','%Y-%m-%d %H:%M:%S'))
final = date.date2num(dt.datetime.strptime('2007-12-18 12:00:00','%Y-%m-%d %H:%M:%S'))
plt.hist(daytime, bins = binnum, color = 'g', range = (begin ,final ))
plt.gca().xaxis.set_major_locator(MonthLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter('%B'))
plt.ylabel('Number of Actions')
plt.title('24-hour count of student actions in 2007Fall Scientific Visualization Course')

# plot due date
deadlines = ['2007-09-18 12:00:00', '2007-10-04 12:00:00', '2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-11 12:00:00','2007-12-15 12:00:00']
deadtime = []
for x in deadlines:
    deadtime.append(dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
labels = ['Assin0 and 1 due', 'Assin2 due', 'Assin3 due', 'Assin4 due', 'Assin6 due', 'Assin5 due']
for i in range(0, 6):
    plt.text(deadtime[i],10000 + 1000*i,labels[i],rotation=0, size='small')
plt.vlines(date2num(deadtime), 0, 16000, color = 'k',linestyle = 'dashed' )
plt.savefig("Problem 2.png")

# I choose every 24 hours between 12:00 to 12:00 as my bins, since the deadline is 12:00 for each assignment.
# More activities in assignment 3,4,5 and 6, which might means that more works with these assignments.
# For assignment 0,1,4,5 and 6, students trend to finished before the deadline, but for assignment 2 and 3, more students finished after the deadline.

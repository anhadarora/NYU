# Gang Zhao, Assignment 5, Problem1a 

import pandas as pd
import matplotlib.pyplot as plt

# read the file and set index used
stockcon = pd.read_csv('stocks.dat')
conindex = stockcon[['month','apple']]
xindex = conindex.set_index('month')
xindex = xindex.sort()

#plot the figure
plot = xindex.plot(legend = True, style = "o-", title = 'Apple Price Jan 06 - Sep 08')
plot.set_ylabel('U.S. Dollars')
plot.set_xlabel('Month')
plt.savefig("Problem 1a.png")

# Ways to make a clear plot: every point has a bigger dot, red line, few lables.

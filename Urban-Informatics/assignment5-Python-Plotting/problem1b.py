# Gang Zhao, Assignment 5, Problem1b

import pandas as pd
import matplotlib.pyplot as plt

# read the file and set index used
stockcon = pd.read_csv('stocks.dat')
conindex = stockcon[['month','apple','microsoft']]
xindex = conindex.set_index('month')
xindex = xindex.sort()

#plot the figure
plot = xindex.plot(legend = True, style = "o-", title = 'Apple and Microsoft Price Jan 06 - Sep 08')
plot.set_ylabel('U.S. Dollars')
plot.set_xlabel('Month')
plt.savefig("Problem 1b.png")

#The prices of these two companies fellow the same trend, although the prices are so different.

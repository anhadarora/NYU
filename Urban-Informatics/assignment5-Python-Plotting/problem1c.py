# Gang Zhao, Assignment 5, Problem1c

import pandas as pd
import matplotlib.pyplot as plt

# read the file and set index used
stockcon = pd.read_csv('stocks.dat')
conindex = stockcon[['month','apple','microsoft']]
xindex = conindex.set_index('month')
xindex = xindex.sort()

#plot the figure
plot = xindex.plot(subplots = True, legend = True, sharex = True, style = "o-", title = 'Apple and Microsoft Price Jan 06 - Sep 08')
plot[0].set_ylabel('U.S. Dollars')
plot[1].set_ylabel('U.S. Dollars')
plt.savefig("Problem 1c.png")

# I choose to use superposition, because the companies's price go through a same timeline. But if the prices are not having that big difference, it would be hard to use.

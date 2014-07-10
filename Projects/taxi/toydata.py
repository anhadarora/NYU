%pylab inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import exp, sqrt
import csv
import sys
import time
import datetime as dt
from matplotlib.dates import date2num
import matplotlib.dates as date
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import cKDTree
import pandas as pd
from scipy import linalg as LA
from scipy.cluster.vq import vq, kmeans2, whiten
#import Pycluster
#import dbflib
#from shapelib import ShapeFile
#import dbflib
from  scipy.linalg import sqrtm, inv
from sklearn.preprocessing import normalize
from sklearn import datasets
from sklearn.metrics import *
from matplotlib.collections import LineCollection
from matplotlib import cm
from sklearn import cluster
from scipy.stats import ttest_ind
from scipy.linalg import eigh, eig
from scipy.sparse.linalg import eigsh



#cluster1 =2+ np.random.randn(50)*0.2
#cluster2 =4+ np.random.randn(50)*0.2
#cluster3 =6+ np.random.randn(50)*0.2
#cluster4 =8+ np.random.randn(50)*0.2
#cluster = np.insert(cluster1, np.array(len(cluster2)), cluster2)
#scluster = np.insert(cluster3, np.array(len(cluster4)), cluster4)
#fcluster = np.insert(cluster, np.array(len(scluster)), scluster)
#np.save('toydata',fcluster)
#plt.hist(fcluster, bins =160 )
#plt.show()
#matrix = np.zeros((200, 200))
#zipcodes = np.arange(200)+1
#tframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
data = np.load('toydata.npy')

#plt.hist(data, bins =100 )
#plt.title('Toydata')
#plt.show()
#for x in range(0, len(data)-1):
 #   for y in range(x+1, len(data)):
  #      tframe.ix[x+1,y+1] = exp(-(data[x]-data[y])**2/2)
#tframe = tframe + tframe.T
#np.save('toyframedata',tframe)
tframe = np.load('toyframedata.npy')
#tframe = np.load('boxtripmatrix.npy')
#print tframe[:,0]

#tframe = tframe/tframe.max().max()


k = 4
trip1matrix = tframe.copy()
tripmatrix = tframe.copy()
weight = tripmatrix.sum(axis = 1)
a = int(len(weight))
#dmatrix = np.zeros((a ,a))
#np.fill_diagonal(dmatrix, weight)
ddmatrix = np.zeros((a ,a))
ght = [0 for i in range(0, a)]
np.fill_diagonal(trip1matrix, ght )
wweight = trip1matrix.sum(axis = 1)
np.fill_diagonal(ddmatrix, wweight)

hdmatrix = sqrtm(ddmatrix)
hdmatrix = inv(hdmatrix)
ulmatrix = np.dot(hdmatrix, trip1matrix)
ulmatrix = np.dot(ulmatrix, hdmatrix)
le_vals, le_vecs = eigsh(ulmatrix, 10 , which = 'LM', tol= 1E-2)
lwrit = le_vecs[:, -4:]
lwrit = normalize(lwrit, norm='l1', axis=1)
lcenter , llabel = kmeans2(lwrit, k, iter = 100, minit ='random' )
# print llabel

lmatrix = ddmatrix - trip1matrix


#print lmatrix[:,0]
#lmatrix -= np.mean(lmatrix, axis=0)
#lmatrix = np.corrcoef(lmatrix,rowvar= 0 )
e_vals, e_vecs = eigh(lmatrix)
writ = e_vecs[:, :4]
center , label = kmeans2(writ, k, iter = 100, minit ='random')


symmatrix = np.dot(hdmatrix, lmatrix)
syme_vals, syme_vecs = eigh(symmatrix)
symwrit = syme_vecs[:, :4]
symcenter , symlabel = kmeans2(symwrit, k, iter = 100, minit ='random')


rmmatrix = np.dot(inv(ddmatrix), lmatrix)
rme_vals, rme_vecs = eigh(rmmatrix)
rmwrit = rme_vecs[:, :4]
rmcenter, rmlabel = kmeans2(rmwrit, k, iter = 100, minit ='random')

#gg = np.array([[1.5, -0.8, -0.6, 0, -0.1, 0],[-0.8, 1.6, -0.8, 0,0,0],[-0.6, -0.8, 1.6, -0.2, 0, 0 ],[-0.8, 0, -0.2, 2.5, -0.8, -0.7],[-0.1, 0, 0, 0.8, 1.7, -0.8],[0, 0, 0, -0.7,-0.8,1.5 ]])

#kk, jj = eigh(gg)

#gg -= np.mean(gg, axis=0)
#gg = np.corrcoef(gg,rowvar= 0 )
#e_vals, e_vecs = LA.eig(gg)


#    la, er, nfoun = Pycluster.kcluster(writ , 3)
spectral = cluster.SpectralClustering(n_clusters = 4, eigen_solver = 'arpack', affinity = 'precomputed')
spectral.fit(tripmatrix)
spectralpredict = spectral.fit_predict(tripmatrix)

 #   print spectralpredict
#print llabel
#print label
#print spectralpredict
#print le_vals
nn = list(np.arange(len(tframe)))
n1 = list(np.arange(10))
yy =  le_vals[:10]
v1 =  list(le_vecs[:,-4])
fig, ax = plt.subplots()

ax.plot(data, v1 , 'ro')
plt.title('Unnormalized Laplacian Eigenvalues')
#ax.set_ylim(-0.4,0.4)
plt.show()


print llabel
print label
print spectralpredict
print rmlabel
print symlabel


#np.save('tripnorlabel', llabel)
#np.save('tripunorlabel', label)
#np.save('tripspeclabel', spectralpredict)
#np.save('rmlabel', rmlabel)
#np.save('symlabel', symlabel)

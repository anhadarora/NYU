import numpy as np
import sys
import pandas as pd
from math import sqrt
import networkx as nx

def getmatrix(data):
    pickupzip = data[:, 18]
    dropoffzip = data[:, 19]
    tip = data[:, 12]
    fare = data[:, 9]
    dis = data[:, 8]
    num = data[:, 15]
    tip = map(int, tip)
    fare = map(int , fare)
    dis = map(int , dis)
    num = map(int , num)
    zipcodes = sorted(list(set(pickupzip).union(set(dropoffzip))))
    np.save('zips', zipcodes)

    matrix = np.zeros((len(zipcodes), len(zipcodes)))
    tripframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    tipframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    disframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    numframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    fareframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    tripinframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    tipinframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    disinframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    numinframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    fareinframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    for x in range (0, len(data)):
        tripframe.ix[[pickupzip[x]],[dropoffzip[x]]] += 1
    for x in range (0, len(data)):
        tripinframe.ix[[dropoffzip[x]],[pickupzip[x]]] += 1      
    for x in range (0, len(data)):
        tipframe.ix[[pickupzip[x]],[dropoffzip[x]]] += tip[x]
    for x in range (0, len(data)):
        tipinframe.ix[[dropoffzip[x]],[pickupzip[x]]] += tip[x]   
    for x in range (0, len(data)):
        disframe.ix[[pickupzip[x]],[dropoffzip[x]]] += dis[x]
    for x in range (0, len(data)):
        disinframe.ix[[dropoffzip[x]],[pickupzip[x]]] += dis[x]   
    for x in range (0, len(data)):
        numframe.ix[[pickupzip[x]],[dropoffzip[x]]] += num[x]
    for x in range (0, len(data)):
        numinframe.ix[[dropoffzip[x]],[pickupzip[x]]] += num[x]   
    for x in range (0, len(data)):
        fareframe.ix[[pickupzip[x]],[dropoffzip[x]]] += fare[x]
    for x in range (0, len(data)):
        fareinframe.ix[[dropoffzip[x]],[pickupzip[x]]] += fare[x]   
    
    np.save('tripframe', tripframe)     
    np.save('tipframe', tipframe)
    np.save('disframe', disframe)
    np.save('numframe', numframe)
    np.save('fareframe', fareframe)
    np.save('tripinframe', tripinframe)     
    np.save('tipinframe', tipinframe)
    np.save('disinframe', disinframe)
    np.save('numinframe', numinframe)
    np.save('fareinframe', fareinframe)
         
def lastmatrix():

    tripframe = np.load('tripframe.npy')
    tipframe = np.load('tipframe.npy')   
    disframe = np.load('disframe.npy')
    numframe = np.load('numframe.npy')
    fareframe = np.load('fareframe.npy')
    tripinframe = np.load('tripinframe.npy')
    tipinframe = np.load('tipinframe.npy')   
    disinframe = np.load('disinframe.npy')
    numinframe = np.load('numinframe.npy')
    fareinframe = np.load('fareinframe.npy')
    zipcodes = np.load('zips.npy')
        
    tripsum = tripframe.sum(axis = 1)  
    tipsum = tipframe.sum(axis = 1)
    dissum = disframe.sum(axis = 1)
    numsum = numframe.sum(axis = 1)     
    faresum = fareframe.sum(axis = 1)  
            
    tripinsum = tripinframe.sum(axis = 1)  
    tipinsum = tipinframe.sum(axis = 1)
    disinsum = disinframe.sum(axis = 1)
    numinsum = numinframe.sum(axis = 1)     
    fareinsum = fareinframe.sum(axis = 1) 
    
    tripsum = np.array(tripsum)
    tipsum = np.array(tipsum)
    dissum = np.array(dissum)
    numsum = np.array(numsum)
    faresum = np.array(faresum)
    tripinsum = np.array(tripinsum)
    tipinsum = np.array(tipinsum)
    disinsum = np.array(disinsum)
    numinsum = np.array(numinsum)
    fareinsum = np.array(fareinsum)
    
    tripsum = (tripsum - float(tripsum.sum())/len(tripsum))/float(np.std(tripsum))
    tipsum = (tipsum - float(tipsum.sum())/len(tipsum))/float(np.std(tipsum))
    dissum = (dissum - float(dissum.sum())/len(dissum))/float(np.std(dissum))
    numsum = (numsum - float(numsum.sum())/len(numsum))/float(np.std(numsum))
    faresum = (faresum - float(faresum.sum())/len(faresum))/float(np.std(faresum))
    tripinsum = (tripinsum - float(tripinsum.sum())/len(tripinsum))/float(np.std(tripinsum))
    tipinsum = (tipinsum - float(tipinsum.sum())/len(tipinsum))/float(np.std(tipinsum))
    disinsum = (disinsum - float(disinsum.sum())/len(disinsum))/float(np.std(disinsum))
    numinsum = (numinsum - float(numinsum.sum())/len(numinsum))/float(np.std(numinsum))
    fareinsum = (fareinsum - float(fareinsum.sum())/len(fareinsum))/float(np.std(fareinsum))
    
    total = zip(tripsum, tipsum, dissum, numsum, faresum, tripinsum, tipinsum, disinsum, numinsum, fareinsum)
    matrix = np.zeros((len(zipcodes), len(zipcodes)))
    lastframe = pd.DataFrame(matrix, index = zipcodes, columns = zipcodes).copy()
    for x in range (0, len(zipcodes)):
        for y in range(0, len(zipcodes)):
            lastframe.ix[[zipcodes[x]],[zipcodes[y]]] = float(np.dot(total[x], total[y]))/(sqrt((np.dot(total[x], total[x])))*(sqrt(np.dot(total[y], total[y]))))
    np.save('lastframe', lastframe)

        
        
if __name__ == '__main__':
    
    data =np.load('newboxdata.npy')
    getmatrix(data)
    lastmatrix()
    data = np.load('lastframe.npy')
    print data[2]
    
    #%pylab inline

    data = np.load('tripframe.npy')
#print data[140]
    ga = np.array(data).copy()
    G = nx.from_numpy_matrix(ga)
    pos = nx.spring_layout(G, k = 3, iterations = 100)
    nx.draw(G, pos, node_color='#A0CBE2',edge_color='#BB0000',width=1,edge_cmap=plt.cm.Blues,with_labels=True)
#plt.savefig("graph.png", dpi=1000)

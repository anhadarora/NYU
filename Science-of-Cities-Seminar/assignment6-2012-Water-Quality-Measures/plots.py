%pylab inline
import pandas as pd
import csv 
import matplotlib.pyplot as plt
import numpy as np
import collections
from itertools import groupby

stocks = pd.read_table('MG+harbor_sampling_ytd_2012.csv', sep=',')
stocks = stocks.applymap(lambda x: np.nan if isinstance(x, basestring) and x.isspace() else x)
stocks.to_csv('output.csv', index = False)


df = pd.read_table('output.csv', sep=',')
df1 = df[pd.notnull(df['FCTop'])]
print len(df1)
df2 = df[pd.notnull(df['DOTop'])]
print len(df2)
df3 = df[pd.notnull(df['ETop'])]
print len(df3)
df2.to_csv('newoutput.csv', index = False)



stocks = pd.read_table('newoutput.csv', sep=',')
sites = pd.read_table('MG+harbor_sampling_coordinates.csv', sep=',')
location = stocks['Site']
uloc = sites['SITE']
mm = sorted(list(location))
d = {x:mm.count(x) for x in mm}
num = [len(list(group)) for key, group in groupby(mm)]
print sum(num)
print sorted(d.keys())
label = sorted(d.keys())
ax = plt.subplot(1, 1, 1)
ax.plot(np.arange(0,71), num, 'ko')
plt.xticks(range(len(label)), label)
ax.tick_params(axis='both', direction='out', labelsize=3)
ax.set_xlim(-1, 73)
plt.title('Number of samplings at each point')
plt.savefig('x.png', dpi=300)

for x in d.keys():
    if x not in list(uloc):
        print x, d[x]
    if d[x]==48:
        print x


def f(x):
    if pd.notnull(x[2]) and pd.notnull(x[3]):
        return float(float(x[2])+float(x[3]))/2
    if pd.notnull(x[2]) and pd.notnull(x[3])== False:
        return float(x[2])
    if pd.notnull(x[2])==False and pd.notnull(x[3]):
        return float(x[3])

def k(x):
    if pd.notnull(x[4]) and pd.notnull(x[5]):
        return float(float(x[4])+float(x[5]))/2
    if pd.notnull(x[4]) and pd.notnull(x[5])== False:
        return float(x[4])
    if pd.notnull(x[4])==False and pd.notnull(x[5]):
        return float(x[5])
def g(x):
    if pd.notnull(x[6]) and pd.notnull(x[7]):
        return float(float(x[6])+float(x[7]))/2
    if pd.notnull(x[6]) and pd.notnull(x[7])== False:
        return float(x[6])
    if pd.notnull(x[6])==False and pd.notnull(x[7]):
        return float(x[7])

df = pd.read_table('newoutput.csv', sep=',')
df['DOav'] = df.apply(f, axis=1) 
df['FCav'] = df.apply(k, axis=1) 
df['Eav'] = df.apply(g, axis=1) 
df.to_csv('Foutput.csv', index = False)


df = pd.read_table('Foutput.csv', sep=',')
df['Date'] = pd.to_datetime(df['Date'],unit='s')
silist = set(df['Site'])
finaldata = pd.DataFrame(np.arange(1,13), index = np.arange(1,13))
print finaldata
for x in silist:
    ddf = df[df['Site']==x]
    ddf.index = ddf['Date']
    del ddf['Date']
    mmlist = ddf.groupby(lambda x: x.month).mean()
    finaldata[x+'DO'] = mmlist['DOav']
    finaldata[x+'FC'] = mmlist['FCav']
    finaldata[x+'E'] = mmlist['Eav']
    finaldata[x+'T'] = mmlist['Tft']
del finaldata[0]
print finaldata

df = pd.read_table('Foutput.csv', sep=',')
df['Date'] = pd.to_datetime(df['Date'],unit='s')
silist = set(df['Site'])
finallist = list(sorted(silist))
print len(finallist)
matrix = np.zeros((12, len(silist)))
framesa = pd.DataFrame(matrix, index = np.arange(1,13), columns = finallist).copy()
framesb = pd.DataFrame(matrix, index = np.arange(1,13), columns = finallist).copy()
framei = pd.DataFrame(matrix, index = np.arange(1,13), columns = finallist).copy()
framesd= pd.DataFrame(matrix, index = np.arange(1,13), columns = finallist).copy()
framet = pd.DataFrame(matrix, index = np.arange(1,13), columns = finallist).copy()

for x in finallist:
    for y in range(1,13):
        if list(finaldata[str(x)+'DO'])[y-1]>= 5 and list(finaldata[str(x)+'E'])[y-1]<35:
            framesb.ix[[y],[x]] = 1
plt.imshow(np.array(framesb), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framesb)], aspect = 'auto',interpolation='nearest')
plt.colorbar()
plt.title('SA in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('sa.png', dpi=300)

for x in finallist:
    for y in range(1,13):
        if list(finaldata[str(x)+'DO'])[y-1]>= 5 and list(finaldata[str(x)+'E'])[y-1]<35  and list(finaldata[str(x)+'FC'])[y-1]<=200:
            framesb.ix[[y],[x]] = 1
plt.imshow(np.array(framesb), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framesb)], aspect = 'auto',interpolation='nearest')
plt.colorbar()
plt.title('SB in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('sb.png', dpi=300)

for x in finallist:
    for y in range(1,13):
        if list(finaldata[str(x)+'DO'])[y-1]>= 4 and list(finaldata[str(x)+'E'])[y-1]<10  and list(finaldata[str(x)+'FC'])[y-1]<=2000:
            framei.ix[[y],[x]] = 1
plt.imshow(np.array(framei), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framei)], aspect = 'auto',interpolation='nearest')  
plt.colorbar()
plt.title('I in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('i.png', dpi=300)

for x in finallist:
    for y in range(1,13):
        if list(finaldata[str(x)+'DO'])[y-1]>= 3 and list(finaldata[str(x)+'E'])[y-1]<10:
            framesd.ix[[y],[x]] = 1
plt.imshow(np.array(framesd), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framesb)], aspect = 'auto',interpolation='nearest') 
plt.colorbar()
plt.title('SD in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('sd.png', dpi=300)

for x in finallist:
    for y in range(1,13):
        if list(finaldata[str(x)+'T'])[y-1]> 5:           
            framet.ix[[y],[x]] = 1    
        if list(finaldata[str(x)+'T'])[y-1]< 3:
            framet.ix[[y],[x]] = -1    
plt.imshow(np.array(framet), cmap=plt.cm.hot, extent = [0,len(np.arange(0,72)),0,len(framesb)], aspect = 'auto',interpolation='nearest') 
plt.colorbar()
plt.title('Transparency in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('T.png', dpi=300)

for x in finallist:
    for y in range(1,13):   
        framet.ix[[y],[x]] = list(finaldata[str(x)+'T'])[y-1]     
plt.imshow(np.array(framet), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framesb)], aspect = 'auto',interpolation='nearest') 
plt.colorbar()
plt.title('Transparency in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('t.png', dpi=300)

for x in finallist:
    for y in range(1,13):       
        framesa.ix[[y],[x]] = list(finaldata[str(x)+'DO'])[y-1]
plt.imshow(np.array(framesa), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framesa)], aspect = 'auto',interpolation='nearest') 
plt.colorbar()
plt.title('DO in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('do.png', dpi=300)

for x in finallist:
    for y in range(1,13):      
        framesa.ix[[y],[x]] = list(finaldata[str(x)+'E'])[y-1]
plt.imshow(np.array(framesa), cmap=plt.cm.hot_r, extent = [0,len(np.arange(0,72)),0,len(framesa)], aspect = 'auto',interpolation='nearest') 
plt.colorbar()
plt.title('Enterococci in 2012')
label = np.arange(12, 0, -1)
plt.yticks(range(len(label)), label)
plt.savefig('e.png', dpi=300)


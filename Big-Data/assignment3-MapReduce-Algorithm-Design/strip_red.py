#!/usr/bin/env python

import sys

key = 'None'
dictt = {}

for line in sys.stdin:

    line = line.strip()
    try:
        currentkey, currentdict = line.split('\t', 1)
    
    except ValueError:
        continue
    try:
        currentdict = eval(currentdict)
        

        if currentkey!= key:
            
            if key != 'None':
                ff = sum(list(dictt.values()))
                for x in dictt.keys():
                    dictt[x] = float(dictt[x])/ff
                    print '%s,%s\t%s' % ( key,x, dictt[x])
            dictt.clear()
            dictt = currentdict
            key = currentkey
            del currentdict[key]
            
        else:
            
            del currentdict[key]
            dictt = dict([(i,dictt.get(i,0) + currentdict.get(i,0)) for i in set(dictt.keys()+currentdict.keys())])


    except ValueError:
        continue


ff =  sum(list(dictt.values()))
for x in dictt.keys():
    dictt[x] = float(dictt[x])/ff
       
    print '%s,%s\t%s' % (key,x, dictt[x])

    

#!/usr/bin/env python

import sys

currentkey1  = 'None'
currentkey2 = '*'
sum = 0
sumsub = 0


for line in sys.stdin:

    line = line.strip()
    try:
        key1,key2,  value = line.split('\t', 2)
    
    except ValueError:
        continue
    try:
        

        if currentkey1== key1 and key2== currentkey2:
            if key2 == '*':
                sum += int(value)
            else:
                sumsub += int(value)
        
        if currentkey1 == key1 and key2 != currentkey2:
            if currentkey2 == '*':
                currentkey2 = key2
                sumsub = int(value)
                
            else:
                
                print '%s,%s\t%s' % (currentkey1,currentkey2, float(sumsub)/sum)
                currentkey2 = key2
                sumsub = int(value)
                
        if currentkey1 != key1:
            if currentkey2 != '*':
                 print '%s,%s\t%s' % (currentkey1,currentkey2, float(sumsub)/sum)
            sum = int(value)
            currentkey1 = key1
            currentkey2 = key2


    except ValueError:
        continue


print '%s,%s\t%s' % (currentkey1,currentkey2, float(sumsub)/sum)   

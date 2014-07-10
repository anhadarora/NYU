#!/usr/bin/env python

import sys


for line in sys.stdin:

    line = line.strip()
    words = line.split()
    
    try:
        words_list = list(set(words))
        mm = {}.fromkeys(words_list, 0)

        for i in range(0, len(words)):
            mm[words[i]]= mm[words[i]]+1

        for key in mm:
            newmm=mm.copy()
            if mm[key] == 1:
                del newmm[key]
                print '%s\t%s\t%s' % (key,'*', sum(newmm.values()))
                for k in newmm.keys():
                    print '%s\t%s\t%s' % (key,k, newmm[k])
            else:
                
                for k in newmm:
                    newmm[k] = newmm[k]*mm[key]
                del newmm[key]
                print '%s\t%s\t%s' % (key,'*', sum(newmm.values()))
                for k in newmm:
                    print '%s\t%s\t%s' % (key,k, newmm[k])
        
    except ValueError:
        continue
        



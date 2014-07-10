#!/usr/bin/env python

import sys

for line in sys.stdin:

    line = line.strip()
    try:
        word, value = line.split('\t', 1)

    except ValueError:
        continue
        
    try:
        if float(value) == 1:
            print '%s\t%s' % (word , value)

    except ValueError:
        continue
    


    

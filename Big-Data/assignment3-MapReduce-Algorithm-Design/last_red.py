#!/usr/bin/env python

import sys

n= 0

for line in sys.stdin:
    if n <100:
        
        line = line.strip()
        word, value = line.split('\t', 1)
        print '%s\t%s' % (word , value)
    
    n = n+1

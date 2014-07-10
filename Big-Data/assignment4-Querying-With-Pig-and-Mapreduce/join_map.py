#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',', 1)
    x = line[0]
    line1 = line[1][::-1]
    line1 = line1.split(',', 1)
    z = line1[0][::-1]
    y = line1[1][::-1]
    try:
	userid = int(x)
	if len(str(userid))>14:
	    print '%s\t%s\t%s\t%s' % (z, 2, x, y)
	else:
	    print '%s\t%s\t%s\t%s' % (x, 1, y, z)
    except ValueError:
	print '%s\t%s\t%s\t%s' % (x, 1, y, z)
	continue

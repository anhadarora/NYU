#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    x, num, y, z = line.split('\t', 3)
    try:
        userid = int(y)
	if len(str(userid))>14:
	    if x == reference:
		print '%s,%s,%s,%s,%s' % (x, name, state, y, z)
	    continue
    except ValueError:
	reference = x
	name = y
	state = z

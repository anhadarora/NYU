#!/usr/bin/env python

import sys
import subprocess

f1 = subprocess.call(["/usr/bin/hadoop", "jar", "/usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3.16.jar", "-D", "mapred.reduce.tasks=1", "-D", "stream.num.map.output.key.fields=2", "-D", "num.key.fields.for.partition=1", "-file", "join_map.py", "-mapper", "join_map.py", "-file", "join_reduce.py", "-reducer", "join_reduce.py", "-partitioner", "org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner", "-input", sys.argv[2], "-input", sys.argv[4], "-output", sys.argv[6]])


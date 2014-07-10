Related commands (Use "wikipedia.txt" to do test)

1. Tests on my own machine
Stripes approach
$ cat wikipedia.txt | strip_map.py | sort | strip_red.py > test.txt
$ cat wikipedia.txt | sort_map.py | sort | sort_red.py > final.txt
Pairs approach
$ cat wikipedia.txt | pair_map.py | sort | pair_red.py > test.txt
$ cat wikipedia.txt | sort_map.py | sort | sort_red.py > final.txt

2. Tests on NYU HPC
scp -r MRExample gz475@hpc.nyu.edu:
ssh gz475@hpc.nyu.edu
scp -r MRExample dumbo:
ssh dumbo.es.its.nyu.edu
bash
alias hfs='/usr/bin/hadoop fs '
export HAS=/usr/lib/hadoop/contrib/streaming 
export HSJ=hadoop-streaming-1.0.3.16.jar 
alias hjs='/usr/bin/hadoop jar $HAS/$HSJ'
hfs -copyFromLocal /home/gz475/MRExample/wikipedia.txt wikipedia.txt
cd MRExample
hjs -file strip_map.py  -mapper strip_map.py   -file strip_pred.py -reducer strip_pred.py   -input /user/gz475/wikipedia.txt -output /user/gz475/wikipedia.output
hfs -cat wikipedia.output/*
hfs -rmr wikipedia.output
hjs -D mapred.reduce.tasks=2 -D stream.num.map.output.key.fields=2 -D num.key.fields.for.partition=1 -file pair_map.py  -mapper pair_map.py -file pair_pred.py -reducer pair_pred.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -input /user/gz475/wikipedia.txt -output /user/gz475/wikipedia.output
hfs -cat wikipedia.output/*

3. Running on AWS
Stripes approach
Configure Hadoop
--site-key-value mapred.tasktracker.reduce.tasks.maximum=20
Arguments
-D mapred.reduce.tasks=300
Pairs approach
Configure Hadoop
--site-key-value mapred.tasktracker.reduce.tasks.maximum=10
Arguments
-D mapred.reduce.tasks=100
-D stream.num.map.output.key.fields=2 
-D num.key.fields.for.partition=1
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
Final sort
Arguments
-D mapred.reduce.tasks=1

# Gang Zhao, Assignment 2, Problem 1
import sys
from datetime import datetime
deadline = datetime.strptime(sys.argv[1],"%m/%d/%Y %H:%M:%S")# set the deadline date
myFile = open('logAfterAssignment1.txt','r')
date = []
commit = []
count = 0
for line in myFile:
    if count == 0: # find commit
        indexofcommit = line.find("commit ")
        if indexofcommit != -1:
            commit.append(line)
            count+=1
    else: # identify the date of commit, and compare the time with deadline
            indexofdata = line.find("Date:")
            if indexofdata != -1:
                data = datetime.strptime(line[8:-7],"%a %b %d %H:%M:%S %Y")
                if data > deadline:
                    for x in commit: # output commit
                        print x
                    count = 0
myFile.close()              
            

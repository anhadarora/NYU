# Gang Zhao, Assignment 3, Problem 1

myfile = open ('input1.txt','r')
trips = myfile.readlines()
costsum = 0
lowchange = 0
highchange = 0
avecost = 0

for x in range(0, len(trips)):
    if trips[x].find(".") == -1 and int(trips[x]) != 0:# find the beginnings of cases
        for y in range(1,int(trips[x])+1):# calculate the sum of cost
            costsum += float(trips[x+y])
        costsum = costsum*100
        cost = costsum/int(trips[x])
        avecost = int(cost) # calculate the average cost and int it      
        for y in range (1,int(trips[x])+1):# find the total change needed from students below int average cost
            if float(trips[x+y])*100 < avecost:
                lowchange +=  float(avecost) - float(trips[x+y])*100
        for y in range (1,int(trips[x])+1):# find the total change needed from the students above int average cost
            if float(trips[x+y])*100 > (avecost+1):
                highchange +=  float(trips[x+y])*100 - float(avecost)-1
        if lowchange > highchange:# compare two, find the bigger one and print
            fchange = float(lowchange)
            fchange = fchange/100
            print "$%.2f"% (fchange)
        else:
            fchange = float(highchange)
            fchange = fchange/100
            print "$%.2f"% (fchange)
        costsum = 0
        lowchange = 0
        highchange = 0

myfile.close()

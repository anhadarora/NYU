# Gang Zhao, Assignment 3, Problem 3

class Sortname:# collect names according to their Erdos numbers
    name  = None
    pnames = None
    
    def  __init__(self, name):
        self.name = name
        self.pnames = []
    
    def addname(self, peoplename):
        self.pnames.append(peoplename)

myfile = open('input3.txt','r')
contents = myfile.readlines()
namedict = {}
sortname = {}
newcont = []
paper = []
name = []
sname = []
rownumb = []
senumb = 1
t = 2

for x in contents:
    newcont.append(x.strip('\n'))

for x in range(0, len(newcont)):
    if x < t:# escape scan loop,  except the first paper in each case
        continue
    if newcont[x].find(":") != -1:# find the location of first papers in cases
        rownumb = newcont[x-1].split(" ")
        papnumb = int(rownumb[0])# find the paper number in each case
        peopnumb = int(rownumb[1])# find the number of people needed to find Erdos number
        for y in range(0, papnumb):# collect papers
            paper.append(newcont[x+y])
        for y in range(0,peopnumb):# collect names
            name.append(newcont[x+y+papnumb])
        for y in name:
            sname.append(y)
        for y in name:# make a dict to record their Erdos numbers
            namedict[y] = 0
        for y in range (0,len(paper)+1):
            sortname[str(y)] = Sortname(str(y))
        for y in paper:
            if y.find("Erdos, P.")!= -1:# find people with Erdos 1
                for n in name:
                    if y.find(n)!= -1:
                        namedict[n]=1# record their Erdos number
                        sortname['1'].addname(n)# collect the names
                        name.remove(n)# remove from name list
                        paper.remove(y)
        for y in paper:# loop to find people's Erdos number except 1
            for n in range(1,len(paper)+1):
                for m in sortname[str(n)].pnames:
                    if y.find(m) != -1:
                        for candi in name:
                            if y.find(candi)!= -1:
                                namedict[candi] = n+1
                                sortname[str(n+1)].addname(candi)
                                name.remove(candi)
                                paper.remove(y)
        for y in name:# define the dict value of remained names in name list
            namedict[y] = 'infinity'
        print 'Scenario'+' '+str(senumb)# print
        for y in sname:
            print y+' '+str(namedict[y])
        senumb += 1
        t = x + papnumb +peopnumb
        namedict = {}
        sortname = {}
        paper = []
        name = []
        sname = []
        rownumb = []

myfile.close()

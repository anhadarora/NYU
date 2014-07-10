# Gang Zhao, Assignment3, Problem 2

myfile = open('input2.txt','r')
votes = myfile.readlines()
senumb = int(votes[0])
candi = []
votelines = []
newline = []
tiedline = []
nline = []
deline = []
count = 0
xline = []
l = 0
k = 0
votecount = 0
candicount = 0
winneroutput = 0

def clean(list):
    checked = []
    for x in list:
        if x not in checked:
            checked.append(x)
    return checked

for x in range(0, len(votes)):
    if votes[x]== '\n':# find the blank lines before cases
        for y in range(1, int(votes[x+1])+1):# collect the names of candidates
            candi.append(votes[x+1+y].strip('\n'))
            z = x+1+y
            m = x+1+y
        while  votes[z+1].find(" ")!=-1:# find the number of votes
            votecount += 1
            z += 1
            if votes[z].find(" ")== -1 or z+1 == len(votes):
                break
        candicount = int(votes[x+1])
        voteplus = int(votes[x+1])+1
        for y in range(x+2+candicount,votecount+x+2+candicount):# parse data of votes
            votelines.append(votes[y].strip('\n'))
        for y in votelines:
            newline.append(y.split(" "))
        for y in newline:
            xline.append(y)
        while candicount!=0 and winneroutput!=1 and count<senumb :# find the winner loop
            voteindex = [0 for y in range(0,voteplus)]# set up an index sequence
            removecandi = 0
            m = 0
            for p in range(0,votecount):# collect the remained candidates
                tiedline.append(newline[p][k])
            tiedline = clean(tiedline)
            for p in range(0,votecount):
                for n in range(1,voteplus):# calculate the votes of each candidate
                    if int(newline[p][k]) == n:
                        voteindex[n] += 1
            for p in newline[0]:
                for n in range (0,len(tiedline)):
                    if tiedline[n].find(p)!= -1:
                        nline.append(p)
            for p in newline[0]:
                if p not in nline:
                        deline.append(p)
                        m += 1
            candicount = candicount - m
            deline = clean(deline)
            nline = clean(nline)
            for p in newline:
                for i in deline:
                    if i in p:
                        p.remove(i)
            for i in range(1,voteplus):# find the candidate with lowest vote
                if voteindex[i]!=0:
                    min = voteindex[i]
                    max = voteindex[i]
            for i in range(1,voteplus):
                if voteindex[i]!=0: 
                    if voteindex[i]<min:
                        min = voteindex[i]
            for i in range(1,voteplus):
                if voteindex[i]!=0: 
                    if voteindex[i]>max:
                        max = voteindex[i]
            if max == min and k<candicount - 1 :
                k = k + 1
                continue
            for i in range(1,voteplus):
                if voteindex[i]> float(votecount*0.5)and voteindex[i]!= min:# winner, if candidate votes plus half of total votes
                    print candi[i-1]
                    winneroutput = 1
                    count += 1
                    if count < senumb:# blank line between cases
                        print '\n'
                if voteindex[i] ==  min:# remove lowest votes from votes list
                    removecandi += 1
                    for p in newline:
                        if str(i) in p:
                            p.remove(str(i))
                            l = l+1
            if removecandi == candicount:# if all removed, print them
                for tiedcandi in sorted(tiedline):
                    print candi[int(tiedcandi)-1]
                count += 1
                winneroutput = 1
                if count < senumb:# blank line between cases
                    print '\n'
            candicount = candicount - removecandi
            tiedline = []
        votecount = 0
        winneroutput = 0
        candi = []
        votelines = []
        deline = []
        nline = []
        newline = []

myfile.close()

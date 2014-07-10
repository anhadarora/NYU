# Gang Zhao, Assignment 3, Problem 4

class Coordinate:# collect coordinates of each Waldorfs' first letters' location
    name  = None
    coords = None
    
    def  __init__(self, name):
        self.name = name
        self.coords = []
    
    def addcoord(self, coord):
        self.coords.append(coord)

myfile = open('input4.txt','r')
content = myfile.readlines()
senumb = int(content[0])
numbline = []
words = []
newwords = []
letters = []
grid = []
lines = []
newgrid = []
coordinate = {}
count = 0
printse = 0

for x in range(0, len(content)):# sacn the input text
    if content[x] == '\n':
        numbline = content[x+1].strip('\n')
        numbline = numbline.split(" ")
        rownumb = int(numbline[0])# find the number of rows
        colnumb = int(numbline[1])# find the nember of columns
        wordnumb = int(content[x+2+rownumb].strip('\n'))#find the number of Waldorfs
        for y in range(x+3+rownumb, x+3+rownumb+wordnumb):
            words.append(content[y].strip('\n'))
        for y in range(0, len(words)):# parse the Waldorfs
            for z in words[y]:
                letters.append(z.lower())
            newwords.append(letters)
            letters = []
        for y in range(x+2, x+2+rownumb):# parse the grid
            grid.append(content[y].strip('\n'))
        for y in range (0, len(grid)):
            for z in grid[y]:
                lines.append(z.lower())
            newgrid.append(lines)
            lines = []
        for y in words:
            coordinate[y]= Coordinate(y)
        for y in range(0,len(newwords)):
            for a in range(0, rownumb):
                for b in range(0,colnumb):
                    if newwords[y][0]== newgrid[a][b]:
                        if a+len(newwords[y])-1 < rownumb and b+len(newwords[y])-1 < colnumb:# move to (+1, +1)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a+c][b+c]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if  b+len(newwords[y])-1 < colnumb:# move to (0,+1)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a][b+c]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if a-len(newwords[y])+1>=0 and b+len(newwords[y])-1 < colnumb:# move to (-1,+1)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a-c][b+c]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if a-len(newwords[y])+1 >= 0:# move to (-1,0)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a-c][b]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if a-len(newwords[y])+1 >=0 and b-len(newwords[y])+1 >=0:# move to (-1,-1)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a-c][b-c]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if  b-len(newwords[y])+1 >= 0:# move to (0,-1)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a][b-c]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if a+len(newwords[y])-1 < rownumb and b-len(newwords[y])+1>=0 :# move to (+1,-1)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a+c][b-c]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
                        if a+len(newwords[y])-1 < rownumb:# move to (+1,0)
                            for c in range(1,len(newwords[y])):
                                if newwords[y][c] == newgrid[a+c][b]:
                                    count += 1  
                                if count == len(newwords[y])-1:
                                    coordinate[words[y]].addcoord((a+1,b+1))
                            count = 0
        for y in range (0,len(words)):# print the first coordinates of Waldorfs
            print coordinate[words[y]].coords[0][0],coordinate[words[y]].coords[0][1]
        printse += 1
        if printse >= 1 and printse<senumb :# blank line between cases
            print '\n'
        numbline = []
        words = []
        newwords = []
        letters = []
        grid = []
        lines = []
        newgrid = []
        coordinate = {}

myfile.close()

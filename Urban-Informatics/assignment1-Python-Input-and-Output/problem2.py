import sys
n=int(sys.argv[1])
if n>=3000:
    print "Wrong"
acount=0
for i in range(1,n):
    if abs(int(sys.argv[i+2])-int(sys.argv[i+1]))==n-i:
        acount+=1
if acount==n-1:
    print "Jolly"
else:
    print "Not jolly"

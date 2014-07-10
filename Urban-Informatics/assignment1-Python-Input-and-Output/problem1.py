import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
n=0
if a>b:
  m=b
  b=a
  a=m
for i in range(a,b+1):
  acount=1
  while i!=1:
    if i%2==0:
      i=i/2
      acount+=1
    else:
      i=3*i+1
      acount+=1
  if acount>n: 
      n=acount
print int(sys.argv[1]),int(sys.argv[2]),n

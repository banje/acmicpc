import sys
a,b=sys.stdin.readline().split()
c=sys.stdin.readline().split()
for i in range(int(a)):
    c[i]=int(c[i])
c.sort()
print(c[int(b)-1])
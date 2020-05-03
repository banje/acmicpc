import sys
a=sys.stdin.readline().split()
b=dict()
for i in range(int(a[0])):
    e=sys.stdin.readline().rstrip()
    b[e]=i+1
    b[str(i+1)]=e
for i in range(int(a[1])):
    c=sys.stdin.readline().rstrip()
    d=b[c]
    print(d)
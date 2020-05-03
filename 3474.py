import sys
a=int(sys.stdin.readline())
for i in range(a):
    b=int(sys.stdin.readline())
    c=5
    d=0
    while c<=b:
        d=d+b//c
        c=c*5
    print(d)
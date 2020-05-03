import sys
a=int(sys.stdin.readline())
for i in range(a):
    b=int(sys.stdin.readline())
    c=b
    while b!=1:
        if b%2==0:
            b=b//2
        else:
            b=b*3+1
            if b>c:
                c=b
    print(c)
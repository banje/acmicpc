import sys
a=int(sys.stdin.readline())
c=[]
for i in range(a):
    b=sys.stdin.readline().rstrip()
    if b=='pop':
        if c!=[]:
            print(c.pop())
        else:
            print(-1)
    elif b=='top':
        if c!=[]:
            print(c[-1])
        else:
            print(-1)
    elif b=='size':
        print(len(c))
    elif b=='empty':
        if c==[]:
            print(1)
        else:
            print(0)
    else:
        d=b[5:]
        c.append(d)
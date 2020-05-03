import sys
n=int(sys.stdin.readline())
b=[]
for i in range(n):
    a=sys.stdin.readline().rstrip()
    if a=="pop":
        if b==[]:
            print(-1)
        else:
            print(b[0])
            b.remove(b[0])
    elif a=="size":
        print(len(b))
    elif a=="empty":
        if b==[]:
            print(1)
        else:
            print(0)
    elif a=="front":
        if b==[]:
            print(-1)
        else:
            print(b[0])
    elif a=="back":
        if b==[]:
            print(-1)
        else:
            print(b[-1])
    else:
        c=int(a[5:])
        b.append(c)
import sys
N=int(sys.stdin.readline())
b=[]
for i in range(N):
    a=sys.stdin.readline().rstrip()
    if a=="pop_front":
        if b==[]:
            print(-1)
        else:
            print(b[0])
            b.pop(0)
    elif a=="pop_back":
        if b==[]:
            print(-1)
        else:
            print(b[-1])
            b.pop()
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
    elif a[5:9]=="fron":
        b.insert(0,a[11:])
    else:
        b.append(a[10:])
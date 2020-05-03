a=int(input())
for i in range(a):
    b=int(input())
    d=[]
    e=[]
    for j in range(b):
        c=input().split()
        if c[1] not in d:
            d.append(c[1])
            e.append(1)
        else:
            f=d.index(c[1])
            e[f]=e[f]+1
    g=1
    for j in e:
        g=g*(j+1)
    g=g-1
    print(g)
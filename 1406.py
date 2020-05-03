a=input()
b=[0]*600001
c=[0]*600001
d=[0]*600001
for i in range(1,len(a)+1):
    b[i]=i-1
    c[i]=a[i-1]
    d[i]=i+1
b[0]=-1
c[0]=-1
d[0]=1
d[len(a)]=-1
e=len(a)
f=int(input())
h=e+1
for i in range(f):
    g=input().split()
    if g[0]=="L":
        if b[e]!=-1:
            e=b[e]
    elif g[0]=="D":
        if d[e]!=-1:
            e=d[e]
    elif g[0]=="B":
        if b[e]!=-1:
            d[b[e]]=d[e]
            if d[e]!=-1:
                b[d[e]]=b[e]
            e=b[e]
    elif g[0]=="P":
        d[h]=d[e]
        d[e]=h
        b[d[h]]=h
        b[h]=e
        c[h]=g[1]
        e=h
        h=h+1
j=0
while True:
    j=d[j]
    if j==-1:
        break
    print(c[j],end="")

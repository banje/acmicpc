g=[]
for i in range(1,11):
    h=1
    for j in range(i):
        h=h*(10-j)
    for j in range(2,i+1):
        h=h//j
    g.append(h)
g[0]=g[0]-1
for i in range(1,10):
    g[i]=g[i]+g[i-1]
e=int(input())
if e<10:
    print(e)
else:
    f=1
    k=""
    l=9
    while f<10:
        for i in range(f):

    print(-1)
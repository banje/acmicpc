a=int(input())
b=[]
for i in range(a):
    b.append(input().split())
g=[0,0]
h=0
c=[[0,0]]
e=a
while True:
    d=0
    l=[]
    for k in c:
        f=b[k[0]][k[1]]
        h=0
        for i in range(k[0],k[0]+e):
            for j in range(k[1],k[1]+e):
                if b[i][j]!=f:
                    d=1
                    h=1
                    break
            if h==1:
                break
        else:
            if f=="0":
                g[0]=g[0]+1
            else:
                g[1]=g[1]+1
            l.append(k)
    if d==0:
        break
    e=e//2
    for i in l:
        c.remove(i)
    h=len(c)
    for i in range(h):
        c.append([c[i][0]+e,c[i][1]])
        c.append([c[i][0],c[i][1]+e])
        c.append([c[i][0]+e,c[i][1]+e])
print(g[0])
print(g[1])
a=int(input())
b=[]
for i in range(a):
    b.append(input())
g=""
c=[[0,0,a]]
k=c[0]
while True:
    h=0
    if c==[]:
        while d<a:
            g=g+")"
            d=d*2
        break
    d=k[2]
    k=c[0]
    f=b[k[1]][k[0]]
    while d<k[2]:
        g=g+")"
        d=d*2
    while d>k[2]:
        g=g+"("
        d=d//2
    h=0
    for i in range(k[0],k[0]+k[2]):
        for j in range(k[1],k[1]+k[2]):
            if b[j][i]!=f:
                h=1
                c.remove(k)
                c.insert(0, [k[0] + k[2]//2, k[1] + k[2]//2, k[2] // 2])
                c.insert(0, [k[0], k[1] + k[2]//2, k[2] // 2])
                c.insert(0, [k[0] + k[2]//2, k[1], k[2] // 2])
                c.insert(0,[k[0],k[1],k[2]//2])
                break
        if h==1:
            break
    else:
        if f=="0":
            g=g+"0"
        else:
            g=g+"1"
        c.remove(k)
print(g)
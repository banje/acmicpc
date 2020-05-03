a=int(input())
b=input()
c=[]
d=set()
g=0
for i in range(a):
    c.append(ord(b[i]))
    d.add(ord(b[i]))
d=list(d)
d.sort(reverse=True)
while True:
    if d==[] or a==1:
        break
    e=d[0]
    if e in c:
        f=c.index(e)
        if f==0:
            if c[1]+1==c[0]:
                c.pop(f)
                a=a-1
                g=g+1
            else:
                c[f]=-1
        elif f==a-1:
            if c[a-2]+1==c[a-1]:
                c.pop(f)
                a = a - 1
                g=g + 1
            else:
                c[f] = -1
        else:
            if c[f-1]+1==c[f] or c[f+1]+1==c[f]:
                c.pop(f)
                a = a - 1
                g = g + 1
            else:
                c[f]=-1
    else:
        while -1 in c:
            c[c.index(-1)]=e
        d.pop(0)
print(g)
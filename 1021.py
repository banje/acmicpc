N,M=map(int,input().split())
c=[]
j=0
for i in range(N):
    c.append(i+1)
a=input().split()
for i in range(M):
    b=int(a[i])
    if c[0]==b:
        c.pop(0)
    else:
        d=c.index(b)
        e=len(c)
        f=e-d
        if d<=f:
            g=c[:d]
            h=c[d+1:]
            c=h+g
            j=j+d
        else:
            for k in range(f):
                l=c.pop()
                c.insert(0,l)
            c.pop(0)
            j=j+f
print(j)
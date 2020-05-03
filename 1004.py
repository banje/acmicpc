def chkin(a,b):
    d=a.split()
    x1=int(d[0])
    y1=int(d[1])
    x2=int(d[2])
    y2=int(d[3])
    e=b.split()
    cx=int(e[0])
    cy=int(e[1])
    r=int(e[2])
    c=1
    if ((x1-cx)**2+(y1-cy)**2<r**2)&((x2-cx)**2+(y2-cy)**2<r**2):
        c=0
    if ((x1-cx)**2+(y1-cy)**2>r**2)&((x2-cx)**2+(y2-cy)**2>r**2):
        c=0
    return c
c=0
t=0
T=int(input())
while t!=T:
    c=0
    a=input()
    n=0
    N=int(input())
    while n!=N:
        b=input()
        c=c+chkin(a,b)
        n=n+1
    print(c)
    t=t+1
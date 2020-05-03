g=[]
h=input().split()
for i in range(2):
    a=h[i]
    b=len(a)
    b=2**b-1
    a=int(a)-1+i
    if a<10:
        if a>=7:
            g.append(4)
        elif a>=4:
            g.append(3)
        else:
            g.append(2)
    else:
        while True:
            c=bin(b)[3:]
            d=c
            d=d.replace('0','4')
            d=d.replace('1','7')
            e=int(d)
            if e>a:
                g.append(b)
                break
            f=e
            b=b+1
print(g[1]-g[0])
T=int(input())
t=0
d=[]
while True:
    a=input()
    b=a.split()
    x1=int(b[0])
    y1=int(b[1])
    r1=int(b[2])
    x2=int(b[3])
    y2=int(b[4])
    r2=int(b[5])
    r=(r1+r2)**2
    c=(x1-x2)**2+(y1-y2)**2
    m=max(r1,r2)
    e=(r1-r2)**2
    if (c==0)&(r1!=r2):
        d.append(0)
    elif (c==0)&(r1==r2):
        d.append(-1)
    elif e>c:
        d.append(0)
    elif e==c:
        d.append(1)
    else:
        if r>c:
            d.append(2)
        elif r==c:
            d.append(1)
        else:
            d.append(0)
    t=t+1
    if t==T:
        break
for i in d:
    print(i)

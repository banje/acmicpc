a=int(input())
b=int(input())
c=int(a**0.5)
d=[]
if c==a**0.5:
    d.append(a)
c=c+1
while True:
    e=c**2
    if e<=b:
        d.append(e)
        c=c+1
    else:
        break
if d==[]:
    print(-1)
else:
    f=0
    for i in range(len(d)):
        f=f+d[i]
    print(f)
    print(min(d))
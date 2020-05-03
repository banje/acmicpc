a=int(input())
b=input().split()
for i in range(a):
    b[i]=int(b[i])
c=[]
i=0
d=0
g=0
while True:
    if b[i]<0:
        if g!=0:
            c.append(d)
        c.append(b[i])
        d=0
        i=i+1
        if i==a:
            break
    else:
        d=d+b[i]
        i=i+1
        g=1
        if i==a:
            c.append(d)
            break
if len(c)==1:
    print(max(c))
    quit()
i=0
e=c[0]
while True:
    f=c[i]+c[i+1]
    if f>0:
        if max(c[i],c[i+1])>e:
            e=max(c[i],c[i+1])
        c[i]=c[i]+c[i+1]
        c.pop(i+1)
    else:
        i=i+2
    if i>len(c)-2:
        break
print(max(max(c),e))
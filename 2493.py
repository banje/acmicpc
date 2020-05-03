a=int(input())
b=input().split()
for i in range(a):
    b[i]=int(b[i])
d=[]
e=0
f=0
for i in range(a):
    c=b[i]
    for j in range(i-1,e-1,-1):
        if b[j]>c:
            d.append(j+1)
            break
    else:
        d.append(0)
    if c>f:
        e=i
        f=c
for i in range(a):
    print(d[i],end=" ")
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[0]
d=[0]
for i in range(a[0]):
    for j in range(len(c)):
        e=c[j]+b[i]
        f=e-1
        if e>=a[1]:
            e=e-a[1]
        if f>=a[1]:
            f=f-a[1]
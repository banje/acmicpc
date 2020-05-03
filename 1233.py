a=list(map(int,input().split()))
b=[]
for i in range(a[0]):
    for j in range(a[1]):
        for k in range(a[2]):
            b.append(i+j+k+3)
d=0
for i in range(4,a[0]+a[1]+a[2]):
    c=b.count(i)
    if c<=d:
        print(i-1)
        break
    d=c
a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in range(a):
    b[i]=b[i]-c[i]
b.sort()
d=0
for i in range(a-1):
    for k in range(i+1,a):
        if b[i]+b[k]>0:
            d=d+a-k
            break
print(d)
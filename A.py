a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
e=0
f=0
for j in range(a):
    if b[j]!=c[j]:
        if b[j]==1:
            e=e+1
        else:
            f=f+1
if e==0:
    print(-1)
else:
    print(f//e+1)
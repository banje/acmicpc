a=int(input())
b=[0,0]
for i in range(a):
    c=list(map(int,input().split()))
    e=0
    for j in range(0,3):
        for k in range(j+1,4):
            for l in range(k+1,5):
                d=(c[j]+c[k]+c[l])%10
                if d>e:
                    e=d
    if e>=b[0]:
        b=[e,i+1]
print(b[1])
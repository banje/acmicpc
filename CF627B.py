a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    e=0
    for j in range(b-2):
        if e==1:
            break
        d=c[j]
        for k in range(j+2,b):
            if c[k]==d:
                print("YES")
                e=1
                break
    if e==0:
        print("NO")
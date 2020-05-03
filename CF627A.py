a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=c[0]%2
    for j in range(1,b):
        if c[j]%2!=d:
            print("NO")
            break
    else:
        print("YES")
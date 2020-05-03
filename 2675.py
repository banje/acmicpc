T=int(input())
for i in range(T):
    a,b=input().split()
    c=""
    for j in range(len(b)):
        c=c+b[j]*int(a)
    print(c)
a=int(input())
for i in range(a):
    b=int(input())
    c=set(map(int,input().split()))
    d=int(input())
    e=list(map(int,input().split()))
    for j in range(d):
        if e[j] in c:
            print(1)
        else:
            print(0)
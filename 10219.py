a=int(input())
for i in range(a):
    b,c=input().split()
    b=int(b)
    c=int(c)
    d=[]
    for j in range(b):
        d.append(input())
    for j in range(b):
        e=""
        for k in range(c):
            e=e+d[j][c-1-k]
        d[j]=e
    for  j in range(b):
        print(d[j])
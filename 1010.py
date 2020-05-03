a=int(input())
for i in range(a):
    b=input().split()
    c=int(b[1])
    b=int(b[0])
    d=c-b
    e=1
    if b>d:
        for j in range(b+1,c+1):
            e=e*j
        for j in range(2,d+1):
            e=e//j
    else:
        for j in range(d+1,c+1):
            e=e*j
        for j in range(2,b+1):
            e=e//j
    print(e)
a=int(input())
for i in range(a):
    b=input()
    c=len(b)
    d=0
    e=0
    if b[0]=="O":
        e=e+1
        d=d+e
    else:
        e=0
    for j in range(1,c):
        if b[j]=="O":
            e=e+1
            d=d+e
        else:
            e=0
    print(d)
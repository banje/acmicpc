a=int(input())
for i in range(a):
    b=input()
    c=len(b)
    d=0
    e=0
    for j in range(c):
        if b[j]=="R":
            e=0
        else:
            e=e+1
        if e>d:
            d=e
    print(d+1)
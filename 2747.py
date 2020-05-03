n=int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a=0
    b=1
    c=1
    while True:
        d=a+b
        c=c+1
        if c==n:
            print(d)
            break
        a=b
        b=d
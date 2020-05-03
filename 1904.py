n=int(input())
if n==1:
    print(1)
else:
    a=1
    b=2
    c=2
    while True:
        d=a+b
        c=c+1
        if c==n:
            print(d%15746)
            break
        a=b
        b=d%15746
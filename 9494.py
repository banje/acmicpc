while True:
    a=int(input())
    if a==0:
        break
    b=input()
    c=0
    d=0
    while True:
        if c>=len(b):
            d=d+1
            if d==a:
                print(c+1)
                break
            b=input()
        elif b[c]==" ":
            d=d+1
            if d==a:
                print(c+1)
                break
            b=input()
        else:
            c=c+1
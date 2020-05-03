for i in range(3):
    a=input()
    b=0
    c=1
    d=[]
    while b<7:
        if a[b]==a[b+1]:
            c=c+1
        else:
            d.append(c)
            c=1
        b=b+1
    d.append(c)
    d.sort()
    print(d[-1])
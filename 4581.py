while True:
    a=input()
    if a=="#":
        break
    b=len(a)
    d=0
    e=0
    f=0
    for i in range(b):
        c=a[i]
        if c=="Y":
            d=d+1
        elif c=="N":
            e=e+1
        elif c=="A":
            f=f+1
    if b/2<=f:
        print("need quorum")
    elif d>e:
        print("yes")
    elif d<e:
        print("no")
    else:
        print("tie")
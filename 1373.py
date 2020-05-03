a=input()
if a=="0":
    print(0)
else:
    b=len(a)
    c=b%3
    if c==1:
        print("1",end="")
    elif c==2:
        if a[0:2]=="10":
            print("2",end="")
        else:
            print("3",end="")
    i=c
    while i<b:
        d=a[i:i+3]
        if d=="000":
            print("0",end="")
        if d=="001":
            print("1",end="")
        if d=="010":
            print("2",end="")
        if d=="011":
            print("3",end="")
        if d=="100":
            print("4",end="")
        if d=="101":
            print("5",end="")
        if d=="110":
            print("6",end="")
        if d=="111":
            print("7",end="")
        i=i+3
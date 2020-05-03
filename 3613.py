a=input()
if a[0].isupper() or a[0]=="_" or a[-1]=="_":
    print("Error!")
    quit()
if "_" in a:
    if a.lower()!=a:
        print("Error!")
        quit()
    b=len(a)
    c=""
    d=0
    for i in range(b):
        if a[i]=="_":
            if a[i+1]=="_":
                print("Error!")
                quit()
            d=1
        else:
            if d==1:
                c=c+a[i].upper()
                d=0
            else:
                c=c+a[i]
    print(c)
else:
    b=len(a)
    c=""
    for i in range(b):
        if a[i].isupper():
            c=c+"_"+a[i].lower()
        else:
            c=c+a[i]
    print(c)
a=input()
if a=="0":
    print(0)
else:
    b=len(a)
    c=int(a[0])
    print(bin(c)[2:],end="")
    for i in range(1,b):
        d=a[i]
        if d=="0":
            print("000",end="")
        elif d=="1":
            print("001",end="")
        elif d=="2":
            print("010",end="")
        elif d=="3":
            print("011",end="")
        elif d=="4":
            print("100",end="")
        elif d=="5":
            print("101",end="")
        elif d=="6":
            print("110",end="")
        elif d=="7":
            print("111",end="")
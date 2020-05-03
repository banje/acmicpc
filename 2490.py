for i in range(3):
    a=input().split()
    b=a.count("0")
    if b==0:
        print("E")
    elif b==1:
        print("A")
    elif b==2:
        print("B")
    elif b==3:
        print("C")
    else:
        print("D")
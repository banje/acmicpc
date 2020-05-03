a=int(input())
for i in range(a):
    b=input().split()
    if b[1]=="kg":
        print("{0:.4f} lb".format(float(b[0])*2.2046))
    elif b[1]=="lb":
        print("{0:.4f} kg".format(float(b[0])*0.4536))
    elif b[1]=="l":
        print("{0:.4f} g".format(float(b[0])*0.2642))
    elif b[1]=="g":
        print("{0:.4f} l".format(float(b[0])*3.7854))
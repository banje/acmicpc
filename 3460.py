a=int(input())
for i in range(a):
    b=str(bin(int(input())))
    c=len(b)
    for j in range(c):
        if b[-1-j]=="1":
            print(j,end=" ")
a=int(input())
for i in range(a):
    b=int(input())
    c=[]
    c.append(b//25)
    b=b%25
    c.append(b//10)
    b=b%10
    c.append(b//5)
    b=b%5
    c.append(b)
    for j in range(4):
        print(c[j],end=" ")
    print("")
a=input()
b=0
while True:
    if len(a)==1:
        print(b)
        if int(a)%3==0:
            print("YES")
        else:
            print("NO")
        break
    c=0
    for i in a:
        c=c+int(i)
    a=str(c)
    b=b+1
a=int(input())
b=input()
d=0
while True:
    if a==1:
        print(d)
        break
    for i in range(a):
        c=ord(b[i])
        if i==0:
            if ord(b[1])+1==c:
                b=b[1:]
                a=a-1
                d=d+1
                break
        elif i==a-1:
            if ord(b[i-1])+1==c:
                b=b[:-1]
                a=a-1
                d=d+1
                break
        else:
            if ord(b[i-1])+1==c or ord(b[i+1])+1==c:
                b=b[:i]+b[i+1:]
                a=a-1
                d=d+1
                break
    else:
        print(d)
        break
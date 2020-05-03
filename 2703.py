a=int(input())
for i in range(a):
    b=input()
    c=input()
    d=""
    for j in b:
        if j==" ":
            d=d+" "
        else:
            d=d+c[ord(j)-65]
    print(d)
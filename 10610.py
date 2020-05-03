c=input()
a=int(c)
if "0" not in c:
    print(-1)
    quit()
elif a%3!=0:
    print(-1)
    quit()
else:
    b=[]
    for i in range(len(c)):
        b.append(c[i])
    b.sort()
    d=""
    for i in range(len(c)):
        d=b[i]+d
    print(d)
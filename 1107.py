a=int(input())
b=int(input())
if b!=0:
    c=input().split()
    for i in range(len(c)):
        c[i]=int(c[i])
    e=0
    f=1
    g=a-1
    j=abs(100-a)
    d = str(a)
    for i in c:
        if str(i) in d:
            a = a + 1
            e = e + 1
            if len(str(a)) + e > j:
                print(j)
                quit()
            break
    else:
        if len(str(a)) + e > j:
            print(j)
            quit()
        print(len(str(a)) + e)
        quit()
    while True:
        if g>=0:
            h=str(g)
            for i in c:
                if str(i) in h:
                    g=g-1
                    f=f+1
                    if len(str(g)) + f > j:
                        print(j)
                        quit()
                    break
            else:
                if len(str(g)) + f > j:
                    print(j)
                    quit()
                print(len(str(g))+f)
                quit()
        d=str(a)
        for i in c:
            if str(i) in d:
                a=a+1
                e=e+1
                if len(str(a)) + e > j:
                    print(j)
                    quit()
                break
        else:
            if len(str(a)) + e > j:
                print(j)
                quit()
            print(len(str(a))+e)
            quit()
else:
    if (98<a) and (a<103):
        print(abs(100-a))
    else:
        print(len(str(a)))
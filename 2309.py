a=[]
c=0
for i in range(9):
    b=int(input())
    a.append(b)
    c=c+b
a.sort()
for i in range(9):
    d=c-a[i]-100
    if d in a:
        if d==a[i]:
            if a.count(d)>1:
                a.remove(d)
                a.remove(d)
                for i in range(7):
                    print(a[i])
                break
        else:
            a.remove(d)
            a.remove(a[i])
            for i in range(7):
                print(a[i])
            break
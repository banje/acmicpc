def b(a,c):
    d=[]
    for z in a:
        for y in c:
            if y not in z:
                e=z[:]
                e.append(y)
                f=e
                f.sort()
                if f not in d:
                    d.append(e)
    return d
a=list(map(int,input().split()))
c=list(map(int,input().split()))
c.sort()
d=[]
for z in range(a[0]):
    d.append([c[z]])
for z in range(a[1]-1):
    d=b(d,c)
for z in d:
    for y in z:
        print(y,end=" ")
    print()
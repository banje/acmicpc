def b(a,c):
    d=[]
    for z in a:
        for y in c:
            e=z[:]
            e.append(y)
            d.append(e)
    return d
a=list(map(int,input().split()))
c=[]
d=[]
for z in range(a[0]):
    c.append(z+1)
    d.append([z+1])
for z in range(a[1]-1):
    d=b(d,c)
for z in d:
    for y in z:
        print(y,end=" ")
    print()
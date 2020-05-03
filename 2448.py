a=int(input())
b=[[a]]
c=[a]
for i in range(int(a/3)):
    d=[]
    e=[]
    f=[]
    for j in c:
        d.append(j-1)
        d.append(j+1)
        e.append(j-2)
        e.append(j-1)
        e.append(j)
        e.append(j+1)
        e.append(j+2)
        if j-3 in f:
            f.remove(j-3)
        else:
            f.append(j-3)
        if j+3 in f:
            f.remove(j+3)
        else:
            f.append(j+3)
    b.append(d)
    b.append(e)
    b.append(f)
    c=f
b.pop()
for i in b:
    g=" "*(2*a-1)
    for j in i:
        g=g[:j-1]+"*"+g[j:]
    print(g)
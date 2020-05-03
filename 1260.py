n,m,v=input().split()
c1=[]
c2=[]
d1=[int(v)]
d2=[int(v)]
for i in range(int(n)):
    c1.append([])
    c2.append([])
for i in range(int(m)):
    a,b=input().split()
    if a!=b:
        if int(b) not in c1[int(a)-1]:
            c1[int(a)-1].append(int(b))
            c2[int(a)-1].append(int(b))
        if int(a) not in c1[int(b)-1]:
            c1[int(b)-1].append(int(a))
            c2[int(b)-1].append(int(a))
for i in range(int(n)):
    c1[i].sort()
    c2[i].sort()
e=int(v)
h2=[]
while True:
    if c2[e-1]==[]:
        if h2==[]:
            break
        else:
            e=h2.pop()
    else:
        l=e
        if c2[e-1][0] not in d2:
            d2.append(c2[e-1][0])
            h2.append(e)
            e=c2[e-1][0]
        j=c2[l-1][0]
        c2[l-1].pop(0)
        k=c2[j-1].index(l)
        c2[j-1].pop(k)
h1=[]
e=int(v)
while True:
    if c1[e-1]==[]:
        if h1==[]:
            break
        else:
            e=h1[0]
            h1.pop(0)
    else:
        for i in c1[e-1]:
            if i not in d1:
                d1.append(i)
            h1.append(i)
        c1[e-1]=[]
        e=h1[0]
        h1.pop(0)
for i in d2:
    print(i,end=" ")
print("")
for i in d1:
    print(i,end=" ")
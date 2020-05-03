a=int(input())
b=[]
c=[]
e=[]
for i in range(a):
    d=input().split()
    b.append(int(d[0]))
    c.append(int(d[1]))
    e.append(1)
for i in range(a):
    for j in range(a):
        if b[i]<b[j]:
            if c[i]<c[j]:
                e[i]=e[i]+1
for i in range(a):
    print(e[i],end=" ")
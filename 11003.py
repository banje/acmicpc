a=input().split()
b=int(a[1])
a=int(a[0])
c=input().split()
d=5000001
e=[]
for i in range(b):
    if c[i]<d:
        d=c[i]
        e=[i]
        print(d,end=" ")
    elif c[i]==d:
        e.append(i)
        print(d,end=" ")
    else:
        print(d,end=" ")
for i in range(b,a):

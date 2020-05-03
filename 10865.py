a=input().split()
b=int(a[1])
a=int(a[0])
c=[0]*a
for i in range(b):
    d=input().split()
    c[int(d[0])-1]=c[int(d[0])-1]+1
    c[int(d[1])-1]=c[int(d[1])-1]+1
for i in range(a):
    print(c[i])
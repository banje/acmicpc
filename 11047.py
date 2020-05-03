a=input().split()
b=int(a[1])
a=int(a[0])
c=[]
for i in range(a):
    c.append(int(input()))
d=a-1
e=0
while d>=0:
    if c[d]<=b:
        f=b//c[d]
        b=b-f*c[d]
        e=e+f
    else:
        d=d-1
print(e)
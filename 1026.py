a=int(input())
b=input().split()
c=input().split()
for i in range(a):
    b[i]=int(b[i])
    c[i]=int(c[i])
b.sort()
c.sort()
d=0
for i in range(a):
    d=d+b[i]*c[a-1-i]
print(d)
a=input().split()
b=int(a[1])
a=int(a[0])
c=[0]
for i in range(1,46):
    for j in range(i):
        c.append(i)
d=0
for i in range(a,b+1):
    d=d+c[i]
print(d)
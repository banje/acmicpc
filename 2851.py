a=0
b=[100]
c=[100]
for i in range(10):
    a=a+int(input())
    if a<100:
        b.append(100-a)
    else:
        c.append(a-100)
b.sort()
c.sort()
if b[0]<c[0]:
    print(100-b[0])
else:
    print(100+c[0])
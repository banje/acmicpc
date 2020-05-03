def a(b):
    c=b
    while b>9:
        c=c+b%10
        b=b//10
    c=c+b
    return c
b=set()
c=set()
for i in range(10000):
    b.add(a(i))
    c.add(i)
d=list(c-b)
d.sort()
for i in d:
    print(i)
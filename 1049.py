a=input().split()
b=int(a[1])
a=int(a[0])
d=1001
e=1001
for i in range(b):
    c=input().split()
    g=int(c[0])
    h=int(c[1])
    if g<d:
        d=g
    if h<e:
        e=h
if d>=6*e:
    print(a*e)
else:
    f=a//6
    print(min(f*d+(a-6*f)*e,(f+1)*d))
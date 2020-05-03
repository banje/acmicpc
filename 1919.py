a=input()
b=input()
d=0
for i in range(97,123):
    c=chr(i)
    e=a.count(c)
    f=b.count(c)
    d=d+(abs(e-f))
print(d)
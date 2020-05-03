a,b=input().split()
c=""
d=""
for i in range(3):
    c=c+a[2-i]
    d=d+b[2-i]
if int(c)>int(d):
    print(c)
else:
    print(d)
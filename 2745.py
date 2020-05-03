a=input().split()
b=int(a[1])
c=0
for i in range(len(a[0])):
    d=ord(a[0][-1-i])
    if d>=65:
        d=d-7
    d=d-48
    c=c+d*b**i
print(c)
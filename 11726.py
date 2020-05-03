a=int(input())
b=0
c=1
for z in range(a):
    d=b+c
    if d>=10007:
        d=d-10007
    b=c
    c=d
print(d)
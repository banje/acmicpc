a=int(input())
b=input().split()
c=int(input())
d=0
for i in b:
    e=int(i)//c
    if int(i)%c==0:
        e=e-1
    d=d+(e+1)*c
print(d)
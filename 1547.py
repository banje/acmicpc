a=int(input())
e=1
for i in range(a):
    b=input().split()
    c=int(b[0])
    d=int(b[1])
    if c==e:
        e=d
    elif d==e:
        e=c
print(e)
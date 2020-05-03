a=int(input())
for i in range(a):
    b=int(input())
    c=input().split()
    d=0
    for j in range(b):
        d=d+int(c[j])
    print(d)
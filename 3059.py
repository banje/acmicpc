a=int(input())
for i in range(a):
    b=input()
    c=set()
    for j in range(len(b)):
        c.add(b[j])
    d=2015
    for j in c:
        d=d-ord(j)
    print(d)
a=input().split()
b=set()
for i in range(int(a[0])):
    b.add(input())
c=[]
for i in range(int(a[1])):
    d=input()
    if d in b:
        c.append(d)
c.sort()
print(len(c))
for i in c:
    print(i)
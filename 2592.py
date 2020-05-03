a=0
b=[]
for i in range(10):
    c=int(input())
    a=a+c
    b.append(c)
d=set(b)
e=[0,0]
for i in d:
    if b.count(i)>e[0]:
        e=[b.count(i),i]
print(a//10)
print(e[1])
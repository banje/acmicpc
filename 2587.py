a=0
b=[]
for i in range(5):
    c=int(input())
    a=a+c
    b.append(c)
b.sort()
print(a//5)
print(b[2])
a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
b.sort()
c=[]
for i in range(a):
    d=b[a-1-i]*(i+1)
    c.append(d)
print(max(c))
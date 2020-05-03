a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(c)
b.sort()
for i in range(a-1,-1,-1):
    print(b[i])
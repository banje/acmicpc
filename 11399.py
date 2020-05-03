a=int(input())
b=input().split()
for i in range(a):
    b[i]=int(b[i])
b.sort()
c=0
for i in range(a):
    c=c+b[i]*(a-i)
print(c)
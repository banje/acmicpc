a=int(input())
b=input().split()
d=0
for i in range(a):
    c=b.pop()
    if c in b:
        d=d+1
print(d)
a=int(input())
b=set(input().split())
c=int(input())
d=input().split()
for i in range(c):
    if d[i] in b:
        print(1)
    else:
        print(0)
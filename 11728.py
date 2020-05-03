a=input()
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=b+c
d.sort()
for i in d:
    print(i,end=" ")
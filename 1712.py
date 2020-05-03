a=input().split()
b=int(a[1])
c=int(a[2])
a=int(a[0])
if b>=c:
    print(-1)
else:
    d=a//(c-b)+1
    print(d)
a=[100,100]
b=int(input())
for i in range(b):
    c=input().split()
    if c[0]>c[1]:
        a[1]=a[1]-int(c[0])
    elif c[0]<c[1]:
        a[0]=a[0]-int(c[1])
print(a[0])
print(a[1])
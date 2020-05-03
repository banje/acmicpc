a=input()
b=len(a)
c=10
d=a[0]
for i in range(1,b):
    if a[i]!=d:
        c=c+5
    c=c+5
    d=a[i]
print(c)
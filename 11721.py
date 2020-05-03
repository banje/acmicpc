a=input()
b=len(a)
c=0
for i in range(b//10):
    d=a[c:c+10]
    print(d)
    c=c+10
d=a[c:]
print(d)
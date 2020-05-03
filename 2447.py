a=int(input())
def b(a):
    c=len(a)
    d=[]
    for i in range(c):
        d.append(a[i]*3)
    for i in range(c):
        d.append(a[i]+" "*c+a[i])
    for i in range(c):
        d.append(a[i]*3)
    return d
c=0
while True:
    a=a//3
    c=c+1
    if a==1:
        break
d="*"
for i in range(c):
    d=b(d)
for i in d:
    print(i)
a=int(input())
b=[]
for z in range(a):
    b.append(list(map(int,input().split())))
b.sort(key=lambda a:[a[1],a[0]])
c=-1
d=0
e=0
while True:
    if b[d][0]<c:
        d=d+1
    else:
        e=e+1
        c=b[d][1]
        d=d+1
    if d==a:
        print(e)
        break
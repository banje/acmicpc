n = int(input())
if n==1:
    print(0)
    quit()
a=[]
N = n+7
b=[0]*N
d=0
for i in range(1000):
    a.append([])
a[0].append(1)
for i in range(1,1000):
    for j in a[i-1]:
        c=j*3
        if c<N and b[c]==0:
            a[i].append(c)
            b[c]=1
        c=j*2
        if c<N and b[c]==0:
            a[i].append(c)
            b[c]=1
        c=j+1
        if c<N and b[c]==0:
            a[i].append(c)
            b[c]=1
    if b[n]==1:
        print(i)
        break
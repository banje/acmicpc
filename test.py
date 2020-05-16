z=0
for n in range(1,100000):
    if n==1:
        z=max(z,0)
    else:
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
                z=max(z,i)
                break
print(z)
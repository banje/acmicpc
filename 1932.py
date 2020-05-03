a=int(input())
f=[0]
g=[0]
for i in range(a):
    e = input().split()
    for j in range(i+1):
        if j==0:
            g[0]=f[0]+int(e[0])
        elif j==i:
            g.append(int(e[j])+f[j-1])
        else:
            if f[j-1]>f[j]:
                g[j]=f[j-1]+int(e[j])
            else:
                g[j]=f[j]+int(e[j])
    f=g[:]
print(max(f))
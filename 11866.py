N,M=map(int,input().split())
a=[]
b=[]
c=0
for i in range(1,N+1):
    a.append(i)
while True:
    if a==[]:
        print("<",end="")
        for i in range(N-1):
            print(b[i],end=", ")
        print(b[N-1],end="")
        print(">")
        break
    d=len(a)
    c=c-1
    for i in range(M):
        c=c+1
        if c>=d:
            c=c-d
    b.append(a[c])
    a.remove(a[c])
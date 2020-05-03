T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    a=input().split()
    b=[]
    c=1
    for i in range(N):
        a[i]=int(a[i])
        b.append(i)
    while True:
        if a[0]<max(a):
            a.append(a[0])
            b.append(b[0])
            a.remove(a[0])
            b.remove(b[0])
        else:
            if b[0]==M:
                print(c)
                break
            else:
                a.remove(a[0])
                b.remove(b[0])
                c=c+1
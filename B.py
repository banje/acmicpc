a=int(input())
b=list(map(int,input().split()))
c=0
d=set()
for i in range(a):
    if i not in d:
        e=b[i]
        f=e
        d.add(i)
        j=i+1
        while True:
            if j==a:
                break
            if j not in d:
                if b[j]-e==j-i:
                    e=b[j]
                    i=j
                    d.add(j)
                    f=f+e
            j=j+1
        if f>c:
            c=f
print(c)
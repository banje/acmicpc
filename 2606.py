a=int(input())
d=[]
for i in range(a):
    d.append([i+1])
b=int(input())
for i in range(b):
    c=list(map(int,input().split()))
    e=len(d)
    f=0
    for j in range(e):
        if c[0] in d[j]:
            for k in range(e):
                if c[1] in d[k]:
                    if j!=k:
                        d[j]=d[j]+d[k]
                        d.remove(d[k])
                    f=1
                    break
        if f==1:
            break
for i in d:
    if 1 in i:
        print(len(i)-1)
        break
a=input().split()
b=a[1]
a=a[0]
d=len(a)
c=len(b)-d
g=51
for i in range(c+1):
    e=b[i:i+d]
    f=0
    for j in range(d):
        if e[j]!=a[j]:
            f=f+1
    if f==0:
        print(0)
        quit()
    if f<g:
        g=f
print(g)
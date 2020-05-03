b=[]
for i in range(100):
    b.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
c=input().split()
d=int(c[1])
c=int(c[0])
if c==0:
    print(0)
    quit()
for i in range(c):
    e=input().split()
    f=int(e[1])-1
    g=int(e[2])-1
    h=int(e[3])-1
    e=int(e[0])-1
    j=e
    while j<=g:
        k=f
        while k<=h:
            b[j][k]=b[j][k]+1
            k=k+1
        j=j+1
o=0
for m in range(100):
    for n in range(100):
        if b[m][n]>d:
            o=o+1
print(o)
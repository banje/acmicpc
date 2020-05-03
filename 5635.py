a=int(input())
c=[]
d=[]
for i in range(a):
    b=input().split()
    c.append(b[0])
    d.append(int(b[1])+int(b[2])*100+int(b[3])*10000)
print(c[d.index(max(d))])
print(c[d.index(min(d))])
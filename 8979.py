a=input().split()
d=[]
for i in range(int(a[0])):
    b=input().split()
    e=int(b[1])*1000001**2+int(b[2])*1000001+int(b[3])
    d.append(e)
    if b[0]==a[1]:
        c=e
d.sort(reverse=True)
f=d.index(c)
print(f+1)
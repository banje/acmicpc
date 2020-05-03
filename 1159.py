a=int(input())
c=dict()
for i in range(a):
    b=input()
    if b[0] in c:
        c[b[0]]=c[b[0]]+1
    else:
        c[b[0]]=1
d=[]
for i in c:
    if c[i]>=5:
        d.append(i)
d.sort()
if d==[]:
    print("PREDAJA")
else:
    for i in d:
        print(i,end="")
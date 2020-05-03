a=int(input())
b=[]
c=[]
for i in range(a):
    d=input()
    if d in b:
        e=b.index(d)
        c[e]=c[e]+1
    else:
        b.append(d)
        c.append(1)
f=[]
g=0
while True:
    if c==[]:
        break
    h=max(c)
    e=c.index(h)
    if h<g:
        break
    f.append(b.pop(e))
    g=c.pop(e)
f.sort()
print(f[0])
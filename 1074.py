a=input().split()
b=int(a[1])
c=int(a[2])
a=int(a[0])
d=bin(b)[2:]
e=bin(c)[2:]
while len(d)<a:
    d="0"+d
while len(e)<a:
    e="0"+e
f=0
for i in range(a):
    if d[i]=="0" and e[i]=="0":
        a
    elif d[i]=="0" and e[i]=="1":
        f=f+(4**(a-1-i))
    elif d[i]=="1" and e[i]=="0":
        f=f+2*(4**(a-1-i))
    elif d[i]=="1" and e[i]=="1":
        f=f+3*(4**(a-1-i))
print(f)
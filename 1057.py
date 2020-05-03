a,b,c=map(int,input().split())
d=1
e=0
while True:
    d=d*2
    e=e+1
    if d>=a:
        break
f=1
g=min(b,c)
h=max(b,c)
for i in range(e):
    if h-g==1:
        if h%2==0:
            print(f)
            break
    g=(g+1)//2
    h=(h+1)//2
    f=f+1
else:
    print(-1)
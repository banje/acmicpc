c=0
d=[]
while True:
    a,b=map(int,input().split())
    c=c-a
    c=c+b
    d.append(c)
    if b==0:
        break
print(max(d))
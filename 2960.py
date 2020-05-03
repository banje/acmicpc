a=input().split()
b=[]
c=int(a[1])
f=int(a[0])
for i in range(2,f+1):
    b.append(i)
while True:
    d=b[0]
    e=d
    while True:
        if e in b:
            b.remove(e)
            c=c-1
            if c==0:
                print(e)
                quit()
            e=e+d
        elif e>f:
            break
        else:
            e=e+d
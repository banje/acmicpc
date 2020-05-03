def e(b,a):
    if a>=b:
        if a+b>0:
            if a==b:
                c=(2*a+1)**2
            else:
                c=(2*(a-1)+1)**2+(a-b)
        else:
            c=(2*(-b-1)+1)**2-(2*b)+(-b-a)
    else:
        if a+b<=0:
            c=(2*(a-1)+1)**2+(4*a)+(b-a)
        else:
            c=(2*(b-1)+1)**2+(6*b)+(a+b)
    return c

a,b,c,d=map(int,input().split())
if abs(a)>abs(c):
    m=a
else:
    m=c
if abs(b)>=abs(d):
    n=b
else:
    n=d
f=e(m,n)
g=len(str(f))
for i in range(a,c+1):
    for j in range(b,d+1):
        h=e(i,j)
        k=g-len(str(h))
        for l in range(k):
            print(" ",end="")
        print(h,end=" ")
    print("")
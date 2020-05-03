def e(a,b):
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
o=int(input())
p=int(input())
c=int((o-1)/2)
d=c
a=-c
b=-c
for i in range(a,c+1):
    for j in range(b,d+1):
        h=e(-i,-j)
        print(h,end=" ")
        if h==p:
            q=[i+c+1,j+c+1]
    print("")
print("{} {}".format(q[0],q[1]))
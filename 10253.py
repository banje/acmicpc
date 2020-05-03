def f(a,b):
    while True:
        if a==b:
            return a
        if (a==1)or(b==1):
            return 1
        c=abs(a-b)
        d=min(a,b)
        a=c
        b=d

a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    while True:
        if b==1:
            print(c)
            break
        e=c//b+1
        b=b*e-c
        c=c*e
        for j in range(b-1):
            if (c%(b-j)==0)and(b%(b-j)==0):
                g=b-j
                b=int(b/g)
                c=int(c/g)
                break
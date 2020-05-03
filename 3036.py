def d(a,b):
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
b=input().split()
for i in range(len(b)):
    b[i]=int(b[i])
c=b.pop(0)
for i in b:
    e=d(c,i)
    print("{}/{}".format(int(c/e),int(i/e)))
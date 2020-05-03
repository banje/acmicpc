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


b,c=map(int,input().split())
print("{}".format(int(b*c/d(b,c))))
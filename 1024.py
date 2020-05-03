a,b=map(int,input().split())
if (b-1)*b/2>a:
    print(-1)
    quit()
d=0
while d==0:
    if b>100:
        print(-1)
        break
    if b%2==0:
        if a%b==b/2:
            c=int((a-b/2)/b-b/2+1)
            if c<0:
                print(-1)
                d=1
            else:
                for i in range(c,c+b):
                    print(i,end=" ")
                    d=1
        else:
            b=b+1
    else:
        if a%b==0:
            c=int((a/b)-(b//2))
            if c<0:
                print(-1)
                d=1
            else:
                for i in range(c,c+b):
                    print(i,end=" ")
                    d=1
        else:
            b=b+1
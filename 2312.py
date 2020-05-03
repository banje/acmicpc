a=int(input())
for i in range(a):
    b=int(input())
    d=dict()
    while True:
        c=int(b**0.5)
        for j in range(2,c+1):
            if b%j==0:
                if j in d:
                    d[j]=d[j]+1
                else:
                    d[j]=1
                b=b//j
                break
        else:
            if b in d:
                d[b]=d[b]+1
            else:
                d[b]=1
            break
    for i in d:
        print("{} {}".format(i,d[i]))
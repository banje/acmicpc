T=int(input())
for i in range(T):
    a=int(input())
    b=int(input())
    c=1
    d=1
    for j in range(a+1):
        c=c*(b+j)
        d=d*(j+1)
    print("{}".format(int(c/d)))
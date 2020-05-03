a=int(input())
if a<100:
    print(a)
else:
    e=99
    for i in range(100,a+1):
        b=i//100
        c=(i//10)%10
        d=i%10
        if c==(b+d)/2:
            e=e+1
    print(e)
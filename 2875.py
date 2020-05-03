a=input().split()
b=int(a[1])
c=int(a[2])
a=int(a[0])
if a>2*b:
    d=a-2*b
    if d>=c:
        print(b)
        quit()
    else:
        b=b-round((c-d)/3+0.4)
        print(b)
        quit()
elif a<2*b:
    if a%2==1:
        a=a-1
        c=c-1
    d=b-a//2
    if d>=c:
        print(a//2)
        quit()
    else:
        b=b-d-(round((c-d)/3+0.4))
        print(b)
        quit()
else:
    b=b-round(c/3+0.4)
    print(b)
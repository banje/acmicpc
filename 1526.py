a=input()
b=len(a)
b=2**b-1
a=int(a)
if a<10:
    if a>=7:
        print(7)
    else:
        print(4)
else:
    while True:
        c=bin(b)[3:]
        d=c
        d=d.replace('0','4')
        d=d.replace('1','7')
        e=int(d)
        if e>a:
            print(f)
            break
        f=e
        b=b+1
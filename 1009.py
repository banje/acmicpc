a=int(input())
for i in range(a):
    b=input().split()
    c=int(b[0][-1])
    d=int(b[1])
    if c in [1,5,6]:
        print(c)
    elif c in [4,9]:
        print(c**(d%2+2)%10)
    elif c in [0]:
        print(10)
    else:
        print(c**(d%4+4)%10)
a=int(input())
for i in range(a):
    b=input().split()
    c=[int(b[0]),int(b[1])]
    while True:
        if c[0]==c[1]:
            d=c[0]
            break
        if min(c)==1:
            d=1
            break
        c=[max(c)-min(c),min(c)]
    print(int(b[0])*int(b[1])//d,d)
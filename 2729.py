a=int(input())
for i in range(a):
    b=input().split()
    if len(b[0])<len(b[1]):
        g=b[0]
        b[0]=b[1]
        b[1]=g
    c=len(b[0])-len(b[1])
    b[1]="0"*c+b[1]
    c=len(b[0])
    d=""
    f=0
    for j in range(1,c+1):
        e=int(b[0][-j])+int(b[1][-j])+f
        if e==0:
            d="0"+d
            f=0
        elif e==1:
            d="1"+d
            f=0
        elif e==2:
            d="0"+d
            f=1
        else:
            d="1"+d
            f=1
    d=str(f)+d
    h=d.lstrip("0")
    if h=="":
        print("0")
    else:
        print(h)
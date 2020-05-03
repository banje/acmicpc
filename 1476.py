a=list(map(int,input().split()))
if a[0]==15:
    a[0]=0
if a[1]==28:
    a[1]=0
if a[2]==19:
    a[2]=0
if a==[0,0,0]:
    print(7980)
    quit()
b=a[1]
while True:
    if b%19==a[2]:
        if b%15==a[0]:
            print(b)
            break
    b=b+28
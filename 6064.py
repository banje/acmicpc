a=int(input())
for z in range(a):
    b=list(map(int,input().split()))
    if b[1]==b[3]:
        b[3]=0
    for y in range(b[1]):
        c=b[0]*y+b[2]
        if c%b[1]==b[3]:
            print(c)
            break
    else:
        print(-1)
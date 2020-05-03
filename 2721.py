a=int(input())
for i in range(a):
    b=int(input())
    c=0
    for j in range(1,b+1):
        c=c+j*(j+1)*(j+2)/2
    print(int(c))
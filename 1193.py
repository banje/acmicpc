a=int(input())
i=1
while True:
    b=i*(i+1)/2
    if b>=a:
        c=a-(i-1)*i/2
        if i%2==0:
            print("{}/{}".format(int(c),int(i-c+1)))
            break
        else:
            print("{}/{}".format(int(i-c+1),int(c)))
            break
    i=i+1
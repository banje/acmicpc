a=int(input())
while True:
    if a==1:
        print("1")
        break
    else:
        if a%2==0:
            a=a//2
        else:
            print("0")
            break
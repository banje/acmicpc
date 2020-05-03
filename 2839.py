a=int(input())
if a in [4,7]:
    print("-1")
else:
    b=a//5
    for i in range(b):
        c=a-b*5
        if c%3==0:
            print("{:d}".format(int(b+c/3)))
            break
        b=b-1
    else:
        print("{:d}".format(int(a/3)))
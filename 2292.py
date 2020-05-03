b=int(input())
i=1
while True:
    a=i*(i-1)*3+1
    if a>=b:
        print(i)
        break
    i=i+1
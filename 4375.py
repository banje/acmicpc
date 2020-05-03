while True:
    try:
        a=int(input())
    except EOFError:
        break
    b=1
    c=1
    while True:
        if b%a==0:
            print(c)
            break
        else:
            b=b*10+1
            c=c+1
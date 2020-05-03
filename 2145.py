while True:
    a=input()
    if a=="0":
        break
    while True:
        if len(a)==1:
            print(a)
            break
        c=0
        for i in a:
            c=c+int(i)
        a=str(c)
a=int(input())
for i in range(a):
    b=int(input())
    d=b
    while True:
        c=int(d**0.5)
        for j in range(2, c+1):
            if not d%j:
                d=d-1
                break
        else:
            e=d
            break
    d=b
    while True:
        c=int(d**0.5)
        for j in range(2, c+1):
            if not d%j:
                d=d+1
                break
        else:
            f=d
            break
    print(f-e)
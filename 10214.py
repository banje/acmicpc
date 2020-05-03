a=int(input())
for i in range(a):
    c=0
    d=0
    for j in range(9):
        b=input().split()
        c=c+int(b[0])
        d=d+int(b[1])
    if c>d:
        print("Yonsei")
    elif c==d:
        print("Draw")
    else:
        print("Korea")
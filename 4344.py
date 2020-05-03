a=int(input())
for i in range(a):
    b=input().split()
    c=int(b[0])
    d=0
    for j in range(1,c+1):
        d=d+int(b[j])
    d=d/c
    e=0
    for j in range(1,c+1):
        if int(b[j])>d:
            e=e+1
    print("{:.3f}%".format(e/c*100))
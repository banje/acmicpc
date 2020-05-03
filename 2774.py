a=int(input())
for i in range(a):
    b=input()
    c=0
    for j in range(10):
        if str(j) in b:
            c=c+1
    print(c)

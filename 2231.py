a=int(input())
for i in range(a):
    b=str(i)
    c=0
    for j in range(len(b)):
        c=c+int(b[j])
    d=i+c
    if d==a:
        print(i)
        break
else:
    print(0)
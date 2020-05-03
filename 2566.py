a=[]
for i in range(9):
    a.append(list(map(int,input().split())))
b=0
for i in range(9):
    for j in range(9):
        if a[i][j]>b:
            b=a[i][j]
            c=i+1
            d=j+1
print(b)
print("{} {}".format(c,d))
a=input().split()
b=[]
c=[]
for i in range(int(a[0])):
    b.append(input().split())
for i in range(int(a[0])):
    c.append(input().split())
for i in range(int(a[0])):
    for j in range(int(a[1])):
        print(int(b[i][j])+int(c[i][j]),end=" ")
    if i!=int(a[0])-1:
        print("")
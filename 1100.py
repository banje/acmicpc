a=[]
for i in range(8):
    a.append(input())
b=0
for i in [0,2,4,6]:
    for j in [0,2,4,6]:
        if a[i][j]=="F":
            b=b+1
for i in [1,3,5,7]:
    for j in [1,3,5,7]:
        if a[i][j]=="F":
            b=b+1
print(b)
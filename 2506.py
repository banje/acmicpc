a=int(input())
b=input().split()
if b[0]=="1":
    c=1
    d=2
else:
    c=0
    d=1
for i in range(1,a):
    if b[i]=="1":
        c=c+d
        d=d+1
    else:
        d=1
print(c)
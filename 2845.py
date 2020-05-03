a=input().split()
b=int(a[0])*int(a[1])
c=list(map(int,input().split()))
for i in c:
    print(i-b,end=" ")
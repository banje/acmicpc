a=list(map(int,input().split()))
a[0]=a[0]-1
a[1]=a[1]-1
b=a[0]//4
c=a[0]%4
d=a[1]//4
e=a[1]%4
print(abs(b-d)+abs(c-e))
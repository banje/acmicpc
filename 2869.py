a=input().split()
b=int(a[1])
c=int(a[2])
a=int(a[0])
d=(c-a+(a-b-1))//(a-b)+1
print(d)
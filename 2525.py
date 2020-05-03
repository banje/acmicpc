a=input().split()
b=int(a[0])*60+int(a[1])
b=b+int(input())
b=b%1440
c=b//60
d=b%60
print("{} {}".format(c,d))
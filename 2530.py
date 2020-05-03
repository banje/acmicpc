a=input().split()
b=int(a[0])*3600+int(a[1])*60+int(a[2])
b=b+int(input())
b=b%86400
c=b//3600
b=b%3600
d=b//60
e=b%60
print("{} {} {}".format(c,d,e))
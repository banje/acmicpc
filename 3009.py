a=input().split()
b=input().split()
c=input().split()
if a[0]==b[0]:
    d=c[0]
elif a[0]==c[0]:
    d=b[0]
else:
    d=a[0]
if a[1]==b[1]:
    e=c[1]
elif a[1]==c[1]:
    e=b[1]
else:
    e=a[1]
print("{} {}".format(d,e))
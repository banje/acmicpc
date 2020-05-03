a=input()
b=a
c=b
for i in range(len(a)):
    if a[i]=="5":
        c=c[:i]+"6"+c[i+1:]
    elif a[i]=="6":
        b=b[:i]+"5"+b[i+1:]
b=b.split()
c=c.split()
print("{} {}".format(int(b[0])+int(b[1]),int(c[0])+int(c[1])))
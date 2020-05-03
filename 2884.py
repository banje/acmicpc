a=input().split()
if int(a[1])<45:
    a[0]=int(a[0])-1
    a[1]=int(a[1])+15
    if a[0]<0:
        a[0]=a[0]+24
else:
    a[1]=int(a[1])-45
print("{} {}".format(a[0],a[1]))
a=list(map(int,input().split(":")))
b=list(map(int,input().split(":")))
c=3600*a[0]+60*a[1]+a[2]
d=3600*b[0]+60*b[1]+b[2]
e=d-c
if e<=0:
    e=e+86400
f=e//3600
e=e-f*3600
g=e//60
e=e-60*g
print("%02d:%02d:%02d" %(f,g,e))
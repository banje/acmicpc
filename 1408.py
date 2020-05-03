a=input()
a=int(a[0:2])*3600+int(a[3:5])*60+int(a[6:8])
b=input()
b=int(b[0:2])*3600+int(b[3:5])*60+int(b[6:8])
c=b-a
if c>=86400:
    c=c-86400
if c<0:
    c=c+86400
d=c//3600
e=(c-3600*d)//60
f=c-3600*d-60*e
if d<10:
    d="0"+str(d)
if e<10:
    e="0"+str(e)
if f<10:
    f="0"+str(f)
print("{}:{}:{}".format(d,e,f))
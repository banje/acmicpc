a=input().split()
b=input().split()
c=int(a[0])*int(b[1])+int(a[1])*int(b[0])
d=int(a[1])*int(b[1])
e=(c,d)
while True:
    if e[0]==e[1]:
        print("{} {}".format(c//e[0],d//e[0]))
        break
    if 1 in e:
        print("{} {}".format(c,d))
        break
    e=(max(e)-min(e),min(e))
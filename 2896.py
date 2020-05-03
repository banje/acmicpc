a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(3):
    c.append(a[i]/b[i])
d=min(c)
if d<1:
    print("0 0 0")
else:
    for i in range(3):
        e=a[i]-(b[i]*d)
        if int(e)==e:
            print(int(e),end=" ")
        else:
            print("{}".format(round(e,6)),end=" ")
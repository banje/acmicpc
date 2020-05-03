T=int(input())
a=[]
for i in range(T):
    b=int(input())
    a.append(b)
c=max(a)
d=[1,1]
while len(d)<c:
    d.append(d[-2]+d[-1])
for i in a:
    if i==0:
        print("1 0")
    elif i==1:
        print("0 1")
    else:
        print("{} {}".format(d[i-2],d[i-1]))
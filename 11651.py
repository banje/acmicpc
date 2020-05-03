a=int(input())
b=[]
for i in range(a):
    c=input().split()
    d=(int(c[1]),int(c[0]))
    b.append(d)
b.sort()
for i in b:
    print("{} {}".format(i[1],i[0]))
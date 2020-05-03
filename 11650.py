a=int(input())
b=[]
for i in range(a):
    c=input().split()
    d=(int(c[0]),int(c[1]))
    b.append(d)
b.sort()
for i in b:
    print("{} {}".format(i[0],i[1]))
    #print(*i)
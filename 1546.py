a=int(input())
b=input().split()
c=[]
d=0
for i in b:
    c.append(int(i))
    d=d+int(i)
print("{}".format(d/a/max(c)*100))
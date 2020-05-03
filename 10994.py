a=int(input())
def b(a):
    c=len(a)
    d=[]
    d.append("*"*(c+4))
    d.append("*"+" "*(c+2)+"*")
    for i in range(c):
        d.append("* "+a[i]+" *")
    d.append("*"+" "*(c+2)+"*")
    d.append("*" * (c + 4))
    return d
c=["*"]
for i in range(a-1):
    c=b(c)
for i in c:
    print(i)
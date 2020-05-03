a=int(input())
def b(a):
    c=len(a)
    d=[]
    d.append("*"*(c+2))
    d.append("*")
    d.append("* "+a[0]+"**")
    d.append("* "+a[1]+" "*(c-2)+"*")
    for i in range(2,c):
        d.append("* "+a[i]+" *")
    d.append("*"+" "*c+"*")
    d.append("*"*(c+2))
    return d
c=["*****","*","* ***","* * *","* * *","*   *","*****"]
if a==1:
    print("*")
else:
    for i in range(a-2):
        c=b(c)
    for i in c:
        print(i)
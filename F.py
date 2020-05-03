a=int(input())
b=input()
c=int(input())
for i in range(c):
    d=input().split()
    e=b[int(d[0])-1:int(d[0])-1+int(d[2])]
    f=b[int(d[1])-1:int(d[1])-1+int(d[2])]
    if e.count("1")!=f.count("1"):
        print("No")
    else:
        g=int(d[2])//2
        if int(d[2])%2==1:
            g=g+1
        l=0
        m=0
        for j in range(g):
            if e[2*j]=="1":
                l=l+1
            if f[2*j]=="1":
                m=m+1
        if l!=m:
            print("No")
        else:
            print("Yes")
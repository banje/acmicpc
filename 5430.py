import sys
T=int(sys.stdin.readline())
for i in range(T):
    a=sys.stdin.readline().rstrip()
    b=int(sys.stdin.readline())
    c=sys.stdin.readline().rstrip()
    e=0
    f=0
    k=0
    if c=="[]":
        d=[]
    else:
        c=c[1:len(c)-1].split(",")
        d=[]
        for j in range(b):
            d.append(int(c[j]))
    g=len(d)
    for j in range(len(a)):
        if a[j]=="R":
            if e==0:
                e=1
            else:
                e=0
        else:
            if f==g:
                k=1
                break
            else:
                if e==0:
                    f=f+1
                else:
                    g=g-1
    if k==0:
        if e==0:
            d=d[f:g]
        else:
            d=d[f:g]
            d.reverse()
        if d==[]:
            print("[]")
        else:
            print("[",end="")
            for j in range(len(d)-1):
                print(d[j],end=",")
            print(d[-1],end="]\n")
    else:
        print("error")
import sys
T=int(sys.stdin.readline())
for i in range(T):
    a,b,c=sys.stdin.readline().split()
    d=(int(c)-1)//int(a)+1
    e=(int(c)-1)%int(a)
    if d<10:
        d="0"+str(d)
    f=str(e+1)+str(d)
    sys.stdout.write(f)
    sys.stdout.write("\n")
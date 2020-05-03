import sys
a=sys.stdin.read().rstrip()
c=0
d=[]
for i in range(97,123):
    b=a.count(chr(i))
    if b>c:
        c=b
        d=[chr(i)]
    elif b==c:
        d.append(chr(i))
for i in range(len(d)):
    print(d[i],end="")
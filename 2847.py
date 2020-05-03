a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
e=0
for i in range(a-1):
    c=b[-1-i]
    d=b[-2-i]
    if d>=c:
        e=e+d-c+1
        b[-2-i]=c-1
print(e)
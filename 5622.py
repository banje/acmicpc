a=input()
b=len(a)
d=0
for i in range(b):
    c=(ord(a[i])-65)
    if c<18:
        d=d+(ord(a[i])-65)//3+3
    elif c==18:
        d=d+8
    elif c<22:
        d=d+9
    else:
        d=d+10
print(d)
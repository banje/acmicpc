a=input().split()
b=int(a[1])
a=int(a[0])
def c(a):
    b=str(a)
    d=""
    for i in range(len(b)):
        d=b[i]+d
    return int(d)
print(c(c(a)+c(b)))
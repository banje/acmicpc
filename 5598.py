a=input()
d=""
for i in range(len(a)):
    b=ord(a[i])
    if b<68:
        c=b+23
    else:
        c=b-3
    d=d+chr(c)
print(d)
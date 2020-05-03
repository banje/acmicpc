a=[64]
b=int(input())
while True:
    a.sort()
    c=sum(a)
    if c>b:
        d=a.pop(0)
        if c-d/2>=b:
            a.append(int(d/2))
        else:
            a.append(int(d/2))
            a.append(int(d/2))
    else:
        break
print(len(a))
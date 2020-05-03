a=input().upper()
b=0
for i in range(65,91):
    c=a.count(chr(i))
    if c>b:
        b=c
        d=chr(i)
    elif c==b:
        d="?"
print(d)
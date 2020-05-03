a=input()
b=0
c=["a","e","i","o","u"]
while True:
    if a[b] in c:
        a=a[:b+1]+a[b+3:]
    b = b + 1
    if b==len(a):
        break
print(a)
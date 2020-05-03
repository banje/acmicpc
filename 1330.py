a=input().split()
b=int(a[1])
a=int(a[0])
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")
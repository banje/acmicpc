a=input().split()
if len(a[0])*int(a[0])<int(a[1]):
    print(a[0]*int(a[0]))
else:
    print(a[0]*(int(a[1])//len(a[0])),end="")
    print(a[0][:int(a[1])%len(a[0])])
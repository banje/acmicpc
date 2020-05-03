a=input().split()
b=int(a[1])
a=int(a[0])
for i in range(a):
    c=input()
    for j in range(b):
        print(c[b-1-j],end="")
    print("")
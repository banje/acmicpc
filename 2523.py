a=int(input())
b=""
for i in range(a):
    b=b+"*"
    print(b)
for i in range(a-1):
    b=b[1:]
    print(b)
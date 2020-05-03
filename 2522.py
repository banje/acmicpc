a=int(input())
b=" "*a
for i in range(a):
    b=b[1:]+"*"
    print(b)
for i in range(a-1):
    b=" "+b[:-1]
    print(b)
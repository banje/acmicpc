a=int(input())
b="*"*a
for i in range(a):
    print(b)
    b=" "+b
    b=b[:-1]
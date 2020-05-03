a=int(input())
b="* "*a
b=b[:-1]
for i in range(a):
    print(b)
    if b[0]=="*":
        b=" "+b
    else:
        b=b[1:]
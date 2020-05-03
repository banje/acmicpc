a=int(input())
b="* "*((a+1)//2)
b=b[:-1]
c = " " + b
if a % 2 == 1:
    c = c[:-2]
for i in range(a):
    print(b)
    print(c)
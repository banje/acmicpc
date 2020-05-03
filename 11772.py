a=int(input())
b=0
for i in range(a):
    c=input()
    b=b+int(c[0:-1])**int(c[-1])
print(b)
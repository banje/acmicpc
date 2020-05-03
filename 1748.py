a=input()
b=len(a)
c=0
a=int(a)
for i in range(1,b):
    c=c+i*(10**(i-1))*9
    a=a-9*(10**(i-1))
c=c+a*b
print(c)
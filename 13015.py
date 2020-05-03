a=int(input())
print("*"*a+" "*(2*(a-1)-1)+"*"*a)
b="*"+" "*(a-2)+"*"
for i in range(a-2):
    print(" "*(i+1)+b+" "*(2*(a-1)-1-2*(i+1))+b)
print(" "*(a-1)+b+b[1:])
for i in range(a-3,-1,-1):
    print(" "*(i+1)+b+" "*(2*(a-1)-1-2*(i+1))+b)
print("*"*a+" "*(2*(a-1)-1)+"*"*a)
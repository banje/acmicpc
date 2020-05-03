a=int(input())-1
b=" "*(a-1)+"*"
if a!=0:
    print(" "+b)
c=" *"
for i in range(a-1):
    b=b[1:]
    print(" "+b + c)
    c="  "+c
print("*"*(2*a+1))
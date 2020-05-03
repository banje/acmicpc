a=int(input())
b=" "*(a-1)+"*"
print(b)
c=" *"
for i in range(a-1):
    b=b[1:]
    print(b + c)
    c="  "+c
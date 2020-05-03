a=int(input())
b=" "*(a-1)+"*"
for i in range(a):
    print(b)
    b=b[1:]+" *"
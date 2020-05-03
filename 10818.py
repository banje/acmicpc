a=int(input())
b=input().split()
for i in range(a):
    b[i]=int(b[i])
print("{} {}".format(min(b),max(b)))
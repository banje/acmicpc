import sys
a=int(input())
b=1
for i in range(a):
    b=b+int(sys.stdin.readline())-1
print(b)
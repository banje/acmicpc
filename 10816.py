a=int(input())
b={}
for i in map(int, input().split()):
    if i in b:
        b[i] = b[i]+1
    else:
        b[i] = 1
a=int(input())
for i in range(a):
    b=input().split()
    c=b[1]
    b=int(b[0])
    print(c[:b-1]+c[b:])
a=int(input())
b=map(int,input().split())
b=set(b)
b=list(b)
b.sort()
print(*b)
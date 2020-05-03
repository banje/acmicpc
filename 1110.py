a=int(input())
N=1
c=a
while True:
    b=a//10+a%10
    a=a%10*10+b%10
    if a==c:
        print(N)
        break
    N=N+1
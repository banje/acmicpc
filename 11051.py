N,K=map(int,input().split())
K=min(K,N-K)
a=1
b=N
for i in range(K):
    a=a*b
    b=b-1
for i in range(K):
    a=a//(i+1)
print(a%10007)
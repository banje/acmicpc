while True:
    N,K=map(int,input().split())
    if (N==0)and(K==0):
        break
    else:
        K=min(K,N-K)
        a=1
        b=N
        for i in range(K):
            a=a*b
            b=b-1
        for i in range(K):
            a=a//(i+1)
        print(a)
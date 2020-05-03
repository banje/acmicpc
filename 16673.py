a=list(map(int,input().split()))
print(a[1]*a[0]*(a[0]+1)//2+a[2]*a[0]*(a[0]+1)*(2*a[0]+1)//6)
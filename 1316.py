N=int(input())
b=0
for i in range(N):
    a=input()
    for j in range(97,123):
        c=a.count(chr(j))
        if c!=0:
            d=chr(j)*c
            if d not in a:
                break
    else:
        b=b+1
print(b)
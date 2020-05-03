a=list(map(int,input().split()))
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        print("Bad")
        break
else:
    print("Good")
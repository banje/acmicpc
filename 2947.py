a=input().split()
while True:
    for i in range(4):
        if a[i]>a[i+1]:
            b=a[i]
            a[i]=a[i+1]
            a[i+1]=b
            for j in a:
                print(j,end=" ")
            if a==["1","2","3","4","5"]:
                quit()
            print("")
a=input()
b=int(input())
for i in range(10):
    for j in range(10):
        c=int(a[:-2]+str(i)+str(j))
        if c%b==0:
            print(str(i)+str(j))
            quit()
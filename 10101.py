a=[]
b=0
for i in range(3):
    a.append(int(input()))
for i in a:
    b=b+i
if b!=180:
    print("Error")
elif a[0]==a[1]:
    if a[1]==a[2]:
        print("Equilateral")
    else:
        print("Isosceles")
elif a[1]==a[2]:
    print("Isosceles")
elif a[0]==a[2]:
    print("Isosceles")
else:
    print("Scalene")
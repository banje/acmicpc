a=input()
d=0
for i in range(len(a)):
    b=ord(a[i])
    if b>90:
        c=b-96
    else:
        c=b-38
    d=d+c
if d==1:
    print("It is a prime word.")
else:
    e=int(d**0.5)
    for j in range(2, e+1):
        if not d%j:
            print("It is not a prime word.")
            break
    else:
        print("It is a prime word.")
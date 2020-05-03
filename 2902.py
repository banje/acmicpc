a=input()
b=""
for i in range(len(a)):
    if ord(a[i])<91:
        if ord(a[i])!=45:
            b=b+a[i]
print(b)
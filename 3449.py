a=int(input())
for i in range(a):
    b=input()
    c=input()
    d=len(b)
    e=0
    for j in range(d):
        if b[j]!=c[j]:
            e=e+1
    print("Hamming distance is {}.".format(e))
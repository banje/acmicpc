a=int(input())
for i in range(a):
    b=input()
    c=(ord(b[0])-65)*26*26+(ord(b[1])-65)*26+(ord(b[2])-65)
    d=int(b[4:8])
    e=abs(c-d)
    if e<=100:
        print("nice")
    else:
        print("not nice")
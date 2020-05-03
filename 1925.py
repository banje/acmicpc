a=input().split()
b=int(a[1])
a=int(a[0])
c=input().split()
d=int(c[1])
c=int(c[0])
e=input().split()
f=int(e[1])
e=int(e[0])
g=((c-a)**2+(d-b)**2)
h=((e-a)**2+(f-b)**2)
i=((e-c)**2+(f-d)**2)
j=[g,h,i]
j.sort()
g=j[0]
h=j[1]
i=j[2]
if i**0.5==(g**0.5+h**0.5):
    print("X")
elif (g==h)or(h==i):
    if (g==h)and(h==i):
        print("JungTriangle")
    elif i>g+h:
        print("Dunkak2Triangle")
    elif i==g+h:
        print("Jikkak2Triangle")
    else:
        print("Yeahkak2Triangle")
else:
    if i>g+h:
        print("DunkakTriangle")
    elif i==g+h:
        print("JikkakTriangle")
    else:
        print("YeahkakTriangle")
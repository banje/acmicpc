a=input()
c=0
for i in [1,2,3,4,5,7,8,0]:
    b=a.count(str(i))
    if b>c:
        c=b
d=(a.count("6")+a.count("9")+1)//2
if d>c:
    c=d
print(c)
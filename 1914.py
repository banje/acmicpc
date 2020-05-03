a=int(input())
print(2**a-1)
def d(a,b,c):
    if c>1:
        d(a,6-a-b,c-1)
        print("{} {}".format(a,b))
        d(6-a-b,b,c-1)
    else:
        print("{} {}".format(a,b))
if a<=20:
    d(1,3,a)

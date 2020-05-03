b = []
for i in range(2, 1000000):
    c = int(i**0.5)
    for j in range(2, c+1):
        if not i%j:
            break
    else:
        b.append(i)

while True:
    c=int(input())
    if c==0:
        break
    d=round(c/4+0.1)
    j=1
    while j<=d:
        if 2*j+1 in b and c-(2*j+1) in b:
            print("{} = {} + {}".format(c,2*j+1,c-(2*j+1)))
            break
        j=j+1
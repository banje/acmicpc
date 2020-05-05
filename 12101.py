[a,b]=list(map(int,input().split()))
c=[["1"],["1+1","2"],["1+1+1","1+2","2+1","3"]]
while a>len(c):
    d=[]
    for z in c[-1]:
        d.append("1+"+z)
    for z in c[-2]:
        d.append("2+"+z)
    for z in c[-3]:
        d.append("3+"+z)
    c.append(d)
if len(c[a-1])<b:
    print(-1)
else:
    print(c[a-1][b-1])
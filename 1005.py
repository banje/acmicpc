a=int(input())
for z in range(a):
    b,c=map(int,input().split())
    d=list(map(int,input().split()))
    k=[set()]
    e=[[]]
    for y in range(b):
        e.append([])
        k.append({y+1})
    for y in range(c):
        f,g=map(int,input().split())
        e[g].append(f)
    h=int(input())
    i=list(range(1,b+1))
    while True:
        j=[]
        y=0
        while True:
            if e[i[y]]==[]:
                j.append(i[y])
                i.remove(i[y])
            else:
                y=y+1
            if y==len(i):
                break
        if h in j:
            print(k[h-1])
            break
        for y in j:
            for x in i:
                if y in e[x]:
                    k[x]=k[x]|{y}
                    e[x].remove(y)

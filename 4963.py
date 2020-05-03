while True:
    a=list(map(int,input().split()))
    if a==[0,0]:
        break
    g=[]
    for i in range(a[0]+2):
        g.append(0)
    b=[]
    b.append(g)
    for i in range(a[1]):
        f=input().split()
        f.insert(0,0)
        f.append(0)
        b.append(f)
    b.append(g)
    c=0
    for i in range(1,a[0]+1):
        for j in range(1,a[1]+1):
            if b[j][i]=="1":
                c=c+1
                d=[[j,i]]
                b[j][i]=-1
                while True:
                    if d==[]:
                        break
                    e=d[0]
                    if b[e[0]-1][e[1]+1]=="1":
                        d.append([e[0]-1,e[1]+1])
                        b[e[0]-1][e[1]+1]=-1
                    if b[e[0]][e[1]+1]=="1":
                        d.append([e[0],e[1]+1])
                        b[e[0]][e[1] + 1] = -1
                    if b[e[0]+1][e[1]+1]=="1":
                        d.append([e[0]+1,e[1]+1])
                        b[e[0] + 1][e[1] + 1] = -1
                    if b[e[0]+1][e[1]]=="1":
                        d.append([e[0]+1,e[1]])
                        b[e[0] + 1][e[1]] = -1
                    if b[e[0] + 1][e[1] - 1] == "1":
                        d.append([e[0] + 1, e[1] - 1])
                        b[e[0] + 1][e[1] - 1] = -1
                    if b[e[0]][e[1] - 1] == "1":
                        d.append([e[0] , e[1] - 1])
                        b[e[0] ][e[1] - 1] = -1
                    if b[e[0] - 1][e[1] - 1] == "1":
                        d.append([e[0] - 1, e[1] - 1])
                        b[e[0] - 1][e[1] - 1] = -1
                    if b[e[0] - 1][e[1] ] == "1":
                        d.append([e[0] - 1, e[1] ])
                        b[e[0] - 1][e[1] ] = -1

                    d.remove(e)
    print(c)
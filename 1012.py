a=int(input())
for i in range(a):
    b=input().split()
    d=[]
    f=0
    for j in range(int(b[1])+2):
        c = [0] * (int(b[0]) + 2)
        d.append(c)
    for j in range(int(b[2])):
        e=input().split()
        d[int(e[1])+1][int(e[0])+1]=1
    for j in range(1,int(b[0])+1):
        for k in range(1,int(b[1])+1):
            if d[k][j]==1:
                f=f+1
                g=[[k,j]]
                d[k][j]=-1
                while True:
                    if g==[]:
                        break
                    h=g[0]
                    if d[h[0]+1][h[1]]==1:
                        d[h[0]+1][h[1]]=-1
                        g.append([h[0]+1,h[1]])
                    if d[h[0]][h[1]+1]==1:
                        d[h[0]][h[1]+1]=-1
                        g.append([h[0],h[1]+1])
                    if d[h[0] - 1][h[1]] == 1:
                        d[h[0] - 1][h[1]] = -1
                        g.append([h[0] - 1, h[1]])
                    if d[h[0]][h[1]-1]==1:
                        d[h[0]][h[1]-1]=-1
                        g.append([h[0],h[1]-1])
                    g.remove(h)
    print(f)
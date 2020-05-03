a=input().split()
b=[]
b.append([-1]*(int(a[0])+2))
for i in range(int(a[1])):
    b.append([-1]+list(map(int,input().split()))+[-1])
b.append([-1]*(int(a[0])+2))
c=0
for i in range(1,int(a[1])+1):
    for j in range(1,int(a[0])+1):
        if b[i][j]==1:
            e=[[i,j,1]]
            while True:
                if e==[]:
                    break
                f=e[0]
                if b[f[0]][f[1]]>0:
                    if (b[f[0]+1][f[1]]<-f[2]-1)or(b[f[0]+1][f[1]]==0):
                        b[f[0]+1][f[1]]=f[2]+1
                        e.append([f[0]+1,f[1],f[2]+1])
                    if (b[f[0]][f[1]+1]<f[2]-1)or(b[f[0]][f[1]+1]==0):
                        b[f[0]][f[1]+1]=f[2]+1
                        e.append([f[0],f[1]+1,f[2]+1])
                    if (b[f[0]-1][f[1]]<f[2]-1)or(b[f[0]-1][f[1]]==0):
                        b[f[0]-1][f[1]]=f[2]+1
                        e.append([f[0]-1,f[1],f[2]+1])
                    if (b[f[0]][f[1]-1]<f[2]-1)or(b[f[0]][f[1]-1]==0):
                        b[f[0]][f[1]-1]=f[2]+1
                        e.append([f[0],f[1]-1,f[2]+1])
                    b[f[0]][f[1]]=-b[f[0]][f[1]]
                e.remove(f)
for i in range(1,int(a[1])+1):
    for j in range(1,int(a[0])+1):
        if b[i][j]==0:
            print(-1)
            quit()
        if b[i][j]<c:
            c=b[i][j]
print(1-c)
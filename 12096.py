a=int(input())
for i in range(a):
    b, c = map(int, input().split())
    d=list(map(int,input().split()))
    e=[]
    for j in range(b):
        e.append([])
    for j in range(c):
        u, v =map(int, input().split())
        e[v-1].append(u-1)
    f = [-1]*b
    g = int(input())
    

        [[],[0],[0],[1,2]]
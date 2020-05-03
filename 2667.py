a=int(input())
b=[]
for i in range(a):
    b.append(list(input()))
d=2
e=[]
for i in range(a):
    for j in range(a):
        c=b[i][j]
        f=0
        if c=="1":
            b[i][j]=d
            f=f+1


def g(a, b, c, d,f):
    e = [(a + 1, b), (a, b + 1), (a - 1, b), (a, b - 1)]
    for i, j in e:
        if 0 <= i < d and 0 <= j < d:
            f[i][j] == '1':

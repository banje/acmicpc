while True:
    try:
        a=input().split()
        b=int(a[1])
        c=int(a[2])
        d=int(a[3])
        e=int(a[4])
        f=int(a[5])
        a=int(a[0])
    except EOFError:
        break
    try:
        g=input().split()
        h=int(g[1])
        i=int(g[2])
        g=int(g[0])
    except EOFError:
        break
    if max(c,f)>=i:
        print(-1)
    else:
        p=[]
        q=0
        r=0
        for j in [a,d]:
            for k in [b,e]:
                for l in [c,f]:
                    m=i/(i-l)
                    n=g-(g-j)*m
                    o=h-(h-k)*m
                    p.append([n,o])
                    q=q+n
                    r=r+o
        q=q/8
        r=r/8
        u=[]
        v=[]
        w=[]
        x=[]
        for j in range(8):
            s=p[j][0]
            t=p[j][1]
            if s>q:
                if t>r:
                    u.append([s,t])
                elif t<r:
                    v.append([s,t])
                else:
                    print(0)
                    break
            elif s<q:
                if t>r:
                    w.append([s,t])
                elif t<r:
                    x.append([s,t])
                else:
                    print(0)
                    break
            else:
                print(0)
                break
        else:
            if u[0][0]>u[1][0]:
                u=u[0]
            else:
                u=u[1]
            if v[0][0]>v[1][0]:
                v=v[0]
            else:
                v=v[1]
            if w[0][0]>w[1][0]:
                w=w[1]
            else:
                w=w[0]
            if x[0][0]>x[1][0]:
                x=x[1]
            else:
                x=x[0]
            y=((u[0]-x[0])**2+(u[1]-x[1])**2)**0.5
            z=((v[0]-w[0])**2+(v[1]-w[1])**2)**0.5
            print(y*z/2)

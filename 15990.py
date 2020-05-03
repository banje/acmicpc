a=int(input())
mod = 1000000009
v = [int(input()) for i in range(a)]
b = max(v)
f1=[1, 0, 1]
f2=[0, 1, 1]
f3=[0, 0, 1]
for i in range(b-3):
    c=(f2[-1]+f3[-1]) % mod
    d=(f1[-2]+f3[-2]) % mod
    e=(f1[-3]+f2[-3]) % mod
    f1.append(c)
    f2.append(d)
    f3.append(e)
for b in v:
    print((f1[b-1]+f2[b-1]+f3[b-1]) % mod)
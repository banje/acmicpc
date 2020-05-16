import heapq
import sys
a=int(input())
b=[sys.stdin.readline() for z in range(a)]
b=list(map(int,b))
c=[]
for z in range(a):
    if b[z]==0:
        if c==[]:
            print(0)
        else:
            d=heapq.heappop(c)
            if int(d+0.1)!=d:
                print(int(-d-0.1))
            else:
                print(d)
    else:
        if b[z]<0:
            heapq.heappush(c,-b[z]-0.1)
        else:
            heapq.heappush(c,b[z])
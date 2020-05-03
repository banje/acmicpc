import sys
T=int(sys.stdin.readline().rstrip())
for i in range(T):
    a,b=sys.stdin.readline().rstrip().split()
    print("{}".format(int(a)+int(b)))
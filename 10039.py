b=0
for i in range(5):
    a=int(input())
    if a>40:
        b=b+a
    else:
        b=b+40
print("{}".format(int(b/5)))
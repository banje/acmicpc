a, b = input().split()
if a==b:
    print(0)
    quit()
c = int(b) - int(a)
i = 1
while True:
    d = i ** 2
    e = i * (i + 1)
    if d >= c:
        print("{}".format(2 * i - 1))
        break
    elif e >= c:
        print("{}".format(2 * i))
        break
    i = i + 1
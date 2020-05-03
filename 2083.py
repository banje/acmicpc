while True:
    a=input().split()
    if a==["#","0","0"]:
        break
    if int(a[1])>17 or int(a[2])>=80:
        print("{} Senior".format(a[0]))
    else:
        print("{} Junior".format(a[0]))
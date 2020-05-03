a=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
b=input().split()
c=int(b[0])+2
if b[1]=="2":
    c=c+3
if b[1]=="3":
    c=c+3
if b[1]=="4":
    c=c+6
if b[1]=="5":
    c=c+1
if b[1]=="6":
    c=c+4
if b[1]=="7":
    c=c+6
if b[1]=="8":
    c=c+2
if b[1]=="9":
    c=c+5
if b[1]=="11":
    c=c+3
if b[1]=="12":
    c=c+5
print(a[c%7])
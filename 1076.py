a=input()
b=input()
c=input()

def f(a):
    if a=="black":
        d=0
    elif a=="brown":
        d=1
    elif a=="red":
        d=2
    elif a=="orange":
        d=3
    elif a=="yellow":
        d=4
    elif a=="green":
        d=5
    elif a=="blue":
        d=6
    elif a=="violet":
        d=7
    elif a=="grey":
        d=8
    elif a=="white":
        d=9
    return d

d=(f(a)*10+f(b))*(10**(f(c)))
print(d)
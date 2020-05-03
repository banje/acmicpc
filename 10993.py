#내가안함
triangle = ['*']
def next_triangle(triangle, n):
    if n%2:
        triangle = triangle[::-1]
    new = ['*'*(2**(n+1)-3)]
    temp = '*'+' '*(2**(n-1)-1)
    for i in range(2**(n-1)-1):
        temp = ' '+temp[:-1]
        new.append(temp+triangle[i]+' '*(2**n-4-2*i)+'*')
    for i in range(2**(n-1)-2):
        new.append(' ' * (i + 2 ** (n - 1)) + '*' + ' ' * (2 ** n - 5 - 2*i) + '*')
    new.append(' '*(2**n-2)+'*')
    if n%2:
        new = new[::-1]
    return new

for i in range(1, int(input())):
    triangle = next_triangle(triangle, i+1)

for line in triangle:
    print(line)
a = []
b = None

while b == None:
    c = input('Enter-->')
    if c == 'done':
        break
    a.append(c)

d = a[:]
a[0] = 'd'
print(a, d)
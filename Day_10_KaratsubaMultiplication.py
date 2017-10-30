from itertools import izip_longest

def add(x, y):
    z, carry = [], 0
    for r, s in izip_longest(x, y, fillvalue=0):
        t = r + s + carry
        carry = t // 10
        z.append(t % 10)
    if carry:
        z.append(carry)
    return z

def sub(x, y):
    z, carry= [], 0
    for r, s in izip_longest(x, y, fillvalue=0):
        t = r - s + carry
        carry = t // 10
        z.append(t % 10)
    return z

def karatsuba(x, y):
    while len(x) < len(y):
        x.append(0)
    while len(y) < len(x):
        y.append(0)
    
    n = len(x)
    n_2 = (n + 1) >> 1
    
    if n == 1:
        return add([x[0] * y[0]], [])
    
    x0, x1 = x[:n_2], x[n_2:]
    y0, y1 = y[:n_2], y[n_2:]
    
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1, y1)
    z2 = karatsuba(add(x0, x1), add(y0, y1))
    z2 = sub(sub(z2, z0), z1)
    
    z = add(z0, [0] * (n_2 << 1) + z1)
    z = add(z, [0] * n_2 + z2)
    
    return z



x, y = '994759257', '928607936'
x = list(map(int, reversed(x)))
y = list(map(int, reversed(y)))
z = karatsuba(x, y)
print ''.join(map(str, reversed(z)))
    
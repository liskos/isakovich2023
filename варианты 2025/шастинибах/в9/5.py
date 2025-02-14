def v(a):
    c = []
    while a > 0:
        c.append(str(a % 8))
        a = a // 8
    return c

def f(n):
    b = v(n)
    if n % 2 == 0:
        for i in range(len(b)):
            if int(b[i]) % 3 == 0:
                b[i] = '2'
            else:
                b[0] = '3'
                b[-1] = '3'
    return int(''.join(b)[::-1], 8)
d = []
for i in range(1, 1000):
    if f(i) < 300:
        d.append(f(i))
print(max(d))
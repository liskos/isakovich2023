def tr(n):
    a = []
    while n > 0:
        a.append(str(n % 3))
        n = n // 3
    return ''.join(a)[::-1]


def f(n):
    b = tr(n)
    b = b.replace('2', '+')
    b = b.replace('0', '2')
    b = b.replace('+', '0')
    while b[0] == '0' and len(b) > 1:
        b = b[1:]
    return abs(n - int(b, 3))

for i in range(1, 100000):
    if f(i) == 378:
        print(i)
        break
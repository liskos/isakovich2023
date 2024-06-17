def tr(n):
    s = ''
    t = '012'
    while n > 0:
        s = t[n % 3] + s
        n = n // 4
    return s


def f(n):
    b = tr(n)
    if n % 3 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = b + tr(n % 3 * 5)
    return int(b, 3)

a = []
for i in range(4, 10000):
    if f(i) > 133:
        a.append(f(i))
print(min(a))
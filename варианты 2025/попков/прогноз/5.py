def tr(n):
    a = []
    while n > 0:
        a.append(str(n % 3))
        n = n // 3
    return ''.join(a)[::-1]


def f(n):
    b = tr(n)
    if n % 3 == 0:
        b = b + b[:3]
    else:
        b = b + tr(sum([int(x) for x in b]) * 5)
    return int(b, 3)
a = []

for i in range(1, 1000):
    if f(i) > 2500 and f(i) % 2 > 0:
        a.append(f(i))
print(min(a))

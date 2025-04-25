def tr(n):
    a = []
    while n > 0:
        a.append(str(n % 3))
        n = n // 3
    return ''.join(a)[::-1]


def f(n):
    b = tr(n)
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + tr(n % 3 * 3)
    return int(b , 3)
a = []
for i in range(1, 1000):
    if f(i) <= 150:
        a.append(i)
print(max(a))
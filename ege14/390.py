def f(n):
    a = []
    while n > 0:
        a.append(n % 12)
        n = n // 12
    return sum(a)

for x in range(16):
    r = (int('57a09', 16) + (x * 16 ** 1)) * (int('540', 8) + (x * 8 ** 0))
    if f(r) == 40:
        print(r, x)

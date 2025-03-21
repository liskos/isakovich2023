def f(n):
    a = []
    while n > 0:
        a.append(n % 5)
        n = n // 5
    return a

for x in range(26):
    r = int('40b5', 26) + (x * 26 ** 2) + int('203', x + 1) + (x * (x + 1) ** 1)
    if sum(f(r)) == 19:
        print(f(r).count(4), x)

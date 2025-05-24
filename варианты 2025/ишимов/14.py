def f(n):
    a = []
    while n > 0:
        a.append(str(n % 25))
        n = n // 25
    return ''.join(a)[::-1]

for x in range(1, 25):
    r = 25 ** 150 + 25 ** 100 - x
    print(x, f(r).count('0'))
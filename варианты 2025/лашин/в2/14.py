def f(n):
    a = []
    while n> 0:
        a.append(n % 98)
        n = n // 98
    return a

for x in range(1, 5001):
    r = 14 ** 230 + 14 ** 30 - x
    if f(r).count(2) == 1:
        print(x)
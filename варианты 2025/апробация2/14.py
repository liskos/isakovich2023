def f(n):
    a = []
    while n > 0:
        a.append(n % 3)
        n = n // 3
    return a


for x in reversed(range(1, 2031)):
    r = 3 ** 100 - x
    if f(r).count(0) == 1:
        print(x)
        break
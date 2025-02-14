def f(a):
    c = []
    while a > 0:
        c.append(a%7)
        a = a // 7
    return c

d = []
for x in range(1, 10001):
    r = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    print(f(r).count(0), x)

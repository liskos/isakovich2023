def fac(a):
    c = 1
    for i in range(2, a + 1):
        c *= i
    return c


def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 4, b) + f(a + fac(a), b)


print(f(1, 10) * f(10, 20))

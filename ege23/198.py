def f(a, b, c, d):
    if a > b:
        return 0
    if a == b:
        return c > d
    return f(a + 1, b, c, d + 1) + f(a * 2, b, c + 1, d) + f(a * 3, b, c + 1, d)

print(f(1, 157, 0, 0))
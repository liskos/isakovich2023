def f(a, b, c, d):
    if a > b:
        return 0
    if a == b:
        return c > d
    return f(a + 1, b, c, d + 1) + f(a * 2, b, c + 1, d) + f(a * 5, b, c + 1, d)

print(f(3, 260, 0, 0))
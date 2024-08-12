def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return c % 2 == 1
    if a > 1:
        return f(a + 2, b, c + 1) + f(a * 2, b, c + 1) + f(a ** 2, b, c + 1)
    else:
        return f(a + 2, b, c + 1) + f(a * 2, b, c + 1)

print(f(1, 100, 0))
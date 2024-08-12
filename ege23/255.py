def f(a, b, c):
    if a > b or a == 10 or a == 38:
        return 0
    if a == b:
        return c <= 3
    return f(a + 1, b, c + 1) + f(a + 2, b, c) + f(a * 3, b, c)

print(f(1, 25, 0) * f(25, 43, 0))
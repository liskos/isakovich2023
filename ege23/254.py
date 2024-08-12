def f(a, b, c):
    if a > b or a == 11 or a == 35:
        return 0
    if a == b:
        return c <= 5
    return f(a + 1, b, c + 1) + f(a + 3, b, c) + f(a * 2, b, c)

print(f(2, 18, 0) * f(18, 40, 0))
def f(a, b, c):
    if a == b:
        return 1
    if a > b or a == 40:
        return 0
    if c == 1:
        return f(a + 1, b, 0) + f(a ** 2, b, 0)
    else:
        return f(a + 1, b, 0) + f(a * 2, b, 1) + f(a ** 2, b, 0)

print(f(5, 80, 0) * f(80, 155, 0))
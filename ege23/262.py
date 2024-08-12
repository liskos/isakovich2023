def f(a, b, c):
    if c > 7:
        return 0
    if a == b and c == 7:
        return 1
    if a >= 6:
        return f(a - 5, b, c + 1) + f(a + 2, b, c + 1) + f(a ** 2, b, c + 1)
    else:
        return f(a + 2, b, c + 1) + f(a ** 2, b, c + 1)

print(f(3, 28, 0))